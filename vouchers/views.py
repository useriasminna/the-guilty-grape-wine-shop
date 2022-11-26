"""
Vouchers App - Views
----------------
Views for Vouchers App.
"""
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib import messages


from .models import Voucher
from .forms import AddVoucherForm


class UpdateDiscountBag(View):
    """"View for updating session variables for discount and vouchers
    to be used in bag/contexts.py"""
    template_name = 'bag/bag.html'

    def post(self, request, *args, **kwargs):
        voucher_remove = request.POST.get('voucher_remove')
        voucher = None
        if voucher_remove:
            request.session['discount'] = None
            request.session['voucher_id'] = None
        else:
            voucher_form = AddVoucherForm(request.POST)
            if voucher_form.is_valid():
                voucher_code = voucher_form.cleaned_data['voucher_code']
                if voucher_code != "":
                    if not Voucher.objects.filter(
                            voucher_code=voucher_code).exists():
                        request.session['discount'] = None
                        request.session['voucher_id'] = None
                        messages.error(
                            request,
                            f'<b>"{voucher_code}"</b> is not a valid\
                                voucher code',
                            extra_tags='safe')
                    else:
                        voucher = Voucher.objects.get(
                            voucher_code=voucher_code)
                        discount = voucher.percentage
                        request.session['discount'] = discount
                        request.session['voucher_id'] = voucher.id
                else:
                    messages.error(
                            request, "Please enter a voucher code")
                    request.session['discount'] = None
                    request.session['voucher_id'] = None
        return redirect('/bag/')
