from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from .models import OrderLineItem
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from django.conf import settings
from django.utils import timezone
from cars.models import Car, TrackDayAddon, InsuranceAddon, PrivateDriverAddon
import stripe


stripe.api_key = settings.STRIPE_SECRET


@login_required
def checkout(request):
    """View to display checkout with relevant information for user"""

    stripe.api_key = settings.STRIPE_SECRET

    if request.method == "POST":
        # getting user and payment information posted
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.customer = request.user
            order.save()

            # Getting from session information of what is being purchased
            # and adding to both the order line and the order itself
            cart = request.session.get('cart', {})
            total = 0

            for item_type, item_dic in cart.items():
                if item_type == 'car':
                    item = get_object_or_404(
                        Car,
                        pk=cart['car']['item_id'])
                    total += item_dic['quantity'] * item.price
                    order_line_item = OrderLineItem(
                        order=order,
                        car=item,
                        rental_days=item_dic['quantity']
                    )
                    order.car = item

                elif item_type == 'track_day':
                    item = get_object_or_404(
                        TrackDayAddon,
                        pk=cart['track_day']['item_id'])
                    total += item_dic['quantity'] * item.price
                    order_line_item = OrderLineItem(
                        order=order,
                        track_day=item,
                        rental_days=item_dic['quantity']
                    )
                    order.track_day = item

                elif item_type == 'insurance':
                    item = get_object_or_404(
                        InsuranceAddon,
                        pk=cart['insurance']['item_id'])
                    total += item_dic['quantity'] * item.price
                    order_line_item = OrderLineItem(
                        order=order,
                        insurance=item,
                        rental_days=item_dic['quantity']
                    )
                    order.insurance = item

                elif item_type == 'private_driver':
                    item = get_object_or_404(
                        PrivateDriverAddon,
                        pk=cart['private_driver']['item_id'])
                    total += item_dic['quantity'] * item.price
                    order_line_item = OrderLineItem(
                        order=order,
                        private_driver=item,
                        rental_days=item_dic['quantity']
                    )
                    order.private_driver = item

                order_line_item.save()
                order.save()

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
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to take payment")
        # If one of the filled forms isn't valid
        else:
            messages.error(request,
                           "We were unable to take a payment with that card!")
    # If method isn't POST
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, 'checkout.html', {
        'order_form': order_form,
        'payment_form': payment_form,
        'publishable': settings.STRIPE_PUBLISHABLE
    })
