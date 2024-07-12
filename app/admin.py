from django.contrib import admin
from .models import Genero, Disco, Tipo_instrumento, Instrumento, Carrito, ElementoCarrito

# Register your models here.
admin.site.register(Genero)
admin.site.register(Disco)
admin.site.register(Tipo_instrumento)
admin.site.register(Instrumento)
admin.site.register(Carrito)
admin.site.register(ElementoCarrito)

# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# AÑADIR LOS REGISTROS DE ADMIN PARA QUE SALGAN EN DJANGO ADMIN SITE
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------