from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from .filters import BookFilter
from .models import Book
from .permissions import IsAdminOrReadCreateUpdate
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('-created_at')
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadCreateUpdate]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'author']
    ordering_fields = ['publication_year', 'created_at', 'title']
