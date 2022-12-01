"""
Product Reviews App - Tests
----------------
Tests for Product Reviews App.
"""


from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.urls import reverse
from products.models import Product, Category
from product_reviews.models import Review


class TestViews(TestCase):
    """
    Unit Tests for Product Reviews App
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

    def test_add_product_review(self):
        """ Test AddReview view """

        # Call post method for AddToBag view
        data = {'rate': 5, 'review_text': 'My favorite wine'}
        response = self.client.post(
            reverse('add_review', kwargs={'product_id': self.product.id, }),
            data,)

        messages = list(get_messages(response.wsgi_request))
        # Test if a message was added to list
        self.assertEqual(len(messages), 1)
        # Test if 'success' is in message tags
        self.assertIn('success', messages[0].tags)
        # Test if the user is redirected after post
        self.assertEqual(response.status_code, 302)
        # Test if the redirect location matches the value from view
        self.assertEqual(response['location'],
                         '/products/product_details/'
                         + str(self.product.id) +
                         '/#reviewsSection')

        response = self.client.get(
            '/products/product_details/' + str(self.product.id) +
            '/#reviewsSection')

        self.assertEqual(response.status_code, 200)
        # Test if product details page get the correct review context
        self.assertTrue('review_list' in response.context)
        self.assertTrue('current_review' in response.context)

        # Test if review list context was updated with
        # the product review that was added
        self.assertEqual(len(response.context['review_list']), 1)
        # Test if the review object was created for the current user and
        # the product passed as argument
        self.assertEqual(
            response.context['review_list'][0].product, self.product)
        self.assertEqual(
            response.context['review_list'][0].author, self.user)
        self.assertEqual(
            response.context['review_list'][0].rate, 5)
        self.assertEqual(
            response.context['review_list'][0].review_text, 'My favorite wine')

        # Test if current review context contains the correct review
        self.assertEqual(
            response.context['current_review'].product, self.product)
        self.assertEqual(
            response.context['current_review'].author, self.user)

    def test_add_product_review_neauthenticated_redirects(self):
        """ Test if AddReview view post method redirects
        the neauthenticated users to login page  """

        self.client.logout()

        # Call post method for AddToBag view
        data = {'rate': '3', 'review_text': 'My favorite wine'}
        response = self.client.post(
            reverse('add_review', kwargs={'product_id': self.product.id, }),
            data,)

        # Test if the user is redirected to login page after post
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response['location'])

    def test_add_product_review_admin_fails(self):
        """ Test if AddReview view post method returns 403 forbidden
        for admin users """

        self.client.login(email='testuser@yahoo.com', password='T12345678.')
        # Set user as admin
        self.user.is_staff = True
        self.user.is_admin = True
        self.user.save()

        # Call post method for AddToBag view
        data = {'rate': '3', 'review_text': 'My favorite wine'}
        response = self.client.post(
            reverse('add_review', kwargs={'product_id': self.product.id, }),
            data,)

        # Test if the user is redirected to login page after post
        self.assertEqual(response.status_code, 403)

        self.user.is_staff = False
        self.user.is_admin = False
        self.user.save()

    def test_update_product_review(self):
        """ Test UpdateReview view """
        # Add review
        data = {'rate': 5, 'review_text': 'My favorite wine'}
        response = self.client.post(
            reverse('add_review', kwargs={'product_id': self.product.id, }),
            data,)

        # Open product details page
        response = self.client.get(
            '/products/product_details/' + str(self.product.id) +
            '/#reviewsSection')
        self.assertEqual(response.status_code, 200)

        messages = list(get_messages(response.wsgi_request))
        # Test if a message was added to list
        self.assertEqual(len(messages), 1)
        # Test if 'success' is in message tags
        self.assertIn('success', messages[0].tags)

        self.assertEqual(
            response.context['review_list'][0].rate, 5)
        self.assertEqual(
            response.context['review_list'][0].review_text, 'My favorite wine')

        review = Review.objects.get(author=self.user, product=self.product)
        # Update review
        data = {'rate': 1, 'review_text': 'Not so good'}
        response = self.client.post(reverse(
            'update_review',
            kwargs={
                'product_id': self.product.id,
                'review_id': review.id,
                }), data,)

        messages = list(get_messages(response.wsgi_request))
        # Test if a message was added to list
        self.assertEqual(len(messages), 1)
        # Test if 'success' is in message tags
        self.assertIn('success', messages[0].tags)
        # Test if the user is redirected after post
        self.assertEqual(response.status_code, 302)
        # Test if the redirect location matches the value from view
        self.assertEqual(response['location'],
                         '/products/product_details/'
                         + str(self.product.id) +
                         '/#reviewsSection')

        # Open product details page
        response = self.client.get(
            '/products/product_details/' + str(self.product.id) +
            '/#reviewsSection')
        self.assertEqual(response.status_code, 200)

        # Test if the values for current review were updated
        self.assertEqual(
            response.context['review_list'][0].rate, 1)
        self.assertEqual(
            response.context['review_list'][0].review_text, 'Not so good')
