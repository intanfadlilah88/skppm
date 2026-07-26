from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from kpm_app.views import ( 
    KegiatanViewSet, 
    KategoriViewSet, 
    UserViewSet, 
    RegisterView, 
    MyTokenObtainPairView,
    ManageUsersView, 
    AdminDashboardView,
    UserAssigningView,
    AssignDPAView,
    ListBimbinganView,
    DeleteAssignmentView,
    MahasiswaViewSet,
    DosenViewSet,
    UserProfileView,# <-- TAMBAHAN 1: Import View untuk Profile. Pastikan namanya sesuai dengan yang ada di views.py Anda.
    DownloadBerkasView,
    AjukanUlangKegiatanView, 
    KemahasiswaanDashboardView, 
    KemahasiswaanKegiatanView,
    PlottingListView
)

# 1. Inisialisasi Router untuk ViewSet (CRUD otomatis)
router = DefaultRouter()
router.register(r'kategori', KategoriViewSet, basename='kategori')
router.register(r'kegiatan', KegiatanViewSet, basename='kegiatan')
router.register(r'users', UserViewSet, basename='user')
router.register(r'mahasiswa', MahasiswaViewSet, basename='mahasiswa')
router.register(r'dosen', DosenViewSet, basename='dosen')

# 2. Daftar URL Patterns
urlpatterns = [
    path('admin/', admin.site.urls),

    # --- ENDPOINT MANUAL (APIView) ---
    # Dashboard & Manajemen User
    path('api/superadmin-dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('api/manage-users-list/', ManageUsersView.as_view(), name='manage_users'),
    
    # Plotting Mahasiswa ke DPA
    path('api/users-list-for-assigning/', UserAssigningView.as_view(), name='users_assigning'),
    path('api/assign-dpa/', AssignDPAView.as_view(), name='assign_dpa'),
    path('api/list-bimbingan/', ListBimbinganView.as_view(), name='list-bimbingan'),
    path('api/assign-dpa/<str:pk>/', DeleteAssignmentView.as_view(), name='delete-assign'),

    # --- TAMBAHAN BARU UNTUK PLOTTING LIST ---
    # Endpoint untuk mengambil daftar mahasiswa yang sudah memiliki DPA
    path('api/plotting-list/', PlottingListView.as_view(), name='plotting-list'),
    
    # --- TAMBAHAN BARU UNTUK PROFIL ---
    # Menambahkan rute spesifik yang dicari oleh Vue (Axios)
    path('api/user/profile/', UserProfileView.as_view(), name='user-profile'),

    # --- AUTH & TOKEN ---
    path('api/register/', RegisterView.as_view(), name='auth_register'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/kemahasiswaan/dashboard/', KemahasiswaanDashboardView.as_view(), name='kemahasiswaan-dashboard'),
    path('api/kemahasiswaan/kegiatan/', KemahasiswaanKegiatanView.as_view(), name='kemahasiswaan-kegiatan'),
    path('api/download-berkas/<str:pk>/', DownloadBerkasView.as_view(), name='download-berkas'),
    # --- ROUTER AUTOMATIC ---
    # Rute otomatis untuk CRUD (kategori, kegiatan, users, mahasiswa, dosen)
    path('api/', include(router.urls)),

    path('api/kegiatan/<str:pk>/ajukan-ulang/', KegiatanViewSet.as_view({'patch': 'ajukan_ulang'}), name='kegiatan-ajukan-ulang'),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)