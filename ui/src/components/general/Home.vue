<script setup lang="ts">
import { ref } from "vue";
import type { ImageDto } from "@/interfaces";
import type { Response } from "@/models";
import { CameraService } from "@/services";
import { useSessionStore } from "@/stores";

const session = useSessionStore();
const newName = ref("");

function setName(value: string) {
  newName.value = value;
}

function onCaptureButtonClicked() {
  CameraService.captureImage()
    .then((value: Response<ImageDto>) => {
      if (value.data) session.imageBase64 = `data:image/png;base64,${value.data.image}`;
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
    <n-image v-if="session.imageBase64" :src="session.imageBase64" alt="Base64 Image" width="500" />
  </n-flex>
</template>
