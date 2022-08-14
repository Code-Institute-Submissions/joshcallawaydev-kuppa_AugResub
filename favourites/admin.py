from django.contrib import admin
from .models import ProductFavourite


class FavouritesAdmin(admin.ModelAdmin):
    """set field names and display in admin dashboard"""
    list_display = (
        'user',
        'favourite_category',
        'favourite_product',
        'order_frequency',
    )


admin.site.register(ProductFavourite, FavouritesAdmin)
