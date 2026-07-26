from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, KategoriKegiatan, Kegiatan

# 1. Kustomisasi Tampilan User di Admin
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'role', 'nim_nip', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Informasi Tambahan', {'fields': ('role', 'nim_nip')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informasi Tambahan', {'fields': ('role', 'nim_nip')}),
    )

# 2. Kustomisasi Tampilan Kategori Kegiatan - TANPA menyebut field spesifik
class KategoriKegiatanAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__')

# 3. Kustomisasi Tampilan Data Kegiatan - TANPA menyebut field spesifik
class KegiatanAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__')

# 4. Daftarkan Model ke Admin Panel
admin.site.register(User, CustomUserAdmin)
admin.site.register(KategoriKegiatan, KategoriKegiatanAdmin)
admin.site.register(Kegiatan, KegiatanAdmin)