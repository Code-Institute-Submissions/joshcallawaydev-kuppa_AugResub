"""product for view"""
from django import forms
from .models import Category, Product


class ProductForm(forms.ModelForm):
    """ a product form """
    class Meta:
        """another docstring"""
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """init method"""
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
