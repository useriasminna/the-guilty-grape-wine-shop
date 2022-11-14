"""
Product Reviews App - Forms
----------------
Forms for Product Reviews App.
"""

from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """Form for update review"""
    rate = forms.IntegerField(widget=forms.NumberInput(
        attrs={'id': 'rateValue', 'type': 'hidden'}))
    review_text = forms.CharField(widget=forms.Textarea(
        attrs={'id': 'addReviewText', 'rows': '6'}), label="Add a message:",
        required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rate'].required = False

    class Meta:
        """Override Meta method"""
        model = Review
        fields = ['review_text', 'rate']


class UpdateReviewForm(forms.ModelForm):
    """Form for update review"""
    rate = forms.IntegerField(widget=forms.NumberInput(
        attrs={'id': 'updateRateValue', 'type': 'hidden'}))
    review_text = forms.CharField(widget=forms.Textarea(attrs={
        'id': 'updateReviewText', 'rows': '6'}), label="Update your message")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rate'].required = False

    class Meta:
        """Override Meta method"""
        model = Review
        fields = ['review_text', 'rate']
