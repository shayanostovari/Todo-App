from django.db import models
from django.contrib.auth import get_user_model

from lib.base_model import BaseModel

User = get_user_model()


class Task(BaseModel):
    HIGH = 1
    MIDDLE = 2
    LOW = 3
    priority_level = (
        (HIGH, 'high'),
        (MIDDLE, 'middle'),
        (LOW, 'low'),
    )

    title = models.TextField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='tasks')
    is_done = models.BooleanField(default=False)
    priority = models.PositiveSmallIntegerField(choices=priority_level, default=MIDDLE)
    reminder_time = models.DateTimeField(null=True, blank=True)
