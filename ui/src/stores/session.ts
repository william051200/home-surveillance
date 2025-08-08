import { defineStore } from "pinia";
import { Session } from "@/models";

export const useSessionStore = defineStore("session", () => {
  const session = new Session();

  return session;
});
