"""trending URL Configuration"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.trending, name='trending'),
]
