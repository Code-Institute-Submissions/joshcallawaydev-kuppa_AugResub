""" add to favourites view """
from django.shortcuts import (get_object_or_404,
                              redirect, reverse, render)
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from products.models import Product
from .forms import ProductFavouriteForm
from .models import ProductFavourite


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

    media_url = settings.MEDIA_URL

    user = User.objects.get(username=request.user)
    print(user)
    # get list of products
    products = Product.objects.all()

    # filter products favourites with this user attached
    user_favourites = products.filter(favourites=user)

    try:
        data = ProductFavourite.objects.get(user=user)
        if request.method == 'POST':
            form = ProductFavouriteForm(request.POST, instance=data)
            if form.is_valid():
                # save new form deets to profile
                form.save()
                messages.success(
                    request, "Favourites updated successfully")
        else:
            # sets form details
            form = ProductFavouriteForm(instance=data)
    except ProductFavourite.DoesNotExist:
        data = ProductFavourite.objects.create(user=user)
        form = ProductFavouriteForm(instance=data)

    # context to be passed to html
    context = {
        "user": user,
        "media_url": media_url,
        "form": form,
        "user_favourites": user_favourites
    }

    return render(request, "favourites.html", context)
