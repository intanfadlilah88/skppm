import { createApp } from 'vue'
import App from './App.vue'
import router from './router' // Mengimpor konfigurasi router
import './style.css'         // CSS Tailwind

const app = createApp(App)

// Memberitahu aplikasi untuk menggunakan router
app.use(router) 

app.mount('#app')