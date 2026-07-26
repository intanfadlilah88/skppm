<template>
  <div class="flex min-h-screen bg-[#f8fafc]">
    <!-- SIDEBAR -->
    <aside class="w-72 bg-[#1e293b] text-white hidden md:flex flex-col">
      <div class="p-6 flex items-center gap-3 border-b border-slate-700/50">
        <div class="w-12 h-12 rounded-xl flex items-center justify-center shadow-lg shadow-blue-900/20 flex-shrink-0 overflow-hidden bg-blue-600">
          <img :src="logoStiesbi" alt="STIE SBI" class="w-full h-full object-cover" />
        </div>
        <div>
          <span class="text-sm font-black tracking-tight uppercase leading-tight block">SKPM</span>
          <span class="text-[10px] font-bold text-blue-300 tracking-wider">STIE SBI Yogyakarta</span>
        </div>
      </div>
      
      <nav class="px-4 py-4 space-y-1 flex-1">
        <div @click="resetFilter" class="flex items-center gap-3 px-4 py-3 bg-blue-600 rounded-xl cursor-pointer shadow-lg shadow-blue-600/20 transition-all hover:bg-blue-700">
          <span class="text-base">🏠</span>
          <span class="font-bold text-sm">Beranda</span>
        </div>
        <div @click="scrollToRiwayat" class="flex items-center gap-3 px-4 py-3 text-slate-400 hover:text-white hover:bg-slate-800 rounded-xl cursor-pointer transition-all group">
          <span class="text-base group-hover:scale-110 transition">🏆</span>
          <span class="font-bold text-sm">Riwayat Prestasi</span>
        </div>
        <div @click="filterRejectedOnly" class="flex items-center gap-3 px-4 py-3 text-slate-400 hover:text-white hover:bg-slate-800 rounded-xl cursor-pointer transition-all group">
          <span class="text-base group-hover:scale-110 transition">⚠️</span>
          <span class="font-bold text-sm">Perlu Revisi</span>
          <span v-if="rejectedCount > 0" class="ml-auto bg-rose-500 text-white text-[10px] font-black px-2 py-1 rounded-full">{{ rejectedCount }}</span>
        </div>
      </nav>

      <!-- FOOTER SIDEBAR -->
      <div class="p-3 lg:p-4 border-t border-white/10 bg-gradient-to-b from-slate-800 to-slate-900 flex-shrink-0 sticky bottom-0 z-10">
        <div class="text-[10px] text-slate-500 text-center">
          <p>Sistem Kredit Poin Prestasi Mahasiswa</p>
          <p class="mt-0.5">STIE SBI Yogyakarta</p>
        </div>
      </div>
    </aside>

    <main class="flex-1 p-6 lg:p-10 overflow-y-auto">
      <!-- PROFIL HEADER (DI ATAS) DENGAN LOGOUT -->
      <div class="mb-6 bg-white p-6 rounded-3xl shadow-sm flex justify-between items-center border border-slate-100 transition-all hover:shadow-md">
        <div @click="openEditModal" class="flex items-center gap-4 cursor-pointer group">
          <div class="relative">
            <div class="w-14 h-14 bg-gradient-to-tr from-blue-700 to-blue-500 rounded-2xl flex items-center justify-center text-white text-2xl font-black shadow-xl shadow-blue-100">
              {{ userProfile?.full_name?.charAt(0) || "L" }}
            </div>
            <div class="absolute -bottom-1 -right-1 w-5 h-5 bg-green-500 border-4 border-white rounded-full"></div>
          </div>
          <div>
            <h2 class="text-xl font-black text-slate-800 group-hover:text-blue-600 transition-colors">
              {{ userProfile?.full_name || "Lila" }}
            </h2>
            <p class="text-sm text-blue-600 font-bold tracking-wide mt-0.5">
              {{ userProfile?.nim_nip || "1400000" }} 
              <span class="text-slate-300 mx-2">•</span> 
              <span class="text-slate-500 text-xs">{{ userProfile?.prodi || "Informatika" }}</span>
            </p>
          </div>
        </div>

        <!-- TOMBOL LOGOUT DI SAMPING PROFIL -->
        <button 
          @click="handleLogout"
          class="bg-rose-500 hover:bg-rose-600 text-white px-6 py-3 rounded-xl transition-all duration-200 font-bold text-sm shadow-lg shadow-rose-200 flex items-center gap-2"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
          </svg>
          <span>Logout</span>
        </button>
      </div>

      <!-- NOTIFIKASI - HANYA MUNCUL JIKA ADA DATA -->
      <div v-if="rejectedCount > 0 || pendingCount > 0" class="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
        <!-- Notifikasi - 3 kolom -->
        <div class="md:col-span-3">
          <!-- NOTIFIKASI BERKAS DITOLAK/REVISI -->
          <div v-if="rejectedCount > 0" class="bg-gradient-to-r from-rose-500 to-rose-600 text-white p-4 rounded-2xl shadow-lg shadow-rose-200 flex items-center justify-between">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 bg-white/20 rounded-xl flex items-center justify-center text-xl flex-shrink-0">
                ⚠️
              </div>
              <div>
                <p class="font-black text-sm">Ada {{ rejectedCount }} pengajuan yang perlu direvisi!</p>
                <p class="text-xs text-rose-100">Silakan periksa dan perbarui data sesuai catatan DPA.</p>
              </div>
            </div>
            <button @click="goToRejectedItems" class="px-4 py-2 bg-white text-rose-600 rounded-xl font-bold text-xs hover:bg-rose-50 transition-all flex-shrink-0">
              Lihat Semua
            </button>
          </div>

          <!-- NOTIFIKASI PENGINGAT UNTUK DATA PENDING -->
          <div v-else-if="pendingCount > 0 && rejectedCount === 0" class="bg-gradient-to-r from-amber-500 to-amber-600 text-white p-4 rounded-2xl shadow-lg shadow-amber-200 flex items-center justify-between">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 bg-white/20 rounded-xl flex items-center justify-center text-xl flex-shrink-0">
                ⏳
              </div>
              <div>
                <p class="font-black text-sm">{{ pendingCount }} pengajuan sedang menunggu validasi!</p>
                <p class="text-xs text-amber-100">Silakan tunggu persetujuan dari DPA Anda.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- TOMBOL TAMBAH PRESTASI - 1 kolom -->
        <div>
          <router-link to="/pengajuan" class="w-full h-full bg-[#0f172a] hover:bg-blue-700 text-white px-4 py-3 rounded-2xl transition-all shadow-lg font-bold flex items-center justify-center gap-2 active:scale-95 text-sm">
            <span class="text-lg">+</span> Tambah Prestasi
          </router-link>
        </div>
      </div>

      <!-- TOMBOL TAMBAH PRESTASI (jika tidak ada notifikasi) -->
      <div v-else class="flex justify-end mb-6">
        <router-link to="/pengajuan" class="bg-[#0f172a] hover:bg-blue-700 text-white px-6 py-3 rounded-xl transition-all shadow-lg font-bold flex items-center gap-2 active:scale-95 text-sm">
          <span class="text-lg">+</span> Tambah Prestasi
        </router-link>
      </div>

      <!-- STATS CARDS -->
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-6 mb-10">
        <div v-for="stat in statsCards" :key="stat.label" 
             :class="stat.bgColor" 
             class="p-6 rounded-2xl text-white relative overflow-hidden shadow-xl transition-all hover:-translate-y-1 group">
          <div class="relative z-10">
            <h3 class="text-3xl font-black mb-1">{{ stat.value }}</h3>
            <p class="text-[10px] font-black uppercase tracking-[0.15em] opacity-80">{{ stat.label }}</p>
          </div>
          <span class="absolute -right-3 -bottom-3 text-7xl opacity-10 rotate-12 group-hover:rotate-0 transition-transform duration-500">
            {{ stat.icon }}
          </span>
        </div>
      </div>

      <!-- RIWAYAT TABLE -->
      <div id="riwayat-section" class="bg-white rounded-3xl shadow-sm border border-slate-50 overflow-hidden flex flex-col">
        <div class="p-6 flex flex-col md:flex-row justify-between items-start md:items-center gap-4 border-b border-slate-100">
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 bg-orange-50 rounded-xl flex items-center justify-center text-xl shadow-sm flex-shrink-0">📋</div>
            <h3 class="font-black text-slate-800 text-lg tracking-tight">
              {{ filterStatus === 'rejected' ? 'Pengajuan Perlu Revisi' : 'Riwayat Pengajuan' }}
            </h3>
            <span v-if="filterStatus === 'rejected' && rejectedCount > 0" class="bg-rose-100 text-rose-700 px-2 py-0.5 rounded-full text-xs font-black">
              {{ rejectedCount }}
            </span>
          </div>
          
          <div class="flex gap-2 flex-wrap">
            <button 
              @click="filterStatus = 'all'; currentPage = 1" 
              :class="['px-3 py-1.5 rounded-xl text-xs font-bold transition-all', filterStatus === 'all' ? 'bg-blue-600 text-white' : 'bg-slate-100 text-slate-600 hover:bg-slate-200']"
            >
              Semua
            </button>
            <button 
              @click="filterStatus = 'rejected'; currentPage = 1" 
              :class="['px-3 py-1.5 rounded-xl text-xs font-bold transition-all', filterStatus === 'rejected' ? 'bg-rose-600 text-white' : 'bg-slate-100 text-slate-600 hover:bg-slate-200']"
            >
              Perlu Revisi
              <span v-if="rejectedCount > 0" class="ml-1">({{ rejectedCount }})</span>
            </button>
            
            <div class="relative w-48">
              <div class="absolute inset-y-0 left-3 flex items-center pointer-events-none">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
              </div>
              <input 
                v-model="searchRiwayat"
                type="text" 
                placeholder="Cari kegiatan..." 
                class="w-full pl-9 pr-3 py-2 bg-slate-50 border-2 border-slate-200 rounded-xl font-bold text-slate-700 text-xs focus:border-blue-500 focus:bg-white focus:ring-0 outline-none transition-all"
              />
            </div>
          </div>
        </div>

        <div class="overflow-x-auto px-4 pb-4 pt-2">
          <table class="w-full border-separate border-spacing-y-3">
            <thead>
              <tr class="text-slate-400 text-[10px] font-black uppercase tracking-widest">
                <th class="px-4 py-2 text-left">Detail Kegiatan</th>
                <th class="px-4 py-2 text-center w-20">Poin</th>
                <th class="px-4 py-2 text-center w-44">Status</th>
                <th class="px-4 py-2 text-right w-40">Tindakan</th>
              </tr>
            </thead>
            
            <tbody v-if="!loading && paginatedRiwayat.length > 0">
              <tr v-for="item in paginatedRiwayat" :key="item.id" class="bg-[#f8fafc]/80 hover:bg-blue-50/50 transition-all group">
                <td class="px-4 py-4 rounded-l-2xl">
                  <div class="font-black text-slate-800 text-base group-hover:text-blue-700 transition-colors mb-1 leading-snug">
                    {{ item.judul_kegiatan }}
                  </div>
                  <div class="text-[10px] text-blue-600 font-bold uppercase tracking-wider bg-blue-100 inline-block px-2 py-0.5 rounded-lg">
                    {{ item.nama_kategori || 'Kategori Umum' }}
                  </div>
                  <div v-if="item.status === 'rejected' && item.komentar_dpa" class="mt-1 text-[10px] text-rose-600 bg-rose-50 inline-flex items-center gap-1 px-2 py-0.5 rounded-lg">
                    <svg class="h-3 w-3" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd" /></svg>
                    {{ item.komentar_dpa.substring(0, 40) }}{{ item.komentar_dpa.length > 40 ? '...' : '' }}
                  </div>
                </td>
                <td class="px-4 py-4 text-center font-black text-slate-800 text-2xl">
                  {{ item.poin_valid || item.bobot_poin_kategori || "0" }}
                </td>
                <td class="px-4 py-4 text-center">
                  <div class="flex flex-col items-center gap-1">
                    <span :class="statusStyle(item.status)" class="px-3 py-1.5 rounded-xl text-[10px] font-black uppercase tracking-wider border shadow-sm w-full text-center">
                      {{ formatStatusText(item.status) }}
                    </span>
                    <span v-if="item.status === 'rejected' && item.komentar_dpa" class="text-[9px] text-red-600 font-black uppercase tracking-wider flex items-center gap-1 mt-0.5 bg-red-100 px-2 py-0.5 rounded-lg">
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" viewBox="0 0 24 24" fill="currentColor"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd" /></svg>
                      Revisi
                    </span>
                  </div>
                </td>
                <td class="px-4 py-4 text-right rounded-r-2xl">
                  <div class="flex gap-2 justify-end">
                    <button @click="openDetail(item)" class="font-black text-white bg-blue-600 hover:bg-blue-800 px-4 py-2 rounded-xl transition-all text-[10px] uppercase tracking-wider shadow-md hover:shadow-lg active:scale-95">
                      Detail
                    </button>
                    <button 
                      v-if="item.status === 'rejected'"
                      @click="openEditPengajuan(item)" 
                      class="font-black text-white bg-amber-500 hover:bg-amber-600 px-4 py-2 rounded-xl transition-all text-[10px] uppercase tracking-wider shadow-md hover:shadow-lg active:scale-95 flex items-center gap-1"
                    >
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                      </svg>
                      Edit
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
          
          <div v-if="paginatedRiwayat.length === 0 && !loading" class="py-12 text-center bg-slate-50/50 rounded-2xl mt-2">
            <div class="text-5xl mb-2 opacity-30">📭</div>
            <p class="text-slate-500 font-bold text-sm">
              {{ searchRiwayat ? 'Kegiatan tidak ditemukan.' : 'Belum ada data prestasi.' }}
            </p>
            <p class="text-slate-400 text-xs mt-1">Silakan ajukan prestasi Anda melalui tombol "Tambah Prestasi".</p>
          </div>
        </div>

        <div v-if="filteredRiwayat.length > 0" class="flex flex-col sm:flex-row justify-between items-center px-6 py-4 bg-slate-50 border-t border-slate-100 gap-3">
          <span class="text-xs font-bold text-slate-500">
            Menampilkan <strong class="text-slate-800">{{ (currentPage - 1) * itemsPerPage + 1 }}</strong> - <strong class="text-slate-800">{{ Math.min(currentPage * itemsPerPage, filteredRiwayat.length) }}</strong> dari <strong class="text-slate-800">{{ filteredRiwayat.length }}</strong> data
          </span>
          <div class="flex gap-2">
            <button @click="prevPage" :disabled="currentPage === 1" class="px-4 py-2 rounded-xl font-black bg-white border-2 border-slate-200 text-slate-600 hover:bg-blue-50 hover:text-blue-600 hover:border-blue-300 disabled:opacity-40 disabled:hover:bg-white disabled:hover:border-slate-200 disabled:cursor-not-allowed transition-all uppercase tracking-wider text-[10px]">
              Sebelumnya
            </button>
            <button @click="nextPage" :disabled="currentPage === totalPages" class="px-4 py-2 rounded-xl font-black bg-white border-2 border-slate-200 text-slate-600 hover:bg-blue-50 hover:text-blue-600 hover:border-blue-300 disabled:opacity-40 disabled:hover:bg-white disabled:hover:border-slate-200 disabled:cursor-not-allowed transition-all uppercase tracking-wider text-[10px]">
              Selanjutnya
            </button>
          </div>
        </div>
      </div>

      <!-- MODAL DETAIL -->
      <Transition name="scale">
        <div v-if="isDetailOpen" class="fixed inset-0 z-[100] flex items-center justify-center p-4">
          <div class="absolute inset-0 bg-slate-900/60 backdrop-blur-md" @click="isDetailOpen = false"></div>
          <div class="relative bg-white w-full max-w-lg rounded-3xl shadow-2xl overflow-hidden flex flex-col max-h-[90vh]">
            <div class="p-6 overflow-y-auto custom-scroll">
              <div class="flex justify-between items-start mb-5">
                <span :class="statusStyle(selectedDetail?.status)" class="px-3 py-1 rounded-full text-[9px] font-black uppercase border">
                  {{ formatStatusText(selectedDetail?.status) }}
                </span>
                <button @click="isDetailOpen = false" class="bg-slate-100 w-8 h-8 rounded-full flex items-center justify-center hover:bg-red-50 hover:text-red-500 transition-all text-sm">✕</button>
              </div>
              
              <h3 class="text-2xl font-black text-slate-900 leading-tight mb-5">{{ selectedDetail?.judul_kegiatan }}</h3>

              <div v-if="selectedDetail?.status === 'rejected' && selectedDetail?.komentar_dpa" class="mb-5 bg-red-50 p-4 rounded-2xl border border-red-200 shadow-sm relative overflow-hidden">
                <div class="absolute top-0 left-0 w-1.5 h-full bg-red-500"></div>
                <div class="flex items-center gap-1.5 mb-1">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-red-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" /></svg>
                  <p class="text-[10px] font-black text-red-600 uppercase tracking-widest">Catatan Revisi</p>
                </div>
                <p class="text-sm font-medium text-red-800 leading-relaxed">{{ selectedDetail.komentar_dpa }}</p>
              </div>

              <div v-if="selectedDetail?.is_edited_by_dpa && selectedDetail?.status !== 'rejected'" class="mb-5 bg-amber-50 p-3 rounded-xl border border-amber-200">
                <p class="text-[10px] font-bold text-amber-700 flex items-center gap-1.5">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" /></svg>
                  Data telah dikoreksi oleh DPA.
                </p>
              </div>

              <div class="grid grid-cols-2 gap-4 mb-5">
                <div class="bg-slate-50 p-4 rounded-2xl border border-slate-100">
                  <p class="text-[9px] font-black text-slate-400 uppercase mb-1">Kategori</p>
                  <p class="text-xs font-black text-slate-800 uppercase leading-snug">{{ selectedDetail?.nama_kategori || selectedDetail?.kategori_name || "Tidak ada" }}</p>
                </div>
                <div class="bg-blue-600 p-4 rounded-2xl text-white shadow-lg shadow-blue-100 flex flex-col justify-center">
                  <p class="text-[9px] font-black opacity-70 uppercase mb-0.5">Poin</p>
                  <p class="text-2xl font-black">{{ selectedDetail?.poin_valid || selectedDetail?.bobot_poin_kategori || "0" }}</p>
                </div>
              </div>

              <div class="space-y-3">
                <p class="text-[9px] font-black text-slate-400 uppercase tracking-widest ml-1">Dokumen Bukti</p>
                <a v-if="selectedDetail?.bukti_sertifikat" :href="getSertifikatUrl(selectedDetail.bukti_sertifikat)" target="_blank" class="flex items-center gap-4 p-4 bg-white border-2 border-dashed border-slate-200 rounded-2xl group cursor-pointer hover:border-blue-400 hover:bg-blue-50 transition-all decoration-transparent">
                  <div class="w-10 h-10 bg-blue-100 rounded-xl flex items-center justify-center text-xl group-hover:scale-110 transition flex-shrink-0">📄</div>
                  <div class="flex flex-col">
                    <span class="font-black text-slate-700 text-sm">Lihat Sertifikat</span>
                    <span class="text-[9px] text-slate-400 font-bold uppercase tracking-tight">Klik untuk membuka</span>
                  </div>
                </a>
                <div v-else class="p-4 bg-red-50 text-red-500 rounded-2xl text-center font-bold text-xs border border-red-100">
                  Sertifikat belum diunggah.
                </div>
              </div>
            </div>
            <div class="p-5 bg-slate-50 border-t border-slate-100 flex justify-between gap-3 shrink-0">
              <button 
                v-if="selectedDetail?.status === 'rejected'"
                @click="openEditPengajuan(selectedDetail); isDetailOpen = false" 
                class="flex-1 py-3 bg-amber-500 text-white font-black rounded-xl hover:bg-amber-600 transition shadow-xl active:scale-95 flex items-center justify-center gap-1.5 text-sm"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                </svg>
                Edit & Ajukan
              </button>
              <button @click="isDetailOpen = false" class="flex-1 py-3 bg-[#0f172a] text-white font-black rounded-xl hover:bg-blue-700 transition shadow-xl active:scale-95 text-sm">
                Selesai
              </button>
            </div>
          </div>
        </div>
      </Transition>

      <!-- MODAL EDIT PENGAJUAN (UNTUK REVISI) -->
      <Transition name="scale">
        <div v-if="isEditPengajuanOpen" class="fixed inset-0 z-[120] flex items-center justify-center p-4">
          <div class="absolute inset-0 bg-slate-900/60 backdrop-blur-md" @click="isEditPengajuanOpen = false"></div>
          <div class="relative bg-white w-full max-w-2xl max-h-[90vh] rounded-3xl shadow-2xl overflow-hidden flex flex-col">
            <div class="p-5 border-b border-slate-100 bg-gradient-to-r from-amber-50 to-orange-50">
              <div class="flex justify-between items-center">
                <div class="flex items-center gap-3">
                  <div class="w-9 h-9 bg-amber-500 rounded-xl flex items-center justify-center text-white text-base shadow-lg flex-shrink-0">
                    ✏️
                  </div>
                  <div>
                    <h3 class="text-lg font-black text-slate-800">Edit & Ajukan Ulang</h3>
                    <p class="text-[10px] text-slate-500 mt-0.5">Perbaiki data sesuai catatan revisi DPA</p>
                  </div>
                </div>
                <button @click="isEditPengajuanOpen = false" class="text-slate-400 hover:text-red-500 transition-all text-2xl">&times;</button>
              </div>
            </div>

            <div class="flex-1 overflow-y-auto p-6 custom-scroll">
              <div v-if="editPengajuanData.komentar_dpa" class="mb-6 bg-red-50 p-4 rounded-xl border border-red-200">
                <div class="flex items-center gap-1.5 mb-1">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-red-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                  </svg>
                  <p class="text-[10px] font-black text-red-600 uppercase tracking-widest">Catatan Revisi</p>
                </div>
                <p class="text-sm text-red-800 font-medium">{{ editPengajuanData.komentar_dpa }}</p>
              </div>

              <div class="space-y-4">
                <div>
                  <label class="text-[10px] font-black text-slate-500 uppercase tracking-widest block mb-1.5">Judul Kegiatan <span class="text-red-500">*</span></label>
                  <input 
                    v-model="editPengajuanForm.judul_kegiatan" 
                    type="text" 
                    class="w-full p-3 bg-slate-50 border-2 border-slate-200 rounded-xl font-bold text-slate-800 text-sm focus:border-amber-400 focus:bg-white focus:ring-4 focus:ring-amber-50 outline-none transition-all"
                    placeholder="Masukkan judul kegiatan"
                  />
                </div>

                <div>
                  <label class="text-[10px] font-black text-slate-500 uppercase tracking-widest block mb-1.5">Kategori Kegiatan <span class="text-red-500">*</span></label>
                  <button 
                    @click="openKategoriModalForEdit" 
                    type="button" 
                    class="w-full p-3 bg-slate-50 border-2 border-slate-200 rounded-xl text-left font-bold text-slate-800 text-sm hover:border-amber-400 transition-all flex justify-between items-center"
                  >
                    <span :class="editPengajuanForm.kategori_id ? 'text-slate-800' : 'text-slate-400'">
                      {{ editPengajuanForm.kategori_name || 'Pilih kategori...' }}
                    </span>
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4" />
                    </svg>
                  </button>
                </div>

                <div class="grid grid-cols-2 gap-4">
                  <div>
                    <label class="text-[10px] font-black text-slate-500 uppercase tracking-widest block mb-1.5">Tanggal <span class="text-red-500">*</span></label>
                    <input 
                      v-model="editPengajuanForm.tanggal_kegiatan" 
                      type="date" 
                      class="w-full p-3 bg-slate-50 border-2 border-slate-200 rounded-xl font-bold text-slate-800 text-sm focus:border-amber-400 focus:bg-white focus:ring-4 focus:ring-amber-50 outline-none transition-all"
                    />
                  </div>
                  <div>
                    <label class="text-[10px] font-black text-slate-500 uppercase tracking-widest block mb-1.5">Durasi</label>
                    <input 
                      v-model="editPengajuanForm.durasi_kegiatan" 
                      type="text" 
                      placeholder="Contoh: 2 Hari"
                      class="w-full p-3 bg-slate-50 border-2 border-slate-200 rounded-xl font-bold text-slate-800 text-sm focus:border-amber-400 focus:bg-white focus:ring-4 focus:ring-amber-50 outline-none transition-all"
                    />
                  </div>
                </div>

                <div>
                  <label class="text-[10px] font-black text-slate-500 uppercase tracking-widest block mb-1.5">Upload Bukti Sertifikat</label>
                  <div class="border-2 border-dashed border-slate-300 rounded-xl p-5 text-center hover:border-amber-400 transition-all cursor-pointer" @click="triggerFileInput">
                    <input type="file" ref="fileInput" @change="handleFileUpload" accept=".pdf,.jpg,.jpeg,.png" class="hidden" />
                    <div v-if="!editPengajuanForm.bukti_sertifikat_file && !editPengajuanForm.existing_file">
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 mx-auto text-slate-400 mb-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                      </svg>
                      <p class="text-slate-500 font-medium text-sm">Klik untuk upload file</p>
                      <p class="text-[10px] text-slate-400 mt-0.5">PDF, JPG, PNG (max 5MB)</p>
                    </div>
                    <div v-else class="flex items-center justify-between p-3 bg-amber-50 rounded-xl">
                      <div class="flex items-center gap-3">
                        <span class="text-xl">📎</span>
                        <div class="text-left">
                          <p class="text-sm font-bold text-slate-700">{{ editPengajuanForm.bukti_sertifikat_file?.name || 'File sudah diupload' }}</p>
                          <p class="text-[10px] text-slate-500">Klik untuk mengganti</p>
                        </div>
                      </div>
                      <button @click.stop="removeFile" class="text-red-500 hover:text-red-700 text-sm">✕</button>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div class="p-5 bg-slate-50 border-t border-slate-100 flex justify-end gap-3 shrink-0">
              <button @click="isEditPengajuanOpen = false" class="px-6 py-2.5 bg-white border-2 border-slate-200 text-slate-600 font-black rounded-xl hover:bg-slate-100 transition-all text-xs uppercase tracking-widest">
                Batal
              </button>
              <button @click="submitEditPengajuan" :disabled="submitting" class="px-6 py-2.5 bg-amber-500 text-white font-black rounded-xl hover:bg-amber-600 transition-all shadow-lg shadow-amber-200 text-xs uppercase tracking-widest flex items-center gap-2 disabled:opacity-50">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                {{ submitting ? 'Menyimpan...' : 'Simpan & Ajukan' }}
              </button>
            </div>
          </div>
        </div>
      </Transition>

      <!-- MODAL PILIH KATEGORI -->
      <Transition name="scale">
        <div v-if="showKategoriModal" class="fixed inset-0 z-[130] flex items-center justify-center p-4">
          <div class="absolute inset-0 bg-slate-900/60 backdrop-blur-md" @click="showKategoriModal = false"></div>
          <div class="relative bg-white w-full max-w-xl max-h-[80vh] rounded-2xl shadow-2xl overflow-hidden flex flex-col">
            <div class="p-4 border-b border-slate-100 flex justify-between items-center bg-slate-50">
              <h3 class="text-base font-black text-slate-800">Pilih Kategori</h3>
              <button @click="showKategoriModal = false" class="text-slate-400 hover:text-red-500 text-xl">&times;</button>
            </div>
            <div class="p-4">
              <div class="relative mb-3">
                <input v-model="searchKategori" type="text" placeholder="Cari kategori..." class="w-full p-3 bg-white border-2 border-slate-200 rounded-xl focus:border-amber-400 outline-none transition-all text-sm" />
              </div>
              <div class="max-h-[40vh] overflow-y-auto space-y-2">
                <div v-for="kat in filteredKategoriList" :key="kat.id" @click="selectKategori(kat)" class="p-3 border-2 border-slate-100 rounded-xl hover:border-amber-400 hover:bg-amber-50 cursor-pointer transition-all flex justify-between items-center">
                  <div>
                    <p class="font-bold text-slate-800 text-sm">{{ kat.nama_kegiatan || kat.kegiatan }}</p>
                    <p class="text-[10px] text-slate-500">Bidang: {{ kat.bidang }}</p>
                  </div>
                  <div class="text-right">
                    <p class="text-xl font-black text-amber-600">{{ kat.bobot_poin }}</p>
                    <p class="text-[9px] text-slate-400">Poin</p>
                  </div>
                </div>
                <div v-if="filteredKategoriList.length === 0" class="text-center py-8 text-slate-500 text-sm">Tidak ada kategori</div>
              </div>
            </div>
          </div>
        </div>
      </Transition>

      <!-- MODAL PROFIL -->
      <Transition name="scale">
        <div v-if="isModalOpen" class="fixed inset-0 z-[100] flex items-center justify-center p-4">
          <div class="absolute inset-0 bg-slate-900/60 backdrop-blur-md" @click="isModalOpen = false"></div>
          <div class="relative bg-white w-full max-w-lg rounded-2xl shadow-2xl overflow-hidden border border-slate-200">
            <div class="p-5 border-b border-slate-100 flex justify-between items-center bg-white">
              <h3 class="text-lg font-bold text-slate-800">Profil Saya</h3>
              <button @click="isModalOpen = false" class="text-slate-400 hover:text-red-500 transition-colors text-xl">&times;</button>
            </div>

            <div class="p-6">
              <div class="border border-slate-200 rounded-xl p-5 space-y-4">
                <div class="grid grid-cols-3 gap-3">
                  <span class="text-slate-500 font-medium text-sm">Nama</span>
                  <span class="col-span-2 text-slate-800 font-bold uppercase text-sm">{{ userProfile?.full_name || '-' }}</span>
                </div>
                <div class="grid grid-cols-3 gap-3">
                  <span class="text-slate-500 font-medium text-sm">Jenis Kelamin</span>
                  <span class="col-span-2 text-slate-800 font-bold text-sm">{{ userProfile?.jenis_kelamin || 'Perempuan' }}</span>
                </div>
                <div class="grid grid-cols-3 gap-3">
                  <span class="text-slate-500 font-medium text-sm">Email</span>
                  <span class="col-span-2 text-slate-800 font-bold text-sm">{{ userProfile?.email || '-' }}</span>
                </div>
                <div class="grid grid-cols-3 gap-3">
                  <span class="text-slate-500 font-medium text-sm">No. Telp.</span>
                  <span class="col-span-2 text-slate-800 font-bold text-sm">{{ userProfile?.no_telp || '-' }}</span>
                </div>

                <hr class="border-slate-100" />

                <div class="grid grid-cols-3 gap-3">
                  <span class="text-slate-500 font-medium text-sm">NIM</span>
                  <span class="col-span-2 text-slate-800 font-bold text-sm">{{ userProfile?.nim_nip || '-' }}</span>
                </div>
                <div class="grid grid-cols-3 gap-3">
                  <span class="text-slate-500 font-medium text-sm">Program Studi</span>
                  <span class="col-span-2 text-slate-800 font-bold text-sm">S1 — {{ userProfile?.prodi || '-' }}</span>
                </div>
                <div class="grid grid-cols-3 gap-3">
                  <span class="text-slate-500 font-medium text-sm">Angkatan</span>
                  <span class="col-span-2 text-slate-800 font-bold text-sm">{{ userProfile?.angkatan || '2023' }}</span>
                </div>
              </div>
              
              <div class="mt-6 flex justify-center">
                <button @click="openUpdateModal" class="w-full max-w-sm py-3 bg-slate-50 text-slate-800 border border-slate-200 rounded-xl font-bold hover:bg-slate-100 transition shadow-sm active:scale-95 text-sm">
                  Perbarui Profil
                </button>
              </div>
            </div>
          </div>
        </div>
      </Transition>

      <!-- MODAL UPDATE PROFIL -->
      <Transition name="scale">
        <div v-if="isUpdateModalOpen" class="fixed inset-0 z-[110] flex items-center justify-center p-4">
          <div class="absolute inset-0 bg-slate-900/60 backdrop-blur-md" @click="isUpdateModalOpen = false"></div>
          <div class="relative bg-white w-full max-w-lg rounded-2xl shadow-2xl overflow-hidden border border-slate-200">
            <div class="p-5 border-b border-slate-100 flex justify-between items-center bg-white">
              <h3 class="text-lg font-bold text-slate-800">Perbarui Profil</h3>
              <button @click="isUpdateModalOpen = false" class="text-slate-400 hover:text-red-500 transition-colors text-xl">&times;</button>
            </div>
            
            <div class="p-6">
              <div class="bg-slate-50 p-3 rounded-xl flex items-start gap-2 mb-5">
                <span class="text-slate-400 mt-0.5 text-sm">ⓘ</span>
                <p class="text-[10px] text-slate-500 font-medium leading-relaxed">
                  Perubahan tidak mempengaruhi data di SIAKAD
                </p>
              </div>

              <div class="mb-6">
                <h4 class="text-base font-black text-slate-800 uppercase leading-none">{{ userProfile?.full_name }}</h4>
                <p class="text-[10px] font-bold text-slate-400 mt-1">{{ userProfile?.nim_nip }} — {{ userProfile?.prodi }}</p>
              </div>

              <div class="space-y-4">
                <div class="space-y-1.5">
                  <label class="text-[10px] font-black text-slate-400 uppercase tracking-widest ml-1">Email</label>
                  <input v-model="editForm.email" type="email" class="w-full p-3 bg-white border border-emerald-500 rounded-xl font-bold text-slate-800 text-sm shadow-sm focus:ring-4 focus:ring-emerald-50/50 outline-none transition-all" />
                </div>
                <div class="space-y-1.5">
                  <label class="text-[10px] font-black text-slate-400 uppercase tracking-widest ml-1">No. Telp.</label>
                  <input v-model="editForm.no_telp" type="text" class="w-full p-3 bg-white border border-emerald-500 rounded-xl font-bold text-slate-800 text-sm shadow-sm focus:ring-4 focus:ring-emerald-50/50 outline-none transition-all" />
                </div>
              </div>

              <div class="mt-6">
                <button @click="handleUpdateProfile" :disabled="updating" class="w-full py-3 bg-[#0f172a] text-white rounded-xl font-black hover:bg-blue-700 transition shadow-xl active:scale-95 disabled:opacity-50 uppercase tracking-widest text-xs">
                  {{ updating ? 'Menyimpan...' : 'Simpan Perubahan' }}
                </button>
              </div>
            </div>
          </div>
        </div>
      </Transition>

    </main>
  </div>
