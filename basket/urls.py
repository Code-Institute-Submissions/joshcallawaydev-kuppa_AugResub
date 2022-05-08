"""Basket URL Configuration"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_basket, name='view_basket'),
    path('add/<item_id>/', views.add_to_basket, name='add_to_basket'),
    path('change_qty/<item_id>/', views.change_qty, name='change_qty')
]
