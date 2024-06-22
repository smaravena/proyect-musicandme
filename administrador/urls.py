from django.urls import path
from .views import homeadm,viewDisco

urlpatterns = [
    path('homeadm', homeadm, name="homeadm"),
    path('viewdisco', viewDisco, name="viewdisco"),
]