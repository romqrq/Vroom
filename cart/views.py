from django.shortcuts import render, redirect, reverse
from cars.models import Car, TrackDayAddon, InsuranceAddon, PrivateDriverAddon


def view_cart(request):
    """A view that renders the cart content page"""

    return render(request, 'cart.html')


def add_to_cart(request, item_type, item_id):
    """
    adds a specified number of days (quantity) of the chosen item(s)
    to the cart
    """

    numberOfDays = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if item_type == 'car':
        item = Car.objects.get(pk=item_id)

    elif item_type == 'track_day':
        item = TrackDayAddon.objects.get(pk=item_id)

    elif item_type == 'insurance':
        item = InsuranceAddon.objects.get(pk=item_id)

    elif item_type == 'private_driver':
        item = PrivateDriverAddon.objects.get(pk=item_id)

    cart[item_type] = {
            'item_type': item_type,
            'item_id': item.id,
            'quantity': numberOfDays,
            }

    request.session['cart'] = cart

    track_day = TrackDayAddon.objects.all()
    insurance = InsuranceAddon.objects.all()
    private_driver = PrivateDriverAddon.objects.all()
    return redirect(reverse('add_ons'),
                    {
                        'track_day': track_day,
                        'insurance': insurance,
                        'private_driver': private_driver
                    })


def adjust_cart(request, id):
    """Adjusts the number of days(quantity) to the specified amount"""

    NumberOfDays = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if NumberOfDays > 0:
        cart[id] = NumberOfDays
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
