"""Performance benchmark and validation script for YOLOv8n detector.

Evaluates latency, FPS, and detection accuracy across all 10 sample images.
"""

import os
import sys
import time
from PIL import Image

# Ensure project root is in python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.config import TARGET_CLASSES
from app.services.yolo_detector import YOLODetector


def run_benchmark():
    detector = YOLODetector.get_instance()
    samples_dir = "data/samples"
    image_files = sorted([f for f in os.listdir(samples_dir) if f.endswith(".jpg")])

    print("=" * 80)
    print(" VisionFlow AI - YOLOv8n Benchmark & Validation Report")
    print("=" * 80)
    print(f"Total Sample Images: {len(image_files)}")
    print(f"Target Classes ({len(TARGET_CLASSES)}): {', '.join(TARGET_CLASSES)}")
    print("-" * 80)

    # Warmup
    warmup_img = Image.open(os.path.join(samples_dir, image_files[0])).convert("RGB")
    for _ in range(3):
        detector.detect(warmup_img)

    results = []
    latencies = []

    for idx, fname in enumerate(image_files, start=1):
        img_path = os.path.join(samples_dir, fname)
        img = Image.open(img_path).convert("RGB")

        # Measure inference latency over 3 iterations
        times = []
        for _ in range(3):
            t0 = time.perf_counter()
            dets = detector.detect(img, confidence_threshold=0.25, filter_target_classes=True)
            times.append((time.perf_counter() - t0) * 1000.0)

        avg_lat = sum(times) / len(times)
        latencies.append(avg_lat)

        det_summary = ", ".join(
            [f"{d.class_name} ({d.confidence:.2f})" for d in sorted(dets, key=lambda x: x.confidence, reverse=True)[:3]]
        )
        if len(dets) > 3:
            det_summary += f" +{len(dets) - 3} more"

        results.append({
            "idx": idx,
            "file": fname,
            "detections_count": len(dets),
            "top_detections": det_summary if det_summary else "No detections",
            "latency_ms": avg_lat,
        })

    # Print Table
    print(f"{'#':<3} {'Image File':<25} {'Detections':<12} {'Latency (ms)':<14} {'Top Detections'}")
    print("-" * 80)
    for r in results:
        print(f"{r['idx']:<3} {r['file']:<25} {r['detections_count']:<12} {r['latency_ms']:<14.2f} {r['top_detections']}")

    avg_latency = sum(latencies) / len(latencies)
    fps = 1000.0 / avg_latency if avg_latency > 0 else 0

    print("=" * 80)
    print(" BENCHMARK SUMMARY")
    print("=" * 80)
    print(f" Average Latency per Image : {avg_latency:.2f} ms")
    print(f" Average Throughput (FPS)  : {fps:.1f} FPS (CPU)")
    print(f" Min Latency               : {min(latencies):.2f} ms")
    print(f" Max Latency               : {max(latencies):.2f} ms")
    print(f" Architecture              : YOLOv8 Nano (yolov8n.pt)")
    print("=" * 80)


if __name__ == "__main__":
    run_benchmark()
