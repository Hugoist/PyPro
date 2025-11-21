from django.shortcuts import render, redirect
from django.views.generic import ListView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .forms import CustomUserCreationForm
from .models import Article
from .permissions import IsAdminOrReadOnly
from .serializers import ArticleSerializer


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = "articles"


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminOrReadOnly]

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = [
        'title',  # ?title=HELLO
        'metadata',  # ?metadata__contains={"key":"value"}
        'tag__name',  # ?tag__name=python
    ]
    search_fields = ['title', 'content']
