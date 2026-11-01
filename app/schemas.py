"""Pydantic schemas for request and response validation.

Adheres strictly to the specification required in section 5.1 of the project document.
"""

from typing import List
from pydantic import BaseModel, Field


class BoundingBox(BaseModel):
    """Bounding box coordinates in pixels."""

    x_min: float = Field(..., description="Minimum X coordinate (left)")
    y_min: float = Field(..., description="Minimum Y coordinate (top)")
    x_max: float = Field(..., description="Maximum X coordinate (right)")
    y_max: float = Field(..., description="Maximum Y coordinate (bottom)")


class DetectionItem(BaseModel):
    """Individual object detection item."""

    class_name: str = Field(..., description="Detected object class name")
    confidence: float = Field(..., description="Confidence score between 0.0 and 1.0")
    box: BoundingBox = Field(..., description="Bounding box of the detected object")


class DetectionResponse(BaseModel):
    """Standard API detection response matching the project specification."""

    status: str = Field("success", description="Status of the detection request")
    detections: List[DetectionItem] = Field(
        default_factory=list, description="List of detected objects"
    )
