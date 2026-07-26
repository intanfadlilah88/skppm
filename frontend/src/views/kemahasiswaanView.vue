<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-50 via-indigo-50/20 to-slate-50 flex font-sans selection:bg-indigo-100 selection:text-indigo-900 overflow-hidden">
    <!-- SIDEBAR - FIXED POSITION -->
    <aside class="w-72 bg-[#1e293b] text-white hidden md:flex flex-col fixed top-0 left-0 bottom-0 h-screen">
      <!-- HEADER SIDEBAR -->
      <div class="p-4 lg:p-5 flex items-center gap-3 border-b border-white/10 flex-shrink-0 bg-gradient-to-b from-slate-800 to-slate-900">
        <div class="h-10 w-10 lg:h-11 lg:w-11 bg-white rounded-xl flex items-center justify-center shadow-lg overflow-hidden flex-shrink-0">
          <img 
            src="/stie-sbilogo.jpg" 
            alt="STIE SBI Logo" 
            class="h-full w-full object-cover"
            @error="(e) => e.target.src = ''"
          />
        </div>
        <div class="flex flex-col min-w-0">
          <span class="font-bold text-sm lg:text-base tracking-tight truncate">SKPM Kemahasiswaan</span>
          <span class="text-[10px] lg:text-xs text-indigo-300 truncate">STIE SBI Yogyakarta</span>
        </div>
      </div>

      <!-- NAVIGASI -->
      <nav class="flex-1 p-3 lg:p-4 space-y-1 overflow-y-auto custom-scroll bg-gradient-to-b from-slate-800 to-slate-900">
        <button class="w-full flex items-center gap-3 px-4 py-2.5 lg:py-3 bg-indigo-600 rounded-xl text-white shadow-lg shadow-indigo-600/30 transition-all duration-200 text-sm">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 lg:h-5 lg:w-5 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
          </svg>
          <span class="font-semibold text-xs lg:text-sm truncate">Dashboard Monitoring</span>
        </button>
      </nav>

      <!-- FOOTER SIDEBAR -->
      <div class="p-3 lg:p-4 border-t border-white/10 bg-gradient-to-b from-slate-800 to-slate-900 flex-shrink-0">
        <div class="text-[10px] text-slate-500 text-center">
          <p>Sistem Kredit Poin Prestasi Mahasiswa</p>
          <p class="mt-0.5">STIE SBI Yogyakarta</p>
        </div>
      </div>
    </aside>

    <!-- MAIN CONTENT - dengan margin kiri untuk sidebar -->
    <main class="flex-1 ml-72 p-4 sm:p-5 md:p-6 lg:p-8 xl:p-10 overflow-y-auto h-screen">
      <!-- HEADER DENGAN TOMBOL LOGOUT -->
      <div class="mb-6 lg:mb-8">
        <div class="bg-gradient-to-r from-indigo-600 via-indigo-700 to-indigo-800 rounded-2xl lg:rounded-3xl p-5 md:p-6 lg:p-8 text-white shadow-2xl shadow-indigo-200/30 relative overflow-hidden">
          <div class="absolute top-0 right-0 w-48 md:w-64 h-48 md:h-64 bg-white/5 rounded-full -mr-24 -mt-24"></div>
          <div class="absolute bottom-0 left-0 w-36 md:w-48 h-36 md:h-48 bg-white/5 rounded-full -ml-18 -mb-18"></div>
          
          <div class="relative z-10 flex flex-col md:flex-row justify-between items-start md:items-center gap-4 md:gap-6">
            <div class="min-w-0">
              <div class="flex items-center gap-2 md:gap-3 mb-1 md:mb-2">
                <div class="h-9 w-9 md:h-10 md:w-10 lg:h-11 lg:w-11 bg-white/20 rounded-xl flex items-center justify-center backdrop-blur-sm flex-shrink-0">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 md:h-5 md:w-5 lg:h-6 lg:w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
                  </svg>
                </div>
                <div class="min-w-0">
                  <h1 class="text-base sm:text-lg md:text-xl lg:text-2xl xl:text-3xl font-black tracking-tight truncate">Dashboard Monitoring Kemahasiswaan</h1>
                  <p class="text-indigo-200 text-[10px] sm:text-xs md:text-sm truncate">Monitoring dan verifikasi berkas mahasiswa</p>
                </div>
              </div>
            </div>
            
            <!-- TOMBOL LOGOUT DI SAMPING KANAN -->
            <button 
              @click="logout"
              class="flex items-center gap-2 bg-white/20 hover:bg-white/30 backdrop-blur-sm px-4 md:px-6 py-2 md:py-2.5 rounded-xl transition-all duration-200 font-bold text-sm shadow-lg flex-shrink-0"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 md:h-5 md:w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
              </svg>
              <span>Logout</span>
            </button>
          </div>
        </div>
      </div>

      <!-- STATS CARDS -->
      <div class="grid grid-cols-2 lg:grid-cols-4 gap-3 md:gap-4 lg:gap-5 mb-6 lg:mb-8">
        <div class="group bg-white p-4 md:p-5 rounded-xl md:rounded-2xl shadow-sm hover:shadow-xl transition-all duration-300 border border-slate-100 hover:border-indigo-200 relative overflow-hidden">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-slate-500 text-[8px] md:text-[10px] font-black uppercase tracking-wider mb-0.5">Total Mahasiswa</p>
              <h4 class="text-xl md:text-2xl font-black text-slate-800">{{ stats.total_mahasiswa }} <span class="text-xs md:text-sm font-medium text-slate-400">Orang</span></h4>
            </div>
            <div class="h-10 w-10 md:h-11 md:w-11 lg:h-12 lg:w-12 bg-gradient-to-br from-blue-500 to-blue-600 rounded-xl flex items-center justify-center shadow-lg shadow-blue-200 group-hover:scale-110 transition-transform flex-shrink-0">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 md:h-6 md:w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
              </svg>
            </div>
          </div>
        </div>

        <div class="group bg-white p-4 md:p-5 rounded-xl md:rounded-2xl shadow-sm hover:shadow-xl transition-all duration-300 border border-slate-100 hover:border-amber-200 relative overflow-hidden">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-slate-500 text-[8px] md:text-[10px] font-black uppercase tracking-wider mb-0.5">Pengajuan Pending</p>
              <h4 class="text-xl md:text-2xl font-black text-slate-800">{{ stats.total_pending }} <span class="text-xs md:text-sm font-medium text-slate-400">Berkas</span></h4>
            </div>
            <div class="h-10 w-10 md:h-11 md:w-11 lg:h-12 lg:w-12 bg-gradient-to-br from-amber-500 to-amber-600 rounded-xl flex items-center justify-center shadow-lg shadow-amber-200 group-hover:scale-110 transition-transform flex-shrink-0">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 md:h-6 md:w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
          </div>
        </div>

        <div class="group bg-white p-4 md:p-5 rounded-xl md:rounded-2xl shadow-sm hover:shadow-xl transition-all duration-300 border border-slate-100 hover:border-emerald-200 relative overflow-hidden">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-slate-500 text-[8px] md:text-[10px] font-black uppercase tracking-wider mb-0.5">Berkas Valid</p>
              <h4 class="text-xl md:text-2xl font-black text-slate-800">{{ stats.total_valid }} <span class="text-xs md:text-sm font-medium text-slate-400">Berkas</span></h4>
            </div>
            <div class="h-10 w-10 md:h-11 md:w-11 lg:h-12 lg:w-12 bg-gradient-to-br from-emerald-500 to-emerald-600 rounded-xl flex items-center justify-center shadow-lg shadow-emerald-200 group-hover:scale-110 transition-transform flex-shrink-0">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 md:h-6 md:w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
          </div>
        </div>

        <div class="group bg-white p-4 md:p-5 rounded-xl md:rounded-2xl shadow-sm hover:shadow-xl transition-all duration-300 border border-slate-100 hover:border-rose-200 relative overflow-hidden">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-slate-500 text-[8px] md:text-[10px] font-black uppercase tracking-wider mb-0.5">Berkas Ditolak</p>
              <h4 class="text-xl md:text-2xl font-black text-slate-800">{{ stats.total_tolak }} <span class="text-xs md:text-sm font-medium text-slate-400">Berkas</span></h4>
            </div>
            <div class="h-10 w-10 md:h-11 md:w-11 lg:h-12 lg:w-12 bg-gradient-to-br from-rose-500 to-rose-600 rounded-xl flex items-center justify-center shadow-lg shadow-rose-200 group-hover:scale-110 transition-transform flex-shrink-0">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 md:h-6 md:w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
          </div>
        </div>
      </div>

      <!-- ALERT INFO + TOMBOL ACTION SEJAJAR -->
      <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-3 md:gap-4 mb-6 lg:mb-8">
        <div v-if="stats.total_pending > 0" class="flex-1 w-full bg-gradient-to-r from-amber-50 to-amber-100/50 rounded-xl lg:rounded-2xl border-l-4 border-amber-500 p-3 md:p-4 lg:p-5 flex items-center gap-3 md:gap-4">
          <div class="h-8 w-8 md:h-9 md:w-9 lg:h-10 lg:w-10 bg-amber-500 rounded-xl flex items-center justify-center shadow-md flex-shrink-0">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 md:h-5 md:w-5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
            </svg>
          </div>
          <div class="min-w-0">
            <p class="font-bold text-amber-800 text-sm md:text-base">Pemberitahuan</p>
            <p class="text-xs md:text-sm text-amber-700 truncate">Terdapat <b>{{ stats.total_pending }}</b> pengajuan yang perlu diverifikasi.</p>
          </div>
        </div>
        <div v-else class="flex-1 w-full"></div>

        <div class="flex flex-wrap gap-3 flex-shrink-0">
          <button 
            @click="exportToExcel" 
            class="bg-green-600 hover:bg-green-700 text-white px-4 md:px-6 py-2 md:py-2.5 rounded-xl transition-all duration-200 font-bold text-xs md:text-sm shadow-md flex items-center gap-2"
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
            </svg>
            Export Excel
          </button>
          
          <button 
            @click="refreshData" 
            :disabled="isLoading"
            class="bg-indigo-500 hover:bg-indigo-600 text-white px-4 md:px-6 py-2 md:py-2.5 rounded-xl transition-all duration-200 font-bold text-xs md:text-sm shadow-md flex items-center gap-2"
          >
            <span :class="{'animate-spin': isLoading}">🔄</span>
            {{ isLoading ? 'Memuat...' : 'Refresh Data' }}
          </button>
        </div>
      </div>

      <!-- TABEL DATA -->
      <div class="bg-white rounded-xl md:rounded-2xl shadow-lg border border-slate-200 overflow-hidden">
        <div class="p-4 md:p-5 lg:p-6 border-b border-slate-200 bg-gradient-to-r from-slate-50 to-white">
          <h2 class="text-sm md:text-base lg:text-lg font-bold text-slate-800 flex items-center gap-2 md:gap-3">
            <div class="h-1.5 w-1.5 md:h-2 md:w-2 bg-indigo-500 rounded-full animate-pulse flex-shrink-0"></div>
            <span>📋 Monitoring Berkas Mahasiswa</span>
            <span class="ml-auto text-xs text-slate-400 font-medium">{{ filteredKegiatan.length }} Data</span>
          </h2>
        </div>

        <!-- SEARCH -->
        <div class="p-4 border-b border-slate-200 bg-white">
          <div class="relative w-full md:w-80">
            <div class="absolute inset-y-0 left-3 md:left-4 flex items-center pointer-events-none">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 md:h-5 md:w-5 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
            </div>
            <input 
              v-model="searchQuery" 
              type="text" 
              placeholder="Cari NIM, Nama, atau Judul..." 
              class="w-full pl-9 md:pl-11 pr-3 md:pr-4 py-2 md:py-2.5 bg-white border-2 border-slate-200 rounded-xl text-xs md:text-sm font-medium text-slate-700 focus:border-indigo-500 focus:ring-0 outline-none transition-all" 
            />
          </div>
        </div>

        <div class="overflow-x-auto">
          <table class="w-full min-w-[800px]">
            <thead class="bg-slate-100/80 border-b-2 border-slate-200">
              <tr>
                <th class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 text-left text-[8px] md:text-[10px] lg:text-xs font-bold text-slate-500 uppercase tracking-wider">No</th>
                <th class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 text-left text-[8px] md:text-[10px] lg:text-xs font-bold text-slate-500 uppercase tracking-wider">NIM</th>
                <th class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 text-left text-[8px] md:text-[10px] lg:text-xs font-bold text-slate-500 uppercase tracking-wider">Nama Mahasiswa</th>
                <th class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 text-left text-[8px] md:text-[10px] lg:text-xs font-bold text-slate-500 uppercase tracking-wider">Prodi</th>
                <th class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 text-left text-[8px] md:text-[10px] lg:text-xs font-bold text-slate-500 uppercase tracking-wider">Judul Kegiatan</th>
                <th class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 text-left text-[8px] md:text-[10px] lg:text-xs font-bold text-slate-500 uppercase tracking-wider">Tgl Pelaksanaan</th>
                <th class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 text-left text-[8px] md:text-[10px] lg:text-xs font-bold text-slate-500 uppercase tracking-wider">Status</th>
                <th class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 text-center text-[8px] md:text-[10px] lg:text-xs font-bold text-slate-500 uppercase tracking-wider">Total Poin</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100">
              <tr v-for="(item, index) in paginatedData" :key="item.id" class="hover:bg-indigo-50/40 transition-colors group">
                <td class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 text-xs md:text-sm font-bold text-slate-500">{{ (currentPage - 1) * itemsPerPage + index + 1 }}</td>
                <td class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 font-mono text-xs md:text-sm font-bold text-slate-700">{{ item.nim || '-' }}</td>
                <td class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4">
                  <div class="flex items-center gap-2 md:gap-3">
                    <div class="h-8 w-8 md:h-9 md:w-9 lg:h-10 lg:w-10 bg-gradient-to-br from-indigo-100 to-indigo-200 rounded-xl flex items-center justify-center font-bold text-indigo-600 text-xs md:text-sm flex-shrink-0">
                      {{ (item.mahasiswa_nama || 'M').charAt(0).toUpperCase() }}
                    </div>
                    <span class="font-bold text-slate-800 group-hover:text-indigo-600 transition-colors text-xs md:text-sm truncate">{{ item.mahasiswa_nama || '-' }}</span>
                  </div>
                </td>
                <td class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 text-xs md:text-sm text-slate-700">{{ item.prodi || '-' }}</td>
                <td class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 text-xs md:text-sm text-slate-700 max-w-[120px] md:max-w-[200px] lg:max-w-xs truncate">{{ item.judul_kegiatan || '-' }}</td>
                <td class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 text-xs md:text-sm text-slate-700">{{ formatDate(item.tanggal_kegiatan) }}</td>
                <td class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4">
                  <span :class="getStatusClass(item.status)" class="px-2 md:px-3 py-1 md:py-1.5 rounded-full text-[8px] md:text-[10px] lg:text-xs font-bold">
                    {{ formatStatus(item.status) }}
                  </span>
                </td>
                <td class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 text-center">
                  <div class="inline-flex items-center gap-1 px-3 md:px-4 py-1.5 md:py-2 bg-gradient-to-br from-blue-50 to-indigo-50 rounded-xl border border-blue-100">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 md:h-4 md:w-4 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
                    </svg>
                    <span class="font-black text-blue-600 text-sm md:text-base">{{ hitungTotalPoin(item.nim) }}</span>
                  </div>
                </td>
              </tr>
              <tr v-if="paginatedData.length === 0 && !isLoading">
                <td colspan="8" class="px-3 md:px-6 py-8 md:py-12 lg:py-16 text-center">
                  <div class="text-4xl md:text-5xl lg:text-6xl mb-2 md:mb-4 opacity-40">📭</div>
                  <p class="text-slate-500 font-semibold text-xs md:text-sm lg:text-base">Tidak ada data berkas ditemukan</p>
                  <p class="text-slate-400 text-[10px] md:text-xs mt-1">Silakan tambah data pengajuan terlebih dahulu</p>
                </td>
              </tr>
              <tr v-if="isLoading">
                <td colspan="8" class="px-3 md:px-6 py-8 md:py-12 lg:py-16 text-center">
                  <div class="flex justify-center items-center gap-2">
                    <div class="w-5 h-5 md:w-6 md:h-6 border-3 border-indigo-500 border-t-transparent rounded-full animate-spin"></div>
                    <p class="text-slate-500 font-semibold text-xs md:text-sm">Memuat data...</p>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- PAGINATION -->
        <div v-if="filteredKegiatan.length > 0" class="p-3 md:p-4 lg:p-5 border-t border-slate-200 flex flex-col sm:flex-row justify-between items-center gap-3 md:gap-4 bg-slate-50/80">
          <span class="text-[10px] md:text-xs lg:text-sm text-slate-500">
            Menampilkan <strong class="text-slate-700">{{ (currentPage - 1) * itemsPerPage + 1 }}</strong> - 
            <strong class="text-slate-700">{{ Math.min(currentPage * itemsPerPage, filteredKegiatan.length) }}</strong> 
            dari <strong class="text-slate-700">{{ filteredKegiatan.length }}</strong> data
          </span>
          <div class="flex gap-1.5 md:gap-2">
            <button 
              @click="prevPage" 
              :disabled="currentPage === 1"
              class="px-3 md:px-4 py-1.5 md:py-2 bg-white border border-slate-200 rounded-lg text-[10px] md:text-xs lg:text-sm font-semibold text-slate-600 hover:bg-indigo-50 hover:text-indigo-600 hover:border-indigo-200 disabled:opacity-50 disabled:cursor-not-allowed transition-all"
            >
              ← Sebelumnya
            </button>
            <div class="flex gap-0.5 md:gap-1">
              <button 
                v-for="page in totalPages" 
                :key="page"
                @click="goToPage(page)"
                :class="[
                  'w-7 h-7 md:w-8 md:h-8 lg:w-9 lg:h-9 rounded-lg text-[10px] md:text-xs lg:text-sm font-semibold transition-all',
                  currentPage === page 
                    ? 'bg-indigo-600 text-white shadow-md' 
                    : 'bg-white border border-slate-200 text-slate-600 hover:bg-indigo-50'
                ]"
              >
                {{ page }}
              </button>
            </div>
            <button 
              @click="nextPage" 
              :disabled="currentPage === totalPages"
              class="px-3 md:px-4 py-1.5 md:py-2 bg-white border border-slate-200 rounded-lg text-[10px] md:text-xs lg:text-sm font-semibold text-slate-600 hover:bg-indigo-50 hover:text-indigo-600 hover:border-indigo-200 disabled:opacity-50 disabled:cursor-not-allowed transition-all"
            >
              Selanjutnya →
            </button>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted, computed, watch } from 'vue';
