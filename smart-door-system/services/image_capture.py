import cv2

def capture_image():
    camera = cv2.VideoCapture(0)
    print("Capturing image...")
    ret, frame = camera.read()
    if ret:
        image_path = "static/visitor_image.jpg"
        cv2.imwrite(image_path, frame)
        print(f"Image saved at {image_path}")
    else:
        print("Failed to capture image.")
        image_path = None
    camera.release()
    return image_path
