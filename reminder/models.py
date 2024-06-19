from django.db import models
from django.contrib.auth import get_user_model
from lib.base_model import BaseModel
from task.models import Task

User = get_user_model()

class Reminder(BaseModel):
    EMAIL = 1
    SMS = 2
    reminder_type = (
        (EMAIL, 'email'),
        (SMS, 'sms')
    )
    reminder_type = models.PositiveSmallIntegerField(choices=reminder_type, default=None)
    time_left = models.TimeField()
    task = models.ForeignKey(Task, on_delete=models.PROTECT, related_name='reminder')
    is_sent = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='tasks')
