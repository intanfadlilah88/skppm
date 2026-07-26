<template>
  <div
    class="min-h-screen bg-gradient-to-br from-slate-50 via-indigo-50/20 to-slate-50 flex font-sans selection:bg-indigo-100 selection:text-indigo-900 overflow-hidden"
  >
    <!-- SIDEBAR - FIXED POSITION -->
    <aside
      class="w-72 bg-[#1e293b] text-white hidden md:flex flex-col fixed top-0 left-0 bottom-0 h-screen"
    >
      <!-- HEADER SIDEBAR -->
      <div
        class="p-4 lg:p-5 flex items-center gap-3 border-b border-white/10 flex-shrink-0 bg-gradient-to-b from-slate-800 to-slate-900"
      >
        <div
          class="h-10 w-10 lg:h-11 lg:w-11 bg-white rounded-xl flex items-center justify-center shadow-lg overflow-hidden flex-shrink-0"
        >
          <img
            src="/stie-sbilogo.jpg"
            alt="STIE SBI Logo"
            class="h-full w-full object-cover"
            @error="(e) => (e.target.src = '')"
          />
        </div>
        <div class="flex flex-col min-w-0">
          <span class="font-bold text-sm lg:text-base tracking-tight truncate"
            >SKPM Super Admin</span
          >
          <span class="text-[10px] lg:text-xs text-indigo-300 truncate"
            >STIE SBI Yogyakarta</span
          >
        </div>
      </div>

      <!-- NAVIGASI -->
      <nav
        class="flex-1 p-3 lg:p-4 space-y-1 overflow-y-auto custom-scroll bg-gradient-to-b from-slate-800 to-slate-900"
      >
        <button
          @click="currentPage = 'dashboard'"
          :class="[
            'w-full flex items-center gap-3 px-4 py-2.5 lg:py-3 rounded-xl transition-all duration-200 text-sm',
            currentPage === 'dashboard'
              ? 'bg-indigo-600 text-white shadow-lg shadow-indigo-600/30'
              : 'hover:bg-slate-700/50 text-slate-300 hover:text-white',
          ]"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-4 w-4 lg:h-5 lg:w-5 flex-shrink-0"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
            />
          </svg>
          <span class="font-semibold text-xs lg:text-sm truncate"
            >Dashboard Admin</span
          >
        </button>

        <button
          @click="currentPage = 'manage-users'"
          :class="[
            'w-full flex items-center gap-3 px-4 py-2.5 lg:py-3 rounded-xl transition-all duration-200 text-sm',
            currentPage === 'manage-users'
              ? 'bg-indigo-600 text-white shadow-lg shadow-indigo-600/30'
              : 'hover:bg-slate-700/50 text-slate-300 hover:text-white',
          ]"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-4 w-4 lg:h-5 lg:w-5 flex-shrink-0"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"
            />
          </svg>
          <span class="font-semibold text-xs lg:text-sm truncate"
            >Manajemen User</span
          >
        </button>

        <button
          @click="currentPage = 'kegiatan'"
          :class="[
            'w-full flex items-center gap-3 px-4 py-2.5 lg:py-3 rounded-xl transition-all duration-200 text-sm',
            currentPage === 'kegiatan'
              ? 'bg-indigo-600 text-white shadow-lg shadow-indigo-600/30'
              : 'hover:bg-slate-700/50 text-slate-300 hover:text-white',
          ]"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-4 w-4 lg:h-5 lg:w-5 flex-shrink-0"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
            />
          </svg>
          <span class="font-semibold text-xs lg:text-sm truncate"
            >Data Kegiatan</span
          >
        </button>

        <button
          @click="currentPage = 'kategori'"
          :class="[
            'w-full flex items-center gap-3 px-4 py-2.5 lg:py-3 rounded-xl transition-all duration-200 text-sm',
            currentPage === 'kategori'
              ? 'bg-indigo-600 text-white shadow-lg shadow-indigo-600/30'
              : 'hover:bg-slate-700/50 text-slate-300 hover:text-white',
          ]"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-4 w-4 lg:h-5 lg:w-5 flex-shrink-0"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M4 6h16M4 12h16M4 18h16"
            />
          </svg>
          <span class="font-semibold text-xs lg:text-sm truncate"
            >Kelola Kategori</span
          >
        </button>

        <button
          @click="currentPage = 'plotting'"
          :class="[
            'w-full flex items-center gap-3 px-4 py-2.5 lg:py-3 rounded-xl transition-all duration-200 text-sm',
            currentPage === 'plotting'
              ? 'bg-indigo-600 text-white shadow-lg shadow-indigo-600/30'
              : 'hover:bg-slate-700/50 text-slate-300 hover:text-white',
          ]"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-4 w-4 lg:h-5 lg:w-5 flex-shrink-0"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1"
            />
          </svg>
          <span class="font-semibold text-xs lg:text-sm truncate"
            >Plotting DPA</span
          >
        </button>
      </nav>

      <!-- FOOTER SIDEBAR -->
      <div
        class="p-3 lg:p-4 border-t border-white/10 bg-gradient-to-b from-slate-800 to-slate-900 flex-shrink-0"
      >
        <div class="text-[10px] text-slate-500 text-center">
          <p>Sistem Kredit Poin Prestasi Mahasiswa</p>
          <p class="mt-0.5">STIE SBI Yogyakarta</p>
        </div>
      </div>
    </aside>

    <!-- MAIN CONTENT -->
    <main
      class="flex-1 ml-72 p-4 sm:p-5 md:p-6 lg:p-8 xl:p-10 overflow-y-auto h-screen"
    >
      <!-- HEADER -->
      <div class="mb-6 lg:mb-8">
        <div
          class="bg-gradient-to-r from-indigo-600 via-indigo-700 to-indigo-800 rounded-2xl lg:rounded-3xl p-5 md:p-6 lg:p-8 text-white shadow-2xl shadow-indigo-200/30 relative overflow-hidden"
        >
          <div
            class="absolute top-0 right-0 w-48 md:w-64 h-48 md:h-64 bg-white/5 rounded-full -mr-24 -mt-24"
          ></div>
          <div
            class="absolute bottom-0 left-0 w-36 md:w-48 h-36 md:h-48 bg-white/5 rounded-full -ml-18 -mb-18"
          ></div>

          <div
            class="relative z-10 flex flex-col md:flex-row justify-between items-start md:items-center gap-4 md:gap-6"
          >
            <div class="min-w-0">
              <div class="flex items-center gap-2 md:gap-3 mb-1 md:mb-2">
                <div
                  class="h-9 w-9 md:h-10 md:w-10 lg:h-11 lg:w-11 bg-white/20 rounded-xl flex items-center justify-center backdrop-blur-sm flex-shrink-0"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-4 w-4 md:h-5 md:w-5 lg:h-6 lg:w-6"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"
                    />
                  </svg>
                </div>
                <div class="min-w-0">
                  <h1
                    class="text-base sm:text-lg md:text-xl lg:text-2xl xl:text-3xl font-black tracking-tight truncate"
                  >
                    Panel Kendali Utama
                  </h1>
                  <p
                    class="text-indigo-200 text-[10px] sm:text-xs md:text-sm truncate"
                  >
                    Super Admin • STIE SBI Yogyakarta
                  </p>
                </div>
              </div>
            </div>

            <button
              @click="handleLogout"
              class="flex items-center gap-2 bg-white/20 hover:bg-white/30 backdrop-blur-sm px-4 md:px-6 py-2 md:py-2.5 rounded-xl transition-all duration-200 font-bold text-sm shadow-lg flex-shrink-0"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-4 w-4 md:h-5 md:w-5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"
                />
              </svg>
              <span>Logout</span>
            </button>
          </div>
        </div>
      </div>

      <!-- ==================== DASHBOARD VIEW ==================== -->
      <div v-if="currentPage === 'dashboard'">
        <!-- STATS CARDS -->
        <div
          class="grid grid-cols-2 lg:grid-cols-4 gap-3 md:gap-4 lg:gap-5 mb-6 lg:mb-8"
        >
          <div
            class="group bg-white p-4 md:p-5 rounded-xl md:rounded-2xl shadow-sm hover:shadow-xl transition-all duration-300 border border-slate-100 hover:border-indigo-200 relative overflow-hidden"
          >
            <div class="flex items-center justify-between">
              <div>
                <p
                  class="text-slate-500 text-[8px] md:text-[10px] font-black uppercase tracking-wider mb-0.5"
                >
                  Total Mahasiswa
                </p>
                <h4 class="text-xl md:text-2xl font-black text-slate-800">
                  {{ stats.total_mahasiswa }}
                  <span class="text-xs md:text-sm font-medium text-slate-400"
                    >Orang</span
                  >
                </h4>
              </div>
              <div
                class="h-10 w-10 md:h-11 md:w-11 lg:h-12 lg:w-12 bg-gradient-to-br from-blue-500 to-blue-600 rounded-xl flex items-center justify-center shadow-lg shadow-blue-200 group-hover:scale-110 transition-transform flex-shrink-0"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5 md:h-6 md:w-6 text-white"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"
                  />
                </svg>
              </div>
            </div>
          </div>

          <div
            class="group bg-white p-4 md:p-5 rounded-xl md:rounded-2xl shadow-sm hover:shadow-xl transition-all duration-300 border border-slate-100 hover:border-amber-200 relative overflow-hidden"
          >
            <div class="flex items-center justify-between">
              <div>
                <p
                  class="text-slate-500 text-[8px] md:text-[10px] font-black uppercase tracking-wider mb-0.5"
                >
                  Antrean Validasi
                </p>
                <h4 class="text-xl md:text-2xl font-black text-slate-800">
                  {{ stats.total_pending }}
                  <span class="text-xs md:text-sm font-medium text-slate-400"
                    >Berkas</span
                  >
                </h4>
              </div>
              <div
                class="h-10 w-10 md:h-11 md:w-11 lg:h-12 lg:w-12 bg-gradient-to-br from-amber-500 to-amber-600 rounded-xl flex items-center justify-center shadow-lg shadow-amber-200 group-hover:scale-110 transition-transform flex-shrink-0"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5 md:h-6 md:w-6 text-white"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
                  />
                </svg>
              </div>
            </div>
          </div>

          <div
            class="group bg-white p-4 md:p-5 rounded-xl md:rounded-2xl shadow-sm hover:shadow-xl transition-all duration-300 border border-slate-100 hover:border-emerald-200 relative overflow-hidden"
          >
            <div class="flex items-center justify-between">
              <div>
                <p
                  class="text-slate-500 text-[8px] md:text-[10px] font-black uppercase tracking-wider mb-0.5"
                >
                  Telah Disahkan
                </p>
                <h4 class="text-xl md:text-2xl font-black text-slate-800">
                  {{ stats.total_valid }}
                  <span class="text-xs md:text-sm font-medium text-slate-400"
                    >Berkas</span
                  >
                </h4>
              </div>
              <div
                class="h-10 w-10 md:h-11 md:w-11 lg:h-12 lg:w-12 bg-gradient-to-br from-emerald-500 to-emerald-600 rounded-xl flex items-center justify-center shadow-lg shadow-emerald-200 group-hover:scale-110 transition-transform flex-shrink-0"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5 md:h-6 md:w-6 text-white"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
                  />
                </svg>
              </div>
            </div>
          </div>

          <div
            class="group bg-white p-4 md:p-5 rounded-xl md:rounded-2xl shadow-sm hover:shadow-xl transition-all duration-300 border border-slate-100 hover:border-rose-200 relative overflow-hidden"
          >
            <div class="flex items-center justify-between">
              <div>
                <p
                  class="text-slate-500 text-[8px] md:text-[10px] font-black uppercase tracking-wider mb-0.5"
                >
                  Ditolak
                </p>
                <h4 class="text-xl md:text-2xl font-black text-slate-800">
                  {{ stats.total_tolak }}
                  <span class="text-xs md:text-sm font-medium text-slate-400"
                    >Berkas</span
                  >
                </h4>
              </div>
              <div
                class="h-10 w-10 md:h-11 md:w-11 lg:h-12 lg:w-12 bg-gradient-to-br from-rose-500 to-rose-600 rounded-xl flex items-center justify-center shadow-lg shadow-rose-200 group-hover:scale-110 transition-transform flex-shrink-0"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5 md:h-6 md:w-6 text-white"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
                  />
                </svg>
              </div>
            </div>
          </div>
        </div>

        <!-- Antrean Validasi -->
        <div
          class="bg-white rounded-xl md:rounded-2xl shadow-lg border border-slate-200 overflow-hidden"
        >
          <div
            class="p-4 md:p-5 lg:p-6 border-b border-slate-200 bg-gradient-to-r from-slate-50 to-white"
          >
            <h2
              class="text-sm md:text-base lg:text-lg font-bold text-slate-800 flex items-center gap-2 md:gap-3"
            >
              <span class="text-xl">📋</span>
              <span>Antrean Validasi Final</span>
              <span class="ml-auto text-xs text-slate-400 font-medium"
                >{{ filteredLogs.length }} Antrean</span
              >
            </h2>
            <p class="text-xs text-slate-500 mt-1">
              Daftar pengajuan yang menunggu persetujuan final.
            </p>
          </div>

          <div class="overflow-x-auto">
            <table class="w-full min-w-[800px]">
              <thead class="bg-slate-100/80 border-b-2 border-slate-200">
                <tr>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-left text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    No
                  </th>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-left text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    Mahasiswa
                  </th>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-left text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    Kegiatan
                  </th>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-center text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    Poin
                  </th>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-center text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    Status
                  </th>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-center text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    Aksi
                  </th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100">
                <tr
                  v-for="(log, index) in paginatedLogs"
                  :key="log.id"
                  class="hover:bg-indigo-50/40 transition-colors"
                >
                  <td
                    class="px-3 md:px-4 py-2 md:py-3 text-center text-xs font-bold text-slate-500"
                  >
                    {{ (logsPage - 1) * logsItemsPerPage + index + 1 }}
                  </td>
                  <td class="px-3 md:px-4 py-2 md:py-3">
                    <p class="font-bold text-slate-800 text-xs md:text-sm">
                      {{ log.mahasiswa_nama || "-" }}
                    </p>
                    <p class="text-[10px] text-slate-500">
                      NIM: {{ log.nim || "-" }}
                    </p>
                    <span
                      class="inline-block mt-0.5 text-[8px] md:text-[10px] bg-purple-100 text-purple-700 px-2 py-0.5 rounded-md"
                      >DPA: {{ log.dpa_nama || "-" }}</span
                    >
                  </td>
                  <td class="px-3 md:px-4 py-2 md:py-3">
                    <p class="font-semibold text-slate-800 text-xs md:text-sm">
                      {{ log.judul_kegiatan || "-" }}
                    </p>
                    <p class="text-[10px] text-slate-500 mt-0.5">
                      {{ formatDate(log.created_at) }}
                    </p>
                  </td>
                  <td class="px-3 md:px-4 py-2 md:py-3 text-center">
                    <span
                      class="inline-block px-2 md:px-3 py-1 rounded-lg bg-blue-100 text-blue-800 font-bold text-xs md:text-sm"
                      >{{ log.poin || 0 }}</span
                    >
                  </td>
                  <td class="px-3 md:px-4 py-2 md:py-3 text-center">
                    <span
                      :class="getStatusBadgeClass(log.status)"
                      class="px-2 md:px-3 py-1 rounded-full text-[8px] md:text-[10px] font-bold"
                    >
                      {{ formatStatusLabel(log.status) }}
                    </span>
                  </td>
                  <td class="px-3 md:px-4 py-2 md:py-3 text-center">
                    <div class="flex gap-1.5 md:gap-2 justify-center">
                      <button
                        @click="updateStatus(log.id, 'approved_final')"
                        class="w-7 h-7 md:w-8 md:h-8 bg-green-500 hover:bg-green-600 text-white rounded-lg transition-all flex items-center justify-center text-sm shadow"
                        title="Setujui"
                      >
                        ✓
                      </button>
                      <button
                        @click="openRejectModal(log.id)"
                        class="w-7 h-7 md:w-8 md:h-8 bg-red-500 hover:bg-red-600 text-white rounded-lg transition-all flex items-center justify-center text-sm shadow"
                        title="Tolak"
                      >
                        ✕
                      </button>
                    </div>
                  </td>
                </tr>
                <tr v-if="filteredLogs.length === 0">
                  <td
                    colspan="6"
                    class="px-3 md:px-6 py-8 md:py-12 text-center"
                  >
                    <div class="text-4xl md:text-5xl mb-2 opacity-40">📋</div>
                    <p class="text-slate-500 font-semibold text-xs md:text-sm">
                      Tidak ada antrean validasi
                    </p>
                    <p class="text-slate-400 text-[10px] md:text-xs mt-1">
                      Semua pengajuan sudah diproses
                    </p>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <div
            v-if="filteredLogs.length > 0"
            class="p-3 md:p-4 border-t border-slate-200 bg-slate-50/80 flex justify-between items-center"
          >
            <span class="text-[10px] md:text-xs font-bold text-slate-500"
              >Halaman {{ logsPage }} dari {{ logsTotalPages }}</span
            >
            <div class="flex gap-1.5 md:gap-2">
              <button
                @click="prevPage"
                :disabled="logsPage === 1"
                class="px-3 md:px-4 py-1.5 bg-white border border-slate-200 rounded-lg text-[10px] md:text-xs font-bold text-slate-600 hover:bg-indigo-50 disabled:opacity-50 transition-all"
              >
                ← Prev
              </button>
              <button
                @click="nextPage"
                :disabled="logsPage === logsTotalPages"
                class="px-3 md:px-4 py-1.5 bg-white border border-slate-200 rounded-lg text-[10px] md:text-xs font-bold text-slate-600 hover:bg-indigo-50 disabled:opacity-50 transition-all"
              >
                Next →
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- ==================== MANAGE USERS VIEW ==================== -->
      <div v-if="currentPage === 'manage-users'">
        <div
          class="bg-white rounded-xl md:rounded-2xl shadow-lg border border-slate-200 overflow-hidden"
        >
          <div
            class="p-4 md:p-5 lg:p-6 border-b border-slate-200 bg-gradient-to-r from-slate-50 to-white"
          >
            <div
              class="flex flex-col md:flex-row justify-between items-start md:items-center gap-3 md:gap-4"
            >
              <div>
                <h2
                  class="text-sm md:text-base lg:text-lg font-bold text-slate-800 flex items-center gap-2 md:gap-3"
                >
                  <span class="text-xl">👥</span>
                  <span>Manajemen User</span>
                </h2>
                <p class="text-xs text-slate-500 mt-1">
                  Kelola data mahasiswa, dosen, akademik, dan kemahasiswaan
                </p>
              </div>
              <div class="flex flex-wrap gap-2">
                <button
                  @click="fetchUsers"
                  class="bg-green-600 hover:bg-green-700 text-white px-4 md:px-5 py-2 rounded-xl font-bold text-xs md:text-sm transition-all shadow-md flex items-center gap-2"
                >
                  <span>🔄</span> Refresh
                </button>
                <button
                  @click="openAddUserModal"
                  class="bg-indigo-600 hover:bg-indigo-700 text-white px-4 md:px-5 py-2 rounded-xl font-bold text-xs md:text-sm transition-all shadow-md flex items-center gap-2"
                >
                  <span>➕</span> Tambah User
                </button>
              </div>
            </div>
          </div>

          <!-- Tabs -->
          <div class="border-b border-slate-200 bg-slate-50/50">
            <div class="flex flex-wrap gap-1 p-2 md:p-3">
              <button
                @click="
                  userTab = 'mahasiswa';
                  resetPagination();
                "
                :class="[
                  'px-4 md:px-5 py-2 md:py-2.5 rounded-xl font-bold transition-all text-xs md:text-sm',
                  userTab === 'mahasiswa'
                    ? 'bg-indigo-600 text-white shadow-md'
                    : 'text-slate-600 hover:bg-slate-200',
                ]"
              >
                🎓 Mahasiswa ({{ allMahasiswa.length }})
              </button>
              <button
                @click="
                  userTab = 'dosen';
                  resetPagination();
                "
                :class="[
                  'px-4 md:px-5 py-2 md:py-2.5 rounded-xl font-bold transition-all text-xs md:text-sm',
                  userTab === 'dosen'
                    ? 'bg-indigo-600 text-white shadow-md'
                    : 'text-slate-600 hover:bg-slate-200',
                ]"
              >
                👨‍🏫 DPA ({{ allDosen.length }})
              </button>
              <button
                @click="
                  userTab = 'akademik';
                  resetPagination();
                "
                :class="[
                  'px-4 md:px-5 py-2 md:py-2.5 rounded-xl font-bold transition-all text-xs md:text-sm',
                  userTab === 'akademik'
                    ? 'bg-indigo-600 text-white shadow-md'
                    : 'text-slate-600 hover:bg-slate-200',
                ]"
              >
                📚 Akademik ({{ allAkademik.length }})
              </button>
              <button
                @click="
                  userTab = 'kemahasiswaan';
                  resetPagination();
                "
                :class="[
                  'px-4 md:px-5 py-2 md:py-2.5 rounded-xl font-bold transition-all text-xs md:text-sm',
                  userTab === 'kemahasiswaan'
                    ? 'bg-indigo-600 text-white shadow-md'
                    : 'text-slate-600 hover:bg-slate-200',
                ]"
              >
                🎯 Kemahasiswaan ({{ allKemahasiswaan.length }})
              </button>
              <button
                @click="
                  userTab = 'admin';
                  resetPagination();
                "
                :class="[
                  'px-4 md:px-5 py-2 md:py-2.5 rounded-xl font-bold transition-all text-xs md:text-sm',
                  userTab === 'admin'
                    ? 'bg-indigo-600 text-white shadow-md'
                    : 'text-slate-600 hover:bg-slate-200',
                ]"
              >
                👑 Admin ({{ allAdmin.length }})
              </button>
            </div>
          </div>

          <!-- Search Bar -->
          <div class="p-4 border-b border-slate-200 bg-white">
            <div class="relative w-full md:w-80">
              <div
                class="absolute inset-y-0 left-3 md:left-4 flex items-center pointer-events-none"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-4 w-4 md:h-5 md:w-5 text-slate-400"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                  />
                </svg>
              </div>
              <input
                v-model="searchUser"
                type="text"
                placeholder="Cari berdasarkan nama, NIM/NIP, atau email..."
                class="w-full pl-9 md:pl-11 pr-3 md:pr-4 py-2 md:py-2.5 bg-white border-2 border-slate-200 focus:border-indigo-500 rounded-xl outline-none text-xs md:text-sm font-medium text-slate-700 transition-all"
              />
            </div>
          </div>

          <!-- Loading Indicator -->
          <div
            v-if="loadingUsers"
            class="flex justify-center items-center py-12"
          >
            <div
              class="w-8 h-8 md:w-10 md:h-10 border-4 border-indigo-500 border-t-transparent rounded-full animate-spin"
            ></div>
            <span class="ml-3 text-slate-600 text-xs md:text-sm"
              >Memuat data user...</span
            >
          </div>

          <!-- MAHASISWA TABLE -->
          <div
            v-if="userTab === 'mahasiswa' && !loadingUsers"
            class="overflow-x-auto"
          >
            <table class="w-full min-w-[900px]">
              <thead class="bg-slate-100/80 border-b-2 border-slate-200">
                <tr>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-left text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    No
                  </th>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-left text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    Nama
                  </th>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-left text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    NIM
                  </th>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-left text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    Prodi
                  </th>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-center text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    Aksi
                  </th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100">
                <tr
                  v-for="(mhs, index) in paginatedMahasiswa"
                  :key="mhs.id"
                  class="hover:bg-indigo-50/40 transition-colors"
                >
                  <td
                    class="px-3 md:px-4 py-2 md:py-3 text-center text-xs font-bold text-slate-500"
                  >
                    {{ (mahasiswaPage - 1) * itemsPerPage + index + 1 }}
                  </td>
                  <td
                    class="px-3 md:px-4 py-2 md:py-3 font-semibold text-xs md:text-sm text-slate-800"
                  >
                    {{ mhs.full_name || mhs.username || "-" }}
                  </td>
                  <td
                    class="px-3 md:px-4 py-2 md:py-3 font-mono text-xs md:text-sm text-slate-700"
                  >
                    {{ mhs.nim_nip || "-" }}
                  </td>
                  <td
                    class="px-3 md:px-4 py-2 md:py-3 text-xs md:text-sm text-slate-700"
                  >
                    {{ mhs.prodi || "-" }}
                  </td>

                  <!-- TAMBAHKAN BAGIAN TD AKSI DI BAWAH INI -->
                  <td class="px-3 md:px-4 py-2 md:py-3 text-center">
                    <button
                      @click="editUser(mhs)"
                      class="px-2 md:px-3 py-1 md:py-1.5 bg-amber-500 hover:bg-amber-600 text-white rounded-lg font-semibold text-[10px] md:text-xs transition-colors mr-1.5"
                      title="Edit"
                    >
                      ✏️
                    </button>
                    <button
                      @click="hapusUser(mhs.id, mhs.full_name || mhs.username)"
                      class="px-2 md:px-3 py-1 md:py-1.5 bg-red-600 hover:bg-red-700 text-white rounded-lg font-semibold text-[10px] md:text-xs transition-colors"
                      title="Hapus"
                    >
                      🗑️
                    </button>
                  </td>
                  <!-- SAMPAI SINI -->
                </tr>
              </tbody>
            </table>
          </div>

          <!-- DOSEN TABLE -->
          <div
            v-if="userTab === 'dosen' && !loadingUsers"
            class="overflow-x-auto"
          >
            <table class="w-full min-w-[900px]">
              <thead class="bg-slate-100/80 border-b-2 border-slate-200">
                <tr>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-left text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    No
                  </th>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-left text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    Nama
                  </th>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-left text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    NIP
                  </th>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-left text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    Email
                  </th>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-center text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    Aksi
                  </th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100">
                <tr
                  v-for="(dosen, index) in paginatedDosen"
                  :key="dosen.id"
                  class="hover:bg-indigo-50/40 transition-colors"
                >
                  <td
                    class="px-3 md:px-4 py-2 md:py-3 text-center text-xs font-bold text-slate-500"
                  >
                    {{ (dosenPage - 1) * itemsPerPage + index + 1 }}
                  </td>
                  <td
                    class="px-3 md:px-4 py-2 md:py-3 font-semibold text-xs md:text-sm text-slate-800"
                  >
                    {{ dosen.full_name || dosen.username || "-" }}
                  </td>
                  <td
                    class="px-3 md:px-4 py-2 md:py-3 font-mono text-xs md:text-sm text-slate-700"
                  >
                    {{ dosen.nim_nip || "-" }}
                  </td>
                  <td
                    class="px-3 md:px-4 py-2 md:py-3 text-xs md:text-sm text-slate-700"
                  >
                    {{ dosen.email || "-" }}
                  </td>
                  <td class="px-3 md:px-4 py-2 md:py-3 text-center">
                    <button
                      @click="editUser(dosen)"
                      class="px-2 md:px-3 py-1 md:py-1.5 bg-amber-500 hover:bg-amber-600 text-white rounded-lg font-semibold text-[10px] md:text-xs transition-colors mr-1.5"
                    >
                      ✏️
                    </button>
                    <button
                      @click="
                        hapusUser(dosen.id, dosen.full_name || dosen.username)
                      "
                      class="px-2 md:px-3 py-1 md:py-1.5 bg-red-600 hover:bg-red-700 text-white rounded-lg font-semibold text-[10px] md:text-xs transition-colors"
                    >
                      🗑️
                    </button>
                  </td>
                </tr>
                <tr v-if="filteredDosen.length === 0">
                  <td
                    colspan="5"
                    class="px-3 md:px-6 py-8 md:py-12 text-center"
                  >
                    <div class="text-4xl md:text-5xl mb-2 opacity-40">📋</div>
                    <p class="text-slate-500 font-semibold text-xs md:text-sm">
                      Tidak ada data dosen
                    </p>
                  </td>
                </tr>
              </tbody>
            </table>
            <div
              v-if="filteredDosen.length > 0"
              class="p-3 md:p-4 border-t border-slate-200 bg-slate-50/80 flex justify-between items-center"
            >
              <span class="text-[10px] md:text-xs font-bold text-slate-500"
                >Halaman {{ dosenPage }} dari {{ dosenTotalPages }}</span
              >
              <div class="flex gap-1.5 md:gap-2">
                <button
                  @click="dosenPage--"
                  :disabled="dosenPage === 1"
                  class="px-3 md:px-4 py-1.5 bg-white border border-slate-200 rounded-lg text-[10px] md:text-xs font-bold text-slate-600 hover:bg-indigo-50 disabled:opacity-50 transition-all"
                >
                  ← Prev
                </button>
                <button
                  @click="dosenPage++"
                  :disabled="dosenPage === dosenTotalPages"
                  class="px-3 md:px-4 py-1.5 bg-white border border-slate-200 rounded-lg text-[10px] md:text-xs font-bold text-slate-600 hover:bg-indigo-50 disabled:opacity-50 transition-all"
                >
                  Next →
                </button>
              </div>
            </div>
          </div>

          <!-- AKADEMIK TABLE -->
          <div
            v-if="userTab === 'akademik' && !loadingUsers"
            class="overflow-x-auto"
          >
            <table class="w-full min-w-[900px]">
              <thead class="bg-slate-100/80 border-b-2 border-slate-200">
                <tr>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-left text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    No
                  </th>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-left text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    Nama
                  </th>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-left text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    Email
                  </th>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-center text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    Aksi
                  </th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100">
                <tr
                  v-for="(akademik, index) in paginatedAkademik"
                  :key="akademik.id"
                  class="hover:bg-indigo-50/40 transition-colors"
                >
                  <td
                    class="px-3 md:px-4 py-2 md:py-3 text-center text-xs font-bold text-slate-500"
                  >
                    {{ (akademikPage - 1) * itemsPerPage + index + 1 }}
                  </td>
                  <td
                    class="px-3 md:px-4 py-2 md:py-3 font-semibold text-xs md:text-sm text-slate-800"
                  >
                    {{ akademik.full_name || akademik.username || "-" }}
                  </td>
                  <td
                    class="px-3 md:px-4 py-2 md:py-3 text-xs md:text-sm text-slate-700"
                  >
                    {{ akademik.email || "-" }}
                  </td>
                  <td class="px-3 md:px-4 py-2 md:py-3 text-center">
                    <button
                      @click="editUser(akademik)"
                      class="px-2 md:px-3 py-1 md:py-1.5 bg-amber-500 hover:bg-amber-600 text-white rounded-lg font-semibold text-[10px] md:text-xs transition-colors mr-1.5"
                    >
                      ✏️
                    </button>
                    <button
                      @click="
                        hapusUser(
                          akademik.id,
                          akademik.full_name || akademik.username,
                        )
                      "
                      class="px-2 md:px-3 py-1 md:py-1.5 bg-red-600 hover:bg-red-700 text-white rounded-lg font-semibold text-[10px] md:text-xs transition-colors"
                    >
                      🗑️
                    </button>
                  </td>
                </tr>
                <tr v-if="filteredAkademik.length === 0">
                  <td
                    colspan="4"
                    class="px-3 md:px-6 py-8 md:py-12 text-center"
                  >
                    <div class="text-4xl md:text-5xl mb-2 opacity-40">📋</div>
                    <p class="text-slate-500 font-semibold text-xs md:text-sm">
                      Tidak ada data akademik
                    </p>
                  </td>
                </tr>
              </tbody>
            </table>
            <div
              v-if="filteredAkademik.length > 0"
              class="p-3 md:p-4 border-t border-slate-200 bg-slate-50/80 flex justify-between items-center"
            >
              <span class="text-[10px] md:text-xs font-bold text-slate-500"
                >Halaman {{ akademikPage }} dari {{ akademikTotalPages }}</span
              >
              <div class="flex gap-1.5 md:gap-2">
                <button
                  @click="akademikPage--"
                  :disabled="akademikPage === 1"
                  class="px-3 md:px-4 py-1.5 bg-white border border-slate-200 rounded-lg text-[10px] md:text-xs font-bold text-slate-600 hover:bg-indigo-50 disabled:opacity-50 transition-all"
                >
                  ← Prev
                </button>
                <button
                  @click="akademikPage++"
                  :disabled="akademikPage === akademikTotalPages"
                  class="px-3 md:px-4 py-1.5 bg-white border border-slate-200 rounded-lg text-[10px] md:text-xs font-bold text-slate-600 hover:bg-indigo-50 disabled:opacity-50 transition-all"
                >
                  Next →
                </button>
              </div>
            </div>
          </div>

          <!-- KEMAHASISWAAN TABLE -->
          <div
            v-if="userTab === 'kemahasiswaan' && !loadingUsers"
            class="overflow-x-auto"
          >
            <table class="w-full min-w-[900px]">
              <thead class="bg-slate-100/80 border-b-2 border-slate-200">
                <tr>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-left text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    No
                  </th>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-left text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    Nama
                  </th>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-left text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    Email
                  </th>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-center text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    Aksi
                  </th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100">
                <tr
                  v-for="(kemahasiswaan, index) in paginatedKemahasiswaan"
                  :key="kemahasiswaan.id"
                  class="hover:bg-indigo-50/40 transition-colors"
                >
                  <td
                    class="px-3 md:px-4 py-2 md:py-3 text-center text-xs font-bold text-slate-500"
                  >
                    {{ (kemahasiswaanPage - 1) * itemsPerPage + index + 1 }}
                  </td>
                  <td
                    class="px-3 md:px-4 py-2 md:py-3 font-semibold text-xs md:text-sm text-slate-800"
                  >
                    {{
                      kemahasiswaan.full_name || kemahasiswaan.username || "-"
                    }}
                  </td>
                  <td
                    class="px-3 md:px-4 py-2 md:py-3 text-xs md:text-sm text-slate-700"
                  >
                    {{ kemahasiswaan.email || "-" }}
                  </td>
                  <td class="px-3 md:px-4 py-2 md:py-3 text-center">
                    <button
                      @click="editUser(kemahasiswaan)"
                      class="px-2 md:px-3 py-1 md:py-1.5 bg-amber-500 hover:bg-amber-600 text-white rounded-lg font-semibold text-[10px] md:text-xs transition-colors mr-1.5"
                    >
                      ✏️
                    </button>
                    <button
                      @click="
                        hapusUser(
                          kemahasiswaan.id,
                          kemahasiswaan.full_name || kemahasiswaan.username,
                        )
                      "
                      class="px-2 md:px-3 py-1 md:py-1.5 bg-red-600 hover:bg-red-700 text-white rounded-lg font-semibold text-[10px] md:text-xs transition-colors"
                    >
                      🗑️
                    </button>
                  </td>
                </tr>
                <tr v-if="filteredKemahasiswaan.length === 0">
                  <td
                    colspan="4"
                    class="px-3 md:px-6 py-8 md:py-12 text-center"
                  >
                    <div class="text-4xl md:text-5xl mb-2 opacity-40">📋</div>
                    <p class="text-slate-500 font-semibold text-xs md:text-sm">
                      Tidak ada data kemahasiswaan
                    </p>
                  </td>
                </tr>
              </tbody>
            </table>
            <div
              v-if="filteredKemahasiswaan.length > 0"
              class="p-3 md:p-4 border-t border-slate-200 bg-slate-50/80 flex justify-between items-center"
            >
              <span class="text-[10px] md:text-xs font-bold text-slate-500"
                >Halaman {{ kemahasiswaanPage }} dari
                {{ kemahasiswaanTotalPages }}</span
              >
              <div class="flex gap-1.5 md:gap-2">
                <button
                  @click="kemahasiswaanPage--"
                  :disabled="kemahasiswaanPage === 1"
                  class="px-3 md:px-4 py-1.5 bg-white border border-slate-200 rounded-lg text-[10px] md:text-xs font-bold text-slate-600 hover:bg-indigo-50 disabled:opacity-50 transition-all"
                >
                  ← Prev
                </button>
                <button
                  @click="kemahasiswaanPage++"
                  :disabled="kemahasiswaanPage === kemahasiswaanTotalPages"
                  class="px-3 md:px-4 py-1.5 bg-white border border-slate-200 rounded-lg text-[10px] md:text-xs font-bold text-slate-600 hover:bg-indigo-50 disabled:opacity-50 transition-all"
                >
                  Next →
                </button>
              </div>
            </div>
          </div>

          <!-- ADMIN TABLE -->
          <div
            v-if="userTab === 'admin' && !loadingUsers"
            class="overflow-x-auto"
          >
            <table class="w-full min-w-[900px]">
              <thead class="bg-slate-100/80 border-b-2 border-slate-200">
                <tr>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-left text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    No
                  </th>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-left text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    Nama
                  </th>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-left text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    Email
                  </th>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-center text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    Aksi
                  </th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100">
                <tr
                  v-for="(admin, index) in paginatedAdmin"
                  :key="admin.id"
                  class="hover:bg-indigo-50/40 transition-colors"
                >
                  <td
                    class="px-3 md:px-4 py-2 md:py-3 text-center text-xs font-bold text-slate-500"
                  >
                    {{ (adminPage - 1) * itemsPerPage + index + 1 }}
                  </td>
                  <td
                    class="px-3 md:px-4 py-2 md:py-3 font-semibold text-xs md:text-sm text-slate-800"
                  >
                    {{ admin.full_name || admin.username || "-" }}
                  </td>
                  <td
                    class="px-3 md:px-4 py-2 md:py-3 text-xs md:text-sm text-slate-700"
                  >
                    {{ admin.email || "-" }}
                  </td>
                  <td class="px-3 md:px-4 py-2 md:py-3 text-center">
                    <button
                      @click="editUser(admin)"
                      class="px-2 md:px-3 py-1 md:py-1.5 bg-amber-500 hover:bg-amber-600 text-white rounded-lg font-semibold text-[10px] md:text-xs transition-colors mr-1.5"
                    >
                      ✏️
                    </button>
                    <button
                      @click="
                        hapusUser(admin.id, admin.full_name || admin.username)
                      "
                      class="px-2 md:px-3 py-1 md:py-1.5 bg-red-600 hover:bg-red-700 text-white rounded-lg font-semibold text-[10px] md:text-xs transition-colors"
                    >
                      🗑️
                    </button>
                  </td>
                </tr>
                <tr v-if="filteredAdmin.length === 0">
                  <td
                    colspan="4"
                    class="px-3 md:px-6 py-8 md:py-12 text-center"
                  >
                    <div class="text-4xl md:text-5xl mb-2 opacity-40">📋</div>
                    <p class="text-slate-500 font-semibold text-xs md:text-sm">
                      Tidak ada data admin
                    </p>
                  </td>
                </tr>
              </tbody>
            </table>
            <div
              v-if="filteredAdmin.length > 0"
              class="p-3 md:p-4 border-t border-slate-200 bg-slate-50/80 flex justify-between items-center"
            >
              <span class="text-[10px] md:text-xs font-bold text-slate-500"
                >Halaman {{ adminPage }} dari {{ adminTotalPages }}</span
              >
              <div class="flex gap-1.5 md:gap-2">
                <button
                  @click="adminPage--"
                  :disabled="adminPage === 1"
                  class="px-3 md:px-4 py-1.5 bg-white border border-slate-200 rounded-lg text-[10px] md:text-xs font-bold text-slate-600 hover:bg-indigo-50 disabled:opacity-50 transition-all"
                >
                  ← Prev
                </button>
                <button
                  @click="adminPage++"
                  :disabled="adminPage === adminTotalPages"
                  class="px-3 md:px-4 py-1.5 bg-white border border-slate-200 rounded-lg text-[10px] md:text-xs font-bold text-slate-600 hover:bg-indigo-50 disabled:opacity-50 transition-all"
                >
                  Next →
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- ==================== KEGIATAN VIEW ==================== -->
      <div v-if="currentPage === 'kegiatan'">
        <div
          class="bg-white rounded-xl md:rounded-2xl shadow-lg border border-slate-200 overflow-hidden"
        >
          <div
            class="p-4 md:p-5 lg:p-6 border-b border-slate-200 bg-gradient-to-r from-slate-50 to-white"
          >
            <div
              class="flex flex-col md:flex-row justify-between items-start md:items-center gap-3 md:gap-4"
            >
              <div>
                <h2
                  class="text-sm md:text-base lg:text-lg font-bold text-slate-800 flex items-center gap-2 md:gap-3"
                >
                  <span class="text-xl">📋</span>
                  <span>Data Kegiatan</span>
                  <span class="ml-2 text-xs text-slate-400 font-medium"
                    >{{ kegiatanList.length }} Kegiatan</span
                  >
                </h2>
                <p class="text-xs text-slate-500 mt-1">
                  Kelola semua data kegiatan mahasiswa
                </p>
              </div>
              <button
                @click="fetchAllData"
                class="bg-green-600 hover:bg-green-700 text-white px-4 md:px-5 py-2 rounded-xl font-bold text-xs md:text-sm transition-all shadow-md flex items-center gap-2"
              >
                <span>🔄</span> Refresh
              </button>
            </div>
          </div>

          <div class="overflow-x-auto">
            <table class="w-full min-w-[900px]">
              <thead class="bg-slate-100/80 border-b-2 border-slate-200">
                <tr>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-left text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    No
                  </th>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-left text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    Mahasiswa
                  </th>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-left text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    Kegiatan
                  </th>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-center text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    Poin
                  </th>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-center text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    Status
                  </th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100">
                <tr
                  v-for="(keg, index) in kegiatanList"
                  :key="keg.id"
                  class="hover:bg-indigo-50/40 transition-colors"
                >
                  <td
                    class="px-3 md:px-4 py-2 md:py-3 text-center text-xs font-bold text-slate-500"
                  >
                    {{ index + 1 }}
                  </td>
                  <td class="px-3 md:px-4 py-2 md:py-3">
                    <p class="font-bold text-slate-800 text-xs md:text-sm">
                      {{ keg.mahasiswa_nama || "-" }}
                    </p>
                    <p class="text-[10px] text-slate-500">
                      NIM: {{ keg.nim || "-" }}
                    </p>
                  </td>
                  <td class="px-3 md:px-4 py-2 md:py-3">
                    <p class="font-semibold text-slate-800 text-xs md:text-sm">
                      {{ keg.judul_kegiatan || "-" }}
                    </p>
                    <p class="text-[10px] text-slate-500 mt-0.5">
                      {{ formatDate(keg.tanggal_kegiatan) }}
                    </p>
                  </td>
                  <td class="px-3 md:px-4 py-2 md:py-3 text-center">
                    <span
                      class="inline-block px-2 md:px-3 py-1 bg-blue-100 text-blue-800 font-bold rounded-lg text-xs md:text-sm"
                      >{{ keg.poin_valid || 0 }}</span
                    >
                  </td>
                  <td class="px-3 md:px-4 py-2 md:py-3 text-center">
                    <span
                      :class="getStatusBadgeClass(keg.status)"
                      class="px-2 md:px-3 py-1 rounded-full text-[8px] md:text-[10px] font-bold"
                    >
                      {{ formatStatusLabel(keg.status) }}
                    </span>
                  </td>
                </tr>
                <tr v-if="kegiatanList.length === 0">
                  <td
                    colspan="5"
                    class="px-3 md:px-6 py-8 md:py-12 text-center"
                  >
                    <div class="text-4xl md:text-5xl mb-2 opacity-40">📋</div>
                    <p class="text-slate-500 font-semibold text-xs md:text-sm">
                      Belum ada data kegiatan
                    </p>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- ==================== KELOLA KATEGORI VIEW ==================== -->
      <div v-if="currentPage === 'kategori'">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 lg:gap-8">
          <!-- Kolom Kiri - Form Tambah Kategori -->
          <div class="lg:col-span-5 space-y-6">
            <div
              class="bg-white rounded-xl md:rounded-2xl shadow-lg border border-slate-200 overflow-hidden"
            >
              <div
                class="p-4 md:p-5 lg:p-6 border-b border-slate-200 bg-gradient-to-r from-slate-50 to-white"
              >
                <h2
                  class="text-sm md:text-base lg:text-lg font-bold text-slate-800 flex items-center gap-2 md:gap-3"
                >
                  <span class="text-xl">✨</span>
                  <span>Tambah Kategori Baru</span>
                </h2>
                <p class="text-xs text-slate-500 mt-1">
                  Isi formulir untuk menambahkan kategori kegiatan SKPM.
                </p>
              </div>

              <form
                @submit.prevent="submitKategori"
                class="p-4 md:p-5 lg:p-6 space-y-4"
              >
                <div>
                  <label class="block text-xs font-bold text-slate-700 mb-1.5"
                    >Bidang Kegiatan <span class="text-red-500">*</span></label
                  >
                  <input
                    v-model="newKategori.bidang"
                    type="text"
                    placeholder="Contoh: Seminar, Workshop, Lomba"
                    class="w-full px-4 py-2.5 bg-white border-2 border-slate-200 focus:border-indigo-500 rounded-xl outline-none text-sm text-slate-700 transition-all"
                    required
                  />
                </div>

                <div>
                  <label class="block text-xs font-bold text-slate-700 mb-1.5"
                    >Nama Kegiatan <span class="text-red-500">*</span></label
                  >
                  <input
                    v-model="newKategori.nama_kegiatan"
                    type="text"
                    placeholder="Detail kegiatan..."
                    class="w-full px-4 py-2.5 bg-white border-2 border-slate-200 focus:border-indigo-500 rounded-xl outline-none text-sm text-slate-700 transition-all"
                    required
                  />
                  <p v-if="kategoriError" class="text-red-500 text-xs mt-1">
                    {{ kategoriError }}
                  </p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div>
                    <label class="block text-xs font-bold text-slate-700 mb-1.5"
                      >Partisipasi (Peran)</label
                    >
                    <input
                      v-model="newKategori.partisipasi"
                      type="text"
                      placeholder="Contoh: Ketua, Anggota"
                      class="w-full px-4 py-2.5 bg-white border-2 border-slate-200 focus:border-indigo-500 rounded-xl outline-none text-sm text-slate-700 transition-all"
                    />
                  </div>
                  <div>
                    <label class="block text-xs font-bold text-slate-700 mb-1.5"
                      >Level <span class="text-red-500">*</span></label
                    >
                    <select
                      v-model="newKategori.level"
                      class="w-full px-4 py-2.5 bg-white border-2 border-slate-200 focus:border-indigo-500 rounded-xl outline-none text-sm text-slate-700 transition-all"
                      required
                    >
                      <option value="" disabled selected>
                        -- Pilih Level --
                      </option>
                      <option value="Lokal/Daerah">
                        Tingkat Lokal / Daerah
                      </option>
                      <option value="Nasional">Tingkat Nasional</option>
                      <option value="Internasional">
                        Tingkat Internasional
                      </option>
                    </select>
                  </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div>
                    <label class="block text-xs font-bold text-slate-700 mb-1.5"
                      >Sifat Kegiatan</label
                    >
                    <select
                      v-model="newKategori.sifat"
                      class="w-full px-4 py-2.5 bg-white border-2 border-slate-200 focus:border-indigo-500 rounded-xl outline-none text-sm text-slate-700 transition-all"
                    >
                      <option value="Pilihan">Sifat Pilihan</option>
                      <option value="Wajib">Sifat Wajib</option>
                    </select>
                  </div>
                  <div>
                    <label class="block text-xs font-bold text-slate-700 mb-1.5"
                      >Bobot Poin <span class="text-red-500">*</span></label
                    >
                    <input
                      v-model="newKategori.bobot_poin"
                      type="number"
                      placeholder="Nilai poin"
                      class="w-full px-4 py-2.5 bg-white border-2 border-slate-200 focus:border-indigo-500 rounded-xl outline-none text-sm font-bold text-slate-700 transition-all"
                      required
                    />
                  </div>
                </div>

                <button
                  type="submit"
                  :disabled="loadingKategori"
                  class="w-full bg-gradient-to-r from-indigo-600 to-indigo-700 hover:from-indigo-700 hover:to-indigo-800 text-white py-3 rounded-xl font-bold text-sm transition-all shadow-lg flex items-center justify-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  {{ loadingKategori ? "Menyimpan..." : "✨ Simpan Kategori" }}
                </button>
              </form>
            </div>
          </div>

          <!-- Kolom Kanan - Daftar Kategori -->
          <div class="lg:col-span-7 space-y-6">
            <div
              class="bg-white rounded-xl md:rounded-2xl shadow-lg border border-slate-200 overflow-hidden"
            >
              <div
                class="p-4 md:p-5 lg:p-6 border-b border-slate-200 bg-gradient-to-r from-slate-50 to-white"
              >
                <h2
                  class="text-sm md:text-base lg:text-lg font-bold text-slate-800 flex items-center gap-2 md:gap-3"
                >
                  <span class="text-xl">📋</span>
                  <span>Daftar Kategori</span>
                  <span class="ml-auto text-xs text-slate-400 font-medium"
                    >{{ listKategori.length }} Kategori</span
                  >
                </h2>
                <p class="text-xs text-slate-500 mt-1">
                  Seluruh kategori yang tersedia di sistem.
                </p>
              </div>
              <div class="max-h-[500px] overflow-y-auto">
                <table class="w-full min-w-[500px]">
                  <thead
                    class="bg-slate-100/80 border-b-2 border-slate-200 sticky top-0 shadow-sm"
                  >
                    <tr>
                      <th
                        class="px-3 md:px-4 py-2 md:py-3 text-left text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                      >
                        No
                      </th>
                      <th
                        class="px-3 md:px-4 py-2 md:py-3 text-left text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                      >
                        Nama Kegiatan
                      </th>
                      <th
                        class="px-3 md:px-4 py-2 md:py-3 text-center text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                      >
                        Poin
                      </th>
                      <th
                        class="px-3 md:px-4 py-2 md:py-3 text-center text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                      >
                        Aksi
                      </th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-slate-100">
                    <tr
                      v-for="(kat, index) in paginatedKategori"
                      :key="kat.id"
                      class="hover:bg-indigo-50/40 transition-colors"
                    >
                      <td
                        class="px-3 md:px-4 py-2 md:py-3 text-center text-xs font-bold text-slate-500"
                      >
                        {{
                          (kategoriPage - 1) * kategoriItemsPerPage + index + 1
                        }}
                      </td>
                      <td class="px-3 md:px-4 py-2 md:py-3">
                        <p class="font-bold text-slate-800 text-xs md:text-sm">
                          {{ kat.nama_kegiatan }}
                        </p>
                        <p class="text-[10px] text-slate-500 mt-0.5">
                          {{ kat.bidang }} • {{ kat.level }}
                        </p>
                      </td>
                      <td class="px-3 md:px-4 py-2 md:py-3 text-center">
                        <span
                          class="inline-block px-2 md:px-3 py-1 bg-blue-100 text-blue-800 font-bold rounded-lg text-[10px] md:text-xs"
                          >{{ kat.bobot_poin }}</span
                        >
                      </td>
                      <td class="px-3 md:px-4 py-2 md:py-3 text-center">
                        <button
                          @click="editKategori(kat)"
                          class="px-2 md:px-3 py-1 md:py-1.5 bg-amber-500 hover:bg-amber-600 text-white rounded-lg font-semibold text-[10px] md:text-xs transition-colors mr-1.5"
                        >
                          ✏️
                        </button>
                        <button
                          @click="hapusKategori(kat.id)"
                          class="px-2 md:px-3 py-1 md:py-1.5 bg-red-600 hover:bg-red-700 text-white rounded-lg font-semibold text-[10px] md:text-xs transition-colors"
                        >
                          🗑️
                        </button>
                      </td>
                    </tr>
                    <tr v-if="listKategori.length === 0">
                      <td
                        colspan="4"
                        class="px-3 md:px-6 py-8 md:py-12 text-center"
                      >
                        <div class="text-4xl md:text-5xl mb-2 opacity-40">
                          📋
                        </div>
                        <p
                          class="text-slate-500 font-semibold text-xs md:text-sm"
                        >
                          Belum ada kategori terdaftar.
                        </p>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <div
                v-if="listKategori.length > kategoriItemsPerPage"
                class="p-3 md:p-4 border-t border-slate-200 bg-slate-50/80 flex justify-between items-center"
              >
                <span class="text-[10px] md:text-xs font-bold text-slate-500"
                  >Halaman {{ kategoriPage }} dari
                  {{ kategoriTotalPages }}</span
                >
                <div class="flex gap-1.5 md:gap-2">
                  <button
                    @click="kategoriPage--"
                    :disabled="kategoriPage === 1"
                    class="px-3 md:px-4 py-1.5 bg-white border border-slate-200 rounded-lg text-[10px] md:text-xs font-bold text-slate-600 hover:bg-indigo-50 disabled:opacity-50 transition-all"
                  >
                    ← Prev
                  </button>
                  <button
                    @click="kategoriPage++"
                    :disabled="kategoriPage === kategoriTotalPages"
                    class="px-3 md:px-4 py-1.5 bg-white border border-slate-200 rounded-lg text-[10px] md:text-xs font-bold text-slate-600 hover:bg-indigo-50 disabled:opacity-50 transition-all"
                  >
                    Next →
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- ==================== PLOTTING DPA VIEW ==================== -->
      <div v-if="currentPage === 'plotting'">
        <!-- Tombol Tambah Plotting -->
        <div class="mb-4">
          <button
            @click="showPlottingForm = !showPlottingForm"
            class="bg-indigo-600 hover:bg-indigo-700 text-white px-6 py-3 rounded-xl font-bold text-sm transition-all shadow-lg flex items-center gap-2"
          >
            <span class="text-lg">➕</span>
            {{ showPlottingForm ? "Tutup Form" : "Tambah Plotting" }}
          </button>
        </div>

        <!-- Form Plotting DPA - Muncul saat tombol diklik -->
        <div
          v-if="showPlottingForm"
          class="bg-white rounded-2xl shadow-xl border border-slate-200 overflow-hidden mb-6"
        >
          <div
            class="p-6 border-b border-slate-200 bg-gradient-to-r from-indigo-50 to-white"
          >
            <h2
              class="text-xl font-bold text-slate-800 flex items-center gap-3"
            >
              <span class="text-2xl">📋</span>
              Plot Dosen Pembimbing Baru
            </h2>
            <p class="text-sm text-slate-500 mt-1">
              Cari dan pilih Mahasiswa serta DPA yang akan dihubungkan.
            </p>
          </div>

          <div class="p-6 space-y-8">
            <!-- STEP 1: Pilih Mahasiswa -->
            <div>
              <div class="flex items-center gap-3 mb-4">
                <span
                  class="flex items-center justify-center w-8 h-8 bg-indigo-600 text-white rounded-full text-sm font-bold"
                  >1</span
                >
                <h3 class="text-lg font-semibold text-slate-800">
                  Pilih Mahasiswa
                </h3>
              </div>

              <!-- Search Mahasiswa -->
              <div class="relative mb-4">
                <div
                  class="absolute inset-y-0 left-3 flex items-center pointer-events-none"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5 text-slate-400"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                    />
                  </svg>
                </div>
                <input
                  v-model="searchMahasiswa"
                  type="text"
                  placeholder="Cari Nama atau NIM..."
                  class="w-full pl-10 pr-4 py-2.5 border-2 border-slate-200 focus:border-indigo-500 rounded-xl outline-none text-sm text-slate-700 transition-all bg-slate-50/50"
                />
              </div>

              <!-- Tabel Mahasiswa -->
              <div class="border border-slate-200 rounded-xl overflow-hidden">
                <table class="w-full">
                  <thead class="bg-slate-50 border-b border-slate-200">
                    <tr>
                      <th
                        class="px-4 py-3 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider w-12"
                      >
                        Pilihan
                      </th>
                      <th
                        class="px-4 py-3 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider"
                      >
                        Mahasiswa
                      </th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-slate-100">
                    <tr
                      v-for="mhs in filteredMahasiswaList"
                      :key="mhs.id"
                      class="hover:bg-indigo-50/40 transition-colors cursor-pointer"
                      @click="selectMahasiswa(mhs)"
                    >
                      <td class="px-4 py-3">
                        <div class="flex items-center">
                          <input
                            type="radio"
                            :value="mhs.id"
                            v-model="assignment.mahasiswa_id"
                            class="w-4 h-4 text-indigo-600 border-slate-300 focus:ring-indigo-500"
                          />
                        </div>
                      </td>
                      <td class="px-4 py-3">
                        <p class="font-semibold text-slate-800 text-sm">
                          {{ mhs.full_name || mhs.username || "Tanpa Nama" }}
                        </p>
                        <p class="text-xs text-slate-500">
                          NIM: {{ mhs.nim_nip || "-" }}
                        </p>
                      </td>
                    </tr>
                    <tr v-if="filteredMahasiswaList.length === 0">
                      <td
                        colspan="2"
                        class="px-4 py-8 text-center text-slate-500 text-sm"
                      >
                        <div class="text-3xl mb-2 opacity-40">📋</div>
                        <p>Tidak ada mahasiswa ditemukan</p>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <!-- STEP 2: Pilih DPA -->
            <div>
              <div class="flex items-center gap-3 mb-4">
                <span
                  class="flex items-center justify-center w-8 h-8 bg-indigo-600 text-white rounded-full text-sm font-bold"
                  >2</span
                >
                <h3 class="text-lg font-semibold text-slate-800">
                  Pilih Dosen Pembimbing (DPA)
                </h3>
              </div>

              <!-- Search DPA -->
              <div class="relative mb-4">
                <div
                  class="absolute inset-y-0 left-3 flex items-center pointer-events-none"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5 text-slate-400"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                    />
                  </svg>
                </div>
                <input
                  v-model="searchDPA"
                  type="text"
                  placeholder="Cari Nama atau NIP..."
                  class="w-full pl-10 pr-4 py-2.5 border-2 border-slate-200 focus:border-indigo-500 rounded-xl outline-none text-sm text-slate-700 transition-all bg-slate-50/50"
                />
              </div>

              <!-- Tabel DPA -->
              <div class="border border-slate-200 rounded-xl overflow-hidden">
                <table class="w-full">
                  <thead class="bg-slate-50 border-b border-slate-200">
                    <tr>
                      <th
                        class="px-4 py-3 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider w-12"
                      >
                        Pilihan
                      </th>
                      <th
                        class="px-4 py-3 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider"
                      >
                        Dosen
                      </th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-slate-100">
                    <tr
                      v-for="dpa in filteredDPAList"
                      :key="dpa.id"
                      class="hover:bg-indigo-50/40 transition-colors cursor-pointer"
                      @click="selectDPA(dpa)"
                    >
                      <td class="px-4 py-3">
                        <div class="flex items-center">
                          <input
                            type="radio"
                            :value="dpa.id"
                            v-model="assignment.dpa_id"
                            class="w-4 h-4 text-indigo-600 border-slate-300 focus:ring-indigo-500"
                          />
                        </div>
                      </td>
                      <td class="px-4 py-3">
                        <p class="font-semibold text-slate-800 text-sm">
                          {{ dpa.full_name || dpa.username || "Tanpa Nama" }}
                        </p>
                        <p class="text-xs text-slate-500">
                          NIP: {{ dpa.nim_nip || "-" }}
                        </p>
                      </td>
                    </tr>
                    <tr v-if="filteredDPAList.length === 0">
                      <td
                        colspan="2"
                        class="px-4 py-8 text-center text-slate-500 text-sm"
                      >
                        <div class="text-3xl mb-2 opacity-40">📋</div>
                        <p>Tidak ada dosen ditemukan</p>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <!-- Tombol Aksi Form -->
            <div class="flex justify-end gap-3 pt-4 border-t border-slate-200">
              <button
                @click="resetAssignment"
                class="px-6 py-2.5 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-xl font-semibold text-sm transition-all"
              >
                Batal
              </button>
              <button
                @click="assignDPA"
                :disabled="
                  !assignment.mahasiswa_id ||
                  !assignment.dpa_id ||
                  loadingAssign
                "
                class="px-6 py-2.5 bg-indigo-600 hover:bg-indigo-700 text-white rounded-xl font-semibold text-sm transition-all shadow-lg shadow-indigo-200 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
              >
                <span
                  v-if="loadingAssign"
                  class="inline-block w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"
                ></span>
                {{ loadingAssign ? "Memproses..." : "💾 Simpan Plotting" }}
              </button>
            </div>
          </div>
        </div>

        <!-- Daftar Plotting DPA -->
        <div
          class="bg-white rounded-xl md:rounded-2xl shadow-lg border border-slate-200 overflow-hidden"
        >
          <div
            class="p-4 md:p-5 lg:p-6 border-b border-slate-200 bg-gradient-to-r from-slate-50 to-white"
          >
            <div
              class="flex flex-col md:flex-row justify-between items-start md:items-center gap-3 md:gap-4"
            >
              <div>
                <h2
                  class="text-sm md:text-base lg:text-lg font-bold text-slate-800 flex items-center gap-2 md:gap-3"
                >
                  <span class="text-xl">👥</span>
                  <span>Daftar Plotting DPA</span>
                  <span class="ml-2 text-xs text-slate-400 font-medium"
                    >{{ filteredPlotting.length }} Mahasiswa</span
                  >
                </h2>
                <p class="text-xs text-slate-500 mt-1">
                  Seluruh mahasiswa yang sudah memiliki Dosen Pembimbing
                  Akademik.
                </p>
              </div>
              <div class="relative w-full md:w-64">
                <div
                  class="absolute inset-y-0 left-3 flex items-center pointer-events-none"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-4 w-4 text-slate-400"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                    />
                  </svg>
                </div>
                <input
                  v-model="searchPlotting"
                  type="text"
                  placeholder="Cari Nama atau NIM..."
                  class="w-full pl-9 pr-4 py-2 bg-white border-2 border-slate-200 focus:border-indigo-500 rounded-xl outline-none text-xs md:text-sm font-medium text-slate-700 transition-all"
                />
              </div>
            </div>
          </div>

          <div class="overflow-x-auto">
            <table class="w-full min-w-[800px]">
              <thead class="bg-slate-100/80 border-b-2 border-slate-200">
                <tr>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-left text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    No
                  </th>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-left text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    Mahasiswa
                  </th>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-left text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    NIM
                  </th>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-left text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    DPA
                  </th>
                  <th
                    class="px-3 md:px-4 py-2 md:py-3 text-center text-[8px] md:text-[10px] font-bold text-slate-500 uppercase tracking-wider"
                  >
                    Aksi
                  </th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100">
                <tr
                  v-for="(item, index) in paginatedPlotting"
                  :key="item.id"
                  class="hover:bg-indigo-50/40 transition-colors"
                >
                  <td
                    class="px-3 md:px-4 py-2 md:py-3 text-center text-xs font-bold text-slate-500"
                  >
                    {{ (plottingPage - 1) * plottingItemsPerPage + index + 1 }}
                  </td>
                  <td class="px-3 md:px-4 py-2 md:py-3">
                    <p class="font-bold text-slate-800 text-xs md:text-sm">
                      {{ item.full_name || item.username || "-" }}
                    </p>
                    <p class="text-[10px] text-slate-500">
                      {{ item.prodi || "-" }}
                    </p>
                  </td>
                  <td
                    class="px-3 md:px-4 py-2 md:py-3 font-mono text-xs md:text-sm text-slate-700"
                  >
                    {{ item.nim_nip || "-" }}
                  </td>
                  <td class="px-3 md:px-4 py-2 md:py-3">
                    <div class="flex items-center gap-2">
                      <span
                        class="w-5 h-5 bg-green-100 border border-green-300 text-green-700 rounded-full flex items-center justify-center text-[10px] font-bold"
                        >✓</span
                      >
                      <span
                        class="font-semibold text-slate-800 text-xs md:text-sm"
                        >{{ item.dpa_name || "-" }}</span
                      >
                    </div>
                  </td>
                  <td class="px-3 md:px-4 py-2 md:py-3 text-center">
                    <button
                      @click="hapusPlotting(item.id, item.full_name)"
                      class="px-2 md:px-3 py-1 md:py-1.5 bg-red-600 hover:bg-red-700 text-white rounded-lg font-semibold text-[10px] md:text-xs transition-colors"
                    >
                      🗑️ Hapus
                    </button>
                  </td>
                </tr>
                <tr v-if="filteredPlotting.length === 0">
                  <td
                    colspan="5"
                    class="px-3 md:px-6 py-8 md:py-12 text-center"
                  >
                    <div class="text-4xl md:text-5xl mb-2 opacity-40">📋</div>
                    <p class="text-slate-500 font-semibold text-xs md:text-sm">
                      Belum ada mahasiswa yang memiliki DPA
                    </p>
                    <p class="text-slate-400 text-[10px] mt-1">
                      Klik tombol "Tambah Plotting" untuk menghubungkan
                      mahasiswa dengan DPA
                    </p>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <div
            v-if="filteredPlotting.length > 0"
            class="p-3 md:p-4 border-t border-slate-200 bg-slate-50/80 flex justify-between items-center"
          >
            <span class="text-[10px] md:text-xs font-bold text-slate-500"
              >Halaman {{ plottingPage }} dari {{ plottingTotalPages }}</span
            >
            <div class="flex gap-1.5 md:gap-2">
              <button
                @click="plottingPage--"
                :disabled="plottingPage === 1"
                class="px-3 md:px-4 py-1.5 bg-white border border-slate-200 rounded-lg text-[10px] md:text-xs font-bold text-slate-600 hover:bg-indigo-50 disabled:opacity-50 transition-all"
              >
                ← Prev
              </button>
              <button
                @click="plottingPage++"
                :disabled="plottingPage === plottingTotalPages"
                class="px-3 md:px-4 py-1.5 bg-white border border-slate-200 rounded-lg text-[10px] md:text-xs font-bold text-slate-600 hover:bg-indigo-50 disabled:opacity-50 transition-all"
              >
                Next →
              </button>
            </div>
          </div>
        </div>
      </div>
    </main>

    <!-- MODAL ADD/EDIT USER -->
    <transition name="modal">
      <div
        v-if="showAddUserModal || showEditUserModal"
        class="fixed inset-0 bg-slate-900/80 z-[60] flex items-center justify-center p-4 overflow-y-auto"
        @click.self="closeUserModal"
      >
        <div
          class="bg-white rounded-xl w-full max-w-2xl p-6 md:p-8 shadow-2xl border border-slate-300 max-h-[90vh] overflow-y-auto"
        >
          <h3 class="text-xl md:text-2xl font-bold text-slate-900 mb-2">
            {{ showEditUserModal ? "Edit Data User" : "Tambah User Baru" }}
          </h3>
          <p class="text-slate-600 text-sm mb-6 border-b border-slate-200 pb-4">
            {{
              showEditUserModal
                ? "Perbarui informasi user ini"
                : "Isi formulir untuk menambahkan user baru ke sistem"
            }}
          </p>

          <div class="space-y-4">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1.5"
                  >Role <span class="text-red-500">*</span></label
                >
                <select
                  v-model="userForm.role"
                  class="w-full px-4 py-2.5 bg-white border-2 border-slate-200 focus:border-indigo-500 rounded-xl outline-none text-sm text-slate-700 transition-all"
                  required
                >
                  <option value="mahasiswa">Mahasiswa</option>
                  <option value="dpa">Dosen / DPA</option>
                  <option value="akademik">Akademik</option>
                  <option value="kemahasiswaan">Kemahasiswaan</option>
                  <option value="superadmin">Admin</option>
                </select>
              </div>
              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1.5"
                  >Username <span class="text-red-500">*</span></label
                >
                <input
                  v-model="userForm.username"
                  type="text"
                  class="w-full px-4 py-2.5 bg-white border-2 border-slate-200 focus:border-indigo-500 rounded-xl outline-none text-sm text-slate-700 transition-all"
                  required
                />
              </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1.5"
                  >Nama Lengkap</label
                >
                <input
                  v-model="userForm.full_name"
                  type="text"
                  class="w-full px-4 py-2.5 bg-white border-2 border-slate-200 focus:border-indigo-500 rounded-xl outline-none text-sm text-slate-700 transition-all"
                />
              </div>
              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1.5"
                  >Email</label
                >
                <input
                  v-model="userForm.email"
                  type="email"
                  class="w-full px-4 py-2.5 bg-white border-2 border-slate-200 focus:border-indigo-500 rounded-xl outline-none text-sm text-slate-700 transition-all"
                />
              </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1.5">{{
                  userForm.role === "mahasiswa"
                    ? "NIM"
                    : userForm.role === "dpa"
                      ? "NIP"
                      : "NIM/NIP (Opsional)"
                }}</label>
                <input
                  v-model="userForm.nim_nip"
                  type="text"
                  class="w-full px-4 py-2.5 bg-white border-2 border-slate-200 focus:border-indigo-500 rounded-xl outline-none text-sm text-slate-700 transition-all"
                />
              </div>
              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1.5"
                  >No. Telepon</label
                >
                <input
                  v-model="userForm.no_telp"
                  type="text"
                  class="w-full px-4 py-2.5 bg-white border-2 border-slate-200 focus:border-indigo-500 rounded-xl outline-none text-sm text-slate-700 transition-all"
                />
              </div>
            </div>

            <div
              v-if="userForm.role === 'mahasiswa'"
              class="grid grid-cols-1 md:grid-cols-2 gap-4"
            >
              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1.5"
                  >Prodi</label
                >
                <input
                  v-model="userForm.prodi"
                  type="text"
                  class="w-full px-4 py-2.5 bg-white border-2 border-slate-200 focus:border-indigo-500 rounded-xl outline-none text-sm text-slate-700 transition-all"
                  placeholder="Program Studi"
                />
              </div>
              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1.5"
                  >Angkatan</label
                >
                <input
                  v-model="userForm.angkatan"
                  type="text"
                  class="w-full px-4 py-2.5 bg-white border-2 border-slate-200 focus:border-indigo-500 rounded-xl outline-none text-sm text-slate-700 transition-all"
                  placeholder="Tahun angkatan"
                />
              </div>
            </div>

            <div
              v-if="userForm.role === 'dpa'"
              class="grid grid-cols-1 md:grid-cols-2 gap-4"
            >
              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1.5"
                  >NIDN</label
                >
                <input
                  v-model="userForm.nidn"
                  type="text"
                  class="w-full px-4 py-2.5 bg-white border-2 border-slate-200 focus:border-indigo-500 rounded-xl outline-none text-sm text-slate-700 transition-all"
                  placeholder="NIDN"
                />
              </div>
              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1.5"
                  >Jabatan</label
                >
                <input
                  v-model="userForm.jabatan"
                  type="text"
                  class="w-full px-4 py-2.5 bg-white border-2 border-slate-200 focus:border-indigo-500 rounded-xl outline-none text-sm text-slate-700 transition-all"
                  placeholder="Jabatan"
                />
              </div>
            </div>

            <div>
              <label class="block text-xs font-bold text-slate-700 mb-1.5"
                >Password <span class="text-red-500">*</span
                ><span
                  v-if="showEditUserModal"
                  class="text-xs font-normal text-slate-500 ml-2"
                  >(Kosongkan jika tidak ingin mengubah)</span
                ></label
              >
              <input
                v-model="userForm.password"
                type="password"
                :required="!showEditUserModal"
                class="w-full px-4 py-2.5 bg-white border-2 border-slate-200 focus:border-indigo-500 rounded-xl outline-none text-sm text-slate-700 transition-all"
                :placeholder="
                  showEditUserModal
                    ? 'Masukkan password baru jika ingin mengubah'
                    : 'Masukkan password'
                "
              />
            </div>
          </div>

          <div class="flex gap-4 mt-6 pt-4 border-t border-slate-200">
            <button
              @click="closeUserModal"
              class="flex-1 py-2.5 bg-slate-200 border border-slate-300 text-slate-700 rounded-xl font-bold text-sm hover:bg-slate-300 transition-colors"
            >
              Batal
            </button>
            <button
              @click="showEditUserModal ? updateUser() : createUser()"
              :disabled="loadingUser"
              class="flex-1 py-2.5 bg-indigo-600 text-white rounded-xl font-bold text-sm hover:bg-indigo-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {{
                loadingUser
                  ? "Memproses..."
                  : showEditUserModal
                    ? "Simpan Perubahan"
                    : "Tambah User"
              }}
            </button>
          </div>
        </div>
      </div>
    </transition>

    <!-- MODAL EDIT KATEGORI -->
    <transition name="modal">
      <div
        v-if="showEditKategoriModal"
        class="fixed inset-0 bg-slate-900/80 z-[60] flex items-center justify-center p-4"
        @click.self="showEditKategoriModal = false"
      >
        <div
          class="bg-white rounded-xl w-full max-w-2xl p-6 md:p-8 shadow-2xl border border-slate-300"
        >
          <h3 class="text-xl md:text-2xl font-bold text-slate-900 mb-2">
            Edit Data Kategori
          </h3>
          <p class="text-slate-600 text-sm mb-6 border-b border-slate-200 pb-4">
            Perbarui informasi kategori ini.
          </p>

          <div class="space-y-4">
            <div>
              <label class="block text-xs font-bold text-slate-700 mb-1.5"
                >Bidang Kegiatan</label
              >
              <input
                v-model="selectedKategori.bidang"
                type="text"
                class="w-full px-4 py-2.5 bg-white border-2 border-slate-200 focus:border-indigo-500 rounded-xl outline-none text-sm text-slate-700 transition-all"
                required
              />
            </div>
            <div>
              <label class="block text-xs font-bold text-slate-700 mb-1.5"
                >Nama Kegiatan</label
              >
              <input
                v-model="selectedKategori.nama_kegiatan"
                type="text"
                class="w-full px-4 py-2.5 bg-white border-2 border-slate-200 focus:border-indigo-500 rounded-xl outline-none text-sm text-slate-700 transition-all"
                required
              />
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1.5"
                  >Partisipasi</label
                >
                <input
                  v-model="selectedKategori.partisipasi"
                  type="text"
                  class="w-full px-4 py-2.5 bg-white border-2 border-slate-200 focus:border-indigo-500 rounded-xl outline-none text-sm text-slate-700 transition-all"
                />
              </div>
              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1.5"
                  >Level</label
                >
                <select
                  v-model="selectedKategori.level"
                  class="w-full px-4 py-2.5 bg-white border-2 border-slate-200 focus:border-indigo-500 rounded-xl outline-none text-sm text-slate-700 transition-all"
                >
                  <option value="Lokal/Daerah">Lokal/Daerah</option>
                  <option value="Nasional">Nasional</option>
                  <option value="Internasional">Internasional</option>
                </select>
              </div>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1.5"
                  >Sifat</label
                >
                <select
                  v-model="selectedKategori.sifat"
                  class="w-full px-4 py-2.5 bg-white border-2 border-slate-200 focus:border-indigo-500 rounded-xl outline-none text-sm text-slate-700 transition-all"
                >
                  <option value="Pilihan">Pilihan</option>
                  <option value="Wajib">Wajib</option>
                </select>
              </div>
              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1.5"
                  >Bobot Poin</label
                >
                <input
                  v-model="selectedKategori.bobot_poin"
                  type="number"
                  class="w-full px-4 py-2.5 bg-white border-2 border-slate-200 focus:border-indigo-500 rounded-xl outline-none text-sm text-slate-700 transition-all"
                />
              </div>
            </div>
          </div>

          <div class="flex gap-4 mt-6 pt-4 border-t border-slate-200">
            <button
              @click="showEditKategoriModal = false"
              class="flex-1 py-2.5 bg-slate-200 border border-slate-300 text-slate-700 rounded-xl font-bold text-sm hover:bg-slate-300 transition-colors"
            >
              Batal
            </button>
            <button
              @click="saveEditKategori"
              class="flex-1 py-2.5 bg-indigo-600 text-white rounded-xl font-bold text-sm hover:bg-indigo-700 transition-colors"
            >
              Simpan Perubahan
            </button>
          </div>
        </div>
      </div>
    </transition>

    <!-- MODAL TOLAK PENGAJUAN -->
    <transition name="modal">
      <div
        v-if="showRejectModal"
        class="fixed inset-0 bg-slate-900/80 z-[60] flex items-center justify-center p-4"
        @click.self="closeRejectModal"
      >
        <div
          class="bg-white rounded-xl w-full max-w-md p-6 md:p-8 shadow-2xl border border-slate-300"
        >
          <h3 class="text-xl md:text-2xl font-bold text-slate-900 mb-2">
            Tolak Pengajuan
          </h3>
          <p class="text-slate-600 text-sm mb-6 border-b border-slate-200 pb-4">
            Berikan alasan penolakan.
          </p>

          <div class="space-y-4">
            <div>
              <label class="block text-xs font-bold text-slate-700 mb-1.5"
                >Alasan Penolakan <span class="text-red-500">*</span></label
              >
              <textarea
                v-model="rejectReason"
                rows="4"
                class="w-full px-4 py-2.5 bg-white border-2 border-slate-200 focus:border-red-500 rounded-xl outline-none text-sm text-slate-700 transition-all"
                placeholder="Tuliskan alasan penolakan..."
              ></textarea>
            </div>
          </div>

          <div class="flex gap-4 mt-6 pt-4 border-t border-slate-200">
            <button
              @click="closeRejectModal"
              class="flex-1 py-2.5 bg-slate-200 border border-slate-300 text-slate-700 rounded-xl font-bold text-sm hover:bg-slate-300 transition-colors"
            >
              Batal
            </button>
            <button
              @click="confirmReject"
              :disabled="!rejectReason.trim()"
              :class="[
                'flex-1 py-2.5 text-white rounded-xl font-bold text-sm transition-colors',
                rejectReason.trim()
                  ? 'bg-red-600 hover:bg-red-700'
                  : 'bg-slate-400 cursor-not-allowed',
              ]"
            >
              Konfirmasi Tolak
            </button>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from "vue";
