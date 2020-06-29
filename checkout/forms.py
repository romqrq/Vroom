from django import forms
from .models import Order


class MakePaymentForm(forms.Form):
    """
    Defines form used by user to make payment
    and information passed to stripe
    """

    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2040)]

    credit_card_number = forms.CharField(label='Credit Card Number',
                                         required=False)
    cvv = forms.CharField(label='Security Code (CVV)',
                          required=False)
    expiry_month = forms.ChoiceField(label='Month',
                                     choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year',
                                    choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput())


class OrderForm(forms.ModelForm):
    """"""

    class Meta:
        model = Order
        fields = (
            'first_name', 'last_name', 'phone_number', 'address1',
            'address2', 'postcode', 'city', 'county', 'country'
        )
