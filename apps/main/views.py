from django.shortcuts import render
from .models import Event, Establishment, Band


def home(request):
    return render(request, 'home.html', {})


def sign_in(request):
    return render(request, 'registration/login.html', {})


def sign_up(request):
    return render(request, 'signup.html', {})





