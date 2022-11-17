"""
Newsletter App - Views
----------------
Views for Newsletter App.
"""
from django.views.generic import CreateView

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from newsletter.forms import AddSubscriber
from newsletter.models import Subscription


class SubscribeToNewsletter(CreateView):
    """A view that provides a form for users to subscribe for newsletter"""
    template_name = "base.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['path'] = self.kwargs.get('path')
        return kwargs

    def post(self, request, *args, **kwargs):
        """Override post method"""
        if request.method == 'POST':

            subscribe_form = AddSubscriber(request.POST, request.FILES)

            if subscribe_form.is_valid():
                email = subscribe_form.cleaned_data['email']
                subscription = Subscription(email=email)
                subscription.save()
                messages.success(
                    request, 'Thank you for your subscription!',
                    extra_tags="form_success")
                return HttpResponseRedirect(request.POST.get(
                    'newsletter_submit_btn', '') + '#newsletter')
            else:
                messages.error(request, subscribe_form.errors['email'],
                               extra_tags="form_errors")
                return HttpResponseRedirect(request.POST.get(
                    'newsletter_submit_btn', '') + '#newsletter')

        subscribe_form = AddSubscriber()
        return render(request, 'base.html',
                      {'add_subscriber_forms': subscribe_form, })