import { useRouter } from "vue-router";
import api from "../api/api";

const router = useRouter();
const currentPage = ref("dashboard");
const showPlottingForm = ref(false);

// LOADING STATES
const loadingKategori = ref(false);
const loadingAssign = ref(false);
const loadingUser = ref(false);
const loadingUsers = ref(false);
const kategoriError = ref("");

// USER INFO
const userFullName = ref("");
const userInitials = ref("SA");

// STATS
const stats = ref({
  total_mahasiswa: 0,
  total_pending: 0,
  total_valid: 0,
  total_tolak: 0,
});

// DATA LISTS
const recentLogs = ref([]);
const dpaList = ref([]);
const allMahasiswaList = ref([]);
const unassignedMhs = ref([]);
const listKategori = ref([]);
const listPlotting = ref([]);
const allUsers = ref([]);
const kegiatanList = ref([]);

// PLOTTING SEARCH
const searchMahasiswa = ref("");
const searchDPA = ref("");

// FORM MODELS
const newKategori = ref({
  bidang: "",
  nama_kegiatan: "",
  partisipasi: "",
  level: "",
  sifat: "Pilihan",
  bobot_poin: 0,
});

const assignment = ref({
  mahasiswa_id: "",
  dpa_id: "",
});

// EDIT KATEGORI
const showEditKategoriModal = ref(false);
const selectedKategori = ref({});

