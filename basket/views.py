"""Basket module views"""
from django.shortcuts import render, redirect
from django.contrib import messages
from products.models import Product


def view_basket(request):
    """renders the basket view of products"""

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """Addaquantity of the specified product to the shopping bag"""

    redirect_url = request.POST.get('redirect_url')
    item = Product.objects.get(id=item_id)
    quantity = int(request.POST.get('quantity'))

    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request, f'{quantity} {item.name} added successfully')
    else:
        basket[item_id] = quantity
        messages.success(request, f'{quantity} {item.name} added successfully')

    request.session['basket'] = basket
    return redirect(redirect_url)


def change_qty(request, item_id):
    """remove item from basket"""

    item = item_id
    quantity = int(request.POST.get('quantity'))
    print(item)
    print(quantity)

    basket = request.session['basket']
    # print(basket)

    if item in basket:
        basket[item] = quantity
        messages.success(request, f'Quantity updated to {quantity}')
        if basket[item] == 0:
            basket.pop(item)
            messages.info(request, 'Item removed')

    request.session['basket'] = basket

    print(basket)

    return render(request, 'basket/basket.html')
