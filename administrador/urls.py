from django.urls import path
from .views import homeadm,viewDisco,viewInstrum

urlpatterns = [
    path('homeadm', homeadm, name="homeadm"),
    path('viewdisco', viewDisco, name="viewdisco"),
    path('viewinstrum', viewInstrum, name="viewinstrum"),
]