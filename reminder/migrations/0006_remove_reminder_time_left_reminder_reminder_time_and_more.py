# Generated by Django 4.2 on 2024-07-04 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0006_task_reminder_time'),
        ('reminder', '0005_remove_reminder_reminder_time_reminder_time_left_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reminder',
            name='time_left',
        ),
        migrations.AddField(
            model_name='reminder',
            name='reminder_time',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reminder',
            name='reminder_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'email'), (2, 'sms')], default=1),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reminders', to='task.task'),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='reminders', to=settings.AUTH_USER_MODEL),
        ),
    ]
