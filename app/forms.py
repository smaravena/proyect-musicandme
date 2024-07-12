from django import forms
from django.forms import ModelForm
from .models import Carrito

class CarritoForm (forms.ModelForm):
    class Meta:
        model = Carrito
        fields = [
            'nombre_comprador',
            'apellido_comprador',
            'email_comprador',
            'direccion',
            'tipo_domicilio',
            'comentario'
        ]