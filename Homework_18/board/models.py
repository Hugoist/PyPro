from django.db import models
from django.contrib.auth.models import User

from .validators import validate_positive_float


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    address = models.TextField(max_length=255)


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    def active_ads_count(self):
        """Get amount of active ads in category"""
        return self.ads.filter(is_active=True).count()


class Ad(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, validators=[validate_positive_float])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='ads')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='ads')

    def short_description(self):
        """show first 100 characters of description"""
        return self.description[:100] + ("..." if len(self.description) > 100 else "")

    def set_expired(self, update=True):
        self.is_active = False

        if update:
            self.save()

    def comments_count(self):
        """ get amount of comments for the Ad """
        return self.ads.count()


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
