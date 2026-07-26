<template>
  <div class="p-6 bg-gray-100 min-h-screen">
    <div class="max-w-6xl mx-auto space-y-6">
      
      <div class="bg-white rounded-xl shadow-sm p-6 border flex justify-between items-center">
        <div>
          <h1 class="text-2xl font-bold text-gray-800">Manajemen Pengguna STIE SBI</h1>
          <p class="text-sm text-gray-500">Kelola akun Mahasiswa, Dosen (DPA), dan Akademik.</p>
        </div>
        <button @click="router.push('/dashboard-superadmin')" class="bg-gray-100 px-4 py-2 rounded-lg text-blue-600 hover:bg-blue-50 text-sm font-bold transition">
           Kembali ke Dashboard
        </button>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
        
        <div class="lg:col-span-4 space-y-6">
          <div class="bg-white p-6 rounded-xl shadow-sm border">
            <h2 class="text-lg font-bold mb-4 text-gray-700">{{ isEdit ? 'Update Data User' : 'Tambah User Baru' }}</h2>
            <form @submit.prevent="saveUser" class="space-y-4">
              <div>
                <label class="text-[10px] font-bold text-gray-400 uppercase">Nama Lengkap</label>
                <input v-model="formData.full_name" type="text" class="w-full p-2 border rounded-lg text-sm mt-1 focus:ring-2 focus:ring-blue-500 outline-none" required />
              </div>
              <div class="grid grid-cols-2 gap-4">
                <div>
                  <label class="text-[10px] font-bold text-gray-400 uppercase">NIM / NIP</label>
                  <input v-model="formData.nim_nip" type="text" class="w-full p-2 border rounded-lg text-sm mt-1 focus:ring-2 focus:ring-blue-500 outline-none" required />
                </div>
                <div>
                  <label class="text-[10px] font-bold text-gray-400 uppercase">Role</label>
                  <select v-model="formData.role" class="w-full p-2 border rounded-lg text-sm mt-1 bg-white focus:ring-2 focus:ring-blue-500 outline-none">
                    <option value="mahasiswa">Mahasiswa</option>
                    <option value="dpa">DPA (Dosen)</option>
                    <option value="akademik">Akademik</option>
                  </select>
                </div>
              </div>

              <div v-if="!isEdit">
                <label class="text-[10px] font-bold text-gray-400 uppercase">Password Awal</label>
                <input v-model="formData.password" type="password" class="w-full p-2 border rounded-lg text-sm mt-1 focus:ring-2 focus:ring-blue-500 outline-none" required />
              </div>

              <div class="flex gap-2 pt-2">
                <button v-if="isEdit" type="button" @click="resetForm" class="flex-1 bg-gray-200 text-gray-700 py-2 rounded-lg text-sm font-bold hover:bg-gray-300 transition">
                  Batal
                </button>
                <button type="submit" class="flex-[2] bg-blue-600 text-white py-2 rounded-lg text-sm font-bold hover:bg-blue-700 shadow-md transition">
                  {{ isEdit ? 'Simpan Perubahan' : 'Daftarkan User' }}
                </button>
              </div>
            </form>
          </div>

          <div v-if="isEdit" class="bg-red-50 p-6 rounded-xl shadow-sm border border-red-100">
            <h2 class="text-sm font-bold text-red-700 mb-2">Pusat Keamanan</h2>
            <p class="text-[10px] text-red-500 mb-4 italic font-medium">*Gunakan fitur ini untuk mereset password user.</p>
            <div class="space-y-3">
              <input v-model="resetPasswordData" type="password" placeholder="Masukkan Password Baru" class="w-full p-2 border rounded-lg text-sm focus:ring-2 focus:ring-red-400 outline-none" />
              <button @click="handleResetPassword" class="w-full bg-red-600 text-white py-2 rounded-lg text-xs font-bold hover:bg-red-700 transition">Reset Password</button>
            </div>
          </div>
        </div>

        <div class="lg:col-span-8">
          <div class="bg-white rounded-xl shadow-sm border overflow-hidden">
            <div class="overflow-x-auto">
              <table class="w-full text-left">
                <thead class="bg-gray-50 text-[10px] text-gray-400 font-bold uppercase">
                  <tr>
                    <th class="p-4 border-b">Identitas</th>
                    <th class="p-4 border-b text-center">Role</th>
                    <th class="p-4 border-b text-center">Aksi</th>
                  </tr>
                </thead>
                <tbody class="text-sm">
                  <tr v-for="user in users" :key="user.id" class="hover:bg-gray-50 border-b transition">
                    <td class="p-4">
                      <div class="font-bold text-gray-800">{{ user.full_name }}</div>
                      <div class="text-[11px] text-gray-500 font-mono">{{ user.nim_nip }}</div>
                    </td>
                    <td class="p-4 text-center">
                      <span :class="{
                        'bg-blue-100 text-blue-700': user.role === 'mahasiswa',
                        'bg-purple-100 text-purple-700': user.role === 'dpa',
                        'bg-green-100 text-green-700': user.role === 'akademik'
                      }" class="px-2 py-1 rounded text-[10px] font-bold uppercase">
                        {{ user.role }}
                      </span>
                    </td>
                    <td class="p-4 text-center">
                      <div class="flex justify-center gap-3 font-bold">
                        <button @click="editUser(user)" class="text-blue-600 hover:text-blue-800 underline decoration-2 underline-offset-4">Edit</button>
                        <button @click="deleteAccount(user.id)" class="text-red-600 hover:text-red-800">Hapus</button>
                      </div>
                    </td>
                  </tr>
                  <tr v-if="users.length === 0">
                    <td colspan="3" class="p-8 text-center text-gray-400 italic">Data tidak ditemukan atau akses ditolak.</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import api from "../api/api";

