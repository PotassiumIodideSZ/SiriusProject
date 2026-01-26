<template>
  <div class="min-h-screen bg-[#0F0F0F] flex flex-col relative overflow-hidden">
    <TheHeader class="relative z-10" />
    <main class="flex-1 relative z-10">
      <router-view />
    </main>
    <TheFooter class="relative z-10" />
    <BackgroundCircles />
    
    <!-- Auth Modal - rendered at root level to avoid z-index stacking context issues -->
    <AuthForm 
      v-if="authStore.showLoginModal" 
      v-model:isLogin="isLogin"
      @close="authStore.showLoginModal = false"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import TheHeader from '@/layout/components/TheHeader.vue'
import TheFooter from '@/layout/components/TheFooter.vue'
import BackgroundCircles from '@/shared/components/BackgroundCircles.vue'
import { AuthForm } from '@/features/auth'
import { useAuthStore } from '@/features/auth/stores/authStore'

const isLogin = ref(true)
const authStore = useAuthStore()
</script>