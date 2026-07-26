from rest_framework import permissions

class IsStaffOrDosenOrOwner(permissions.BasePermission):
    """
    Logika Bisnis Lengkap:
    1. Super Admin & Akademik (is_staff): Akses penuh ke semua data
    2. Dosen (DPA): Akses penuh untuk validasi (Approve/Reject/Edit)
    3. Mahasiswa: Hanya bisa edit data milik sendiri dengan status 'rejected'
    """
    
    def has_permission(self, request, view):
        # Wajib login
        if not request.user or not request.user.is_authenticated:
            return False
        return True

    def has_object_permission(self, request, view, obj):
        user = request.user
        user_role = getattr(user, 'role', '')
        
        # 1. METHOD SAFE (GET, HEAD, OPTIONS) - SEMUA BISA MELIHAT
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # 2. SUPER ADMIN atau AKADEMIK - AKSES PENUH
        if user.is_staff:
            return True
        
        # 3. DOSEN (DPA) - AKSES PENUH UNTUK VALIDASI
        # Perhatikan: role bisa 'dosen', 'dpa', atau 'dosen_pembimbing'
        if user_role in ['dosen', 'dpa', 'dosen_pembimbing']:
            print(f"✅ DPA {user.username} diizinkan melakukan {request.method}")  # Untuk debugging
            return True
        
        # 4. MAHASISWA - HANYA UNTUK DATA SENDIRI DENGAN STATUS 'REJECTED'
        if user_role == 'mahasiswa':
            # Cek kepemilikan data
            is_owner = False
            if hasattr(obj, 'mahasiswa') and obj.mahasiswa == user:
                is_owner = True
            elif hasattr(obj, 'user') and obj.user == user:
                is_owner = True
            elif hasattr(obj, 'mahasiswa_nim') and obj.mahasiswa_nim == getattr(user, 'nim_nip', None):
                is_owner = True
            
            if not is_owner:
                return False
            
            # Mahasiswa bisa POST (buat baru)
            if request.method == 'POST':
                return True
            
            # Mahasiswa bisa PATCH hanya jika status 'rejected'
            if request.method in ['PUT', 'PATCH']:
                if hasattr(obj, 'status'):
                    return obj.status == 'rejected'
                return False
            
            return False
        
        # 5. ROLE LAIN - TIDAK DIIZINKAN
        print(f"❌ User {user.username} dengan role {user_role} tidak diizinkan")
        return False