import base64
import cv2

from mappers import ImageMapper


class CameraService:
    def __init__(self, camera):
        self._camera = camera

    def capture_image(self):
        frame, is_success = self._camera.capture()

        if not is_success:
            return

        # Encode frame as JPEG (or use '.png')
        ret, buffer = cv2.imencode(".png", frame)

        if not ret:
            return

        # Convert to base64
        image_base64 = base64.b64encode(buffer).decode("utf-8")

        return ImageMapper.map_to_image_json(image_base64)
