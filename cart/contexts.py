from django.shortcuts import get_object_or_404
from cars.models import Car, TrackDayAddon, InsuranceAddon, PrivateDriverAddon


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering every page
    Different products are manipulated to render back cohesive and relevant
    information
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total_cart = 0
    item_count = 0
    partial_value = []

    for item in cart:
        if item == 'car':
            id = cart['car']['item_id']
            quantity = cart['car']['quantity']
            instance = Car
            item_type = 'car'
        elif item == 'track_day':
            id = cart['track_day']['item_id']
            quantity = cart['track_day']['quantity']
            instance = TrackDayAddon
            item_type = 'track_day'
        elif item == 'insurance':
            id = cart['insurance']['item_id']
            quantity = cart['insurance']['quantity']
            instance = InsuranceAddon
            item_type = 'insurance'
        elif item == 'private_driver':
            id = cart['private_driver']['item_id']
            quantity = cart['private_driver']['quantity']
            instance = PrivateDriverAddon
            item_type = 'private_driver'

        item = get_object_or_404(instance, pk=id)
        total_cart += quantity * item.price
        item_total = quantity * item.price
        item_count += 1
        partial_value.append({
            'item': item,
            'item_type': item_type,
            'id': id,
            'item_total': item_total
            })
        cart_items.append({
            'item': item,
            'item_type': item_type,
            'id': id,
            'quantity': quantity,
            })
    return {'cart_items': cart_items, 'partial_value': partial_value,
            'total_cart': total_cart, 'item_count': item_count}
