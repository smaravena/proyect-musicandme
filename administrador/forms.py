from django import forms
from django.forms import ModelForm
from app.models import Disco

class formDisco(ModelForm):
    class Meta:
        model = Disco
        fields=['id_disco',        
                'artista' ,        
                'nombre',            
                'precio',            
                'id_genero',         
                'imagen',           
                'descripcion',
                'spotify_iframe',   
        ]
        