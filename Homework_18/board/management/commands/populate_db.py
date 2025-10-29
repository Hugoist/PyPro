from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from board.models import UserProfile, Category, Ad, Comment
import random

class Command(BaseCommand):
    help = "Populate the database with test data"

    def handle(self, *args, **options):
        # create user
        user_obj = User.objects.get_or_create(username='testuser', defaults={'email': 'test@test.com'})
        user_profile = UserProfile.objects.get_or_create(user=user_obj, defaults={'phone': '123456789', 'address': 'Some address'})

        # create categories
        categories = []
        for i in range(3):
            cat = Category.objects.get_or_create(
                name=f'Category {i+1}',
                defaults={'description': f'Description for category {i+1}'}
            )
            categories.append(cat)

        # create ads
        ads = []
        for i in range(5):
            ad = Ad.objects.create(
                title=f'Ad {i+1}',
                description=f'Description for ad {i+1}',
                price=random.uniform(10, 100),
                user=user_profile,
                category=random.choice(categories)
            )
            ads.append(ad)

        # create comments
        for ad in ads:
            for j in range(2):
                Comment.objects.create(
                    content=f'Comment {j+1} for {ad.title}',
                    ad=ad,
                    user=user_profile
                )

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
