<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-50 via-indigo-50/20 to-slate-50 flex font-sans selection:bg-indigo-100 selection:text-indigo-900">
    <!-- SIDEBAR -->
    <aside class="w-72 bg-[#1e293b] text-white hidden md:flex flex-col">
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
          <span class="font-bold text-sm lg:text-base tracking-tight truncate">SKPPM DPA</span>
          <span class="text-[10px] lg:text-xs text-indigo-300 truncate">STIE SBI Yogyakarta</span>
        </div>
      </div>

      <!-- NAVIGASI -->
      <nav class="flex-1 p-3 lg:p-4 space-y-1 overflow-y-auto custom-scroll bg-gradient-to-b from-slate-800 to-slate-900">
        <button @click="resetFilter" :class="['w-full flex items-center gap-3 px-4 py-2.5 lg:py-3 rounded-xl transition-all duration-200 text-sm', !selectedMhsNim && !isShowingAll ? 'bg-indigo-600 text-white shadow-lg shadow-indigo-600/30' : 'text-slate-400 hover:bg-slate-700/50 hover:text-white']">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 lg:h-5 lg:w-5 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" /></svg>
          <span class="font-semibold text-xs lg:text-sm truncate">Perlu Validasi</span>
          <span v-if="totalBelumFinal > 0" class="ml-auto bg-rose-500 text-white text-[10px] font-black px-2 py-0.5 rounded-full shadow-sm flex-shrink-0">{{ totalBelumFinal }}</span>
        </button>

        <button @click="showMhsModal = true" :class="['w-full flex items-center gap-3 px-4 py-2.5 lg:py-3 rounded-xl transition-all duration-200 text-sm', selectedMhsNim ? 'bg-indigo-600 text-white shadow-lg shadow-indigo-600/30' : 'text-slate-400 hover:bg-slate-700/50 hover:text-white']">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 lg:h-5 lg:w-5 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" /></svg>
          <span class="font-semibold text-xs lg:text-sm truncate">Daftar Mahasiswa</span>
        </button>

        <button @click="showAllData" :class="['w-full flex items-center gap-3 px-4 py-2.5 lg:py-3 rounded-xl transition-all duration-200 text-sm', isShowingAll ? 'bg-indigo-600 text-white shadow-lg shadow-indigo-600/30' : 'text-slate-400 hover:bg-slate-700/50 hover:text-white']">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 lg:h-5 lg:w-5 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 7v10c0 2.21 3.582 4 8 4s8-1.79 8-4V7M4 7c0 2.21 3.582 4 8 4s8-1.79 8-4M4 7c0-2.21 3.582-4 8-4s8 1.79 8 4m0 5c0 2.21-3.582 4-8 4s-8-1.79-8-4" /></svg>
          <span class="font-semibold text-xs lg:text-sm truncate">Semua Riwayat</span>
        </button>

        <!-- MENU PROFIL -->
        <button @click="showProfileModal = true" class="w-full flex items-center gap-3 px-4 py-2.5 lg:py-3 rounded-xl transition-all duration-200 text-sm text-slate-400 hover:bg-slate-700/50 hover:text-white">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 lg:h-5 lg:w-5 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
          </svg>
          <span class="font-semibold text-xs lg:text-sm truncate">Profil Saya</span>
        </button>
      </nav>

      <!-- FOOTER SIDEBAR -->
      <div class="p-3 lg:p-4 border-t border-white/10 bg-gradient-to-b from-slate-800 to-slate-900 flex-shrink-0 sticky bottom-0 z-10">
        <div class="text-[10px] text-slate-500 text-center">
          <p>Sistem Kredit Poin Prestasi Mahasiswa</p>
          <p class="mt-0.5">STIE SBI Yogyakarta</p>
        </div>
      </div>
    </aside>

    <!-- MAIN CONTENT -->
    <main class="flex-1 p-4 sm:p-5 md:p-6 lg:p-8 xl:p-10 overflow-y-auto">
      <!-- HEADER WELCOME BANNER DENGAN LOGOUT DI KANAN -->
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
                  <h1 class="text-base sm:text-lg md:text-xl lg:text-2xl xl:text-3xl font-black tracking-tight truncate">Selamat Datang, {{ dosenProfile?.full_name || dosenProfile?.nama || dosenProfile?.username || 'Dosen' }}!</h1>
                  <p class="text-indigo-200 text-[10px] sm:text-xs md:text-sm truncate">Sistem Kredit Poin Prestasi Mahasiswa - STIE SBI Yogyakarta</p>
                </div>
              </div>
            </div>
            
            <!-- TOMBOL LOGOUT DI KANAN ATAS -->
            <div class="flex items-center gap-2 md:gap-3 flex-shrink-0">
              <button 
                @click="handleLogout"
                class="flex items-center gap-2 bg-rose-500 hover:bg-rose-600 text-white px-4 md:px-5 py-2 md:py-2.5 rounded-xl transition-all duration-200 font-bold text-xs md:text-sm shadow-lg shadow-rose-200/50"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 md:h-5 md:w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
                </svg>
                <span class="hidden sm:inline">Logout</span>
              </button>
              
            </div>
          </div>
        </div>
      </div>

      <!-- STATISTIK CARDS -->
      <div class="grid grid-cols-2 lg:grid-cols-4 gap-3 md:gap-4 lg:gap-5 mb-6 lg:mb-8">
        <div class="group bg-white p-4 md:p-5 rounded-xl md:rounded-2xl shadow-sm hover:shadow-xl transition-all duration-300 border border-slate-100 hover:border-indigo-200">
          <div class="h-10 w-10 md:h-11 md:w-11 lg:h-12 lg:w-12 bg-gradient-to-br from-blue-500 to-blue-600 rounded-xl flex items-center justify-center mb-2 md:mb-3 shadow-lg shadow-blue-200 group-hover:scale-110 transition-transform">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 md:h-6 md:w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" /></svg>
          </div>
          <p class="text-slate-500 text-[8px] md:text-[10px] font-black uppercase tracking-wider mb-0.5">Total Mahasiswa</p>
          <h4 class="text-xl md:text-2xl font-black text-slate-800">{{ mhsBimbinganList.length }} <span class="text-xs md:text-sm font-medium text-slate-400">Orang</span></h4>
        </div>

        <div class="group bg-white p-4 md:p-5 rounded-xl md:rounded-2xl shadow-sm hover:shadow-xl transition-all duration-300 border border-slate-100 hover:border-amber-200">
          <div class="h-10 w-10 md:h-11 md:w-11 lg:h-12 lg:w-12 bg-gradient-to-br from-amber-500 to-amber-600 rounded-xl flex items-center justify-center mb-2 md:mb-3 shadow-lg shadow-amber-200 group-hover:scale-110 transition-transform">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 md:h-6 md:w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
          </div>
          <p class="text-slate-500 text-[8px] md:text-[10px] font-black uppercase tracking-wider mb-0.5">Menunggu Validasi</p>
          <h4 class="text-xl md:text-2xl font-black text-slate-800">{{ totalBelumFinal }} <span class="text-xs md:text-sm font-medium text-slate-400">Berkas</span></h4>
        </div>

        <div class="group bg-white p-4 md:p-5 rounded-xl md:rounded-2xl shadow-sm hover:shadow-xl transition-all duration-300 border border-slate-100 hover:border-emerald-200">
          <div class="h-10 w-10 md:h-11 md:w-11 lg:h-12 lg:w-12 bg-gradient-to-br from-emerald-500 to-emerald-600 rounded-xl flex items-center justify-center mb-2 md:mb-3 shadow-lg shadow-emerald-200 group-hover:scale-110 transition-transform">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 md:h-6 md:w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
          </div>
          <p class="text-slate-500 text-[8px] md:text-[10px] font-black uppercase tracking-wider mb-0.5">Disetujui</p>
          <h4 class="text-xl md:text-2xl font-black text-slate-800">{{ pengajuanList.filter(p => p.status === 'approved_final').length }} <span class="text-xs md:text-sm font-medium text-slate-400">Berkas</span></h4>
        </div>

        <div class="group bg-white p-4 md:p-5 rounded-xl md:rounded-2xl shadow-sm hover:shadow-xl transition-all duration-300 border border-slate-100 hover:border-rose-200">
          <div class="h-10 w-10 md:h-11 md:w-11 lg:h-12 lg:w-12 bg-gradient-to-br from-rose-500 to-rose-600 rounded-xl flex items-center justify-center mb-2 md:mb-3 shadow-lg shadow-rose-200 group-hover:scale-110 transition-transform">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 md:h-6 md:w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
          </div>
          <p class="text-slate-500 text-[8px] md:text-[10px] font-black uppercase tracking-wider mb-0.5">Ditolak / Revisi</p>
          <h4 class="text-xl md:text-2xl font-black text-slate-800">{{ pengajuanList.filter(p => p.status === 'rejected').length }} <span class="text-xs md:text-sm font-medium text-slate-400">Berkas</span></h4>
        </div>
      </div>

      <!-- ALERT INFO -->
      <div v-if="totalBelumFinal > 0" class="mb-6 lg:mb-8 p-3 md:p-4 lg:p-5 bg-gradient-to-r from-amber-50 to-amber-100/50 rounded-xl lg:rounded-2xl border-l-4 border-amber-500 flex items-center gap-3 md:gap-4">
        <div class="h-8 w-8 md:h-9 md:w-9 lg:h-10 lg:w-10 bg-amber-500 rounded-xl flex items-center justify-center shadow-md flex-shrink-0">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 md:h-5 md:w-5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
          </svg>
        </div>
        <div class="min-w-0">
          <p class="font-bold text-amber-800 text-sm md:text-base">Pemberitahuan Validasi</p>
          <p class="text-xs md:text-sm text-amber-700 truncate">Terdapat <b>{{ totalBelumFinal }}</b> pengajuan baru yang memerlukan validasi dari Anda.</p>
        </div>
      </div>

      <!-- TABEL DATA -->
      <div class="bg-white rounded-xl md:rounded-2xl shadow-lg border border-slate-200 overflow-hidden flex flex-col">
        <div class="p-4 md:p-5 lg:p-6 border-b border-slate-200 flex flex-col lg:flex-row justify-between items-start lg:items-center gap-3 md:gap-4 lg:gap-6 bg-gradient-to-r from-slate-50 to-white">
          <h2 class="text-sm md:text-base lg:text-lg font-bold text-slate-800 flex items-center gap-2 md:gap-3 min-w-0">
            <div class="h-1.5 w-1.5 md:h-2 md:w-2 bg-indigo-500 rounded-full animate-pulse flex-shrink-0"></div>
            <span class="truncate">{{ selectedMhsNim ? `📘 Data Mahasiswa: ${selectedMhsNim}` : (isShowingAll ? '📋 Riwayat Seluruh Pengajuan' : '📌 Daftar Antrean Validasi') }}</span>
          </h2>

          <div class="flex flex-col sm:flex-row gap-2 md:gap-3 w-full lg:w-auto">
            <select 
              v-if="isShowingAll"
              v-model="filterStatus"
              class="px-3 md:px-4 py-2 md:py-2.5 bg-white border-2 border-slate-200 rounded-xl text-xs md:text-sm font-semibold text-slate-700 focus:border-indigo-500 outline-none transition-all"
            >
              <option value="all">📋 Semua Status</option>
              <option value="pending">🟡 Menunggu Validasi</option>
              <option value="approved_final">🟢 Disetujui</option>
              <option value="rejected">🔴 Ditolak / Revisi</option>
            </select>

            <div class="relative w-full lg:w-72 xl:w-80">
              <div class="absolute inset-y-0 left-3 md:left-4 flex items-center pointer-events-none">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 md:h-5 md:w-5 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                </svg>
              </div>
              <input 
                v-model="searchRiwayat" 
                type="text" 
                placeholder="Cari kegiatan, nama, atau NIM..." 
                class="w-full pl-9 md:pl-11 pr-3 md:pr-4 py-2 md:py-2.5 bg-white border-2 border-slate-200 rounded-xl text-xs md:text-sm font-medium text-slate-700 focus:border-indigo-500 focus:ring-0 outline-none transition-all" 
              />
            </div>
          </div>
        </div>

        <div class="overflow-x-auto">
          <table class="w-full min-w-[640px]">
            <thead class="bg-slate-100/80 border-b-2 border-slate-200">
              <tr>
                <th class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 text-left text-[8px] md:text-[10px] lg:text-xs font-bold text-slate-500 uppercase tracking-wider">No</th>
                <th class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 text-left text-[8px] md:text-[10px] lg:text-xs font-bold text-slate-500 uppercase tracking-wider">Data Mahasiswa</th>
                <th class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 text-left text-[8px] md:text-[10px] lg:text-xs font-bold text-slate-500 uppercase tracking-wider">Judul Kegiatan</th>
                <th class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 text-left text-[8px] md:text-[10px] lg:text-xs font-bold text-slate-500 uppercase tracking-wider">Status</th>
                <th class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 text-center text-[8px] md:text-[10px] lg:text-xs font-bold text-slate-500 uppercase tracking-wider">Aksi</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100">
              <tr v-for="(item, index) in (isShowingAll ? paginatedFilteredList : paginatedList)" :key="item.id" class="hover:bg-indigo-50/40 transition-colors group">
                <td class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 text-xs md:text-sm font-bold text-slate-500">{{ (currentPage - 1) * itemsPerPage + index + 1 }}</td>
                <td class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4">
                  <div class="flex items-center gap-2 md:gap-3">
                    <div class="h-8 w-8 md:h-9 md:w-9 lg:h-10 lg:w-10 bg-gradient-to-br from-indigo-100 to-indigo-200 rounded-xl flex items-center justify-center font-bold text-indigo-600 text-xs md:text-sm flex-shrink-0">
                      {{ item.mahasiswa_nama?.charAt(0).toUpperCase() }}
                    </div>
                    <div class="min-w-0">
                      <p class="font-bold text-slate-800 group-hover:text-indigo-600 transition-colors text-xs md:text-sm truncate">{{ item.mahasiswa_nama }}</p>
                      <p class="text-[10px] md:text-xs font-mono text-slate-500 truncate">{{ item.nim || item.mahasiswa_nim }}</p>
                    </div>
                  </div>
                </td>
                <td class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4">
                  <p class="text-xs md:text-sm font-semibold text-slate-700 max-w-[120px] md:max-w-[200px] lg:max-w-xs truncate">{{ item.judul_kegiatan }}</p>
                  <span v-if="item.is_edited_by_dpa" class="inline-flex items-center gap-0.5 md:gap-1 text-[8px] md:text-[10px] lg:text-xs font-bold text-amber-600 mt-0.5">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-2 w-2 md:h-3 md:w-3" viewBox="0 0 20 20" fill="currentColor">
                      <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                    </svg>
                    Koreksi
                  </span>
                </td>
                <td class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4">
                  <span :class="['px-2 md:px-3 py-1 md:py-1.5 rounded-full text-[8px] md:text-[10px] lg:text-xs font-bold border shadow-sm inline-flex items-center gap-1', statusClass(item.status)]">
                    <span v-if="item.status === 'pending'" class="w-1 h-1 md:w-1.5 md:h-1.5 bg-amber-500 rounded-full"></span>
                    <span v-else-if="item.status === 'approved_final'" class="w-1 h-1 md:w-1.5 md:h-1.5 bg-emerald-500 rounded-full"></span>
                    <span v-else-if="item.status === 'rejected'" class="w-1 h-1 md:w-1.5 md:h-1.5 bg-rose-500 rounded-full"></span>
                    {{ formatStatusLabel(item.status) }}
                  </span>
                </td>
                <td class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4">
                  <div class="flex gap-1 md:gap-2 justify-center flex-wrap">
                    <button @click="openDetail(item)" class="px-2 md:px-3 py-1 md:py-1.5 bg-white border border-slate-200 rounded-lg text-slate-600 font-semibold text-[8px] md:text-[10px] lg:text-xs hover:bg-indigo-600 hover:text-white hover:border-indigo-600 transition-all shadow-sm">
                      🔍 Periksa
                    </button>
                    <button @click="openEditExisting(item)" class="px-2 md:px-3 py-1 md:py-1.5 bg-amber-50 border border-amber-200 rounded-lg text-amber-600 font-semibold text-[8px] md:text-[10px] lg:text-xs hover:bg-amber-500 hover:text-white hover:border-amber-500 transition-all shadow-sm">
                      ✏️ Edit
                    </button>
                  </div>
                </td>
              </tr>
              <tr v-if="(isShowingAll ? paginatedFilteredList : paginatedList).length === 0">
                <td colspan="5" class="px-3 md:px-6 py-8 md:py-12 lg:py-16 text-center">
                  <div class="text-4xl md:text-5xl lg:text-6xl mb-2 md:mb-4 opacity-40">📭</div>
                  <p class="text-slate-500 font-semibold text-xs md:text-sm lg:text-base">{{ searchRiwayat ? 'Data tidak ditemukan.' : 'Tidak ada antrean data.' }}</p>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- PAGINATION -->
        <div v-if="(isShowingAll ? filteredByStatusList : displayList).length > 0" class="p-3 md:p-4 lg:p-5 border-t border-slate-200 flex flex-col sm:flex-row justify-between items-center gap-3 md:gap-4 bg-slate-50/80">
          <span class="text-[10px] md:text-xs lg:text-sm text-slate-500">
            Menampilkan <strong class="text-slate-700">{{ (currentPage - 1) * itemsPerPage + 1 }}</strong> - 
            <strong class="text-slate-700">{{ Math.min(currentPage * itemsPerPage, (isShowingAll ? filteredByStatusList : displayList).length) }}</strong> 
            dari <strong class="text-slate-700">{{ (isShowingAll ? filteredByStatusList : displayList).length }}</strong> data
          </span>
          <div class="flex gap-1 md:gap-2 flex-wrap justify-center">
            <button @click="currentPage > 1 ? currentPage-- : null" :disabled="currentPage === 1" class="px-3 md:px-4 lg:px-5 py-1.5 md:py-2 bg-white border border-slate-200 rounded-lg text-[10px] md:text-xs lg:text-sm font-semibold text-slate-600 hover:bg-indigo-50 hover:text-indigo-600 hover:border-indigo-200 disabled:opacity-50 disabled:cursor-not-allowed transition-all">
              ← Sebelumnya
            </button>
            <div class="flex gap-0.5 md:gap-1">
              <button 
                v-for="page in Math.min(5, totalPages)" 
                :key="page"
                @click="currentPage = page"
                :class="[
                  'w-7 h-7 md:w-8 md:h-8 lg:w-9 lg:h-9 rounded-lg text-[10px] md:text-xs lg:text-sm font-semibold transition-all',
                  currentPage === page 
                    ? 'bg-indigo-600 text-white shadow-md' 
                    : 'bg-white border border-slate-200 text-slate-600 hover:bg-indigo-50'
                ]"
              >
                {{ page }}
              </button>
              <span v-if="totalPages > 5" class="px-1 md:px-2 text-slate-400 text-xs md:text-sm">...</span>
            </div>
            <button @click="currentPage < totalPages ? currentPage++ : null" :disabled="currentPage === totalPages" class="px-3 md:px-4 lg:px-5 py-1.5 md:py-2 bg-white border border-slate-200 rounded-lg text-[10px] md:text-xs lg:text-sm font-semibold text-slate-600 hover:bg-indigo-50 hover:text-indigo-600 hover:border-indigo-200 disabled:opacity-50 disabled:cursor-not-allowed transition-all">
              Selanjutnya →
            </button>
          </div>
        </div>
      </div>
    </main>

    <!-- ========== MODAL-MODAL ========== -->

    <!-- MODAL DETAIL -->
    <transition name="fade">
      <div v-if="showDetailModal" class="fixed inset-0 z-[60] flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-sm">
        <div class="bg-white rounded-3xl shadow-2xl w-full max-w-5xl max-h-[95vh] overflow-hidden flex flex-col">
          <!-- Header -->
          <div class="p-5 md:p-6 lg:p-8 border-b border-slate-100 flex justify-between items-center bg-gradient-to-r from-indigo-600 to-indigo-700">
            <div class="flex items-center gap-3 md:gap-5">
              <div class="h-10 w-10 md:h-12 md:w-12 lg:h-14 lg:w-14 bg-white/20 rounded-2xl flex items-center justify-center text-white backdrop-blur-sm flex-shrink-0">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 md:h-6 md:w-6 lg:h-7 lg:w-7" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
              </div>
              <div>
                <h3 class="text-xl md:text-2xl lg:text-3xl font-black text-white uppercase tracking-tight">PEMERIKSAAN BERKAS</h3>
                <p class="text-[10px] md:text-xs lg:text-sm font-bold text-indigo-200 mt-0.5 uppercase tracking-widest">VERIFIKASI POIN KEGIATAN MAHASISWA</p>
              </div>
            </div>
            <button @click="closeDetail" class="text-white/70 hover:text-white hover:bg-white/20 h-9 w-9 md:h-10 md:w-10 lg:h-12 lg:w-12 flex items-center justify-center rounded-2xl transition-all text-xl md:text-2xl">&times;</button>
          </div>

          <!-- Body -->
          <div class="flex-1 overflow-y-auto p-5 md:p-6 lg:p-8 bg-gradient-to-br from-slate-50 to-white custom-scroll">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 lg:gap-8">
              <!-- KOLOM KIRI -->
              <div class="space-y-4 md:space-y-6">
                <!-- Profil Mahasiswa -->
                <div class="bg-gradient-to-r from-indigo-50 via-white to-indigo-50 p-4 md:p-5 lg:p-6 rounded-2xl border border-indigo-100 shadow-sm">
                  <div class="flex items-center gap-4 md:gap-5">
                    <div class="h-14 w-14 md:h-16 md:w-16 lg:h-20 lg:w-20 bg-gradient-to-br from-indigo-500 to-indigo-600 rounded-2xl flex items-center justify-center text-white shadow-lg flex-shrink-0">
                      <span class="font-black text-xl md:text-2xl lg:text-3xl">{{ selectedItem.mahasiswa_nama?.charAt(0).toUpperCase() }}</span>
                    </div>
                    <div class="min-w-0">
                      <p class="text-[10px] text-indigo-500 font-black uppercase tracking-wider mb-0.5">Nama Mahasiswa</p>
                      <p class="text-base md:text-lg lg:text-xl font-black text-slate-800 truncate">{{ selectedItem.mahasiswa_nama }}</p>
                      <div class="flex items-center gap-2 mt-1 flex-wrap">
                        <span class="px-2 md:px-3 py-0.5 md:py-1 bg-indigo-100 text-indigo-700 rounded-lg text-xs md:text-sm font-bold font-mono">{{ selectedItem.nim || selectedItem.mahasiswa_nim }}</span>
                        <span v-if="selectedItem.status === 'pending'" class="px-2 md:px-3 py-0.5 md:py-1 bg-amber-100 text-amber-700 rounded-lg text-[10px] md:text-xs font-bold uppercase">Menunggu</span>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Informasi Kegiatan -->
                <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm">
                  <div class="px-4 md:px-6 py-3 md:py-4 bg-slate-50 border-b border-slate-200">
                    <h4 class="text-[10px] md:text-xs font-black text-slate-500 uppercase tracking-wider flex items-center gap-2">
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 md:h-5 md:w-5 text-indigo-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                      </svg>
                      INFORMASI KEGIATAN
                    </h4>
                  </div>
                  <div class="p-4 md:p-5 lg:p-6 space-y-4">
                    <div>
                      <label class="text-[8px] md:text-[10px] font-black text-slate-400 uppercase tracking-wider block mb-1">JUDUL KEGIATAN</label>
                      <div class="bg-slate-50 rounded-xl p-3 md:p-4 border border-slate-200">
                        <p class="text-sm md:text-base font-bold text-slate-800">{{ selectedItem.judul_kegiatan }}</p>
                      </div>
                    </div>

                    <div>
                      <label class="text-[8px] md:text-[10px] font-black text-slate-400 uppercase tracking-wider block mb-1">KATEGORI</label>
                      <div class="bg-gradient-to-r from-indigo-50 to-indigo-100/30 rounded-xl p-3 md:p-4 border border-indigo-200 flex items-center justify-between">
                        <p class="text-sm md:text-base font-bold text-indigo-800">{{ getNamaKegiatanFromKategori(selectedItem) }}</p>
                        <span class="bg-indigo-600 text-white text-[10px] md:text-xs font-black uppercase px-3 md:px-4 py-1 md:py-2 rounded-full shadow-md">{{ selectedItem.bobot_poin_kategori || 0 }} POIN</span>
                      </div>
                    </div>

                    <div class="grid grid-cols-2 gap-3 md:gap-4">
                      <div>
                        <label class="text-[8px] md:text-[10px] font-black text-slate-400 uppercase tracking-wider block mb-1">TANGGAL</label>
                        <div class="bg-slate-50 rounded-xl p-2 md:p-3 border border-slate-200">
                          <p class="text-xs md:text-sm font-bold text-slate-700">{{ selectedItem.tanggal_kegiatan || '-' }}</p>
                        </div>
                      </div>
                      <div>
                        <label class="text-[8px] md:text-[10px] font-black text-slate-400 uppercase tracking-wider block mb-1">DURASI</label>
                        <div class="bg-slate-50 rounded-xl p-2 md:p-3 border border-slate-200">
                          <p class="text-xs md:text-sm font-bold text-slate-700">{{ selectedItem.durasi_kegiatan || hitungDurasiOtomatis(selectedItem) }}</p>
                        </div>
                      </div>
                    </div>

                    <div v-if="selectedItem.informasi_kegiatan && selectedItem.informasi_kegiatan.trim() !== ''">
                      <label class="text-[8px] md:text-[10px] font-black text-slate-400 uppercase tracking-wider block mb-1">LINK</label>
                      <div class="bg-slate-50 rounded-xl p-3 border border-slate-200">
                        <a :href="selectedItem.informasi_kegiatan" target="_blank" class="text-indigo-600 font-bold text-xs md:text-sm hover:underline break-all flex items-center gap-2">
                          <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 md:h-4 md:w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.102m1.858-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1" />
                          </svg>
                          {{ selectedItem.informasi_kegiatan }}
                        </a>
                      </div>
                    </div>

                    <div v-if="selectedItem.catatan && selectedItem.catatan.trim() !== ''">
                      <label class="text-[8px] md:text-[10px] font-black text-slate-400 uppercase tracking-wider block mb-1">📝 CATATAN MAHASISWA</label>
                      <div class="bg-amber-50 rounded-xl p-3 border border-amber-200">
                        <p class="text-xs md:text-sm italic text-amber-800">"{{ selectedItem.catatan }}"</p>
                      </div>
                    </div>

                    <div v-if="selectedItem.status === 'rejected' && selectedItem.komentar_dpa">
                      <label class="text-[8px] md:text-[10px] font-black text-rose-500 uppercase tracking-wider block mb-1">⚠️ CATATAN REVISI</label>
                      <div class="bg-rose-50 rounded-xl p-3 border border-rose-200">
                        <p class="text-xs md:text-sm text-rose-700">{{ selectedItem.komentar_dpa }}</p>
                      </div>
                    </div>

                    <div v-if="!isEditMode && selectedItem.status === 'pending'" class="pt-3 border-t border-slate-200">
                      <label class="text-[8px] md:text-[10px] font-black text-slate-400 uppercase tracking-wider block mb-1">
                        CATATAN (jika Ditolak/Revisi)
                        <span class="text-rose-500 text-[10px] ml-1">*Wajib</span>
                      </label>
                      <textarea v-model="komentarRevisi" rows="3" placeholder="Tuliskan alasan penolakan..." class="w-full bg-slate-50 border-2 border-slate-200 rounded-xl p-3 md:p-4 text-xs md:text-sm font-medium focus:border-indigo-400 focus:ring-4 focus:ring-indigo-100 outline-none transition-all"></textarea>
                    </div>
                  </div>
                </div>
              </div>

              <!-- KOLOM KANAN -->
              <div class="space-y-4 md:space-y-6">
                <div class="bg-gradient-to-br from-slate-50 to-slate-100 rounded-2xl border-2 border-dashed border-indigo-200 overflow-hidden shadow-sm">
                  <div class="px-4 md:px-6 py-3 md:py-4 bg-indigo-50 border-b border-indigo-200">
                    <div class="flex justify-between items-center flex-wrap gap-3">
                      <h4 class="text-[10px] md:text-xs font-black text-indigo-700 uppercase tracking-wider flex items-center gap-2">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 md:h-5 md:w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                        </svg>
                        DOKUMEN SERTIFIKAT
                      </h4>
                      <div class="flex gap-2">
                        <a v-if="selectedItem.bukti_sertifikat" :href="selectedItem.bukti_sertifikat" target="_blank" class="px-3 md:px-4 py-1 md:py-2 bg-white border border-indigo-300 text-indigo-600 text-[10px] font-black rounded-xl hover:bg-indigo-600 hover:text-white transition-all">
                          🔗 Buka
                        </a>
                        <button 
                          v-if="selectedItem.bukti_sertifikat"
                          @click="downloadFile(selectedItem.bukti_sertifikat, 'sertifikat')"
                          class="px-3 md:px-4 py-1 md:py-2 bg-indigo-600 text-white text-[10px] font-black rounded-xl hover:bg-indigo-700 transition-all flex items-center gap-1"
                        >
                          <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 md:h-4 md:w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                          </svg>
                          Download
                        </button>
                      </div>
                    </div>
                  </div>
                  
                  <div class="p-4 md:p-6 bg-white/50 min-h-[250px] md:min-h-[350px] flex items-center justify-center">
                    <div v-if="selectedItem.bukti_sertifikat" class="w-full">
                      <img v-if="isImage(selectedItem.bukti_sertifikat)" :src="selectedItem.bukti_sertifikat" class="w-full max-h-[300px] md:max-h-[400px] object-contain rounded-xl shadow-lg" />
                      <embed v-else-if="isPdf(selectedItem.bukti_sertifikat)" :src="selectedItem.bukti_sertifikat" type="application/pdf" class="w-full h-[300px] md:h-[400px] rounded-xl shadow-lg" />
                      <div v-else class="text-center p-8 bg-slate-100 rounded-xl">
                        <div class="text-4xl md:text-5xl mb-3">📄</div>
                        <p class="text-slate-500 font-bold text-sm md:text-base mb-3">File tidak dapat dipratinjau</p>
                        <button @click="downloadFile(selectedItem.bukti_sertifikat, 'sertifikat')" class="px-4 md:px-6 py-2 md:py-3 bg-indigo-600 text-white rounded-xl text-xs md:text-sm font-bold hover:bg-indigo-700 transition-all">
                          📥 Download File
                        </button>
                      </div>
                    </div>
                    <div v-else class="text-center p-8">
                      <div class="text-4xl md:text-5xl mb-3 opacity-50">📭</div>
                      <p class="text-slate-400 font-bold text-sm md:text-base italic">Tidak ada dokumen</p>
                    </div>
                  </div>
                </div>

                <div class="bg-gradient-to-r from-slate-50 to-slate-100 rounded-2xl p-3 md:p-4 border border-slate-200">
                  <div class="flex items-center justify-between flex-wrap gap-2">
                    <div>
                      <p class="text-[8px] md:text-[10px] text-slate-400 font-black uppercase">Status</p>
                      <span :class="['mt-1 inline-flex px-3 md:px-4 py-1 md:py-2 rounded-xl text-[10px] md:text-xs font-bold', statusClass(selectedItem.status)]">
                        {{ formatStatusLabel(selectedItem.status) }}
                      </span>
                    </div>
                    <div v-if="selectedItem.is_edited_by_dpa" class="flex items-center gap-1 md:gap-2 text-amber-600">
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 md:h-5 md:w-5" viewBox="0 0 20 20" fill="currentColor">
                        <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                      </svg>
                      <span class="text-[8px] md:text-[10px] font-bold">Dikoreksi DPA</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Footer -->
          <div class="p-4 md:p-5 lg:p-6 bg-white border-t border-slate-200 flex flex-col sm:flex-row justify-end gap-3 md:gap-4 shrink-0">
            <template v-if="selectedItem.status === 'pending' && !isEditMode">
              <button @click="submitTolakRevisi" class="px-6 md:px-8 py-2.5 md:py-3.5 bg-white border-2 border-rose-300 text-rose-600 font-black rounded-xl hover:bg-rose-50 hover:border-rose-500 transition-all shadow-sm text-xs md:text-sm uppercase tracking-wider flex items-center gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 md:h-5 md:w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                TOLAK / REVISI
              </button>
              <button @click="updateStatus(selectedItem.id, 'approved_final')" class="px-6 md:px-8 py-2.5 md:py-3.5 bg-gradient-to-r from-indigo-600 to-indigo-700 text-white font-black rounded-xl hover:from-indigo-700 hover:to-indigo-800 transition-all shadow-lg shadow-indigo-200 text-xs md:text-sm uppercase tracking-wider flex items-center gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 md:h-5 md:w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                ✓ SETUJUI
              </button>
            </template>
            <template v-else>
              <button @click="closeDetail" class="px-6 md:px-8 py-2.5 md:py-3.5 bg-slate-600 text-white font-black rounded-xl hover:bg-slate-700 transition-all shadow-md text-xs md:text-sm uppercase tracking-wider">
                TUTUP
              </button>
            </template>
          </div>
        </div>
      </div>
    </transition>

    <!-- MODAL EDIT EXISTING -->
    <transition name="fade">
      <div v-if="showEditExistingModal" class="fixed inset-0 z-[70] flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-sm">
        <div class="bg-white rounded-3xl shadow-2xl w-full max-w-5xl max-h-[90vh] overflow-hidden flex flex-col">
          <!-- Header -->
          <div class="p-5 md:p-6 lg:p-8 border-b border-slate-100 flex justify-between items-center bg-gradient-to-r from-amber-500 to-orange-600">
            <div class="flex items-center gap-3 md:gap-5">
              <div class="h-10 w-10 md:h-12 md:w-12 lg:h-14 lg:w-14 bg-white/20 rounded-2xl flex items-center justify-center text-white backdrop-blur-sm flex-shrink-0">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 md:h-6 md:w-6 lg:h-7 lg:w-7" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                </svg>
              </div>
              <div>
                <h3 class="text-xl md:text-2xl lg:text-3xl font-black text-white uppercase tracking-tight">EDIT & UBAH STATUS</h3>
                <p class="text-[10px] md:text-xs lg:text-sm font-bold text-amber-100 mt-0.5 uppercase tracking-widest">Untuk Data yang Sudah Tervalidasi</p>
              </div>
            </div>
            <button @click="closeEditExistingModal" class="text-white/70 hover:text-white hover:bg-white/20 h-9 w-9 md:h-10 md:w-10 lg:h-12 lg:w-12 flex items-center justify-center rounded-2xl transition-all text-xl md:text-2xl">&times;</button>
          </div>

          <!-- Body -->
          <div class="flex-1 overflow-y-auto p-5 md:p-6 lg:p-8 bg-gradient-to-br from-slate-50 to-white custom-scroll">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 lg:gap-8">
              <!-- KOLOM KIRI -->
              <div class="space-y-4 md:space-y-6">
                <div class="bg-gradient-to-r from-amber-50 via-white to-amber-50 p-4 md:p-5 lg:p-6 rounded-2xl border border-amber-100 shadow-sm">
                  <div class="flex items-center gap-4 md:gap-5">
                    <div class="h-14 w-14 md:h-16 md:w-16 lg:h-20 lg:w-20 bg-gradient-to-br from-amber-500 to-orange-600 rounded-2xl flex items-center justify-center text-white shadow-lg flex-shrink-0">
                      <span class="font-black text-xl md:text-2xl lg:text-3xl">{{ selectedEditItem.mahasiswa_nama?.charAt(0).toUpperCase() }}</span>
                    </div>
                    <div class="min-w-0">
                      <p class="text-[10px] text-amber-600 font-black uppercase tracking-wider mb-0.5">Data Mahasiswa</p>
                      <p class="text-base md:text-lg lg:text-xl font-black text-slate-800 truncate">{{ selectedEditItem.mahasiswa_nama }}</p>
                      <div class="flex items-center gap-2 mt-1 flex-wrap">
                        <span class="px-2 md:px-3 py-0.5 md:py-1 bg-amber-100 text-amber-700 rounded-lg text-xs md:text-sm font-bold font-mono">{{ selectedEditItem.nim || selectedEditItem.mahasiswa_nim }}</span>
                        <span :class="['px-2 md:px-3 py-0.5 md:py-1 rounded-lg text-[10px] md:text-xs font-bold uppercase', statusClass(selectedEditItem.status)]">
                          {{ formatStatusLabel(selectedEditItem.status) }}
                        </span>
                      </div>
                    </div>
                  </div>
                </div>

                <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm">
                  <div class="px-4 md:px-6 py-3 md:py-4 bg-slate-50 border-b border-slate-200">
                    <h4 class="text-[10px] md:text-xs font-black text-slate-500 uppercase tracking-wider flex items-center gap-2">
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 md:h-5 md:w-5 text-amber-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                      </svg>
                      EDIT KEGIATAN
                    </h4>
                  </div>
                  <div class="p-4 md:p-5 lg:p-6 space-y-4">
                    <div>
                      <label class="text-[8px] md:text-[10px] font-black text-slate-500 uppercase tracking-wider block mb-1">JUDUL KEGIATAN</label>
                      <input v-model="editExistingForm.judul_kegiatan" type="text" class="w-full bg-slate-50 border-2 border-slate-200 rounded-xl px-3 md:px-4 py-2 md:py-3 text-xs md:text-sm font-bold text-slate-700 focus:border-amber-400 focus:ring-4 focus:ring-amber-50 outline-none transition-all" placeholder="Judul kegiatan" />
                    </div>

                    <div>
                      <label class="text-[8px] md:text-[10px] font-black text-slate-500 uppercase tracking-wider block mb-1">KATEGORI</label>
                      <button @click="showKategoriModal = true; tempEditMode = true" type="button" class="w-full bg-slate-50 border-2 border-slate-200 rounded-xl px-3 md:px-4 py-2 md:py-3 text-left text-xs md:text-sm font-bold hover:border-amber-400 hover:bg-amber-50 transition-all flex justify-between items-center group">
                        <span :class="editExistingForm.kategori_id ? 'text-slate-800' : 'text-slate-400'">
                          {{ editExistingForm.kategori_name || 'Pilih kategori...' }}
                        </span>
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-slate-400 group-hover:text-amber-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                        </svg>
                      </button>
                    </div>

                    <div class="grid grid-cols-2 gap-3 md:gap-4">
                      <div>
                        <label class="text-[8px] md:text-[10px] font-black text-slate-500 uppercase tracking-wider block mb-1">TANGGAL</label>
                        <input v-model="editExistingForm.tanggal_kegiatan" type="date" class="w-full bg-slate-50 border-2 border-slate-200 rounded-xl px-3 md:px-4 py-2 md:py-3 text-xs md:text-sm font-bold text-slate-700 focus:border-amber-400 focus:ring-4 focus:ring-amber-50 outline-none transition-all" />
                      </div>
                      <div>
                        <label class="text-[8px] md:text-[10px] font-black text-slate-500 uppercase tracking-wider block mb-1">DURASI</label>
                        <input v-model="editExistingForm.durasi_kegiatan" type="text" placeholder="2 Hari" class="w-full bg-slate-50 border-2 border-slate-200 rounded-xl px-3 md:px-4 py-2 md:py-3 text-xs md:text-sm font-bold text-slate-700 focus:border-amber-400 focus:ring-4 focus:ring-amber-50 outline-none transition-all" />
                      </div>
                    </div>

                    <div>
                      <label class="text-[8px] md:text-[10px] font-black text-slate-500 uppercase tracking-wider block mb-1">STATUS VALIDASI</label>
                      <select v-model="editExistingForm.status" class="w-full bg-slate-50 border-2 border-slate-200 rounded-xl px-3 md:px-4 py-2 md:py-3 text-xs md:text-sm font-bold focus:border-amber-400 focus:ring-4 focus:ring-amber-100 outline-none transition-all appearance-none">
                        <option v-for="status in availableStatuses" :key="status.value" :value="status.value">{{ status.label }}</option>
                      </select>
                    </div>

                    <div>
                      <label class="text-[8px] md:text-[10px] font-black text-slate-500 uppercase tracking-wider block mb-1 flex items-center gap-2">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
                        </svg>
                        KOMENTAR
                        <span v-if="editExistingForm.status === 'rejected'" class="text-rose-500 text-[10px] bg-rose-50 px-2 py-0.5 rounded-full">WAJIB</span>
                      </label>
                      <textarea v-model="komentarEditExisting" rows="3" placeholder="Tuliskan catatan..." class="w-full border-2 rounded-xl p-3 md:p-4 text-xs md:text-sm font-medium focus:ring-4 outline-none transition-all resize-none bg-slate-50 border-slate-200 focus:ring-amber-100 focus:border-amber-400"></textarea>
                    </div>
                  </div>
                </div>
              </div>

              <!-- KOLOM KANAN -->
              <div class="space-y-4 md:space-y-6">
                <div class="bg-gradient-to-br from-slate-50 to-slate-100 rounded-2xl border-2 border-dashed border-amber-200 overflow-hidden shadow-sm">
                  <div class="px-4 md:px-6 py-3 md:py-4 bg-amber-50 border-b border-amber-200">
                    <div class="flex justify-between items-center flex-wrap gap-3">
                      <h4 class="text-[10px] md:text-xs font-black text-amber-700 uppercase tracking-wider flex items-center gap-2">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 md:h-5 md:w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                        </svg>
                        SERTIFIKAT
                      </h4>
                      <div class="flex gap-2">
                        <a v-if="selectedEditItem.bukti_sertifikat" :href="selectedEditItem.bukti_sertifikat" target="_blank" class="px-3 md:px-4 py-1 md:py-2 bg-white border border-amber-300 text-amber-600 text-[10px] font-black rounded-xl hover:bg-amber-600 hover:text-white transition-all">
                          🔗 Buka
                        </a>
                        <button v-if="selectedEditItem.bukti_sertifikat" @click="downloadFile(selectedEditItem.bukti_sertifikat, 'sertifikat')" class="px-3 md:px-4 py-1 md:py-2 bg-amber-600 text-white text-[10px] font-black rounded-xl hover:bg-amber-700 transition-all flex items-center gap-1">
                          <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 md:h-4 md:w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                          </svg>
                          Download
                        </button>
                      </div>
                    </div>
                  </div>
                  
                  <div class="p-4 md:p-6 bg-white/50 min-h-[250px] md:min-h-[350px] flex items-center justify-center">
                    <div v-if="selectedEditItem.bukti_sertifikat" class="w-full">
                      <img v-if="isImage(selectedEditItem.bukti_sertifikat)" :src="selectedEditItem.bukti_sertifikat" class="w-full max-h-[300px] md:max-h-[400px] object-contain rounded-xl shadow-lg" />
                      <embed v-else-if="isPdf(selectedEditItem.bukti_sertifikat)" :src="selectedEditItem.bukti_sertifikat" type="application/pdf" class="w-full h-[300px] md:h-[400px] rounded-xl shadow-lg" />
                      <div v-else class="text-center p-8 bg-slate-100 rounded-xl">
                        <div class="text-4xl md:text-5xl mb-3">📄</div>
                        <p class="text-slate-500 font-bold text-sm md:text-base mb-3">File tidak dapat dipratinjau</p>
                        <button @click="downloadFile(selectedEditItem.bukti_sertifikat, 'sertifikat')" class="px-4 md:px-6 py-2 md:py-3 bg-amber-600 text-white rounded-xl text-xs md:text-sm font-bold hover:bg-amber-700 transition-all">
                          📥 Download
                        </button>
                      </div>
                    </div>
                    <div v-else class="text-center p-8">
                      <div class="text-4xl md:text-5xl mb-3 opacity-50">📭</div>
                      <p class="text-slate-400 font-bold text-sm md:text-base italic">Tidak ada dokumen</p>
                    </div>
                  </div>
                </div>

                <div v-if="selectedEditItem.komentar_dpa && selectedEditItem.status === 'rejected'" class="bg-rose-50 rounded-2xl p-4 border border-rose-200">
                  <p class="text-[10px] font-black text-rose-600 uppercase tracking-wider mb-1">Catatan Revisi Sebelumnya</p>
                  <p class="text-sm text-rose-700 italic">"{{ selectedEditItem.komentar_dpa }}"</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Footer -->
          <div class="p-4 md:p-5 lg:p-6 bg-white border-t border-slate-200 flex justify-end gap-3 md:gap-4 shrink-0 flex-wrap">
            <button @click="closeEditExistingModal" class="px-6 md:px-8 py-2.5 md:py-3.5 bg-white border-2 border-slate-300 text-slate-600 font-black rounded-xl hover:bg-slate-50 hover:border-slate-400 transition-all text-xs md:text-sm uppercase tracking-wider flex items-center gap-2">
              BATAL
            </button>
            <button @click="saveEditExisting" class="px-6 md:px-8 py-2.5 md:py-3.5 bg-gradient-to-r from-amber-500 to-orange-600 text-white font-black rounded-xl hover:from-amber-600 hover:to-orange-700 transition-all shadow-lg shadow-amber-200 text-xs md:text-sm uppercase tracking-wider flex items-center gap-2">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 md:h-5 md:w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
              </svg>
              SIMPAN
            </button>
          </div>
        </div>
      </div>
    </transition>

    <!-- MODAL KATEGORI -->
    <transition name="fade">
      <div v-if="showKategoriModal" class="fixed inset-0 z-[80] flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-sm">
        <div class="bg-white rounded-2xl shadow-2xl w-full max-w-3xl overflow-hidden flex flex-col max-h-[85vh]">
          <div class="p-4 md:p-6 border-b border-slate-100 flex justify-between items-center bg-gradient-to-r from-indigo-600 to-indigo-700">
            <div class="flex items-center gap-3">
              <div class="h-8 w-8 md:h-9 md:w-9 bg-white/20 rounded-xl flex items-center justify-center flex-shrink-0">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 md:h-5 md:w-5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
                </svg>
              </div>
              <div>
                <h3 class="text-base md:text-lg font-black text-white uppercase tracking-tight">Pilih Kategori</h3>
                <p class="text-[10px] text-indigo-200 mt-0.5">Level → Bidang → Sifat → Nama → Peran</p>
              </div>
            </div>
            <button @click="showKategoriModal = false" class="text-white/70 hover:text-white hover:bg-white/20 h-8 w-8 md:h-9 md:w-9 flex items-center justify-center rounded-xl transition-all text-xl">&times;</button>
          </div>
          
          <div class="p-4 border-b bg-white">
            <input v-model="searchKategori" type="text" placeholder="Cari kategori..." class="w-full bg-slate-50 border-2 border-slate-200 rounded-xl py-2 md:py-3 px-3 md:px-4 text-xs md:text-sm font-bold outline-none focus:border-indigo-500 transition-all" />
          </div>
          
          <div class="flex-1 overflow-y-auto p-4 md:p-6 custom-scroll">
            <div v-if="Object.keys(groupedKategori).length === 0" class="text-center py-8">
              <div class="text-4xl mb-3 opacity-40">🔍</div>
              <p class="text-slate-500 font-bold text-sm">Tidak ada kategori ditemukan</p>
            </div>
            
            <div v-for="(levelItems, levelName) in groupedKategori" :key="levelName" class="mb-4 last:mb-0">
              <div class="sticky top-0 z-10 bg-white/95 pt-2 pb-2 border-b border-indigo-100">
                <div class="flex items-center justify-between">
                  <h4 class="text-sm font-black text-indigo-700 uppercase tracking-tight">Level: {{ levelName }}</h4>
                  <span class="text-[10px] font-bold bg-indigo-100 text-indigo-700 px-2 py-0.5 rounded-full">{{ levelItems.totalCount }}</span>
                </div>
              </div>
              
              <div v-for="(bidangItems, bidangName) in levelItems.byBidang" :key="bidangName" class="ml-3 md:ml-4 mb-3">
                <div class="flex items-center gap-2 mt-2">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 md:h-4 md:w-4 text-emerald-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
                  </svg>
                  <h5 class="text-xs md:text-sm font-black text-emerald-700 uppercase tracking-wider">{{ bidangName }}</h5>
                </div>
                
                <div class="ml-4 md:ml-6 mt-1 space-y-1.5">
                  <div v-for="kat in bidangItems" :key="kat.id" @click="pilihKategori(kat)" class="group bg-white p-3 md:p-4 rounded-xl border-2 border-slate-200 hover:border-indigo-400 hover:shadow-lg transition-all cursor-pointer">
                    <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-2 md:gap-4">
                      <div class="min-w-0">
                        <div class="flex flex-wrap gap-1.5 mb-1">
                          <span class="inline-flex items-center gap-0.5 px-2 py-0.5 bg-indigo-50 text-indigo-700 text-[8px] md:text-[10px] font-black uppercase tracking-wider rounded-lg">Peran: {{ kat.partisipasi || '-' }}</span>
                          <span class="inline-flex items-center gap-0.5 px-2 py-0.5 bg-amber-50 text-amber-600 text-[8px] md:text-[10px] font-black uppercase tracking-wider rounded-lg">Sifat: {{ kat.sifat || '-' }}</span>
                        </div>
                        <p class="text-xs md:text-sm font-bold text-slate-800 group-hover:text-indigo-600 transition-colors">{{ kat.nama_kegiatan || kat.kegiatan }}</p>
                      </div>
                      <div class="text-right shrink-0">
                        <span class="text-lg md:text-xl font-black text-indigo-600 group-hover:scale-110 transition-transform inline-block">{{ kat.poin || kat.bobot_poin || 0 }}</span>
                        <span class="text-[8px] md:text-[10px] font-bold text-slate-500 uppercase">POIN</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <div class="p-4 border-t bg-slate-50 flex justify-end">
            <button @click="showKategoriModal = false" class="px-4 md:px-6 py-2 bg-slate-600 text-white font-bold rounded-xl hover:bg-slate-700 transition-all text-xs md:text-sm">Tutup</button>
          </div>
        </div>
      </div>
    </transition>

    <!-- MODAL MAHASISWA -->
    <transition name="fade">
      <div v-if="showMhsModal" class="fixed inset-0 z-[60] flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-sm">
        <div class="bg-white rounded-3xl shadow-2xl w-full max-w-6xl overflow-hidden flex flex-col max-h-[85vh]">
          <div class="p-5 md:p-6 lg:p-8 border-b border-slate-100 flex justify-between items-center bg-gradient-to-r from-indigo-600 to-indigo-700">
            <div class="flex items-center gap-3 md:gap-5">
              <div class="h-10 w-10 md:h-12 md:w-12 lg:h-14 lg:w-14 bg-white/20 rounded-2xl flex items-center justify-center text-white backdrop-blur-sm flex-shrink-0">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 md:h-6 md:w-6 lg:h-7 lg:w-7" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
                </svg>
              </div>
              <div>
                <h3 class="text-xl md:text-2xl lg:text-3xl font-black text-white uppercase tracking-tight">DAFTAR MAHASISWA</h3>
                <p class="text-[10px] md:text-xs lg:text-sm font-bold text-indigo-200 mt-0.5 uppercase tracking-widest">Total {{ mhsBimbinganList.length }} Mahasiswa</p>
              </div>
            </div>
            <button @click="showMhsModal = false" class="text-white/70 hover:text-white hover:bg-white/20 h-9 w-9 md:h-10 md:w-10 lg:h-12 lg:w-12 flex items-center justify-center rounded-2xl transition-all text-xl md:text-2xl">&times;</button>
          </div>
          
          <div class="p-4 border-b bg-white">
            <div class="relative">
              <input v-model="searchMhs" type="text" placeholder="Cari mahasiswa..." class="w-full pl-9 md:pl-12 pr-3 md:pr-5 py-2 md:py-3 bg-slate-50 border-2 border-slate-200 rounded-xl text-xs md:text-sm font-bold focus:border-indigo-500 outline-none transition-all" />
              <svg xmlns="http://www.w3.org/2000/svg" class="absolute left-3 md:left-4 top-1/2 transform -translate-y-1/2 h-4 w-4 md:h-5 md:w-5 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
            </div>
          </div>

          <div class="overflow-x-auto flex-1">
            <table class="w-full min-w-[600px]">
              <thead class="bg-indigo-50 sticky top-0">
                <tr>
                  <th class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 text-left text-[8px] md:text-[10px] lg:text-xs font-black text-indigo-600 uppercase tracking-wider">No</th>
                  <th class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 text-left text-[8px] md:text-[10px] lg:text-xs font-black text-indigo-600 uppercase tracking-wider">NIM</th>
                  <th class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 text-left text-[8px] md:text-[10px] lg:text-xs font-black text-indigo-600 uppercase tracking-wider">Nama</th>
                  <th class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 text-center text-[8px] md:text-[10px] lg:text-xs font-black text-indigo-600 uppercase tracking-wider">Total Poin</th>
                  <th class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 text-center text-[8px] md:text-[10px] lg:text-xs font-black text-indigo-600 uppercase tracking-wider">Validasi</th>
                  <th class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 text-center text-[8px] md:text-[10px] lg:text-xs font-black text-indigo-600 uppercase tracking-wider">Aksi</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100">
                <tr v-for="(mhs, idx) in paginatedMhsList" :key="mhs.nim" class="hover:bg-indigo-50/40 transition-all">
                  <td class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 text-xs md:text-sm font-bold text-slate-400">{{ (mhsCurrentPage - 1) * mhsItemsPerPage + idx + 1 }}</td>
                  <td class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 font-mono text-xs md:text-sm font-bold">{{ mhs.nim }}</td>
                  <td class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4">
                    <div class="flex items-center gap-2 md:gap-3">
                      <div class="h-8 w-8 md:h-9 md:w-9 lg:h-10 lg:w-10 bg-gradient-to-br from-indigo-100 to-indigo-200 rounded-xl flex items-center justify-center font-black text-indigo-600 text-xs md:text-sm flex-shrink-0">
                        {{ mhs.nama.charAt(0).toUpperCase() }}
                      </div>
                      <span class="font-bold text-slate-800 text-xs md:text-sm truncate">{{ mhs.nama }}</span>
                    </div>
                  </td>
                  <td class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 text-center font-bold text-emerald-600 text-sm md:text-base">{{ mhs.totalPoin }}</td>
                  <td class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 text-center">
                    <span v-if="mhs.perluFinal > 0" class="inline-flex items-center gap-1 px-2 md:px-3 py-0.5 md:py-1 bg-amber-100 text-amber-700 rounded-full text-[10px] md:text-xs font-bold">
                      ⏳ {{ mhs.perluFinal }}
                    </span>
                    <span v-else class="text-slate-400 text-xs">-</span>
                  </td>
                  <td class="px-3 md:px-4 lg:px-6 py-2 md:py-3 lg:py-4 text-center">
                    <button @click="selectMahasiswa(mhs.nim)" class="px-3 md:px-4 py-1 md:py-2 bg-indigo-600 text-white rounded-xl text-[10px] md:text-xs font-bold hover:bg-indigo-700 transition-all">
                      Lihat Data
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="p-4 border-t bg-slate-50 flex flex-col sm:flex-row justify-between items-center gap-3">
            <span class="text-[10px] md:text-xs text-slate-500">Menampilkan {{ (mhsCurrentPage - 1) * mhsItemsPerPage + 1 }} - {{ Math.min(mhsCurrentPage * mhsItemsPerPage, filteredMhsList.length) }} dari {{ filteredMhsList.length }}</span>
            <div class="flex gap-2">
              <button @click="mhsCurrentPage > 1 ? mhsCurrentPage-- : null" :disabled="mhsCurrentPage === 1" class="px-3 md:px-4 py-1 md:py-2 bg-white border rounded-xl text-[10px] md:text-xs font-bold text-slate-600 hover:bg-indigo-50 disabled:opacity-50 transition-all">←</button>
              <button @click="mhsCurrentPage < mhsTotalPages ? mhsCurrentPage++ : null" :disabled="mhsCurrentPage === mhsTotalPages" class="px-3 md:px-4 py-1 md:py-2 bg-white border rounded-xl text-[10px] md:text-xs font-bold text-slate-600 hover:bg-indigo-50 disabled:opacity-50 transition-all">→</button>
            </div>
          </div>
        </div>
      </div>
    </transition>

    <!-- MODAL PROFILE -->
    <transition name="fade">
      <div v-if="showProfileModal" class="fixed inset-0 z-[60] flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-sm">
        <div class="bg-white rounded-3xl shadow-2xl w-full max-w-sm overflow-hidden text-center p-6 md:p-8 lg:p-10 relative flex flex-col max-h-[95vh]">
          <button @click="showProfileModal = false" class="absolute top-4 right-4 md:top-6 md:right-6 p-2 text-slate-400 hover:bg-rose-50 hover:text-rose-600 rounded-xl transition-all">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 md:h-7 md:w-7" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>
          </button>
          
          <div class="mt-4 md:mt-6 flex justify-center mb-4 md:mb-6">
            <div class="h-24 w-24 md:h-28 md:w-28 lg:h-32 lg:w-32 rounded-3xl overflow-hidden border-4 border-indigo-100 shadow-xl shadow-indigo-200">
              <img v-if="dosenProfile?.avatar" :src="dosenProfile.avatar" class="w-full h-full object-cover" />
              <div v-else class="w-full h-full bg-indigo-600 text-white flex items-center justify-center font-black text-3xl md:text-4xl lg:text-5xl">
                {{ (dosenProfile?.full_name || dosenProfile?.nama || dosenProfile?.username || 'D').charAt(0).toUpperCase() }}
              </div>
            </div>
          </div>
          <h2 class="text-xl md:text-2xl font-black text-slate-800 uppercase tracking-tight leading-tight">{{ dosenProfile?.full_name || dosenProfile?.nama || dosenProfile?.username }}</h2>
          <p class="text-xs md:text-sm font-bold text-indigo-600 uppercase tracking-widest mt-1 md:mt-2">{{ dosenProfile?.nim_nip || dosenProfile?.nidn }}</p>
          <p class="text-sm md:text-base font-bold text-slate-500 mt-1">{{ dosenProfile?.jabatan || 'Dosen Pembimbing' }}</p>

          <div class="mt-6 md:mt-8 space-y-4 md:space-y-5 text-left border-t border-slate-100 pt-6 md:pt-8 overflow-y-auto custom-scroll">
            <div>
              <label class="text-[10px] font-black text-slate-400 uppercase tracking-widest ml-2 block mb-1 md:mb-2">Email</label>
              <input v-model="dosenProfile.email" type="email" class="w-full bg-slate-50 border-2 border-slate-200 rounded-2xl px-4 md:px-5 py-3 md:py-4 text-sm md:text-base font-bold outline-none focus:border-indigo-500 transition-all" />
            </div>
            <div>
              <label class="text-[10px] font-black text-slate-400 uppercase tracking-widest ml-2 block mb-1 md:mb-2">No. WhatsApp</label>
              <input v-model="dosenProfile.no_telp" type="text" class="w-full bg-slate-50 border-2 border-slate-200 rounded-2xl px-4 md:px-5 py-3 md:py-4 text-sm md:text-base font-bold outline-none focus:border-indigo-500 transition-all" />
            </div>
          </div>

          <div class="mt-6 md:mt-8 shrink-0">
            <button @click="updateProfile" class="w-full py-3 md:py-4 bg-indigo-600 text-white font-black rounded-2xl shadow-lg shadow-indigo-200 hover:bg-indigo-700 active:scale-95 transition-all text-xs md:text-sm uppercase tracking-widest">
              Simpan Perubahan
            </button>
          </div>
        </div>
      </div>
    </transition>

  </div>
