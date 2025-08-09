import { useLoadingStore } from "@/stores";

export class LoadingService {
  static start() {
    const { showLoading } = useLoadingStore();
    showLoading();
  }

  static stop() {
    const { hideLoading } = useLoadingStore();
    hideLoading();
  }
}
