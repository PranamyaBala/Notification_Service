from flask import Flask, request, jsonify
from models import db, Notification
from redis import Redis
from rq import Queue
import notifications.email as email_handler
import notifications.sms as sms_handler
import notifications.inapp as inapp_handler

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mypassword@127.0.0.1/notification_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Redis + RQ setup
redis_conn = Redis()
q = Queue(connection=redis_conn)

# Create DB tables on startup
with app.app_context():
    db.create_all()

@app.route('/notifications', methods=['POST'])
def send_notification():
    data = request.json
    notif = Notification(user_id=data['user_id'], message=data['message'], type=data['type'])
    db.session.add(notif)
    db.session.commit()

    # Enqueue to background worker
    if notif.type == 'email':
        q.enqueue(email_handler.send_email, notif.id)
    elif notif.type == 'sms':
        q.enqueue(sms_handler.send_sms, notif.id)
    else:
        q.enqueue(inapp_handler.send_inapp, notif.id)

    return jsonify({'message': 'Notification queued.'}), 201

@app.route('/users/<int:user_id>/notifications', methods=['GET'])
def get_notifications(user_id):
    notifs = Notification.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'id': n.id,
        'message': n.message,
        'type': n.type,
        'status': n.status
    } for n in notifs])

@app.route('/')
def home():
    return "Hello! Your app is working."


if __name__ == '__main__':
    app.run(debug=True)