</template>

<script setup>
import { ref, onMounted, computed, watch } from "vue";
import { useRouter } from "vue-router";
import api from "../api/api";

const router = useRouter();

// STATE UTAMA
const pengajuanList = ref([]);
const mhsBimbinganList = ref([]);
const listKategori = ref([]);
const dosenProfile = ref({ full_name: "", nama: "", username: "", nim_nip: "", nidn: "", jabatan: "", avatar: null, email: "", no_telp: "" });

// UI STATE
const selectedMhsNim = ref(null);
const isShowingAll = ref(false);
const showDetailModal = ref(false);
const showMhsModal = ref(false);
const showProfileModal = ref(false);
const showKategoriModal = ref(false);
const searchKategori = ref("");
const selectedItem = ref({});
const komentarRevisi = ref("");

// STATE UNTUK MODAL MAHASISWA
const searchMhs = ref("");
const mhsCurrentPage = ref(1);
const mhsItemsPerPage = ref(10);

// STATE UNTUK EDIT MODE (KOREKSI)
const isEditMode = ref(false);
const editForm = ref({
  judul_kegiatan: "",
  kategori_id: null,
  kategori_name: "",
  tanggal_kegiatan: "",
  durasi_kegiatan: "",
  bobot_poin_kategori: 0
});

