
"""
Products App - Forms
----------------
Forms for Products App
"""
import datetime
from django import forms
from .models import Category, Product
from .widgets import CustomClearableFileInput


class AddUpdateProductForm(forms.ModelForm):
    """Form for update product details"""

    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      empty_label='Category*')
    is_deluxe = forms.BooleanField(label='Deluxe Collection', required=False,
                                   widget=forms.CheckboxInput(attrs={
                                     'class': 'custom-control-input'
                                     }))
    year = forms.IntegerField(max_value=datetime.datetime.now().year)
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Set checkbox default value for update, add placeholders
        and remove auto-generated labels
        """
        is_deluxe = kwargs.pop('is_deluxe', None)
        super().__init__(*args, **kwargs)

        if is_deluxe:
            self.fields['is_deluxe'].initial = True

        placeholders = {
            'sku': 'Sku',
            'name': 'Product Name',
            'region': 'Region',
            'grapes': 'Grapes',
            'year': 'Year',
            'style': 'Style',
            'code': 'Code',
            'food_pairing': 'Food Pairing',
            'price': 'Price',
            'stock': 'Stock',
        }

        for field in self.fields:
            if field != 'country' and field != 'category'\
                 and field != 'is_deluxe' and field != 'image':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder

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
