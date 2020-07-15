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


def adjust_cart(request, item_type, item_id):
    """Adjusts the number of days(quantity) to the specified amount"""

    numberOfDays = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if numberOfDays > 0:
        if item_type == 'car':
            cart['car']['quantity'] = numberOfDays
        elif item_type == 'track_day':
            cart['track_day']['quantity'] = numberOfDays
        elif item_type == 'insurance':
            cart['insurance']['quantity'] = numberOfDays
        elif item_type == 'private_driver':
            cart['private_driver']['quantity'] = numberOfDays

        # print(item.id)
# quantity = cart['private_driver']['quantity']
    # if numberOfDays > 0:
    #     cart[id] = numberOfDays
    else:
        if item_type == 'car':
            del(cart['car'])
        elif item_type == 'track_day':
            del(cart['track_day'])
        elif item_type == 'insurance':
            del(cart['insurance'])
        elif item_type == 'private_driver':
            # cart.pop(cart['private_driver'])
            del(cart['private_driver'])
        # cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
