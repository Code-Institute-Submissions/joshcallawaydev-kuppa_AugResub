""" account views """
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from checkout.models import Order
from products.models import Product
from .models import UserAccount
from .forms import UserAccountForm


@login_required
def account(request):
    """Display the user's profile."""
    # creates instance of user account
    account = get_object_or_404(UserAccount, user=request.user)
    media_url = settings.MEDIA_URL

    if request.method == "POST":
        form = UserAccountForm(request.POST, instance=account)
        if form.is_valid():
            # save new form deets to profile
            form.save()
            messages.success(request, "account updated successfully")
    else:
        # sets form details
        form = UserAccountForm(instance=account)

    # gets list of orders
    orders = account.orders.all()

    # sets context for html
    context = {
        "orders": orders,
        "account": account,
        "form": form,
        "media_url": media_url,
    }

    return render(request, "account.html", context)


def order_history(request, order_number):
    """order history func"""
    # gets order
    order = get_object_or_404(Order, order_number=order_number)

    # make context available
    context = {
        "order": order,
        "account": True,
    }

    return render(request, "checkout/checkout_complete.html", context)
