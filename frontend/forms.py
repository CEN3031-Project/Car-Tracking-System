from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Reservation


# Customize the user form to include fields for an email, first name, and last name
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")


class ReservationForm(forms.ModelForm):
    rental_date = forms.DateTimeField(required=True)
    return_date = forms.DateTimeField(required=True)

    class Meta:
        model = Reservation
        fields = ['car', 'client', 'rental_date', 'return_date']
