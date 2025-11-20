from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']

    def validate_due_date(self, value):
        """Due date cannot be in the past"""
        if value < timezone.now():
            raise serializers.ValidationError('due date cannot be in the past')
        return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class TaskWithUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # nested serializer, read-only

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'user']

    def validate_due_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Due date cannot be in the past")
        return value
