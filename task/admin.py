from django.contrib import admin
from task.models import Task
from reminder.models import Reminder


class ReminderInline(admin.TabularInline):
    model = Reminder
    extra = 1


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'user', 'is_done', 'priority', 'reminder_time')
    list_filter = ('priority', 'is_done', 'reminder_time')
    search_fields = ('title', 'description', 'user__username')
    inlines = [ReminderInline]


admin.site.register(Task, TaskAdmin)
