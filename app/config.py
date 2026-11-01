"""Application configuration and constants."""

from typing import List

# 10 Target Classes for UrbanSense / VisionFlow
TARGET_CLASSES: List[str] = [
    "person",
    "bicycle",
    "car",
    "motorcycle",
    "bus",
    "truck",
    "traffic light",
    "fire hydrant",
    "stop sign",
    "backpack",
]

DEFAULT_MODEL_NAME: str = "yolov8n.pt"
DEFAULT_CONFIDENCE_THRESHOLD: float = 0.25

APP_TITLE: str = "VisionFlow AI - Object Detection Microservice"
APP_DESCRIPTION: str = (
    "Backend REST API for real-time object detection using YOLO and FastAPI. "
    "Specialized in 10 urban mobility and smart city object classes."
)
APP_VERSION: str = "1.0.0"
