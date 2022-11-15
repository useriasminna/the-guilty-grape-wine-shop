"""
Bag App - Context
----------------
Context for Bag App.
"""

from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """Method that returns context for bag page"""
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    # GET LIST OF BAG ITEMS WITH PROPERTIES: PRODUCT, QUANTITY AND SUBTOTAL
    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        subtotal = quantity * product.price
        total += subtotal
        product_count += quantity
        bag_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    # CALCULATE DELIVERY AND FREE DELIVERY DELTA VALUE
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
