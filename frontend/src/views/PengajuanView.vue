<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-900 via-blue-900 to-slate-900 py-8 px-4 sm:px-6">
    <div class="max-w-2xl mx-auto">
      
      <div class="bg-white/95 backdrop-blur-sm rounded-2xl shadow-2xl overflow-hidden border border-blue-200">
        
        <div class="bg-gradient-to-r from-blue-700 to-blue-800 px-6 py-4 flex items-center gap-3">
          <button 
            @click="router.push('/dashboard-mahasiswa')" 
            class="group p-2 bg-white/20 hover:bg-white/30 rounded-xl transition-all duration-200 text-white hover:scale-105"
            title="Kembali ke Dashboard"
          >
            <svg class="w-5 h-5 transition-transform group-hover:-translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path>
            </svg>
          </button>
          <div>
            <h2 class="text-xl font-bold text-white tracking-tight">Ajukan Prestasi Baru</h2>
            <p class="text-xs text-blue-200 font-medium mt-0.5">Lengkapi formulir di bawah untuk klaim poin SKPM</p>
          </div>
        </div>

        <div class="p-6">
          <form @submit.prevent="submitPengajuan" class="space-y-5">
            
            <div>
              <label class="block text-xs font-bold text-slate-700 mb-1.5">
                Judul / Nama Kegiatan <span class="text-red-500">*</span>
              </label>
              <input
                v-model="form.judul_kegiatan"
                type="text"
                placeholder="Contoh: Juara 1 Lomba Debat Nasional"
                required
                class="w-full px-4 py-2.5 bg-white border-2 border-slate-200 rounded-xl focus:border-blue-500 focus:ring-0 outline-none transition-all text-slate-800 font-medium text-sm placeholder-slate-400"
              />
            </div>

            <div>
              <label class="block text-xs font-bold text-slate-700 mb-1.5">
                Komponen Penilaian Kategori <span class="text-red-500">*</span>
              </label>
              <button
                type="button"
                @click="isModalOpen = true"
                class="w-full p-3 bg-white border-2 border-slate-200 rounded-xl text-left flex justify-between items-center hover:border-blue-500 hover:bg-slate-50 outline-none transition-all group"
                :class="{'border-blue-500 bg-blue-50': form.kategori}"
              >
                <div class="flex flex-col overflow-hidden">
                  <span v-if="selectedCategoryName" class="text-slate-800 font-bold text-sm truncate">
                    {{ selectedCategoryName }}
                  </span>
                  <span v-else class="text-slate-400 font-medium text-sm">Klik untuk memilih kategori kegiatan...</span>
                </div>
                <svg class="w-5 h-5 text-slate-400 group-hover:text-blue-600 transition-colors shrink-0 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
                </svg>
              </button>
            </div>

            <div class="grid grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1.5">
                  Tanggal Pelaksanaan <span class="text-red-500">*</span>
                </label>
                <input
                  v-model="form.tanggal_kegiatan"
                  type="date"
                  required
                  class="w-full px-4 py-2.5 bg-white border-2 border-slate-200 rounded-xl focus:border-blue-500 focus:ring-0 outline-none transition-all text-slate-800 font-medium text-sm"
                />
              </div>
              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1.5">
                  Durasi Kegiatan
                </label>
                <input
                  v-model="form.durasi"
                  type="text"
                  placeholder="Misal: 3 Hari"
                  class="w-full px-4 py-2.5 bg-white border-2 border-slate-200 rounded-xl focus:border-blue-500 focus:ring-0 outline-none transition-all text-slate-800 font-medium text-sm placeholder-slate-400"
                />
              </div>
            </div>

            <div>
              <label class="block text-xs font-bold text-slate-700 mb-1.5">
                Bukti / Sertifikat Kegiatan <span class="text-red-500">*</span>
              </label>
              <div class="relative group">
                <input
                  type="file"
                  @change="handleFileChange"
                  accept=".pdf,image/*"
                  required
                  class="absolute inset-0 w-full h-full opacity-0 cursor-pointer z-20"
                />
                <div :class="[
                  'border-2 border-dashed rounded-xl p-4 transition-all duration-200 flex flex-col items-center justify-center text-center',
                  form.bukti_sertifikat ? 'border-blue-500 bg-blue-50' : 'border-slate-200 bg-slate-50 group-hover:border-blue-400'
                ]">
                  <div :class="['p-2 rounded-full shadow-sm mb-2', form.bukti_sertifikat ? 'bg-blue-600 text-white' : 'bg-white text-blue-500']">
                    <svg v-if="!form.bukti_sertifikat" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path>
                    </svg>
                    <svg v-else class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                    </svg>
                  </div>
                  <p class="text-sm font-medium text-slate-700">
                    {{ form.bukti_sertifikat ? form.bukti_sertifikat.name : 'Pilih file sertifikat' }}
                  </p>
                  <p v-if="!form.bukti_sertifikat" class="text-xs text-slate-400 mt-1">PDF, JPG, PNG (Max 2MB)</p>
                  <p v-else class="text-xs text-blue-600 font-semibold mt-1">File siap diunggah</p>
                </div>
              </div>
            </div>

            <div>
              <label class="block text-xs font-bold text-slate-700 mb-1.5">
                Link Informasi Kegiatan <span class="text-slate-400 font-normal">(Opsional)</span>
              </label>
              <input
                v-model="form.informasi_kegiatan"
                type="url"
                placeholder="Contoh: https://pengumuman-lomba.com"
                class="w-full px-4 py-2.5 bg-white border-2 border-slate-200 rounded-xl focus:border-blue-500 focus:ring-0 outline-none transition-all text-slate-800 font-medium text-sm placeholder-slate-400"
              />
            </div>

            <div>
              <label class="block text-xs font-bold text-slate-700 mb-1.5">
                Catatan Tambahan <span class="text-slate-400 font-normal">(Opsional)</span>
              </label>
              <textarea
                v-model="form.komentar"
                rows="2"
                placeholder="Berikan keterangan tambahan untuk verifikator jika perlu..."
                class="w-full px-4 py-2.5 bg-white border-2 border-slate-200 rounded-xl focus:border-blue-500 focus:ring-0 outline-none resize-none transition-all text-slate-700 text-sm placeholder-slate-400"
              ></textarea>
            </div>

            <div class="pt-2">
              <button
                type="submit"
                :disabled="isSubmitting"
                class="w-full bg-gradient-to-r from-blue-700 to-blue-800 text-white py-3 rounded-xl hover:from-blue-800 hover:to-blue-900 active:scale-[0.98] transition-all font-bold text-sm shadow-md disabled:opacity-50 disabled:cursor-not-allowed flex justify-center items-center gap-2"
              >
                <svg v-if="isSubmitting" class="animate-spin h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                  <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                {{ isSubmitting ? "Memproses..." : "Kirim Pengajuan" }}
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>

    <Teleport to="body">
      <Transition name="modal">
        <div v-if="isModalOpen" class="fixed inset-0 z-[100] flex items-center justify-center p-4">
          <div @click="isModalOpen = false" class="absolute inset-0 bg-slate-900/80 backdrop-blur-sm"></div>
          
          <div class="bg-white rounded-2xl shadow-2xl w-full max-w-2xl flex flex-col max-h-[85vh] overflow-hidden relative z-10 border border-blue-200">
            
            <div class="px-5 py-4 border-b border-slate-200 flex justify-between items-center bg-gradient-to-r from-blue-700 to-blue-800 shrink-0">
              <div>
                <h3 class="font-bold text-lg text-white">Pilih Komponen Penilaian</h3>
                <p class="text-xs text-blue-200 mt-0.5">Pilih kategori yang sesuai dengan sertifikat Anda</p>
              </div>
              <button @click="isModalOpen = false" class="p-1.5 bg-white/20 hover:bg-white/30 rounded-full transition-all text-white">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
              </button>
            </div>

            <div class="p-4 bg-slate-50 border-b border-slate-200 shrink-0">
              <div class="relative">
                <div class="absolute inset-y-0 left-3 flex items-center pointer-events-none">
                  <svg class="w-4 h-4 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
                </div>
                <input 
                  v-model="searchQuery"
                  type="text" 
                  placeholder="Cari kategori kegiatan..." 
                  class="w-full pl-9 pr-3 py-2 bg-white border border-slate-200 rounded-xl text-sm text-slate-700 outline-none focus:border-blue-500 focus:ring-0 transition-all"
                >
              </div>
            </div>

            <div class="p-4 overflow-y-auto flex-1 bg-slate-50 space-y-3 custom-scrollbar">
              
              <div v-if="filteredKategori.length === 0" class="flex flex-col items-center justify-center py-12 text-slate-500">
                <svg class="w-12 h-12 mb-3 text-slate-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                <p class="font-bold text-sm text-slate-600">Kategori tidak ditemukan</p>
                <p class="text-xs mt-1">Coba gunakan kata kunci lain.</p>
              </div>

              <div 
                v-for="cat in filteredKategori" 
                :key="cat.id"
                class="bg-white border border-slate-200 rounded-xl p-4 hover:border-blue-400 hover:shadow-md transition-all duration-200"
              >
                <div class="flex flex-col sm:flex-row justify-between gap-3">
                  <div class="space-y-2 flex-1">
                    <div class="flex flex-wrap gap-1.5">
                      <span class="inline-block px-2 py-0.5 bg-slate-100 text-slate-600 text-[10px] font-bold uppercase tracking-wider rounded-md">
                        {{ cat.bidang }}
                      </span>
                      <span class="inline-block px-2 py-0.5 bg-amber-50 text-amber-600 text-[10px] font-bold rounded-md">
                        {{ cat.level || 'Lokal' }}
                      </span>
                      <span class="inline-block px-2 py-0.5 bg-emerald-50 text-emerald-600 text-[10px] font-bold rounded-md">
                        {{ cat.sifat || 'Pilihan' }}
                      </span>
                    </div>
                    <h4 class="font-bold text-slate-800 text-sm leading-snug">
                      {{ cat.nama_kegiatan || cat.kegiatan }}
                    </h4>
                    <p class="text-xs text-slate-500">Peran: {{ cat.partisipasi || 'Umum' }}</p>
                  </div>
                  
                  <div class="flex flex-row sm:flex-col items-center justify-between sm:justify-center gap-3 shrink-0">
                    <div class="text-center">
                      <p class="text-[10px] font-bold text-slate-400 uppercase">Poin</p>
                      <p class="text-2xl font-black text-blue-600 leading-none">{{ cat.bobot_poin }}</p>
                    </div>
                    <button 
                      @click="pilihKategori(cat)"
                      type="button"
                      class="px-4 py-1.5 bg-blue-600 hover:bg-blue-700 text-white text-xs font-bold rounded-lg transition-all shadow active:scale-95 whitespace-nowrap"
                    >
                      Pilih
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </Transition>
    </Teleport>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { useRouter } from "vue-router";
