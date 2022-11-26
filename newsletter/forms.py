"""
Newsletter App - Forms
----------------
Forms for Newsletter App.
"""
from django import forms
from .models import Subscription


class AddSubscriber(forms.ModelForm):
    """Form for adding email to newsletter subscribers"""
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'id': 'newsletter_email', }), label="Enter your email:")

    class Meta:
        """Meta class"""
        model = Subscription
        fields = ['email', ]
