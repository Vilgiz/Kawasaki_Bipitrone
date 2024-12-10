from fastapi import FastAPI
from app.routers import predict
from fastapi import FastAPI
from app.routers.camera_router import router as camera_router

app = FastAPI()

# Основной маршрут


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Пример маршрута


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "status": "available"}


# Подключаем маршруты из predict.py
app.include_router(predict.router)
app.include_router(camera_router, prefix="/api")
