from rest_framework import serializers

from reminder.models import Reminder
from task.models import Task
from user.serializers import UserSerializer


class TaskCreateSerializer(serializers.ModelSerializer):
    reminder_type = serializers.ChoiceField(choices=Reminder.reminder_type_choices, write_only=True)

    class Meta:
        model = Task
        fields = ('title', 'description', 'priority', 'reminder_type', 'reminder_time',)

    def create(self, validated_data):
        reminder_type = validated_data.pop('reminder_type')
        task = Task.objects.create(**validated_data)
        Reminder.objects.create(
            task=task,
            reminder_time=task.reminder_time,
            user=task.user,
            reminder_type=reminder_type
        )
        return task

    def validate_description(self, attr):
        if len(attr) >= 50:
            raise serializers.ValidationError('description can not be more than 50 characters')
        return attr

    def validate_title(self, attr):
        if len(attr) >= 50:
            raise serializers.ValidationError('title can not be more than 50 characters')
        attr = attr.title()
        return attr


class TaskRetrieveDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'priority', 'is_done', 'reminder_time')


class TaskUpdateSerializer(serializers.ModelSerializer):
    reminder_type = serializers.ChoiceField(choices=Reminder.reminder_type_choices, write_only=True)

    class Meta:
        model = Task
        fields = ('title', 'description', 'priority', 'is_done',  'reminder_type', 'reminder_time',)

    def validate_description(self, attr):
        if len(attr) >= 50:
            raise serializers.ValidationError('description can not be more than 50 characters')
        return attr

    def validate_title(self, attr):
        if len(attr) >= 50:
            raise serializers.ValidationError('title can not be more than 50 characters')
        attr = attr.title()
        return attr


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'priority', 'is_done')


class TaskRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('user', 'title', 'description', 'priority', 'is_done')