import api from "../api/api"; 

const router = useRouter();
const isSubmitting = ref(false);
const isModalOpen = ref(false);
const searchQuery = ref("");
const selectedCategoryName = ref("");

// State Data Form
const form = ref({
  judul_kegiatan: "",
  kategori: "",
  tanggal_kegiatan: "",
  durasi: "",
  informasi_kegiatan: "", 
  bukti_sertifikat: null,
  komentar: "",
});

const daftarKategori = ref([]);

const filteredKategori = computed(() => {
  if (!searchQuery.value) return daftarKategori.value;
  const query = searchQuery.value.toLowerCase();
  return daftarKategori.value.filter(cat => {
    const bidang = (cat.bidang || '').toLowerCase();
    const kegiatan = (cat.nama_kegiatan || cat.kegiatan || '').toLowerCase();
    const partisipasi = (cat.partisipasi || '').toLowerCase();
    return bidang.includes(query) || kegiatan.includes(query) || partisipasi.includes(query);
  });
});

onMounted(async () => {
  try {
    const response = await api.get("api/kategori/");
    daftarKategori.value = response.data;
  } catch (err) {
    console.error("Gagal mengambil kategori:", err);
  }
});

const pilihKategori = (cat) => {
  form.value.kategori = cat.id;
  selectedCategoryName.value = `${cat.nama_kegiatan || cat.kegiatan} - ${cat.bobot_poin} Poin`;
  isModalOpen.value = false; 
  searchQuery.value = "";
};

