"""Context processor avaioable to all templates"""
from decimal import Decimal
from django.conf import settings


def basket_contents(request):
    """Context func"""

    basket_items = []
    product_count = 0
    total = 0
    delivery = 0
    delivery_threshold = settings.DELIVERY_THRESHOLD


    if total < delivery_threshold:
        delivery = total * Decimal(settings.DELIVERY_PERCENTAGE / 100)
    else:
        delivery = 0

    grand_total = total + delivery

    # empty dict
    context = {
        'basket_items': basket_items,
        'grand_total': grand_total,
        'total': total,
        'delivery': delivery,
        'product_count': product_count,
        'delivery_threshold': delivery_threshold,
    }

    return context
