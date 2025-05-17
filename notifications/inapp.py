from models import db, Notification
import time

def send_inapp(notification_id):
    notif = Notification.query.get(notification_id)
    try:
        print(f"[IN-APP] Sending: {notif.message}")
        time.sleep(1)
        notif.status = 'sent'
    except:
        notif.status = 'failed'
        notif.retries += 1
    db.session.commit()
