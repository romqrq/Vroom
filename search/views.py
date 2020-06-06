from django.shortcuts import render
from cars.models import Car


def do_search(request):
    """"""

    cars = Car.objects.filter(name__icontains=request.GET['q'])
    return render(request, 'findcar.html', {'cars': cars})
