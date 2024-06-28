from django.shortcuts import render
from .models import Genero, Disco, Tipo_instrumento, Instrumento

# Create your views here.

def inicio(request):
    contex = {}
    return render(request, 'app/index.html')

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
def lista_discos(request):
    discos = Disco.objects.all()  # Obtener todos los objetos Disco de la base de datos
    return render(request, 'app/lista_discos.html', {'discos': discos})
def lista_instrumentos(request):
    instrumento = Instrumento.objects.all()  # Obtener todos los objetos Disco de la base de datos
    return render(request, 'app/lista_instrumentos.html', {'instrumento': instrumento})