</template>

<script setup>
import { ref, onMounted, computed, watch } from "vue";
import { useRouter } from "vue-router";
import api from "../api/api";
// IMPORT LOGO
import logoStiesbi from "/src/assets/stie-sbilogo.jpg";

const router = useRouter();
const listPengajuan = ref([]);
const userProfile = ref(null);
const loading = ref(true);
const updating = ref(false);
const submitting = ref(false);

const isModalOpen = ref(false);
const isUpdateModalOpen = ref(false);
const isDetailOpen = ref(false);
const isEditPengajuanOpen = ref(false);
const selectedDetail = ref(null);
const showKategoriModal = ref(false);
const searchKategori = ref("");
const listKategori = ref([]);
const fileInput = ref(null);

// FILTER STATUS: 'all' atau 'rejected'
const filterStatus = ref("all");

// Data untuk edit pengajuan
const editPengajuanData = ref({});
const editPengajuanForm = ref({
  judul_kegiatan: "",
  kategori_id: null,
  kategori_name: "",
  tanggal_kegiatan: "",
  durasi_kegiatan: "",
  bukti_sertifikat_file: null,
  existing_file: ""
});

const editForm = ref({ 
  email: "",
  no_telp: "" 
});

const BASE_URL = "https://kreditpoin.pythonanywhere.com"; 