const handleFileChange = (e) => {
  const file = e.target.files[0];
  if (!file) return;
  
  // Validasi ukuran file (max 2MB)
  if (file.size > 2 * 1024 * 1024) {
    alert("Ukuran file maksimal 2MB!");
    e.target.value = "";
    return;
  }
  
  form.value.bukti_sertifikat = file;
};

const submitPengajuan = async () => {
  if (!form.value.kategori) {
    alert("Silakan pilih Komponen Penilaian terlebih dahulu.");
    return;
  }

  isSubmitting.value = true;
  const formData = new FormData();

  formData.append("judul_kegiatan", form.value.judul_kegiatan);
  formData.append("kategori", form.value.kategori); 
  formData.append("tanggal_kegiatan", form.value.tanggal_kegiatan);
  
  if (form.value.durasi) formData.append("durasi_kegiatan", form.value.durasi);
  if (form.value.komentar) formData.append("catatan", form.value.komentar);
  
  // <-- Tambahan push data Link ke FormData
  if (form.value.informasi_kegiatan) {
    formData.append("informasi_kegiatan", form.value.informasi_kegiatan);
  }
  
  if (form.value.bukti_sertifikat) {
    formData.append("bukti_sertifikat", form.value.bukti_sertifikat);
  }

  try {
    const token = localStorage.getItem("access_token");
    await api.post("api/kegiatan/", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
        Authorization: `Bearer ${token}`,
      },
    });
    alert("✅ Pengajuan berhasil dikirim!");
    router.push("/dashboard-mahasiswa");
  } catch (error) {
    console.error("Error:", error.response?.data);
    alert("❌ Gagal mengirim. Pastikan semua field wajib terisi.");
  } finally {
    isSubmitting.value = false;
  }
};
</script>

<style scoped>
/* Modal Transition */
.modal-enter-active, .modal-leave-active {
  transition: opacity 0.2s ease;
}
.modal-enter-from, .modal-leave-to {
  opacity: 0;
}
.modal-enter-active .bg-white, .modal-leave-active .bg-white {
  transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.modal-enter-from .bg-white {
  transform: scale(0.95) translateY(10px);
}
.modal-leave-to .bg-white {
  transform: scale(0.98);
}

/* Custom Scrollbar */
.custom-scrollbar::-webkit-scrollbar {
  width: 6px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: #f1f5f9;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background: #cbd5e1;
  border-radius: 10px;
}
.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background: #94a3b8;
}

input[type="date"]::-webkit-calendar-picker-indicator {
  cursor: pointer;
  opacity: 0.5;
}
input[type="date"]::-webkit-calendar-picker-indicator:hover {
  opacity: 1;
}
</style>