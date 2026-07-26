from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Kegiatan, KategoriKegiatan
from .serializers import KegiatanSerializer, KategoriSerializer, UserSerializer, MyTokenObtainPairSerializer, MahasiswaDetailSerializer  
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsStaffOrDosenOrOwner  # Import permission yang sudah diperbaiki

User = get_user_model()

# --- 1. DASHBOARD VIEW ---
class AdminDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Validasi Role
        if request.user.role not in ['superadmin', 'akademik', 'kemahasiswaan']:
            return Response({"detail": "Akses ditolak"}, status=status.HTTP_403_FORBIDDEN)

        stats = {
            'total_mahasiswa': User.objects.filter(role='mahasiswa').count(),
            'total_pending': Kegiatan.objects.filter(status='pending').count(),
            'total_valid': Kegiatan.objects.filter(status__in=['valid', 'approved_final']).count(), 
            'total_tolak': Kegiatan.objects.filter(status='rejected').count(),
        }
        
        # Ambil log kegiatan terbaru
        logs = Kegiatan.objects.select_related('mahasiswa', 'mahasiswa__dpa_pembimbing').order_by('-created_at')[:10]
        recent_logs = []
        for log in logs:
            recent_logs.append({
                'id': log.id,
                'mahasiswa_nama': getattr(log.mahasiswa, 'full_name', log.mahasiswa.username),
                'nim': getattr(log.mahasiswa, 'nim_nip', '-'),
                'dpa_nama': getattr(log.mahasiswa.dpa_pembimbing, 'full_name', 'BELUM DI-PLOT') if log.mahasiswa.dpa_pembimbing else 'BELUM DI-PLOT',
                'judul_kegiatan': log.judul_kegiatan,
                'status': log.status,
                'poin': log.poin_valid if hasattr(log, 'poin_valid') else 0,
                'created_at': log.created_at
            })

        return Response({'stats': stats, 'recent_logs': recent_logs})

# --- FITUR BARU: DOWNLOAD BERKAS (Khusus Kemahasiswaan/Admin) ---
class DownloadBerkasView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        # Hanya role tertentu yang bisa download berkas mahasiswa secara bebas
        if request.user.role not in ['kemahasiswaan', 'superadmin', 'akademik']:
            return Response({"detail": "Anda tidak memiliki akses untuk mengunduh berkas ini."}, 
                            status=status.HTTP_403_FORBIDDEN)
        
        kegiatan = get_object_or_404(Kegiatan, pk=pk)
        
        if kegiatan.bukti_sertifikat:
            file_path = kegiatan.bukti_sertifikat.path
            if os.path.exists(file_path):
                # Mengirim file sebagai attachment
                return FileResponse(open(file_path, 'rb'), as_attachment=True)
        
        return Response({"error": "File tidak ditemukan di server."}, status=status.HTTP_404_NOT_FOUND)

# --- 2. MANAGE USERS VIEW ---
class ManageUsersView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        users = User.objects.all().order_by('-id')
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

# --- 3. USER ASSIGNING VIEW (Untuk Dropdown di Vue) ---
class UserAssigningView(APIView):
    permission_classes = [IsAuthenticated] 

    def get(self, request):
        # Mahasiswa yang belum punya DPA
        unassigned_mhs = User.objects.filter(role='mahasiswa', dpa_pembimbing__isnull=True)
        # Daftar Dosen/DPA (PERBAIKAN: Menghapus 'akademik' agar hanya role 'dpa' yang muncul)
        dosen_list = User.objects.filter(role='dpa')

        return Response({
            'unassigned_mhs': UserSerializer(unassigned_mhs, many=True).data,
            'dpa_list': UserSerializer(dosen_list, many=True).data
        })

# --- 4. ASSIGN DPA ACTION ---
class AssignDPAView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        mhs_id = request.data.get('mahasiswa_id')
        dpa_id = request.data.get('dpa_id')
        try:
            mahasiswa = User.objects.get(id=mhs_id)
            dpa = User.objects.get(id=dpa_id)
            mahasiswa.dpa_pembimbing = dpa
            mahasiswa.save()
            return Response({"message": "Berhasil menghubungkan mahasiswa ke DPA"})
        except User.DoesNotExist:
            return Response({"error": "User tidak ditemukan"}, status=404)

