"""A module to build the views"""
from django.shortcuts import render


def index(request):
    """A view to return the index page"""

    return render(request, 'home/index.html')


def terms_of_server(request):
    """ a page for the site terms of service"""
    return render(request, 'home/terms_of_server.html')


def privacy_policy(request):
    """link to privacy policy"""
    return render(request, 'home/privacy_policy.html')
