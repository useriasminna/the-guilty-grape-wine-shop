"""
Vouchers App - Forms
----------------
Forms for Vouchers App.
"""

from django import forms


class AddVoucherForm(forms.Form):
    voucher_code = forms.CharField(max_length=254, required=False)