// STATE UNTUK PENCARIAN & PAGINASI
const searchRiwayat = ref("");
const currentPage = ref(1);
const itemsPerPage = ref(5);

// COMPUTED UNTUK STATS
const totalPoin = computed(() =>
  listPengajuan.value
    .filter((i) => i.status === "approved_final")
    .reduce((s, i) => s + (Number(i.poin_valid) || Number(i.bobot_poin_kategori) || 0), 0)
);
const pendingCount = computed(() => listPengajuan.value.filter((i) => i.status === "pending").length);
const approvedDpaCount = computed(() => listPengajuan.value.filter((i) => i.status === "approved_dpa" || i.status === "approved_final").length);
const rejectedCount = computed(() => listPengajuan.value.filter((i) => i.status === "rejected").length);

// COMPUTED UNTUK FILTER
const filteredRiwayat = computed(() => {
  let filtered = listPengajuan.value;
  
  if (filterStatus.value === 'rejected') {
    filtered = filtered.filter(item => item.status === 'rejected');
  }
  
  if (searchRiwayat.value) {
    const query = searchRiwayat.value.toLowerCase();
    filtered = filtered.filter(item => 
      (item.judul_kegiatan || '').toLowerCase().includes(query) ||
      (item.nama_kategori || '').toLowerCase().includes(query)
    );
  }
  
  return filtered;
});

