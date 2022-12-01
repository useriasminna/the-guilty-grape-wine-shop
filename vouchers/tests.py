"""
Vouchers App - Tests
----------------
Tests for Vouchers App.
"""


from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from vouchers.models import Voucher


class TestViews(TestCase):
    """
    Unit Tests for Vouchers App Views
    """

    def setUp(self):
        """ Create test voucher """

        # creates test user
        email = "testuser@yahoo.com"
        first = "test"
        last = "user"
        pswd = "T12345678."
        user_model = get_user_model()
        self.user = user_model.objects.create_user(
            email=email, first_name=first, last_name=last, password=pswd)
        logged_in = self.client.login(email=email, password=pswd)
        self.assertTrue(logged_in)

        # creates test category object
        self.voucher = Voucher.objects.create(
            user=self.user,
            percentage=11,
            voucher_code='voucher_test'
        )

    def test_voucher_apply_remove(self):

        # Test if voucher_id session variable is not created
        self.assertNotIn('voucher_id', self.client.session)

        # Voucher form submit
        data = {'voucher_code': 'voucher_test'}
        self.client.post(reverse('update_discount'), data,)

        # Test if voucher_id session was added after form submit
        self.assertIn('voucher_id', self.client.session)

        self.assertEqual(self.client.session['voucher_id'], self.voucher.pk)

        # Voucher remove form submit
        data = {'voucher_remove': True}
        self.client.post(reverse('update_discount'), data,)

        # Test if current voucher is None after removing
        self.assertIsNone(self.client.session['voucher_id'])
