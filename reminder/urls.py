from reminder.views import ReminderCreateApiView
from django.urls import path

urlpatterns = [

    path('create/', ReminderCreateApiView.as_view(), name='reminder-create')
]
