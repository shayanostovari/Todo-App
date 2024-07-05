# reminder/sms.py

from celery import shared_task
from kavenegar import KavenegarAPI
from django.utils import timezone
from reminder.models import Reminder
from todoapp.local_setting import KAVENEGAR_API
import pytz

@shared_task
def send_sms_reminder(reminder_id):
    try:
        reminder = Reminder.objects.get(id=reminder_id)
        tehran_tz = pytz.timezone('Asia/Tehran')
        now = timezone.now().astimezone(tehran_tz)
        if reminder.reminder_time <= now and not reminder.is_sent:
            api = KavenegarAPI(KAVENEGAR_API)
            params = {
                'sender': '1000689696',
                'receptor': reminder.user.phone_number,  # Use the user's phone number
                'message': f'Reminder: {reminder.task.title} - {reminder.task.description}',
            }
            response = api.sms_send(params)
            print(response)
            reminder.is_sent = True
            reminder.save()
    except Reminder.DoesNotExist:
        pass

@shared_task
def check_sms_reminders():
    tehran_tz = pytz.timezone('Asia/Tehran')
    now = timezone.now().astimezone(tehran_tz)
    reminders = Reminder.objects.filter(reminder_time__lte=now, is_sent=False)
    for reminder in reminders:
        if reminder.reminder_type == Reminder.SMS:
            send_sms_reminder.delay(reminder.id)
