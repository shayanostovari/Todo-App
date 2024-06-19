from rest_framework.generics import ListAPIView, CreateAPIView

from reminder.models import Reminder
from reminder.serializers import ReminderSerializer


class ReminderCreateApiView(CreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
