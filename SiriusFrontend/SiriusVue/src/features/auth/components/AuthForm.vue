<template>
  <BaseModal @close="$emit('close')">
    <div class="relative">
      <!-- Крестик для закрытия -->
      <button 
        @click="$emit('close')" 
        class="absolute -right-2 -top-4 text-gray-500 hover:text-gray-700"
      >
        <i class="fas fa-times text-xl"></i>
      </button>

      <!-- Заголовок -->
      <h2 class="text-2xl text-gray-700 font-semibold text-center mb-8">
        {{ isLogin ? 'Вход' : 'Регистрация' }}
      </h2>

      <!-- Форма -->
      <form @submit.prevent="handleSubmit" class="space-y-4">
        <!-- Поле Username -->
        <div>
          <label class="block text-sm text-gray-600 mb-1">Имя пользователя</label>
          <input 
            type="text" 
            v-model="form.username"
            autocomplete="username"
            class="w-full px-4 py-2 rounded-lg bg-gray-100 border border-transparent focus:border-purple-500 focus:bg-white focus:outline-none text-gray-800"
            placeholder="Введите имя пользователя"
          />
        </div>

        <!-- Поля для регистрации -->
        <template v-if="!isLogin">
          <div>
            <label class="block text-sm text-gray-600 mb-1">Имя</label>
            <input 
              type="text" 
              v-model="form.firstName"
              autocomplete="given-name"
              required
              class="w-full px-4 py-2 rounded-lg bg-gray-100 border border-transparent focus:border-purple-500 focus:bg-white focus:outline-none text-gray-800"
              placeholder="Введите имя"
            />
          </div>
          <div>
            <label class="block text-sm text-gray-600 mb-1">Фамилия</label>
            <input 
              type="text" 
              v-model="form.lastName"
              autocomplete="family-name"
              required
              class="w-full px-4 py-2 rounded-lg bg-gray-100 border border-transparent focus:border-purple-500 focus:bg-white focus:outline-none text-gray-800"
              placeholder="Введите фамилию"
            />
          </div>
          <div>
            <label class="block text-sm text-gray-600 mb-1">Email</label>
            <input 
              type="email" 
              v-model="form.email"
              autocomplete="email"
              required
              class="w-full px-4 py-2 rounded-lg bg-gray-100 border border-transparent focus:border-purple-500 focus:bg-white focus:outline-none text-gray-800"
              placeholder="Введите email"
            />
          </div>
        </template>

        <!-- Поле Пароль -->
        <div class="relative">
          <label class="block text-sm text-gray-600 mb-1">Пароль</label>
          <input 
            :type="showPassword ? 'text' : 'password'"
            v-model="form.password"
            :autocomplete="isLogin ? 'current-password' : 'new-password'"
            required
            class="w-full px-4 py-2 rounded-lg bg-gray-100 border border-transparent focus:border-purple-500 focus:bg-white focus:outline-none text-gray-800"
            placeholder="Введите пароль"
          />
          <!-- Иконка показать/скрыть пароль -->
          <button 
            type="button"
            @click="showPassword = !showPassword"
            class="absolute right-3 top-8 text-gray-500 hover:text-gray-700"
          >
            <i :class="showPassword ? 'fas fa-eye-slash' : 'fas fa-eye'"></i>
          </button>
        </div>

        <!-- Поле подтверждения пароля (только для регистрации) -->
        <div v-if="!isLogin" class="relative">
          <label class="block text-sm text-gray-600 mb-1">Подтвердите пароль</label>
          <input 
            :type="showConfirmPassword ? 'text' : 'password'"
            v-model="form.confirmPassword"
            autocomplete="new-password"
            required
            class="w-full px-4 py-2 rounded-lg bg-gray-100 border border-transparent focus:border-purple-500 focus:bg-white focus:outline-none text-gray-800"
            placeholder="Введите пароль еще раз"
          />
          <!-- Иконка показать/скрыть подтверждение пароля -->
          <button 
            type="button"
            @click="showConfirmPassword = !showConfirmPassword"
            class="absolute right-3 top-8 text-gray-500 hover:text-gray-700"
          >
            <i :class="showConfirmPassword ? 'fas fa-eye-slash' : 'fas fa-eye'"></i>
          </button>
        </div>

        <!-- Ссылка "Забыли пароль?" -->
        <div class="flex justify-end">
          <a href="#" class="text-sm text-purple-600 hover:text-purple-700">
            Забыли пароль?
          </a>
        </div>

        <!-- Кнопка отправки -->
        <button 
          type="submit"
          class="w-full py-2 px-4 bg-purple-600 hover:bg-purple-700 text-white font-semibold rounded-lg transition duration-200"
        >
          {{ isLogin ? 'Войти' : 'Зарегистрироваться' }}
        </button>

        <!-- Переключение между регистрацией и входом -->
        <div class="text-center text-sm text-gray-600 mt-4">
          {{ isLogin ? 'Еще не зарегистрированы?' : 'Уже есть аккаунт?' }}
          <button 
            type="button"
            @click="toggleAuthMode"
            class="text-purple-600 hover:text-purple-700 font-medium ml-1"
          >
            {{ isLogin ? 'Зарегистрироваться' : 'Войти' }}
          </button>
        </div>

        <!-- Сообщение об ошибке -->
        <div v-if="error" class="text-red-500 text-sm text-center">
          {{ error }}
        </div>
      </form>
    </div>
  </BaseModal>
</template>

<script setup>
import { ref, reactive, computed } from 'vue'
import { useAuth } from '../composables/useAuth'
import BaseModal from '@/shared/components/BaseModal.vue'

const props = defineProps({
  isLogin: {
    type: Boolean,
    default: false
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
  console.log('handleSubmit called, isLogin:', props.isLogin)
  let success
  if (props.isLogin) {
    console.log('Calling login with:', { username: form.username, password: form.password })
    success = await login({
      username: form.username,
      password: form.password
    })
  } else {
    // Validate password confirmation for registration
    if (form.password !== form.confirmPassword) {
      error.value = 'Пароли не совпадают'
      return
    }
    
    // Log form data for debugging
    console.log('Form data being sent:', {
      username: form.username,
      firstName: form.firstName,
      lastName: form.lastName,
      email: form.email,
      password: form.password,
      confirmPassword: form.confirmPassword
    })
    
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
