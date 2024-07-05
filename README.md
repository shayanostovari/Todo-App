# Task Reminder App

This project is a Django-based task reminder application that allows users to create tasks and set reminders. Users can receive reminders via email or SMS based on their preferences. The application uses Celery for task scheduling and asynchronous task execution.

## Features

- User authentication and task management.
- Create, update, and delete tasks.
- Set reminders for tasks with email or SMS notifications.
- Scheduled reminders using Celery and Django Celery Beat.
- Admin panel to manage tasks and reminders.

## Technologies Used

- Django: Backend framework.
- Django REST Framework: API creation.
- Celery: Asynchronous task queue.
- Django Celery Beat: Periodic task scheduling.
- Redis: Broker and backend for Celery.
- Kavenegar API: SMS sending service.
- SMTP: Email sending service.

## Installation

### Prerequisites

- Python 3.8+
- Django 3.2+
- Redis server

### Steps

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/task-reminder-app.git
    cd task-reminder-app
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

### Setting up Celery

1. Start Redis server:
    ```sh
    redis-server
    ```

2. Start Celery worker:
    ```sh
    celery -A task_reminder_app worker --loglevel=info
    ```

3. Start Celery Beat:
    ```sh
    celery -A task_reminder_app beat --loglevel=info
    ```

### Environment Variables

Create a `.env` file in the project root and add the following variables:

```env
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost, 127.0.0.1

# Email settings
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_email_password

# Kavenegar API Key
KAVENEGAR_API=your_kavenegar_api_key

# Celery settings
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
