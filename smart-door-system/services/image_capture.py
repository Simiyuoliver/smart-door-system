# In services/image_capture.py
import cv2
from PIL import Image
import os

def capture_image():
    camera = cv2.VideoCapture(0)
    print("Capturing image...")
    ret, frame = camera.read()
    if ret:
        # Convert the image from BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image_path = "static/visitor_image.jpg"
        # Convert the NumPy array to a PIL Image and save it
        pil_image = Image.fromarray(frame_rgb)
        pil_image.save(image_path)
        print(f"Image saved at {image_path}")
    else:
        print("Failed to capture image.")
        image_path = None
    camera.release()
    return image_path