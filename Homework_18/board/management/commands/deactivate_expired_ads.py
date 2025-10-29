from datetime import timedelta

from django.core.management import BaseCommand
from django.utils import timezone

from ...models import Ad


class Command(BaseCommand):
    help = 'Deactivate expired ads'

    def handle(self, *args, **options):
        """Deactivate all ads older than 30 days"""

        now = timezone.now()
        expired_ads = list(
            Ad
            .objects
            .filter(created_at__lt=now - timedelta(days=30))
            .only('id', 'is_active', 'updated_at')
        )

        count = 0
        for ad in expired_ads:
            ad.set_expired()
            count += 1

        Ad.objects.bulk_update(expired_ads, ['is_active', 'updated_at'])

        self.stdout.write(self.style.SUCCESS(f"Deactivated {count} expired ads"))
