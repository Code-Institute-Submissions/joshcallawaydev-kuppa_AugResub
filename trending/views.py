""" Module for trending products """
from django.shortcuts import render


def trending(request):
    """ function to show trending products"""

    # context to be passed to html
    context = {}

    return render(request, "trending.html", context)
