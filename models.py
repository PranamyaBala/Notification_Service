from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    message = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # 'email', 'sms', 'inapp'
    status = db.Column(db.String(50), default='pending')  # 'sent', 'failed', etc.
    retries = db.Column(db.Integer, default=0)
