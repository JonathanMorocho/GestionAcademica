from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(forms.ModelForm):
    class Meta:
        
        model = Carrera 
        fields = '__all__'
    
class MatriculasForm(forms.ModelForm):
    class Meta:
        
        model = Estudiante 
        fields = '__all__'

# class MateriasForm(forms.ModelForm):
#     class Meta:
        
#         model = Materias
#         fields = '__all__'


class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Estudiante
    
        fields = [
                    'dni',
                    'Nombres',
                    'Apellidos',
                    'Fecha_Nacimiento',
                    'Edad',
                    'sexoM',
                    'PeriodoAcademico',
                ]
        labels  = {
            'dni' : 'Cédula',
            'sexoM' : 'Genero',
            'PeriodoAcademico' : 'Periodo Academico',
        }
        
class InscripcionEditarForm(forms.ModelForm):
    class Meta:
        model = Estudiante
    
        fields = [
                    'dni',
                    'Nombres',
                    'Apellidos',
                    # 'Fecha_Nacimiento',
                    'Edad',
                    'sexoM',
                    'PeriodoAcademico',
                ]
        labels  = {
            'dni' : 'Cédula',
            'sexoM' : 'Genero',
            'PeriodoAcademico' : 'Periodo Academico',
        }