watch([searchRiwayat, filterStatus], () => {
  currentPage.value = 1;
});

const totalPages = computed(() => Math.ceil(filteredRiwayat.value.length / itemsPerPage.value) || 1);
const paginatedRiwayat = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value;
  const end = start + itemsPerPage.value;
  return filteredRiwayat.value.slice(start, end);
});

const filteredKategoriList = computed(() => {
  if (!searchKategori.value) return listKategori.value;
  const q = searchKategori.value.toLowerCase();
  return listKategori.value.filter(k => 
    (k.nama_kegiatan || k.kegiatan || '').toLowerCase().includes(q) ||
    (k.bidang || '').toLowerCase().includes(q)
  );
});

const nextPage = () => {
  if (currentPage.value < totalPages.value) currentPage.value++;
};
const prevPage = () => {
  if (currentPage.value > 1) currentPage.value--;
};

const goToRejectedItems = () => {
  filterStatus.value = 'rejected';
  currentPage.value = 1;
  scrollToRiwayat();
};

const filterRejectedOnly = () => {
  filterStatus.value = 'rejected';
  currentPage.value = 1;
  scrollToRiwayat();
};

const resetFilter = () => {
  filterStatus.value = 'all';
  searchRiwayat.value = '';
  currentPage.value = 1;
  scrollToRiwayat();
};

