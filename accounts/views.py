""" account views """
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from checkout.models import Order
from .models import UserAccount
from .forms import UserAccountForm


def account(request):
    """ Display the user's profile. """
    # creates instance of user account
    account = get_object_or_404(UserAccount, user=request.user)

    if request.method == 'POST':
        form = UserAccountForm(request.POST, instance=account)
        if form.is_valid():
            # save new form deets to profile
            form.save()
            messages.success(request, 'account updated successfully')

    # sets form details
    form = UserAccountForm(instance=account)
    # gets list of orders
    orders = account.orders.all()
    print(orders)

    # sets context for html
    context = {
        'orders': orders,
        'account': account,
        'form': form,
    }

    return render(request, 'account.html', context)

# will develop this in future iterations
# def order_history(request, order_number):
#     """ order history func """
#     # gets order
#     order = get_object_or_404(Order, order_nbr=order_number)

#     # make context available
#     context = {
#         'order': order,
#         'from_account': True,
#     }

#     return render(request, 'checkout/checkout_complete.html', context)
