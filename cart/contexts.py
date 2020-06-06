from django.shortcuts import get_object_or_404
from cars.models import Car


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering every page
    """

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0

    for id, quantity in cart.items():
        car = get_object_or_404(Car, pk=id)
        total += quantity * car.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'car': car})

    return {'cart_items': cart_items, 'total': total,
            'product_count': product_count}
