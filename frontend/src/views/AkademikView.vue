<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-50 via-indigo-50/20 to-slate-50 flex font-sans selection:bg-indigo-100 selection:text-indigo-900">
    <!-- SIDEBAR PREMIUM -->
    <aside class="w-72 bg-gradient-to-b from-slate-800 to-slate-900 flex flex-col shadow-xl fixed h-full z-50 text-white">
      <div class="p-6 flex items-center gap-4 border-b border-white/10">
        <div class="h-12 w-12 bg-white rounded-xl flex items-center justify-center shadow-lg overflow-hidden">
          <img 
            src="/stie-sbilogo.jpg" 
            alt="STIE SBI Logo" 
            class="h-full w-full object-cover"
            @error="(e) => e.target.src = ''"
          />
        </div>
        <div class="flex flex-col">
          <span class="font-bold text-xl tracking-tight">SKPM</span>
          <span class="text-xs text-indigo-300">STIE SBI Yogyakarta</span>
        </div>
      </div>

      <nav class="flex-1 p-4 space-y-2 overflow-y-auto custom-scroll mt-4">
        <a href="#" @click.prevent="changeMenu('dashboard')" 
           :class="['w-full flex items-center gap-4 px-5 py-3.5 rounded-xl transition-all duration-200', activeMenu === 'dashboard' ? 'bg-indigo-600 text-white shadow-lg shadow-indigo-600/30' : 'text-slate-400 hover:bg-slate-700/50 hover:text-white']">
          <span class="text-xl">📊</span>
          <span class="font-semibold text-sm">Dashboard</span>
        </a>

        <a href="#" @click.prevent="changeMenu('monitoring')" 
           :class="['w-full flex items-center gap-4 px-5 py-3.5 rounded-xl transition-all duration-200', activeMenu === 'monitoring' ? 'bg-indigo-600 text-white shadow-lg shadow-indigo-600/30' : 'text-slate-400 hover:bg-slate-700/50 hover:text-white']">
          <span class="text-xl">📋</span>
          <span class="font-semibold text-sm">Monitoring DPA</span>
        </a>

        <a href="#" @click.prevent="changeMenu('kategori')" 
           :class="['w-full flex items-center gap-4 px-5 py-3.5 rounded-xl transition-all duration-200', activeMenu === 'kategori' ? 'bg-indigo-600 text-white shadow-lg shadow-indigo-600/30' : 'text-slate-400 hover:bg-slate-700/50 hover:text-white']">
          <span class="text-xl">🏷️</span>
          <span class="font-semibold text-sm">Kelola Kategori</span>
        </a>

        <a href="#" @click.prevent="changeMenu('mahasiswa')" 
           :class="['w-full flex items-center gap-4 px-5 py-3.5 rounded-xl transition-all duration-200', activeMenu === 'mahasiswa' ? 'bg-indigo-600 text-white shadow-lg shadow-indigo-600/30' : 'text-slate-400 hover:bg-slate-700/50 hover:text-white']">
          <span class="text-xl">👥</span>
          <span class="font-semibold text-sm">Plotting DPA & Mahasiswa</span>
        </a>
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
    <main class="flex-1 ml-72 p-6 lg:p-10 overflow-y-auto">
      <!-- HEADER PREMIUM DENGAN LOGOUT DI KANAN -->
      <header class="mb-8">
        <div class="bg-gradient-to-r from-indigo-600 via-indigo-700 to-indigo-800 rounded-3xl p-8 text-white shadow-2xl shadow-indigo-200/30 relative overflow-hidden">
          <div class="absolute top-0 right-0 w-64 h-64 bg-white/5 rounded-full -mr-32 -mt-32"></div>
          <div class="absolute bottom-0 left-0 w-48 h-48 bg-white/5 rounded-full -ml-24 -mb-24"></div>
          
          <div class="relative z-10 flex flex-col md:flex-row justify-between items-start md:items-center gap-6">
            <div>
              <div class="flex items-center gap-3 mb-2">
                <div class="h-12 w-12 bg-white/20 rounded-2xl flex items-center justify-center backdrop-blur-sm">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
                  </svg>
                </div>
                <div>
                  <h1 class="text-2xl lg:text-3xl font-black tracking-tight">
                    {{ activeMenu === 'dashboard' ? 'Panel Bagian Akademik' : activeMenu === 'monitoring' ? 'Monitoring Aktivitas DPA' : activeMenu === 'kategori' ? 'Manajemen Kategori SKPM' : 'Data Mahasiswa & Plotting DPA' }}
                  </h1>
                  <p class="text-indigo-200 text-sm mt-1">Verifikator Pusat • STIE SBI Yogyakarta</p>
                </div>
              </div>
            </div>
            
            <!-- TOMBOL LOGOUT DI SAMPING KANAN -->
            <button 
              @click="handleLogout"
              class="flex items-center gap-2 bg-rose-500 hover:bg-rose-600 text-white px-5 md:px-6 py-2.5 md:py-3 rounded-xl transition-all duration-200 font-bold text-sm shadow-lg shadow-rose-200/50 flex-shrink-0"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
              </svg>
              <span>Logout</span>
            </button>
          </div>
        </div>
      </header>

      <!-- DASHBOARD MENU -->
      <div v-if="activeMenu === 'dashboard'">
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          <div class="group bg-white p-6 rounded-2xl shadow-sm hover:shadow-xl transition-all duration-300 border border-slate-100 hover:border-indigo-200">
            <div class="h-14 w-14 bg-gradient-to-br from-blue-500 to-blue-600 rounded-2xl flex items-center justify-center mb-4 shadow-lg shadow-blue-200 group-hover:scale-110 transition-transform">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>
            </div>
            <p class="text-slate-500 text-xs font-black uppercase tracking-wider mb-1">Total Pengajuan</p>
            <h4 class="text-3xl font-black text-slate-800">{{ listPengajuan.length }} <span class="text-base font-medium text-slate-400">Berkas</span></h4>
            <div class="mt-3 h-1 w-full bg-slate-100 rounded-full overflow-hidden">
              <div class="h-full w-full bg-blue-500 rounded-full" style="width: 100%"></div>
            </div>
          </div>

          <div class="group bg-white p-6 rounded-2xl shadow-sm hover:shadow-xl transition-all duration-300 border border-slate-100 hover:border-amber-200">
            <div class="h-14 w-14 bg-gradient-to-br from-amber-500 to-amber-600 rounded-2xl flex items-center justify-center mb-4 shadow-lg shadow-amber-200 group-hover:scale-110 transition-transform">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
            </div>
            <p class="text-slate-500 text-xs font-black uppercase tracking-wider mb-1">Menunggu Validasi</p>
            <h4 class="text-3xl font-black text-slate-800">{{ listPengajuan.filter(i => i.status === 'pending').length }} <span class="text-base font-medium text-slate-400">Berkas</span></h4>
            <div class="mt-3 h-1 w-full bg-slate-100 rounded-full overflow-hidden">
              <div class="h-full bg-amber-500 rounded-full" :style="{ width: (listPengajuan.filter(i => i.status === 'pending').length / (listPengajuan.length || 1) * 100) + '%' }"></div>
            </div>
          </div>

          <div class="group bg-white p-6 rounded-2xl shadow-sm hover:shadow-xl transition-all duration-300 border border-slate-100 hover:border-emerald-200">
            <div class="h-14 w-14 bg-gradient-to-br from-emerald-500 to-emerald-600 rounded-2xl flex items-center justify-center mb-4 shadow-lg shadow-emerald-200 group-hover:scale-110 transition-transform">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
            </div>
            <p class="text-slate-500 text-xs font-black uppercase tracking-wider mb-1">Tervalidasi</p>
            <h4 class="text-3xl font-black text-slate-800">{{ listPengajuan.filter(i => String(i.status).toLowerCase() === 'approved_final' || String(i.status).toLowerCase() === 'valid').length }} <span class="text-base font-medium text-slate-400">Berkas</span></h4>
            <div class="mt-3 h-1 w-full bg-slate-100 rounded-full overflow-hidden">
              <div class="h-full bg-emerald-500 rounded-full" :style="{ width: (listPengajuan.filter(i => String(i.status).toLowerCase() === 'approved_final' || String(i.status).toLowerCase() === 'valid').length / (listPengajuan.length || 1) * 100) + '%' }"></div>
            </div>
          </div>

          <div class="group bg-white p-6 rounded-2xl shadow-sm hover:shadow-xl transition-all duration-300 border border-slate-100 hover:border-rose-200">
            <div class="h-14 w-14 bg-gradient-to-br from-rose-500 to-rose-600 rounded-2xl flex items-center justify-center mb-4 shadow-lg shadow-rose-200 group-hover:scale-110 transition-transform">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
            </div>
            <p class="text-slate-500 text-xs font-black uppercase tracking-wider mb-1">Ditolak</p>
            <h4 class="text-3xl font-black text-slate-800">{{ listPengajuan.filter(i => i.status === 'rejected' || i.status === 'tolak').length }} <span class="text-base font-medium text-slate-400">Berkas</span></h4>
            <div class="mt-3 h-1 w-full bg-slate-100 rounded-full overflow-hidden">
              <div class="h-full bg-rose-500 rounded-full" :style="{ width: (listPengajuan.filter(i => i.status === 'rejected' || i.status === 'tolak').length / (listPengajuan.length || 1) * 100) + '%' }"></div>
            </div>
          </div>
        </div>

        <div v-if="listPendingPengajuan.length > 0" class="mb-8 p-5 bg-gradient-to-r from-amber-50 to-amber-100/50 rounded-2xl border-l-4 border-amber-500 flex items-center gap-4">
          <div class="h-10 w-10 bg-amber-500 rounded-xl flex items-center justify-center shadow-md">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
            </svg>
          </div>
          <div>
            <p class="font-bold text-amber-800">Pemberitahuan Validasi</p>
            <p class="text-sm text-amber-700">Terdapat <b>{{ listPendingPengajuan.length }}</b> pengajuan baru yang memerlukan validasi dari Anda.</p>
          </div>
        </div>

        <div class="bg-white rounded-2xl shadow-lg border border-slate-200 overflow-hidden">
          <div class="p-6 border-b border-slate-200 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 bg-gradient-to-r from-slate-50 to-white">
            <div>
              <h2 class="text-lg lg:text-xl font-bold text-slate-800 flex items-center gap-3">
                <div class="h-2 w-2 bg-indigo-500 rounded-full animate-pulse"></div>
                Antrean Validasi Berkas
              </h2>
              <p class="text-sm text-slate-500 mt-1">Daftar pengajuan SKPM mahasiswa yang perlu diverifikasi</p>
            </div>
            <div class="inline-flex items-center gap-2 px-4 py-2 bg-amber-100 text-amber-800 rounded-xl font-bold shadow-sm">
              <span class="w-2 h-2 bg-amber-500 rounded-full animate-pulse"></span>
              {{ listPendingPengajuan.length }} Antrean Menunggu
            </div>
          </div>
          
          <div class="overflow-x-auto">
            <table class="w-full">
              <thead class="bg-slate-100/80 border-b-2 border-slate-200">
                <tr>
                  <th class="px-6 py-4 text-left text-xs font-bold text-slate-500 uppercase tracking-wider w-16">No</th>
                  <th class="px-6 py-4 text-left text-xs font-bold text-slate-500 uppercase tracking-wider">Data Mahasiswa</th>
                  <th class="px-6 py-4 text-left text-xs font-bold text-slate-500 uppercase tracking-wider">Detail Kegiatan</th>
                  <th class="px-6 py-4 text-center text-xs font-bold text-slate-500 uppercase tracking-wider">Poin</th>
                  <th class="px-6 py-4 text-center text-xs font-bold text-slate-500 uppercase tracking-wider">Aksi</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100">
                <tr v-for="(item, idx) in paginatedPendingPengajuan" :key="item.id" class="hover:bg-indigo-50/40 transition-colors group">
                  <td class="px-6 py-4 text-sm font-bold text-slate-500 text-center">{{ (pendingPage - 1) * pendingItemsPerPage + idx + 1 }}</td>
                  <td class="px-6 py-4">
                    <div class="flex items-center gap-3">
                      <div class="h-10 w-10 bg-gradient-to-br from-indigo-100 to-indigo-200 rounded-xl flex items-center justify-center font-bold text-indigo-600">
                        {{ (item.mahasiswa_nama || 'M').charAt(0).toUpperCase() }}
                      </div>
                      <div>
                        <p class="font-bold text-slate-800 group-hover:text-indigo-600 transition-colors">{{ item.mahasiswa_nama }}</p>
                        <p class="text-xs font-mono text-slate-500">NIM: {{ item.nim || item.mahasiswa_nim }}</p>
                      </div>
                    </div>
                  </td>
                  <td class="px-6 py-4">
                    <p class="text-sm font-semibold text-slate-700 max-w-xs truncate">{{ item.judul_kegiatan }}</p>
                    <span class="inline-block text-xs bg-slate-100 text-slate-600 px-2 py-1 rounded-md mt-1">{{ item.nama_kategori }}</span>
                  </td>
                  <td class="px-6 py-4 text-center">
                    <span class="inline-flex items-center justify-center w-14 h-14 bg-gradient-to-br from-blue-500 to-blue-600 text-white font-black text-xl rounded-2xl shadow-md">
                      {{ item.bobot_poin_kategori || item.poin_valid || 0 }}
                    </span>
                  </td>
                  <td class="px-6 py-4 text-center">
                    <div class="flex gap-2 justify-center">
                      <button @click="openDetailModal(item)" class="px-4 py-2 bg-white border border-slate-200 rounded-xl text-slate-600 font-semibold text-sm hover:bg-indigo-600 hover:text-white hover:border-indigo-600 transition-all shadow-sm inline-flex items-center gap-2">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                        Cek Detail
                      </button>
                      <button @click="openEditStatus(item)" class="px-4 py-2 bg-amber-50 border border-amber-200 rounded-xl text-amber-600 font-semibold text-sm hover:bg-amber-500 hover:text-white transition-all shadow-sm inline-flex items-center gap-2">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" /></svg>
                        Ubah Status
                      </button>
                    </div>
                  </td>
                </tr>
                <tr v-if="listPendingPengajuan.length === 0">
                  <td colspan="5" class="px-6 py-16 text-center">
                    <div class="text-6xl mb-4 opacity-40">✅</div>
                    <p class="text-slate-500 font-semibold text-base">Tidak ada antrean validasi!</p>
                    <p class="text-slate-400 text-sm mt-1">Semua pengajuan sudah diproses.</p>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <div v-if="listPendingPengajuan.length > 0" class="p-5 border-t border-slate-200 bg-slate-50/80 flex flex-col sm:flex-row justify-between items-center gap-4">
            <span class="text-sm text-slate-500">
              Menampilkan <strong class="text-slate-700">{{ (pendingPage - 1) * pendingItemsPerPage + 1 }}</strong> - 
              <strong class="text-slate-700">{{ Math.min(pendingPage * pendingItemsPerPage, listPendingPengajuan.length) }}</strong> 
              dari <strong class="text-slate-700">{{ listPendingPengajuan.length }}</strong> antrean
            </span>
            <div class="flex gap-2">
              <button @click="pendingPage > 1 ? pendingPage-- : null" :disabled="pendingPage === 1" class="px-5 py-2 bg-white border border-slate-200 rounded-lg text-sm font-semibold text-slate-600 hover:bg-indigo-50 hover:text-indigo-600 hover:border-indigo-200 disabled:opacity-50 disabled:cursor-not-allowed transition-all">
                ← Sebelumnya
              </button>
              <button v-for="page in pendingTotalPages" :key="page" @click="pendingPage = page" :class="['px-3 py-2 rounded-lg text-sm font-semibold transition-all', pendingPage === page ? 'bg-indigo-600 text-white shadow-md' : 'bg-white border border-slate-200 text-slate-600 hover:bg-indigo-50']">
                {{ page }}
              </button>
              <button @click="pendingPage < pendingTotalPages ? pendingPage++ : null" :disabled="pendingPage === pendingTotalPages" class="px-5 py-2 bg-white border border-slate-200 rounded-lg text-sm font-semibold text-slate-600 hover:bg-indigo-50 hover:text-indigo-600 hover:border-indigo-200 disabled:opacity-50 disabled:cursor-not-allowed transition-all">
                Selanjutnya →
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- MONITORING DPA MENU -->
      <div v-if="activeMenu === 'monitoring'">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <div class="group bg-white p-6 rounded-2xl shadow-sm hover:shadow-xl transition-all duration-300 border border-slate-100 hover:border-indigo-200">
            <div class="h-14 w-14 bg-gradient-to-br from-indigo-500 to-indigo-600 rounded-2xl flex items-center justify-center mb-4 shadow-lg shadow-indigo-200 group-hover:scale-110 transition-transform">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" /></svg>
            </div>
            <p class="text-slate-500 text-xs font-black uppercase tracking-wider mb-1">Total DPA Aktif</p>
            <h4 class="text-3xl font-black text-slate-800">{{ listDPA.length }} <span class="text-base font-medium text-slate-400">Dosen</span></h4>
            <div class="mt-3 h-1 w-full bg-slate-100 rounded-full overflow-hidden">
              <div class="h-full w-full bg-indigo-500 rounded-full" style="width: 100%"></div>
            </div>
          </div>

          <div class="group bg-white p-6 rounded-2xl shadow-sm hover:shadow-xl transition-all duration-300 border border-slate-100 hover:border-emerald-200">
            <div class="h-14 w-14 bg-gradient-to-br from-emerald-500 to-emerald-600 rounded-2xl flex items-center justify-center mb-4 shadow-lg shadow-emerald-200 group-hover:scale-110 transition-transform">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
            </div>
            <p class="text-slate-500 text-xs font-black uppercase tracking-wider mb-1">Total Validasi DPA</p>
            <h4 class="text-3xl font-black text-slate-800">{{ totalDpaActions }} <span class="text-base font-medium text-slate-400">Aksi</span></h4>
            <div class="mt-3 h-1 w-full bg-slate-100 rounded-full overflow-hidden">
              <div class="h-full bg-emerald-500 rounded-full" style="width: 100%"></div>
            </div>
          </div>

          <div class="group bg-white p-6 rounded-2xl shadow-sm hover:shadow-xl transition-all duration-300 border border-slate-100 hover:border-purple-200">
            <div class="h-14 w-14 bg-gradient-to-br from-purple-500 to-purple-600 rounded-2xl flex items-center justify-center mb-4 shadow-lg shadow-purple-200 group-hover:scale-110 transition-transform">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" /></svg>
            </div>
            <p class="text-slate-500 text-xs font-black uppercase tracking-wider mb-1">Rata-rata per DPA</p>
            <h4 class="text-3xl font-black text-slate-800">{{ avgActionsPerDpa }} <span class="text-base font-medium text-slate-400">Aksi/DPA</span></h4>
            <div class="mt-3 h-1 w-full bg-slate-100 rounded-full overflow-hidden">
              <div class="h-full bg-purple-500 rounded-full" style="width: 100%"></div>
            </div>
          </div>
        </div>

        <div class="bg-white rounded-2xl shadow-lg border border-slate-200 overflow-hidden">
          <div class="p-6 border-b border-slate-200 bg-gradient-to-r from-slate-50 to-white">
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
              <div>
                <h2 class="text-lg lg:text-xl font-bold text-slate-800 flex items-center gap-3">
                  <div class="h-2 w-2 bg-indigo-500 rounded-full animate-pulse"></div>
                  Aktivitas Validasi DPA
                </h2>
                <p class="text-sm text-slate-500 mt-1">Seluruh riwayat perubahan status yang dilakukan oleh Dosen Pembimbing.</p>
              </div>
              <div class="flex gap-3">
                <div class="relative">
                  <svg xmlns="http://www.w3.org/2000/svg" class="absolute left-4 top-1/2 transform -translate-y-1/2 h-5 w-5 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
                  <input v-model="searchDpaActivity" type="text" placeholder="Cari DPA atau Mahasiswa..." class="pl-11 pr-4 py-2.5 bg-white border-2 border-slate-200 rounded-xl text-sm focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100 outline-none w-64">
                </div>
                <select v-model="filterActivityStatus" class="px-4 py-2.5 bg-white border-2 border-slate-200 rounded-xl text-sm font-semibold text-slate-700 focus:border-indigo-500 outline-none cursor-pointer">
                  <option value="all">📋 Semua Status</option>
                  <option value="pending">🕒 Menunggu</option>
                  <option value="approved_dpa">🔵 DPA ACC</option>
                  <option value="approved_final">✅ Disetujui Final</option>
                  <option value="rejected">❌ Ditolak</option>
                </select>
                <button @click="fetchDpaActivities" class="px-5 py-2.5 bg-indigo-600 text-white rounded-xl font-semibold text-sm hover:bg-indigo-700 transition-all shadow-md inline-flex items-center gap-2">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" /></svg>
                  Refresh
                </button>
              </div>
            </div>
            
            <div class="mt-4 flex items-center gap-2 text-sm text-indigo-600 bg-indigo-50 px-4 py-2 rounded-xl">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <span>Total <strong>{{ filteredDpaActivities.length }}</strong> aktivitas validasi dari <strong>{{ totalDpaActions }}</strong> keseluruhan</span>
            </div>
          </div>

          <div class="overflow-x-auto">
            <table class="w-full">
              <thead class="bg-slate-100/80 border-b-2 border-slate-200">
                <tr>
                  <th class="px-6 py-4 text-left text-xs font-bold text-slate-500 uppercase tracking-wider">No</th>
                  <th class="px-6 py-4 text-left text-xs font-bold text-slate-500 uppercase tracking-wider">DPA / Validator</th>
                  <th class="px-6 py-4 text-left text-xs font-bold text-slate-500 uppercase tracking-wider">Mahasiswa</th>
                  <th class="px-6 py-4 text-left text-xs font-bold text-slate-500 uppercase tracking-wider">Judul Kegiatan</th>
                  <th class="px-6 py-4 text-center text-xs font-bold text-slate-500 uppercase tracking-wider">Status</th>
                  <th class="px-6 py-4 text-left text-xs font-bold text-slate-500 uppercase tracking-wider">Komentar</th>
                  <th class="px-6 py-4 text-center text-xs font-bold text-slate-500 uppercase tracking-wider">Waktu</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100">
                <tr v-for="(activity, index) in paginatedDpaActivities" :key="activity.id" class="hover:bg-indigo-50/40 transition-colors group">
                  <td class="px-6 py-4 text-sm font-bold text-slate-500">{{ (dpaActivityPage - 1) * dpaActivityItemsPerPage + index + 1 }}</td>
                  <td class="px-6 py-4">
                    <div class="flex items-center gap-3">
                      <div class="h-10 w-10 bg-gradient-to-br from-indigo-100 to-indigo-200 rounded-xl flex items-center justify-center font-bold text-indigo-600">
                        {{ getDpaInitials(activity) }}
                      </div>
                      <div>
                        <p class="font-bold text-slate-800">{{ getDpaNameFromActivity(activity) }}</p>
                        <p class="text-xs text-slate-500">{{ getDpaNip(activity) }}</p>
                      </div>
                    </div>
                  </td>
                  <td class="px-6 py-4">
                    <p class="font-semibold text-slate-800">{{ activity.mahasiswa_nama }}</p>
                    <p class="text-xs text-slate-500">NIM: {{ activity.nim || activity.mahasiswa_nim }}</p>
                  </td>
                  <td class="px-6 py-4">
                    <p class="text-sm font-medium text-slate-700 max-w-xs truncate">{{ activity.judul_kegiatan }}</p>
                  </td>
                  <td class="px-6 py-4 text-center">
                    <span :class="getStatusBadgeClass(activity.status)" class="px-3 py-1.5 rounded-full text-xs font-bold whitespace-nowrap inline-flex items-center gap-1 border shadow-sm">
                      {{ formatStatusLabel(activity.status) }}
                    </span>
                    <span v-if="activity.is_edited_by_dpa" class="inline-flex items-center gap-1 text-xs font-bold text-amber-600 ml-2">
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" viewBox="0 0 20 20" fill="currentColor"><path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" /></svg>
                      Diedit
                    </span>
                  </td>
                  <td class="px-6 py-4">
                    <p class="text-sm text-slate-600 max-w-xs truncate" :title="activity.komentar_dpa">{{ activity.komentar_dpa || '-' }}</p>
                  </td>
                  <td class="px-6 py-4 text-center text-sm text-slate-500">
                    {{ formatDate(activity.updated_at || activity.created_at) }}
                  </td>
                </tr>
                <tr v-if="filteredDpaActivities.length === 0">
                  <td colspan="7" class="px-6 py-16 text-center">
                    <div class="text-6xl mb-4 opacity-40">📋</div>
                    <p class="text-slate-500 font-semibold text-base">Belum ada aktivitas validasi DPA</p>
                    <p class="text-slate-400 text-sm mt-1">Data akan muncul ketika DPA melakukan validasi.</p>
                    <button @click="fetchDpaActivities" class="mt-4 px-4 py-2 bg-indigo-600 text-white rounded-lg text-sm font-semibold hover:bg-indigo-700 transition-all">
                      🔄 Refresh Data
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <div v-if="filteredDpaActivities.length > 0" class="p-5 border-t border-slate-200 bg-slate-50/80 flex flex-col sm:flex-row justify-between items-center gap-4">
            <span class="text-sm text-slate-500">
              Menampilkan <strong class="text-slate-700">{{ (dpaActivityPage - 1) * dpaActivityItemsPerPage + 1 }}</strong> - 
              <strong class="text-slate-700">{{ Math.min(dpaActivityPage * dpaActivityItemsPerPage, filteredDpaActivities.length) }}</strong> 
              dari <strong class="text-slate-700">{{ filteredDpaActivities.length }}</strong> aktivitas
            </span>
            <div class="flex gap-2">
              <button @click="dpaActivityPage > 1 ? dpaActivityPage-- : null" :disabled="dpaActivityPage === 1" class="px-5 py-2 bg-white border border-slate-200 rounded-lg text-sm font-semibold text-slate-600 hover:bg-indigo-50 hover:text-indigo-600 hover:border-indigo-200 disabled:opacity-50 disabled:cursor-not-allowed transition-all">
                ← Sebelumnya
              </button>
              <button v-for="page in dpaActivityTotalPages" :key="page" @click="dpaActivityPage = page" :class="['px-3 py-2 rounded-lg text-sm font-semibold transition-all', dpaActivityPage === page ? 'bg-indigo-600 text-white shadow-md' : 'bg-white border border-slate-200 text-slate-600 hover:bg-indigo-50']">
                {{ page }}
              </button>
              <button @click="dpaActivityPage < dpaActivityTotalPages ? dpaActivityPage++ : null" :disabled="dpaActivityPage === dpaActivityTotalPages" class="px-5 py-2 bg-white border border-slate-200 rounded-lg text-sm font-semibold text-slate-600 hover:bg-indigo-50 hover:text-indigo-600 hover:border-indigo-200 disabled:opacity-50 disabled:cursor-not-allowed transition-all">
                Selanjutnya →
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- KATEGORI MENU -->
      <div v-if="activeMenu === 'kategori'">
        <div class="grid grid-cols-1 xl:grid-cols-2 gap-8">
          <div class="bg-white rounded-2xl shadow-lg border border-slate-200 overflow-hidden">
            <div class="p-6 border-b border-slate-200 bg-gradient-to-r from-indigo-50 to-white">
              <h2 class="text-xl font-bold text-slate-800 flex items-center gap-3">
                <div class="h-2 w-2 bg-indigo-500 rounded-full"></div>
                Formulir Tambah Kategori Baru
              </h2>
              <p class="text-sm text-slate-500 mt-1">Isi formulir di bawah ini untuk menambahkan kategori kegiatan.</p>
            </div>
            
            <form @submit.prevent="submitKategori" class="p-6 space-y-5">
              <div>
                <label class="block text-xs font-black text-slate-500 uppercase tracking-wider mb-2">Bidang Kegiatan</label>
                <div class="relative">
                  <svg xmlns="http://www.w3.org/2000/svg" class="absolute left-4 top-1/2 transform -translate-y-1/2 h-5 w-5 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" /></svg>
                  <input v-model="newKategori.bidang" type="text" class="w-full pl-12 pr-4 py-4 bg-slate-50 border-2 border-slate-200 rounded-xl text-base font-medium focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100 outline-none transition-all" required />
                </div>
              </div>
              <div>
                <label class="block text-xs font-black text-slate-500 uppercase tracking-wider mb-2">Nama Detail Kegiatan</label>
                <div class="relative">
                  <svg xmlns="http://www.w3.org/2000/svg" class="absolute left-4 top-1/2 transform -translate-y-1/2 h-5 w-5 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" /></svg>
                  <input v-model="newKategori.nama_kegiatan" type="text" class="w-full pl-12 pr-4 py-4 bg-slate-50 border-2 border-slate-200 rounded-xl text-base font-medium focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100 outline-none transition-all" required />
                </div>
              </div>
              
              <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
                <div>
                  <label class="block text-xs font-black text-slate-500 uppercase tracking-wider mb-2">Partisipasi (Peran)</label>
                  <div class="relative">
                    <svg xmlns="http://www.w3.org/2000/svg" class="absolute left-4 top-1/2 transform -translate-y-1/2 h-5 w-5 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" /></svg>
                    <input v-model="newKategori.partisipasi" type="text" placeholder="Contoh: Ketua / Anggota" class="w-full pl-12 pr-4 py-4 bg-slate-50 border-2 border-slate-200 rounded-xl text-base font-medium focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100 outline-none transition-all" />
                  </div>
                </div>
                <div>
                  <label class="block text-xs font-black text-slate-500 uppercase tracking-wider mb-2">Tingkatan / Level</label>
                  <div class="relative">
                    <svg xmlns="http://www.w3.org/2000/svg" class="absolute left-4 top-1/2 transform -translate-y-1/2 h-5 w-5 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3" /></svg>
                    <select v-model="newKategori.level" class="w-full pl-12 pr-4 py-4 bg-slate-50 border-2 border-slate-200 rounded-xl text-base font-medium focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100 outline-none transition-all appearance-none cursor-pointer" required>
                      <option value="" disabled selected>-- Pilih Tingkat --</option>
                      <option value="Lokal/Daerah">🏛️ Tingkat Lokal / Daerah</option>
                      <option value="Nasional">🇮🇩 Tingkat Nasional</option>
                      <option value="Internasional">🌍 Tingkat Internasional</option>
                    </select>
                  </div>
                </div>
              </div>

              <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
                <div>
                  <label class="block text-xs font-black text-slate-500 uppercase tracking-wider mb-2">Sifat Kegiatan</label>
                  <div class="relative">
                    <svg xmlns="http://www.w3.org/2000/svg" class="absolute left-4 top-1/2 transform -translate-y-1/2 h-5 w-5 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l5 5a2 2 0 01.586 1.414V19a2 2 0 01-2 2H7a2 2 0 01-2-2V5a2 2 0 012-2z" /></svg>
                    <select v-model="newKategori.sifat" class="w-full pl-12 pr-4 py-4 bg-slate-50 border-2 border-slate-200 rounded-xl text-base font-medium focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100 outline-none transition-all appearance-none cursor-pointer" required>
                      <option value="Pilihan">⭐ Sifat Pilihan</option>
                      <option value="Wajib">📌 Sifat Wajib</option>
                    </select>
                  </div>
                </div>
                <div>
                  <label class="block text-xs font-black text-slate-500 uppercase tracking-wider mb-2">Bobot Poin</label>
                  <div class="relative">
                    <svg xmlns="http://www.w3.org/2000/svg" class="absolute left-4 top-1/2 transform -translate-y-1/2 h-5 w-5 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z" /></svg>
                    <input v-model="newKategori.bobot_poin" type="number" class="w-full pl-12 pr-4 py-4 bg-slate-50 border-2 border-slate-200 rounded-xl text-xl font-bold focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100 outline-none transition-all" required />
                  </div>
                </div>
              </div>

              <div class="pt-4">
                <button type="submit" :disabled="loadingKategori" class="w-full py-4 bg-gradient-to-r from-indigo-600 to-indigo-700 text-white font-black rounded-xl hover:from-indigo-700 hover:to-indigo-800 transition-all shadow-lg shadow-indigo-200 text-sm uppercase tracking-wider flex items-center justify-center gap-2">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" /></svg>
                  {{ loadingKategori ? 'Menyimpan Data...' : 'Simpan Kategori Baru' }}
                </button>
              </div>
            </form>
          </div>

          <div class="bg-white rounded-2xl shadow-lg border border-slate-200 overflow-hidden flex flex-col">
            <div class="p-6 border-b border-slate-200 bg-gradient-to-r from-slate-50 to-white">
              <h2 class="text-xl font-bold text-slate-800 flex items-center gap-3">
                <div class="h-2 w-2 bg-indigo-500 rounded-full"></div>
                Daftar Kategori Aktif
              </h2>
            </div>
            <div class="flex-1 overflow-y-auto custom-scroll p-4 space-y-4 max-h-[600px]">
              <div v-for="kat in listKategori" :key="kat.id" class="bg-white p-5 rounded-xl border-2 border-slate-200 hover:border-indigo-300 hover:shadow-lg transition-all">
                <div class="flex flex-col lg:flex-row justify-between gap-4">
                  <div class="flex-1">
                    <div class="flex flex-wrap gap-2 mb-3">
                      <span class="inline-flex items-center gap-1 px-3 py-1 bg-indigo-50 text-indigo-700 text-xs font-black uppercase tracking-wider rounded-lg">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" /></svg>
                        {{ kat.bidang }}
                      </span>
                      <span class="inline-flex items-center gap-1 px-3 py-1 bg-amber-50 text-amber-600 text-xs font-black uppercase tracking-wider rounded-lg">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l5 5a2 2 0 01.586 1.414V19a2 2 0 01-2 2H7a2 2 0 01-2-2V5a2 2 0 012-2z" /></svg>
                        {{ kat.sifat }}
                      </span>
                    </div>
                    <p class="font-bold text-slate-800 text-lg mb-2">{{ kat.nama_kegiatan }}</p>
                    <div class="grid grid-cols-2 gap-2 text-sm text-slate-600">
                      <p>Peran: <strong class="text-slate-800">{{ kat.partisipasi || '-' }}</strong></p>
                      <p>Level: <strong class="text-slate-800">{{ kat.level || '-' }}</strong></p>
                    </div>
                  </div>
                  
                  <div class="flex flex-row lg:flex-col items-center gap-4 bg-slate-50 p-4 rounded-xl border border-slate-200">
                    <div class="text-center">
                      <span class="text-xs font-black text-slate-500 uppercase tracking-wider">Poin</span>
                      <span class="block text-3xl font-black text-indigo-600">{{ kat.bobot_poin }}</span>
                    </div>
                    <div class="flex gap-2">
                      <button @click="openEditKategori(kat)" class="px-4 py-2 bg-white border border-amber-200 rounded-lg text-amber-600 font-semibold text-sm hover:bg-amber-500 hover:text-white transition-all">
                        ✏️ Edit
                      </button>
                      <button @click="hapusKategori(kat.id)" class="px-4 py-2 bg-white border border-rose-200 rounded-lg text-rose-600 font-semibold text-sm hover:bg-rose-500 hover:text-white transition-all">
                        🗑️ Hapus
                      </button>
                    </div>
                  </div>
                </div>
              </div>
              <div v-if="listKategori.length === 0" class="text-center py-12">
                <div class="text-6xl mb-4 opacity-40">🏷️</div>
                <p class="text-slate-500 font-semibold text-lg">Belum ada kategori terdaftar</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- PLOTTING DPA & MAHASISWA MENU -->
      <div v-if="activeMenu === 'mahasiswa'">
        <div class="bg-white rounded-2xl shadow-lg border border-slate-200 overflow-hidden">
          <div class="p-6 border-b border-slate-200 bg-gradient-to-r from-slate-50 to-white">
            <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
              <div>
                <h2 class="text-xl font-bold text-slate-800 flex items-center gap-3">
                  <div class="h-2 w-2 bg-indigo-500 rounded-full animate-pulse"></div>
                  Daftar Plotting DPA & Mahasiswa
                </h2>
                <p class="text-sm text-slate-500 mt-1">Daftar seluruh mahasiswa yang terdaftar di sistem beserta Dosen Pembimbing (DPA).</p>
              </div>
              
              <div class="flex flex-col sm:flex-row gap-3">
                <div class="relative">
                  <svg xmlns="http://www.w3.org/2000/svg" class="absolute left-4 top-1/2 transform -translate-y-1/2 h-5 w-5 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
                  <input v-model="searchMahasiswa" type="text" placeholder="Cari Nama atau NIM..." class="pl-11 pr-4 py-2.5 bg-white border-2 border-slate-200 rounded-xl text-sm focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100 outline-none w-64">
                </div>
                <button @click="openPlotDPABaru" class="px-5 py-2.5 bg-gradient-to-r from-indigo-600 to-indigo-700 text-white rounded-xl font-bold text-sm hover:from-indigo-700 hover:to-indigo-800 transition-all shadow-md inline-flex items-center gap-2">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 5a1 1 0 011 1v3h3a1 1 0 110 2h-3v3a1 1 0 11-2 0v-3H6a1 1 0 110-2h3V6a1 1 0 011-1z" clip-rule="evenodd" /></svg>
                  Plot DPA Baru
                </button>
              </div>
            </div>
          </div>
          
          <div class="overflow-x-auto">
            <table class="w-full">
              <thead class="bg-slate-100/80 border-b-2 border-slate-200">
                <tr>
                  <th class="px-6 py-4 text-left text-xs font-bold text-slate-500 uppercase tracking-wider w-16">No</th>
                  <th class="px-6 py-4 text-left text-xs font-bold text-slate-500 uppercase tracking-wider">Nama Mahasiswa</th>
                  <th class="px-6 py-4 text-left text-xs font-bold text-slate-500 uppercase tracking-wider">NIM</th>
                  <th class="px-6 py-4 text-center text-xs font-bold text-slate-500 uppercase tracking-wider">Total Poin SKPM</th>
                  <th class="px-6 py-4 text-left text-xs font-bold text-slate-500 uppercase tracking-wider">Dosen Pembimbing (DPA)</th>
                  <th class="px-6 py-4 text-left text-xs font-bold text-slate-500 uppercase tracking-wider">NIP DPA</th>
                  <th class="px-6 py-4 text-center text-xs font-bold text-slate-500 uppercase tracking-wider">Aksi</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100">
                <tr v-for="(mhs, index) in paginatedMahasiswa" :key="mhs.id" class="hover:bg-indigo-50/40 transition-colors group">
                  <td class="px-6 py-4 text-sm font-bold text-slate-500 text-center">{{ (mahasiswaPage - 1) * mahasiswaItemsPerPage + index + 1 }}</td>
                  <td class="px-6 py-4">
                    <div class="flex items-center gap-3">
                      <div class="h-10 w-10 bg-gradient-to-br from-indigo-100 to-indigo-200 rounded-xl flex items-center justify-center font-bold text-indigo-600">
                        {{ (mhs.full_name || mhs.username || 'M').charAt(0).toUpperCase() }}
                      </div>
                      <p class="font-bold text-slate-800">{{ mhs.full_name || mhs.username || 'Tanpa Nama' }}</p>
                    </div>
                  </td>
                  <td class="px-6 py-4">
                    <span class="font-mono text-sm font-bold bg-slate-100 text-slate-700 px-3 py-1.5 rounded-lg">{{ mhs.nim_nip || '-' }}</span>
                  </td>
                  <td class="px-6 py-4 text-center">
                    <div class="inline-flex items-center gap-2 px-4 py-2.5 bg-emerald-50 rounded-xl">
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-emerald-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                      <span class="text-xl font-black text-emerald-700">{{ hitungTotalPoin(mhs) }}</span>
                      <span class="text-xs font-bold text-emerald-500">POIN</span>
                    </div>
                  </td>
                  <td class="px-6 py-4">
                    <div v-if="getDpaName(mhs) !== '-'" class="flex items-center gap-2">
                      <span class="w-2 h-2 bg-green-500 rounded-full"></span>
                      <span class="font-semibold text-slate-800">{{ getDpaName(mhs) }}</span>
                    </div>
                    <div v-else class="flex items-center gap-2">
                      <span class="w-2 h-2 bg-rose-500 rounded-full"></span>
                      <span class="text-rose-600 font-medium">Belum Punya DPA</span>
                    </div>
                  </td>
                  <td class="px-6 py-4">
                    <span class="text-sm text-slate-600">{{ getDpaNipFromMahasiswa(mhs) }}</span>
                  </td>
                  <td class="px-6 py-4 text-center">
                    <div class="flex gap-2 justify-center">
                      <button @click="openEditMahasiswa(mhs)" class="px-4 py-2 bg-amber-50 border border-amber-200 rounded-lg text-amber-600 font-semibold text-sm hover:bg-amber-500 hover:text-white transition-all inline-flex items-center gap-1">
                        ✏️ Edit
                      </button>
                      <button @click="hapusPlotting(mhs)" class="px-4 py-2 bg-rose-50 border border-rose-200 rounded-lg text-rose-600 font-semibold text-sm hover:bg-rose-500 hover:text-white transition-all inline-flex items-center gap-1">
                        🗑️ Hapus Plot
                      </button>
                    </div>
                  </td>
                </tr>
                <tr v-if="filteredMahasiswa.length === 0">
                  <td colspan="7" class="px-6 py-16 text-center">
                    <div class="text-6xl mb-4 opacity-40">👥</div>
                    <p class="text-slate-500 font-semibold text-base">Tidak ada data mahasiswa</p>
                    <p class="text-slate-400 text-sm mt-1">Data mahasiswa akan muncul setelah terdaftar di sistem.</p>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <div v-if="filteredMahasiswa.length > 0" class="p-5 border-t border-slate-200 bg-slate-50/80 flex flex-col sm:flex-row justify-between items-center gap-4">
            <span class="text-sm text-slate-500">
              Menampilkan <strong class="text-slate-700">{{ (mahasiswaPage - 1) * mahasiswaItemsPerPage + 1 }}</strong> - 
              <strong class="text-slate-700">{{ Math.min(mahasiswaPage * mahasiswaItemsPerPage, filteredMahasiswa.length) }}</strong> 
              dari <strong class="text-slate-700">{{ filteredMahasiswa.length }}</strong> mahasiswa
            </span>
            <div class="flex gap-2">
              <button @click="mahasiswaPage > 1 ? mahasiswaPage-- : null" :disabled="mahasiswaPage === 1" class="px-5 py-2 bg-white border border-slate-200 rounded-lg text-sm font-semibold text-slate-600 hover:bg-indigo-50 hover:text-indigo-600 hover:border-indigo-200 disabled:opacity-50 disabled:cursor-not-allowed transition-all">
                ← Sebelumnya
              </button>
              <button v-for="page in mahasiswaTotalPages" :key="page" @click="mahasiswaPage = page" :class="['px-3 py-2 rounded-lg text-sm font-semibold transition-all', mahasiswaPage === page ? 'bg-indigo-600 text-white shadow-md' : 'bg-white border border-slate-200 text-slate-600 hover:bg-indigo-50']">
                {{ page }}
              </button>
              <button @click="mahasiswaPage < mahasiswaTotalPages ? mahasiswaPage++ : null" :disabled="mahasiswaPage === mahasiswaTotalPages" class="px-5 py-2 bg-white border border-slate-200 rounded-lg text-sm font-semibold text-slate-600 hover:bg-indigo-50 hover:text-indigo-600 hover:border-indigo-200 disabled:opacity-50 disabled:cursor-not-allowed transition-all">
                Selanjutnya →
              </button>
            </div>
          </div>
        </div>
      </div>
    </main>

    <!-- MODAL DETAIL PENGAJUAN -->
    <transition name="modal">
      <div v-if="showDetailModal" class="fixed inset-0 bg-slate-900/80 backdrop-blur-sm z-[60] flex items-center justify-center p-4">
        <div class="bg-white rounded-3xl shadow-2xl w-full max-w-2xl max-h-[90vh] overflow-hidden flex flex-col">
          <div class="p-6 border-b border-slate-100 flex justify-between items-center bg-gradient-to-r from-indigo-600 to-indigo-700">
            <div class="flex items-center gap-4">
              <div class="h-12 w-12 bg-white/20 rounded-2xl flex items-center justify-center backdrop-blur-sm">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
              </div>
              <div>
                <h3 class="text-2xl font-black text-white uppercase tracking-tight">DETAIL PENGAJUAN</h3>
                <p class="text-sm text-indigo-200 mt-0.5">Informasi lengkap pengajuan SKPM Mahasiswa</p>
              </div>
            </div>
            <button @click="showDetailModal = false" class="text-white/70 hover:text-white hover:bg-white/20 h-10 w-10 flex items-center justify-center rounded-xl transition-all text-2xl">&times;</button>
          </div>
          
          <div class="flex-1 overflow-y-auto p-6 bg-gradient-to-br from-slate-50 to-white custom-scroll">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
              <div class="bg-gradient-to-r from-indigo-50 to-white p-5 rounded-xl border border-indigo-100">
                <div class="flex items-center gap-3 mb-2">
                  <div class="h-10 w-10 bg-indigo-100 rounded-xl flex items-center justify-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-indigo-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" /></svg>
                  </div>
                  <div>
                    <p class="text-xs font-black text-indigo-500 uppercase tracking-wider">Nama Mahasiswa</p>
                    <p class="text-base font-bold text-slate-800">{{ selectedDetail.mahasiswa_nama || '-' }}</p>
                  </div>
                </div>
              </div>
              <div class="bg-gradient-to-r from-indigo-50 to-white p-5 rounded-xl border border-indigo-100">
                <div class="flex items-center gap-3 mb-2">
                  <div class="h-10 w-10 bg-indigo-100 rounded-xl flex items-center justify-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-indigo-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V8a2 2 0 00-2-2h-5m-4 0V5a2 2 0 114 0v1m-4 0a2 2 0 104 0m-5 8a2 2 0 100-4 2 2 0 000 4zm0 0c1.306 0 2.417.835 2.83 2M9 14a3.001 3.001 0 00-2.83 2M15 11h3m-3 4h2" /></svg>
                  </div>
                  <div>
                    <p class="text-xs font-black text-indigo-500 uppercase tracking-wider">NIM</p>
                    <p class="text-base font-bold text-slate-800 font-mono">{{ selectedDetail.nim || selectedDetail.mahasiswa_nim || '-' }}</p>
                  </div>
                </div>
              </div>
            </div>

            <div class="bg-white p-5 rounded-xl border border-slate-200 mb-6 shadow-sm">
              <div class="flex items-center gap-2 mb-3">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-indigo-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>
                <p class="text-xs font-black text-slate-400 uppercase tracking-wider">JUDUL KEGIATAN</p>
              </div>
              <p class="text-base font-bold text-slate-800">{{ selectedDetail.judul_kegiatan || '-' }}</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
              <div class="bg-slate-50 p-5 rounded-xl border border-slate-200">
                <div class="flex items-center gap-2 mb-2">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-emerald-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" /></svg>
                  <p class="text-xs font-black text-slate-400 uppercase tracking-wider">TANGGAL PELAKSANAAN</p>
                </div>
                <p class="text-base font-bold text-slate-800">{{ formatDate(selectedDetail.tanggal_pelaksanaan || selectedDetail.tanggal_kegiatan || selectedDetail.tanggal) }}</p>
              </div>
              <div class="bg-slate-50 p-5 rounded-xl border border-slate-200">
                <div class="flex items-center gap-2 mb-2">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-emerald-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                  <p class="text-xs font-black text-slate-400 uppercase tracking-wider">DURASI</p>
                </div>
                <p class="text-base font-bold text-slate-800">{{ selectedDetail.durasi_pelaksanaan || selectedDetail.durasi_kegiatan || selectedDetail.durasi || '-' }}</p>
              </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
              <div class="bg-slate-50 p-5 rounded-xl border border-slate-200">
                <div class="flex items-center gap-2 mb-2">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-indigo-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l5 5a2 2 0 01.586 1.414V19a2 2 0 01-2 2H7a2 2 0 01-2-2V5a2 2 0 012-2z" /></svg>
                  <p class="text-xs font-black text-slate-400 uppercase tracking-wider">KATEGORI</p>
                </div>
                <p class="text-base font-bold text-slate-800">{{ selectedDetail.nama_kategori || '-' }}</p>
              </div>
              <div class="bg-gradient-to-br from-blue-50 to-indigo-50 p-5 rounded-xl border border-blue-200 text-center">
                <div class="flex items-center justify-center gap-2 mb-1">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z" /></svg>
                  <p class="text-xs font-black text-blue-500 uppercase tracking-wider">POIN YANG DIAJUKAN</p>
                </div>
                <p class="text-5xl font-black text-blue-600">{{ selectedDetail.bobot_poin_kategori || selectedDetail.poin_valid || 0 }}</p>
              </div>
            </div>

            <div v-if="selectedDetail.bukti_sertifikat" class="bg-slate-50 p-5 rounded-xl border border-slate-200 mb-6">
              <div class="flex items-center gap-2 mb-3">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-emerald-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>
                <p class="text-xs font-black text-slate-400 uppercase tracking-wider">BERKAS SERTIFIKAT</p>
              </div>
              <a :href="getFileUrl(selectedDetail.bukti_sertifikat)" target="_blank" class="inline-flex items-center gap-2 px-5 py-3 bg-emerald-600 text-white rounded-xl font-bold hover:bg-emerald-700 transition-all shadow-md">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" /></svg>
                ☑ Lihat Berkas
              </a>
            </div>

            <div class="bg-gradient-to-r from-amber-50 to-amber-100/50 p-5 rounded-xl border border-amber-200">
              <div class="flex items-center gap-2 mb-2">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-amber-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                <p class="text-xs font-black text-amber-700 uppercase tracking-wider">STATUS SAAT INI</p>
              </div>
              <span :class="getStatusBadgeClass(selectedDetail.status)" class="px-4 py-2 rounded-xl text-sm font-bold inline-flex items-center gap-2 border shadow-sm">
                {{ formatStatusLabel(selectedDetail.status) }}
              </span>
            </div>
          </div>
          
          <div class="p-6 border-t border-slate-200 bg-slate-50 flex justify-end">
            <button @click="showDetailModal = false" class="px-8 py-3 bg-slate-600 text-white font-black rounded-xl hover:bg-slate-700 transition-all shadow-md text-sm uppercase tracking-wider">
              TUTUP PANEL
            </button>
          </div>
        </div>
      </div>
    </transition>

    <!-- MODAL EDIT STATUS -->
    <transition name="modal">
      <div v-if="showEditStatusModal" class="fixed inset-0 bg-slate-900/80 backdrop-blur-sm z-[60] flex items-center justify-center p-4">
        <div class="bg-white rounded-3xl shadow-2xl w-full max-w-md overflow-hidden">
          <div class="p-6 border-b border-slate-100 bg-gradient-to-r from-amber-500 to-orange-600">
            <h3 class="text-2xl font-black text-white text-center uppercase tracking-tight">Ubah Status</h3>
            <p class="text-sm text-amber-100 text-center mt-1">Nama: <strong>{{ selectedPengajuan.mahasiswa_nama }}</strong></p>
          </div>
          <div class="p-6 space-y-3">
            <button @click="saveEditStatus('pending')" :class="['w-full p-4 rounded-xl border-2 transition-all text-left font-bold flex items-center gap-3', String(selectedPengajuan.status).toLowerCase() === 'pending' ? 'border-amber-500 bg-amber-50 text-amber-900' : 'border-slate-200 bg-white text-slate-700 hover:bg-amber-50']">
              <span class="text-2xl">🕒</span>
              <div>
                <p class="font-bold">Kembalikan ke Menunggu</p>
                <p class="text-xs opacity-70">Set status menjadi pending/menunggu validasi</p>
              </div>
            </button>
            <button @click="saveEditStatus('approved_final')" :class="['w-full p-4 rounded-xl border-2 transition-all text-left font-bold flex items-center gap-3', String(selectedPengajuan.status).toLowerCase() === 'approved_final' ? 'border-emerald-500 bg-emerald-50 text-emerald-900' : 'border-slate-200 bg-white text-slate-700 hover:bg-emerald-50']">
              <span class="text-2xl">✅</span>
              <div>
                <p class="font-bold">Setujui Dokumen</p>
                <p class="text-xs opacity-70">Validasi pengajuan dan tambahkan poin</p>
              </div>
            </button>
            <button @click="openRejectModal(selectedPengajuan)" :class="['w-full p-4 rounded-xl border-2 transition-all text-left font-bold flex items-center gap-3', String(selectedPengajuan.status).toLowerCase() === 'rejected' ? 'border-rose-500 bg-rose-50 text-rose-900' : 'border-slate-200 bg-white text-slate-700 hover:bg-rose-50']">
              <span class="text-2xl">❌</span>
              <div>
                <p class="font-bold">Tolak Dokumen</p>
                <p class="text-xs opacity-70">Tolak pengajuan dengan alasan</p>
              </div>
            </button>
          </div>
          <div class="p-6 border-t border-slate-200 bg-slate-50">
            <button @click="showEditStatusModal = false" class="w-full py-3 bg-slate-200 hover:bg-slate-300 text-slate-800 rounded-xl font-bold transition-all">Batal</button>
          </div>
        </div>
      </div>
    </transition>

    <!-- MODAL REJECT -->
    <transition name="modal">
      <div v-if="showRejectModal" class="fixed inset-0 bg-slate-900/80 backdrop-blur-sm z-[60] flex items-center justify-center p-4">
        <div class="bg-white rounded-3xl shadow-2xl w-full max-w-md overflow-hidden">
          <div class="p-6 border-b border-slate-100 bg-gradient-to-r from-rose-500 to-rose-600">
            <h3 class="text-2xl font-black text-white text-center uppercase tracking-tight">Tolak Pengajuan</h3>
          </div>
          <div class="p-6">
            <label class="block text-sm font-bold text-slate-700 mb-2">Alasan Penolakan <span class="text-rose-500">*</span></label>
            <textarea v-model="rejectReason" rows="4" class="w-full p-4 bg-slate-50 border-2 border-slate-200 focus:border-rose-500 rounded-xl outline-none transition-all resize-none" placeholder="Tuliskan alasan penolakan di sini..."></textarea>
            <p class="text-xs text-slate-500 mt-2">Alasan ini akan terlihat oleh mahasiswa.</p>
          </div>
          <div class="p-6 border-t border-slate-200 bg-slate-50 flex gap-3">
            <button @click="showRejectModal = false" class="flex-1 py-3 bg-slate-200 hover:bg-slate-300 text-slate-800 rounded-xl font-bold transition-all">Batal</button>
            <button @click="confirmReject" :disabled="!rejectReason.trim()" :class="['flex-1 py-3 text-white rounded-xl font-bold transition-all', rejectReason.trim() ? 'bg-rose-600 hover:bg-rose-700' : 'bg-slate-400 cursor-not-allowed']">Konfirmasi</button>
          </div>
        </div>
      </div>
    </transition>

    <!-- MODAL EDIT KATEGORI -->
    <transition name="modal">
      <div v-if="showEditKategoriModal" class="fixed inset-0 bg-slate-900/80 backdrop-blur-sm z-[60] flex items-center justify-center p-4">
        <div class="bg-white rounded-3xl shadow-2xl w-full max-w-2xl max-h-[90vh] overflow-y-auto">
          <div class="p-6 border-b border-slate-100 bg-gradient-to-r from-indigo-600 to-indigo-700">
            <h3 class="text-2xl font-black text-white uppercase tracking-tight">Edit Kategori</h3>
          </div>
          <div class="p-6 space-y-5">
            <div>
              <label class="block text-xs font-black text-slate-500 uppercase tracking-wider mb-2">Bidang Kegiatan</label>
              <input v-model="selectedKategori.bidang" type="text" class="w-full p-4 bg-slate-50 border-2 border-slate-200 rounded-xl focus:border-indigo-500 outline-none transition-all" required />
            </div>
            <div>
              <label class="block text-xs font-black text-slate-500 uppercase tracking-wider mb-2">Nama Detail Kegiatan</label>
              <input v-model="selectedKategori.nama_kegiatan" type="text" class="w-full p-4 bg-slate-50 border-2 border-slate-200 rounded-xl focus:border-indigo-500 outline-none transition-all" required />
            </div>
            <div class="grid grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-black text-slate-500 uppercase tracking-wider mb-2">Partisipasi</label>
                <input v-model="selectedKategori.partisipasi" type="text" class="w-full p-4 bg-slate-50 border-2 border-slate-200 rounded-xl focus:border-indigo-500 outline-none transition-all" />
              </div>
              <div>
                <label class="block text-xs font-black text-slate-500 uppercase tracking-wider mb-2">Level</label>
                <select v-model="selectedKategori.level" class="w-full p-4 bg-slate-50 border-2 border-slate-200 rounded-xl focus:border-indigo-500 outline-none transition-all">
                  <option value="Lokal/Daerah">Tingkat Lokal / Daerah</option>
                  <option value="Nasional">Tingkat Nasional</option>
                  <option value="Internasional">Tingkat Internasional</option>
                </select>
              </div>
            </div>
            <div class="grid grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-black text-slate-500 uppercase tracking-wider mb-2">Sifat</label>
                <select v-model="selectedKategori.sifat" class="w-full p-4 bg-slate-50 border-2 border-slate-200 rounded-xl focus:border-indigo-500 outline-none transition-all">
                  <option value="Pilihan">Sifat Pilihan</option>
                  <option value="Wajib">Sifat Wajib</option>
                </select>
              </div>
              <div>
                <label class="block text-xs font-black text-slate-500 uppercase tracking-wider mb-2">Bobot Poin</label>
                <input v-model="selectedKategori.bobot_poin" type="number" class="w-full p-4 bg-slate-50 border-2 border-slate-200 rounded-xl text-xl font-bold focus:border-indigo-500 outline-none transition-all" required />
              </div>
            </div>
          </div>
          <div class="p-6 border-t border-slate-200 bg-slate-50 flex gap-3">
            <button @click="showEditKategoriModal = false" class="flex-1 py-3 bg-slate-200 hover:bg-slate-300 text-slate-800 rounded-xl font-bold transition-all">Batal</button>
            <button @click="saveEditKategori" class="flex-1 py-3 bg-indigo-600 hover:bg-indigo-700 text-white rounded-xl font-bold transition-all">Simpan</button>
          </div>
        </div>
      </div>
    </transition>

    <!-- MODAL PLOT DPA BARU -->
    <transition name="modal">
      <div v-if="showPlotDPAModal" class="fixed inset-0 bg-slate-900/80 backdrop-blur-sm z-[60] flex items-center justify-center p-4">
        <div class="bg-white rounded-3xl shadow-2xl w-full max-w-6xl max-h-[90vh] overflow-hidden flex flex-col">
          <div class="p-6 border-b border-slate-100 bg-gradient-to-r from-indigo-600 to-indigo-700">
            <div class="flex justify-between items-center">
              <div>
                <h3 class="text-2xl font-black text-white uppercase tracking-tight">Plot Dosen Pembimbing Baru</h3>
                <p class="text-sm text-indigo-200 mt-1">Cari dan pilih Mahasiswa serta DPA yang akan dihubungkan.</p>
              </div>
              <button @click="showPlotDPAModal = false" class="text-white/70 hover:text-white hover:bg-white/20 h-10 w-10 flex items-center justify-center rounded-xl transition-all text-2xl">&times;</button>
            </div>
          </div>
          
          <div class="flex-1 overflow-hidden p-6">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 h-full">
              <div class="flex flex-col border border-slate-200 rounded-xl overflow-hidden bg-white shadow-sm">
                <div class="p-4 bg-slate-50 border-b border-slate-200">
                  <label class="block text-sm font-bold text-slate-700 mb-2">1. Pilih Mahasiswa</label>
                  <div class="relative">
                    <svg xmlns="http://www.w3.org/2000/svg" class="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
                    <input v-model="searchPlotMahasiswa" type="text" placeholder="Cari Nama atau NIM..." class="w-full pl-10 pr-4 py-2.5 bg-white border border-slate-200 rounded-lg focus:border-indigo-500 outline-none transition-all">
                  </div>
                </div>
                <div class="flex-1 overflow-y-auto custom-scroll">
                  <table class="w-full text-sm">
                    <thead class="bg-slate-100 sticky top-0">
                      <tr><th class="py-2 px-3 w-12 text-center">Pilih</th><th class="py-2 px-3 text-left">Mahasiswa</th></tr>
                    </thead>
                    <tbody>
                      <tr v-for="mhs in filteredPlotMahasiswa" :key="mhs.id" @click="formPlotDPA.mahasiswa_id = mhs.id" :class="['cursor-pointer hover:bg-indigo-50 transition-colors', formPlotDPA.mahasiswa_id === mhs.id ? 'bg-indigo-100' : '']">
                        <td class="py-2 px-3 text-center"><input type="radio" :value="mhs.id" v-model="formPlotDPA.mahasiswa_id" class="w-4 h-4"></td>
                        <td class="py-2 px-3"><p class="font-semibold">{{ mhs.full_name || mhs.username }}</p><p class="text-xs text-slate-500">NIM: {{ mhs.nim_nip }}</p></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>

              <div class="flex flex-col border border-slate-200 rounded-xl overflow-hidden bg-white shadow-sm">
                <div class="p-4 bg-slate-50 border-b border-slate-200">
                  <label class="block text-sm font-bold text-slate-700 mb-2">2. Pilih Dosen Pembimbing (DPA)</label>
                  <div class="relative">
                    <svg xmlns="http://www.w3.org/2000/svg" class="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
                    <input v-model="searchPlotDPA" type="text" placeholder="Cari Nama atau NIP..." class="w-full pl-10 pr-4 py-2.5 bg-white border border-slate-200 rounded-lg focus:border-indigo-500 outline-none transition-all">
                  </div>
                </div>
                <div class="flex-1 overflow-y-auto custom-scroll">
                  <table class="w-full text-sm">
                    <thead class="bg-slate-100 sticky top-0">
                      <tr><th class="py-2 px-3 w-12 text-center">Pilih</th><th class="py-2 px-3 text-left">Dosen</th></tr>
                    </thead>
                    <tbody>
                      <tr v-for="dosen in filteredPlotDPA" :key="dosen.id" @click="formPlotDPA.dpa_id = dosen.id" :class="['cursor-pointer hover:bg-indigo-50 transition-colors', formPlotDPA.dpa_id === dosen.id ? 'bg-indigo-100' : '']">
                        <td class="py-2 px-3 text-center"><input type="radio" :value="dosen.id" v-model="formPlotDPA.dpa_id" class="w-4 h-4"></td>
                        <td class="py-2 px-3"><p class="font-semibold">{{ dosen.full_name || dosen.username }}</p><p class="text-xs text-slate-500">NIP: {{ dosen.nim_nip }}</p></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
          
          <div class="p-6 border-t border-slate-200 bg-slate-50 flex gap-3">
            <button @click="showPlotDPAModal = false" class="flex-1 py-3 bg-slate-200 hover:bg-slate-300 text-slate-800 rounded-xl font-bold transition-all">Batal</button>
            <button @click="savePlotDPA" :disabled="!formPlotDPA.dpa_id || !formPlotDPA.mahasiswa_id" :class="['flex-1 py-3 text-white rounded-xl font-bold transition-all', (!formPlotDPA.dpa_id || !formPlotDPA.mahasiswa_id) ? 'bg-slate-400 cursor-not-allowed' : 'bg-indigo-600 hover:bg-indigo-700']">Simpan Plotting</button>
          </div>
        </div>
      </div>
    </transition>

    <!-- MODAL EDIT MAHASISWA (PLOTTING) -->
    <transition name="modal">
      <div v-if="showEditMahasiswaModal" class="fixed inset-0 bg-slate-900/80 backdrop-blur-sm z-[60] flex items-center justify-center p-4">
        <div class="bg-white rounded-3xl shadow-2xl w-full max-w-4xl max-h-[90vh] overflow-hidden flex flex-col">
          <div class="p-6 border-b border-slate-100 bg-gradient-to-r from-amber-500 to-orange-600">
            <h3 class="text-2xl font-black text-white uppercase tracking-tight">Edit Plotting DPA</h3>
          </div>
          
          <div class="flex-1 overflow-y-auto p-6 space-y-5 custom-scroll">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 bg-indigo-50 p-4 rounded-xl border border-indigo-100">
              <div><p class="text-xs font-black text-indigo-600 uppercase">Nama Mahasiswa</p><p class="text-lg font-bold text-slate-800">{{ formEditMahasiswa.full_name }}</p></div>
              <div><p class="text-xs font-black text-indigo-600 uppercase">NIM</p><p class="text-lg font-bold text-slate-800 font-mono">{{ formEditMahasiswa.nim_nip || '-' }}</p></div>
            </div>

            <div v-if="formEditMahasiswa.currentDpaId && !formEditMahasiswa.hapusDPA" class="bg-green-50 p-4 rounded-xl border border-green-200">
              <p class="text-xs font-black text-green-700 uppercase">DPA Saat Ini</p>
              <p class="text-base font-bold text-green-800">{{ formEditMahasiswa.currentDpaName }}</p>
            </div>

            <div class="border border-slate-200 rounded-xl overflow-hidden">
              <div class="p-4 bg-slate-50 border-b border-slate-200">
                <label class="block text-sm font-bold text-slate-700 mb-2">Cari Dosen Pembimbing Baru</label>
                <div class="relative">
                  <svg xmlns="http://www.w3.org/2000/svg" class="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
                  <input v-model="searchEditDPA" type="text" placeholder="Cari Nama atau NIP..." class="w-full pl-10 pr-4 py-2.5 bg-white border border-slate-200 rounded-lg focus:border-indigo-500 outline-none transition-all">
                </div>
              </div>
              <div class="max-h-[300px] overflow-y-auto">
                <table class="w-full text-sm">
                  <thead class="bg-slate-100 sticky top-0"><tr><th class="py-2 px-3 w-12">Pilih</th><th class="py-2 px-3">Nama Dosen</th><th class="py-2 px-3">NIP</th></tr></thead>
                  <tbody>
                    <tr v-for="dosen in filteredEditDPA" :key="dosen.id" @click="pilihDPA(dosen.id)" :class="['cursor-pointer hover:bg-indigo-50', formEditMahasiswa.dpa_pembimbing === dosen.id && !formEditMahasiswa.hapusDPA ? 'bg-indigo-100' : '']">
                      <td class="py-2 px-3 text-center"><input type="radio" :value="dosen.id" v-model="formEditMahasiswa.dpa_pembimbing" class="w-4 h-4"></td>
                      <td class="py-2 px-3 font-semibold">{{ dosen.full_name || dosen.username }}</td>
                      <td class="py-2 px-3 text-slate-600">{{ dosen.nim_nip || '-' }}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <div class="border border-slate-200 rounded-lg p-4 bg-amber-50">
              <label class="flex items-center gap-3 cursor-pointer">
                <input type="checkbox" v-model="formEditMahasiswa.hapusDPA" @change="handleHapusDPAClick" class="w-5 h-5 text-rose-600 rounded">
                <span class="text-sm font-semibold text-rose-700">Hapus Plotting DPA (kosongkan DPA)</span>
              </label>
            </div>

            <div v-if="!formEditMahasiswa.hapusDPA && formEditMahasiswa.dpa_pembimbing" class="bg-emerald-50 p-4 rounded-xl border border-emerald-200">
              <p class="text-xs font-black text-emerald-700 uppercase">DPA yang akan disimpan</p>
              <p class="text-base font-bold text-emerald-800">{{ getSelectedDpaName }}</p>
            </div>
            <div v-else-if="formEditMahasiswa.hapusDPA" class="bg-rose-50 p-4 rounded-xl border border-rose-200">
              <p class="text-xs font-black text-rose-700 uppercase">Status</p>
              <p class="text-base font-bold text-rose-800">DPA akan dihapus dari mahasiswa ini</p>
            </div>
          </div>
          
          <div class="p-6 border-t border-slate-200 bg-slate-50 flex gap-3">
            <button @click="closeEditMahasiswaModal" class="flex-1 py-3 bg-slate-200 hover:bg-slate-300 text-slate-800 rounded-xl font-bold transition-all">Batal</button>
            <button @click="saveEditMahasiswa" class="flex-1 py-3 bg-indigo-600 hover:bg-indigo-700 text-white rounded-xl font-bold transition-all">Simpan Plotting</button>
          </div>
        </div>
      </div>
    </transition>

  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import api from '../api/api'; 

