from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.contrib import messages
# from django.http import HttpResponse

# Display the homepage of the website
def home(request):
    return render(request, 'frontend/home.html')

# Handle user registration using Django's built-in UserCreationForm:
# https://docs.djangoproject.com/en/5.0/topics/auth/default/
def register(request):
    # If form data is being submitted, save valid form data to create a new user
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
        # https://docs.djangoproject.com/en/5.0/ref/contrib/messages/
        messages.success(request, "User profile successfully created.")
        return redirect('home')
    # If the request is GET, then display the form
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
