from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import UserProfile


class RegistrationForm(forms.ModelForm):
    """Form for registering a new user."""
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_username(self):
        """Clean username if already exists"""
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("Користувач з таким іменем вже існує")
        return username

    def clean_email(self):
        """Clean user email if already exists"""
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Користувач з таким email вже існує")

    def clean(self):
        """Clean password and confirm password if they aren't same"""
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise ValidationError("Паролі не співпадають")
        return cleaned_data


class UserProfileForm(forms.ModelForm):
    """Form for editing user profile"""

    class Meta:
        model = UserProfile
        fields = ['bio', 'birth_date', 'location']
        widgets = {
            "bio": forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            "birth_date": forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            "location": forms.TextInput(attrs={'class': 'form-control'}),
        }


class CustomPasswordChangeForm(PasswordChangeForm):
    """Form for changing user password"""
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap class to all visible fields
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
