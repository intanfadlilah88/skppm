import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# 1. MODEL USER (Sudah mendukung Plotting DPA & Multi-Role)
class User(AbstractUser):
    ROLE_CHOICES = (
        ('mahasiswa', 'Mahasiswa'),
        ('dpa', 'DPA'),
        ('akademik', 'Akademik'),
        ('kemahasiswaan', 'Kemahasiswaan'),
        ('superadmin', 'Admin'),
    )

    JENIS_KELAMIN_CHOICES = [
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='mahasiswa')
    nim_nip = models.CharField(max_length=20, unique=True, help_text="Isi dengan NIM atau NIP")
    full_name = models.CharField(max_length=255, blank=True, null=True)
    jenis_kelamin = models.CharField(max_length=1, choices=JENIS_KELAMIN_CHOICES, null=True, blank=True)
    # --- Tambahan Field Baru ---
    no_telp = models.CharField(max_length=15, blank=True, null=True)
    angkatan = models.CharField(max_length=4, blank=True, null=True) # Untuk Mahasiswa
    nidn = models.CharField(max_length=20, blank=True, null=True)    # Untuk DPA
    jabatan = models.CharField(max_length=100, blank=True, null=True) # Untuk DPA/Akademik
    # ---------------------------

    dpa_pembimbing = models.ForeignKey(
        'self', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='anak_bimbingan',
        limit_choices_to={'role': 'dpa'}
    )
    
    prodi = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return f"{self.nim_nip} - {self.full_name or self.username}"

# 2. MODEL KATEGORI (Tetap sama)
class KategoriKegiatan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bidang = models.CharField(max_length=255)
    nama_kegiatan = models.CharField(max_length=255)
    partisipasi = models.CharField(max_length=255, null=True, blank=True)
    level = models.CharField(max_length=100)
    sifat = models.CharField(max_length=50, default='Pilihan')
    bobot_poin = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Kategori Kegiatan"

    def __str__(self):
        return f"{self.nama_kegiatan} ({self.bobot_poin} Poin)"

# 3. MODEL KEGIATAN (Otomatisasi Tetap Jalan)
class Kegiatan(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved_dpa', 'Disetujui DPA'),
        ('approved_final', 'Approved Final'),
        ('revisi', 'Revisi'),
        ('rejected', 'Rejected'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mahasiswa = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pengajuan_saya')
    dpa = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='verifikasi_dpa')
    judul_kegiatan = models.CharField(max_length=255)
    kategori = models.ForeignKey(KategoriKegiatan, on_delete=models.PROTECT)
    tanggal_kegiatan = models.DateField(null=True, blank=True) 
    durasi_kegiatan = models.CharField(max_length=100, null=True, blank=True) # Misal: "2 Hari" atau "20 Jam"
    bukti_sertifikat = models.FileField(upload_to='sertifikat/%Y/%m/', null=True, blank=True)
    informasi_kegiatan = models.CharField(max_length=500, blank=True, null=True)
    # Field untuk catatan tambahan mahasiswa (dari PengajuanView)
    catatan = models.TextField(blank=True, null=True) 
    komentar_dpa = models.TextField(blank=True, null=True)
    poin_valid = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Data Kegiatan"

    def save(self, *args, **kwargs):
        if not self.id and not self.dpa:
            if self.mahasiswa.dpa_pembimbing:
                self.dpa = self.mahasiswa.dpa_pembimbing
        
        if self.status == 'approved_final':
            self.poin_valid = self.kategori.bobot_poin
        else:
            self.poin_valid = 0
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.judul_kegiatan} - {self.mahasiswa.full_name}"