// STATE UNTUK EDIT RIWAYAT
const showEditExistingModal = ref(false);
const selectedEditItem = ref({});
const tempEditMode = ref(false);
const komentarEditExisting = ref("");
const editExistingForm = ref({
  judul_kegiatan: "",
  kategori_id: null,
  kategori_name: "",
  tanggal_kegiatan: "",
  durasi_kegiatan: "",
  bobot_poin_kategori: 0,
  status: ""
});

// DAFTAR STATUS
const availableStatuses = [
  { value: 'pending', label: 'Menunggu Validasi', color: 'amber' },
  { value: 'approved_final', label: 'Disetujui', color: 'emerald' },
  { value: 'rejected', label: 'Ditolak / Revisi', color: 'rose' }
];

// FILTER STATUS UNTUK TABEL UTAMA
const filterStatus = ref("all");
const searchRiwayat = ref("");
const currentPage = ref(1);
const itemsPerPage = ref(10);

// ========== COMPUTED UNTUK MODAL MAHASISWA ==========
const filteredMhsList = computed(() => {
  let list = mhsBimbinganList.value;
  if (searchMhs.value) {
    const q = searchMhs.value.toLowerCase();
    list = list.filter(m => 
      m.nama.toLowerCase().includes(q) || 
      m.nim.toLowerCase().includes(q)
    );
  }
  return list;
});

