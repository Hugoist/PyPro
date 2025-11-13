from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView
from rest_framework.authtoken import views as drf_auth_views
from rest_framework.routers import DefaultRouter

from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-token-auth/', drf_auth_views.obtain_auth_token),
    path('docs/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularAPIView.as_view(), name='swagger-ui')
]
