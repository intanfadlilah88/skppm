import { createRouter, createWebHistory } from 'vue-router';

// 1. Impor semua komponen yang digunakan
import AdminDashboardView from '../views/AdminDashboardView.vue';
import DashboardView from '../views/DashboardView.vue';
import PengajuanView from '../views/PengajuanView.vue';
import LoginView from '../views/LoginView.vue';
import RegisterView from '../views/RegisterView.vue';
import DpaView from '../views/DpaView.vue';
import AkademikView from '../views/AkademikView.vue';
import MahasiswaView from '../views/MahasiswaView.vue';
import ManageUsers from '../views/ManageUsers.vue';

const routes = [
  { 
  path: '/super-admin', 
  name:'SuperAdmin',
  component: AdminDashboardView,
  beforeEnter: (to, from, next) => {
    const role = localStorage.getItem('role');
    // Hanya izinkan jika role-nya superadmin
    if (role === 'superadmin') {
      next();
    } else {
      next('/login');
    }
  }
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterView
  },
  
  { 
    path: '/', 
    name: 'Dashboard', 
    component: DashboardView 
  },
  { 
    path: '/pengajuan', 
    name: 'Pengajuan', 
    component: PengajuanView 
  },
 
  // Rute untuk berbagai peran (role)
  {
    path: '/dashboard-dpa',
    name: 'Dpa',
    component: DpaView
  },
  {
    path: '/dashboard-superadmin',
    name: 'Admin',
    component: AdminDashboardView
  },
  {
    path: '/dashboard-akademik',
    name: 'Akademik',
    component: AkademikView
  },
  {
    path: '/dashboard-mahasiswa',
    name: 'Mahasiswa',
    component: MahasiswaView
  },
   {
    path: '/manage-users',
    name: 'ManageUsers',
    component: ManageUsers,
     meta: { requiresAuth: true, role: 'superadmin' }
  },
  {
  path: '/dashboard-kemahasiswaan',
  name: 'DashboardKemahasiswaan',
  component: () => import('../views/kemahasiswaanView.vue'),
  meta: { requiresAuth: true, role: 'kemahasiswaan' }
}
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Navigation Guard (Proteksi Rute)
router.beforeEach((to, from, next) => {
  const role = localStorage.getItem('user_role');
  
  if (to.meta.role && to.meta.role !== role) {
    // Jika role tidak sesuai, paksa kembali ke dashboard yang benar
    if (role === 'mahasiswa') next('/dashboard-mahasiswa');
    else if (role === 'akademik') next('/dashboard-akademik');
    else if (role === 'dpa') next('/dashboard-dpa');
    else if (role === 'kemahsaiswaan') next('/dashboard-kemahasiswaan');
    else if (role === 'admin') next('/dashboard-superadmin');
    else next('/login');
  } else {
    next();
  }
});

export default router;