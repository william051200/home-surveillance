import type { ImageDto } from "@/interfaces";
import type { Response } from "@/models";
import axios from "axios";

export class CameraService {
  private static baseUrl = "http://rpiwilliam001:5000/api/capture";

  static captureImage(): Promise<Response<ImageDto>> {
    console.log("Capturing image.");
    return axios.get(CameraService.baseUrl);
  }
}
