""" add to favourites view """
from django.shortcuts import (get_object_or_404,
                              redirect, reverse, render, HttpResponse)
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

    username = User.objects.get(username=request.user)
    user = username
    # get list of products
    products = Product.objects.all()

    # filter products favourites with this user attached
    user_favourites = products.filter(favourites=user)

    get_all = ProductFavourite.objects.all()
    my_data = get_all.filter(user=username)
    print(my_data)

    if my_data.count() > 0:
        data = get_object_or_404(ProductFavourite, user=request.user)
        if request.method == "POST":
            form = ProductFavouriteForm(request.POST, instance=data)
            if form.is_valid():
                # save new form deets to profile
                form.save()
                messages.success(request, "Favourites updated successfully")
        else:
            # sets form details
            form = ProductFavouriteForm(instance=data)
    else:
        form = ProductFavouriteForm()

    # context to be passed to html
    context = {
        "user": user,
        "media_url": media_url,
        "form": form,
        "user_favourites": user_favourites
    }

    return render(request, "favourites.html", context)


# @login_required
# def favourite_tracker(request):
#     """ html form for tracking a customers favourite product """

#     print(" ******** this is a test ********")

#     media_url = settings.MEDIA_URL
#     # account = get_object_or_404(ProductFavourite)
#     account = ProductFavourite.objects.get()

#     try:
#         if request.method == "POST":
#             # post form details, populated in the html
#             form = ProductFavouriteForm(request.POST, instance=account)
#             print("you are here, in the of of the post request code")
#             # check ofrm is valid and accurate
#             if form.is_valid():
#                 # save form
#                 form.save()
#                 messages.success(request, "Form submitted")
#             else:
#                 messages.error(request, "Failed to submit form")
#         else:
#             # generates form
#             form = ProductFavouriteForm(instance=account)
#             print("you are actually here, the else statement")
#     except Exception as e:
#         messages.error(
#             request, f'{e} occured')
#         return HttpResponse(status=500)

#     context = {
#         "media_url": media_url,
#         "account": account,
#         "form": form,
#     }

    # return render(request, "favourites.html", context)
