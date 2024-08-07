from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todoapp.settings')

app = Celery('todoapp')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'check-reminders-every-minute': {
        'task': 'reminder.email.check_reminders',
        'schedule': crontab(),  # every minute
    },
    'check-sms-reminders-every-minute': {
        'task': 'reminder.sms.check_sms_reminders',
        'schedule': crontab(),  # every minute
    },
}
