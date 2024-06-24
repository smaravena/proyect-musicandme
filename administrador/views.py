from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import Genero,Disco,Tipo_instrumento,Instrumento
from .forms import formDisco
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
@login_required
def discoAdd(request):
    #entregando formulario a discoAdd.html
    context={'form':formDisco()}
    if request.method=='POST':
        formulario=formDisco(request.POST,files=request.FILES)
        if formulario.is_valid:
            #procedimiento para guardar en la base de datos
            formulario.save()
            #mensaje de confirmación
            context={'mensaje':'Disco agregado con exito'}
    return render(request,'administrador/discoAdd.html',context)
@login_required
def discoEdit(request,pk):
    #buscar disco para formulario segun la ID del disco
    disco=Disco.objects.get(id_disco = pk)
    context= {'form':formDisco(instance=disco)}
    if request.method=='POST':
        form=formDisco(data=request.POST,files=request.FILES,instance=disco)
        #validacion de campos del formulario
        if form.is_valid:
            #guardar datos editados en la BASE DE DATOS
            form.save()
            context={'mensaje':'Disco modificado con exito'}
    return render(request,'administrador/discosEdit.html',context)

def discoDelete(request,pk):
    disco= Disco.objects.get(id_disco=pk)
    disco.delete()
    return redirect(to='viewdisco')

           



