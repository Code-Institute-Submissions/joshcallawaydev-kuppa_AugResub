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


def remove_item(request, item_id):
    """remove item from basket"""

    item = item_id
    # print(item)

    basket = request.session['basket']
    # print(basket)

    if item in basket:
        basket[item] -= 1
        if basket[item] == 0:
            basket.pop(item)

    request.session['basket'] = basket

    print(basket)

    return render(request, 'basket/basket.html')
