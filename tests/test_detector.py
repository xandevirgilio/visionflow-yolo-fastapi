"""Unit tests for YOLODetector service and class coverage."""

import os
from PIL import Image
from app.config import TARGET_CLASSES
from app.services.yolo_detector import YOLODetector


def test_detector_initialization():
    """Verify YOLODetector loads properly and contains 10 target classes."""
    detector = YOLODetector.get_instance()
    assert detector is not None
    assert len(detector.target_classes) == 10
    for cls in TARGET_CLASSES:
        assert cls in detector.target_classes


def test_detector_inference_on_all_samples():
    """Verify inference runs successfully on all sample images."""
    detector = YOLODetector.get_instance()
    samples_dir = "data/samples"
    image_files = sorted([f for f in os.listdir(samples_dir) if f.endswith(".jpg")])

    assert len(image_files) == 10, f"Expected 10 sample images, found {len(image_files)}"

    detected_classes_all = set()

    for img_name in image_files:
        img_path = os.path.join(samples_dir, img_name)
        image = Image.open(img_path).convert("RGB")
        detections = detector.detect(image, confidence_threshold=0.25, filter_target_classes=True)

        assert isinstance(detections, list)
        for det in detections:
            detected_classes_all.add(det.class_name)

    # Verify high coverage of the target classes across the 10 varied sample images
    assert len(detected_classes_all) >= 8, (
        f"Expected at least 8 distinct target classes detected across samples, got {len(detected_classes_all)}"
    )