const mhsTotalPages = computed(() => Math.ceil(filteredMhsList.value.length / mhsItemsPerPage.value) || 1);

const paginatedMhsList = computed(() => {
  const start = (mhsCurrentPage.value - 1) * mhsItemsPerPage.value;
  const end = start + mhsItemsPerPage.value;
  return filteredMhsList.value.slice(start, end);
});

// ========== COMPUTED UNTUK TABEL UTAMA ==========
const displayList = computed(() => {
  let list = pengajuanList.value;

  if (selectedMhsNim.value) {
    list = list.filter(p => (p.nim || p.mahasiswa_nim) === selectedMhsNim.value);
  } else if (!isShowingAll.value) {
    list = list.filter(p => p.status === 'pending');
  }

  if (searchRiwayat.value) {
    const q = searchRiwayat.value.toLowerCase();
    list = list.filter(p => 
      (p.judul_kegiatan || '').toLowerCase().includes(q) ||
      (p.mahasiswa_nama || '').toLowerCase().includes(q) ||
      (p.nim || p.mahasiswa_nim || '').toLowerCase().includes(q) ||
      (p.kategori_name || p.nama_kategori || '').toLowerCase().includes(q)
    );
  }
  
  return list;
});

const filteredByStatusList = computed(() => {
  let list = displayList.value;
  if (filterStatus.value !== "all") {
    list = list.filter(p => p.status === filterStatus.value);
  }
  return list;
});

