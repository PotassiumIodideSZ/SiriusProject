import { defineStore } from 'pinia'
import { authAPI } from '@/services/api'
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

export const useAuthStore = defineStore('auth', () => {
  const router = useRouter()
  const token = ref(localStorage.getItem('token') || null)
  const user = ref(null)
  const error = ref(null)
  const showLoginModal = ref(false)

  const isAuthenticated = computed(() => !!token.value)

  const formatError = (err) => {
    if (err.response?.data?.non_field_errors) {
      return err.response.data.non_field_errors[0]
    }
    return err.response?.data || 'Произошла ошибка'
  }

  const setToken = (newToken) => {
    token.value = newToken
    localStorage.setItem('token', newToken)
  }

  const clearAuth = () => {
    token.value = null
    user.value = null
    localStorage.removeItem('token')
  }

  const fetchUserData = async () => {
    try {
      const userData = await authAPI.getUserData()
      user.value = userData
    } catch (err) {
      console.error('Ошибка при получении данных пользователя:', err)
      clearAuth()
    }
  }

  const register = async (userData) => {
    try {
      error.value = null
      const response = await authAPI.register({
        username: userData.username,
        email: userData.email,
        first_name: userData.firstName,
        last_name: userData.lastName,
        password1: userData.password,
        password2: userData.password
      })
      setToken(response.key)
      await fetchUserData()
      router.push('/profile')
      return true
    } catch (err) {
      error.value = formatError(err)
      return false
    }
  }

  const login = async (credentials) => {
    try {
      error.value = null
      const response = await authAPI.login(credentials)
      setToken(response.key)
      await fetchUserData()
      router.push('/profile')
      return true
    } catch (err) {
      error.value = formatError(err)
      return false
    }
  }

  const logout = () => {
    clearAuth()
    router.push('/')
  }

  // Загружаем данные пользователя при инициализации, если есть токен
  if (token.value) {
    fetchUserData()
  }

  return {
    token,
    user,
    error,
    isAuthenticated,
    showLoginModal,
    register,
    login,
    logout,
    fetchUserData
  }
}) 