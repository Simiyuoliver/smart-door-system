from services.image_capture import capture_image
from services.face_recognition import recognize_face
from services.firebase_logger import log_visitor
from services.door_control import open_door
from services.notification import send_notification
import time

# In main.py
def main():
    print("System initialized.")
    # Step 1: Capture visitor's image
    image_path = capture_image()
    if image_path:
        print(f"Image captured at {image_path}")
        
        # Step 2: Recognize face
        result = recognize_face(image_path)
        print(f"Face recognition result: {result}")
        
        # Step 3: Log visitor's data to Firebase
        timestamp = int(time.time())  # Generate a UNIX timestamp
        if result:
            # Determine visitor category
            category = "Family" if result[0]['FaceId'].startswith('Fam') else "Friend"
            similarity = result[0]['Similarity']
            visitor_id = f"visitor_{timestamp}"  # Unique visitor ID
            log_visitor(visitor_id, category, similarity, timestamp)
            print(f"Visitor logged: {visitor_id}, {category}, {similarity}, {timestamp}")
            
            # Step 4: Handle access control
            if similarity > 75:
                open_door()
                send_notification(f"Visitor identified as {category} with {similarity}% confidence.")
            else:
                send_notification("Access denied.")
        else:
            # Log unknown visitor
            visitor_id = f"visitor_{timestamp}"  # Unique visitor ID
            log_visitor(visitor_id, "Unknown", 0, timestamp)
            send_notification("Unknown visitor detected.")
            print("Unknown visitor logged.")
    else:
        print("No image captured.")
