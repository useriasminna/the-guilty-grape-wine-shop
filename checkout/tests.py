"""
Checkout App - Tests
----------------
Tests for Checkout App.
"""


from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.urls import reverse
from products.models import Product, Category
from checkout.models import Order, OrderLine


class TestViews(TestCase):
    """
    Unit Tests for Checkout App
    """

    def setUp(self):
        """ Create test login """

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
        self.category = Category.objects.create(
            name="red_wines",
            friendly_name="Red Wines",
        )

        # creates test product object
        self.product = Product.objects.create(
            category=self.category,
            is_deluxe=False,
            sku='wre10778',
            name='Flor de Crasto',
            region='Douro',
            country='PT',
            grapes='Tinta Roriz, Touriga Franca, Touriga Nacional,\
            Vinhas Velhas',
            year='2019',
            style='Red',
            code='10778',
            food_pairing='Spicy Food, Pasta and Pizza, Hard Cheese',
            price=15.10,
            image='red10778.webp',
            stock=100,
        )

    def test_checkout_page(self):
        """ Test if checkout page renders correct page when user is
        authenticated"""

        # Set bag session
        session = self.client.session
        session['bag'] = {str(self.product.id): 5}
        session.save()

        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

    def test_checkout_page_neauthenticated(self):
        """ Test if checkout page renders correct page
        without user authentication """

        self.client.logout()

        # Set bag session
        session = self.client.session
        session['bag'] = {str(self.product.id): 5}
        session.save()

        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

    def test_checkout_context(self):
        """ Test if correct context is rendered to create checkout page"""

        # Set bag session
        session = self.client.session
        session['bag'] = {str(self.product.id): 5}
        session.save()

        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('order_form' in response.context)
        self.assertTrue('stripe_public_key' in response.context)
        self.assertTrue('client_secret' in response.context)

    def test_checkout_post(self):
        """Test if authenticated client user can complete
        an order with success"""

        self.client.login(email='testuser@yahoo.com', password='T12345678.')
        # Set bag session
        session = self.client.session
        session['bag'] = {str(self.product.id): 5}
        session.save()

        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)

        data = {
            'client_secret': response.context['client_secret'],
            'full_name': 'Test User',
            'email': 'testuser@yahoo.com',
            'phone_number': '0896754834',
            'country': 'IE',
            'postcode': 'd38p3c4',
            'town_or_city': 'Dublin',
            'street_address1': '75 St Anne',
            'street_address2': '',
            'county': 'Dublin',
            }

        response = self.client.post(
            reverse('checkout'), data,)

        self.assertTrue(Order.objects.all().count(), 1)
        self.assertTrue(OrderLine.objects.all().count(), 1)

        # Get created order object
        order = Order.objects.first()

        # Test if the user is redirected to checkout success after post
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response['location'],
            '/checkout/checkout_success/' + str(order.order_number))

    def test_checkout_post_neauthenticated(self):
        """Test if neauthenticated user can complete
        an order with success"""

        self.client.logout()
        # Set bag session
        session = self.client.session
        session['bag'] = {str(self.product.id): 5}
        session.save()

        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)

        data = {
            'client_secret': response.context['client_secret'],
            'full_name': 'Test User',
            'email': 'testuser@yahoo.com',
            'phone_number': '0896754834',
            'country': 'IE',
            'postcode': 'd38p3c4',
            'town_or_city': 'Dublin',
            'street_address1': '75 St Anne',
            'street_address2': '',
            'county': 'Dublin',
            }

        response = self.client.post(
            reverse('checkout'), data,)

        self.assertTrue(Order.objects.all().count(), 1)
        self.assertTrue(OrderLine.objects.all().count(), 1)

        # Get created order object
        order = Order.objects.first()

        # Test if the user is redirected to checkout success after post
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response['location'],
            '/checkout/checkout_success/' + str(order.order_number))

    def test_checkout_succes_context(self):
        """Test if neauthenticated user can complete
        an order with success"""

        # Set bag session
        session = self.client.session
        session['bag'] = {str(self.product.id): 5}
        session.save()

        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)

        data = {
            'client_secret': response.context['client_secret'],
            'full_name': 'Test User',
            'email': 'testuser@yahoo.com',
            'phone_number': '0896754834',
            'country': 'IE',
            'postcode': 'd38p3c4',
            'town_or_city': 'Dublin',
            'street_address1': '75 St Anne',
            'street_address2': '',
            'county': 'Dublin',
            }

        response = self.client.post(
            reverse('checkout'), data,)

        # Get created order object
        order = Order.objects.first()

        # Test if the user is redirected to checkout success after post
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response['location'],
            '/checkout/checkout_success/' + str(order.order_number))

        # Get checkout success page
        response = self.client.get(
            reverse('checkout_success',
                    kwargs={'order_number': order.order_number}))
        self.assertTrue(response.status_code, 200)

        # Test if context contains current order
        self.assertTrue('order' in response.context)
        messages = list(get_messages(response.wsgi_request))
        # Test if a message was added to list
        self.assertEqual(len(messages), 1)
        # Test if 'success' is in message tags
        self.assertIn('success', messages[0].tags)
