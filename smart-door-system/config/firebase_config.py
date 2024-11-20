import firebase_admin
from firebase_admin import credentials, db

# Path to your Firebase service account key
cred = credentials.Certificate("firebase_service_account.json")  # Update this path if necessary
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smart-door-home-2b4a4-default-rtdb.firebaseio.com/'  # Replace with your actual database URL
})
