from django.contrib import admin
from task.models import Task
from django.contrib.admin import register


@register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'title', 'description', 'is_done', 'priority', 'reminder_time')
    list_filter = ('is_done', 'priority')
