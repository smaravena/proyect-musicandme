from django import forms
from django.forms import ModelForm
from app.models import Disco,Instrumento,Tipo_instrumento,Genero

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
class formGenre(ModelForm):
    class Meta:
        model = Genero
        fields = ['id_genero',
                  'genero',]         
class formInstrumType(ModelForm):
    class Meta:
        model = Tipo_instrumento
        fields=['id_tipo',
                'tipo']