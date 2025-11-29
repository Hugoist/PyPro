from django.conf import settings
from django.urls import path

from .views import login_view, welcome_view, logout_view, books_list_view, start_import_view, task_status_view, \
    books_stats_view, authors_view, mongo_books_list_view

urlpatterns = [
    path('', login_view, name='login'),
    path('welcome/', welcome_view, name='welcome'),
    path('logout/', logout_view, name='logout'),
    path('books_list/', books_list_view, name='books_list'),
    path('import/', start_import_view, name='import'),
    path('task/<str:task_id>/', task_status_view, name='task_status'),
    path('books_stats/', books_stats_view, name='books_stats_view'),
    path('authors/', authors_view, name="authors"),
    path("mongo_books/", mongo_books_list_view, name="mongo_books_list"),
]

if settings.DEBUG:
    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns = [
                      *urlpatterns,
                  ] + debug_toolbar_urls()
