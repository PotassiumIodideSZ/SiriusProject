import { ref, watch } from 'vue'

/**
 * Composable для работы с localStorage
 * @param {string} key - ключ localStorage
 * @param {any} defaultValue - значение по умолчанию
 * @returns {Array} [value, setValue] - значение и функция для его изменения
 */
export function useLocalStorage(key, defaultValue) {
  const stored = localStorage.getItem(key)
  const value = ref(stored ? JSON.parse(stored) : defaultValue)
  
  const setValue = (newValue) => {
    value.value = newValue
    if (newValue === null || newValue === undefined) {
      localStorage.removeItem(key)
    } else {
      localStorage.setItem(key, JSON.stringify(newValue))
    }
  }
  
  // Слушаем изменения value и синхронизируем с localStorage
  watch(value, (newValue) => {
    if (newValue === null || newValue === undefined) {
      localStorage.removeItem(key)
    } else {
      localStorage.setItem(key, JSON.stringify(newValue))
    }
  }, { deep: true })
  
  return [value, setValue]
}
