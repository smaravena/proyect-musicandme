from django.shortcuts import render
from .models import Genero, Disco, Tipo_instrumento, Instrumento

# Create your views here.

def home(request):
    contex = {}
    return render(request, 'app/home.html')

def discos(request):
    return render(request, 'app/discos.html')

def instrumentos(request):
    return render(request, 'app/instrumentos.html')

def carro(request):
    return render(request, 'app/carro.html')

def login(request):
    return render(request, 'app/login.html')

# VISTA BASE DE DATOS
#def discos_list(request):
    ##DEFINIR OBJ PARA TRAER DE LA BD
    #Alumno.objects.all() <=> 'Select * From Alumnos'
    discos = Disco.objects.all() 
    contex = {'discos' : discos}
    return render(request,'app/discos_list.html',contex)