// STATS CARDS
const statsCards = computed(() => [
  { label: "Total Poin", value: totalPoin.value, icon: "👤", bgColor: "bg-cyan-500 shadow-cyan-100" },
  { label: "Menunggu", value: pendingCount.value, icon: "🏫", bgColor: "bg-amber-400 shadow-amber-100" },
  { label: "Disetujui DPA", value: approvedDpaCount.value, icon: "👨‍🏫", bgColor: "bg-emerald-500 shadow-emerald-100" },
  { label: "Total Pengajuan", value: listPengajuan.value.length, icon: "🏆", bgColor: "bg-slate-700 shadow-slate-100" },
]);

const statusStyle = (status) => {
  switch (status) {
    case "approved_final": return "bg-emerald-50 text-emerald-600 border-emerald-100";
    case "approved_dpa": return "bg-blue-50 text-blue-600 border-blue-100";
    case "pending": return "bg-amber-50 text-amber-600 border-amber-100";
    case "rejected": return "bg-red-50 text-red-600 border-red-100";
    default: return "bg-slate-50 text-slate-500 border-slate-100";
  }
};

const formatStatusText = (status) => {
  const labels = {
    approved_final: "DISETUJUI",
    approved_dpa: "DPA ACC",
    pending: "MENUNGGU",
    rejected: "DITOLAK / REVISI",
  };
  return labels[status] || status?.toUpperCase() || "UNKNOWN";
};

