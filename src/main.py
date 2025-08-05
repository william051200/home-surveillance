from flask import Flask

from resources import CameraResource
from utils import Camera

app = Flask(__name__)

camera = Camera()


@app.route("/capture")
def capture():
    # return "<h1>Hello, World!</h1>", {"Content-Type": "text/html"}
    return CameraResource(camera)


if __name__ == "__main__":
    app.run()
