from flask import Flask
from flask_restful import Api

from mappers import ImageMapper
from resources import CameraResource
from utils import Camera

app = Flask(__name__)
api = Api(app)

camera = Camera()

api.add_resource(
    CameraResource,
    "/api/capture",
    resource_class_kwargs={"camera": camera, "image_mapper": ImageMapper()},
)

if __name__ == "__main__":
    app.run()
