from django.urls import path
from .views import register_view, edit_profile_view, change_password_view, profile_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('profile/<str:username>/edit/', edit_profile_view, name='edit_profile'),
    path('profile/<str:username>/change-password/', change_password_view, name='change_password'),
    path('profile/<str:username>/', profile_view, name='profile'),
]
