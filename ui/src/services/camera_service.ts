import type { ImageDto } from "@/interfaces";
import type { Response } from "@/models";
import axios from "axios";

export class CameraService {
  private static baseUrl = "/api/capture";

  static captureImage(): Promise<Response<ImageDto>> {
    console.log("Capturing image.");
    return axios.get(CameraService.baseUrl);
  }
}
