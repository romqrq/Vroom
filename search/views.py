from django.shortcuts import render
from django.contrib import messages
from cars.models import Car


def do_search(request):
    """
    Function to generate search results on findcar page based
    on the "cars" object built from the filter function applied
    to the form named "search_value"
    """
    search_key = request.GET['search_key']

    if search_key == 'Brand':
        cars = Car.objects.filter(brand__icontains=request.GET['search_value'])
    if search_key == 'Model':
        cars = Car.objects.filter(model__icontains=request.GET['search_value'])
    if search_key == 'Year':
        cars = Car.objects.filter(year__icontains=request.GET['search_value'])
    if search_key == 'Location':
        cars = Car.objects.filter(city__icontains=request.GET['search_value'])

    if not cars:
        messages.error(request, "Sorry, there are no results for this search.")

    return render(request, 'findcar.html', {'cars': cars})
