
"""
Products App - Forms
----------------
Forms for Products App
"""
import datetime
from django import forms
from .models import Category, Product
from .widgets import CustomClearableFileInput


class UpdateProductForm(forms.ModelForm):
    """Form for update product details"""

    category = forms.ChoiceField(label="Category", choices=(),
                                 widget=forms.Select(attrs={
                                     'class': 'custom-select custom-select-sm'
                                     }))
    is_deluxe = forms.BooleanField(label='Deluxe Collection', required=False,
                                   widget=forms.CheckboxInput(attrs={
                                     'class': 'custom-control-input'
                                     }))
    sku = forms.CharField(max_length=254)
    name = forms.CharField(max_length=254)
    country = forms.CharField(max_length=100)
    region = forms.CharField(max_length=100)
    grapes = forms.CharField(max_length=254)
    year = forms.IntegerField(max_value=datetime.datetime.now().year)
    style = forms.CharField(max_length=50)
    code = forms.CharField(max_length=6)
    food_pairing = forms.CharField(max_length=254)
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)
    stock = forms.IntegerField(min_value=0)

    def __init__(self, *args, **kwargs):
        is_deluxe = kwargs.pop('is_deluxe', None)
        super().__init__(*args, **kwargs)

        if is_deluxe:
            self.fields['is_deluxe'].initial = True

        choices = [
            (category.get_friendly_name(),
             str(category.get_friendly_name()))
            for category in Category.objects.all()
        ]
        self.fields['category'].choices = choices

    def clean_category(self):
        """Method for assinging the correponding Category object to category
        field"""
        category_name = self.cleaned_data['category']
        category = Category.objects.get(friendly_name=category_name)
        return category

    def clean_is_deluxe(self):
        """Method for assinging boolean value to is_deluxe field depending
        checkbox value"""
        deluxe = self.cleaned_data.get('is_deluxe', False)
        if deluxe:
            is_deluxe = True
        else:
            is_deluxe = False
        return is_deluxe

    class Meta:
        """Override Meta class"""
        model = Product
        fields = ['category', 'is_deluxe', 'sku', 'name', 'country', 'region',
                  'grapes', 'year', 'style', 'code', 'food_pairing', 'price',
                  'image', 'stock']
