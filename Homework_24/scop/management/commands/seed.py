from django.core.management.base import BaseCommand
from scop.models import Author, Book, Review
import random

class Command(BaseCommand):
    help = "Seed DB with authors, books and reviews"

    def handle(self, *args, **options):
        authors = []
        for i in range(10):
            a = Author.objects.create(name=f"Author {i+1}")
            authors.append(a)

        books = []
        for a in authors:
            n_books = random.randint(1, 5)
            for j in range(n_books):
                b = Book.objects.create(title=f"Book {a.name} #{j+1}", author=a)
                books.append(b)

        for b in books:
            n_rev = random.randint(1, 5)
            for _ in range(n_rev):
                Review.objects.create(
                    book=b,
                    rating=random.randint(1, 5),
                    text="Review text"
                )

        self.stdout.write(self.style.SUCCESS("Seeding completed"))
