from django.db import models
class Genero(models.Model):
    id_genero  = models.AutoField(db_column='idGenero', primary_key=True) 
    genero     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)

class Disco(models.Model):
    id_disco         = models.IntegerField(primary_key=True)
    artista          = models.CharField(max_length=20,null=False)
    nombre           = models.CharField(max_length=20,null=False)  
    precio           = models.IntegerField(null=False) 
    id_genero        = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')  
    imagen           = models.ImageField(upload_to="app", null=False)
    descripcion      = models.CharField(max_length=200,null=False)

    def __str__(self):
        return str(self.nombre)+"-"+str(self.artista)
class Tipo_instrumento(models.Model):
    id_tipo  = models.AutoField(db_column='id_tipo', primary_key=True) 
    tipo     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.tipo)
class Instrumento(models.Model):
    id_instrumento   = models.IntegerField(primary_key=True)
    marca            = models.CharField(max_length=20,null=False)
    nombre           = models.CharField(max_length=20,null=False)  
    precio           = models.IntegerField(null=False) 
    id_tipo          = models.ForeignKey('Tipo_instrumento',on_delete=models.CASCADE, db_column='id_tipo')  
    imagen           = models.ImageField(upload_to="app", null=False)
    descripcion      = models.CharField(max_length=200,null=False)
    def __str__(self):
        return str(self.nombre)+"-"+str(self.marca)
          
# Create your models here.
