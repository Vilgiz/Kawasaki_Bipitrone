import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array


class ImageProcessor:
    def __init__(self, model_path, class_labels, img_height=128, img_width=128):
        self.model = load_model(model_path)
        self.class_labels = class_labels
        self.img_height = img_height
        self.img_width = img_width

    def process_image(self, image):
        # Предварительная обработка изображения
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

        # Морфологическая обработка
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

        # Поиск контуров
        contours, _ = cv2.findContours(
            thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        results = []
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            area = w * h

            # Фильтр по размеру
            if area < 3000 or area > 15000:
                continue

            roi = image[y:y + h, x:x + w]
            resized_roi = cv2.resize(roi, (self.img_width, self.img_height))
            img_array = img_to_array(resized_roi) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            predictions = self.model.predict(img_array)
            class_index = np.argmax(predictions[0])
            class_label = self.class_labels[class_index]
            confidence = predictions[0][class_index]

            results.append({
                "coordinates": (x, y, w, h),
                "class": class_label,
                # Преобразование в стандартный float
                "confidence": float(confidence)
            })

        return results
