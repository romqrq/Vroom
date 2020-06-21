from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Car
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import CarRegistrationForm


def all_cars(request):
    """Function to display all cars into the search page"""
    cars = Car.objects.all()
    return render(request, "findcar.html", {"cars": cars})


def custom_classic_only(request):
    """Function to display only Custom Classic cars into the search page"""
    CS = []
    for car in Car.objects.all():
        if car.car_class == 'Custom Classic':
            CS.append(car)
    return render(request, "findcar.html", {"cars": CS})


def luxury_only(request):
    """Function to display only Luxury cars into the search page"""
    LX = []
    for car in Car.objects.all():
        if car.car_class == 'Luxury':
            LX.append(car)
    return render(request, "findcar.html", {"cars": LX})


def supersport_only(request):
    """Function to display only Supersport cars into the search page"""
    SS = []
    for car in Car.objects.all():
        if car.car_class == 'Supersport':
            SS.append(car)
    return render(request, "findcar.html", {"cars": SS})


def car_register(request):
    """Function to allow users to add their cars to the database"""

    if request.method == 'POST':
        form = CarRegistrationForm(request.POST, request.FILES)

        if form.is_valid():
            car_reg_form = form.save(commit=False)
            car_reg_form.user_id = request.user.id
            car_reg_form.save()

            messages.error(request, "Your car is ready to Vroom!")
            return redirect(reverse('index'))
        else:
            messages.error(
                request,
                "We were unable to add your car! Please check the information"
            )

    else:
        car_reg_form = CarRegistrationForm()

    args = {'car_reg_form': car_reg_form}
    return render(request, 'rentmycar.html', args)


def car_detail(request, car_id):
    """Function to display expanded details of the chosen car based on its ID"""

    all_cars = Car.objects.all()
    all_users = User.objects.all()

    for car in all_cars:

        if car.id == int(car_id):
            for owner in all_users:
                # print(type(user.id))
                # print(type(car.user_id))
                if owner.id == int(car.user_id):
                    # print(user.id)
                    # print(car.user_id)
                    car_owner = owner
                    # print(car_owner.email)
                    return render(request, 'cardetail.html', {'car': car, 'car_owner': car_owner})
    # return render(request, 'cardetail.html')
