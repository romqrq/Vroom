from django.shortcuts import render, redirect, reverse


def view_cart(request):
    """A view that renders the cart content page"""

    return render(request, 'cart.html')


def add_to_cart(request, id):
    """adds a specified number of days (quantity) of the chosen car(s) to the cart"""

    numberOfDays = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, numberOfDays)

    request.session['cart'] = cart

    return redirect(reverse('index'))


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
