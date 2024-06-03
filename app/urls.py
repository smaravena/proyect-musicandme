from django.urls import path
from .views import home, discos, instrumentos, carro, login

urlpatterns = [
    path('index', home, name="home"),
    path('discos', discos, name="discos"),
    path('instrumentos', instrumentos, name="instrumentos"),
    path('carro', carro, name="carro"),
    path('login', login, name="login"),
]
