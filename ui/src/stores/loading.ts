import { ref } from "vue";

const visible = ref(false);

export function useLoadingStore() {
  function showLoading() {
    console.log('show loading')
    visible.value = true;
  }

  function hideLoading() {
    console.log('hide loading')
    visible.value = false;
  }

  return { visible, showLoading, hideLoading };
}
