"""
Newsletter App - Tests
----------------
Tests for Newsletter App.
"""


from django.test import TestCase
from django.contrib.messages import get_messages
from django.urls import reverse


class TestViews(TestCase):
    """
    Unit Tests for Newsletter App Views
    """

    def test_newsleter_template(self):
        """ Test if SubscribeToNewsletter view renders correct
        template"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_subscribe(self):
        """ Test SubscribeToNewsletter view"""

        response = self.client.get('/bag/')

        data = {'email': 'testuser@yahoo.com', 'newsletter_submit_btn': '/'}
        response = self.client.post(
            reverse('subscribe_to_newsletter'), data,)

        messages = list(get_messages(response.wsgi_request))
        # Test if a message was added to list
        self.assertEqual(len(messages), 1)
        # Test if 'form_success' is in message tags
        self.assertIn('form_success', messages[0].tags)
        # Test if the user is redirected after post
        self.assertEqual(response.status_code, 302)
        # Test if the redirect location matches the value from
        # newsletter_submit_btn data + #newsletter
        self.assertEqual(response['location'], '/#newsletter')

        # Test if post method fails if the same email is trying to subscribe
        data = {'email': 'testuser@yahoo.com', 'newsletter_submit_btn': '/'}
        response = self.client.post(
            reverse('subscribe_to_newsletter'), data,)

        messages = list(get_messages(response.wsgi_request))
        # Test if a message was added to list
        self.assertEqual(len(messages), 2)
        # Test if 'form_errors' is in message tags
        self.assertIn('form_errors', messages[1].tags)
        # Test if the user is redirected after post
        self.assertEqual(response.status_code, 302)
        # Test if the redirect location matches the value from
        # newsletter_submit_btn data + #newsletter
        self.assertEqual(response['location'], '/#newsletter')
