from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def home(request):
    return render(request, 'Main/home.html', {'title': 'Главная страница'})

def all_products(request):
    return render(request, 'Main/all-products.html', {'title': 'Все товары'})

def single_product(request):
    return render(request, 'Main/single-product.html')

def about(request):
    return render(request, 'Main/about.html', {'title': 'О нас'})

def contact(request):
    return render(request, 'Main/contact.html', {'title': 'Контакты'})

def pageNotFound(request, exception):
    return HttpResponseNotFound("Error 404")
