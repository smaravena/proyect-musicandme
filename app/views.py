from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def discos(request):
    return render(request, 'app/discos.html')

def instrumentos(request):
    return render(request, 'app/instrumentos.html')

def carro(request):
    return render(request, 'app/carro.html')

def login(request):
    return render(request, 'app/login.html')