"""Basket module views"""
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.conf import settings
from django.contrib import messages
from products.models import Product


def view_basket(request):
    """renders the basket view of products"""
    media_url = settings.MEDIA_URL

    context = {
        'media_url': media_url
    }

    return render(request, 'basket/basket.html', context)


def add_to_basket(request, item_id):
    """Addaquantity of the specified product to the shopping bag"""

    redirect_url = request.POST.get('redirect_url')
    item = get_object_or_404(Product, pk=item_id)
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

    basket = request.session['basket']

    try:
        if item in basket:
            basket[item] = quantity
            messages.success(request, f'Quantity updated to {quantity}')
            if basket[item] == 0:
                basket.pop(item)
                messages.info(request, 'Item removed')

    except Exception as e:
        messages.error(
            request, f'{e} occured during your last action for {item}')
        return HttpResponse(status=500)

    request.session['basket'] = basket

    return render(request, 'basket/basket.html')
