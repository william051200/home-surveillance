import { createRouter, createWebHistory } from "vue-router";
import { Home } from "@/components";

const routes = [{ path: "/", component: Home }];

// ✅ Export the router instance
export const router = createRouter({
  history: createWebHistory(),
  routes,
});
