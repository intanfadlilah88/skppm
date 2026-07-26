<template>
  <div class="p-6 bg-gray-50 min-h-screen font-sans">
    <div class="max-w-6xl mx-auto">
      
      <div class="flex justify-between items-center mb-6 bg-white p-5 rounded-2xl shadow-sm border border-gray-100">
        <div>
          <h2 class="text-2xl font-extrabold text-gray-800 tracking-tight">Verifikasi DPA</h2>
          <p class="text-xs text-gray-400 mt-1 font-medium italic">Sistem Kredit Poin Mahasiswa (SKPM) STIE SBI</p>
        </div>
        <button @click="handleLogout" class="flex items-center gap-2 bg-red-50 text-red-600 px-5 py-2.5 rounded-xl hover:bg-red-600 hover:text-white transition-all duration-200 font-bold text-sm shadow-sm">
          Keluar
        </button>
      </div>

      <div class="bg-white shadow-xl rounded-2xl overflow-hidden border border-gray-100">
        <table class="w-full text-left border-collapse">
          <thead class="bg-gray-50/50 text-gray-500 text-[11px] uppercase tracking-widest font-black border-b">
            <tr>
              <th class="p-5">Informasi Mahasiswa</th>
              <th class="p-5">Detail Kegiatan</th>
              <th class="p-5 text-center">Dokumen Bukti</th>
              <th class="p-5 text-center">Status</th>
              <th class="p-5 text-center">Tindakan</th>
            </tr>
          </thead>
          <tbody class="text-sm divide-y divide-gray-50">
            <tr v-for="item in pengajuanList" :key="item.id" class="hover:bg-blue-50/30 transition-colors">
              <td class="p-5">
                <div class="font-bold text-gray-800">{{ item.user_detail?.full_name || item.mahasiswa_nama || 'Tanpa Nama' }}</div>
                <div class="text-[10px] text-gray-400 font-mono mt-0.5 tracking-tighter">{{ item.user_detail?.nim_nip || 'NIM tidak tersedia' }}</div>
              </td>
              <td class="p-5">
                <div class="text-gray-700 font-medium line-clamp-1">{{ item.nama_kegiatan || item.judul_kegiatan }}</div>
                <div class="text-[10px] text-blue-500 font-bold uppercase tracking-tighter">{{ item.kategori_nama || 'Kategori Umum' }}</div>
              </td>
              <td class="p-5 text-center">
                <a :href="item.bukti_sertifikat" target="_blank" class="inline-flex items-center text-blue-600 font-bold hover:text-blue-800 transition-colors decoration-2 underline underline-offset-4">
                  Buka Sertifikat
                </a>
              </td>
              <td class="p-5 text-center">
                <span :class="{
                  'text-yellow-700 bg-yellow-100 border-yellow-200': item.status === 'pending',
                  'text-green-700 bg-green-100 border-green-200': item.status === 'disetujui',
                  'text-red-700 bg-red-100 border-red-200': item.status === 'ditolak'
                }" class="px-3 py-1 rounded-full text-[9px] font-black uppercase border shadow-sm">
                  {{ item.status }}
                </span>
              </td>
              <td class="p-5">
                <div class="flex space-x-2 justify-center">
                  <template v-if="item.status === 'pending'">
                    <button @click="updateStatus(item.id, 'disetujui')" class="bg-green-600 text-white px-4 py-1.5 rounded-lg text-[11px] font-bold hover:bg-green-700 shadow-md transition-transform active:scale-95">Setujui</button>
                    <button @click="updateStatus(item.id, 'ditolak')" class="bg-white border border-red-200 text-red-600 px-4 py-1.5 rounded-lg text-[11px] font-bold hover:bg-red-50 transition-transform active:scale-95">Tolak</button>
                  </template>
                  <span v-else class="text-gray-400 italic text-[11px] font-medium tracking-tight">Sudah Diverifikasi</span>
                </div>
              </td>
            </tr>
            
            <tr v-if="pengajuanList.length === 0 && !loading">
              <td colspan="5" class="p-20 text-center text-gray-400 italic bg-gray-50/20">
                <div class="flex flex-col items-center gap-2">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-gray-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4" />
                  </svg>
                  <span>Data ajuan mahasiswa bimbingan belum tersedia.</span>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import api from '../api/api';

const router = useRouter();
const pengajuanList = ref([]);
const loading = ref(false);

const fetchPengajuan = async () => {
  const token = localStorage.getItem('access_token');
  if (!token) return router.push('/login');
  
  loading.value = true;
  try {
    // PERBAIKAN: Tambahkan "/" di akhir URL agar sesuai dengan DefaultRouter Django
    const res = await api.get('api/kegiatan/', {
      headers: { Authorization: `Bearer ${token}` }
    });
    
    // PERBAIKAN: Antisipasi jika Django menggunakan Pagination (res.data.results)
    if (Array.isArray(res.data)) {
      pengajuanList.value = res.data;
    } else if (res.data && res.data.results) {
      pengajuanList.value = res.data.results;
    } else {
      pengajuanList.value = [];
    }
  } catch (err) {
    console.error("Gagal memuat data bimbingan:", err);
    if (err.response?.status === 401) {
      localStorage.clear();
      router.push('/login');
    }
  } finally {
    loading.value = false;
  }
};

const updateStatus = async (id, status) => {
  const token = localStorage.getItem('access_token');
  // Gunakan kata "Verifikasi" agar lebih profesional
  if (!confirm(`Konfirmasi Verifikasi: Tandai sebagai ${status.toUpperCase()}?`)) return;

  try {
    // PERBAIKAN: Pastikan URL berakhir dengan "/" sebelum ID (api/kegiatan/ID/)
    await api.patch(`api/kegiatan/${id}/`, { status: status }, {
      headers: { Authorization: `Bearer ${token}` }
    });
    alert(`Status berhasil diperbarui menjadi: ${status}`);
    fetchPengajuan(); 
  } catch (err) {
    console.error(err);
    alert("Gagal memperbarui status. Pastikan role Anda adalah DPA.");
  }
};

const handleLogout = () => {
  if (confirm("Keluar dari sistem verifikasi?")) {
    localStorage.clear();
    router.push('/login');
  }
};

onMounted(fetchPengajuan);
</script>

