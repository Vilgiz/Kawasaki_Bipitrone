from fastapi import APIRouter
from app.services.camera import Camera
from app.services.image_processor import ImageProcessor
from fastapi.responses import JSONResponse
import cv2

router = APIRouter()

# Инициализация компонентов
# camera = Camera()
image_processor = ImageProcessor(
    model_path="detail_classifier_model.keras",
    class_labels=["class1", "class2", "class3"]
)


@router.get("/capture")
def capture_image():
    try:
        # frame = camera.capture_frame()
        frame = cv2.imread("test.png")
        results = image_processor.process_image(frame)
        return JSONResponse(content={"results": results})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@router.on_event("shutdown")
def shutdown_event():
    # camera.release()
    pass
