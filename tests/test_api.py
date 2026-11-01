"""Integration tests for FastAPI endpoints."""

import os
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.config import TARGET_CLASSES

client = TestClient(app)


def test_root_endpoint():
    """Verify root endpoint returns healthy status and metadata."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "supported_classes" in data
    assert len(data["supported_classes"]) == 10


def test_health_endpoint():
    """Verify health check endpoint returns 200 ok."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"


def test_detect_endpoint_valid_image():
    """Verify /detect endpoint processes valid image and returns schema-compliant JSON."""
    sample_path = "data/samples/01_car.jpg"
    assert os.path.exists(sample_path), f"Sample image {sample_path} not found"

    with open(sample_path, "rb") as f:
        files = {"file": ("01_car.jpg", f, "image/jpeg")}
        response = client.post("/detect", files=files)

    assert response.status_code == 200
    payload = response.json()

    # Validate schema strictly according to PDF section 5.1
    assert "status" in payload
    assert payload["status"] == "success"
    assert "detections" in payload
    assert isinstance(payload["detections"], list)
    assert len(payload["detections"]) > 0

    first_det = payload["detections"][0]
    assert "class_name" in first_det
    assert "confidence" in first_det
    assert "box" in first_det
    assert 0.0 <= first_det["confidence"] <= 1.0

    box = first_det["box"]
    assert "x_min" in box
    assert "y_min" in box
    assert "x_max" in box
    assert "y_max" in box
    assert box["x_min"] <= box["x_max"]
    assert box["y_min"] <= box["y_max"]


def test_detect_endpoint_invalid_file_type():
    """Verify /detect rejects non-image mime types."""
    files = {"file": ("test.txt", b"plain text content", "text/plain")}
    response = client.post("/detect", files=files)
    assert response.status_code == 400


def test_detect_endpoint_corrupted_image():
    """Verify /detect rejects corrupted image content."""
    files = {"file": ("corrupt.jpg", b"invalid_binary_header", "image/jpeg")}
    response = client.post("/detect", files=files)
    assert response.status_code == 400
