# views.py
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from task.models import Task
from task.serializers import TaskCreateSerializer, TaskUpdateSerializer, TaskListSerializer, TaskRetrieveDeleteSerializer, TaskRetrieveSerializer
from reminder.email import send_reminder_email
from reminder.models import Reminder

class TaskCreateApiView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        task = serializer.save(user=self.request.user)
        if task.reminder_time:
            # Create Reminder
            Reminder.objects.create(task=task, reminder_time=task.reminder_time, user=task.user)
            # Schedule reminder email
            send_reminder_email.apply_async((task.id,), eta=task.reminder_time)

class TaskListApiView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class TaskRetrieveApiView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskRetrieveSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class TaskUpdateApiView(RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskUpdateSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def perform_update(self, serializer):
        task = serializer.save()
        if task.reminder_time:
            # Update or Create Reminder
            reminder, created = Reminder.objects.update_or_create(
                task=task,
                defaults={'reminder_time': task.reminder_time, 'user': task.user}
            )
            # Schedule reminder email
            send_reminder_email.apply_async((task.id,), eta=task.reminder_time)

class TaskDeleteApiView(RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskRetrieveDeleteSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def perform_destroy(self, instance):
        # Delete associated reminders
        Reminder.objects.filter(task=instance).delete()
        super().perform_destroy(instance)
