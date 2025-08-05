import cv2

from flask import Response


class CameraResource(Response):
    def __init__(self, camera):
        self._camera = camera

    def get(self):
        frame = self._camera.capture()

        if not frame:
            return

        # Encode frame as JPEG (or use '.png')
        success, encoded_image = cv2.imencode(".png", frame)

        if not success:
            return

        image_bytes = encoded_image.tobytes()
        print(f"Image converted to bytes, size: {len(image_bytes)} bytes")

        return image_bytes
