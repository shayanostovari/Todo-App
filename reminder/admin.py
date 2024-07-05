from django.contrib import admin
from reminder.models import Reminder


class ReminderAdmin(admin.ModelAdmin):
    list_display = ('reminder_type', 'reminder_time', 'task', 'is_sent', 'user')
    list_filter = ('reminder_type', 'is_sent', 'reminder_time')
    search_fields = ('task__title', 'user__username')


admin.site.register(Reminder, ReminderAdmin)
