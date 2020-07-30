from django.db import models
from django.contrib.auth.models import User
from cars.models import Car, TrackDayAddon, InsuranceAddon, PrivateDriverAddon


class Order(models.Model):
    """Model for Order"""

    customer = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    car = models.ForeignKey(Car, on_delete=models.PROTECT, null=True)
    track_day = models.ForeignKey(
        TrackDayAddon,
        on_delete=models.PROTECT,
        null=True)
    insurance = models.ForeignKey(
        InsuranceAddon,
        on_delete=models.PROTECT,
        null=True)
    private_driver = models.ForeignKey(
        PrivateDriverAddon,
        on_delete=models.PROTECT,
        null=True)
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
        order_description = [
            str(self.id),
            str(self.date),
            str(self.car),
            str(self.customer)
            ]
        return ' - '.join(order_description)


class OrderLineItem(models.Model):
    """Model for each line in the order representing a product"""

    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    car = models.ForeignKey(Car, on_delete=models.PROTECT, null=True)
    track_day = models.ForeignKey(TrackDayAddon,
                                  on_delete=models.PROTECT, null=True)
    insurance = models.ForeignKey(InsuranceAddon,
                                  on_delete=models.PROTECT, null=True)
    private_driver = models.ForeignKey(PrivateDriverAddon,
                                       on_delete=models.PROTECT, null=True)
    rental_days = models.IntegerField(blank=False)
    
    if car:
        def __str__(self):
            return "{0} {1} per day".format(
                self.rental_days, self.car.brand,
                self.car.model, self.car.price
            )

    elif track_day:
        def __str__(self):
            return "{0} {1} {2} @ {3} per day".format(
                self.rental_days, self.track_day.title,
                self.track_day.coverage, self.track_day.price
            )
    elif insurance:
        def __str__(self):
            return "{0} {1} {2} @ {3} per day".format(
                self.rental_days, self.insurance.title,
                self.insurance.coverage, self.insurance.price
            )
    elif private_driver:
        def __str__(self):
            return "{0} {1} {2} @ {3} per day".format(
                self.rental_days, self.private_driver.title,
                self.private_driver.coverage, self.private_driver.price
            )
