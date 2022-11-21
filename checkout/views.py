"""
Checkout App - Views
----------------
Views for Checkout App.
"""

from django.views.generic import View, TemplateView
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.conf import settings


from .models import Order, OrderLine
from .forms import OrderForm
from products.models import Product
from bag.contexts import bag_contents

import stripe


class Checkout(TemplateView):
    """View for displaying order forms and
    creating Order and OrderLine objects"""

    template_name = 'checkout/checkout.html'
    model = Order

    def get(self, request):
        """Override get method"""
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(
                request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
                Did you forget to set it in your environment?')

        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)

    def post(self, request):
        """Override post method for submiting order form"""
        bag = request.session.get('bag', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, quantity in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line = OrderLine(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line.save()

                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in\
                            our database. Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse(
                'checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
        return redirect(reverse('checkout'))


class CheckoutSuccess(View):
    """
    Handle successful checkouts
    """

    def get(self, request, order_number):
        """Override get method"""
        order = get_object_or_404(Order, order_number=order_number)
        messages.success(request, f'Order successfully processed! \
            Your order number is {order_number}. A confirmation \
            email will be sent to {order.email}.')

        if 'bag' in request.session:
            del request.session['bag']

        template = 'checkout/checkout_success.html'
        context = {
            'order': order,
        }

        return render(request, template, context)
