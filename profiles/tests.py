"""
Profile App - Tests
----------------
Tests for Profile App.
"""


from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from products.models import Product, Category
from checkout.models import Order
from profiles.models import UserProfile


class TestViews(TestCase):
    """
    Unit Tests for Profile App
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

    def test_profile_page_neauthenticated(self):
        """ Test if profile page redirects to login page when user is
        neauthenticated"""
        self.client.logout()
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response['location'])

    def test_profile_page_for_admin(self):
        """ Test if profile page returns 403 forbidden for admin"""

        self.client.login(email='testuser@yahoo.com', password='T12345678.')
        # Set user as admin
        self.user.is_staff = True
        self.user.is_admin = True
        self.user.save()

        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 403)

    def test_profile_page(self):
        """ Test if profile page renders correct page when user is
        authenticated as client user"""
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_profile_page_context(self):
        """ Test if profile page renders correct context """
        self.client.login(email='testuser@yahoo.com', password='T12345678.')

        # Set bag session
        session = self.client.session
        session['bag'] = {str(self.product.id): 5}
        session.save()

        # Create order object
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

        # Create order
        response = self.client.post(
            reverse('checkout'), data,)

        order = Order.objects.first()
        # Get checkout success page where the user
        # profile will be attached to order
        response = self.client.get(
            reverse('checkout_success',
                    kwargs={'order_number': order.order_number}))
        self.assertTrue(response.status_code, 200)

        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)

        self.assertTrue('delivery_details_form' in response.context)
        # Test if orders context get the created order
        self.assertTrue('orders' in response.context)
        self.assertTrue(len(response.context['orders']), 1)
        self.assertTrue(response.context['orders'][0], order)

    def test_update_delivery(self):
        """Test post method for ProfileDeliveryUpdate view"""

        current_profile = UserProfile.objects.get(user=self.user)
        self.assertIsNone(current_profile.default_street_address1)

        delivery = {
            'default_phone_number': '',
            'default_country': 'IE',
            'default_postcode': '',
            'default_town_or_city': 'Dublin',
            'default_street_address1': '90 Square',
            'default_street_address2': '',
            'default_county': 'Dublin',
            }

        self.client.post(
            reverse('profile_delivery_update',
                    kwargs={'user_pk': self.user.pk}),
            delivery,)

        # Test if value was updated
        current_profile = UserProfile.objects.get(user=self.user)
        self.assertTrue(current_profile.default_street_address1, '90 Square')

    def test_order_details_page(self):
        """ Test if order details page renders correct template"""

        self.client.login(email='testuser@yahoo.com', password='T12345678.')

        # Set bag session
        session = self.client.session
        session['bag'] = {str(self.product.id): 5}
        session.save()

        # Create order object
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

        # Create order
        response = self.client.post(
            reverse('checkout'), data,)
        # Get checkout success page where the user
        # profile will be attached to order
        order = Order.objects.first()
        response = self.client.get(
            reverse('checkout_success',
                    kwargs={'order_number': order.order_number}))

        response = self.client.get(
            reverse('order_details',
                    kwargs={'order_number': order.order_number}))
        self.assertTrue(response.status_code, 200)

        # Test context
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
        self.assertTrue('order' in response.context)
        self.assertTrue(response.context['order'], order)

    def test_admin_orders_page_neauthenticated(self):
        """ Test if admin orders page redirects to login page when user is
        neauthenticated"""
        self.client.logout()
        response = self.client.get(reverse('admin_manage_orders'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response['location'])

    def test_admin_orders_page_for_admin(self):
        """ Test if admin orders page use the correct template
        for rendering the page"""

        self.client.login(email='testuser@yahoo.com', password='T12345678.')
        # Set user as admin
        self.user.is_staff = True
        self.user.is_admin = True
        self.user.save()

        response = self.client.get(reverse('admin_manage_orders'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/admin_orders.html')

    def test_admin_orders_page(self):
        """ Test if admin orders page return
        403 forbidden for client user"""

        self.user.is_staff = False
        self.user.is_admin = False
        self.user.save()

        response = self.client.get(reverse('admin_manage_orders'))
        self.assertEqual(response.status_code, 403)

    def test_admin_orders_page_context(self):
        """ Test if admin orders page renders correct context """
        self.client.login(email='testuser@yahoo.com', password='T12345678.')

        # Set bag session
        session = self.client.session
        session['bag'] = {str(self.product.id): 5}
        session.save()

        # Create order object
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

        # Create order
        response = self.client.post(
            reverse('checkout'), data,)

        order = Order.objects.first()
        # Get checkout success page where the user
        # profile will be attached to order
        response = self.client.get(
            reverse('checkout_success',
                    kwargs={'order_number': order.order_number}))
        self.assertTrue(response.status_code, 200)

        # Set user as staff
        self.user.is_staff = True
        self.user.is_admin = True
        self.user.save()

        response = self.client.get(reverse('admin_manage_orders'))
        self.assertEqual(response.status_code, 200)

        self.assertTrue('date_form' in response.context)
        # Test if orders context get the created order
        self.assertTrue('date' in response.context)
        self.assertTrue('orders' in response.context)

        self.assertTrue(len(response.context['orders']), 1)
        self.assertTrue(response.context['orders'][0], order)

    def test_admin_order_details_page(self):
        """ Test if admin order details page renders correct template"""

        self.client.login(email='testuser@yahoo.com', password='T12345678.')

        # Set bag session
        session = self.client.session
        session['bag'] = {str(self.product.id): 5}
        session.save()

        # Create order object
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

        # Create order
        response = self.client.post(
            reverse('checkout'), data,)
        # Get checkout success page where the user
        # profile will be attached to order
        order = Order.objects.first()
        response = self.client.get(
            reverse('checkout_success',
                    kwargs={'order_number': order.order_number}))

        # Set user as staff
        self.user.is_staff = True
        self.user.is_admin = True
        self.user.save()

        response = self.client.get(
            reverse('admin_order_details',
                    kwargs={'order_number': order.order_number}))
        self.assertTrue(response.status_code, 200)

        # Test context
        self.assertTrue('from_admin' in response.context)
        self.assertTrue('order' in response.context)
        self.assertTrue(response.context['order'], order)

    def test_admin_orders_delete(self):
        """ Test AdminDeleteOrder view """
        self.client.login(email='testuser@yahoo.com', password='T12345678.')

        # Set bag session
        session = self.client.session
        session['bag'] = {str(self.product.id): 5}
        session.save()

        # Create order object
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

        # Create order
        response = self.client.post(
            reverse('checkout'), data,)

        order = Order.objects.first()
        # Get checkout success page where the user
        # profile will be attached to order
        response = self.client.get(
            reverse('checkout_success',
                    kwargs={'order_number': order.order_number}))
        self.assertTrue(response.status_code, 200)

        # Set user as staff
        self.user.is_staff = True
        self.user.is_admin = True
        self.user.save()

        response = self.client.get(
            reverse('admin_delete_order',
                    kwargs={'pk': order.pk}))
        self.assertTrue(response.status_code, 200)

        # Check if order has been deleted
        self.assertTrue(Order.objects.all().count, 0)
