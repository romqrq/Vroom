from django.shortcuts import render
from cars.models import Car


def do_search(request):
    """
    Function to generate search results on findcar page based
    on the "cars" object built from the filter function applied
    to the form named "q"
    """

    cars = Car.objects.filter(brand__icontains=request.GET['q'])
    return render(request, 'findcar.html', {'cars': cars})
