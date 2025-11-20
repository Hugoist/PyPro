from django import forms
from django.utils import timezone

from .models import Task


class TaskForm(forms.ModelForm):
    """Form for creating/updating Task with due_date validation"""

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']

    def clean_due_date(self):
        """Validate that due_date is not in the past"""

        due = self.cleaned_data.get('due_date')
        # If due is None, other validators will catch it if field required
        if due and due < timezone.now():
            raise forms.ValidationError('due date cannot be in the past')
        return due
