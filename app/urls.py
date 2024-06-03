from django.urls import path
from .views import home, discos

urlpatterns = [
    path('index', home, name="home"),
    path('discos', discos, name="discos"),
]
