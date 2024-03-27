from django.shortcuts import render, redirect
from .models import ClientAccount
from .models import Car
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import logout
from .forms import UserRegisterForm, ReservationForm, User


# Display the homepage of the website
def home(request):
    return render(request, 'frontend/home.html')


# Handle user registration with the user register form
# https://docs.djangoproject.com/en/5.0/topics/auth/default/
def user_register(request):
    # redirect to home if user is already logged in
    if request.user.is_authenticated:
        return redirect('home')
    
    # If form data is being submitted, save valid form data to create a new user
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            ClientAccount.objects.create(user=user)
            login(request, user)
            # https://docs.djangoproject.com/en/5.0/ref/contrib/messages/
            messages.success(request, "User profile successfully created.")
            return redirect('home')
    # If the request is GET, then display the form
    else:
        form = UserRegisterForm()
    return render(request, 'frontend/account/register.html', {'form': form})


# Handle user login with the authentication form
def user_login(request):
    # redirect to home if user is already logged in
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect users based on the account type
            # https://medium.com/djangotube/django-roles-groups-and-permissions-introduction-a54d1070544
            if user.is_superuser or user.is_staff:
                return redirect('/admin/')
            else:
                return redirect('home')
        else:
            return redirect('login')
    else:
        form = AuthenticationForm()
    return render(request, 'frontend/account/login.html', {'form': form})


# Handle user logout when the 'signout' button is clicked
def user_logout(request):
    logout(request)
    return redirect('home')


def make_reservation(request, id):
    car = Car.objects.get(pk=id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            try:
                user = User.objects.get(username=username)
                client_account, created = ClientAccount.objects.get_or_create(user=user)
                reservation = form.save(commit=False)
                reservation.client = client_account
                reservation.car = car
                reservation.save()
                car.availability = False
                car.save()
                messages.success(request, "Reservation successfully made.")
                return redirect('home')
            except User.DoesNotExist:
                form.add_error("username", "This username is not registered with any account.")
    else:
        form = ReservationForm(initial={'car': car})
    return render(request, 'frontend/reservation.html', {'form': form, 'car': car})


def car_list(request):
    car_list = Car.objects.all()
    return render(request, 'frontend/car_list.html', {'car_list': car_list})
