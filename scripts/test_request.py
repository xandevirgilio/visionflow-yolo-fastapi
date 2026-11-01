"""Script to test live FastAPI /detect endpoint with a sample image.

Usage:
    python scripts/test_request.py [path_to_image]
"""

import json
import sys
import requests

API_URL = "http://localhost:8000/detect"
DEFAULT_IMAGE = "data/samples/01_car.jpg"


def main():
    img_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_IMAGE
    print(f"Sending '{img_path}' to {API_URL}...")

    try:
        with open(img_path, "rb") as f:
            files = {"file": (img_path, f, "image/jpeg")}
            response = requests.post(API_URL, files=files, params={"confidence": 0.25})

        print(f"HTTP Status: {response.status_code}")
        if response.status_code == 200:
            print("\nResponse JSON:")
            print(json.dumps(response.json(), indent=2))
        else:
            print(f"Error: {response.text}")
    except requests.exceptions.ConnectionError:
        print("\n[!] Connection Error: FastAPI server is not running on http://localhost:8000.")
        print("    Start it with: uvicorn app.main:app --reload")


if __name__ == "__main__":
    main()
