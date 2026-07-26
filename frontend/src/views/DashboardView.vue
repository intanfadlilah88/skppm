<template>
  <div class="min-h-screen bg-white text-gray-800 font-sans">
    <nav
      class="flex justify-between items-center px-8 py-6 border-b border-gray-100 sticky top-0 bg-white/80 backdrop-blur-md z-50"
    >
      <div class="flex items-center gap-2">
        <div
          class="w-10 h-10 bg-blue-600 rounded-lg flex items-center justify-center text-white font-bold text-xl"
        >
          P
        </div>
        <span class="text-xl font-bold tracking-tight text-gray-900">
          Portal <span class="text-blue-600">SKPPM</span>
        </span>
      </div>
      <div class="flex gap-4">
        <router-link
          to="/login"
          class="px-5 py-2 text-gray-600 font-semibold hover:text-blue-600 transition"
        >
          Masuk
        </router-link>
        <router-link
          to="/register"
          class="px-5 py-2 bg-blue-600 text-white rounded-full font-semibold hover:bg-blue-700 transition shadow-md"
        >
          Daftar Sekarang
        </router-link>
      </div>
    </nav>

    <header
      class="px-8 py-20 max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-12 items-center"
    >
      <div>
        <span
          class="inline-block px-4 py-1.5 mb-6 text-sm font-bold tracking-wider text-blue-600 uppercase bg-blue-50 rounded-full"
        >
          Sistem Informasi Terpadu 2026
        </span>
        <h1
          class="text-5xl lg:text-6xl font-black text-gray-900 leading-tight mb-6"
        >
          Kelola Poin Prestasi <br />
          <span class="text-blue-600">Lebih Transparan.</span>
        </h1>
        <p class="text-lg text-gray-600 mb-8 leading-relaxed">
          Platform digital untuk mempermudah mahasiswa dalam pengajuan poin
          kegiatan, proses verifikasi oleh DPA, hingga rekapitulasi nilai akhir
          prestasi secara otomatis.
        </p>
        <div class="flex items-center gap-6">
          <router-link
            to="/login"
            class="group flex items-center gap-2 text-lg font-bold text-gray-900 hover:text-blue-600 transition"
          >
            Mulai Sekarang
            <span class="group-hover:translate-x-1 transition-transform"
              >→</span
            >
          </router-link>
        </div>
      </div>

      <div class="hidden lg:block relative">
        <div
          class="absolute -inset-4 bg-blue-100 rounded-full blur-3xl opacity-30"
        ></div>
      </div>
    </header>

    <section class="bg-gray-50 py-24 px-8">
      <div class="max-w-6xl mx-auto">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold text-gray-900 mb-4">
            Bagaimana Sistem Bekerja?
          </h2>
          <p class="text-gray-500 max-w-xl mx-auto">
            Tiga langkah sederhana untuk memastikan setiap prestasi Anda
            tercatat dengan valid di sistem akademik.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-12">
          <div class="text-center">
            <div
              class="w-16 h-16 bg-blue-600 text-white rounded-2xl flex items-center justify-center text-2xl font-bold mx-auto mb-6 shadow-lg shadow-blue-200"
            >
              1
            </div>
            <h3 class="text-xl font-bold mb-3">Login & Input</h3>
            <p class="text-gray-600 leading-relaxed">
              Mahasiswa masuk ke akun dan mengunggah dokumen sertifikat prestasi
              yang dimiliki.
            </p>
          </div>
          <div class="text-center">
            <div
              class="w-16 h-16 bg-white text-blue-600 border-2 border-blue-600 rounded-2xl flex items-center justify-center text-2xl font-bold mx-auto mb-6"
            >
              2
            </div>
            <h3 class="text-xl font-bold mb-3">Verifikasi DPA</h3>
            <p class="text-gray-600 leading-relaxed">
              Dosen Pembimbing memeriksa keaslian dokumen dan memberikan status
              persetujuan.
            </p>
          </div>
          <div class="text-center">
            <div
              class="w-16 h-16 bg-white text-blue-600 border-2 border-blue-600 rounded-2xl flex items-center justify-center text-2xl font-bold mx-auto mb-6"
            >
              3
            </div>
            <h3 class="text-xl font-bold mb-3">Poin Terakumulasi</h3>
            <p class="text-gray-600 leading-relaxed">
              Poin yang disetujui akan otomatis masuk ke database untuk syarat
              kelulusan.
            </p>
          </div>
        </div>
      </div>
    </section>

    <section class="py-24 px-8 max-w-7xl mx-auto">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div class="p-10 bg-indigo-900 rounded-3xl text-white">
          <h3 class="text-2xl font-bold mb-4">Untuk Mahasiswa</h3>
          <p class="mb-8 opacity-80 leading-relaxed">
            Unggah sertifikat organisasi, kompetisi, dan seminar Anda. Pantau
            target poin minimum dengan grafik yang mudah dipahami.
          </p>
          <router-link
            to="/register"
            class="inline-block px-6 py-3 bg-white text-indigo-900 rounded-xl font-bold hover:bg-indigo-50 transition"
          >
            Buat Akun Mahasiswa
          </router-link>
        </div>
        <div class="p-10 bg-blue-600 rounded-3xl text-white">
          <h3 class="text-2xl font-bold mb-4">Untuk DPA & Admin</h3>
          <p class="mb-8 opacity-80 leading-relaxed">
            Kelola daftar antrean verifikasi mahasiswa bimbingan Anda secara
            efisien. Berikan komentar revisi jika dokumen tidak sesuai.
          </p>
          <router-link
            to="/login"
            class="inline-block px-6 py-3 bg-indigo-900 text-white rounded-xl font-bold hover:bg-indigo-950 transition"
          >
            Masuk ke Panel Kontrol
          </router-link>
        </div>
      </div>
    </section>

    <footer
      class="border-t border-gray-100 py-12 px-8 text-center text-gray-400 text-sm"
    >
      <p>&copy; 2026 Sistem KPPM Terpadu. Seluruh Hak Cipta Dilindungi.</p>
    </footer>
  </div>
</template>

<script setup>
// Dashboard ini hanya berisi informasi statis dan navigasi
</script>

<style scoped>
::-webkit-scrollbar {
  width: 8px;
}
::-webkit-scrollbar-track {
  background: #f1f1f1;
}
::-webkit-scrollbar-thumb {
  background: #cbd5e1;
  border-radius: 4px;
}
</style>
