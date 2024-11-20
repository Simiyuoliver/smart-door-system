import face_recognition
import os

# Directory where known face images are stored
KNOWN_FACES_DIR = "static/known_faces"

def recognize_face(image_path):
    """
    Recognizes faces in the given image.

    Args:
        image_path (str): Path to the visitor's image.

    Returns:
        list: List containing recognized face data, such as category and similarity.
    """
    # Load the visitor image
    visitor_image = face_recognition.load_image_file(image_path)
    visitor_encoding = face_recognition.face_encodings(visitor_image)

    if not visitor_encoding:
        # No face found in the visitor image
        return None

    visitor_encoding = visitor_encoding[0]  # Assume one face in the image
    results = []

    # Compare against known faces
    for known_face_name in os.listdir(KNOWN_FACES_DIR):
        known_face_path = os.path.join(KNOWN_FACES_DIR, known_face_name)
        known_image = face_recognition.load_image_file(known_face_path)
        known_encoding = face_recognition.face_encodings(known_image)

        if known_encoding:
            known_encoding = known_encoding[0]
            # Calculate face distance
            distance = face_recognition.face_distance([known_encoding], visitor_encoding)[0]
            similarity = max(0, int((1 - distance) * 100))  # Convert to similarity percentage
            results.append({
                "FaceId": known_face_name.split('.')[0],
                "Similarity": similarity
            })

    # Return the most similar face (if any)
    return sorted(results, key=lambda x: x['Similarity'], reverse=True) if results else None
