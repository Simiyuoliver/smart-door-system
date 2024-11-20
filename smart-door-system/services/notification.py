from firebase_admin import messaging

def send_notification(message):
    notification = messaging.Message(
        notification=messaging.Notification(
            title="Visitor Notification",
            body=message,
        ),
        topic="visitor_alerts"
    )
    response = messaging.send(notification)
    print(f"Notification sent: {response}")