const router = useRouter();
const users = ref([]);
const isEdit = ref(false);
const resetPasswordData = ref("");

const formData = ref({
  id: null, full_name: "", nim_nip: "", role: "mahasiswa", password: ""
});

// Fungsi utama mengambil data dengan Token
const fetchData = async () => {
  const token = localStorage.getItem('access_token');
  try {
    const res = await api.get("api/manage-users-list/", {
      headers: { Authorization: `Bearer ${token}` }
    });
    users.value = res.data;
  } catch (err) {
    console.error("Fetch Error:", err);
    // Jika Unauthorized (401), arahkan ke login atau berikan peringatan
    if (err.response?.status === 401) {
       alert("Sesi habis atau Anda bukan Admin. Silakan Login kembali.");
    }
  }
};

const saveUser = async () => {
  const token = localStorage.getItem('access_token');
  try {
    const payload = { 
      full_name: formData.value.full_name,
      nim_nip: formData.value.nim_nip,
      role: formData.value.role,
      username: formData.value.nim_nip 
    };

    if (isEdit.value) {
      await api.patch(`api/users/${formData.value.id}/`, payload, {
        headers: { Authorization: `Bearer ${token}` }
      });
      alert("Data berhasil diperbarui!");
    } else {
      payload.password = formData.value.password;
      await api.post("api/register/", payload); // Registrasi biasanya public
      alert("User berhasil didaftarkan!");
    }
    
    resetForm();
    fetchData();
  } catch (err) {
    const errorMsg = err.response?.data?.nim_nip ? "NIM/NIP sudah terdaftar!" : "Gagal menyimpan data.";
    alert(errorMsg);
  }
};

const handleResetPassword = async () => {
  const token = localStorage.getItem('access_token');
  if (!resetPasswordData.value || resetPasswordData.value.length < 4) {
    return alert("Password minimal 4 karakter!");
  }
  try {
    // Di Django, updating password biasanya butuh logic hashing di perform_update
    await api.patch(`api/users/${formData.value.id}/`, { 
      password: resetPasswordData.value 
    }, {
      headers: { Authorization: `Bearer ${token}` }
    });
    alert("Password Berhasil Direset!");
    resetPasswordData.value = "";
  } catch (err) {
    alert("Gagal mereset password. Pastikan akun memiliki izin.");
  }
};

const editUser = (user) => {
  isEdit.value = true;
  formData.value = { 
    id: user.id, 
    full_name: user.full_name, 
    nim_nip: user.nim_nip, 
    role: user.role, 
    password: "" 
  };
  window.scrollTo({ top: 0, behavior: 'smooth' });
};

const resetForm = () => {
  isEdit.value = false;
  resetPasswordData.value = "";
  formData.value = { id: null, full_name: "", nim_nip: "", role: "mahasiswa", password: "" };
};

const deleteAccount = async (id) => {
  const token = localStorage.getItem('access_token');
  if (confirm("Hapus akun secara permanen?")) {
    try {
      await api.delete(`api/users/${id}/`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      fetchData();
    } catch (err) {
      alert("Gagal menghapus akun.");
    }
  }
};

onMounted(fetchData);
</script>