""" favourites form """
from django import forms
from .models import ProductFavourite


class ProductFavouriteForm(forms.ModelForm):
    """ favourite product form class """
    class Meta:
        """ meta class """
        model = ProductFavourite
        fields = ('user', 'favourite_category', 'favourite_product',
                  'order_frequency',)
        # exclude = None

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'user': 'User',
            'favourite_category': 'Favourite Category',
            'favourite_product': 'Favourite Product',
            'order_frequency': 'Order Frequency',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
