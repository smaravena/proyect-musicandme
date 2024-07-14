from django.urls import path
from .views import inicio, discos, instrumentos, lista_carro, login,lista_discos, lista_instrumentos,confirmar_compra,agregar_al_carrito

urlpatterns = [
    path('inicio', inicio, name="inicio"),
    path('discos', discos, name="discos"),
    path('instrumentos', instrumentos, name="instrumentos"),
    path('carro', confirmar_compra, name="carro"),
    path('lista_carro', lista_carro, name="lista_carro"),
    path('login', login, name="login"),
    path('lista_discos',lista_discos, name='lista_discos'),
    path('lista_instrumentos',lista_instrumentos, name='lista_instrumentos'),
    path('confirmar_compra',confirmar_compra,name='confirmar_compra'),
    path ('agregar',agregar_al_carrito,name='CarroAdd')
]

