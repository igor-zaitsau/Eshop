from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def home(request):
    return render(request, 'Main/home.html')

def single_product(request):
    return render(request, 'Main/single-product.html')

def about(request):
    return render(request, 'Main/about.html')

def contact(request):
    return render(request, 'Main/contact.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound("Error 404")
