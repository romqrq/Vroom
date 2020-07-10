from django.db import models
from cars.models import Car


class Order(models.Model):
    """Model for Order"""

    first_name = models.CharField(max_length=40, blank=False)
    last_name = models.CharField(max_length=40, blank=False)
    phone_number = models.CharField(max_length=40, blank=False)
    address1 = models.CharField(max_length=80, blank=False)
    address2 = models.CharField(max_length=80, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=True)
    country = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2} {3}".format(
            self.id, self.date, self.first_name, self.last_name
        )


class OrderLineItem(models.Model):
    """Model for each line in the order representing a product"""

    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    car = models.ForeignKey(Car,on_delete=models.PROTECT, null=False)
    rental_days = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} {2} @ {3} per day".format(
            self.rental_days, self.car.brand,
            self.car.model, self.car.price
        )
