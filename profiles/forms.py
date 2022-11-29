"""
Profiles App - Forms
----------------
Forms for Profiles App.
"""
from django.forms import ModelForm
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from datetime import date
from .models import UserProfile


class UserProfileForm(ModelForm):
    default_phone_number = PhoneNumberField(region="IE", required=False)

    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, set delivery fields to readonly,
        remove auto-generated labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_county'].widget.attrs['readonly'] = True
        self.fields['default_town_or_city'].widget.attrs['readonly'] = True

        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False

    def clean(self):
        """Add validation"""
        cleaned_data = super().clean()
        country = cleaned_data.get('default_country')
        county = cleaned_data.get('default_county')
        town_or_city = cleaned_data.get('default_town_or_city')

        if country != 'IE':
            self._errors["default_country"] = self.error_class(
                ['Deliveries only for country Ireland at the moment'])
        if not all(x.isalpha() or x.isspace() for x in county):
            self._errors["default_county"] = self.error_class(
                ['The format is invalid'])
        else:
            if str(county).lower() != 'dublin':
                self._errors["default_county"] = self.error_class(
                    ['Deliveries only for county Dublin at the moment'])
            else:
                cleaned_data['default_county'] = 'Dublin'

        if not all(x.isalpha() or x.isspace() for x in town_or_city):
            self._errors["default_town_or_city"] = self.error_class(
                ['The format is invalid'])
        else:
            if str(town_or_city).lower() != 'dublin':
                self._errors["default_town_or_city"] = self.error_class(
                    ['Deliveries only for city Dublin at the moment'])
            else:
                cleaned_data['default_town_or_city'] = 'Dublin'

        return cleaned_data


class DateOrdersForm(forms.Form):
    """
    Form for filtering the orders in admin manage orders page
    """
    date = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date', 'class': 'px-2', 'value': date.today}))

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['date'].required = False
        self.fields['date'].label = "Filter By Date:"
