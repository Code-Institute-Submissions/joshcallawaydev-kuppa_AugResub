"""fav URL Configuration"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.favourites, name='favourites'),
    path('', views.favourite_tracker, name='favourite_tracker'),
]
