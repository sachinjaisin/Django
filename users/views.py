from django.shortcuts import render

# Create your views here.
# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            # Optionally log in the user after registration
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)

            messages.success(request, "Registration successful!")
        else:
            messages.error(request, "Error in registration.")
    else:
        form = UserRegistrationForm()
    
    return render(request, 'users/register.html', {'form': form})
