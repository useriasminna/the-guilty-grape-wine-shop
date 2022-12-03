"""
Profiles App - Views
----------------
Views for Profiles App.
"""
from django.views.generic import TemplateView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import base64
import os
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from datetime import date
from django.http import HttpResponseRedirect

from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from checkout.models import Order
from users.models import User
from .forms import DateOrdersForm


class Profile(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    """A view for rendering user profile page with delivery form
    and orders history"""

    template_name = "profiles/profile.html"
    model = UserProfile

    def get(self, request):
        profile = get_object_or_404(UserProfile, user=request.user)
        # Set initial values
        form = UserProfileForm(instance=profile, initial={
            'default_country': 'IE',
            'default_town_or_city': 'Dublin',
            'default_county': 'Dublin',
            })
        orders = Order.objects.filter(user=profile).order_by('-date')

        template = 'profiles/profile.html'
        context = {
            'delivery_details_form': form,
            'orders': orders,
        }

        return render(request, template, context)

    def test_func(self):
        return not self.request.user.is_superuser


class ProfileDeliveryUpdate(LoginRequiredMixin, UserPassesTestMixin,
                            UpdateView):
    """A view for updating delivery details for current user"""
    template_name = "profiles/profile.html"
    model = UserProfile

    def post(self, request, user_pk):
        profile = get_object_or_404(UserProfile, user=user_pk)
        orders = Order.objects.filter(user=profile)
        if request.method == 'POST':
            delivery_details_form = UserProfileForm(
                request.POST, instance=profile)
            if delivery_details_form.is_valid():
                # Set IE as default country value
                profile.default_country = 'IE'
                profile.save()
                delivery_details_form.save()
                messages.success(request, 'Delivery details updated\
                    successfully')
                HttpResponseRedirect(reverse_lazy('profile'))
            else:
                # If form is not valid pass the form with errors to context
                delivery_details_form = UserProfileForm(
                    request.POST, instance=profile)
                template = 'profiles/profile.html'
                context = {
                    'delivery_details_form': delivery_details_form,
                    'orders': orders,
                }
                messages.error(request, 'There was an error with your form. \
                Please double check your information.')
                return render(request, template, context)
        elif request.method == 'GET':
            delivery_details_form = UserProfileForm(
                initial={
                    'default_country': 'IE',
                    'default_town_or_city': 'Dublin',
                    'default_county': 'Dublin',
                    },
                instance=profile)

        return HttpResponseRedirect(reverse_lazy('profile'))

    def test_func(self):
        user = User.objects.get(pk=self.kwargs['user_pk'])
        return self.request.user == user


class OrderDetails(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    """A view for rendering order details page"""
    template_name = "checkout/checkout_success.html"

    def get(self, request, order_number):
        order = get_object_or_404(Order, order_number=order_number)

        template = 'checkout/checkout_success.html'
        context = {
            'order': order,
            'from_profile': True,
        }

        return render(request, template, context)

    def test_func(self):
        order = Order.objects.get(order_number=self.kwargs['order_number'])
        user_not_admin = not self.request.user.is_superuser
        return user_not_admin and order.user.user == self.request.user


class AdminOrdersList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """A view for rendering orders filtered by date"""
    model = Order
    template_name = "profiles/admin_orders.html"
    context_object_name = "orders"

    def get(self, request):
        if request.method == 'GET':
            today = date.today()
            date_form = DateOrdersForm(data=request.GET)
            if date_form.is_valid():
                # if form is valid filter orders by date field value
                orders_date = date_form.cleaned_data['date']
                if orders_date:
                    orders_date = orders_date
                if orders_date:
                    query = Order.objects.filter(
                        date=orders_date).order_by('-date')
                else:
                    orders_date = today
                query = Order.objects.filter(
                    date__date=orders_date).order_by('-date')
                context = {'date_form': date_form,
                           'date': orders_date,
                           'orders': query}

        return render(request, 'profiles/admin_orders.html', context)

    def test_func(self):
        return self.request.user.is_superuser


class AdminDeleteOrder(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """A view for removing order object"""
    model = Order
    template_name = "profiles/admin_orders.html"
    success_url = reverse_lazy('admin_manage_orders')
    success_message = "Order was successfully deleted."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        """Create success url to keep current date filtering"""
        orders_date = self.get_object().date
        csrf = base64.b64encode(os.urandom(64))
        return '/profile/manage_orders/?csrfmiddlewaretoken=' +\
               csrf.decode("utf-8") + '&date=' + \
               orders_date.strftime("%Y-%m-%d")

    def test_func(self):
        return self.request.user.is_superuser


class AdminOrderDetails(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    """A view for rendering order details page"""
    template_name = "checkout/checkout_success.html"

    def get(self, request, order_number):
        order = get_object_or_404(Order, order_number=order_number)

        template = 'checkout/checkout_success.html'
        context = {
            'order': order,
            'from_admin': True,
        }

        return render(request, template, context)

    def test_func(self):
        return self.request.user.is_superuser
