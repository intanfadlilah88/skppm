<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-slate-900 via-blue-900 to-slate-900">
    <div class="bg-white/95 backdrop-blur-sm rounded-2xl shadow-2xl border border-blue-200 w-full max-w-sm">
      
      <!-- Logo dan Header -->
      <div class="text-center pt-6 pb-2">
        <!-- Logo Gambar -->
        <div class="flex justify-center mb-3">
          <img 
            src="/stie-sbilogo.jpg" 
            alt="STIE SBI Logo" 
            class="w-32 h-32 md:w-36 md:h-36 object-contain rounded-xl shadow-md bg-white p-2 mx-auto"
          />
        </div>
      </div>

      <!-- Judul Form -->
      <h2 class="text-lg font-bold text-center text-slate-700 mb-4">
        LOGIN SKPPM
      </h2>

      <!-- Form Login -->
      <form @submit.prevent="handleLogin" class="px-6 pb-6 space-y-4">
        <div>
          <label class="block text-xs font-semibold text-slate-700 mb-1">
            NIM / NIP
          </label>
          <div class="relative">
            <span class="absolute inset-y-0 left-0 pl-3 flex items-center text-slate-400 text-sm">
              👤
            </span>
            <input
              v-model="credentials.username"
              type="text"
              name="username"
              id="username"
              required
              placeholder="Masukkan NIM/NIP"
              class="w-full pl-9 pr-3 py-2 text-sm border-2 border-slate-200 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all text-slate-700 placeholder-slate-400"
              autocomplete="username"
            />
          </div>
        </div>

        <div>
          <label class="block text-xs font-semibold text-slate-700 mb-1">
            Password
          </label>
          <div class="relative">
            <span class="absolute inset-y-0 left-0 pl-3 flex items-center text-slate-400 text-sm">
              🔒
            </span>
            <input
              v-model="credentials.password"
              :type="showPassword ? 'text' : 'password'"
              name="password"
              id="password"
              required
              placeholder="••••••••"
              class="w-full pl-9 pr-9 py-2 text-sm border-2 border-slate-200 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all text-slate-700 placeholder-slate-400"
              autocomplete="current-password"
            />
            <button
              type="button"
              @click="showPassword = !showPassword"
              class="absolute inset-y-0 right-0 pr-3 flex items-center text-slate-400 hover:text-slate-600 transition text-sm"
            >
              {{ showPassword ? '🙈' : '👁️' }}
            </button>
          </div>
        </div>

        <button
          type="submit"
          :disabled="loading"
          class="w-full bg-gradient-to-r from-blue-700 to-blue-900 text-white py-2 rounded-lg font-bold text-sm hover:from-blue-800 hover:to-blue-950 transition-all disabled:from-gray-400 disabled:to-gray-500 shadow-md hover:shadow-lg mt-4"
        >
          {{ loading ? "Memproses..." : "Masuk ke Sistem" }}
        </button>

        <div class="text-center mt-4 pt-3 border-t border-slate-200">
          <p class="text-xs text-slate-500">
            Belum punya akun?
            <router-link
              to="/register"
              class="text-blue-600 font-semibold hover:text-blue-800 hover:underline transition"
            >
              Daftar di sini
            </router-link>
          </p>
        </div>

        <!-- Footer -->
        <div class="mt-3 text-center">
          <p class="text-[9px] text-slate-400">
            © 2024 STIE SBI Yogyakarta
          </p>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import api from "../api/api";

const router = useRouter();
const loading = ref(false);
const showPassword = ref(false);

const credentials = ref({
  username: "",
  password: "",
});

const handleLogin = async () => {
  // Validasi input
  if (!credentials.value.username.trim()) {
    alert("Mohon masukkan NIM/NIP!");
    return;
  }
  
  if (!credentials.value.password) {
    alert("Mohon masukkan password!");
    return;
  }
  
  loading.value = true;
  
  try {
    // 1. Ambil Token JWT
    const res = await api.post("api/token/", {
      username: credentials.value.username,
      password: credentials.value.password,
    });

    // 2. Simpan Token
    localStorage.setItem("access_token", res.data.access);
    localStorage.setItem("refresh_token", res.data.refresh);

    // 3. Set default Authorization header
    api.defaults.headers.common["Authorization"] = `Bearer ${res.data.access}`;

    // 4. Ambil data profil
    const userRes = await api.get("api/users/me/");
    const userRole = userRes.data.role;

    localStorage.setItem("user_role", userRole);
    localStorage.setItem("user_name", userRes.data.full_name || userRes.data.username);
    localStorage.setItem("user_nim_nip", userRes.data.nim_nip || credentials.value.username);
    
    // Simpan data tambahan
    if (userRes.data.email) {
      localStorage.setItem("user_email", userRes.data.email);
    }
    if (userRes.data.avatar) {
      localStorage.setItem("user_avatar", userRes.data.avatar);
    }

    // 5. Redirect sesuai Role
    if (userRole === "mahasiswa") {
      router.push("/dashboard-mahasiswa");
    } else if (userRole === "akademik") {
      router.push("/dashboard-akademik");
    } else if (userRole === "dpa") {
      router.push("/dashboard-dpa");
    } else if (userRole === "kemahasiswaan") {
      router.push("/dashboard-kemahasiswaan");
    } else if (userRole === "superadmin") {
      router.push("/dashboard-superadmin");
    } else {
      router.push("/");
    }
  } catch (err) {
    console.error("Login Error:", err.response?.data);
    
    // Handle berbagai jenis error
    let errorMsg = "Periksa NIM/NIP dan Password Anda.";
    
    if (err.response?.data?.detail) {
      errorMsg = err.response.data.detail;
    } else if (err.response?.data?.non_field_errors) {
      errorMsg = err.response.data.non_field_errors.join(", ");
    } else if (err.response?.data?.username) {
      errorMsg = `NIM/NIP: ${err.response.data.username.join(", ")}`;
    } else if (err.response?.data?.password) {
      errorMsg = `Password: ${err.response.data.password.join(", ")}`;
    }
    
    alert("Login Gagal!\n" + errorMsg);
    
    // Kosongkan password saja, username tetap biar tidak perlu mengetik ulang
    credentials.value.password = "";
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

/* Animasi loading */
button:disabled {
  cursor: not-allowed;
  opacity: 0.7;
}
</style>