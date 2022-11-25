"""
Bag App - Context
----------------
Context for Bag App.
"""

from decimal import Decimal
from django.conf import settings
from django.db.models import Q
from django.shortcuts import get_object_or_404
from products.models import Product
from wishlist.models import WishlistLine
from vouchers.models import Voucher


def bag_contents(request):
    """Method that returns context for bag page"""
    bag_items = []
    total = 0
    product_count = 0
    discount_value = 0
    voucher_id = request.session.get('voucher_id', None)
    discount = request.session.get('discount', None)
    bag = request.session.get('bag', {})

    # GET LIST OF BAG ITEMS WITH PROPERTIES: PRODUCT, QUANTITY AND SUBTOTAL
    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        subtotal = quantity * product.price
        total += subtotal
        product_count += quantity
        current_wishlist_line = None

        # GET CURRENT WISHLIST LINE OBJECT FOR EVERY PRODUCT
        if request.user.is_authenticated and \
            WishlistLine.objects.filter(
                Q(user=request.user) & Q(product=product)).exists():
            current_wishlist_line = WishlistLine.objects.get(
                user=request.user, product=product)

        bag_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
            'current_wishlist_line': current_wishlist_line
        })

    if discount:
        # CALCULATE DISCOUNT VALUE
        discount_value = total * Decimal(discount / 100)
        if (total - discount_value) < settings.FREE_DELIVERY_THRESHOLD:
            delivery = (total - discount_value) * Decimal(
                settings.STANDARD_DELIVERY_PERCENTAGE / 100)
            free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - (
                total - discount_value)
        else:
            delivery = 0
            free_delivery_delta = 0
        grand_total = (total - discount_value) + delivery
    # CALCULATE DELIVERY AND FREE DELIVERY DELTA VALUE
    elif total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
        grand_total = delivery + total
    else:
        delivery = 0
        free_delivery_delta = 0
        grand_total = delivery + total

    if voucher_id:
        voucher = Voucher.objects.get(pk=voucher_id)
    else:
        voucher = None
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'voucher': voucher,
        'discount_value': discount_value,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
