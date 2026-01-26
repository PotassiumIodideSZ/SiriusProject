# Frontend Architecture Guide

## 📋 Обзор

Этот документ описывает новую модульную архитектуру фронтенда на основе **Feature-Based Modules**.

---

## 🏗️ Структура проекта

```
SiriusFrontend/SiriusVue/src/
├── features/              # Функциональные модули
│   ├── auth/            # Модуль аутентификации
│   ├── survey/          # Модуль опросов
│   ├── profile/         # Модуль профиля
│   └── results/         # Модуль результатов
├── shared/               # Общие компоненты и утилиты
│   ├── components/       # Переиспользуемые компоненты
│   ├── composables/      # Общие composables
│   ├── utils/           # Утилиты
│   └── types/           # Общие типы
├── layout/               # Layout компоненты
│   ├── components/       # Header, Footer и др.
│   └── composables/      # Layout composables
├── core/                # Ядро приложения
│   ├── api/             # Базовая конфигурация API
│   ├── router/          # Главный роутер
│   ├── config/          # Конфигурация
│   └── plugins/         # Vue плагины
├── views/               # Page-level компоненты
├── App.vue             # Главный компонент приложения
└── main.js             # Точка входа
```

---

## 📦 Модули

### 1. Auth Module (`features/auth/`)

**Ответственность:** Аутентификация, регистрация, управление сессией

**Структура:**
```
features/auth/
├── components/
│   └── AuthForm.vue
├── composables/
│   └── useAuth.js
├── stores/
│   └── authStore.js
├── services/
│   └── authAPI.js
├── routes/
│   └── index.js
└── index.js           # Публичный API модуля
```

**Использование:**
```javascript
// Импорт из модуля
import { useAuth, AuthForm } from '@/features/auth'

// Использование в компоненте
const { login, register, user, isAuthenticated } = useAuth()
```

---

### 2. Survey Module (`features/survey/`)

**Ответственность:** Опросы, вопросы, ответы, прогресс

**Структура:**
```
features/survey/
├── components/
│   └── SurveyView.vue
├── composables/
│   └── useSurvey.js
├── stores/
│   └── surveyStore.js
├── services/
│   └── surveyAPI.js
├── routes/
│   └── index.js
└── index.js
```

**Использование:**
```javascript
import { useSurvey } from '@/features/survey'

const { currentQuestion, nextQuestion, submitAnswer, finishSurvey } = useSurvey()
```

---

### 3. Profile Module (`features/profile/`)

**Ответственность:** Профиль пользователя, статистика, история

**Структура:**
```
features/profile/
├── components/
│   └── ProfileView.vue
├── composables/
│   └── useProfile.js
├── stores/
│   └── profileStore.js
├── services/
│   └── profileAPI.js
├── routes/
│   └── index.js
└── index.js
```

**Использование:**
```javascript
import { useProfile } from '@/features/profile'

const { profile, stats, history, updateProfile } = useProfile()
```

---

### 4. Results Module (`features/results/`)

**Ответственность:** Результаты опросов, рекомендации, визуализация

**Структура:**
```
features/results/
├── components/
│   └── ResultsView.vue
├── composables/
│   └── useResults.js
├── stores/
│   └── resultsStore.js
├── services/
│   └── resultsAPI.js
├── routes/
│   └── index.js
└── index.js
```

**Использование:**
```javascript
import { useResults } from '@/features/results'

const { results, recommendations, riskScore } = useResults()
```

---

## 🧩 Shared Components

### Доступные компоненты

- **BaseModal** - Переиспользуемый модальный компонент
- **BackgroundCircles** - Декоративный фон

### Использование:
```javascript
import { BaseModal } from '@/shared/components/BaseModal'
import { BackgroundCircles } from '@/shared/components/BackgroundCircles'
```

---

## 🛠️ Shared Composables

### Доступные composables

- **useLocalStorage** - Работа с localStorage
- **useAsyncState** - Управление асинхронным состоянием

### Использование:
```javascript
import { useLocalStorage, useAsyncState } from '@/shared/composables'

const [token, setToken] = useLocalStorage('token', null)
const { state, isLoading, execute } = useAsyncState(fetchData)
```

---

## 🔧 Core

### API Configuration

**Файл:** `core/api/axiosInstance.js`

- Базовая конфигурация axios
- Request interceptor (добавление токена)
- Response interceptor (обработка ошибок)

