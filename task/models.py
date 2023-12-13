from django.db import models
from django.contrib.auth import get_user_model

from lib.base_model import BaseModel

User = get_user_model()


class Task(BaseModel):
    title = models.TextField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='tasks')
    is_done = models.BooleanField()