import { useRouter } from 'vue-router';
import api from '../api/api';
import * as XLSX from 'xlsx';

const router = useRouter();

// State data
const isLoading = ref(true);
const stats = ref({
  total_mahasiswa: 0,
  total_pending: 0,
  total_valid: 0,
  total_tolak: 0
});
const kegiatanList = ref([]);
const searchQuery = ref('');

// Pagination
const currentPage = ref(1);
const itemsPerPage = ref(5);

// Fungsi menghitung total poin per mahasiswa (hanya status yang disetujui)
const hitungTotalPoin = (nim) => {
  if (!nim) return 0;
  const kegiatanMahasiswa = kegiatanList.value.filter(item => item.nim === nim);
  let totalPoin = 0;
  kegiatanMahasiswa.forEach(item => {
    // Hanya status yang disetujui yang mendapat poin
    if (item.status === 'approved_final' || item.status === 'valid' || item.status === 'disetujui') {
      totalPoin += Number(item.bobot_poin_kategori || item.bobot_poin || 0);
    }
  });
  return totalPoin;
};

// Computed untuk mendapatkan total poin per NIM (digunakan di export)
const totalPoinPerNIM = computed(() => {
  const map = {};
  kegiatanList.value.forEach(item => {
    const nim = item.nim;
    if (!map[nim]) map[nim] = 0;
    if (item.status === 'approved_final' || item.status === 'valid' || item.status === 'disetujui') {
      map[nim] += Number(item.bobot_poin_kategori || item.bobot_poin || 0);
    }
  });
  return map;
});