const totalPages = computed(() => Math.ceil((isShowingAll ? filteredByStatusList.value : displayList.value).length / itemsPerPage.value) || 1);

const paginatedList = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value;
  const end = start + itemsPerPage.value;
  return displayList.value.slice(start, end);
});

const paginatedFilteredList = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value;
  const end = start + itemsPerPage.value;
  return filteredByStatusList.value.slice(start, end);
});

const totalBelumFinal = computed(() => {
  return pengajuanList.value.filter(p => p.status === 'pending').length;
});

// WATCHERS
watch([selectedMhsNim, isShowingAll, searchRiwayat, filterStatus], () => {
  currentPage.value = 1;
});

watch(searchMhs, () => {
  mhsCurrentPage.value = 1;
});

// HELPER FUNCTIONS
const getNamaKegiatanFromKategori = (item) => {
  const kategoriId = item.kategori || item.kategori_id;
  if (kategoriId && listKategori.value.length > 0) {
    const kat = listKategori.value.find(k => k.id === kategoriId);
    if (kat) return kat.nama_kegiatan || kat.kegiatan;
  }
  return item.nama_kategori || item.kategori_name || "Tidak ada kategori";
};

const statusClass = (status) => {
  const s = String(status).toLowerCase();
  if (s === 'approved_final' || s === 'valid') return 'bg-emerald-50 text-emerald-700 border-emerald-200';
  if (s === 'rejected' || s === 'tolak') return 'bg-rose-50 text-rose-700 border-rose-200';
  if (s === 'pending') return 'bg-amber-50 text-amber-700 border-amber-200';
  return 'bg-slate-100 text-slate-600 border-slate-200';
};

