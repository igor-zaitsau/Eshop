from django.urls import path, include

from .views import *

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('wishlist/', wishlist, name='wishlist'),
    path('signup/', SignUp.as_view(), name="signup"),
]