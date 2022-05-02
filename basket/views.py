"""Basket module views"""
from django.shortcuts import render, redirect


def view_basket(request):
    """renders the basket view of products"""

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """Addaquantity of the specified product to the shopping bag"""

    redirect_url = request.POST.get('redirect_url')

    quantity = int(request.POST.get('quantity'))

    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)
