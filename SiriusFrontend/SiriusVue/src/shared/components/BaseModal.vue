<template>
  <Teleport to="body">
    <div v-if="show" class="fixed inset-0 z-[9999] flex items-center justify-center p-4">
      <!-- Backdrop with soft blur -->
      <div 
        class="absolute inset-0 bg-stone-900/40 backdrop-blur-sm transition-opacity"
        @click="$emit('close')"
      ></div>
      
      <!-- Modal Content -->
      <div 
        class="relative bg-white border border-ink-200 rounded-2xl shadow-xl max-w-md w-full max-h-[90vh] overflow-y-auto z-[10000] transition-all p-6 text-ink-900"
        @click.stop
      >
        <slot></slot>
      </div>
    </div>
  </Teleport>
</template>

<script setup>
defineProps({
  show: {
    type: Boolean,
    default: true
  }
})

defineEmits(['close'])
</script>
