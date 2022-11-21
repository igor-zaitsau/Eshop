from django.urls import path

from .views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('cart/', cart, name='cart'),
    path('wishlist/', wishlist, name='wishlist'),
]