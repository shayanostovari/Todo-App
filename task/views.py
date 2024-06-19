from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, UpdateAPIView, RetrieveUpdateAPIView, \
    RetrieveAPIView, DestroyAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from lib.permissions import SelfUserPermission
from task.models import Task
from task.serializers import TaskCreateSerializer, TaskUpdateSerializer, TaskListSerializer, \
    TaskRetrieveDeleteSerializer, TaskRetrieveSerializer


class TaskCreateApiView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskListApiView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated, SelfUserPermission)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)


class TaskRetrieveApiView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskRetrieveSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)


class TaskUpdateApiView(RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class TaskDeleteApiView(RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskRetrieveDeleteSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)
