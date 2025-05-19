<template>
  <header class="w-full flex flex-col sm:flex-row sm:justify-between items-center sm:items-center py-4 sm:py-6 px-2 sm:px-8  text-white ">
    <router-link 
      to="/" 
      class="text-xl sm:text-2xl font-semibold flex items-center gap-2 hover:text-purple-400 transition self-start sm:self-auto"
    >
      <i class="fas fa-chart-line text-purple-500"></i>
      invest.ru
    </router-link>
    <nav class="flex flex-col sm:flex-row gap-4 sm:gap-8 text-sm sm:text-base font-medium mt-2 sm:mt-0 w-full sm:w-auto items-start sm:items-center">
      <router-link to="/about" class="hover:text-purple-400 transition flex items-center gap-2">
        <i class="fas fa-info-circle"></i>
        О НАС
      </router-link>
      <router-link to="/contacts" class="hover:text-purple-400 transition flex items-center gap-2">
        <i class="fas fa-address-book"></i>
        КОНТАКТЫ
      </router-link>
      <template v-if="authStore.isAuthenticated">
        <router-link to="/profile" class="hover:text-purple-400 transition flex items-center gap-2">
          <i class="fas fa-user"></i>
          ПРОФИЛЬ
        </router-link>
        <button @click="handleLogout" class="hover:text-purple-400 transition flex items-center gap-2">
          <i class="fas fa-sign-out-alt"></i>
          ВЫЙТИ
        </button>
      </template>
      <template v-else>
        <button @click="authStore.showLoginModal = true" class="hover:text-purple-400 transition flex items-center gap-2">
          <i class="fas fa-sign-in-alt"></i>
          ВОЙТИ
        </button>
      </template>
    </nav>

    <!-- Модальные окна -->
    <AuthForm 
      v-if="authStore.showLoginModal" 
      v-model:isLogin="isLogin"
      @close="authStore.showLoginModal = false"
    />
  </header>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/authStore'
import AuthForm from '../auth/AuthForm.vue'

// const showLoginModal = ref(false)
const isLogin = ref(true)
const authStore = useAuthStore()

const handleLogout = () => {
  authStore.logout()
}
</script> 