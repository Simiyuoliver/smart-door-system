# Smart Door System

A smart door system that uses facial recognition to grant or deny access. The system captures an image of the visitor, recognizes the face by comparing it with known faces, logs the visitor's data to Firebase, and controls the door based on recognition results. It also sends notifications regarding access attempts.

# Features
Face Capture: Uses a webcam to capture an image of the visitor.
Face Recognition: Compares the captured image with known faces.
Access Control: Opens the door if the visitor is recognized with high confidence.
Visitor Logging: Logs visitor information to Firebase.
Notifications: Sends notifications about access attempts.

# Prerequisites

## Python 3.6 or higher

**Firebase**
**AWS**
Virtual Environment: Recommended to avoid package conflicts.
pip: Python package installer.

# Python packages
opencv-python
face-recognition
numpy
Pillow
firebase-admin

# System dependancies
CMake
dlib

  - **Installation**
    git clone https://github.com/oliversimiyu/smart-door-system.git
    cd smart-door-system
    - **Set up a virtual environment**:
      ```bash
      python -m venv venv
      ```
    - **activate the virtual environment**:
      ```bash
      venv\Scripts\activate
      source venv/bin/activate for Linux and Mac
      ```

- **Install System Dependencies**

  - **Windows**: Install Visual Studio Build Tools.
  - **Install CMake:**:
    ```bash
    pip install cmake
    ```
  - **Linux**:
    ```
    sudo apt-get install build-essential cmake
    sudo apt-get install libgtk-3-dev
    ```

- **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

**Content of requirement.txt**

  ```bash
opencv-python
face-recognition
numpy
Pillow
firebase-admin
  ```

# Configure firebase
- Create a Firebase project.
- Generate a service account key (serviceAccountKey.json) and place it in the project root directory.
# Set up known Faces
- Place images of known individuals in the known_faces directory.
- Name the images in the format PersonName.jpg.
**Usage**

```bash
python main.py
```

## Process flow
- System Initialization: Sets up the GPIO mode and pin.
- Face Recognition: Compares the captured image with known faces.
- Access Decision:
  If the visitor is recognized with more than 75% similarity, the door opens.
  If not recognized or similarity is low, access is denied.
- Logging and Notifications: Visitor data is logged to Firebase, and notifications are sent.

## Project structure

```bash
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
```
## Contributing
**Contributions are welcome! Please follow these steps:**
- Fork the repository.
- Create a new branch for your feature or bug fix.
- Commit your changes with clear messages.
- Push to your fork and submit a pull request.
**Please ensure all new code includes appropriate tests and documentation**

## License
- This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- face_recognition
- Firebase
- Opencv

## Note
- This project is intended for educational purposes. Ensure compliance with local laws and regulations when using surveillance and facial recognition technologies.
