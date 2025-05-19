<template>
  <teleport to="body">
    <div class="fixed inset-0 flex items-center justify-center z-50">
      <!-- Затемнённый фон -->
      <div class="absolute inset-0 bg-black bg-opacity-50" @click="$emit('close')"></div>
      
      <!-- Модальное окно -->
      <div class="bg-white rounded-lg w-full max-w-md p-8 relative z-30">
        <slot></slot>
      </div>
    </div>
  </teleport>
</template>

<script setup>
defineEmits(['close'])
</script> 