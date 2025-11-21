from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)


class UpperCaseCharField(models.CharField):
    """Custom CharField that always stores data in uppercase"""
    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        if value:
            return value.upper()
        return value

class Article(models.Model):
    title = UpperCaseCharField(max_length=255)
    content = models.TextField()
    metadata = models.JSONField(default=dict, blank=True)

    def word_count(self):
        return len(self.content.split())

    def __str__(self):
        return self.title


class Tag(models.Model):
    document = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)