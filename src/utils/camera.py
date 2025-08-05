import cv2


class Camera:
    def __init__(self):
        # Open the default camera (0 = built-in webcam, use 1 or other for external)
        self._camera = cv2.VideoCapture(0)

    def release_camera(self):
        self._camera.release()

    def capture(self):
        if not self._camera.isOpened():
            print("Cannot open camera")
            return

        ret, frame = self._camera.read()

        if not ret:
            print("Can't receive frame. Exiting...")
            return
        return frame
