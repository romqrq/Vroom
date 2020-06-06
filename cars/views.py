from django.shortcuts import render
from .models import Car


def all_cars(request):
    cars = Car.objects.all()
    return render(request, "findcar.html", {"cars": cars})