const formatStatusLabel = (status) => {
  const s = String(status).toLowerCase();
  if (s === 'approved_final' || s === 'valid') return 'DISETUJUI';
  if (s === 'rejected' || s === 'tolak') return 'DITOLAK';
  if (s === 'pending') return 'MENUNGGU';
  return s.toUpperCase();
};

const isImage = (url) => /\.(jpeg|jpg|gif|png|webp)$/i.test(url);
const isPdf = (url) => /\.pdf$/i.test(url);

// Grouping functions
const groupBySifat = (items) => {
  const groups = { 'Wajib': [], 'Pilihan': [], 'Lainnya': [] };
  items.forEach(item => {
    const sifat = (item.sifat || '').toLowerCase();
    if (sifat === 'wajib' || sifat.includes('wajib')) {
      groups['Wajib'].push(item);
    } else if (sifat === 'pilihan' || sifat.includes('pilihan')) {
      groups['Pilihan'].push(item);
    } else {
      groups['Lainnya'].push(item);
    }
  });
  const result = {};
  for (const key in groups) {
    if (groups[key].length > 0) result[key] = groups[key];
  }
  return result;
};

const groupByNamaKegiatan = (items) => {
  const groups = {};
  items.forEach(item => {
    const nama = item.nama_kegiatan || item.kegiatan || 'Tidak Bernama';
    if (!groups[nama]) groups[nama] = [];
    groups[nama].push(item);
  });
  const sortedGroups = {};
  Object.keys(groups).sort().forEach(key => {
    sortedGroups[key] = groups[key];
  });
  return sortedGroups;
};

