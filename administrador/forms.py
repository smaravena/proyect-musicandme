from django import forms
from django.forms import ModelForm
from app.models import Disco,Instrumento

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
class formInstrum(ModelForm):
    class Meta:
        model = Instrumento
        fields=[ 'id_instrumento',
                    'marca',            
                    'nombre',           
                    'precio',           
                    'id_tipo',          
                    'imagen',           
                    'descripcion',      
                    'yt_iframe',       
        ]        