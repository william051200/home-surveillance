import base64
import cv2

from flask_restful import Resource


class CameraResource(Resource):
    def __init__(self, camera, image_mapper):
        self._camera = camera
        self._image_mapper = image_mapper

    def get(self):
        frame, is_success = self._camera.capture()

        if not is_success:
            return

        # Encode frame as JPEG (or use '.png')
        ret, buffer = cv2.imencode(".png", frame)

        if not ret:
            return

        # Convert to base64
        image_base64 = base64.b64encode(buffer).decode("utf-8")

        return self._image_mapper.map_to_image_json(image_base64)
