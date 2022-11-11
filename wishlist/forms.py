"""
Wishlist App - Forms
----------------
Forms for Wishlist App.
"""

from django import forms
from .models import WishlistLine


class SetWishlistRelation(forms.ModelForm):
    """Form for setting product state of favourite"""

    class Meta:
        model = WishlistLine
        fields = []