const router = useRouter();
const activeMenu = ref('dashboard'); 

const listPengajuan = ref([]);
const listKategori = ref([]);
const listMahasiswa = ref([]);
const listDPA = ref([]);
const dpaActivities = ref([]);

const loadingKategori = ref(false);
const newKategori = ref({ 
  bidang: '', 
  nama_kegiatan: '', 
  partisipasi: '',
  level: '',
  sifat: 'Pilihan',
  bobot_poin: 0 
});

// Pagination untuk Antrean Validasi (Dashboard)
const pendingPage = ref(1);
const pendingItemsPerPage = ref(10);

// Pagination untuk Monitoring DPA
const dpaActivityPage = ref(1);
const dpaActivityItemsPerPage = ref(10);
const searchDpaActivity = ref('');
const filterActivityStatus = ref('all');

// Pagination untuk Mahasiswa
const mahasiswaPage = ref(1);
const mahasiswaItemsPerPage = ref(10);
const searchMahasiswa = ref('');

const showEditKategoriModal = ref(false);
const showEditStatusModal = ref(false);
const showRejectModal = ref(false);
const selectedKategori = ref({});
const selectedPengajuan = ref({});
const rejectReason = ref('');
const pendingRejectId = ref(null);

const showDetailModal = ref(false);
const selectedDetail = ref({});

