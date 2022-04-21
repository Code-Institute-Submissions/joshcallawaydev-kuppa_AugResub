"""A module to build the product views"""
from django.shortcuts import render
from .models import Product


def all_products(request):
    """
    A view to return the products page
    """

    all_products = Product.objects.all()
    print(all_products)
    context = {
        'all_products': all_products,
    }

    return render(request, 'all_products/all_products.html', context)
