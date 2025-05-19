import axios from 'axios'

const BASE_URL = import.meta.env.VITE_API_URL

const api = axios.create({
  baseURL: BASE_URL,
  headers: {
    'Content-Type': 'application/json'
  }
})

export const authAPI = {
  async register(userData) {
    const response = await api.post('auth/registration/', userData)
    return response.data
  },

  async login(credentials) {
    const response = await api.post('auth/login/', {
      username: credentials.username,
      password: credentials.password
    })
    return response.data
  },

  async getUserData() {
    const response = await api.get('auth/user/')
    return response.data
  }
}

// Интерцептор для добавления токена к запросам
api.interceptors.request.use(config => {
  const token = localStorage.getItem('token')
  if (token) {
    config.headers.Authorization = `Token ${token}`
  }
  return config
})

export default api 