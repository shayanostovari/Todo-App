from rest_framework import serializers
from task.models import Task
from user.serializers import UserSerializer


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'priority', 'reminder_time')

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
    class Meta:
        model = Task
        fields = ('title', 'description', 'priority', 'is_done', 'reminder_time')

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
