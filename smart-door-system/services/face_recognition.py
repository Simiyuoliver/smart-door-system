# In services/face_recognition.py
import cv2
import face_recognition
import os
import numpy as np

def recognize_face(image_path):
    """
    Recognizes faces in the given image.

    Args:
        image_path (str): Path to the visitor's image.

    Returns:
        list: List containing recognized face data, such as category and similarity.
    """
    # Load the visitor image using OpenCV
    visitor_image_bgr = cv2.imread(image_path)
    if visitor_image_bgr is None:
        # Image not found or cannot be read
        print(f"Failed to load image at {image_path}")
        return None
    # Convert the image from BGR to RGB
    visitor_image = cv2.cvtColor(visitor_image_bgr, cv2.COLOR_BGR2RGB)
    visitor_encoding = face_recognition.face_encodings(visitor_image)

    if not visitor_encoding:
        # No face found in the visitor image
        return None

    visitor_encoding = visitor_encoding[0]  # Assume one face in the image
    results = []

    # Compare against known faces
    for known_face_name in os.listdir(KNOWN_FACES_DIR):
        known_face_path = os.path.join(KNOWN_FACES_DIR, known_face_name)
        # Load known image using OpenCV
        known_image_bgr = cv2.imread(known_face_path)
        if known_image_bgr is None:
            print(f"Failed to load known image at {known_face_path}")
            continue  # Skip if image cannot be read
        # Convert the image from BGR to RGB
        known_image = cv2.cvtColor(known_image_bgr, cv2.COLOR_BGR2RGB)
        known_encoding = face_recognition.face_encodings(known_image)
        
        if known_encoding:
            known_encoding = known_encoding[0]
            # Calculate face distance
            distance = face_recognition.face_distance([known_encoding], visitor_encoding)[0]
            similarity = max(0, int((1 - distance) * 100))  # Convert to similarity percentage
            results.append({
                "FaceId": os.path.splitext(known_face_name)[0],
                "Similarity": similarity
            })

    # Return the most similar face (if any)
    return sorted(results, key=lambda x: x['Similarity'], reverse=True) if results else None