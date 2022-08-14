""" Module for trending products """
from django.shortcuts import render
from products.models import Product


def trending(request):
    """ function to show trending products"""

    products = Product.objects.all()
    item = {}
    all_products = []
    trending_products = []

    for product in products:
        item["id"] = product.pk
        item["name"] = product.name
        item["category"] = product.category
        item["description"] = product.description
        item["image"] = product.image
        item["image_url"] = product.image_url
        item["price"] = product.price
        item["rating"] = product.rating
        item["sku"] = product.sku
        item["value"] = product.favourites.count()
        all_products.append(item.copy())

    for each_item in all_products:
        if each_item["value"] > 0:
            trending_products.append(each_item.copy())

    # context to be passed to html
    context = {
        "all_products": all_products,
        "trending_products": trending_products,
    }

    return render(request, "trending.html", context)
