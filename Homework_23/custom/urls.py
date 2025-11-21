from django.urls import path, include
from rest_framework import routers

from .views import (
    ArticleListView,
    register_view
)
from .views import ArticleViewSet

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='articles')

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('register/', register_view, name='register'),
    path('api/', include(router.urls)),
]
