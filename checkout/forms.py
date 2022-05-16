""" doc string """
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """ docstring """
    class Meta:
        """ docstring """
        model = Order
        fields = ('email', 'full_name', 'phone_nbr',
                  'address_line_one', 'address_line_two',
                  'city', 'county', 'postcode',
                  'country',)

    def __init__(self, *args, **kwargs):
        """docstring"""
        super().__init__(*args, **kwargs)
        placeholders = {
            'email': 'Email Address',
            'full_name': 'Full Name',
            'phone_nbr': 'Phone Number',
            'address_line_one': 'Street Line 1',
            'address_line_two': 'Street Line 2',
            'city': 'City',
            'county': 'County',
            'postcode': 'Postcode',
            'country': 'Country',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False