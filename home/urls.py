"""home URL Configuration"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('terms/', views.terms_of_server, name='terms_of_server'),
    path('privacy/', views.privacy_policy, name='privacy_policy')
]
