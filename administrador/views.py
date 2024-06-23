from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import Genero,Disco,Tipo_instrumento,Instrumento
# Create your views here.
@login_required
def index(request):
    context = {}
    return render(request,'administrador/index.html',context)
@login_required
def viewDisco(request):
    discos=Disco.objects.all()
    return render(request, 'administrador/lista_discosAdm.html', {'discos': discos})
@login_required
def viewInstrum(request):
    instrumento=Instrumento.objects.all()
    return render(request, 'administrador/lista_instrumAdm.html', {'instrumento': instrumento})



