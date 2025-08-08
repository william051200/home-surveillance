import axios from "axios";

export class CameraService {
  private static baseUrl = "http://rpiwilliam001:5000/api/capture";

  static captureImage() {
    return axios.get(CameraService.baseUrl);
  }
}