// USER MANAGEMENT
const userTab = ref("mahasiswa");
const showAddUserModal = ref(false);
const showEditUserModal = ref(false);
const searchUser = ref("");

const userForm = ref({
  id: null,
  username: "",
  password: "",
  full_name: "",
  email: "",
  nim_nip: "",
  no_telp: "",
  prodi: "",
  angkatan: "",
  nidn: "",
  jabatan: "",
  role: "mahasiswa",
});

// PAGINATION
const logsPage = ref(1);
const logsItemsPerPage = ref(10);
const kategoriPage = ref(1);
const kategoriItemsPerPage = ref(5);
const plottingPage = ref(1);
const plottingItemsPerPage = ref(10);
const searchPlotting = ref("");
const mahasiswaPage = ref(1);
const dosenPage = ref(1);
const akademikPage = ref(1);
const kemahasiswaanPage = ref(1);
const adminPage = ref(1);
const itemsPerPage = ref(10);

// MODAL REJECT
const showRejectModal = ref(false);
const rejectReason = ref("");
const pendingRejectId = ref(null);

// HELPER FUNCTIONS
const resetPagination = () => {
  mahasiswaPage.value = 1;
  dosenPage.value = 1;
  akademikPage.value = 1;
  kemahasiswaanPage.value = 1;
  adminPage.value = 1;
};

