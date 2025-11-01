from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # main page
    path('categories/', views.categories_list, name='categories_list'),  # all categories
    path('ad/<int:ad_id>/', views.ad_detail, name='ad_detail'),  # page for specific ad
    path('category/<int:category_id>/', views.category_ads, name='category_ads'),  # ads in category
]
