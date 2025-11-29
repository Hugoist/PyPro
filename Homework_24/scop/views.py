from datetime import timedelta

from celery.result import AsyncResult
from django.conf import settings
from django.core.cache import cache
from django.db import connection
from django.db.models import Count, Avg
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from .mongo import *
from .forms import LoginForm
from .models import Book, MongoBook
from .tasks import import_books_from_csv, import_books_from_mongo_csv

SESSION_AGE = settings.SESSION_COOKIE_AGE
COOKIE_AGE = settings.SESSION_COOKIE_AGE


def set_name_cookie(response, name):
    """
    Set or refresh name cookie with expiry
    """
    expires = timezone.now() + timedelta(seconds=COOKIE_AGE)
    response.set_cookie(
        'name',
        name,
        expires=expires,
        httponly=False,
        samesite='Lax'
    )


def login_view(request):
    """
    Show form and on POST store name in cookie and age in session
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']

            # store age in session
            request.session['age'] = age

            # set a test cookie to check cookie support
            response = redirect('welcome')
            response.set_cookie('test_cookie', '1')
            set_name_cookie(response, name)
            return response
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def welcome_view(request):
    """
    Greeting view; checks cookies, extends cookie lifetime on activity,
    and shows message if cookies are disabled
    """
    cookies_supported = True if 'test_cookie' in request.COOKIES else False

    name = request.COOKIES.get('name')
    age = request.session.get('age')

    if not name and not age:
        return redirect('login')

    greeting = f"Привіт, {name}, вам {age} років" if name and age else "Привіт"

    response = render(request, 'welcome.html', {
        'greeting': greeting,
        'cookies_supported': cookies_supported,
    })

    # remove test_cookie if present
    if 'test_cookie' in request.COOKIES:
        response.delete_cookie('test_cookie')

    # Auto-extend name cookie on activity
    if name:
        set_name_cookie(response, name)

    # Extend session expiry on activity
    request.session.set_expiry(SESSION_AGE)

    return response


def logout_view(request):
    """
    Clear session and delete name cookie
    """
    request.session.flush()
    response = redirect('login')
    response.delete_cookie('name')
    return response


def books_list_view(request):
    """
    Display list of books with authors, cached
    """
    cache_key = "books_list"
    books = cache.get(cache_key)

    if books is None:
        books = Book.objects.select_related("author").all()
        cache.set(cache_key, books, timeout=60 * 5)

    return render(request, "books_list.html", {"books": books})


def start_import_view(request):
    if request.method == "POST":
        csv_text = request.FILES['file'].read().decode('utf-8')
        user_email = request.POST['email']
        backend = request.POST.get('backend', 'sql')  # 'sql' или 'mongo'

        if backend == 'mongo':
            task = import_books_from_mongo_csv.delay(csv_text, user_email)
        else:
            task = import_books_from_csv.delay(csv_text, user_email)

        return redirect('task_status', task_id=task.id)

    return render(request, "start_import.html")


def task_status_view(request, task_id):
    res = AsyncResult(task_id)
    return JsonResponse({
        "task_id": task_id,
        "status": res.status,
        "result": res.result
    })


def books_stats_view(request):
    books = Book.objects.annotate(
        review_count=Count('reviews'),
        avg_rating=Avg('reviews__rating')
    ).order_by('-review_count', '-avg_rating')

    return render(request, "books_stats.html", {"books": books})


def authors_view(request):
    """
    Display authors with more than 10 reviews and total book count using raw SQL
    """
    with connection.cursor() as cursor:
        min_reviews = request.GET.get("min_reviews", 10)
        cursor.execute("""
                       SELECT a.id, a.name, COUNT(r.id) as review_count
                       FROM scop_author a
                                JOIN scop_book b ON b.author_id = a.id
                                JOIN scop_review r ON r.book_id = b.id
                       GROUP BY a.id, a.name
                       HAVING COUNT(r.id) > %s
                       """, [min_reviews])
        authors = cursor.fetchall()

        cursor.execute("SELECT COUNT(*) FROM scop_book")
        total_books = cursor.fetchone()[0]

    context = {
        "authors": authors,
        "total_books": total_books,
    }
    return render(request, "authors.html", context)


def mongo_books_list_view(request):
    """
    Display list of books stored in MongoDB with author info
    """
    books = MongoBook.objects.select_related()
    return render(request, "mongo_books_list.html", {"books": books})
