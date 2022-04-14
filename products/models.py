"""
Models docstring
"""
from django.db import models

# Create your models here.


class Category(models.Model):
    """
    categories class
    """
    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)

    def str_(self):
        """
        returns name from class
        """
        return self.name

    def get_friendly_name(self):
        """
        returns name from class
        """
        return self.friendly_name


class Product(models.Model):
    """
    products class
    """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1035, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def _str_(self):
        """gets name from class"""
        return self.name
