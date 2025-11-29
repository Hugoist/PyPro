import time

from django import db
from django.core.management.base import BaseCommand
from django.db import connection

from scop.models import Book


def reset_queries():
    db.reset_queries()


def run_unoptimized():
    reset_queries()
    start = time.time()

    books = Book.objects.all()
    data = [(book.title, book.author.name, list(book.reviews.all())) for book in books]

    duration = time.time() - start
    sql_count = len(connection.queries)

    return duration, sql_count


def run_optimized():
    reset_queries()
    start = time.time()

    books = Book.objects.select_related("author").prefetch_related("reviews")
    data = [(b.title, b.author.name, list(b.reviews.all())) for b in books]

    duration = time.time() - start
    sql_count = len(connection.queries)

    return duration, sql_count


class Command(BaseCommand):
    help = "Measure ORM performance"

    def handle(self, *args, **kwargs):
        unopt_time, unopt_queries = run_unoptimized()
        opt_time, opt_queries = run_optimized()

        self.stdout.write("\n*** RESULTS ***\n")
        self.stdout.write(f"Unoptimized time: {unopt_time:.4f}s, SQL queries: {unopt_queries}")
        self.stdout.write(f"Optimized time:   {opt_time:.4f}s, SQL queries: {opt_queries}")
