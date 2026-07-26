<template>
  <div class="min-h-screen flex items-center justify-center py-8 px-4">
    <div class="bg-white/95 backdrop-blur-sm rounded-2xl shadow-2xl border border-blue-200 w-full max-w-lg">
      
      <!-- Logo dan Header - Lebih Besar -->
      <div class="text-center pt-8 pb-4">
        <div class="flex justify-center mb-3">
          <img 
            src="/stie-sbilogo.jpg" 
            alt="STIE SBI Logo" 
            class="w-32 h-32 md:w-36 md:h-36 object-contain rounded-xl shadow-md bg-white p-2"
          />
        </div>
        <h1 class="text-xl font-bold text-slate-800">STIE SBI</h1>
        <p class="text-xs text-blue-600 font-semibold">YOGYAKARTA</p>
        <div class="w-12 h-0.5 bg-gradient-to-r from-blue-500 to-blue-700 mx-auto mt-2 rounded-full"></div>
      </div>

      <h2 class="text-lg font-bold text-center text-slate-700 mb-4">
        Daftar Akun SKPPM
      </h2>
      
      <form @submit.prevent="handleRegister" class="px-6 pb-8">
        <!-- Role Selection -->
        <div class="mb-4">
          <label class="block text-xs font-semibold text-slate-700 mb-2">Daftar Sebagai</label>
          <div class="grid grid-cols-5 gap-2">
            <button 
              type="button"
              @click="form.role = 'mahasiswa'"
              :class="['py-2 px-2 rounded-lg font-semibold text-xs transition-all', 
                       form.role === 'mahasiswa' ? 'bg-blue-600 text-white shadow-md' : 'bg-slate-100 text-slate-600 hover:bg-slate-200']">
              🎓 Mhs
            </button>
            <button 
              type="button"
              @click="form.role = 'dpa'"
              :class="['py-2 px-2 rounded-lg font-semibold text-xs transition-all', 
                       form.role === 'dpa' ? 'bg-blue-600 text-white shadow-md' : 'bg-slate-100 text-slate-600 hover:bg-slate-200']">
              📖 DPA
            </button>
            <button 
              type="button"
              @click="form.role = 'akademik'"
              :class="['py-2 px-2 rounded-lg font-semibold text-xs transition-all', 
                       form.role === 'akademik' ? 'bg-blue-600 text-white shadow-md' : 'bg-slate-100 text-slate-600 hover:bg-slate-200']">
              📚 Akad
            </button>
            <button 
              type="button"
              @click="form.role = 'kemahasiswaan'"
              :class="['py-2 px-2 rounded-lg font-semibold text-xs transition-all', 
                       form.role === 'kemahasiswaan' ? 'bg-blue-600 text-white shadow-md' : 'bg-slate-100 text-slate-600 hover:bg-slate-200']">
              🏢 Kmhs
            </button>
            <button 
              type="button"
              @click="form.role = 'superadmin'"
              :class="['py-2 px-2 rounded-lg font-semibold text-xs transition-all', 
                       form.role === 'superadmin' ? 'bg-blue-600 text-white shadow-md' : 'bg-slate-100 text-slate-600 hover:bg-slate-200']">
              👑 Admin
            </button>
          </div>
        </div>

        <!-- Form Fields - Compact -->
        <div class="space-y-3">
          <div>
            <label class="block text-xs font-semibold text-slate-700 mb-1">Nama Lengkap</label>
            <input v-model="form.full_name" type="text" placeholder="Masukkan nama lengkap" 
                   class="w-full px-3 py-2 text-sm border-2 border-slate-200 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all" required>
          </div>
          
          <div class="grid grid-cols-2 gap-3">
            <div>
              <label class="block text-xs font-semibold text-slate-700 mb-1">
                {{ form.role === 'mahasiswa' ? 'NIM' : 'NIP' }}
              </label>
              <input v-model="form.nim_nip" type="text" :placeholder="form.role === 'mahasiswa' ? 'NIM' : 'NIP'"
                     class="w-full px-3 py-2 text-sm border-2 border-slate-200 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all" required>
            </div>

            <div>
              <label class="block text-xs font-semibold text-slate-700 mb-1">Email</label>
              <input v-model="form.email" type="email" placeholder="Email"
                     class="w-full px-3 py-2 text-sm border-2 border-slate-200 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all" required>
            </div>
          </div>

          <div class="grid grid-cols-2 gap-3">
            <div>
              <label class="block text-xs font-semibold text-slate-700 mb-1">No. WhatsApp</label>
              <input v-model="form.no_telp" type="tel" placeholder="08123456789"
                     class="w-full px-3 py-2 text-sm border-2 border-slate-200 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all" required>
            </div>

            <!-- Program Studi untuk Mahasiswa, DPA, Akademik, Kemahasiswaan -->
            <div v-if="form.role === 'mahasiswa' || form.role === 'dpa' || form.role === 'akademik' || form.role === 'kemahasiswaan'">
              <label class="block text-xs font-semibold text-slate-700 mb-1">Program Studi</label>
              <select v-model="form.prodi" class="w-full px-3 py-2 text-sm border-2 border-slate-200 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none" required>
                <option value="" disabled>Prodi</option>
                <option value="Manajemen">Manajemen</option>
                <option value="Akuntansi">Akuntansi</option>
              </select>
            </div>

            <div v-if="form.role === 'superadmin'" class="invisible"></div>
          </div>

          <!-- Mahasiswa Additional Fields -->
          <div v-if="form.role === 'mahasiswa'" class="grid grid-cols-2 gap-3">
            <div>
              <label class="block text-xs font-semibold text-slate-700 mb-1">Jenis Kelamin</label>
              <select v-model="form.jenis_kelamin" class="w-full px-3 py-2 text-sm border-2 border-slate-200 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none" required>
                <option value="" disabled>Pilih</option>
                <option value="L">Laki-laki</option>
                <option value="P">Perempuan</option>
              </select>
            </div>
            <div>
              <label class="block text-xs font-semibold text-slate-700 mb-1">Angkatan</label>
              <input v-model="form.angkatan" type="text" placeholder="2024"
                     class="w-full px-3 py-2 text-sm border-2 border-slate-200 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none" required>
            </div>
          </div>

          <!-- DPA, Akademik, & Kemahasiswaan Additional Fields -->
          <div v-if="form.role === 'dpa' || form.role === 'akademik' || form.role === 'kemahasiswaan'" class="grid grid-cols-2 gap-3">
            <div>
              <label class="block text-xs font-semibold text-slate-700 mb-1">NIDN</label>
              <input v-model="form.nidn" type="text" placeholder="NIDN"
                     class="w-full px-3 py-2 text-sm border-2 border-slate-200 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none">
            </div>
            <div>
              <label class="block text-xs font-semibold text-slate-700 mb-1">Jabatan</label>
              <input v-model="form.jabatan" type="text" placeholder="Jabatan"
                     class="w-full px-3 py-2 text-sm border-2 border-slate-200 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none">
            </div>
          </div>

          <!-- Password Field -->
          <div>
            <label class="block text-xs font-semibold text-slate-700 mb-1">Password</label>
            <div class="relative">
              <input v-model="form.password" :type="showPassword ? 'text' : 'password'" placeholder="Minimal 8 karakter"
                     class="w-full px-3 py-2 text-sm border-2 border-slate-200 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all pr-8" required>
              <button type="button" @click="showPassword = !showPassword"
                      class="absolute inset-y-0 right-0 pr-3 flex items-center text-slate-400 hover:text-slate-600 text-xs">
                {{ showPassword ? '🙈' : '👁️' }}
              </button>
            </div>
          </div>
        </div>

        <button type="submit" :disabled="loading"
                class="w-full bg-gradient-to-r from-blue-700 to-blue-900 text-white py-2.5 rounded-xl font-bold text-sm hover:from-blue-800 hover:to-blue-950 transition-all disabled:from-gray-400 disabled:to-gray-500 shadow-md hover:shadow-lg mt-5">
          {{ loading ? "Memproses..." : "Daftar Sekarang" }}
        </button>

        <div class="text-center mt-4 pt-3 border-t border-slate-200">
          <p class="text-xs text-slate-500">
            Sudah punya akun?
            <router-link to="/login" class="text-blue-600 font-semibold hover:text-blue-800 hover:underline transition">
              Login di sini
            </router-link>
          </p>
        </div>

        <!-- Footer -->
        <div class="mt-4 text-center">
          <p class="text-[9px] text-slate-400">
            © 2024 STIE SBI Yogyakarta
          </p>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import api from '../api/api'; 