// PLOTTING DPA VARIABLES
const showPlotDPAModal = ref(false);
const formPlotDPA = ref({ mahasiswa_id: null, dpa_id: null });
const searchPlotMahasiswa = ref('');
const searchPlotDPA = ref('');

const showEditMahasiswaModal = ref(false);
const formEditMahasiswa = ref({
  id: null,
  full_name: '',
  nim_nip: '',
  dpa_pembimbing: null,
  currentDpaId: null,
  currentDpaName: '',
  hapusDPA: false
});
const searchEditDPA = ref('');

// COMPUTED
const listPendingPengajuan = computed(() => {
  return listPengajuan.value.filter(item => 
    String(item.status).toLowerCase() === 'pending'
  );
});

const pendingTotalPages = computed(() => Math.ceil(listPendingPengajuan.value.length / pendingItemsPerPage.value) || 1);

const paginatedPendingPengajuan = computed(() => {
  const start = (pendingPage.value - 1) * pendingItemsPerPage.value;
  return listPendingPengajuan.value.slice(start, start + pendingItemsPerPage.value);
});

const totalDpaActions = computed(() => dpaActivities.value.length);
const avgActionsPerDpa = computed(() => {
  if (listDPA.value.length === 0) return 0;
  return Math.round(totalDpaActions.value / listDPA.value.length);
});

