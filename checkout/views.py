""" views"""
from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    """ checkout view """

    basket = request.session.get('basket', {})
    print(basket)

    if not basket:
        messages.error(request, "There's nothing in your basket")
        return redirect(reverse('basket'))

    order_form = OrderForm()
    print(order_form)

    context = {'order_form': order_form}
    return render(request, 'checkout/checkout.html', context)
