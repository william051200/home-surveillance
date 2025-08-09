<script setup>
  import { ref } from "vue";

  import { LoadingOverlay } from "@/components";
  import { useSessionStore } from "@/stores";

  const session = useSessionStore();
</script>

<template>
  <div>
    <router-view />

    <LoadingOverlay />
  </div>
</template>

<style scoped>
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(255, 255, 255, 0.8); /* white with transparency */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999; /* on top of everything */
}
</style>
