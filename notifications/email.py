from models import db, Notification
import time

def send_email(notification_id):
    notif = Notification.query.get(notification_id)
    try:
        print(f"Sending EMAIL: {notif.message}")
        time.sleep(2)
        notif.status = 'sent'
    except:
        notif.status = 'failed'
        notif.retries += 1
    db.session.commit()
