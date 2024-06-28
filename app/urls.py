from django.urls import path
from .views import inicio, discos, instrumentos, carro, login,lista_discos,lista_instrumentos

urlpatterns = [
    path('inicio', inicio, name="inicio"),
    path('discos', discos, name="discos"),
    path('instrumentos', instrumentos, name="instrumentos"),
    path('carro', carro, name="carro"),
    path('login', login, name="login"),
    path('lista_discos',lista_discos, name='lista_discos'),
    path('lista_instrumentos',lista_instrumentos, name='lista_instrumentos'),
]

