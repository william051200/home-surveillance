<script setup lang="ts">
import { ref } from "vue";
import { useSessionStore } from "@/stores";
import { CameraService } from "@/services";

const session = useSessionStore();
const newName = ref("");

function setName(value: string) {
  newName.value = value;
}

function onCaptureButtonClicked() {
  CameraService.captureImage()
    .then((value) => {
      console.log(value);
    })
    .catch((err) => {
      console.log(err);
    });
}
</script>

<template>
  <n-flex vertical>
    <n-h1>Welcome, {{ session.name }}</n-h1>
    <n-input v-model:value="newName" placeholder="Enter your name" />
    <n-button type="primary" @click="setName(newName)">Update Name</n-button>
    <n-button type="primary" @click="onCaptureButtonClicked">Capture</n-button>
  </n-flex>
</template>
