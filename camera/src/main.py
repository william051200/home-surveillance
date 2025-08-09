from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from resources import CameraResource
from services import CameraService
from utils import Camera

app = Flask(__name__)
api = Api(app)

CORS(app)

camera = Camera()
camera_service = CameraService(camera)

api.add_resource(
    CameraResource,
    "/api/capture",
    resource_class_kwargs={"camera_service": camera_service},
)

if __name__ == "__main__":
    app.run()
