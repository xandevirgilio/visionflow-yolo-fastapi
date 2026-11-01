"""FastAPI application for VisionFlow AI object detection microservice.

Provides REST endpoints for detecting objects using YOLOv8, returning
standardized JSON detections as required by the specification.
"""

import io
import logging
from typing import Optional
from fastapi import FastAPI, File, HTTPException, Query, UploadFile, status
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image, UnidentifiedImageError

from app.config import (
    APP_DESCRIPTION,
    APP_TITLE,
    APP_VERSION,
    DEFAULT_CONFIDENCE_THRESHOLD,
    TARGET_CLASSES,
)
from app.schemas import DetectionResponse
from app.services.yolo_detector import YOLODetector

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager to preload YOLO model before serving requests."""
    logger.info("Initializing YOLO model on startup...")
    YOLODetector.get_instance()
    logger.info("YOLO model ready for inference.")
    yield


# Initialize FastAPI app
app = FastAPI(
    title=APP_TITLE,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# Enable CORS for web clients / integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Health"])
def root():
    """Root endpoint with API metadata and supported classes."""
    return {
        "service": APP_TITLE,
        "version": APP_VERSION,
        "status": "healthy",
        "docs": "/docs",
        "supported_classes": TARGET_CLASSES,
        "endpoints": {
            "detect": "POST /detect",
            "health": "GET /health",
        },
    }


@app.get("/health", tags=["Health"])
def health_check():
    """Liveness probe / health check endpoint."""
    return {"status": "ok", "service": APP_TITLE, "version": APP_VERSION}


@app.post(
    "/detect",
    response_model=DetectionResponse,
    status_code=status.HTTP_200_OK,
    tags=["Inference"],
    summary="Detect objects in uploaded image",
    description=(
        "Receives an image binary file (UploadFile), performs object detection "
        "using YOLO, and returns structured JSON with bounding boxes, classes, "
        "and confidence scores."
    ),
)
async def detect_objects(
    file: UploadFile = File(
        ...,
        description="Binary image file to process (JPEG, PNG, WEBP, etc.)",
    ),
    confidence: Optional[float] = Query(
        DEFAULT_CONFIDENCE_THRESHOLD,
        ge=0.05,
        le=1.0,
        description="Minimum confidence threshold for detections",
    ),
    filter_classes: bool = Query(
        True,
        description="If True, filters only the 10 target classes. If False, returns all detected classes.",
    ),
) -> DetectionResponse:
    """Run object detection on the uploaded image file."""
    # Validate content type
    if file.content_type and not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid file type '{file.content_type}'. Must be an image.",
        )

    # Read binary content
    try:
        image_bytes = await file.read()
        if not image_bytes:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Empty image file received.",
            )
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    except UnidentifiedImageError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Uploaded file is not a valid or readable image.",
        )
    except Exception as exc:
        logger.error(f"Error reading image: {exc}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to process image: {str(exc)}",
        )

    # Run detection
    try:
        detector = YOLODetector.get_instance()
        detections = detector.detect(
            image=image,
            confidence_threshold=confidence,
            filter_target_classes=filter_classes,
        )
        return DetectionResponse(status="success", detections=detections)
    except Exception as exc:
        logger.error(f"Inference error: {exc}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error during model inference.",
        )
