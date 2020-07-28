from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from .forms import UserLoginForm, UserRegistrationForm, EditUserForm, EditUserPasswordForm
from cars.models import Car
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


def login(request):
    """A view that manages the login form"""
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request.POST['username_or_email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                request.session['user_id'] = user.id

                if request.GET and request.GET['next'] != '':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                user_form.add_error(None,
                                    "Your username or password are incorrect")
    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)


@login_required
def profile(request):
    """A view that displays the profile page of a logged in user"""

    car_owner = request.user
    user_cars = Car.objects.filter(car_owner=car_owner)

    return render(request, 'profile.html', {'cars': user_cars})


@login_required
def visit_profile(request, user_id):
    """Function to allow a user to visit other users' profile pages"""

    visited_user = User.objects.get(pk=user_id)
    user_cars = Car.objects.filter(car_owner=visited_user)

    return render(request, 'profile.html',
                  {'user': visited_user, 'cars': user_cars})


def register(request):
    """A view that manages the registration form"""

    if request.user.is_authenticated():
        messages.success(request, "You are already registered")
        return redirect(reverse('index'))
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))

            else:
                messages.error(request, "Unable to register at this time!")
        else:
            messages.error(request,
                           "Please fill the required fields correctly")
    else:
        user_form = UserRegistrationForm()

    args = {'user_form': user_form}
    return render(request, 'register.html', args)


@login_required
def edit_user_view(request, user_id):
    """Function to allow user to edit their own profile"""

    u = User.objects.get(pk=user_id)

    if request.method == 'POST':
        form = EditUserForm(request.POST)
        pwform = EditUserPasswordForm(request.POST)

        if form.is_valid():
            if form['username'].value():
                u.username = request.POST.get('username')
                u.save()
            if form['first_name'].value():
                u.first_name = request.POST.get('first_name')
                u.save()
            if form['last_name'].value():
                u.last_name = request.POST.get('last_name')
                u.save()
            if form['email'].value():
                u.email = request.POST.get('email')
                u.save()

        if pwform.is_valid():
            if pwform['password1'].value() and pwform['password2'].value():
                if pwform['password1'].value() == pwform['password2'].value():
                    u = User.objects.get(pk=user_id)
                    u.set_password(pwform['password2'].value())
                    u.save()
                    messages.success(
                        request,
                        "Your password was successfully updated!"
                    )
                else:
                    messages.error(
                        request,
                        "Make sure the password is the same on both fields"
                    )
            if pwform['password1'].value() != pwform['password2'].value():
                messages.error(
                    request,
                    "Make sure the password is the same on both fields"
                )

        return redirect(reverse('index'))

    else:
        form = EditUserForm()
        pwform = EditUserPasswordForm()

    args = {'edit_user_form': form, 'edit_pw_form': pwform, 'user': u}
    return render(request, 'editprofile.html', args)


@login_required
def del_user(request, user_id):
    """Function to allow users to delete their own profile"""

    u = User.objects.get(pk=user_id)
    u.delete()
    messages.success(request, "The user is deleted")

    return redirect(reverse('index'))
