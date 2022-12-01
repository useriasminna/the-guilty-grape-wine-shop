"""
Bag App - Tests
----------------
Tests for Bag App.
"""


from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.urls import reverse
from products.models import Product, Category


class TestViews(TestCase):
    """
    Unit Tests for Bag App Views
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

    def test_bag_page(self):
        """ Test if bag page renders correct page when user is
        authenticated as client user"""
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_bag_page_neauthenticated(self):
        """ Test if bag page renders correct page
        without user authentication """
        self.client.logout()
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_bag_context(self):
        """ Test if Voucher form is rendered to create bag page"""
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('add_voucher_form' in response.context)

    def test_bag_page_fails_for_admin(self):
        """ Test if bag page returns 403 forbiden when
        logged in user is admin """

        self.client.login(email='testuser@yahoo.com', password='T12345678.')
        self.user.is_staff = True
        self.user.is_admin = True
        self.user.save()

        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 403)
        self.user.is_staff = False
        self.user.is_admin = False
        self.user.save()

    def test_update_shopping_bag(self):
        """Test if user can add/remove product from shopping bag
        and if class method redirects the user after post"""

        self.client.logout()

        # Call post method for AddToBag view
        data = {'quantity': '5', 'current_url': '/products/'}
        response = self.client.post(
            reverse('add_to_bag', kwargs={'product_id': self.product.id, }),
            data,)

        # Test if bag session variable was created
        self.assertIn('bag', self.client.session)
        # Test if bag session contains the corresponding quantity
        # value added for the product id key
        self.assertEqual(self.client.session['bag'], {str(self.product.id): 5})

        messages = list(get_messages(response.wsgi_request))
        # Test if a message was added to list
        self.assertEqual(len(messages), 1)
        # Test if 'success' is in message tags
        self.assertIn('success', messages[0].tags)
        # Test if the user is redirected after post
        self.assertEqual(response.status_code, 302)
        # Test if the redirect location matches the value from
        # current_url
        self.assertEqual(response['location'], '/products/')

        # Call post method for RemoveFromBag view
        data = {'current_url': '/bag/'}
        response = self.client.post(
            reverse('remove_from_bag',
                    kwargs={'product_id': self.product.id, }),
            data,)

        # Test if bag session variable was created
        self.assertIn('bag', self.client.session)
        # Test if bag session is empty after removing the only product
        # added to the shoping bag
        self.assertEqual(self.client.session['bag'], {})

        messages = list(get_messages(response.wsgi_request))
        # Test if another message was added to list
        self.assertEqual(len(messages), 2)
        # Test if 'success' is in the last message's tags
        self.assertIn('success', messages[1].tags)
        # Test if the user is redirected after post
        self.assertEqual(response.status_code, 302)
        # Test if the redirect location matches the value from
        # current_url
        self.assertEqual(response['location'], '/bag/')

    def test_update_product_quantity_in_shopping_bag(self):
        """Test if the user can update a product quantity
        in the shopping bag page"""

        # Call post method for AddToBag view
        data = {'quantity': '3', 'current_url': '/bag/'}
        response = self.client.post(
            reverse('add_to_bag',
                    kwargs={'product_id': self.product.id, }),
            data,)

        # Test if bag session variable was created
        self.assertIn('bag', self.client.session)
        # Test if bag session contains the corresponding quantity
        # value added for the product id key
        self.assertEqual(self.client.session['bag'], {str(self.product.id): 3})

        # Call post method for UpdateBagQuantity view
        data = {'quantity': '2', 'current_url': '/bag/'}
        response = self.client.post(
            reverse('update_quantity',
                    kwargs={'product_id': self.product.id, }),
            data,)

        # Test if bag session contains the corresponding quantity
        # value updated for the product id key
        self.assertEqual(self.client.session['bag'], {str(self.product.id): 2})

        messages = list(get_messages(response.wsgi_request))
        # Test if another message was added to list
        self.assertEqual(len(messages), 2)
        # Test if 'success' is in the last message's tags
        self.assertIn('success', messages[1].tags)
        # Test if the user is redirected after post
        self.assertEqual(response.status_code, 302)
        # Test if the redirect location matches the value from
        # current_url
        self.assertEqual(response['location'], '/bag/')
