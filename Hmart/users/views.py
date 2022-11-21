from django.shortcuts import render

def login(request):
    return render(request, 'users/login.html')

def logout(request):
    pass

def cart(request):
    return render(request, 'users/cart.html')

def wishlist(request):
    return render(request, 'users/wishlist.html')
