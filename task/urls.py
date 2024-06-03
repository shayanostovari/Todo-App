from django.urls import path

from task.views import TaskCreateApiView, TaskUpdateApiView, TaskListApiView, TaskDeleteApiView, TaskRetrieveApiView

from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import TaskCreateApiView


urlpatterns = [

    path('create/', TaskCreateApiView.as_view(), name='task-create'),
    path('update/<int:pk>/', TaskUpdateApiView.as_view(), name='task-update'),
    path('list/', TaskListApiView.as_view(), name='task-list'),
    path('retrieve/<int:pk>/', TaskRetrieveApiView.as_view(), name='task-retrieve'),
    path('delete/<int:pk>/', TaskDeleteApiView.as_view(), name='task-delete'),

]
