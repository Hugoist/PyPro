import django_filters

from .models import Book


class BookFilter(django_filters.FilterSet):
    author = django_filters.CharFilter(field_name='author', lookup_expr='iexact')
    genre = django_filters.CharFilter(field_name='genre', lookup_expr='iexact')
    publication_year = django_filters.NumberFilter(field_name='publication_year')
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['author', 'genre', 'publication_year', 'title']