# --- 5. AUTH & REGISTRATION ---
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # Tangkap data dari Vue
            nim_nip_input = request.data.get('nim_nip')
            role_input = request.data.get('role', 'mahasiswa')
            
            # Paksa simpan field yang diset read_only (username, nim_nip, role)
            serializer.save(
                username=nim_nip_input,
                nim_nip=nim_nip_input,
                role=role_input
            )
            return Response({"message": "Registrasi Berhasil"}, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- 6. VIEWSETS (Penting: Untuk Router di urls.py) ---
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get', 'patch'], permission_classes=[IsAuthenticated])
    def me(self, request):
        user = request.user
        
        if request.method == 'GET':
            serializer = UserSerializer(user)
            return Response(serializer.data)
        
        elif request.method == 'PATCH':
            # partial=True memungkinkan update hanya pada field yang dikirim saja
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KategoriViewSet(viewsets.ModelViewSet):
    queryset = KategoriKegiatan.objects.all()
    serializer_class = KategoriSerializer
    permission_classes = [AllowAny]

# --- 7. KEGIATAN VIEWSET - DIPERBAIKI ---
# views.py - Bagian KegiatanViewSet

class KegiatanViewSet(viewsets.ModelViewSet):
    serializer_class = KegiatanSerializer
    permission_classes = [IsAuthenticated, IsStaffOrDosenOrOwner]

    def get_queryset(self):
        user = self.request.user
        user_role = getattr(user, 'role', '')
        
        # Admin & Akademik melihat semua
        if user.is_staff or user_role in ['superadmin', 'akademik']:
            return Kegiatan.objects.all().order_by('-id')
        
        # DPA melihat mahasiswa bimbingannya
        if user_role in ['dosen', 'dpa', 'dosen_pembimbing']:
            return Kegiatan.objects.filter(mahasiswa__dpa_pembimbing=user).order_by('-id')
        
        # Mahasiswa melihat miliknya sendiri
        return Kegiatan.objects.filter(mahasiswa=user).order_by('-id')

    def perform_create(self, serializer):
        serializer.save(mahasiswa=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        user_role = getattr(user, 'role', '')
        
        # ADMIN, AKADEMIK, DPA - AKSES PENUH
        if user.is_staff or user_role in ['superadmin', 'akademik', 'dosen', 'dpa', 'dosen_pembimbing']:
            # DPA melakukan validasi - LANGSUNG SAVE
            return super().update(request, *args, **kwargs)
        
        # MAHASISWA - hanya bisa update jika status 'rejected'
        if user_role == 'mahasiswa':
            if instance.status != 'rejected':
                return Response(
                    {"detail": "Data sudah diproses, tidak bisa diubah. Hanya data yang ditolak yang dapat diedit."}, 
                    status=status.HTTP_403_FORBIDDEN
                )
            
            # Reset data saat mahasiswa mengajukan ulang
            data = request.data.copy()
            if 'komentar_dpa' not in data:
                data['komentar_dpa'] = ''
            if 'status' not in data:
                data['status'] = 'pending'
            data['is_edited_by_dpa'] = False
            
            serializer = self.get_serializer(instance, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        
        return Response(
            {"detail": f"Anda tidak memiliki izin. Role Anda: {user_role}"}, 
            status=status.HTTP_403_FORBIDDEN
        )

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

# --- 8. DAFTAR BIMBINGAN ---
class ListBimbinganView(APIView):
    def get(self, request):
        queryset = User.objects.filter(role='mahasiswa').exclude(dpa_pembimbing__isnull=True).select_related('dpa_pembimbing')
        
        data = []
        for mhs in queryset:
            data.append({
                "id": mhs.id,
                "mahasiswa_nama": mhs.full_name or mhs.username,
                "nim": mhs.nim_nip,
                "dpa_nama": mhs.dpa_pembimbing.full_name if mhs.dpa_pembimbing else "-",
                "dpa_nip": mhs.dpa_pembimbing.nim_nip if mhs.dpa_pembimbing else "-"
            })
        return Response(data)

# --- 9. HAPUS HUBUNGAN BIMBINGAN ---
class DeleteAssignmentView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            mahasiswa = User.objects.get(pk=pk, role='mahasiswa')
            mahasiswa.dpa_pembimbing = None
            mahasiswa.save()
            return Response({"message": "Hubungan bimbingan berhasil dihapus"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "Mahasiswa tidak ditemukan"}, status=status.HTTP_404_NOT_FOUND)

# =========================================================================
# --- 10. VIEWSET UNTUK KEBUTUHAN DASHBOARD AKADEMIK (MHS & DOSEN) ---
# =========================================================================

class MahasiswaViewSet(viewsets.ModelViewSet):
    """ ViewSet khusus untuk mengambil dan mengedit data mahasiswa (termasuk plot DPA) """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Hanya mengembalikan user yang memiliki role 'mahasiswa'
        return User.objects.filter(role='mahasiswa').order_by('-id')

    def partial_update(self, request, *args, **kwargs):
        # Memastikan metode PATCH dari Vue (untuk plotting DPA) berjalan lancar
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

class DosenViewSet(viewsets.ModelViewSet):
    """ ViewSet khusus untuk mengambil daftar dosen/DPA di dropdown """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # PERBAIKAN: Hanya mengembalikan user dengan role 'dpa' 
        # (Menghapus 'akademik' agar tidak masuk di pilihan)
        return User.objects.filter(role='dpa').order_by('-id')

# =========================================================================
# --- 11. ENDPOINT PROFIL USER (UNTUK FIX ERROR 404 AXIOS) ---
# =========================================================================

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def patch(self, request):
        user = request.user
        
        serializer = UserSerializer(user, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Profil berhasil diperbarui!",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# =========================================================================
# --- 12. ENDPOINT UNTUK MAHASISWA MENGAJUKAN ULANG (TAMBAHAN) ---
# =========================================================================

class AjukanUlangKegiatanView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        try:
            kegiatan = Kegiatan.objects.get(pk=pk)
            user = request.user
            
            # Validasi kepemilikan
            if user.role == 'mahasiswa' and kegiatan.mahasiswa != user:
                return Response(
                    {"error": "Anda tidak memiliki izin"},
                    status=status.HTTP_403_FORBIDDEN
                )
            
            # Validasi status
            if kegiatan.status != 'rejected':
                return Response(
                    {"error": "Hanya pengajuan yang ditolak yang bisa diajukan ulang"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Update data
            serializer = KegiatanSerializer(kegiatan, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(status='pending', komentar_dpa='', is_edited_by_dpa=False)
                return Response({
                    "message": "Pengajuan berhasil diajukan ulang",
                    "data": serializer.data
                })
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except Kegiatan.DoesNotExist:
            return Response({"error": "Data tidak ditemukan"}, status=status.HTTP_404_NOT_FOUND)
        

        # views.py - Tambahkan class ini

class KemahasiswaanDashboardView(APIView):
    """Endpoint khusus untuk dashboard kemahasiswaan"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Validasi Role
        if request.user.role != 'kemahasiswaan':
            return Response({"detail": "Akses ditolak"}, status=status.HTTP_403_FORBIDDEN)

        # Statistik
        stats = {
            'total_mahasiswa': User.objects.filter(role='mahasiswa').count(),
            'total_pending': Kegiatan.objects.filter(status='pending').count(),
            'total_valid': Kegiatan.objects.filter(status='approved_final').count(),
            'total_tolak': Kegiatan.objects.filter(status='rejected').count(),
        }
        
        return Response({'stats': stats})

class KemahasiswaanKegiatanView(APIView):
    """Endpoint khusus untuk mengambil data kegiatan untuk kemahasiswaan"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Validasi Role
        if request.user.role != 'kemahasiswaan':
            return Response({"detail": "Akses ditolak"}, status=status.HTTP_403_FORBIDDEN)
        
        # Ambil semua kegiatan dengan data mahasiswa lengkap
        kegiatan = Kegiatan.objects.select_related('mahasiswa', 'kategori').all().order_by('-created_at')
        
        data = []
        for k in kegiatan:
            data.append({
                'id': k.id,
                'nim': k.mahasiswa.nim_nip if k.mahasiswa else '-',
                'mahasiswa_nama': k.mahasiswa.full_name if k.mahasiswa else '-',
                'prodi': k.mahasiswa.prodi if k.mahasiswa else '-',
                'email': k.mahasiswa.email if k.mahasiswa else '-',
                'no_telp': k.mahasiswa.no_telp if k.mahasiswa else '-',
                'judul_kegiatan': k.judul_kegiatan,
                'status': k.status,
                'bukti_sertifikat': k.bukti_sertifikat.url if k.bukti_sertifikat else None,
                'tanggal_pelaksanaan': k.tanggal_kegiatan,
                'durasi': k.durasi_kegiatan,
                'catatan': k.catatan or '-',
                'created_at': k.created_at,
                'bobot_poin_kategori': k.kategori.bobot_poin if k.kategori else 0,
                'bobot_poin': k.kategori.bobot_poin if k.kategori else 0,  # alias
                'poin_valid': k.poin_valid if hasattr(k, 'poin_valid') else 0,
            })
        
        return Response(data)
# =========================================================================
# --- 13. PLOTTING LIST VIEW (TAMBAHAN BARU UNTUK MENAMPILKAN DAFTAR PLOTTING) ---
# =========================================================================

class PlottingListView(APIView):
    """Endpoint untuk mengambil daftar mahasiswa yang sudah memiliki DPA"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Ambil semua mahasiswa yang sudah punya DPA
        mahasiswa_with_dpa = User.objects.filter(
            role='mahasiswa',
            dpa_pembimbing__isnull=False
        ).select_related('dpa_pembimbing').order_by('-id')
        
        data = []
        for mhs in mahasiswa_with_dpa:
            data.append({
                "id": mhs.id,
                "full_name": mhs.full_name or mhs.username,
                "username": mhs.username,
                "nim_nip": mhs.nim_nip,
                "prodi": mhs.prodi,
                "dpa_name": mhs.dpa_pembimbing.full_name or mhs.dpa_pembimbing.username,
                "dpa_id": mhs.dpa_pembimbing.id,
                "dpa_nip": mhs.dpa_pembimbing.nim_nip
            })
        return Response(data)

    