const matchRole = (userRole, targetRole) => {
  if (!userRole) return false;
  const role = userRole.toString().toLowerCase().trim();

  const roleMappings = {
    mahasiswa: ["mahasiswa", "mhs", "student"],
    dosen: ["dpa", "dosen", "lecturer", "pembimbing"],
    akademik: ["akademik", "academic"],
    kemahasiswaan: ["kemahasiswaan", "studentaffairs"],
    admin: ["superadmin", "admin", "administrator"],
  };

  const targets = roleMappings[targetRole] || [targetRole];
  return targets.includes(role);
};

const isKategoriNameExists = (name, excludeId = null) => {
  return listKategori.value.some(
    (kat) =>
      kat.nama_kegiatan.toLowerCase() === name.toLowerCase() &&
      kat.id !== excludeId,
  );
};

const getStatusBadgeClass = (status) => {
  const s = String(status).toLowerCase();
  if (s === "approved_final" || s === "valid")
    return "bg-green-100 text-green-700";
  if (s === "approved_dpa") return "bg-blue-100 text-blue-700";
  if (s === "rejected" || s === "tolak") return "bg-red-100 text-red-700";
  if (s === "pending") return "bg-amber-100 text-amber-700";
  return "bg-slate-100 text-slate-600";
};

const formatStatusLabel = (status) => {
  const s = String(status).toLowerCase();
  if (s === "approved_final" || s === "valid") return "✅ Disetujui";
  if (s === "approved_dpa") return "🔵 ACC DPA";
  if (s === "rejected" || s === "tolak") return "❌ Ditolak";
  if (s === "pending") return "🕒 Menunggu DPA";
  return status;
};

