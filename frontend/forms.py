from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Reservation, ClientAccount


# Customize the user form to include fields for an email, first name, and last name
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))

    # Associate the user form with the user model and appropriate fields
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


# Define a model form for creating or updating reservations
class ReservationForm(forms.ModelForm):

    # Use the date time field for rental dates and read the input in the same format as the example
    rental_date = forms.DateTimeField(
        required=True,
        help_text="Example: 01/20/2024",
        input_formats=['%m/%d/%Y'],
    )
    return_date = forms.DateTimeField(
        required=True,
        help_text="Example: 01/27/2024",
        input_formats=['%m/%d/%Y'],
    )
    username = forms.CharField(required=True)

    class Meta:
        model = Reservation
        fields = ["username", "rental_date", "return_date"]


# Define a model form for creating a client account in the database
class ClientAccountForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = ClientAccount
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    # Create a new user object using the data from the form
    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name']
        )
        # Link the new `ClientAccount` to the created `User` instance and save it
        client_account = super(ClientAccountForm, self).save(commit=False)
        client_account.user = user
        # Commit changes to the database only when the user object is ready
        if commit:
            client_account.save()
        return client_account
