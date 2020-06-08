from django.db import models


class Car(models.Model):
    """Class for the car object"""

    price = models.DecimalField(max_digits=6, decimal_places=2)
    brand = models.CharField(max_length=30, default='')
    model = models.CharField(max_length=30, default='')
    year = models.CharField(max_length=4, default='')
    engine = models.CharField(max_length=10, default='')
    transmission = models.CharField(max_length=10, default='')
    fuel = models.CharField(max_length=40, default='')
    passengers = models.CharField(max_length=10, default='')
    doors = models.CharField(max_length=10, default='')
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
