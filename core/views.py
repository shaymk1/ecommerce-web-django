from django.shortcuts import render


def home(request):
    return render(request, 'store/index.html')


def store(request):
    return render(request, 'store/store.html')