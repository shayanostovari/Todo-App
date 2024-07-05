# email.py
from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from reminder.models import Reminder
import pytz

@shared_task
def send_reminder_email(reminder_id):
    try:
        reminder = Reminder.objects.get(id=reminder_id)
        tehran_tz = pytz.timezone('Asia/Tehran')
        now = timezone.now().astimezone(tehran_tz)
        if reminder.reminder_time <= now and not reminder.is_sent:
            send_mail(
                subject=f'Reminder: {reminder.task.title}',
                message=reminder.task.description,
                from_email='shayan.work.python@gmail.com',
                recipient_list=[reminder.user.email],
                fail_silently=False,
            )
            reminder.is_sent = True
            reminder.save()
    except Reminder.DoesNotExist:
        pass

@shared_task
def check_reminders():
    tehran_tz = pytz.timezone('Asia/Tehran')
    now = timezone.now().astimezone(tehran_tz)
    reminders = Reminder.objects.filter(reminder_time__lte=now, is_sent=False)
    for reminder in reminders:
        send_reminder_email.delay(reminder.id)
