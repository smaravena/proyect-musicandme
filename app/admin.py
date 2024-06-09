from django.contrib import admin
from .models import Genero, Disco, Tipo_instrumento, Instrumento

# Register your models here.
admin.site.register(Genero)
admin.site.register(Disco)
admin.site.register(Tipo_instrumento)
admin.site.register(Instrumento)