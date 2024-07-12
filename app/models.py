from django.db import models
from django.utils import timezone

# Create your models here.
class Genero(models.Model):
    id_genero  = models.AutoField(db_column='idGenero', primary_key=True) 
    genero     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)

class Disco(models.Model):
    id_disco         = models.AutoField(primary_key=True)
    artista          = models.CharField(max_length=20,null=False)
    nombre           = models.CharField(max_length=20,null=False)  
    precio           = models.IntegerField(null=False) 
    stock            = models.PositiveIntegerField(null=False)
    id_genero        = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')  
    imagen           = models.ImageField(upload_to="disco", null=True)
    descripcion      = models.TextField(null=False)
    spotify_iframe   = models.TextField(null=True, blank=True) 
    def __str__(self):
        return str(self.nombre)+"-"+str(self.artista)
    
class Tipo_instrumento(models.Model):
    id_tipo  = models.AutoField(db_column='id_tipo', primary_key=True) 
    tipo     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.tipo)
    
class Instrumento(models.Model):
    id_instrumento   = models.AutoField(primary_key=True)
    marca            = models.CharField(max_length=20,null=False)
    nombre           = models.CharField(max_length=20,null=False)  
    precio           = models.IntegerField(null=False) 
    stock            = models.PositiveIntegerField(null=False)
    id_tipo          = models.ForeignKey('Tipo_instrumento',on_delete=models.CASCADE, db_column='id_tipo')  
    imagen           = models.ImageField(upload_to="instrumento", null=True)
    descripcion      = models.TextField(null=False)
    yt_iframe        = models.TextField(null=True, blank=True) 
    def __str__(self):
        return str(self.nombre)+"-"+str(self.marca)

class Carrito(models.Model):
    session_key = models.CharField(max_length=40, unique=True)
    nombre_comprador = models.CharField(max_length=100, blank=True, null=True)
    apellido_comprador = models.CharField(max_length=100, blank=True, null=True)
    email_comprador = models.EmailField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    tipo_domicilio = models.CharField(max_length=50, blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Carrito de {self.nombre_comprador or 'Desconocido'} ({self.session_key})"

class ElementoCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='elementos')
    disco = models.ForeignKey(Disco, on_delete=models.CASCADE, null=True, blank=True)
    instrumento = models.ForeignKey(Instrumento, on_delete=models.CASCADE, null=True, blank=True)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.disco or self.instrumento} x {self.cantidad}"
