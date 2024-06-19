from rest_framework import serializers
from reminder.models import Reminder


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ('user', 'reminder_type', 'time_left', 'task', 'is_sent')
