from django.db import models


class Car(models.Model):
    """Class for the car object"""

    CAR_CLASS_CHOICES = [
        ('CC', 'Custom Classic'),
        ('LX', 'Luxury'),
        ('SS', 'Supersport')
    ]
    YEAR_CHOICES = [(i, i) for i in range(1800, 2021)]
    TRANSMISSION_CHOICES = [
        ('AT', 'Automatic'),
        ('MT', 'Manual')
    ]
    FUEL_CHOICES = [
        ('D', 'Diesel'),
        ('E', 'Full Electric'),
        ('H', 'Hybrid'),
        ('P', 'Petrol')
    ]
    PASSENGER_CHOICES = [(i, i) for i in range(1, 30)]
    DOORS_CHOICES = [(i, i) for i in range(1, 10)]
    CITY_CHOICES = [
        ('DUB', 'Dublin'),
        ('COR', 'Cork'),
        ('GAL', 'Galway')
    ]
    COUNTY_CHOICES = [
        ('CTDUB', 'Dublin'),
        ('CTCOR', 'Cork'),
        ('CTGAL', 'Galway')
    ]
    COUNTRY_CHOICES = [('IRE', 'Ireland')]

    car_class = models.CharField(max_length=30, choices=CAR_CLASS_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    brand = models.CharField(max_length=30, default='')
    model = models.CharField(max_length=30, default='')
    year = models.DecimalField(max_digits=4,
                               decimal_places=0, choices=YEAR_CHOICES)
    engine = models.CharField(max_length=10, default='')
    transmission = models.CharField(max_length=10,
                                    choices=TRANSMISSION_CHOICES)
    fuel = models.CharField(max_length=40, choices=FUEL_CHOICES)
    passengers = models.DecimalField(max_digits=10,
                                     decimal_places=0,
                                     choices=PASSENGER_CHOICES)
    doors = models.DecimalField(max_digits=10,
                                decimal_places=0, choices=DOORS_CHOICES)
    accessories = models.CharField(max_length=200, default='')
    city = models.CharField(max_length=10, choices=CITY_CHOICES)
    county = models.CharField(max_length=10, choices=COUNTY_CHOICES)
    country = models.CharField(max_length=10, choices=COUNTRY_CHOICES)
    image1 = models.ImageField(upload_to='media/images')
    image2 = models.ImageField(upload_to='media/images')
    image3 = models.ImageField(upload_to='media/images')
    image4 = models.ImageField(upload_to='media/images')
    image5 = models.ImageField(upload_to='media/images')
    guidelines = models.TextField()

    def __str__(self):
        return self.brand
