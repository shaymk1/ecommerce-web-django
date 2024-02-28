from django.shortcuts import render
from store.models import Product


def home(request):
    products = Product.objects.all().filter(is_available=True)
    context = {"products": products}
    return render(request, "store/home.html", context)


def store(request):
    return render(request, "store/store.html")
