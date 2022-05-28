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
from accounts.models import UserAccount
from accounts.forms import UserAccountForm
from .forms import OrderForm
from .models import Order, OrderItem


@require_POST
def cache_checkout_data(request):
    """ cache checlout data """
    try:
        stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.PaymentIntent.modify(pid, metadata={
            'username': request.user,
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, ('Sorry your payment cannot be processed.'))
        return HttpResponse(content=e, status=400)


def checkout(request):
    """ checkout view """

    # grab keys from .env file
    stripe_public_key = os.getenv('STRIPE_PUBLIC_KEY')
    stripe_secret_key = os.getenv('STRIPE_SECRET_KEY')

    media_url = settings.MEDIA_URL

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
            'phone_number': request.POST['phone_number'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_basket = json.dumps(basket)
            order.save()
            for item_id, item_data in basket.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_item = OrderItem(order=order, product=product,
                                           quantity=item_data)
                    order_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag isnt available")
                    )
                    order.delete()
                    return redirect(reverse('view_basket'))

            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_complete',
                                    args=[order.order_number]))
        else:
            messages.error(request, ('There was an error with your form. '
                                     'Please double check your information.'))
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request,
                           "There's nothing in your basket at the moment")
            return redirect(reverse('products'))

    # get basket contents
    current_basket = basket_contents(request)
    # get basket total
    total = current_basket['grand_total']
    # total for stripe
    stripe_total = round(total * 100)
    # gets secret key
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(amount=stripe_total,
                                         currency=settings.STRIPE_CURRENCY)

    if not stripe_public_key:
        messages.warning(request, ('Stripe public key missing'))

    # prefill form details
    if request.user.is_authenticated:
        try:
            account = UserAccount.objects.get(user=request.user)
            order_form = OrderForm(initial={
                'full_name': account.user.get_full_name(),
                'email': account.user.email,
                'address_line_one': account.default_address_line_one,
                'address_line_two': account.default_address_line_two,
                'city': account.default_city,
                'phone_number': account.default_phone_number,
                'county': account.default_county,
                'postcode': account.default_postcode,
                'country': account.default_country,
            })
        except UserAccount.DoesNotExist:
            order_form = OrderForm()
    else:
        order_form = OrderForm()

    # print(account.user)

    # generate context for html
    context = {
        'order_form': order_form,
        'client_secret': intent.client_secret,
        'public_key': stripe_public_key,
        'media_url': media_url
        }
    return render(request, 'checkout/checkout.html', context)


def checkout_complete(request, order_number):
    """Handles a successful checkout"""
    # gets order
    order = get_object_or_404(Order, order_number=order_number)
    # monitors save info check box
    save_info = request.session.get('save_info')

    # is active user?
    if request.user.is_authenticated:
        account = UserAccount.objects.get(user=request.user)

        order.user_account = account
        order.save()

        if save_info:
            account_data = {
                'default_phone_number': order.phone_number,
                'default_address_line_one': order.address_line_one,
                'default_address_line_two': order.address_line_two,
                'default_city': order.city,
                'default_county': order.county,
                'default_postcode': order.postcode,
                'default_country': order.country,
            }
            user_account_form = UserAccountForm(account_data, instance=account)
            if user_account_form.is_valid():
                user_account_form.save()

        messages.success(request, f'{order_number} successfully processed!')

    # deletes basket is one is active
    if 'basket' in request.session:
        del request.session['basket']

    # sets context for html
    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout_complete.html', context)
