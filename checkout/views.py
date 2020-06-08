from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from .models import OrderLineItem
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from django.conf import settings
from django.utils import timezone
from cars.models import Car
import stripe


stripe.api_key = settings.STRIPE_SECRET


@login_required
def checkout(request):
    """View to display checkout with relevant information for user"""

    if request.method == "POST":
        # getting user and payment information posted
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            # Getting from session information of what is being purchased
            cart = request.session.get('cart', {})
            total = 0

            for id, quantity in cart.items():

                car = get_object_or_404(Car, pk=id)
                total += quantity * car.price

                order_line_item = OrderLineItem(
                    order=order,
                    car=car,
                    quantity=quantity
                )

                order_line_item.save()

            # Trying to create a charge with stripe based on the cart content
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.error(request, "You have successfully paid!")
                request.session['cart'] = {}
                return redirect(reverse('products'))
            else:
                messages.error(request, "Unable to take payment")
        # If one of the filled forms isn't valid
        else:
            print(payment_form.errors)
            messages.error(request,
                           "We were unable to take a payment with that card!")
    # If method isn't POST
    else:
        payment_form = MakePaymentForm()

    return render(request, 'checkout.html', {
        'order_form': order_form,
        'payment_form': payment_form,
        'publishable': settings.STRIPE_PUBLISHABLE
    })