// Computed untuk pencarian
const filteredKegiatan = computed(() => {
  if (!searchQuery.value) return kegiatanList.value;
  const q = searchQuery.value.toLowerCase();
  return kegiatanList.value.filter(item => 
    (item.nim && item.nim.toLowerCase().includes(q)) || 
    (item.mahasiswa_nama && item.mahasiswa_nama.toLowerCase().includes(q)) ||
    (item.judul_kegiatan && item.judul_kegiatan.toLowerCase().includes(q)) ||
    (item.prodi && item.prodi.toLowerCase().includes(q))
  );
});

// Computed untuk pagination
const totalPages = computed(() => Math.ceil(filteredKegiatan.value.length / itemsPerPage.value) || 1);

const paginatedData = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value;
  const end = start + itemsPerPage.value;
  return filteredKegiatan.value.slice(start, end);
});

// Reset page when search changes
watch(searchQuery, () => {
  currentPage.value = 1;
});

// Pagination functions
const prevPage = () => {
  if (currentPage.value > 1) currentPage.value--;
};

const nextPage = () => {
  if (currentPage.value < totalPages.value) currentPage.value++;
};

const goToPage = (page) => {
  currentPage.value = page;
};

// Fungsi mengambil data dashboard
const fetchDashboardData = async () => {
  try {
    const response = await api.get('/api/kemahasiswaan/dashboard/');
    if (response.data && response.data.stats) {
      stats.value = {
        total_mahasiswa: response.data.stats.total_mahasiswa || 0,
        total_pending: response.data.stats.total_pending || 0,
        total_valid: response.data.stats.total_valid || 0,
        total_tolak: response.data.stats.total_tolak || 0
      };
      return true;
    }
    return false;
  } catch (error) {
    console.error("Gagal mengambil data statistik:", error);
    return false;
  }
};

