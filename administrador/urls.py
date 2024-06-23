from django.urls import path
from .views import homeadm,viewDisco,viewInstrum,discoAdd

urlpatterns = [
    path('homeadm', homeadm, name="homeadm"),
    path('viewdisco', viewDisco, name="viewdisco"),
    path('viewinstrum', viewInstrum, name="viewinstrum"),
    path('discoadd',discoAdd, name="discoadd"),
]