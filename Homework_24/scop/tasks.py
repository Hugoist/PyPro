import csv
from datetime import datetime
from io import StringIO

from celery import shared_task
from django.core.mail import send_mail

from .models import Book, Author, MongoBook, MongoAuthor


@shared_task
def import_books_from_csv(csv_text, user_email):
    f = StringIO(csv_text)
    reader = csv.reader(f, delimiter=',')

    next(reader, None)

    for row in reader:
        if not row or len(row) != 3:
            continue

        title, author_name, published_at = row

        author, _ = Author.objects.get_or_create(name=author_name)

        Book.objects.create(
            title=title,
            author=author,
            published_at=datetime.strptime(published_at, "%Y-%m-%d").date()
        )

    send_mail(
        "Import complete",
        "Books were successfully imported.",
        "noreply@example.com",
        [user_email],
        fail_silently=True,
    )

    return "OK"


@shared_task
def import_books_from_mongo_csv(csv_text, user_email):
    f = StringIO(csv_text)
    reader = csv.reader(f, delimiter=',')

    next(reader, None)

    for row in reader:
        if not row or len(row) != 3:
            continue
        title, author_name, published_at = row

        author = MongoAuthor.objects(name=author_name).first()
        if not author:
            author = MongoAuthor(name=author_name)
            author.save()

        book = MongoBook(
            title=title,
            author=author,
            published_at=datetime.strptime(published_at, "%Y-%m-%d")
        )
        book.save()

    send_mail(
        "Mongo Import Complete",
        "Books were successfully imported to MongoDB.",
        "noreply@example.com",
        [user_email],
        fail_silently=True
    )
    return "OK"