const formatDate = (date) => {
  if (!date) return "-";
  return new Date(date).toLocaleDateString("id-ID", {
    day: "numeric",
    month: "short",
    year: "numeric",
  });
};

// COMPUTED USERS
const allMahasiswa = computed(() =>
  allUsers.value.filter((u) => matchRole(u.role, "mahasiswa")),
);
const allDosen = computed(() =>
  allUsers.value.filter((u) => matchRole(u.role, "dosen")),
);
const allAkademik = computed(() =>
  allUsers.value.filter((u) => matchRole(u.role, "akademik")),
);
const allKemahasiswaan = computed(() =>
  allUsers.value.filter((u) => matchRole(u.role, "kemahasiswaan")),
);
const allAdmin = computed(() =>
  allUsers.value.filter((u) => matchRole(u.role, "admin")),
);

// FILTERED USERS
const filteredMahasiswa = computed(() => {
  let filtered = allMahasiswa.value;
  if (searchUser.value && searchUser.value.trim()) {
    const q = searchUser.value.toLowerCase().trim();
    filtered = filtered.filter((u) => {
      const name = (u.full_name || u.username || "").toLowerCase();
      const nim = (u.nim_nip || "").toLowerCase();
      const email = (u.email || "").toLowerCase();
      return name.includes(q) || nim.includes(q) || email.includes(q);
    });
  }
  return filtered;
});