const getSertifikatUrl = (path) => {
  if (!path) return "#";
  if (path.startsWith("http")) return path;
  return `${BASE_URL}${path.startsWith('/') ? '' : '/'}${path}`;
};

// FETCH DATA
const fetchData = async () => {
  try {
    loading.value = true;
    const token = localStorage.getItem("access_token");
    if (!token) { router.push("/login"); return; }

    const [reqProfile, reqKegiatan, reqKategori] = await Promise.all([
      api.get("api/users/me/"),
      api.get("api/kegiatan/"),
      api.get("api/kategori/").catch(() => [])
    ]);
    userProfile.value = reqProfile.data;
    listPengajuan.value = reqKegiatan.data;
    listKategori.value = reqKategori.data || [];
    
    editForm.value.email = reqProfile.data.email;
    editForm.value.no_telp = reqProfile.data.no_telp;
  } catch (err) {
    console.error(err);
    if (err.response?.status === 401) router.push("/login");
  } finally {
    loading.value = false;
  }
};

// DETAIL & EDIT MODAL
const openDetail = (item) => {
  selectedDetail.value = item;
  isDetailOpen.value = true;
};

const openEditPengajuan = (item) => {
  editPengajuanData.value = { ...item };
  editPengajuanForm.value = {
    judul_kegiatan: item.judul_kegiatan || "",
    kategori_id: item.kategori || item.kategori_id,
    kategori_name: item.nama_kategori || "",
    tanggal_kegiatan: item.tanggal_kegiatan || "",
    durasi_kegiatan: item.durasi_kegiatan || "",
    bukti_sertifikat_file: null,
    existing_file: item.bukti_sertifikat || ""
  };
  isEditPengajuanOpen.value = true;
};

