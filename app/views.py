from django.shortcuts import render,redirect, get_object_or_404
from .models import Genero, Disco, Tipo_instrumento, Instrumento,Carrito,ElementoCarrito
from .forms import CarritoForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.db import IntegrityError
from django.db import transaction

# Create your views here.

def inicio(request):
    contex = {}
    return render(request, 'app/index.html')

def discos(request):
    return render(request, 'app/discos.html')

def instrumentos(request):
    return render(request, 'app/instrumentos.html')


def lista_carro(request):
    return render(request, 'app/lista_carro.html')

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
    #obtenemos la id del genero para poder hacer el filtro
    genero_id = request.GET.get('genero', None)
    if genero_id:
        discos = Disco.objects.filter(id_genero_id=genero_id)
    else:
        discos = Disco.objects.all()
    generos = Genero.objects.all()
    return render(request, 'app/lista_discos.html', {'discos': discos, 'generos': generos})
def lista_instrumentos(request):
    #obtenemos la id del tipo dei instrumento para hacer el filtro
    tipo_id=request.GET.get('tipo',None)
    if tipo_id:
        instrumentos = Instrumento.objects.filter(id_tipo=tipo_id)
    else:
        instrumentos = Instrumento.objects.all()
    tipos = Tipo_instrumento.objects.all()        
    return render(request, 'app/lista_instrumentos.html', {'instrumento': instrumentos,'tipos': tipos})

@csrf_exempt

def agregar_al_carrito(request):
    if request.method == 'POST':
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        
        disco_id = request.POST.get('disco_id')
        cantidad = int(request.POST.get('cantidad', 1))  # Por defecto 1 si no se especifica cantidad
        disco = get_object_or_404(Disco, id_disco=disco_id)

        if cantidad > disco.stock:
            return JsonResponse({'mensaje': 'Cantidad solicitada excede el stock disponible.'}, status=400)
        
        carrito, created = Carrito.objects.get_or_create(session_key=session_key)
        
        try:
            elemento, elemento_created = ElementoCarrito.objects.get_or_create(
                carrito=carrito,
                disco=disco,
                defaults={'cantidad': cantidad}
            )
        
            if not elemento_created:
                if elemento.cantidad + cantidad > disco.stock:
                    return JsonResponse({'mensaje': 'Cantidad total solicitada excede el stock disponible.'}, status=400)
                elemento.cantidad += cantidad
                elemento.save()
        
            return JsonResponse({'mensaje': 'Elemento(s) agregado(s) al carrito', 'cantidad': elemento.cantidad})
        except IntegrityError as e:
            return JsonResponse({'mensaje': 'Error al agregar el elemento al carrito.'}, status=500)

    return JsonResponse({'mensaje': 'Solicitud inválida'}, status=400)
def ver_carrito(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key
    
    carrito = Carrito.objects.filter(session_key=session_key).first()
    context = {'carrito': carrito}
    return render(request, 'app/ver_carrito.html', context)
def confirmar_compra(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    carrito = get_object_or_404(Carrito, session_key=session_key)
    
    if request.method == 'POST':
        form = CarritoForm(request.POST, instance=carrito)
        if form.is_valid():
            with transaction.atomic():
                for elemento in carrito.elementos.all():
                    if elemento.disco:
                        disco = elemento.disco
                        if elemento.cantidad > disco.stock:
                            return JsonResponse({'mensaje': f'El stock de {disco.nombre} es insuficiente para la cantidad solicitada.'}, status=400)
                        disco.stock -= elemento.cantidad
                        disco.save()
                    elif elemento.instrumento:
                        instrumento = elemento.instrumento
                        if elemento.cantidad > instrumento.stock:
                            return JsonResponse({'mensaje': f'El stock de {instrumento.nombre} es insuficiente para la cantidad solicitada.'}, status=400)
                        instrumento.stock -= elemento.cantidad
                        instrumento.save()
                form.save()
                carrito.fecha_modificacion = timezone.now()
                carrito.save()
            return redirect('inicio')  # Redirigir a una página de éxito después de confirmar la compra
    else:
        form = CarritoForm(instance=carrito)

    return render(request, 'app/carro.html', {'form': form, 'carrito': carrito})

