from django.urls import path
from .views import index,viewDisco,viewInstrum

urlpatterns = [
    path('index', index, name="index"),
    path('viewdisco', viewDisco, name="viewdisco"),
    path('viewinstrum', viewInstrum, name="viewinstrum"),
]