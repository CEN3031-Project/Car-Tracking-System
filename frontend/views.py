from django.shortcuts import render, redirect
from .models import ClientAccount
from .models import Car
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django import forms
from django.contrib.auth import logout


# Display the homepage of the website
def home(request):
    return render(request, 'frontend/home.html')


# Customize the user form to include fields for an email, first name, and last name
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")


# Handle user registration with the user register form
# https://docs.djangoproject.com/en/5.0/topics/auth/default/
def user_register(request):
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
    return render(request, 'account/register.html', {'form': form})


# Handle user login with the authentication form
def user_login(request):
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
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})


# Handle user logout when the 'signout' button is clicked
def user_logout(request):
    logout(request)
    return redirect('home')

def car_list(request):
    car_list = Car.objects.all()
    return render(request, 'frontend/car_list.html', {'car_list': car_list})

def update_availability(request, car_id):
    car = Car.objects.get(pk=car_id)
    car.availability = not car.availability
    car.save()
    return redirect('/cars/')