const filteredDpaActivities = computed(() => {
  let filtered = dpaActivities.value;
  
  if (searchDpaActivity.value && searchDpaActivity.value.trim() !== '') {
    const q = searchDpaActivity.value.toLowerCase().trim();
    filtered = filtered.filter(activity => {
      const dpaName = getDpaNameFromActivity(activity).toLowerCase();
      const mahasiswaName = (activity.mahasiswa_nama || '').toLowerCase();
      const judulKegiatan = (activity.judul_kegiatan || '').toLowerCase();
      const nim = (activity.nim || activity.mahasiswa_nim || '').toLowerCase();
      
      return dpaName.includes(q) || 
             mahasiswaName.includes(q) || 
             judulKegiatan.includes(q) ||
             nim.includes(q);
    });
  }
  
  if (filterActivityStatus.value && filterActivityStatus.value !== 'all') {
    filtered = filtered.filter(activity => {
      const status = String(activity.status).toLowerCase();
      const filterStatus = filterActivityStatus.value.toLowerCase();
      return status === filterStatus;
    });
  }
  
  return filtered;
});

const dpaActivityTotalPages = computed(() => Math.ceil(filteredDpaActivities.value.length / dpaActivityItemsPerPage.value) || 1);

const paginatedDpaActivities = computed(() => {
  const start = (dpaActivityPage.value - 1) * dpaActivityItemsPerPage.value;
  return filteredDpaActivities.value.slice(start, start + dpaActivityItemsPerPage.value);
});

