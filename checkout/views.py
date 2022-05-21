""" views"""
import os
import json
import stripe


from django.shortcuts import (
    render, reverse, redirect, get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from basket.contexts import basket_contents
from products.models import Product
from .forms import OrderForm
from .models import Order, OrderItem


# @require_POST
# def cache_checkout_data(request):
#     try:
#         pid = request.POST.get('client_secret').split('_secret')[0]
#         stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
#         stripe.PaymentIntent.modify(pid, metadata={
#             'basket': json.dumps(request.session.get('basket', {})),
#             'save_info': request.POST.get('save_info'),
#             'username': request.user,
#         })
#         return HttpResponse(status=200)
#     except Exception as e:
#         messages.error(request, ('Sorry your payment cannot be processed.'))


def checkout(request):
    """ checkout view """

    # grab keys from .env file
    stripe_public_key = os.getenv('STRIPE_PUBLIC_KEY')
    stripe_secret_key = os.getenv('STRIPE_SECRET_KEY')

    if request.method == 'POST':
        basket = request.session.get('basket', {})
        form_data = {
            'email': request.POST['email'],
            'full_name': request.POST['full_name'],
            'address_line_one': request.POST['address_line_one'],
            'address_line_two': request.POST['address_line_two'],
            'city': request.POST['city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
            'phone_nbr': request.POST['phone_nbr'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_basket = json.dumps(basket)
            order.save()
            for item_id, item_data in basket.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_item = OrderItem(
                            order=order,
                            product=product,
                            quantity=item_data)
                        order_item.save()

                    else:
                        messages.error(request, ("We do not recognise the items in your basket."))

                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag isnt available")
                    )
                    order.delete()
                    return redirect(reverse('view_basket'))

            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_complete',
                                    args=[order.order_nbr]))
        else:
            messages.error(request, ('There was an error with your form. '
                                     'Please double check your information.'))
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request,
                           "There's nothing in your basket at the moment")
            return redirect(reverse('products'))

    current_basket = basket_contents(request)
    total = current_basket['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(amount=stripe_total,
                                         currency=settings.STRIPE_CURRENCY)

    if not stripe_public_key:
        messages.warning(request, ('Stripe public key is missing'))

    order_form = OrderForm()
    # print(intent)

    context = {
        'order_form': order_form,
        'client_secret': intent.client_secret,
        'public_key': stripe_public_key,
        }
    return render(request, 'checkout/checkout.html', context)


def checkout_complete(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_nbr=order_number)
    messages.success(request, f'{order_number} successfully processed! \
                            A confirmation email will be sent to {order.email}.')

    if 'basket' in request.session:
        del request.session['basket']

    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout_complete.html', context)
