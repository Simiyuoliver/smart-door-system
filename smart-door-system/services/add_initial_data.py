import sys
import os

# Ensure the parent directory is in the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.firebase_logger import add_initial_data

# Add debug message
print("Running add_initial_data.py...")

# Call the function to add initial data
add_initial_data()

print("Script execution completed.")
