"""Basket module views"""
from django.shortcuts import render


def view_basket(request):
    """renders the basket view of products"""

    return render(request, 'basket/basket.html')