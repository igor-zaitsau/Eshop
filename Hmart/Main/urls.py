from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('products/', all_products, name='all_products'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('product/<int:product_id>', single_product, name='single_product')
]