"""fav URL Configuration"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.favourites, name='favourites'),
    # path('tracker/', views.favourite_tracker, name='favourite_tracker'),
]