const filteredDosen = computed(() => {
  let filtered = allDosen.value;
  if (searchUser.value && searchUser.value.trim()) {
    const q = searchUser.value.toLowerCase().trim();
    filtered = filtered.filter((u) => {
      const name = (u.full_name || u.username || "").toLowerCase();
      const nip = (u.nim_nip || "").toLowerCase();
      const email = (u.email || "").toLowerCase();
      return name.includes(q) || nip.includes(q) || email.includes(q);
    });
  }
  return filtered;
});

const filteredAkademik = computed(() => {
  let filtered = allAkademik.value;
  if (searchUser.value && searchUser.value.trim()) {
    const q = searchUser.value.toLowerCase().trim();
    filtered = filtered.filter((u) => {
      const name = (u.full_name || u.username || "").toLowerCase();
      const email = (u.email || "").toLowerCase();
      return name.includes(q) || email.includes(q);
    });
  }
  return filtered;
});

const filteredKemahasiswaan = computed(() => {
  let filtered = allKemahasiswaan.value;
  if (searchUser.value && searchUser.value.trim()) {
    const q = searchUser.value.toLowerCase().trim();
    filtered = filtered.filter((u) => {
      const name = (u.full_name || u.username || "").toLowerCase();
      const email = (u.email || "").toLowerCase();
      return name.includes(q) || email.includes(q);
    });
  }
  return filtered;
});

