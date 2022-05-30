"""
products admin module
"""
from django.contrib import admin
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    """ set category name options in admin"""
    list_display = (
        'name',
        'friendly_name',
    )


class ProductAdmin(admin.ModelAdmin):
    """set product metrics for admin"""
    list_display = (
        'name',
        'category',
        'price',
        'sku',
        'rating',
        'image',
    )
    ordering = ('sku',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
