""" favourites model """
from django.db import models
from django.contrib.auth.models import User
from products.models import Category, Product


class ProductFavourite(models.Model):
    """
    table for building knowledge of customers fav products
    could be used in the future to set up subscriptions
    """

    class OrderFrequency(models.IntegerChoices):
        """ Integer Choices """
        ONE_WEEK = 1
        TWO_WEEK = 2
        THREE_WEEKS = 3
        FOUR_WEEKS = 4

    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    favourite_category = models.ForeignKey(
        Category, null=True, on_delete=models.SET_NULL)
    favourite_product = models.ForeignKey(
        Product, null=True, on_delete=models.SET_NULL)
    order_frequency = models.IntegerField(choices=OrderFrequency.choices)

    def __str__(self):
        return self.user.username
