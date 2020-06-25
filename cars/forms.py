from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Car
# from django.core.exceptions import ValidationError


class CarRegistrationForm(ModelForm):

    # CAR_CLASS_CHOICES = [
    #     ('Custom Classic', 'Custom Classic'),
    #     ('Luxury', 'Luxury'),
    #     ('Supersport', 'Supersport')
    # ]
    # YEAR_CHOICES = [(i, i) for i in range(1900, 2021)]
    # TRANSMISSION_CHOICES = [
    #     ('Automatic', 'Automatic'),
    #     ('Manual', 'Manual')
    # ]
    # FUEL_CHOICES = [
    #     ('Diesel', 'Diesel'),
    #     ('Full Electric', 'Full Electric'),
    #     ('Hybrid', 'Hybrid'),
    #     ('Petrol', 'Petrol')
    # ]
    # PASSENGER_CHOICES = [(i, i) for i in range(1, 30)]
    # DOORS_CHOICES = [(i, i) for i in range(1, 10)]
    # ACCESSORIES_CHOICES = [
    #     ('Basic', 'Basic'),
    #     ('Standard', 'Standard'),
    #     ('Custom', 'Custom')
    # ]
    # CITY_CHOICES = [
    #     ('Dublin', 'Dublin'),
    #     ('Cork', 'Cork'),
    #     ('Galway', 'Galway')
    # ]
    # COUNTY_CHOICES = [
    #     ('Dublin', 'Dublin'),
    #     ('Cork', 'Cork'),
    #     ('Galway', 'Galway')
    # ]
    # COUNTRY_CHOICES = [('Ireland', 'Ireland')]

    # user_id = forms.CharField(widget=forms.HiddenInput())
    # user_id = User.objects.create(user_id=request.user.id)
    # car_class = forms.ChoiceField(choices=CAR_CLASS_CHOICES)
    # price = forms.DecimalField(max_digits=6, decimal_places=2)
    # brand = forms.CharField(max_length=30)
    # model = forms.CharField(max_length=30)
    # year = forms.ChoiceField(choices=YEAR_CHOICES)
    # engine = forms.CharField(max_length=10)
    # transmission = forms.ChoiceField(choices=TRANSMISSION_CHOICES)
    # fuel = forms.ChoiceField(choices=FUEL_CHOICES)
    # passengers = forms.ChoiceField(choices=PASSENGER_CHOICES)
    # doors = forms.ChoiceField(choices=DOORS_CHOICES)
    # accessories = forms.ChoiceField(choices=ACCESSORIES_CHOICES)
    # city = forms.ChoiceField(choices=CITY_CHOICES)
    # county = forms.ChoiceField(choices=COUNTY_CHOICES)
    # county = forms.ChoiceField(choices=COUNTRY_CHOICES)
    # image1 = forms.ImageField()
    # image2 = forms.ImageField()
    # image3 = forms.ImageField()
    # image4 = forms.ImageField()
    # image5 = forms.ImageField()
    guidelines = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Car
        fields = [
            'car_class', 'price', 'brand', 'model', 'year', 'engine',
            'transmission', 'fuel', 'passengers', 'doors',
            'accessories', 'city', 'county', 'country', 'image1',
            'image2', 'image3', 'image4', 'image5', 'guidelines'
        ]