const filteredAdmin = computed(() => {
  let filtered = allAdmin.value;
  if (searchUser.value && searchUser.value.trim()) {
    const q = searchUser.value.toLowerCase().trim();
    filtered = filtered.filter((u) => {
      const name = (u.full_name || u.username || "").toLowerCase();
      const email = (u.email || "").toLowerCase();
      return name.includes(q) || email.includes(q);
    });
  }
  return filtered;
});

// PLOTTING FILTERS
const filteredMahasiswaList = computed(() => {
  let list = allMahasiswaList.value;
  if (searchMahasiswa.value && searchMahasiswa.value.trim()) {
    const q = searchMahasiswa.value.toLowerCase().trim();
    list = list.filter((item) => {
      const name = (item.full_name || item.username || "").toLowerCase();
      const nim = (item.nim_nip || "").toLowerCase();
      return name.includes(q) || nim.includes(q);
    });
  }
  return list;
});

const filteredDPAList = computed(() => {
  let list = dpaList.value;
  if (searchDPA.value && searchDPA.value.trim()) {
    const q = searchDPA.value.toLowerCase().trim();
    list = list.filter((item) => {
      const name = (item.full_name || item.username || "").toLowerCase();
      const nip = (item.nim_nip || "").toLowerCase();
      return name.includes(q) || nip.includes(q);
    });
  }
  return list;
});

// TOTAL PAGES
const mahasiswaTotalPages = computed(
  () => Math.ceil(filteredMahasiswa.value.length / itemsPerPage.value) || 1,
);
const dosenTotalPages = computed(
  () => Math.ceil(filteredDosen.value.length / itemsPerPage.value) || 1,
);
const akademikTotalPages = computed(
  () => Math.ceil(filteredAkademik.value.length / itemsPerPage.value) || 1,
);
const kemahasiswaanTotalPages = computed(
  () => Math.ceil(filteredKemahasiswaan.value.length / itemsPerPage.value) || 1,
);
const adminTotalPages = computed(
  () => Math.ceil(filteredAdmin.value.length / itemsPerPage.value) || 1,
);

// PAGINATED USERS
const paginatedMahasiswa = computed(() =>
  filteredMahasiswa.value.slice(
    (mahasiswaPage.value - 1) * itemsPerPage.value,
    mahasiswaPage.value * itemsPerPage.value,
  ),
);
const paginatedDosen = computed(() =>
  filteredDosen.value.slice(
    (dosenPage.value - 1) * itemsPerPage.value,
    dosenPage.value * itemsPerPage.value,
  ),
);
const paginatedAkademik = computed(() =>
  filteredAkademik.value.slice(
    (akademikPage.value - 1) * itemsPerPage.value,
    akademikPage.value * itemsPerPage.value,
  ),
);
const paginatedKemahasiswaan = computed(() =>
  filteredKemahasiswaan.value.slice(
    (kemahasiswaanPage.value - 1) * itemsPerPage.value,
    kemahasiswaanPage.value * itemsPerPage.value,
  ),
);
const paginatedAdmin = computed(() =>
  filteredAdmin.value.slice(
    (adminPage.value - 1) * itemsPerPage.value,
    adminPage.value * itemsPerPage.value,
  ),
);

// LOGS
const filteredLogs = computed(() => {
  return recentLogs.value.filter((log) => {
    const status = String(log.status || "").toLowerCase();
    return status === "pending" || status === "approved_dpa";
  });
});

const logsTotalPages = computed(
  () => Math.ceil(filteredLogs.value.length / logsItemsPerPage.value) || 1,
);
const paginatedLogs = computed(() =>
  filteredLogs.value.slice(
    (logsPage.value - 1) * logsItemsPerPage.value,
    logsPage.value * logsItemsPerPage.value,
  ),
);

// KATEGORI
const kategoriTotalPages = computed(
  () => Math.ceil(listKategori.value.length / kategoriItemsPerPage.value) || 1,
);
const paginatedKategori = computed(() =>
  listKategori.value.slice(
    (kategoriPage.value - 1) * kategoriItemsPerPage.value,
    kategoriPage.value * kategoriItemsPerPage.value,
  ),
);

// PLOTTING
const filteredPlotting = computed(() => {
  let filtered = listPlotting.value;
  if (searchPlotting.value && searchPlotting.value.trim()) {
    const q = searchPlotting.value.toLowerCase().trim();
    filtered = filtered.filter((item) => {
      const name = (item.full_name || item.username || "").toLowerCase();
      const nim = (item.nim_nip || "").toLowerCase();
      const dpa = (item.dpa_name || "").toLowerCase();
      return name.includes(q) || nim.includes(q) || dpa.includes(q);
    });
  }
  return filtered;
});

const plottingTotalPages = computed(
  () =>
    Math.ceil(filteredPlotting.value.length / plottingItemsPerPage.value) || 1,
);
const paginatedPlotting = computed(() =>
  filteredPlotting.value.slice(
    (plottingPage.value - 1) * plottingItemsPerPage.value,
    plottingPage.value * plottingItemsPerPage.value,
  ),
);

// WATCH
let searchTimeout;
watch(searchUser, () => {
  if (searchTimeout) clearTimeout(searchTimeout);
  searchTimeout = setTimeout(() => resetPagination(), 300);
});

// PAGINATION METHODS
const prevPage = () => {
  if (logsPage.value > 1) logsPage.value--;
};
const nextPage = () => {
  if (logsPage.value < logsTotalPages.value) logsPage.value++;
};

// SELECT METHODS
const selectMahasiswa = (mhs) => {
  assignment.value.mahasiswa_id = mhs.id;
};

const selectDPA = (dpa) => {
  assignment.value.dpa_id = dpa.id;
};

const resetAssignment = () => {
  assignment.value = { mahasiswa_id: "", dpa_id: "" };
  searchMahasiswa.value = "";
  searchDPA.value = "";
};

// FETCH USER PROFILE
const fetchUserProfile = async () => {
  const token = localStorage.getItem("access_token");
  if (!token) return;

  try {
    const response = await api.get("api/users/me/", {
      headers: { Authorization: `Bearer ${token}` },
    });
    const user = response.data;
    userFullName.value = user.full_name || user.username || "Super Admin";
    userInitials.value =
      userFullName.value
        .split(" ")
        .map((n) => n[0])
        .join("")
        .toUpperCase()
        .slice(0, 2) || "SA";
  } catch (err) {
    console.error("Gagal memuat profil user:", err);
  }
};

// FETCH KEGIATAN
const fetchKegiatan = async () => {
  const token = localStorage.getItem("access_token");
  if (!token) return;

  try {
    const response = await api.get("api/kegiatan/", {
      headers: { Authorization: `Bearer ${token}` },
    });
    const data = response.data || [];
    kegiatanList.value = Array.isArray(data) ? data : data.results || [];
  } catch (err) {
    console.error("Gagal memuat data kegiatan:", err);
    kegiatanList.value = [];
  }
};

// FETCH PLOTTING DATA
const fetchPlottingData = async () => {
  const token = localStorage.getItem("access_token");
  if (!token) return;

  try {
    const [userRes, plottingRes] = await Promise.all([
      api
        .get("api/users-list-for-assigning/", {
          headers: { Authorization: `Bearer ${token}` },
        })
        .catch(() => ({
          data: { all_mahasiswa: [], dpa_list: [], unassigned_mhs: [] },
        })),
      api
        .get("api/plotting-list/", {
          headers: { Authorization: `Bearer ${token}` },
        })
        .catch(() => ({ data: [] })),
    ]);

    allMahasiswaList.value = userRes.data.all_mahasiswa || [];
    dpaList.value = userRes.data.dpa_list || [];
    unassignedMhs.value = userRes.data.unassigned_mhs || [];
    listPlotting.value = plottingRes.data || [];
  } catch (err) {
    console.error("Gagal memuat data plotting:", err);
  }
};

