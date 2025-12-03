import secrets

from django.contrib.auth.models import User
from django.db import models


class UserToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="token")
    key = models.CharField(max_length=40, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = secrets.token_hex(20)
        super().save(*args, **kwargs)
