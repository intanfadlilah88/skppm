// src/api/api.js
import axios from 'axios';

const api = axios.create({
  baseURL: 'https://kreditpoin.pythonanywhere.com',
});

// Request Interceptor (KODE ASLI ANDA - TIDAK DIRUBAH)
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token');
  
  if (token && !config.url.includes('register') && !config.url.includes('token')) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
}, (error) => {
  return Promise.reject(error);
});

// Response Interceptor (TAMBAHAN BARU - UNTUK HANDLE ERROR)
api.interceptors.response.use(
  (response) => response,
  (error) => {
    // Handle 401 Unauthorized
    if (error.response?.status === 401 && 
        !error.config.url.includes('register') && 
        !error.config.url.includes('token')) {
      
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
      localStorage.removeItem('user_role');
      localStorage.removeItem('user_name');
      localStorage.removeItem('user_nim_nip');
      
      window.location.href = '/login';
    }
    
    return Promise.reject(error);
  }
);

export default api;