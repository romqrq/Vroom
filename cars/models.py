from django.db import models


class Car(models.Model):
    """Class for the car object"""

    TRANSMISSION_OPTIONS = ['Manual', 'Automatic']
    FUEL_OPTIONS = ['Diesel', 'Full Electric', 'Gasoline', 'Hybrid', 'Other']
    # PASSENGER_OPTIONS = [(i, i) for i in (1, 10+)]
    # DOORS_OPTIONS = [(i, i) for i in (1, 6+)]

    price = models.DecimalField(max_digits=6, decimal_places=2)
    brand = models.CharField(max_length=30, default='')
    model = models.CharField(max_length=30, default='')
    year = models.CharField(max_length=4, default='')
    engine = models.CharField(max_length=10, default='')
    # transmission = GET OPTIONS
    # fuel = GET OPTIONS
    # passengers = GET OPTIONS
    # doors = GET OPTIONS
    accessories = models.CharField(max_length=200, default='')
    city = models.CharField(max_length=10, default='')
    county = models.CharField(max_length=10, default='')
    country = models.CharField(max_length=10, default='')
    image1 = models.ImageField(upload_to='images')
    image2 = models.ImageField(upload_to='images')
    image3 = models.ImageField(upload_to='images')
    image4 = models.ImageField(upload_to='images')
    image5 = models.ImageField(upload_to='images')
    guidelines = models.TextField()

    def __str__(self):
        return self.brand
