from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape


class CustomUser(AbstractUser):
    """Minimal custom user model"""
    # Email should be unique for many projects
    email = models.EmailField(unique=True)

    def save(self, *args, **kwargs):
        self.username = escape(self.username)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
