"""A module to build the product views"""
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """
    A view to return the products page
    """

    categories = None
    query = None
    direction = None
    sort = None

    all_products = Product.objects.all()
    categories = Category.objects.all()
    media_url = settings.MEDIA_URL

    if request.GET:
        if 'sort' in request.GET:
            sort_key = request.GET['sort']
            sort = sort_key
            if sort_key == 'name':
                sort_key = 'lower_name'
                all_products = all_products.annotate(lower_name=Lower('name'))
            if sort_key == 'Category':
                sort_key = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sort_key = f'-{sort_key}'
            all_products = all_products.order_by(sort_key)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            all_products = all_products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please specify a search!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)

            all_products = all_products.filter(queries)

    sorting_choice = f'{sort}_{direction}'

    context = {
        'all_products': all_products,
        'search': query,
        'categories': categories,
        'sorting_choice': sorting_choice,
        'media_url': media_url
    }

    return render(request, 'all_products/all_products.html', context)


def product_details(request, product_id):
    """
    A view to return the product details
    """

    product = get_object_or_404(Product, pk=product_id)
    media_url = settings.MEDIA_URL
    context = {
        'product': product,
        'media_url': media_url
    }

    return render(request, 'all_products/product_details.html', context)


@login_required
def add_product(request):
    """Add product to store"""

    # determine user is super before accessing page
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorised to visit this page.')
        return redirect(reverse('all_products'))

    # grab all the products
    all_products = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'You successfully added a product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(
                request, 'Failed to add product. Please check form.')
    else:
        form = ProductForm()

    # generate context for html page
    media_url = settings.MEDIA_URL

    context = {
        'form': form,
        'all_products': all_products,
        'media_url': media_url
    }

    return render(request, 'all_products/add_product.html', context)


@login_required
def delete_product(request, product_id):
    """ delete a product """

    # determine user is super before accessing page
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorised to visit this page.')
        return redirect(reverse('all_products'))

    # get the product
    product = get_object_or_404(Product, pk=product_id)
    # delete the product
    product.delete()
    messages.success(request, 'Product Deleted')

    return redirect(reverse('add_product'))


@login_required
def edit_product(request, product_id):
    """ edit a product """

    # determine user is super before accessing page
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorised to visit this page.')
        return redirect(reverse('all_products'))

    product = get_object_or_404(Product, pk=product_id)
    media_url = settings.MEDIA_URL

    if request.method == 'POST':
        # populate form
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            # if form valid, save
            form.save()
            messages.success(request, 'Product updated!')
            # redirect to the product
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to update product. Please try again.')
    else:
        form = ProductForm(instance=product)

    # generate context for html
    context = {
        'product': product,
        'media_url': media_url,
        'form': form,
    }

    return render(request, 'all_products/edit_product.html', context)
