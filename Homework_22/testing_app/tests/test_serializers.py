from datetime import timedelta

import pytest
from django.contrib.auth.models import User
from django.utils import timezone

from testing_app.models import Task
from testing_app.serializers import TaskSerializer, TaskWithUserSerializer


@pytest.mark.django_db
def test_serializer_valid_data():
    """Check serializer is valid with correct data"""
    data = {
        'title': 'Test Task',
        'description': 'Some description',
        'due_date': timezone.now() + timedelta(days=1),
    }
    serializer = TaskSerializer(data=data)
    assert serializer.is_valid() is True


@pytest.mark.django_db
def test_serializer_missing_title():
    """Check serializer errors if title is missing"""
    data = {
        'title': '',
        'description': 'Serialize task without title',
        'due_date': timezone.now() + timedelta(days=1),
    }
    serializer = TaskSerializer(data=data)
    assert serializer.is_valid() is False
    assert 'title' in serializer.errors


@pytest.mark.django_db
def test_serializer_due_date_in_past():
    """Check serializer custom validation for past due_date"""
    data = {
        'title': 'Past Task',
        'description': 'This due date is past',
        'due_date': timezone.now() - timedelta(days=1),
    }
    serializer = TaskSerializer(data=data)
    assert serializer.is_valid() is False
    assert 'due_date' in serializer.errors


@pytest.mark.django_db
def test_task_with_user_serializer_valid():
    """Valid serializer: nested user should display correctly"""
    user = User.objects.create_user(username='testuser', email='test@test.com')
    task = Task.objects.create(
        title='Task with user',
        description='Some description',
        due_date=timezone.now() + timedelta(days=1),
    )
    task.user = user
    serializer = TaskWithUserSerializer(task)
    data = serializer.data
    assert data['title'] == 'Task with user'
    assert data['user']['id'] == user.id
    assert data['user']['username'] == user.username
    assert data['user']['email'] == user.email


@pytest.mark.django_db
def test_task_with_user_serializer_invalid_user():
    """Invalid serializer if user is missing"""
    task = Task(
        title='Task without user',
        description='Some description',
        due_date=timezone.now() + timedelta(days=1),
    )
    serializer = TaskWithUserSerializer(task)
    data = serializer.data
    assert data.get('user') is None
