try:
    import RPi.GPIO as GPIO
except ImportError:
    from services.mock_gpio import GPIO

# GPIO Configuration
DOOR_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(DOOR_PIN, GPIO.OUT)

def open_door():
    GPIO.output(DOOR_PIN, GPIO.HIGH)
    print("Door is opened.")
    time.sleep(5)  # Simulate door open duration
    GPIO.output(DOOR_PIN, GPIO.LOW)
    print("Door is closed.")
