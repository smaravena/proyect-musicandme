from django.urls import path
from .views import home, discos, instrumentos, carro, login,lista_discos

urlpatterns = [
    path('index', home, name="home"),
    path('discos', discos, name="discos"),
    path('instrumentos', instrumentos, name="instrumentos"),
    path('carro', carro, name="carro"),
    path('login', login, name="login"),
    path('lista_discos',lista_discos, name='lista_discos'),
]

