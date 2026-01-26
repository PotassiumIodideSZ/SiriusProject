import api from '@/core/api/axiosInstance'
import { API_ENDPOINTS } from '@/core/config/constants'

export const authAPI = {
  async register(userData) {
    const response = await api.post(API_ENDPOINTS.AUTH.REGISTER, {
      username: userData.username,
      email: userData.email,
      first_name: userData.firstName,
      last_name: userData.lastName,
      password1: userData.password,
      password2: userData.password
    })
    return response.data
  },

  async login(credentials) {
    const response = await api.post(API_ENDPOINTS.AUTH.LOGIN, {
      username: credentials.username,
      password: credentials.password
    })
    return response.data
  },

  async getUserData() {
    const response = await api.get(API_ENDPOINTS.AUTH.USER)
    return response.data
  },

  async logout() {
    const response = await api.post(API_ENDPOINTS.AUTH.LOGOUT)
    return response.data
  }
}