const filteredMahasiswa = computed(() => {
  let filtered = listMahasiswa.value;
  
  if (searchMahasiswa.value) {
    const q = searchMahasiswa.value.toLowerCase();
    filtered = filtered.filter(mhs => 
      (mhs.full_name || mhs.username || '').toLowerCase().includes(q) ||
      (mhs.nim_nip || '').toLowerCase().includes(q)
    );
  }
  
  return filtered;
});

const mahasiswaTotalPages = computed(() => Math.ceil(filteredMahasiswa.value.length / mahasiswaItemsPerPage.value) || 1);

const paginatedMahasiswa = computed(() => {
  const start = (mahasiswaPage.value - 1) * mahasiswaItemsPerPage.value;
  return filteredMahasiswa.value.slice(start, start + mahasiswaItemsPerPage.value);
});

const filteredPlotMahasiswa = computed(() => {
  if (!searchPlotMahasiswa.value) return listMahasiswa.value;
  const q = searchPlotMahasiswa.value.toLowerCase();
  return listMahasiswa.value.filter(mhs => 
    (mhs.full_name || mhs.username || '').toLowerCase().includes(q) ||
    (mhs.nim_nip || '').toLowerCase().includes(q)
  );
});

const filteredPlotDPA = computed(() => {
  if (!searchPlotDPA.value) return listDPA.value;
  const q = searchPlotDPA.value.toLowerCase();
  return listDPA.value.filter(dpa => 
    (dpa.full_name || dpa.username || '').toLowerCase().includes(q) ||
    (dpa.nim_nip || '').toLowerCase().includes(q)
  );
});

