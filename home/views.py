"""A module to build the views"""
from django.shortcuts import render


def index(request):
    """A view to return the index page"""

    return render(request, 'home/index.html')
