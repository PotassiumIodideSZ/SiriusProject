import { ref } from 'vue'

/**
 * Composable для управления асинхронным состоянием
 * @param {Function} asyncFn - асинхронная функция
 * @param {any} initialState - начальное состояние
 * @returns {Object} { state, error, isLoading, execute, reset }
 */
export function useAsyncState(asyncFn, initialState = null) {
  const state = ref(initialState)
  const error = ref(null)
  const isLoading = ref(false)
  
  const execute = async (...args) => {
    isLoading.value = true
    error.value = null
    try {
      const result = await asyncFn(...args)
      state.value = result
      return result
    } catch (err) {
      error.value = err
      throw err
    } finally {
      isLoading.value = false
    }
  }
  
  const reset = () => {
    state.value = initialState
    error.value = null
    isLoading.value = false
  }
  
  return {
    state,
    error,
    isLoading,
    execute,
    reset
  }
}
