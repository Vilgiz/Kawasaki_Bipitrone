import cv2


class Camera:
    def __init__(self, source=0):
        self.cap = cv2.VideoCapture(source)

        if not self.cap.isOpened():
            raise ValueError(f"Unable to open camera source: {source}")

    def capture_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            raise RuntimeError("Failed to capture frame from camera")
        return frame

    def release(self):
        self.cap.release()