const filteredEditDPA = computed(() => {
  if (!searchEditDPA.value) return listDPA.value;
  const q = searchEditDPA.value.toLowerCase();
  return listDPA.value.filter(dpa => 
    (dpa.full_name || dpa.username || '').toLowerCase().includes(q) ||
    (dpa.nim_nip || '').toLowerCase().includes(q)
  );
});

const getSelectedDpaName = computed(() => {
  if (!formEditMahasiswa.value.dpa_pembimbing) return 'Belum memilih DPA';
  const selectedDpa = listDPA.value.find(d => d.id === formEditMahasiswa.value.dpa_pembimbing);
  if (selectedDpa) {
    return `${selectedDpa.full_name || selectedDpa.username} (NIP: ${selectedDpa.nim_nip || '-'})`;
  }
  return 'Belum memilih DPA';
});

const handleApiError = (err, customMessage) => {
  const msg = err.response && err.response.data ? JSON.stringify(err.response.data) : err.message;
  console.error(`${customMessage} Alasan: ${msg}`);
  alert(`${customMessage}\nDetail: ${msg}`);
};

onMounted(() => {
  fetchData();
  fetchKategori();
  fetchMahasiswa();
  fetchDPA();
  fetchDpaActivities();
});

const changeMenu = (menuName) => {
  activeMenu.value = menuName;
  if (menuName === 'dashboard') fetchData();
  if (menuName === 'kategori') fetchKategori();
  if (menuName === 'monitoring') fetchDpaActivities();
  if (menuName === 'mahasiswa') {
    fetchMahasiswa();
    fetchDPA();
    mahasiswaPage.value = 1;
    searchMahasiswa.value = '';
  }
};