const openKategoriModalForEdit = () => {
  showKategoriModal.value = true;
};

const selectKategori = (kat) => {
  editPengajuanForm.value.kategori_id = kat.id;
  editPengajuanForm.value.kategori_name = kat.nama_kegiatan || kat.kegiatan;
  showKategoriModal.value = false;
  searchKategori.value = "";
};

const triggerFileInput = () => {
  fileInput.value?.click();
};

const handleFileUpload = (event) => {
  const file = event.target.files[0];
  if (file) {
    const allowedTypes = ['application/pdf', 'image/jpeg', 'image/jpg', 'image/png'];
    if (!allowedTypes.includes(file.type)) {
      alert("Hanya file PDF, JPG, atau PNG yang diperbolehkan!");
      return;
    }
    if (file.size > 5 * 1024 * 1024) {
      alert("Ukuran file maksimal 5MB!");
      return;
    }
    editPengajuanForm.value.bukti_sertifikat_file = file;
  }
};

const removeFile = () => {
  editPengajuanForm.value.bukti_sertifikat_file = null;
  if (fileInput.value) fileInput.value.value = "";
};

const submitEditPengajuan = async () => {
  if (!editPengajuanForm.value.judul_kegiatan.trim()) {
    alert("Judul kegiatan harus diisi!");
    return;
  }
  if (!editPengajuanForm.value.kategori_id) {
    alert("Pilih kategori kegiatan!");
    return;
  }
  if (!editPengajuanForm.value.tanggal_kegiatan) {
    alert("Tanggal pelaksanaan harus diisi!");
    return;
  }

  submitting.value = true;
  
  try {
    const formData = new FormData();
    formData.append("judul_kegiatan", editPengajuanForm.value.judul_kegiatan);
    formData.append("kategori_id", editPengajuanForm.value.kategori_id);
    formData.append("tanggal_kegiatan", editPengajuanForm.value.tanggal_kegiatan);
    formData.append("durasi_kegiatan", editPengajuanForm.value.durasi_kegiatan || "-");
    formData.append("status", "pending");
    formData.append("komentar_dpa", "");
    formData.append("is_edited_by_dpa", false);
    
    if (editPengajuanForm.value.bukti_sertifikat_file) {
      formData.append("bukti_sertifikat", editPengajuanForm.value.bukti_sertifikat_file);
    }

    const response = await api.patch(`api/kegiatan/${editPengajuanData.value.id}/`, formData, {
      headers: { "Content-Type": "multipart/form-data" }
    });
    
    if (response.status === 200 || response.status === 201) {
      alert("✅ Pengajuan berhasil diperbarui dan diajukan ulang!");
      isEditPengajuanOpen.value = false;
      await fetchData();
    }
    
  } catch (err) {
    console.error("Error:", err);
    
    if (err.response?.status === 403) {
      alert("❌ Anda tidak memiliki izin untuk mengubah data ini.");
    } else if (err.response?.status === 400) {
      const errorData = err.response.data;
      let errorMessage = "Gagal menyimpan perubahan:\n";
      if (typeof errorData === 'object') {
        for (const [key, value] of Object.entries(errorData)) {
          errorMessage += `• ${key}: ${Array.isArray(value) ? value.join(', ') : value}\n`;
        }
      } else {
        errorMessage += errorData;
      }
      alert(errorMessage);
    } else {
      alert("❌ Gagal menyimpan perubahan. Silakan coba lagi.");
    }
  } finally {
    submitting.value = false;
  }
};

