"""A module to build the product views"""
from django.shortcuts import render, get_object_or_404
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


def product_details(request, product_id):
    """
    A view to return the product details
    """

    product = get_object_or_404(Product, pk=product_id)
    print(all_products)
    context = {
        'product': product,
    }

    return render(request, 'all_products/product_details.html', context)
