import { computed } from 'vue'
import { useAuthStore } from '../stores/authStore'

export function useAuth() {
  const authStore = useAuthStore()
  
  const user = computed(() => authStore.user)
  const isAuthenticated = computed(() => authStore.isAuthenticated)
  const error = computed(() => authStore.error)
  const showLoginModal = computed({
    get: () => authStore.showLoginModal,
    set: (value) => { authStore.showLoginModal = value }
  })
  
  const login = async (credentials) => {
    return await authStore.login(credentials)
  }
  
  const register = async (userData) => {
    return await authStore.register(userData)
  }
  
  const logout = () => {
    authStore.logout()
  }
  
  const fetchUserData = async () => {
    await authStore.fetchUserData()
  }
  
  return {
    user,
    isAuthenticated,
    error,
    showLoginModal,
    login,
    register,
    logout,
    fetchUserData
  }
}