const openEditModal = () => {
  isModalOpen.value = true;
};

const openUpdateModal = () => {
  isModalOpen.value = false;
  isUpdateModalOpen.value = true;
};

const handleUpdateProfile = async () => {
  try {
    updating.value = true;
    await api.patch("api/users/me/", editForm.value);
    alert("Profil berhasil diperbarui!");
    isUpdateModalOpen.value = false;
    fetchData(); 
  } catch (err) {
    alert("Gagal memperbarui profil: " + (err.response?.data?.message || err.message));
  } finally {
    updating.value = false;
  }
};

const handleLogout = () => {
  if (confirm("Apakah Anda yakin ingin keluar?")) {
    localStorage.clear();
    router.push("/login");
  }
};

const scrollToRiwayat = () => {
  document.getElementById("riwayat-section")?.scrollIntoView({ behavior: "smooth" });
};

onMounted(fetchData);
</script>

<style scoped>
.scale-enter-active, .scale-leave-active {
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}
.scale-enter-from, .scale-leave-to {
  opacity: 0;
  transform: scale(0.9) translateY(20px);
}

.custom-scroll::-webkit-scrollbar {
  width: 6px;
}
.custom-scroll::-webkit-scrollbar-track {
  background: #f1f5f9;
}
.custom-scroll::-webkit-scrollbar-thumb {
  background: #cbd5e1;
  border-radius: 10px;
}
.custom-scroll::-webkit-scrollbar-thumb:hover {
  background: #94a3b8;
}

::-webkit-scrollbar {
  width: 8px;
}
::-webkit-scrollbar-track {
  background: #f1f5f9;
}
::-webkit-scrollbar-thumb {
  background: #cbd5e1;
  border-radius: 10px;
}
</style>