from django.db import connection
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Article


@receiver(post_save, sender=Article)
def post_save_article(sender, instance, **kwargs):
    print(f"Article '{instance.title}' saved!")
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM custom_article")
        row = cursor.fetchone()
        print("Total articles:", row[0])