const getDpaName = (mhs) => {
  if (mhs.dpa_pembimbing_detail && mhs.dpa_pembimbing_detail.full_name) {
    return mhs.dpa_pembimbing_detail.full_name;
  }
  if (mhs.nama_dpa) {
    return mhs.nama_dpa;
  }
  if (mhs.dpa_pembimbing) {
    const dosen = listDPA.value.find(d => d.id == mhs.dpa_pembimbing);
    if (dosen) {
      return dosen.full_name || dosen.username;
    }
  }
  return '-';
};

const getDpaNipFromMahasiswa = (mhs) => {
  if (mhs.dpa_pembimbing_detail && mhs.dpa_pembimbing_detail.nim_nip) {
    return mhs.dpa_pembimbing_detail.nim_nip;
  }
  if (mhs.dpa_pembimbing) {
    const dosen = listDPA.value.find(d => d.id == mhs.dpa_pembimbing);
    if (dosen) {
      return dosen.nim_nip || '-';
    }
  }
  return '-';
};

const getDpaNameFromActivity = (activity) => {
  if (activity.dpa_name) return activity.dpa_name;
  if (activity.dpa_pembimbing_detail && activity.dpa_pembimbing_detail.full_name) return activity.dpa_pembimbing_detail.full_name;
  if (activity.dpa_pembimbing && typeof activity.dpa_pembimbing === 'object') return activity.dpa_pembimbing.full_name;
  if (activity.dpa_username) return activity.dpa_username;
  return 'DPA';
};

const getDpaNip = (activity) => {
  if (activity.dpa_nip) return activity.dpa_nip;
  if (activity.dpa_pembimbing_detail && activity.dpa_pembimbing_detail.nim_nip) return activity.dpa_pembimbing_detail.nim_nip;
  if (activity.dpa_pembimbing && typeof activity.dpa_pembimbing === 'object') return activity.dpa_pembimbing.nim_nip;
  return '-';
};

const getDpaInitials = (activity) => {
  const name = getDpaNameFromActivity(activity);
  return name.charAt(0).toUpperCase();
};

const getStatusBadgeClass = (status) => {
  const s = String(status).toLowerCase();
  if (s === 'approved_final' || s === 'valid') return 'bg-emerald-50 text-emerald-700 border-emerald-200';
  if (s === 'approved_dpa') return 'bg-indigo-50 text-indigo-700 border-indigo-200';
  if (s === 'rejected' || s === 'tolak') return 'bg-rose-50 text-rose-700 border-rose-200';
  if (s === 'pending') return 'bg-amber-50 text-amber-700 border-amber-200';
  return 'bg-slate-100 text-slate-600 border-slate-200';
};