// Fungsi mengambil list kegiatan
const fetchKegiatan = async () => {
  try {
    const response = await api.get('/api/kemahasiswaan/kegiatan/');
    if (response.data && Array.isArray(response.data)) {
      kegiatanList.value = response.data.map(item => ({
        id: item.id,
        nim: item.nim || '-',
        mahasiswa_nama: item.mahasiswa_nama || '-',
        prodi: item.prodi || '-',
        judul_kegiatan: item.judul_kegiatan || '-',
        status: item.status || 'pending',
        bukti_sertifikat: item.bukti_sertifikat || null,
        tanggal_kegiatan: item.tanggal_pelaksanaan || null,
        durasi_kegiatan: item.durasi || '-',
        created_at: item.created_at || null,
        bobot_poin_kategori: item.bobot_poin_kategori || 0,
        bobot_poin: item.bobot_poin || 0
      }));
      return true;
    }
    return false;
  } catch (error) {
    console.error("Gagal mengambil data kegiatan:", error);
    return false;
  }
};

// Fungsi untuk memuat data
const loadData = async () => {
  isLoading.value = true;
  const token = localStorage.getItem('access_token');
  if (!token) {
    router.push('/login');
    return;
  }
  api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  await Promise.all([fetchDashboardData(), fetchKegiatan()]);
  isLoading.value = false;
};

