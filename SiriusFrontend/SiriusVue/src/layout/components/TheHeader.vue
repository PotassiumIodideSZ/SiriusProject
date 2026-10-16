<template>
  <header class="w-full sticky top-0 z-40 bg-paper-100/90 backdrop-blur-md border-b border-ink-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
      <!-- Logo & Brand -->
      <router-link 
        to="/" 
        class="flex items-center gap-3.5 group transition-transform active:scale-[0.98]"
      >
        <img 
          src="/logo.png" 
          alt="Psy Otkliq" 
          class="w-16 h-16 object-contain group-hover:scale-105 transition-transform drop-shadow-sm flex-shrink-0" 
        />
        <div class="flex flex-col">
          <div class="flex items-center gap-2">
            <span class="font-serif font-bold text-base text-ink-950 tracking-tight group-hover:text-academic-amber transition-colors">
              Psy Otkliq
            </span>
            <span class="px-1.5 py-0.5 rounded text-[10px] font-mono font-medium bg-amber-50 text-academic-amber border border-amber-200/60 uppercase tracking-wider">
              Data Lab
            </span>
          </div>
          <span class="text-[11px] text-ink-500 font-mono tracking-tight -mt-0.5">
            Анализ данных и когнитивное моделирование
          </span>
        </div>
      </router-link>

      <!-- Desktop Navigation Links -->
      <nav class="hidden md:flex items-center gap-1 sm:gap-2">
        <router-link 
          to="/" 
          class="px-3.5 py-1.5 rounded-lg text-sm font-medium text-ink-600 hover:text-ink-950 hover:bg-ink-100/70 transition-all"
          active-class="text-academic-amber bg-amber-50 border border-amber-200/60 font-semibold"
        >
          Главная
        </router-link>
        <router-link 
          to="/about" 
          class="px-3.5 py-1.5 rounded-lg text-sm font-medium text-ink-600 hover:text-ink-950 hover:bg-ink-100/70 transition-all"
          active-class="text-academic-amber bg-amber-50 border border-amber-200/60 font-semibold"
        >
          О проекте
        </router-link>
        <router-link 
          to="/contacts" 
          class="px-3.5 py-1.5 rounded-lg text-sm font-medium text-ink-600 hover:text-ink-950 hover:bg-ink-100/70 transition-all"
          active-class="text-academic-amber bg-amber-50 border border-amber-200/60 font-semibold"
        >
          Методология
        </router-link>
      </nav>

      <!-- Auth Actions -->
      <div class="flex items-center gap-3">
        <template v-if="authStore.isAuthenticated">
          <router-link 
            to="/survey"
            class="hidden sm:inline-flex items-center gap-2 px-3.5 py-1.5 rounded-lg text-xs font-mono font-medium text-ink-700 hover:text-ink-950 bg-white hover:bg-ink-50 border border-ink-200 shadow-sm transition-all"
          >
            <i class="fas fa-pen-nib text-academic-amber"></i>
            Тестирование
          </router-link>
          <router-link 
            to="/profile" 
            class="inline-flex items-center gap-2 px-3 py-1.5 rounded-lg text-sm font-medium text-ink-700 hover:text-ink-950 hover:bg-ink-100/80 border border-ink-200 transition-all"
            active-class="border-amber-400 bg-amber-50 text-academic-amber font-semibold"
          >
            <i class="fas fa-user-circle text-academic-amber"></i>
            <span class="hidden sm:inline">Кабинет</span>
          </router-link>
          <button 
            @click="handleLogout" 
            class="px-2.5 py-1.5 rounded-lg text-xs font-mono text-ink-400 hover:text-academic-crimson hover:bg-red-50 transition-colors"
            title="Выйти"
          >
            <i class="fas fa-sign-out-alt"></i>
          </button>
        </template>
        <template v-else>
          <button 
            @click="authStore.showLoginModal = true" 
            class="px-4 py-2 rounded-xl text-sm font-medium text-ink-700 hover:text-ink-950 hover:bg-ink-100/80 transition-all"
          >
            Вход
          </button>
          <button 
            @click="authStore.showLoginModal = true" 
            class="px-4 py-2 rounded-xl text-sm font-medium bg-ink-950 hover:bg-ink-800 text-amber-300 shadow-sm hover:shadow transition-all active:scale-[0.98]"
          >
            Начать тест
          </button>
        </template>
      </div>
    </div>
  </header>
</template>

<script setup>
import { useAuthStore } from '@/features/auth/stores/authStore'

const authStore = useAuthStore()

const handleLogout = () => {
  authStore.logout()
}
</script>
