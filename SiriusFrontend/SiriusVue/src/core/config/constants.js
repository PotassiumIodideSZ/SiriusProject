// Application constants
export const APP_CONFIG = {
  API_URL: import.meta.env.VITE_API_URL || 'http://localhost:8000/api',
  APP_NAME: 'Sirius Investment Platform',
  APP_VERSION: '1.0.0'
}

// API endpoints
export const API_ENDPOINTS = {
  AUTH: {
    LOGIN: '/auth/login/',
    REGISTER: '/auth/registration/',
    USER: '/auth/user/',
    LOGOUT: '/auth/logout/'
  },
  SURVEY: {
    QUESTIONS: '/surveys/questions/',
    SUBMIT: '/surveys/submit/',
    HISTORY: '/surveys/history/'
  },
  PROFILE: {
    GET: '/profile/',
    UPDATE: '/profile/update/',
    HISTORY: '/profile/history/',
    STATS: '/profile/stats/'
  },
  RESULTS: {
    GET: '/results/',
    RECOMMENDATIONS: '/results/recommendations/'
  }
}

// Error messages
export const ERROR_MESSAGES = {
  NETWORK_ERROR: 'Ошибка сети. Проверьте подключение к интернету.',
  UNAUTHORIZED: 'Не авторизован. Войдите в систему.',
  FORBIDDEN: 'Доступ запрещен.',
  NOT_FOUND: 'Ресурс не найден.',
  SERVER_ERROR: 'Ошибка сервера. Попробуйте позже.',
  UNKNOWN_ERROR: 'Произошла неизвестная ошибка.'
}

// Survey options
export const SURVEY_OPTIONS = [
  { value: 1, text: 'Полностью согласен' },
  { value: 2, text: 'Скорее согласен' },
  { value: 3, text: 'Затрудняюсь ответить' },
  { value: 4, text: 'Скорее не согласен' },
  { value: 5, text: 'Полностью не согласен' }
]

// LocalStorage keys
export const STORAGE_KEYS = {
  TOKEN: 'token',
  USER: 'user',
  SURVEY_ANSWERS: 'survey_answers'
}