import { useRouter } from 'vue-router';

const router = useRouter();
const loading = ref(false);
const showPassword = ref(false);

const form = ref({ 
  full_name: '', 
  nim_nip: '', 
  role: 'mahasiswa', 
  email: '',
  no_telp: '',
  prodi: '',
  jenis_kelamin: '',
  angkatan: '',
  nidn: '',
  jabatan: '',
  password: '' 
});

const handleRegister = async () => {
  loading.value = true;
  try {
    const payload = {
      username: form.value.nim_nip,
      password: form.value.password,
      role: form.value.role,
      nim_nip: form.value.nim_nip,
      full_name: form.value.full_name,
      email: form.value.email,
      no_telp: form.value.no_telp,
      prodi: form.value.prodi,
      jenis_kelamin: form.value.jenis_kelamin,
      angkatan: form.value.angkatan,
      nidn: form.value.nidn,
      jabatan: form.value.jabatan
    };
    
    // Clean payload berdasarkan role
    if (form.value.role === 'mahasiswa') {
      delete payload.nidn;
      delete payload.jabatan;
    } else if (form.value.role === 'dpa' || form.value.role === 'akademik' || form.value.role === 'kemahasiswaan') {
      delete payload.angkatan;
      delete payload.jenis_kelamin;
    } else if (form.value.role === 'superadmin') {
      delete payload.angkatan;
      delete payload.jenis_kelamin;
      delete payload.prodi;
      delete payload.nidn;
      delete payload.jabatan;
    }
    
    await api.post('api/register/', payload);
    
    alert('Registrasi berhasil! Silakan login.');
    router.push('/login');
  } catch (err) {
    console.error(err.response?.data);
    let errorMsg = 'Gagal mendaftar. ';
    if (err.response?.data?.nim_nip) {
      errorMsg += err.response.data.nim_nip.join(', ');
    } else if (err.response?.data?.username) {
      errorMsg += err.response.data.username.join(', ');
    } else if (err.response?.data?.detail) {
      errorMsg += err.response.data.detail;
    } else if (typeof err.response?.data === 'object') {
      errorMsg += JSON.stringify(err.response.data);
    }
    alert(errorMsg);
  } finally {
    loading.value = false;
  }
};
</script>

<style scoped>
.min-h-screen {
  background: linear-gradient(135deg, #0a0f1a 0%, #0f2b3d 50%, #0a1628 100%);
  position: relative;
}

/* Efek grid pattern */
.min-h-screen::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: 
    linear-gradient(rgba(59, 130, 246, 0.05) 1px, transparent 1px),
    linear-gradient(90deg, rgba(59, 130, 246, 0.05) 1px, transparent 1px);
  background-size: 40px 40px;
  pointer-events: none;
}

/* Efek bintang/glow */
.min-h-screen::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: radial-gradient(circle at 20% 30%, rgba(59, 130, 246, 0.08) 0%, transparent 60%);
  pointer-events: none;
}
</style>