const formatStatusLabel = (status) => {
  const s = String(status).toLowerCase();
  if (s === 'approved_final' || s === 'valid') return '✅ Disetujui';
  if (s === 'approved_dpa') return '🔵 DPA ACC';
  if (s === 'rejected' || s === 'tolak') return '❌ Ditolak';
  if (s === 'pending') return '🕒 Menunggu';
  return status;
};

const formatDate = (dateString) => {
  if (!dateString) return '-';
  const date = new Date(dateString);
  return date.toLocaleDateString('id-ID', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  });
};

const getFileUrl = (path) => {
  if (!path) return '#';
  if (path.startsWith('http')) return path;
  return `http://localhost:8000${path.startsWith('/') ? '' : '/'}${path}`;
};

const hitungTotalPoin = (mhs) => {
  if (!listPengajuan.value || listPengajuan.value.length === 0) return 0;
  
  let total = 0;
  
  listPengajuan.value.forEach(p => {
    const isStatusValid = String(p.status).toLowerCase() === 'approved_final' || String(p.status).toLowerCase() === 'valid';
    
    if (isStatusValid) {
      const nimPengajuan = String(p.nim || p.mahasiswa_nim || '').trim();
      const nimMhs = String(mhs.nim_nip || '').trim();
      
      const namaPengajuan = String(p.mahasiswa_nama || '').trim().toLowerCase();
      const namaMhs = String(mhs.full_name || mhs.username || '').trim().toLowerCase();

      if (
        (p.mahasiswa == mhs.id) || 
        (p.mahasiswa_id == mhs.id) || 
        (nimPengajuan && nimMhs && nimPengajuan === nimMhs) ||
        (namaPengajuan && namaMhs && namaPengajuan === namaMhs)
      ) {
        total += Number(p.bobot_poin_kategori || p.poin_valid || p.poin || 0);
      }
    }
  });

  if (total === 0 && (mhs.total_poin > 0 || mhs.poin > 0)) {
    return Number(mhs.total_poin || mhs.poin);
  }

  return total;
};

// FETCH DATA
const fetchData = async () => {
  try {
    const res = await api.get('api/kegiatan/');
    listPengajuan.value = res.data;
  } catch (err) { handleApiError(err, "Gagal memuat data kegiatan."); }
};

const fetchDpaActivities = async () => {
  try {
    const res = await api.get('api/kegiatan/');
    const activities = [...res.data].sort((a, b) => {
      const dateA = new Date(a.updated_at || a.created_at);
      const dateB = new Date(b.updated_at || b.created_at);
      return dateB - dateA;
    });
    dpaActivities.value = activities;
  } catch (err) { 
    console.error("Gagal memuat aktivitas DPA", err);
    dpaActivities.value = [];
  }
};

const openDetailModal = (item) => {
  selectedDetail.value = { ...item };
  showDetailModal.value = true;
};

const openEditStatus = (item) => {
  selectedPengajuan.value = { ...item };
  showEditStatusModal.value = true;
};

const openRejectModal = (item) => {
  pendingRejectId.value = item.id;
  rejectReason.value = '';
  showRejectModal.value = true;
};

const confirmReject = async () => {
  if (!rejectReason.value.trim()) {
    alert('Alasan penolakan harus diisi!');
    return;
  }
  
  try {
    await api.patch(`api/kegiatan/${pendingRejectId.value}/`, { 
      status: 'rejected',
      komentar_dpa: rejectReason.value
    });
    alert('Pengajuan berhasil ditolak!');
    showRejectModal.value = false;
    showEditStatusModal.value = false;
    fetchData();
    fetchDpaActivities();
  } catch (err) { handleApiError(err, "Gagal menolak pengajuan."); }
};

const saveEditStatus = async (statusBaru) => {
  try {
    await api.patch(`api/kegiatan/${selectedPengajuan.value.id}/`, { status: statusBaru });
    alert('Status berhasil diubah!');
    fetchData();
    fetchDpaActivities();
    showEditStatusModal.value = false;
  } catch (err) { handleApiError(err, "Gagal mengubah status."); }
};

const fetchKategori = async () => {
  try {
    const res = await api.get('api/kategori/');
    listKategori.value = res.data;
  } catch (err) { handleApiError(err, "Gagal memuat daftar kategori."); }
};

const openEditKategori = (kat) => {
  selectedKategori.value = { ...kat };
  showEditKategoriModal.value = true;
};

const saveEditKategori = async () => {
  const namaEdit = selectedKategori.value.nama_kegiatan.trim().toLowerCase();
  const isDuplicate = listKategori.value.some(kat => 
    kat.id !== selectedKategori.value.id && 
    kat.nama_kegiatan.trim().toLowerCase() === namaEdit
  );

  if (isDuplicate) {
    alert('Nama Detail Kegiatan sudah ada! Silakan gunakan nama lain.');
    return;
  }

  try {
    await api.patch(`api/kategori/${selectedKategori.value.id}/`, selectedKategori.value);
    fetchKategori();
    showEditKategoriModal.value = false;
    alert('Informasi Kategori berhasil diperbarui!');
  } catch (err) { handleApiError(err, "Gagal menyimpan pembaruan kategori."); }
};

const submitKategori = async () => {
  const namaBaru = newKategori.value.nama_kegiatan.trim().toLowerCase();
  const isDuplicate = listKategori.value.some(kat => 
    kat.nama_kegiatan.trim().toLowerCase() === namaBaru
  );

  if (isDuplicate) {
    alert('Nama Detail Kegiatan sudah ada! Silakan gunakan nama lain.');
    return;
  }

  loadingKategori.value = true;
  try {
    await api.post('api/kategori/', newKategori.value);
    newKategori.value = { bidang: '', nama_kegiatan: '', partisipasi: '', level: '', sifat: 'Pilihan', bobot_poin: 0 };
    fetchKategori();
    alert('Kategori berhasil ditambahkan!');
  } catch (err) { handleApiError(err, "Gagal menambah kategori."); }
  finally { loadingKategori.value = false; }
};

const hapusKategori = async (id) => {
  if (!confirm('Yakin hapus permanen kategori ini?')) return;
  try {
    await api.delete(`api/kategori/${id}/`);
    fetchKategori();
  } catch (err) { handleApiError(err, "Gagal menghapus data kategori."); }
};

const fetchMahasiswa = async () => {
  try {
    const res = await api.get('api/mahasiswa/');
    listMahasiswa.value = res.data;
  } catch (err) { handleApiError(err, "Gagal memuat data mahasiswa."); }
};

const fetchDPA = async () => {
  try {
    const res = await api.get('api/dosen/');
    listDPA.value = res.data;
  } catch (err) { handleApiError(err, "Gagal memuat data dosen (DPA)."); }
};

const openPlotDPABaru = () => {
  formPlotDPA.value = { mahasiswa_id: null, dpa_id: null };
  searchPlotMahasiswa.value = '';
  searchPlotDPA.value = '';
  showPlotDPAModal.value = true;
};

const savePlotDPA = async () => {
  try {
    const payload = { dpa_pembimbing: formPlotDPA.value.dpa_id };
    await api.patch(`api/mahasiswa/${formPlotDPA.value.mahasiswa_id}/`, payload);
    
    alert('Plotting DPA Berhasil Disimpan!');
    showPlotDPAModal.value = false;
    fetchMahasiswa(); 
  } catch (err) { handleApiError(err, "Gagal menyimpan plotting DPA."); }
};

const openEditMahasiswa = (mhs) => {
  let currentDpaId = null;
  let currentDpaName = 'Tidak ada DPA';
  
  if (mhs.dpa_pembimbing_detail && mhs.dpa_pembimbing_detail.id) {
    currentDpaId = mhs.dpa_pembimbing_detail.id;
    currentDpaName = mhs.dpa_pembimbing_detail.full_name || mhs.dpa_pembimbing_detail.username;
    if (mhs.dpa_pembimbing_detail.nim_nip) {
      currentDpaName += ` (NIP: ${mhs.dpa_pembimbing_detail.nim_nip})`;
    }
  } else if (mhs.dpa_pembimbing) {
    const dosen = listDPA.value.find(d => d.id == mhs.dpa_pembimbing);
    if (dosen) {
      currentDpaId = dosen.id;
      currentDpaName = dosen.full_name || dosen.username;
      if (dosen.nim_nip) {
        currentDpaName += ` (NIP: ${dosen.nim_nip})`;
      }
    }
  }
  
  formEditMahasiswa.value = { 
    id: mhs.id,
    full_name: mhs.full_name || mhs.username,
    nim_nip: mhs.nim_nip,
    dpa_pembimbing: currentDpaId,
    currentDpaId: currentDpaId,
    currentDpaName: currentDpaName,
    hapusDPA: false
  };
  searchEditDPA.value = '';
  showEditMahasiswaModal.value = true;
};

const pilihDPA = (dpaId) => {
  formEditMahasiswa.value.dpa_pembimbing = dpaId;
  formEditMahasiswa.value.hapusDPA = false;
};

const handleHapusDPAClick = () => {
  if (formEditMahasiswa.value.hapusDPA) {
    formEditMahasiswa.value.dpa_pembimbing = null;
  }
};

const closeEditMahasiswaModal = () => {
  showEditMahasiswaModal.value = false;
  searchEditDPA.value = '';
  formEditMahasiswa.value = {
    id: null,
    full_name: '',
    nim_nip: '',
    dpa_pembimbing: null,
    currentDpaId: null,
    currentDpaName: '',
    hapusDPA: false
  };
};

const saveEditMahasiswa = async () => {
  try {
    let dpaId = formEditMahasiswa.value.dpa_pembimbing;
    
    if (formEditMahasiswa.value.hapusDPA) {
      dpaId = null;
    }
    
    await api.patch(`api/mahasiswa/${formEditMahasiswa.value.id}/`, {
      dpa_pembimbing: dpaId
    });
    
    alert('Plotting DPA berhasil diperbarui!');
    closeEditMahasiswaModal();
    fetchMahasiswa();
  } catch (err) { 
    handleApiError(err, "Gagal menyimpan pembaruan plotting DPA."); 
  }
};

const hapusPlotting = async (mhs) => {
  if (!confirm(`Yakin hapus plotting DPA untuk ${mhs.full_name || mhs.username}?`)) return;
  try {
    await api.patch(`api/mahasiswa/${mhs.id}/`, { dpa_pembimbing: null });
    alert('Plotting DPA berhasil dihapus!');
    fetchMahasiswa();
  } catch (err) { handleApiError(err, "Gagal menghapus plotting DPA."); }
};

const handleLogout = () => {
  if(confirm("Apakah Anda yakin ingin keluar dari aplikasi?")) {
    localStorage.clear();
    router.push('/login'); 
  }
};
</script>

<style scoped>
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.2s ease, transform 0.2s ease;
}
.modal-enter-from,
.modal-leave-to {
  opacity: 0;
  transform: scale(0.98);
}

.custom-scroll::-webkit-scrollbar {
  width: 6px;
}
.custom-scroll::-webkit-scrollbar-track {
  background: transparent;
}
.custom-scroll::-webkit-scrollbar-thumb {
  background: #cbd5e1;
  border-radius: 10px;
}
.custom-scroll::-webkit-scrollbar-thumb:hover {
  background: #94a3b8;
}
</style>