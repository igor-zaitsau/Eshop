from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *

def home(request):
    new_products = ProductModel.objects.all().order_by('-time_create')[:8]
    return render(request, 'Main/home.html', {'title': 'Главная страница', 'new_products': new_products})

def all_products(request):
    products = ProductModel.objects.all()
    category = CategoryModel.objects.all()
    brand = BrandModel.objects.all()
    context = {
        'title': 'Все товары',
        'products': products,
        'category': category,
        'brand': brand
    }
    return render(request, 'Main/all-products.html', context=context)

def single_product(request, product_id):
    product = ProductModel.objects.get(pk=product_id)
    return render(request, 'Main/single-product.html', {'product': product})

def about(request):
    return render(request, 'Main/about.html', {'title': 'О нас'})

def contact(request):
    return render(request, 'Main/contact.html', {'title': 'Контакты'})

def pageNotFound(request, exception):
    return HttpResponseNotFound("Error 404")
