<template>
  <BaseModal @close="$emit('close')">
    <div class="relative space-y-6">
      <!-- Close Button -->
      <button 
        @click="$emit('close')" 
        class="absolute -right-2 -top-2 w-8 h-8 rounded-lg bg-ink-100 hover:bg-ink-200 text-ink-500 hover:text-ink-900 flex items-center justify-center transition-colors"
      >
        <i class="fas fa-times text-sm"></i>
      </button>

      <!-- Header Title -->
      <div class="text-center space-y-1">
        <h2 class="text-2xl font-serif font-bold text-ink-950 tracking-tight">
          {{ isLogin ? 'Авторизация в системе' : 'Создание профиля' }}
        </h2>
        <p class="text-xs font-mono text-ink-500">
          {{ isLogin ? 'Войдите для доступа к истории тестов' : 'Регистрация в исследовательской платформе' }}
        </p>
      </div>

      <!-- Form -->
      <form @submit.prevent="handleSubmit" class="space-y-4">
        <!-- Username -->
        <div class="space-y-1.5">
          <label class="block text-xs font-mono font-medium text-ink-700">Имя пользователя / Логин</label>
          <input 
            type="text" 
            v-model="form.username"
            autocomplete="username"
            required
            class="w-full px-4 py-2.5 rounded-xl bg-paper-50 border border-ink-200 focus:border-amber-600 focus:bg-white focus:outline-none text-ink-900 text-sm placeholder:text-ink-400 font-mono transition-all"
            placeholder="например, admin или ivan"
          />
        </div>

        <!-- Registration Fields -->
        <template v-if="!isLogin">
          <div class="grid grid-cols-2 gap-3">
            <div class="space-y-1.5">
              <label class="block text-xs font-mono font-medium text-ink-700">Имя</label>
              <input 
                type="text" 
                v-model="form.firstName"
                autocomplete="given-name"
                required
                class="w-full px-3 py-2.5 rounded-xl bg-paper-50 border border-ink-200 focus:border-amber-600 focus:bg-white focus:outline-none text-ink-900 text-sm placeholder:text-ink-400 transition-all"
                placeholder="Иван"
              />
            </div>
            <div class="space-y-1.5">
              <label class="block text-xs font-mono font-medium text-ink-700">Фамилия</label>
              <input 
                type="text" 
                v-model="form.lastName"
                autocomplete="family-name"
                required
                class="w-full px-3 py-2.5 rounded-xl bg-paper-50 border border-ink-200 focus:border-amber-600 focus:bg-white focus:outline-none text-ink-900 text-sm placeholder:text-ink-400 transition-all"
                placeholder="Иванов"
              />
            </div>
          </div>

          <div class="space-y-1.5">
            <label class="block text-xs font-mono font-medium text-ink-700">Email</label>
            <input 
              type="email" 
              v-model="form.email"
              autocomplete="email"
              required
              class="w-full px-4 py-2.5 rounded-xl bg-paper-50 border border-ink-200 focus:border-amber-600 focus:bg-white focus:outline-none text-ink-900 text-sm placeholder:text-ink-400 font-mono transition-all"
              placeholder="user@example.com"
            />
          </div>
        </template>

        <!-- Password -->
        <div class="space-y-1.5">
          <label class="block text-xs font-mono font-medium text-ink-700">Пароль</label>
          <div class="relative">
            <input 
              :type="showPassword ? 'text' : 'password'"
              v-model="form.password"
              :autocomplete="isLogin ? 'current-password' : 'new-password'"
              required
              class="w-full px-4 py-2.5 rounded-xl bg-paper-50 border border-ink-200 focus:border-amber-600 focus:bg-white focus:outline-none text-ink-900 text-sm placeholder:text-ink-400 font-mono transition-all pr-10"
              placeholder="••••••••"
            />
            <button 
              type="button"
              @click="showPassword = !showPassword"
              class="absolute right-3 top-1/2 -translate-y-1/2 text-ink-400 hover:text-ink-800 transition-colors"
            >
              <i :class="showPassword ? 'fas fa-eye-slash' : 'fas fa-eye'" class="text-xs"></i>
            </button>
          </div>
        </div>

        <!-- Confirm Password -->
        <div v-if="!isLogin" class="space-y-1.5">
          <label class="block text-xs font-mono font-medium text-ink-700">Подтвердите пароль</label>
          <div class="relative">
            <input 
              :type="showConfirmPassword ? 'text' : 'password'"
              v-model="form.confirmPassword"
              autocomplete="new-password"
              required
              class="w-full px-4 py-2.5 rounded-xl bg-paper-50 border border-ink-200 focus:border-amber-600 focus:bg-white focus:outline-none text-ink-900 text-sm placeholder:text-ink-400 font-mono transition-all pr-10"
              placeholder="••••••••"
            />
            <button 
              type="button"
              @click="showConfirmPassword = !showConfirmPassword"
              class="absolute right-3 top-1/2 -translate-y-1/2 text-ink-400 hover:text-ink-800 transition-colors"
            >
              <i :class="showConfirmPassword ? 'fas fa-eye-slash' : 'fas fa-eye'" class="text-xs"></i>
            </button>
          </div>
        </div>

        <!-- Submit Button -->
        <button 
          type="submit"
          class="w-full py-3 px-4 mt-2 bg-ink-950 hover:bg-ink-800 text-amber-300 font-medium rounded-xl shadow-sm hover:shadow transition-all active:scale-[0.98]"
        >
          {{ isLogin ? 'Войти в профиль' : 'Зарегистрироваться' }}
        </button>

        <!-- Toggle Auth Mode -->
        <div class="text-center text-xs text-ink-600 pt-2">
          {{ isLogin ? 'Впервые на платформе?' : 'Уже зарегистрированы?' }}
          <button 
            type="button"
            @click="toggleAuthMode"
            class="text-academic-amber hover:text-academic-amber-hover font-semibold ml-1 underline decoration-amber-400/50 underline-offset-4"
          >
            {{ isLogin ? 'Создать аккаунт' : 'Войти' }}
          </button>
        </div>

        <!-- Error Alert -->
        <div v-if="error" class="p-3 rounded-lg bg-red-50 border border-red-200 text-academic-crimson text-xs font-mono text-center">
          {{ error }}
        </div>
      </form>
    </div>
  </BaseModal>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useAuth } from '../composables/useAuth'
import BaseModal from '@/shared/components/BaseModal.vue'

const props = defineProps({
  isLogin: {
    type: Boolean,
    default: true
  }
})

const emit = defineEmits(['close', 'update:isLogin'])
const { login, register, error } = useAuth()

const showPassword = ref(false)
const showConfirmPassword = ref(false)
const form = reactive({
  username: '',
  firstName: '',
  lastName: '',
  email: '',
  password: '',
  confirmPassword: ''
})

const toggleAuthMode = () => {
  emit('update:isLogin', !props.isLogin)
}

const handleSubmit = async () => {
  let success
  if (props.isLogin) {
    success = await login({
      username: form.username,
      password: form.password
    })
  } else {
    if (form.password !== form.confirmPassword) {
      error.value = 'Пароли не совпадают'
      return
    }
    success = await register({
      username: form.username,
      firstName: form.firstName,
      lastName: form.lastName,
      email: form.email,
      password: form.password,
      confirmPassword: form.confirmPassword
    })
  }

  if (success) {
    emit('close')
  }
}
</script>