### Router

**Файл:** `core/router/index.js`

- Объединяет все маршруты из модулей
- Navigation guards для защиты маршрутов

### Constants

**Файл:** `core/config/constants.js`

- API endpoints
- Error messages
- Survey options
- LocalStorage keys

---

## 📝 Правила разработки

### 1. Импорты

✅ **Правильно:**
```javascript
// Импорт из модуля
import { useAuth } from '@/features/auth'
import { BaseModal } from '@/shared/components/BaseModal'
```

❌ **Неправильно:**
```javascript
// Глубокая вложенность
import { useAuth } from '@/features/auth/composables/useAuth'
```

### 2. Зависимости между модулями

✅ **Правильно:** Модули зависят только от `shared` и `core`

❌ **Неправильно:** Модули зависят друг от друга

### 3. Размер компонентов

- Компоненты должны быть < 300 строк
- Если больше - разбить на подкомпоненты
- Логика выносится в composables

### 4. Store правила

- Один store на модуль
- Store не должен зависеть от других stores
- Коммуникация между stores через composables

---

## 🚀 Добавление нового функционала

### Шаги:

1. **Создать модуль** в `features/`
   ```
   features/new-feature/
   ├── components/
   ├── composables/
   ├── stores/
   ├── services/
   ├── routes/
   └── index.js
   ```

2. **Создать API service** в `services/`
   ```javascript
   import api from '@/core/api/axiosInstance'
   import { API_ENDPOINTS } from '@/core/config/constants'
   
   export const newFeatureAPI = {
     async getData() {
       const response = await api.get(API_ENDPOINTS.NEW_FEATURE.GET)
       return response.data
     }
   }
   ```

3. **Создать store** в `stores/`
   ```javascript
   import { defineStore } from 'pinia'
   import { newFeatureAPI } from '../services/newFeatureAPI'
   
   export const useNewFeatureStore = defineStore('newFeature', () => {
     const data = ref(null)
     // ...
     return { data, ... }
   })
   ```

4. **Создать composable** в `composables/`
   ```javascript
   import { computed } from 'vue'
   import { useNewFeatureStore } from '../stores/newFeatureStore'
   
   export function useNewFeature() {
     const store = useNewFeatureStore()
     return { data: computed(() => store.data), ... }
   }
   ```

5. **Создать компоненты** в `components/`

6. **Создать routes** в `routes/`
   ```javascript
   export const newFeatureRoutes = [
     {
       path: '/new-feature',
       name: 'NewFeature',
       component: () => import('../components/NewFeatureView.vue'),
       meta: { requiresAuth: true }
     }
   ]
   ```

7. **Обновить публичный API** в `index.js`
   ```javascript
   export { default as NewFeatureView } from './components/NewFeatureView.vue'
   export { useNewFeature } from './composables/useNewFeature.js'
   export { useNewFeatureStore } from './stores/newFeatureStore.js'
   export { newFeatureAPI } from './services/newFeatureAPI.js'
   export { newFeatureRoutes } from './routes/index.js'
   ```

8. **Добавить routes** в `core/router/index.js`
   ```javascript
   import { newFeatureRoutes } from '@/features/new-feature/routes'
   
   const router = createRouter({
     routes: [
       ...staticRoutes,
       ...newFeatureRoutes,
       // ... другие модули
     ]
   })
   ```

---

## 🎯 Преимущества новой архитектуры

### 1. Разделение контекста
- Каждый модуль изолирован и самодостаточен
- Четкие границы ответственности
- Легко понять, где находится код

### 2. Масштабируемость
- Новые фичи добавляются как новые модули
- Нет влияния на существующий код
- Параллельная разработка

### 3. Переиспользование
- Shared компоненты используются везде
- Composables переиспользуются
- Нет дублирования кода

### 4. Навигация
- Четкая структура, легко находить нужный код
- Понятные зависимости
- Быстрая разработка

### 5. Тестируемость
- Каждый модуль тестируется независимо
- Composables легко мокать
- API сервисы изолированы

---

## 📚 Дополнительные ресурсы

- [Vue 3 Composition API](https://vuejs.org/guide/extras/composition-api-faq.html)
- [Pinia Documentation](https://pinia.vuejs.org/)
- [Vue Router](https://router.vuejs.org/)
- [Feature-Sliced Design](https://feature-sliced.design/) - вдохновение для архитектуры
