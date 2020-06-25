from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    """Class for the car object"""

    CAR_CLASS_CHOICES = [
        ('Custom Classic', 'Custom Classic'),
        ('Luxury', 'Luxury'),
        ('Supersport', 'Supersport')
    ]
    YEAR_CHOICES = [(i, i) for i in range(1800, 2021)]
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
    PASSENGER_CHOICES = [(i, i) for i in range(1, 30)]
    DOORS_CHOICES = [(i, i) for i in range(1, 10)]
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

    car_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # user_id = models.CharField(max_length=10)
    car_class = models.CharField(max_length=40, choices=CAR_CLASS_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    brand = models.CharField(max_length=30, default='')
    model = models.CharField(max_length=30, default='')
    year = models.DecimalField(max_digits=4,
                               decimal_places=0, choices=YEAR_CHOICES)
    engine = models.CharField(max_length=10, default='')
    transmission = models.CharField(max_length=20,
                                    choices=TRANSMISSION_CHOICES)
    fuel = models.CharField(max_length=50, choices=FUEL_CHOICES)
    passengers = models.DecimalField(max_digits=10,
                                     decimal_places=0,
                                     choices=PASSENGER_CHOICES)
    doors = models.DecimalField(max_digits=10,
                                decimal_places=0, choices=DOORS_CHOICES)
    accessories = models.CharField(max_length=200, choices=ACCESSORIES_CHOICES)
    city = models.CharField(max_length=10, choices=CITY_CHOICES)
    county = models.CharField(max_length=10, choices=COUNTY_CHOICES)
    country = models.CharField(max_length=10, choices=COUNTRY_CHOICES)
    image1 = models.ImageField(upload_to='media/images')
    image2 = models.ImageField(upload_to='media/images')
    image3 = models.ImageField(upload_to='media/images')
    image4 = models.ImageField(upload_to='media/images')
    image5 = models.ImageField(upload_to='media/images')
    guidelines = models.TextField(max_length=500)

    def __str__(self):
        car_description = [str(self.year), str(self.brand), str(self.model)]
        return ' '.join(car_description)
