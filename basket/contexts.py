"""Context processor avaioable to all templates"""
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):
    """Context func"""

    basket_items = []
    product_count = 0
    total = 0
    delivery = 0
    delivery_threshold = settings.DELIVERY_THRESHOLD

    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)

        total += quantity * product.price

        product_count += quantity

        basket_items.append({
            'product': product,
            'product_description': product.description,
            'product_name': product.name,
            'product_image': product.image,
            'product_rating': product.rating,
            'product_price': product.price,
            'quantity': int(quantity),
            'item_id': item_id,
        })

    if total < delivery_threshold:
        delivery = total * Decimal(settings.DELIVERY_PERCENTAGE / 100)
    else:
        delivery = 0

    grand_total = total + delivery

    context = {
        'basket_items': basket_items,
        'grand_total': grand_total,
        'total': total,
        'delivery': delivery,
        'product_count': product_count,
        'delivery_threshold': delivery_threshold,
    }

    return context