// Refresh data
const refreshData = () => {
  currentPage.value = 1;
  loadData();
};

// Format tanggal
const formatDate = (date) => {
  if (!date) return '-';
  try {
    const d = new Date(date);
    if (isNaN(d.getTime())) return '-';
    return d.toLocaleDateString('id-ID', {
      day: '2-digit',
      month: 'long',
      year: 'numeric'
    });
  } catch (e) {
    return '-';
  }
};

// Export ke Excel - FIXED
const exportToExcel = () => {
  if (filteredKegiatan.value.length === 0) {
    alert('Tidak ada data untuk diexport');
    return;
  }

  // Buat data export dengan total poin yang benar
  const excelData = filteredKegiatan.value.map((item, index) => ({
    'No': (currentPage.value - 1) * itemsPerPage.value + index + 1,
    'NIM': item.nim || '-',
    'Nama Mahasiswa': item.mahasiswa_nama || '-',
    'Program Studi': item.prodi || '-',
    'Judul Kegiatan': item.judul_kegiatan || '-',
    'Tanggal Pelaksanaan': formatDate(item.tanggal_kegiatan),
    'Durasi': item.durasi_kegiatan || '-',
    'Status': formatStatus(item.status),
    'Bobot Poin': item.bobot_poin_kategori || item.bobot_poin || 0,
    'Total Poin Mahasiswa': totalPoinPerNIM.value[item.nim] || 0
  }));

  // Data summary
  const summaryData = [
    { 'No': '', 'NIM': '', 'Nama Mahasiswa': '', 'Program Studi': '', 'Judul Kegiatan': '', 'Tanggal Pelaksanaan': '', 'Durasi': '', 'Status': '', 'Bobot Poin': '', 'Total Poin Mahasiswa': '' },
    { 'No': '📊 SUMMARY', 'NIM': '', 'Nama Mahasiswa': '', 'Program Studi': '', 'Judul Kegiatan': '', 'Tanggal Pelaksanaan': '', 'Durasi': '', 'Status': '', 'Bobot Poin': '', 'Total Poin Mahasiswa': '' },
    { 'No': 'Total Mahasiswa:', 'NIM': stats.value.total_mahasiswa.toString(), 'Nama Mahasiswa': '', 'Program Studi': '', 'Judul Kegiatan': '', 'Tanggal Pelaksanaan': '', 'Durasi': '', 'Status': '', 'Bobot Poin': '', 'Total Poin Mahasiswa': '' },
    { 'No': 'Pengajuan Pending:', 'NIM': stats.value.total_pending.toString(), 'Nama Mahasiswa': '', 'Program Studi': '', 'Judul Kegiatan': '', 'Tanggal Pelaksanaan': '', 'Durasi': '', 'Status': '', 'Bobot Poin': '', 'Total Poin Mahasiswa': '' },
    { 'No': 'Berkas Valid:', 'NIM': stats.value.total_valid.toString(), 'Nama Mahasiswa': '', 'Program Studi': '', 'Judul Kegiatan': '', 'Tanggal Pelaksanaan': '', 'Durasi': '', 'Status': '', 'Bobot Poin': '', 'Total Poin Mahasiswa': '' },
    { 'No': 'Berkas Ditolak:', 'NIM': stats.value.total_tolak.toString(), 'Nama Mahasiswa': '', 'Program Studi': '', 'Judul Kegiatan': '', 'Tanggal Pelaksanaan': '', 'Durasi': '', 'Status': '', 'Bobot Poin': '', 'Total Poin Mahasiswa': '' }
  ];

  const finalData = [...excelData, ...summaryData];
  const ws = XLSX.utils.json_to_sheet(finalData);
  ws['!cols'] = [
    { wch: 8 }, { wch: 15 }, { wch: 25 }, { wch: 15 }, 
    { wch: 40 }, { wch: 20 }, { wch: 10 }, { wch: 15 },
    { wch: 12 }, { wch: 18 }
  ];

  const wb = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(wb, ws, 'Monitoring Kemahasiswaan');
  const fileName = `Monitoring_Kemahasiswaan_${new Date().toISOString().slice(0, 19).replace(/:/g, '-')}.xlsx`;
  XLSX.writeFile(wb, fileName);
  alert('✅ Data berhasil diexport ke Excel!');
};