// FETCH ALL DATA
const fetchAllData = async () => {
  const token = localStorage.getItem("access_token");
  if (!token) {
    router.push("/login");
    return;
  }

  const config = { headers: { Authorization: `Bearer ${token}` } };

  try {
    const [dashRes, userRes, kategoriRes, plottingRes] = await Promise.all([
      api.get("api/superadmin-dashboard/", config),
      api.get("api/users-list-for-assigning/", config).catch(() => ({
        data: { all_mahasiswa: [], dpa_list: [], unassigned_mhs: [] },
      })),
      api.get("api/kategori/", config).catch(() => ({ data: [] })),
      api.get("api/plotting-list/", config).catch(() => ({ data: [] })),
    ]);

    stats.value = dashRes.data.stats || {
      total_mahasiswa: 0,
      total_pending: 0,
      total_valid: 0,
      total_tolak: 0,
    };
    recentLogs.value = dashRes.data.recent_logs || [];

    allMahasiswaList.value = userRes.data.all_mahasiswa || [];
    dpaList.value = userRes.data.dpa_list || [];
    unassignedMhs.value = userRes.data.unassigned_mhs || [];

    listKategori.value = kategoriRes.data || [];
    listPlotting.value = plottingRes.data || [];

    await fetchUsers();
    await fetchKegiatan();
    await fetchUserProfile();
  } catch (err) {
    console.error("Gagal memuat data:", err);
    if (err.response?.status === 401) {
      localStorage.clear();
      router.push("/login");
    }
  }
};

// FETCH USERS
const fetchUsers = async () => {
  loadingUsers.value = true;
  const token = localStorage.getItem("access_token");

  try {
    const response = await api.get("api/users/", {
      headers: { Authorization: `Bearer ${token}` },
    });

    let usersData = response.data || [];

    if (Array.isArray(usersData)) {
      allUsers.value = usersData;
    } else if (usersData.results && Array.isArray(usersData.results)) {
      allUsers.value = usersData.results;
    } else if (usersData.data && Array.isArray(usersData.data)) {
      allUsers.value = usersData.data;
    } else {
      allUsers.value = [];
    }
  } catch (err) {
    console.error("Gagal memuat data user:", err);
    allUsers.value = [];
    if (err.response?.status === 401) {
      localStorage.clear();
      router.push("/login");
    }
  } finally {
    loadingUsers.value = false;
  }
};

// KATEGORI CRUD
const submitKategori = async () => {
  kategoriError.value = "";

  if (
    !newKategori.value.bidang ||
    !newKategori.value.nama_kegiatan ||
    !newKategori.value.level ||
    !newKategori.value.bobot_poin
  ) {
    alert("Harap lengkapi semua field yang wajib diisi!");
    return;
  }

  if (isKategoriNameExists(newKategori.value.nama_kegiatan)) {
    kategoriError.value = `Nama kegiatan "${newKategori.value.nama_kegiatan}" sudah ada!`;
    return;
  }

  loadingKategori.value = true;
  const token = localStorage.getItem("access_token");

  try {
    await api.post("api/kategori/", newKategori.value, {
      headers: { Authorization: `Bearer ${token}` },
    });
    newKategori.value = {
      bidang: "",
      nama_kegiatan: "",
      partisipasi: "",
      level: "",
      sifat: "Pilihan",
      bobot_poin: 0,
    };
    alert("Kategori berhasil ditambahkan!");
    fetchAllData();
  } catch (err) {
    console.error(err);
    alert(
      "Gagal menyimpan kategori: " +
        (err.response?.data?.message || err.message),
    );
  } finally {
    loadingKategori.value = false;
  }
};

const editKategori = (kat) => {
  selectedKategori.value = { ...kat };
  showEditKategoriModal.value = true;
};

const saveEditKategori = async () => {
  if (
    isKategoriNameExists(
      selectedKategori.value.nama_kegiatan,
      selectedKategori.value.id,
    )
  ) {
    alert(`Nama kegiatan "${selectedKategori.value.nama_kegiatan}" sudah ada!`);
    return;
  }

  const token = localStorage.getItem("access_token");
  try {
    await api.patch(
      `api/kategori/${selectedKategori.value.id}/`,
      selectedKategori.value,
      { headers: { Authorization: `Bearer ${token}` } },
    );
    alert("Kategori berhasil diperbarui!");
    showEditKategoriModal.value = false;
    fetchAllData();
  } catch (err) {
    alert(
      "Gagal memperbarui kategori: " +
        (err.response?.data?.message || err.message),
    );
  }
};

const hapusKategori = async (id) => {
  if (!confirm("Yakin ingin menghapus kategori ini?")) return;
  const token = localStorage.getItem("access_token");
  try {
    await api.delete(`api/kategori/${id}/`, {
      headers: { Authorization: `Bearer ${token}` },
    });
    alert("Kategori berhasil dihapus!");
    fetchAllData();
  } catch (err) {
    alert(
      "Gagal menghapus kategori: " +
        (err.response?.data?.message || err.message),
    );
  }
};

// DPA ASSIGNMENT
const assignDPA = async () => {
  if (!assignment.value.mahasiswa_id || !assignment.value.dpa_id) {
    alert("Harap pilih Mahasiswa dan DPA terlebih dahulu!");
    return;
  }

  loadingAssign.value = true;
  const token = localStorage.getItem("access_token");

  try {
    await api.patch(
      `api/update-plotting/${assignment.value.mahasiswa_id}/`,
      { dpa_pembimbing: assignment.value.dpa_id },
      { headers: { Authorization: `Bearer ${token}` } },
    );

    assignment.value = { mahasiswa_id: "", dpa_id: "" };
    searchMahasiswa.value = "";
    searchDPA.value = "";
    showPlottingForm.value = false;
    alert("Plotting DPA berhasil diperbarui!");
    await fetchAllData();
    await fetchPlottingData();
  } catch (err) {
    console.error(err);
    alert(
      "Gagal menghubungkan DPA: " +
        (err.response?.data?.message || err.message),
    );
  } finally {
    loadingAssign.value = false;
  }
};

const hapusPlotting = async (mahasiswaId, namaMahasiswa) => {
  if (
    !confirm(
      `Yakin ingin menghapus plotting DPA untuk mahasiswa ${namaMahasiswa}?`,
    )
  )
    return;

  const token = localStorage.getItem("access_token");
  try {
    await api.patch(
      `api/update-plotting/${mahasiswaId}/`,
      { dpa_pembimbing: null },
      { headers: { Authorization: `Bearer ${token}` } },
    );
    alert("Plotting DPA berhasil dihapus!");
    await fetchAllData();
    await fetchPlottingData();
  } catch (err) {
    alert(
      "Gagal menghapus plotting: " +
        (err.response?.data?.message || err.message),
    );
  }
};

// USER MANAGEMENT CRUD
const openAddUserModal = () => {
  userForm.value = {
    id: null,
    username: "",
    password: "",
    full_name: "",
    email: "",
    nim_nip: "",
    no_telp: "",
    prodi: "",
    angkatan: "",
    nidn: "",
    jabatan: "",
    role: "mahasiswa",
  };
  showAddUserModal.value = true;
  showEditUserModal.value = false;
};

const editUser = (user) => {
  userForm.value = {
    id: user.id,
    username: user.username || "",
    password: "",
    full_name: user.full_name || "",
    email: user.email || "",
    nim_nip: user.nim_nip || "",
    no_telp: user.no_telp || "",
    prodi: user.prodi || "",
    angkatan: user.angkatan || "",
    nidn: user.nidn || "",
    jabatan: user.jabatan || "",
    role: user.role || "mahasiswa",
  };
  showEditUserModal.value = true;
  showAddUserModal.value = false;
};

const closeUserModal = () => {
  showAddUserModal.value = false;
  showEditUserModal.value = false;
  userForm.value = {
    id: null,
    username: "",
    password: "",
    full_name: "",
    email: "",
    nim_nip: "",
    no_telp: "",
    prodi: "",
    angkatan: "",
    nidn: "",
    jabatan: "",
    role: "mahasiswa",
  };
};

const createUser = async () => {
  if (!userForm.value.username || !userForm.value.password) {
    alert("Username dan password harus diisi!");
    return;
  }

  loadingUser.value = true;
  const token = localStorage.getItem("access_token");

  try {
    await api.post("api/users/", userForm.value, {
      headers: { Authorization: `Bearer ${token}` },
    });
    alert("User berhasil ditambahkan!");
    closeUserModal();
    await fetchUsers();
  } catch (err) {
    console.error(err);
    alert(
      "Gagal menambahkan user: " + (err.response?.data?.message || err.message),
    );
  } finally {
    loadingUser.value = false;
  }
};

const updateUser = async () => {
  loadingUser.value = true;
  const token = localStorage.getItem("access_token");

  try {
    const updateData = {
      username: userForm.value.username,
      full_name: userForm.value.full_name,
      email: userForm.value.email,
      nim_nip: userForm.value.nim_nip,
      no_telp: userForm.value.no_telp,
      prodi: userForm.value.prodi,
      angkatan: userForm.value.angkatan,
      nidn: userForm.value.nidn,
      jabatan: userForm.value.jabatan,
      role: userForm.value.role,
    };
    if (userForm.value.password && userForm.value.password.trim() !== "") {
      updateData.password = userForm.value.password;
    }
    await api.patch(`api/users/${userForm.value.id}/`, updateData, {
      headers: { Authorization: `Bearer ${token}` },
    });
    alert("User berhasil diperbarui!");
    closeUserModal();
    await fetchUsers();
  } catch (err) {
    console.error(err);
    alert(
      "Gagal memperbarui user: " + (err.response?.data?.message || err.message),
    );
  } finally {
    loadingUser.value = false;
  }
};

const hapusUser = async (id, nama) => {
  if (!confirm(`Yakin ingin menghapus user "${nama}"?`)) return;

  const token = localStorage.getItem("access_token");
  try {
    await api.delete(`api/users/${id}/`, {
      headers: { Authorization: `Bearer ${token}` },
    });
    alert("User berhasil dihapus!");
    await fetchUsers();
  } catch (err) {
    alert(
      "Gagal menghapus user: " + (err.response?.data?.message || err.message),
    );
  }
};

// UPDATE STATUS
const updateStatus = async (id, status) => {
  if (
    !confirm(
      `Apakah Anda yakin ingin ${status === "approved_final" ? "MENGESAHKAN" : "MENOLAK"} pengajuan ini?`,
    )
  )
    return;

  const token = localStorage.getItem("access_token");
  try {
    await api.patch(
      `api/kegiatan/${id}/`,
      { status: status },
      { headers: { Authorization: `Bearer ${token}` } },
    );
    alert(
      `Pengajuan berhasil ${status === "approved_final" ? "disahkan!" : "ditolak!"}`,
    );
    fetchAllData();
  } catch (err) {
    console.error(err);
    alert(
      "Gagal mengupdate status: " +
        (err.response?.data?.message || err.message),
    );
  }
};

// REJECT MODAL
const openRejectModal = (id) => {
  pendingRejectId.value = id;
  rejectReason.value = "";
  showRejectModal.value = true;
};

const closeRejectModal = () => {
  showRejectModal.value = false;
  pendingRejectId.value = null;
  rejectReason.value = "";
};

const confirmReject = async () => {
  if (!rejectReason.value.trim()) {
    alert("Alasan penolakan harus diisi!");
    return;
  }

  const token = localStorage.getItem("access_token");
  try {
    await api.patch(
      `api/kegiatan/${pendingRejectId.value}/`,
      {
        status: "rejected",
        komentar_dpa: rejectReason.value,
      },
      { headers: { Authorization: `Bearer ${token}` } },
    );
    alert("Pengajuan berhasil ditolak!");
    closeRejectModal();
    fetchAllData();
  } catch (err) {
    console.error(err);
    alert(
      "Gagal menolak pengajuan: " +
        (err.response?.data?.message || err.message),
    );
  }
};

// LOGOUT
const handleLogout = () => {
  if (confirm("Apakah Anda yakin ingin keluar?")) {
    localStorage.clear();
    router.push("/login");
  }
};

// LIFECYCLE
onMounted(() => {
  fetchAllData();
});
</script>

<style scoped>
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

@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
.animate-spin {
  animation: spin 1s linear infinite;
}

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

.modal-enter-active,
.modal-leave-active {
  transition:
    opacity 0.2s ease,
    transform 0.2s ease;
}
.modal-enter-from,
.modal-leave-to {
  opacity: 0;
  transform: scale(0.95);
}

.hover\:scale-105:hover {
  transform: scale(1.05);
}

.transition-all {
  transition-property: all;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 300ms;
}

input:focus,
select:focus,
textarea:focus {
  border-color: #6366f1;
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
}

button:disabled {
  cursor: not-allowed;
  opacity: 0.6;
}

thead th {
  position: sticky;
  top: 0;
  z-index: 10;
}
</style>
