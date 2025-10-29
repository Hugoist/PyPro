from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta

from board.models import UserProfile, Category, Ad, Comment

class Command(BaseCommand):
    help = "Run ORM queries for testing"

    def handle(self, *args, **kwargs):
        # 1. All ads for last month
        one_month_ago = timezone.now() - timedelta(days=30)
        ads_last_month = Ad.objects.filter(created_at__gte=one_month_ago)
        self.stdout.write(f"Ads last month: {ads_last_month.count()}")

        # 2. All Ads by category
        category = Category.objects.first()
        if category:
            active_ads_in_category = category.ads.filter(is_active=True)
            self.stdout.write(f"Active ads in category '{category.name}': {active_ads_in_category.count()}")
        else:
            self.stdout.write("No categories found.")

        # 3. Comments amounts for each Ad
        for ad in Ad.objects.all():
            self.stdout.write(f"Ad '{ad.title}' has {ad.comments.count()} comments")

        # 4. All Ads of user
        user = UserProfile.objects.first()
        if user:
            user_ads = user.ads.all()
            self.stdout.write(f"User '{user.user.username}' has {user_ads.count()} ads")
        else:
            self.stdout.write("No users found.")
