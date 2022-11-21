from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


def login(request):
    return render(request, 'users/login.html')

def registration(request):
    return render(request, 'users/registration.html')

def logout(request):
    pass

def cart(request):
    return render(request, 'users/cart.html')

def wishlist(request):
    return render(request, 'users/wishlist.html')
