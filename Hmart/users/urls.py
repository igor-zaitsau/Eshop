from django.urls import path, include

from .views import *

urlpatterns = [
    #path('login/', login, name='login'),
    #path('logout/', logout, name='logout'),
    #path('registration', registration, name='registration'),
    path('cart/', cart, name='cart'),
    path('wishlist/', wishlist, name='wishlist'),
    path("signup/", SignUp.as_view(), name="signup"),
]