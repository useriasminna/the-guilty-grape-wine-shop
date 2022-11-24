"""
Profiles App - Models
----------------
Models for Profiles App.
"""

from django.db import models
from users.models import User
from django.db.models.signals import post_save
from allauth.account.signals import email_confirmed
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True,
                                            blank=True)
    default_country = CountryField(blank_label='Country', null=True,
                                   blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True,
                                            blank=True)
    default_county = models.CharField(max_length=80, null=True,
                                      blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True,
                                               blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True,
                                               blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()


@receiver(email_confirmed)
def send_discount_voucher_on_email_confirmed_(request,
                                              email_address, **kwargs):

    user = User.objects.get(email=email_address.email)
    customer_email = email_address.email
    subject = render_to_string(
        'profiles/discount_emails/discount_email_subject.txt',
        {'user': user})
    body = render_to_string(
        'profiles/discount_emails/discount_email_body.txt',
        {'user': user, 'contact_email': settings.DEFAULT_FROM_EMAIL})

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [customer_email],
    )
    messages.info(request, 'A voucher code was sent to \
        {{email_address.email}}')


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created and not instance.is_superuser:
        UserProfile.objects.create(user=instance)
    if not instance.is_superuser:
        instance.userprofile.save()
