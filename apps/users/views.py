from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm


def registration_view(request):
    context = {}
    if request.POST:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")

            account = authenticate(username=username, password=raw_password)
            login(request, account)
            return redirect('index')
        else:
            context['form'] = form
    else:
        form = CustomUserCreationForm()
        context['form'] = form
    return render(request, 'register.html', context)