// Logout
const logout = () => {
  localStorage.removeItem('access_token');
  localStorage.removeItem('refresh_token');
  localStorage.removeItem('user_role');
  router.push('/login');
};

// Helper status
const getStatusClass = (status) => {
  const statusMap = {
    'pending': 'bg-amber-100 text-amber-800',
    'approved_final': 'bg-emerald-100 text-emerald-800',
    'rejected': 'bg-rose-100 text-rose-800',
    'revisi': 'bg-orange-100 text-orange-800',
    'valid': 'bg-emerald-100 text-emerald-800',
    'disetujui': 'bg-emerald-100 text-emerald-800'
  };
  return statusMap[status] || 'bg-gray-100 text-gray-800';
};

const formatStatus = (status) => {
  const statusMap = {
    'pending': 'PENDING',
    'approved_final': 'DISETUJUI FINAL',
    'rejected': 'DITOLAK',
    'revisi': 'REVISI',
    'valid': 'VALID',
    'disetujui': 'DISETUJUI'
  };
  return statusMap[status] || (status || 'UNKNOWN').toUpperCase();
};

// Lifecycle
onMounted(() => {
  const token = localStorage.getItem('access_token');
  const role = localStorage.getItem('user_role');
  
  if (!token || role !== 'kemahasiswaan') {
    router.push('/login');
    return;
  }
  
  api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  loadData();
});
</script>

<style scoped>
/* Custom scroll untuk sidebar */
.custom-scroll::-webkit-scrollbar { 
  width: 4px; 
}
.custom-scroll::-webkit-scrollbar-track { 
  background: transparent; 
}
.custom-scroll::-webkit-scrollbar-thumb { 
  background: #475569; 
  border-radius: 10px; 
}
.custom-scroll::-webkit-scrollbar-thumb:hover { 
  background: #1e293b; 
}

/* Animasi spin */
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
.animate-spin { 
  animation: spin 1s linear infinite; 
}

/* Scroll untuk main content */
::-webkit-scrollbar { 
  width: 6px; 
  height: 6px; 
}
::-webkit-scrollbar-track { 
  background: #f1f5f9; 
  border-radius: 10px; 
}
::-webkit-scrollbar-thumb { 
  background: #94a3b8; 
  border-radius: 10px; 
}
::-webkit-scrollbar-thumb:hover { 
  background: #64748b; 
}
</style>