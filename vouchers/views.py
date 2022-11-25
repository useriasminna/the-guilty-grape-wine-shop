"""
Vouchers App - Views
----------------
Views for Vouchers App.
"""
from django.views.generic import View
from django.shortcuts import render

from .models import Voucher


class UpdateDiscountBag(View):
    """"View for updating session variables for discount and vouchers
    to be used in bag/contexts.py"""
    template_name = 'bag/bag.html'

    def post(self, request, *args, **kwargs):
        voucher_remove = request.POST.get('voucher_remove')
        if voucher_remove:
            voucher = None
            request.session['discount'] = None
            request.session['voucher_id'] = None
        else:
            voucher_code = request.POST.get('voucher_code')
            voucher = Voucher.objects.get(voucher_code=voucher_code)
            discount = voucher.percentage
            request.session['discount'] = discount
            request.session['voucher_id'] = voucher.id

        template = 'bag/bag.html'
        context = {
            'voucher': voucher,
        }

        return render(request, template, context)
