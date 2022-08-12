"""home URL Configuration"""

from django.urls import path
from favourites import views as fav_views
from . import views


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>', views.product_details, name='product_details'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>',
         views.delete_product, name='delete_product'),
    path('fav/<int:product_id>',
         fav_views.favourite_add, name='favourite_add'),
]
