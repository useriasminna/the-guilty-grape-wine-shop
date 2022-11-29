"""
Checkout App - Forms
----------------
Forms for Checkout App.
"""
from django import forms
from .models import Order
from phonenumber_field.formfields import PhoneNumberField


class OrderForm(forms.ModelForm):
    phone_number = PhoneNumberField(region="IE")

    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'country', 'town_or_city', 'county',
                  'postcode', 'street_address1', 'street_address2',
                  )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        self.fields['county'].widget.attrs['readonly'] = True
        self.fields['town_or_city'].widget.attrs['readonly'] = True

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('full_name')
        country = cleaned_data.get('country')
        county = cleaned_data.get('county')
        town_or_city = cleaned_data.get('town_or_city')

        if not all(x.isalpha() or x.isspace() for x in name):
            self._errors["full_name"] = self.error_class(
                ['Invalid format. Only letters and spaces accepted'])
        if country != 'IE':
            self._errors["country"] = self.error_class(
                ['Deliveries only for country Ireland at the moment'])
        if not all(x.isalpha() or x.isspace() for x in county):
            self._errors["county"] = self.error_class(
                ['Invalid format. Only letters and spaces accepted'])
        else:
            if str(county).lower() != 'dublin':
                self._errors["county"] = self.error_class(
                    ['Deliveries only for county Dublin at the moment'])
            else:
                cleaned_data['county'] = 'Dublin'

        if not all(x.isalpha() or x.isspace() for x in town_or_city):
            self._errors["town_or_city"] = self.error_class(
                ['The format is invalid'])
        else:
            if str(town_or_city).lower() != 'dublin':
                self._errors["town_or_city"] = self.error_class(
                    ['Deliveries only for city Dublin at the moment'])
            else:
                cleaned_data['town_or_city'] = 'Dublin'

        return cleaned_data
