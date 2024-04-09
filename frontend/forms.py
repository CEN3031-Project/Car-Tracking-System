from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Reservation


# Customize the user form to include fields for an email, first name, and last name
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class ReservationForm(forms.ModelForm):
    rental_date = forms.DateTimeField(
        required=True,
        help_text="Example: 01/20/2024, 9:30 AM",
        input_formats=['%m/%d/%Y, %I:%M %p'],
    )
    return_date = forms.DateTimeField(
        required=True,
        help_text="Example: 01/27/2024, 4:30 PM",
        input_formats=['%m/%d/%Y, %I:%M %p'],
    )
    username = forms.CharField(required=True)

    class Meta:
        model = Reservation
        fields = ["car", "username", "rental_date", "return_date"]
