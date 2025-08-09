<script setup>
  import { useLoadingStore } from "@/stores";

  const { visible } = useLoadingStore();
</script>

<template>
  <div v-if="visible" class="loading-overlay">
    <n-spin size="large" tip="Loading..." />
  </div>
</template>

<style scoped>
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(255, 255, 255, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
}
</style>
