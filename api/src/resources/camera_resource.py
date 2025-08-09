from flask_restful import Resource


class CameraResource(Resource):
    def __init__(self, camera_service):
        self._camera_service = camera_service

    def get(self):
        return self._camera_service.capture_image()
