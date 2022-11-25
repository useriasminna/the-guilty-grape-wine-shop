"""
Vouchers App - Models
----------------
Models for Vouchers App.
"""

from django.db import models
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.dispatch import receiver
from django.contrib import messages
from allauth.account.signals import email_confirmed

from users.models import User
import uuid
import humanhash


class Voucher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=False, blank=False)
    percentage = models.PositiveIntegerField(default=15, null=False,
                                             blank=False)
    voucher_code = models.CharField(max_length=254, null=False, blank=False,
                                    unique=True)


@receiver(email_confirmed)
def send_discount_voucher_on_email_confirmed_(request,
                                              email_address, **kwargs):
    """Send email with a discount voucher when the user confirms his email.
    Create a voucher instance"""
    user = User.objects.get(email=email_address.email)

    code = uuid.uuid4().hex
    voucher_code = humanhash.humanize(str(code))
    while len(Voucher.objects.filter(voucher_code=code)) != 0:
        code = uuid.uuid4().hex
        voucher_code = humanhash.humanize(str(code))
    voucher = Voucher(user=user, percentage=15, voucher_code=voucher_code)
    voucher.save()

    customer_email = email_address.email
    subject = render_to_string(
        'vouchers/discount_emails/discount_email_subject.txt')
    body = render_to_string(
        'vouchers/discount_emails/discount_email_body.html',
        {
            'user': user,
            'contact_email': settings.DEFAULT_FROM_EMAIL,
            'voucher_code': voucher_code,
        })

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [customer_email],
        html_message=body,
    )
    messages.info(request, 'A voucher code was sent to ' + email_address.email)