const groupedKategori = computed(() => {
  const groups = {};
  const filtered = listKategori.value.filter(k => {
    if (!searchKategori.value) return true;
    const q = searchKategori.value.toLowerCase();
    return (k.level || '').toLowerCase().includes(q) ||
           (k.bidang || '').toLowerCase().includes(q) ||
           (k.sifat || '').toLowerCase().includes(q) ||
           (k.nama_kegiatan || k.kegiatan || '').toLowerCase().includes(q) ||
           (k.partisipasi || '').toLowerCase().includes(q);
  });
  
  filtered.forEach(kat => {
    const level = kat.level || 'Tidak Ada Level';
    if (!groups[level]) groups[level] = { byBidang: {} };
    const bidang = kat.bidang || 'Tidak Ada Bidang';
    if (!groups[level].byBidang[bidang]) groups[level].byBidang[bidang] = [];
    groups[level].byBidang[bidang].push(kat);
  });
  
  const sortedGroups = {};
  Object.keys(groups).sort().forEach(level => {
    sortedGroups[level] = { byBidang: {}, totalCount: 0 };
    Object.keys(groups[level].byBidang).sort().forEach(bidang => {
      const sortedItems = [...groups[level].byBidang[bidang]].sort((a, b) => {
        const sifatA = a.sifat || '';
        const sifatB = b.sifat || '';
        if (sifatA !== sifatB) return sifatA.localeCompare(sifatB);
        const namaA = a.nama_kegiatan || a.kegiatan || '';
        const namaB = b.nama_kegiatan || b.kegiatan || '';
        if (namaA !== namaB) return namaA.localeCompare(namaB);
        const peranA = a.partisipasi || '';
        const peranB = b.partisipasi || '';
        return peranA.localeCompare(peranB);
      });
      sortedGroups[level].byBidang[bidang] = sortedItems;
      sortedGroups[level].totalCount += sortedItems.length;
    });
  });
  return sortedGroups;
});

