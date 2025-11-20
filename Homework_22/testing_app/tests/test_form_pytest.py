from datetime import timedelta

import pytest
from django.utils import timezone

from testing_app.forms import TaskForm


@pytest.mark.django_db
class TestTaskForm:

    def test_valid_data(self):
        """Form is valid with correct data"""
        data = {
            'title': 'Test task',
            'description': 'Some description',
            'due_date': timezone.now() + timedelta(days=1),
        }
        form = TaskForm(data=data)
        assert form.is_valid() is True

    def test_missing_required_field(self):
        """Missing title should produce errors"""
        data = {
            'title': '',
            'description': 'Task without title',
            'due_date': timezone.now() + timedelta(days=1),
        }
        form = TaskForm(data=data)
        assert form.is_valid() is False
        assert 'title' in form.errors

    def test_due_date_in_past(self):
        """due_date in the past should be invalid"""
        data = {
            'title': 'Past task',
            'description': 'This due date is past',
            'due_date': timezone.now() - timedelta(days=1),
        }
        form = TaskForm(data=data)
        assert form.is_valid() is False
        errors = form.errors.get('due_date')
        assert errors is not None
        assert any('past' in str(e) for e in errors)
