from django.urls import path, re_path
from . import views

urlpatterns = [
    path('home/', views.home_view),
    path('about/', views.about_view),
    path('contact/', views.contact_view),
    re_path(r'^post/(?P<id>[0-9]+)/$', views.post_view),
    re_path(r'^profile/(?P<username>[A-Za-z]+)/$', views.profile_view),
    re_path(r'^event/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.event_view),
]
