from django.db import models
from django.contrib.auth.models import User


class BookGenre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    genres = models.ManyToManyField(BookGenre, blank=True)
    authors = models.ManyToManyField(Author)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    available_copies = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title


class Rental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rented_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ("user", "book", "returned_at")
