Smart Door System
A smart door system that uses facial recognition to grant or deny access. The system captures an image of the visitor, recognizes the face by comparing it with known faces, logs the visitor's data to Firebase, and controls the door based on recognition results. It also sends notifications regarding access attempts.

Table of Contents
Features
Prerequisites
Installation
Usage
Project Structure
Troubleshooting
Contributing
License
Features
Face Capture: Uses a webcam to capture an image of the visitor.
Face Recognition: Compares the captured image with known faces.
Access Control: Opens the door if the visitor is recognized with high confidence.
Visitor Logging: Logs visitor information to Firebase.
Notifications: Sends notifications about access attempts.
Mock GPIO Control: Simulates GPIO operations for door control, suitable for testing without actual hardware.
Prerequisites
Python 3.6 or higher
Virtual Environment: Recommended to avoid package conflicts.
pip: Python package installer.
Python Packages
opencv-python
face-recognition
numpy
Pillow
firebase-admin
System Dependencies
CMake
dlib
Note: Installing dlib can be challenging on some systems. Follow the instructions carefully.

Installation
1. Clone the Repository
git clone https://github.com/yourusername/smart-door-system.git
cd smart-door-system
Copy
Insert

2. Set Up a Virtual Environment
python -m venv venv
Copy
Insert

Activate the virtual environment:

Windows:
venv\Scripts\activate
Copy
Insert

Linux/MacOS:
source venv/bin/activate
Copy
Insert

3. Install System Dependencies
Windows
Install Visual Studio Build Tools.
Install CMake:
pip install cmake
Copy
Insert

Linux
sudo apt-get install build-essential cmake
sudo apt-get install libgtk-3-dev
Copy
Insert

4. Install Python Dependencies
pip install -r requirements.txt
Copy
Insert

Content of requirements.txt:

opencv-python
face-recognition
numpy
Pillow
firebase-admin
Copy
Insert

5. Configure Firebase
Create a Firebase project.
Generate a service account key (serviceAccountKey.json) and place it in the project root directory.
6. Set Up Known Faces
Place images of known individuals in the known_faces directory.
Name the images in the format PersonName.jpg.
Ensure images are clear and show only one face per image.
Usage
Run the main script:

python main.py
Copy
Insert

Process Flow:

System Initialization: Sets up the GPIO mode and pin.
Capture Image: Takes a photo of the visitor.
Face Recognition: Compares the captured image with known faces.
Access Decision:
If the visitor is recognized with more than 75% similarity, the door opens.
If not recognized or similarity is low, access is denied.
Logging and Notifications: Visitor data is logged to Firebase, and notifications are sent.
Project Structure
smart-door-system/
│
├── main.py
├── requirements.txt
├── serviceAccountKey.json
├── known_faces/
│   ├── PersonA.jpg
│   ├── PersonB.jpg
│   └── ...
├── static/
│   └── visitor_image.jpg
├── services/
│   ├── face_recognition.py
│   ├── image_capture.py
│   ├── notification.py
│   ├── gpio_control.py
│   └── firebase_logging.py
└── README.md
Copy
Insert

main.py: Entry point of the application.
services/: Contains modules for different functionalities.
known_faces/: Contains images of known individuals.
static/: Stores images captured during runtime.
Troubleshooting
RuntimeError: Unsupported image type, must be 8bit gray or RGB image.
Problem: The face_recognition library throws an error about an unsupported image type.

Cause: OpenCV captures images in BGR format, but face_recognition expects images in RGB format.

Solution:

Option 1: Convert Image to RGB Before Saving
Modify the capture_image function in services/image_capture.py:

import cv2
from PIL import Image

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
Copy
Insert

Option 2: Convert Image During Recognition
Modify the recognize_face function in services/face_recognition.py:

import cv2
import face_recognition
import os

def recognize_face(image_path):
    # Load the visitor image using OpenCV
    visitor_image_bgr = cv2.imread(image_path)
    if visitor_image_bgr is None:
        print(f"Failed to load image at {image_path}")
        return None
    # Convert the image from BGR to RGB
    visitor_image = cv2.cvtColor(visitor_image_bgr, cv2.COLOR_BGR2RGB)
    visitor_encoding = face_recognition.face_encodings(visitor_image)
    # Rest of the code...
Copy
Insert

Recommendation: Use Option 1 for simplicity unless you need consistent image handling throughout your application.

dlib Installation Issues
If you face issues installing dlib, refer to the official dlib installation guide. Ensure all dependencies are installed and your compiler is up to date.

Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Commit your changes with clear messages.
Push to your fork and submit a pull request.
Please ensure all new code includes appropriate tests and documentation.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
face_recognition
Firebase
OpenCV
Note: This project is intended for educational purposes. Ensure compliance with local laws and regulations when using surveillance and facial recognition technologies.