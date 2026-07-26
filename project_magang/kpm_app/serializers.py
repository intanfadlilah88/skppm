from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User, KategoriKegiatan, Kegiatan

# ==============================
# TOKEN CUSTOMIZER
# ==============================
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Menambahkan data ke dalam payload token untuk mempermudah Vue
        token['username'] = user.username
        token['role'] = user.role
        token['full_name'] = user.full_name or user.username
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        # Mengembalikan data user saat login agar Vue bisa langsung simpan di LocalStorage
        data['user'] = {
            'id': self.user.id,
            'username': self.user.username,
            'full_name': self.user.full_name,
            'role': self.user.role,
        }
        return data

# ==============================
# SERIALIZER USER (DIPERBAIKI)
# ==============================
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    dpa_pembimbing_nama = serializers.ReadOnlyField(source='dpa_pembimbing.full_name')
    
    class Meta:
        model = User
        # Field lengkap sesuai model yang baru diperbaiki
        fields = [
            'id', 'username', 'password', 'role', 'nim_nip', 
            'full_name', 'jenis_kelamin', 'prodi', 'email', 'no_telp', 'angkatan', 
            'nidn', 'jabatan', 'dpa_pembimbing', 'dpa_pembimbing_nama'
        ]
        # NIM, Role, dan Username jangan sampai bisa diubah oleh Mahasiswa lewat PATCH
        read_only_fields = ['username', 'nim_nip', 'role']

    def to_representation(self, instance):
        """Menyesuaikan output JSON berdasarkan role user"""
        data = super().to_representation(instance)
        
        # Logika tampilan profil Mahasiswa
        if instance.role == 'mahasiswa':
            data.pop('nidn', None)
            data.pop('jabatan', None)
        
        # Logika tampilan profil DPA,akademik,kemahasiswaan
        elif instance.role in ['dpa', 'akademik', 'kemahasiswaan']:
            data.pop('angkatan', None)
            # Menjamin nim_nip bisa dibaca sebagai NIDN di frontend jika diperlukan
            data['nidn'] = instance.nidn
            
        return data

    def validate_nim_nip(self, value):
        user_id = self.instance.id if self.instance else None
        if User.objects.filter(nim_nip=value).exclude(id=user_id).exists():
            raise serializers.ValidationError("NIM/NIP sudah terdaftar oleh pengguna lain")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        if not validated_data.get('username'):
            validated_data['username'] = validated_data.get('nim_nip')

        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        
        # Update field lainnya secara dinamis (Termasuk no_telp, angkatan, dll)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
            
        if password:
            instance.set_password(password)
            
        instance.save()
        return instance

# ==========================================================
# SERIALIZER KHUSUS MAHASISWA (Untuk Total Poin & DPA)
# ==========================================================
class MahasiswaDetailSerializer(UserSerializer):
    """
    Serializer ini mewarisi UserSerializer namun ditambahkan 
    fitur total_poin untuk digunakan di Dashboard Akademik.
    """
    total_poin = serializers.IntegerField(read_only=True)
    dpa_pembimbing_detail = serializers.SerializerMethodField()

    class Meta(UserSerializer.Meta):
        # Menggabungkan field bawaan UserSerializer dengan field baru
        fields = UserSerializer.Meta.fields + ['total_poin', 'dpa_pembimbing_detail']

    def get_dpa_pembimbing_detail(self, obj):
        if obj.dpa_pembimbing:
            return {
                "id": obj.dpa_pembimbing.id,
                "full_name": obj.dpa_pembimbing.full_name or obj.dpa_pembimbing.username
            }
        return None

# ==============================
# SERIALIZER KATEGORI KEGIATAN
# ==============================
class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = KategoriKegiatan
        fields = ['id', 'bidang', 'nama_kegiatan', 'partisipasi', 'level', 'sifat', 'bobot_poin']

# ==============================
# SERIALIZER KEGIATAN
# ==============================
class KegiatanSerializer(serializers.ModelSerializer):
    mahasiswa_nama = serializers.SerializerMethodField()
    nim = serializers.ReadOnlyField(source='mahasiswa.nim_nip')
    nama_kategori = serializers.ReadOnlyField(source='kategori.nama_kegiatan')
    bobot_poin_kategori = serializers.ReadOnlyField(source='kategori.bobot_poin')
    dpa_nama = serializers.SerializerMethodField()
    nip = serializers.ReadOnlyField(source='dpa.nim_nip')
    durasi_kegiatan = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    tanggal_kegiatan = serializers.DateField(required=False, allow_null=True)
    
    # TAMBAHKAN field baru ini (jika belum ada di model, lihat catatan di bawah)
    informasi_kegiatan = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    catatan = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    class Meta:
        model = Kegiatan
        fields = [
            'id', 'mahasiswa', 'mahasiswa_nama', 'nim', 
            'judul_kegiatan', 'kategori', 'nama_kategori', 
            'bobot_poin_kategori', 'dpa', 'dpa_nama', 'nip', 
            'tanggal_kegiatan', 'durasi_kegiatan',
            'bukti_sertifikat', 'komentar_dpa', 'status', 
            'poin_valid', 'created_at',
            # TAMBAHKAN field di bawah ini:
            'informasi_kegiatan',  # Link informasi kegiatan dari mahasiswa
            'catatan'              # Catatan tambahan dari mahasiswa
           
        ]
        read_only_fields = ['mahasiswa', 'dpa', 'poin_valid', 'created_at']

    def get_mahasiswa_nama(self, obj):
        if obj.mahasiswa:
            return obj.mahasiswa.full_name or obj.mahasiswa.username
        return "Data Mahasiswa"

    def get_dpa_nama(self, obj):
        dpa = obj.dpa or (obj.mahasiswa.dpa_pembimbing if obj.mahasiswa else None)
        if dpa:
            return dpa.full_name or dpa.username
        return "BELUM DI-PLOT"

    def validate_bukti_sertifikat(self, value):
        if value and hasattr(value, 'size'):
            if value.size > 2 * 1024 * 1024:
                raise serializers.ValidationError("Ukuran file maksimal adalah 2MB")
            ext = value.name.split('.')[-1].lower()
            if ext not in ['pdf', 'jpg', 'jpeg', 'png']:
                raise serializers.ValidationError("Format file harus berupa PDF, JPG, atau PNG")
        return value