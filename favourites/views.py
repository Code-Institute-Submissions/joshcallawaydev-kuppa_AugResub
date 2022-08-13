""" add to favourites view """
from django.shortcuts import get_object_or_404, redirect, reverse, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from products.models import Product


@login_required
def favourite_add(request, product_id):
    """
    Add to favs func
    """

    product = get_object_or_404(Product, pk=product_id)
    user = User.objects.get(username=request.user)
    print(user)

    if user in list(product.favourites.all()):
        product.favourites.remove(user)
        messages.success(request, f'{product.name} removed from favourites')
        print('removed')
    else:
        product.favourites.add(user)
        messages.success(request, f'{product.name} added to favourites')
        print('added')

    return redirect(reverse('product_details', args=[product.id]))


@login_required
def favourites(request):
    """ favourites list function """

    user = User.objects.get(username=request.user)
    # get list of products
    products = Product.objects.all()

    # filter products favourites with this user attached
    user_favourites = products.filter(favourites=user)

    # context to be passed to html
    context = {
        "user": user,
        "user_favourites": user_favourites
    }

    return render(request, "favourites.html", context)
