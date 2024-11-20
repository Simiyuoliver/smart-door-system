from config.firebase_config import db

def add_initial_data():
    print("Creating reference to 'visitors'...")
    ref = db.reference('visitors')
    print("Reference created:", ref)

    initial_data = {
        "visitor1": {
            "category": "Family",
            "similarity": 95,
            "timestamp": 1690482080
        },
        "visitor2": {
            "category": "Unknown",
            "similarity": 0,
            "timestamp": 1690482080
        }
    }

    print("Adding initial data to Firebase...")
    ref.set(initial_data)
    print("Data added to Firebase successfully.")

def log_visitor(visitor_id, category, similarity, timestamp):
    """
    Logs a new visitor to the Firebase Realtime Database.

    Args:
        visitor_id (str): Unique identifier for the visitor (e.g., 'visitor3').
        category (str): Visitor category (e.g., 'Friend', 'Family', 'Unknown').
        similarity (int): Similarity score.
        timestamp (int): Timestamp of the visit.
    """
    print(f"Logging visitor {visitor_id}...")
    ref = db.reference(f'visitors/{visitor_id}')
    ref.set({
        "category": category,
        "similarity": similarity,
        "timestamp": timestamp
    })
    print(f"Visitor {visitor_id} logged successfully.")
