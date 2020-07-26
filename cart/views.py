from django.contrib import messages
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
        cart['insurance'] = {
            'item_type': 'insurance',
            'item_id': 2,
            'quantity': numberOfDays,
        }
        addon = InsuranceAddon.objects.all()
        next_page = 'track_day'

    elif item_type == 'track_day':
        item = TrackDayAddon.objects.get(pk=item_id)
        addon = TrackDayAddon.objects.all()
        next_page = 'insurance'

    elif item_type == 'insurance':
        item = InsuranceAddon.objects.get(pk=item_id)
        addon = InsuranceAddon.objects.all()
        next_page = 'private_driver'

    elif item_type == 'private_driver':
        item = PrivateDriverAddon.objects.get(pk=item_id)
        addon = PrivateDriverAddon.objects.all()
        next_page = 'checkout'

    cart[item_type] = {
            'item_type': item_type,
            'item_id': item.id,
            'quantity': numberOfDays,
            }

    request.session['cart'] = cart

    messages.success(request, "Successfully added to cart!")

    if next_page == 'checkout':
        return redirect(reverse('checkout'))
    else:
        return redirect(reverse('add_ons', args=(next_page,)),
                        {
                            'addon': addon,
                            'iType': next_page,
                        })


def adjust_cart(request, item_type, item_id):
    """Adjusts the number of days(quantity) to the specified amount"""

    numberOfDays = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if numberOfDays > 0:
        if item_type == 'car':
            cart['car']['quantity'] = numberOfDays
            cart['insurance']['quantity'] = numberOfDays
        elif item_type == 'track_day':
            cart['track_day']['quantity'] = numberOfDays
        elif item_type == 'private_driver':
            cart['private_driver']['quantity'] = numberOfDays

    else:
        if item_type == 'car':
            del(cart['car'])
            del(cart['insurance'])
        elif item_type == 'track_day':
            del(cart['track_day'])
        elif item_type == 'private_driver':
            del(cart['private_driver'])

    request.session['cart'] = cart
    messages.success(request, "Cart successfully updated!")
    return redirect(reverse('view_cart'))
