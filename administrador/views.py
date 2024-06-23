from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import Genero,Disco,Tipo_instrumento,Instrumento
from .forms import formDisco
# Create your views here.
@login_required
def homeadm(request):
    context = {}
    return render(request,'administrador/test.html',context)
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



