from django import forms
from django.forms import ModelForm
from .models import Car


class CarRegistrationForm(ModelForm):

    price = forms.DecimalField(label='Rental price',
                               widget=forms.NumberInput(attrs={
                                   'placeholder': 'i.e. 500'
                                   }))
    brand = forms.CharField(label='Brand',
                            widget=forms.TextInput(attrs={
                                'placeholder': 'Brand of your car'
                                }))
    model = forms.CharField(label='Model',
                            widget=forms.TextInput(attrs={
                                'placeholder': 'Model of the car'
                                }))
    displacement = forms.DecimalField(label='Engine displacement',
                                      widget=forms.NumberInput(attrs={
                                          'placeholder': 'i.e. 3.2'
                                          }))
    passengers = forms.DecimalField(label='Seats',
                                    widget=forms.NumberInput(attrs={
                                        'placeholder': 'i.e. 5'
                                        }))
    doors = forms.DecimalField(label='Number of doors',
                               widget=forms.NumberInput(attrs={
                                   'placeholder': 'i.e. 2'
                                   }))
    image1 = forms.ImageField(label='Image 1')
    image2 = forms.ImageField(label='Image 2', required=False)
    image3 = forms.ImageField(label='Image 3', required=False)
    image4 = forms.ImageField(label='Image 4', required=False)
    image5 = forms.ImageField(label='Image 5', required=False)
    guidelines = forms.CharField(widget=forms.Textarea(attrs={
                                          'placeholder': "Tell other users about the car and set some guidelines to improve everyone's experience"
                                          }))

    class Meta:
        model = Car
        fields = [
            'car_class', 'price', 'brand', 'model', 'year', 'track_day',
            'engine_type', 'displacement', 'transmission', 'fuel',
            'passengers', 'doors', 'accessories', 'city', 'county', 'country',
            'image1', 'image2', 'image3', 'image4', 'image5', 'guidelines'
        ]


class CarUpdateForm(ModelForm):

    CAR_CLASS_CHOICES = [
        ('Custom Classic', 'Custom Classic'),
        ('Luxury', 'Luxury'),
        ('Supersport', 'Supersport')
    ]
    YEAR_CHOICES = [(i, i) for i in range(1900, 2021)]
    TRACK_DAY_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]
    ENGINE_TYPE_CHOICES = [
        ('Inline 3', 'Inline 3'),
        ('Inline 4', 'Inline 4'),
        ('Inline 6', 'Inline 6'),
        ('Boxer 4', 'Boxer 4'),
        ('Boxer 6', 'Boxer 6'),
        ('V6', 'V6'),
        ('V8', 'V8'),
        ('V10', 'V10'),
        ('V12', 'V12'),
        ('W10', 'W10'),
        ('W12', 'W12'),
        ('Other', 'Other')
    ]
    TRANSMISSION_CHOICES = [
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual')
    ]
    FUEL_CHOICES = [
        ('Diesel', 'Diesel'),
        ('Full Electric', 'Full Electric'),
        ('Hybrid', 'Hybrid'),
        ('Petrol', 'Petrol')
    ]
    ACCESSORIES_CHOICES = [
        ('Basic', 'Basic'),
        ('Standard', 'Standard'),
        ('Custom', 'Custom')
    ]
    CITY_CHOICES = [
        ('Dublin', 'Dublin'),
        ('Cork', 'Cork'),
        ('Galway', 'Galway')
    ]
    COUNTY_CHOICES = [
        ('Dublin', 'Dublin'),
        ('Cork', 'Cork'),
        ('Galway', 'Galway')
    ]
    COUNTRY_CHOICES = [('Ireland', 'Ireland')]

    car_class = forms.ChoiceField(choices=CAR_CLASS_CHOICES, required=False)
    price = forms.DecimalField(required=False)
    brand = forms.CharField(required=False)
    model = forms.CharField(required=False)
    year = forms.ChoiceField(choices=YEAR_CHOICES, required=False)
    track_day = forms.ChoiceField(choices=TRACK_DAY_CHOICES, required=False)
    engine_type = forms.ChoiceField(choices=ENGINE_TYPE_CHOICES,
                                    required=False)
    displacement = forms.DecimalField(max_digits=4, decimal_places=1,
                                      required=False)
    transmission = forms.ChoiceField(choices=TRANSMISSION_CHOICES,
                                     required=False)
    fuel = forms.ChoiceField(choices=FUEL_CHOICES, required=False)
    passengers = forms.DecimalField(max_digits=2, decimal_places=0,
                                    required=False)
    doors = forms.DecimalField(max_digits=2, decimal_places=0, required=False)
    accessories = forms.ChoiceField(choices=ACCESSORIES_CHOICES,
                                    required=False)
    city = forms.ChoiceField(choices=CITY_CHOICES, required=False)
    county = forms.ChoiceField(choices=COUNTY_CHOICES, required=False)
    country = forms.ChoiceField(choices=COUNTRY_CHOICES, required=False)
    image1 = forms.ImageField(required=False)
    image2 = forms.ImageField(required=False)
    image3 = forms.ImageField(required=False)
    image4 = forms.ImageField(required=False)
    image5 = forms.ImageField(required=False)
    guidelines = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Car
        fields = [
            'car_class', 'price', 'brand', 'model', 'year', 'track_day',
            'engine_type', 'displacement', 'transmission', 'fuel',
            'passengers', 'doors', 'accessories', 'city', 'county', 'country',
            'image1', 'image2', 'image3', 'image4', 'image5', 'guidelines'
        ]
