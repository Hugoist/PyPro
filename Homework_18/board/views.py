from django.shortcuts import render, get_object_or_404
from .models import Ad, Category


def index(request):
    """Show all active ads"""
    ads = Ad.objects.filter(is_active=True)
    return render(request, 'index.html', {'ads': ads})


def ad_detail(request, ad_id):
    """Show a single ad with its comments"""
    ad = get_object_or_404(Ad, id=ad_id)
    comments = ad.comments.all()
    return render(request, 'ad_detail.html', {'ad': ad, 'comments': comments})


def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'categories_list.html', {'categories': categories})


def category_ads(request, category_id):
    """Show all active ads in a category"""
    category = get_object_or_404(Category, id=category_id)
    ads = category.ads.filter(is_active=True)
    return render(request, 'category_ads.html', {'category': category, 'ads': ads})
