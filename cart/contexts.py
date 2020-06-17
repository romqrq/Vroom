from django.shortcuts import get_object_or_404
from cars.models import Car


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering every page
    """

    cart = request.session.get('cart', {})

    cart_items = []
    total_cart = 0
    item_count = 0
    partial_value = []

    for id, quantity in cart.items():
        car = get_object_or_404(Car, pk=id)
        total_cart += quantity * car.price
        item_total = quantity * car.price
        item_count += 1
        partial_value.append({'id': id, 'item_total': item_total})
        cart_items.append({'id': id, 'quantity': quantity, 'car': car})

    return {'cart_items': cart_items, 'partial_value': partial_value,
            'total_cart': total_cart, 'item_count': item_count}
