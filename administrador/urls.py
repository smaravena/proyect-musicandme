from django.urls import path
from .views import homeadm

urlpatterns = [
    path('homeadm', homeadm, name="homeadm"),
]