import cv2
import face_recognition
import os
import numpy as np
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def load_and_encode_image(image_path):
    """Load an image and return its face encoding."""
    image_bgr = cv2.imread(image_path)
    if image_bgr is None:
        logging.error(f"Failed to load image at {image_path}")
        return None
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    encodings = face_recognition.face_encodings(image_rgb)
    return encodings[0] if encodings else None

def recognize_face(image_path, known_faces_dir):
    """
    Recognizes faces in the given image.

    Args:
        image_path (str): Path to the visitor's image.
        known_faces_dir (str): Directory containing known face images.

    Returns:
        list: List containing recognized face data, such as category and similarity.
    """
    visitor_encoding = load_and_encode_image(image_path)
    if visitor_encoding is None:
        return None

    results = []

    # Compare against known faces
    for known_face_name in os.listdir(known_faces_dir):
        known_face_path = os.path.join(known_faces_dir, known_face_name)
        known_encoding = load_and_encode_image(known_face_path)
        
        if known_encoding is not None:
            distance = face_recognition.face_distance([known_encoding], visitor_encoding)[0]
            similarity = max(0, int((1 - distance) * 100))
            results.append({
                "FaceId": os.path.splitext(known_face_name)[0],
                "Similarity": similarity
            })

    return sorted(results, key=lambda x: x['Similarity'], reverse=True) if results else None