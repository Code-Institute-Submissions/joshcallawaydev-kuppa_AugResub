"""A module to build the product views"""
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
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
                    sort_key = '-{0}'.format(sort_key)
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

            queries = Q(name__icontains=query) | Q(description__icontains=query)

            all_products = all_products.filter(queries)

    # print(all_products)

    sorting_choice = '{0}_{1}'.format(sort, direction)

    context = {
        'all_products': all_products,
        'search': query,
        'categories': categories,
        "sorting_choice": sorting_choice
    }

    return render(request, 'all_products/all_products.html', context)


def product_details(request, product_id):
    """
    A view to return the product details
    """

    product = get_object_or_404(Product, pk=product_id)
    # print(product)
    context = {
        'product': product,
    }

    return render(request, 'all_products/product_details.html', context)


def add_product(request):
    """Add product to store"""
    # grab all the products
    all_products = Product.objects.all()
    # store product form in form var
    form = ProductForm()
    # generate context for html page
    context = {
        'form': form,
        'all_products': all_products
    }

    return render(request, 'all_products/add_product.html', context)
