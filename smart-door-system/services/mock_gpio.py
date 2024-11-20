class GPIO:
    BCM = "BCM"
    OUT = "OUT"

    @staticmethod
    def setmode(mode):
        print(f"Mock: GPIO mode set to {mode}")

    @staticmethod
    def setup(pin, mode):
        print(f"Mock: GPIO pin {pin} set to mode {mode}")

    @staticmethod
    def output(pin, state):
        print(f"Mock: GPIO pin {pin} set to {'HIGH' if state else 'LOW'}")

    @staticmethod
    def cleanup():
        print("Mock: GPIO cleanup called")