const pilihKategori = (kat) => {
  if (tempEditMode.value) {
    editExistingForm.value.kategori_id = kat.id;
    editExistingForm.value.kategori_name = `${kat.nama_kegiatan || kat.kegiatan} (${kat.poin || kat.bobot_poin || 0} Poin)`;
    editExistingForm.value.bobot_poin_kategori = kat.poin || kat.bobot_poin || 0;
    tempEditMode.value = false;
  } else {
    editForm.value.kategori_id = kat.id;
    editForm.value.kategori_name = `${kat.nama_kegiatan || kat.kegiatan} (${kat.poin || kat.bobot_poin || 0} Poin)`;
    editForm.value.bobot_poin_kategori = kat.poin || kat.bobot_poin || 0;
  }
  showKategoriModal.value = false;
};

// API CALLS
const fetchDosenProfile = async () => {
  try {
    const res = await api.get("api/users/me/");
    dosenProfile.value = res.data;
  } catch (err) {
    if (err.response?.status === 401) router.push("/login");
  }
};

const updateProfile = async () => {
  try {
    await api.patch("api/users/me/", { 
      email: dosenProfile.value.email, 
      no_telp: dosenProfile.value.no_telp 
    });
    alert("Profil berhasil diperbarui!");
    showProfileModal.value = false;
  } catch (err) {
    console.error("Gagal update profil", err);
    alert("Terjadi kesalahan saat memperbarui profil.");
  }
};

const fetchKategori = async () => {
  try {
    const res = await api.get("api/kategori/");
    listKategori.value = res.data;
  } catch (err) {
    console.error("Gagal memuat kategori", err);
  }
};

const fetchPengajuan = async () => {
  try {
    const res = await api.get("api/kegiatan/");
    const allData = res.data;
    pengajuanList.value = allData;
    
    const map = new Map();
    allData.forEach((item) => {
      const nim = item.nim || item.mahasiswa_nim;
      if (!nim) return;
      
      const poin = Number(item.bobot_poin_kategori) || 0;
      if (!map.has(nim)) {
        map.set(nim, {
          nama: item.mahasiswa_nama,
          nim,
          totalPoin: item.status === 'approved_final' ? poin : 0,
          perluFinal: item.status === 'pending' ? 1 : 0
        });
      } else {
        const m = map.get(nim);
        if (item.status === 'approved_final') m.totalPoin += poin;
        if (item.status === 'pending') m.perluFinal += 1;
      }
    });
    mhsBimbinganList.value = Array.from(map.values());
  } catch (err) {
    if (err.response?.status === 401) router.push("/login");
  }
};

// ACTIONS
const openDetail = (item) => {
  selectedItem.value = { ...item };
  komentarRevisi.value = item.komentar_dpa || "";
  isEditMode.value = false;
  showDetailModal.value = true;
};

const closeDetail = () => {
  showDetailModal.value = false;
  isEditMode.value = false;
};

const openEditExisting = (item) => {
  selectedEditItem.value = { ...item };
  komentarEditExisting.value = item.komentar_dpa || "";
  
  editExistingForm.value = {
    judul_kegiatan: item.judul_kegiatan || "",
    kategori_id: item.kategori || item.kategori_id,
    kategori_name: getNamaKegiatanFromKategori(item),
    tanggal_kegiatan: item.tanggal_kegiatan || "",
    durasi_kegiatan: item.durasi_kegiatan || "",
    bobot_poin_kategori: item.bobot_poin_kategori || 0,
    status: item.status || "pending"
  };
  showEditExistingModal.value = true;
};

const closeEditExistingModal = () => {
  showEditExistingModal.value = false;
  komentarEditExisting.value = "";
  tempEditMode.value = false;
};

const saveEditExisting = async () => {
  if (editExistingForm.value.status === 'rejected' && !komentarEditExisting.value.trim()) {
    alert("⚠️ Status Ditolak/Revisi wajib diisi komentar!");
    return;
  }
  
  try {
    const payload = {
      status: editExistingForm.value.status,
      is_edited_by_dpa: true,
      komentar_dpa: komentarEditExisting.value || "-"
    };
    
    if (editExistingForm.value.kategori_id) payload.kategori_id = editExistingForm.value.kategori_id;
    if (editExistingForm.value.tanggal_kegiatan) payload.tanggal_kegiatan = editExistingForm.value.tanggal_kegiatan;
    if (editExistingForm.value.durasi_kegiatan) payload.durasi_kegiatan = editExistingForm.value.durasi_kegiatan;
    
    await api.patch(`api/kegiatan/${selectedEditItem.value.id}/`, payload);
    alert("✅ Data berhasil diperbarui!");
    closeEditExistingModal();
    await fetchPengajuan();
  } catch (err) {
    alert("Gagal menyimpan perubahan.");
    console.error(err);
  }
};

const submitTolakRevisi = async () => {
  if (!komentarRevisi.value || komentarRevisi.value.trim() === '') {
    alert("Mohon sertakan alasan penolakan!");
    return;
  }
  try {
    await api.patch(`api/kegiatan/${selectedItem.value.id}/`, {
      status: 'rejected',
      komentar_dpa: komentarRevisi.value
    });
    alert("Pengajuan ditolak.");
    showDetailModal.value = false;
    await fetchPengajuan();
  } catch (err) {
    alert("Gagal memperbarui status.");
  }
};

const updateStatus = async (id, statusBaru) => {
  try {
    await api.patch(`api/kegiatan/${id}/`, { 
      status: statusBaru,
      komentar_dpa: komentarRevisi.value || "-"
    });
    alert("✅ Pengajuan disetujui!");
    showDetailModal.value = false;
    await fetchPengajuan();
  } catch (err) {
    alert("Gagal memperbarui status.");
  }
};

const selectMahasiswa = (nim) => { 
  selectedMhsNim.value = nim; 
  isShowingAll.value = false; 
  showMhsModal.value = false; 
  searchRiwayat.value = ""; 
  filterStatus.value = "all";
};

const showAllData = () => { 
  selectedMhsNim.value = null; 
  isShowingAll.value = true; 
  showMhsModal.value = false; 
  searchRiwayat.value = ""; 
  filterStatus.value = "all";
};

const resetFilter = () => { 
  selectedMhsNim.value = null; 
  isShowingAll.value = false; 
  showMhsModal.value = false; 
  searchRiwayat.value = ""; 
  filterStatus.value = "all";
};

const handleLogout = () => { 
  if(confirm("Apakah Anda yakin ingin keluar?")) { 
    localStorage.removeItem('access_token'); 
    router.push("/login"); 
  } 
};

const hitungDurasiOtomatis = (item) => {
  if (item.durasi_kegiatan && item.durasi_kegiatan !== '-') {
    return item.durasi_kegiatan;
  }
  if (item.jam_mulai && item.jam_selesai) {
    return 'Dihitung dalam Jam';
  }
  return '1 Hari';
};

const downloadFile = async (url) => {
  if (!url) return alert("Tidak ada file.");
  try {
    window.open(url, '_blank');
  } catch (err) {
    alert("Gagal membuka file.");
  }
};

onMounted(() => { 
  fetchDosenProfile(); 
  fetchKategori();
  fetchPengajuan(); 
});
</script>

<style scoped>
.fade-enter-active, .fade-leave-active { transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); }
.fade-enter-from, .fade-leave-to { opacity: 0; transform: scale(0.95) translateY(10px); }

.custom-scroll::-webkit-scrollbar { width: 4px; }
.custom-scroll::-webkit-scrollbar-track { background: transparent; }
.custom-scroll::-webkit-scrollbar-thumb { background: #475569; border-radius: 10px; }
.custom-scroll::-webkit-scrollbar-thumb:hover { background: #1e293b; }

/* Responsive table */
@media (max-width: 640px) {
  .min-w-\[600px\] {
    min-width: 500px;
  }
}
</style>