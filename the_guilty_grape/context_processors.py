"""
the_guilty_grape project - Context processors
"""
from newsletter.forms import AddSubscriber


def add_subscription_form_to_context(request):
    """Method to return subscription form as context"""
    return {
        'add_subscriber_form': AddSubscriber
    }
