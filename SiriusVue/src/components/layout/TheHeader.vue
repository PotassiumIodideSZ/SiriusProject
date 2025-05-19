<template>
  <header class="w-full flex justify-between items-center py-6 px-8 bg-[#0F0F0F] text-white border-b border-gray-800">
    <div class="text-2xl font-semibold flex items-center gap-2">
      <i class="fas fa-chart-line text-purple-500"></i>
      invest.ru
    </div>
    <nav class="flex gap-8 text-base font-medium">
      <a href="#" class="hover:text-purple-400 transition flex items-center gap-2">
        <i class="fas fa-info-circle"></i>
        О НАС
      </a>
      <button @click="showLoginModal = true" class="hover:text-purple-400 transition flex items-center gap-2">
        <i class="fas fa-sign-in-alt"></i>
        ВОЙТИ
      </button>
      <a href="#" class="hover:text-purple-400 transition flex items-center gap-2">
        <i class="fas fa-address-book"></i>
        КОНТАКТЫ
      </a>
    </nav>

    <!-- Модальные окна -->
    <AuthForm 
      v-if="showLoginModal" 
      :isLogin="true"
      @close="showLoginModal = false"
    />
  </header>
</template>

<script setup>
import { ref } from 'vue'
import AuthForm from '../auth/AuthForm.vue'

const showLoginModal = ref(false)
</script> 