from django import forms
from .models import *

class RegistroForm(forms.ModelForm):
    class Meta:
        
        model = Carrera 
        fields = '__all__'
    
class MatriculasForm(forms.ModelForm):
    class Meta:
        
        model = Estudiante 
        fields = '__all__'