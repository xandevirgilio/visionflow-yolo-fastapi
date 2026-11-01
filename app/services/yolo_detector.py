"""YOLO Object Detector Service.

Encapsulates YOLO inference, model loading, and result serialization
into the required Pydantic schema.
"""

import logging
from typing import List, Optional
from PIL import Image
from ultralytics import YOLO

from app.config import DEFAULT_CONFIDENCE_THRESHOLD, DEFAULT_MODEL_NAME, TARGET_CLASSES
from app.schemas import BoundingBox, DetectionItem

logger = logging.getLogger(__name__)


class YOLODetector:
    """Service wrapper for YOLO model inference."""

    _instance: Optional["YOLODetector"] = None

    def __init__(self, model_name: str = DEFAULT_MODEL_NAME):
        self.model_name = model_name
        logger.info(f"Loading YOLO model: {model_name}")
        self.model = YOLO(model_name)
        self.target_classes = set(TARGET_CLASSES)
        logger.info(f"Model loaded. Target classes count: {len(self.target_classes)}")

    @classmethod
    def get_instance(cls, model_name: str = DEFAULT_MODEL_NAME) -> "YOLODetector":
        """Get or initialize singleton detector instance."""
        if cls._instance is None:
            cls._instance = YOLODetector(model_name=model_name)
        return cls._instance

    def detect(
        self,
        image: Image.Image,
        confidence_threshold: float = DEFAULT_CONFIDENCE_THRESHOLD,
        filter_target_classes: bool = True,
    ) -> List[DetectionItem]:
        """Run object detection on a PIL Image.

        Args:
            image: PIL Image to run inference on.
            confidence_threshold: Minimum confidence score (0.0 to 1.0).
            filter_target_classes: Whether to filter only the 10 target classes.

        Returns:
            List of DetectionItem with class_name, confidence, and bounding box.
        """
        # Run inference
        results = self.model.predict(
            source=image,
            conf=confidence_threshold,
            verbose=False,
        )

        detections: List[DetectionItem] = []
        if not results:
            return detections

        first_result = results[0]
        boxes = first_result.boxes

        if boxes is None or len(boxes) == 0:
            return detections

        for box in boxes:
            cls_id = int(box.cls[0].item())
            class_name = self.model.names[cls_id]

            # If filtering is enabled, skip classes not in target classes
            if filter_target_classes and class_name not in self.target_classes:
                continue

            conf = float(box.conf[0].item())
            xyxy = box.xyxy[0].tolist()  # [x_min, y_min, x_max, y_max]

            detection_item = DetectionItem(
                class_name=class_name,
                confidence=round(conf, 4),
                box=BoundingBox(
                    x_min=round(xyxy[0], 2),
                    y_min=round(xyxy[1], 2),
                    x_max=round(xyxy[2], 2),
                    y_max=round(xyxy[3], 2),
                ),
            )
            detections.append(detection_item)

        return detections
