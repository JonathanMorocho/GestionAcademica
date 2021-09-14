from django import forms
from .models import *

class RegistroForm(forms.ModelForm):
    class Meta:
        
        model = Carrera 
        fields = '__all__'