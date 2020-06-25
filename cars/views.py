from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Car
from django.contrib.auth.models import User
# from django.db.models import Q
from .forms import CarRegistrationForm


def all_cars(request):
    """Function to display all cars into the search page"""

    cars = Car.objects.all()
    return render(request, "findcar.html", {"cars": cars})


def custom_classic_only(request):
    """Function to display only Custom Classic cars into the search page"""

    CS = Car.objects.filter(car_class="Custom Classic")
    return render(request, "findcar.html", {"cars": CS})


def luxury_only(request):
    """Function to display only Luxury cars into the search page"""

    LX = Car.objects.filter(car_class="Luxury")
    return render(request, "findcar.html", {"cars": LX})


def supersport_only(request):
    """Function to display only Supersport cars into the search page"""

    SS = Car.objects.filter(car_class="Supersport")
    return render(request, "findcar.html", {"cars": SS})


def car_register(request):
    """Function to allow users to add their cars to the database"""

    if request.method == 'POST':
        # print(request.user)
        # this_user = User.objects.create(request.user)
        form = CarRegistrationForm(request.POST, request.FILES)
        # print(this_user)
        if form.is_valid():
            # print(form['car_owner'])
            print('VALIDATED')
            # car_reg_form = form
            car_reg_form = form.save(commit=False)
            car_reg_form.car_owner = request.user
            form.save()

            messages.error(request, "Your car is ready to Vroom!")
            return redirect(reverse('index'))
        else:
            # print('FAILED VALIDATION')
            messages.error(
                request,
                "We were unable to add your car! Please check the information"
            )

    else:
        car_reg_form = CarRegistrationForm()

    args = {'car_reg_form': car_reg_form}
    return render(request, 'rentmycar.html', args)


def car_detail(request, car_id):
    """
    Function to display expanded details of the chosen car based on its ID
    """

    car = Car.objects.get(pk=car_id)
    # car_owner = User.objects.get(pk=car.car_owner)
# , 'car_owner': car_owner
    return render(request, 'cardetail.html', {'car': car})


def car_edit_form(request, car_id):
    """Function to allow user to edit their own cars"""

    this_car = Car.objects.get(pk=car_id)

    if request.method == 'POST':
        form = CarRegistrationForm(request.POST, request.FILES)

        if form.is_valid():
            for key in form:
                if this_car.key != key:
                    this_car.key = key
                    this_car.save()

            messages.error(request, "Your car has been successfully updated!")
            return redirect(reverse('index'))
        else:
            messages.error(
                request,
                "We were unable to update your car!"
            )

    else:
        car_edit_form = CarRegistrationForm(this_car)

    return render(request, 'rentmycar.html', {'car_edit_form': car_edit_form})
