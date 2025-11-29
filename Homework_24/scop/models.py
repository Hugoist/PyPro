from django.core.cache import cache
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from mongoengine import Document, StringField, ReferenceField, DateTimeField


class Author(models.Model):
    """
    Author of books
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book written by an author
    """
    title = models.CharField(max_length=300)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    published_at = models.DateField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['published_at']),
        ]

    def __str__(self):
        return self.title


class Review(models.Model):
    """
    Review for a book with integer rating 1..5
    """
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['rating']),
        ]


@receiver([post_save, post_delete], sender=Book)
def clear_books_list_cache(sender, **kwargs):
    """
    Clear cached book list when a Book is added, updated or deleted
    """
    cache.delete("books_list")


class MongoAuthor(Document):
    name = StringField(required=True, unique=True)


class MongoBook(Document):
    title = StringField(required=True)
    author = ReferenceField(MongoAuthor)
    published_at = DateTimeField()
