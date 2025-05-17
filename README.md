# Notification Service

A simple notification service built with Flask that supports sending notifications via Email, SMS, and In-App. The service uses a Redis-backed queue (RQ) for asynchronous processing of notifications, including retries on failure.

---

1. Features

- **API Endpoints**:
  - `POST /notifications` — Send a notification (Email, SMS, or In-App)
  - `GET /users/{id}/notifications` — Get all notifications for a user

- **Notification Types**:
  - Email
  - SMS
  - In-App

- **Queue & Worker**:
  - Uses Redis and RQ (Redis Queue) to handle notifications asynchronously
  - Worker script processes notifications and updates their status
  - Retry mechanism for failed notifications (can be extended)

---

2. Getting Started

- **Prerequisites**
    - Python 3.8+
    - Redis Server (running locally or remotely)
    - pip (Python package manager)


3. Setup Instructions
    - **Clone the repository**
    - **Install dependencies**
        pip install -r requirements.txt
    - Start Redis server (make sure Redis is installed and running).
    - Run the Flask application: python app.py
    - In another terminal, start the worker to process notifications: python queue_worker.py

4. API Endpoints
    - Send Notification
        POST /notifications
        Body (JSON):
        {
            "user_id": 1,
            "type": "email",
            "message": "Your notification message"
        }
    - Get User Notifications: GET /users/{id}/notifications