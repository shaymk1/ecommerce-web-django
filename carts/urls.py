from django.urls import path
from . import views

# from ..core import views

urlpatterns = [
    path("", views.carts, name="cart"),
 
]
