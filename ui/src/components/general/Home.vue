<script setup lang="ts">
import { ref } from "vue";
import { useSessionStore } from "@/stores";

const session = useSessionStore();
const newName = ref("");

function setName(value: string) {
  newName.value = value;
}
</script>

<template>
  <n-h1>Welcome, {{ session.name }}</n-h1>
  <n-input v-model:value="newName" placeholder="Enter your name" />
  <n-button type="primary" @click="setName(newName)">Update Name</n-button>
</template>
