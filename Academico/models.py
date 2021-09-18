from django.db import models

# Create your models here.
class Carrera(models.Model):
    Periodo_Academico = models.CharField(max_length=25)
    Fecha_inicio_Periodo = models.DateField()
    Duracion_Ciclo = models.CharField(max_length=25)
    
    
    def __str__(self):
        return self.Periodo_Academico



class Estudiante(models.Model):
    sexos = (('Masculino', 'Masculino'),('Femenino', 'Femenino'))
    dni = models.CharField(max_length=10)
    Nombres = models.CharField(max_length=25)
    Apellidos = models.CharField(max_length=25)
    Fecha_Nacimiento = models.DateField()
    Edad = models.IntegerField()
    sexoM = models.CharField(max_length=10, choices=sexos)
    PeriodoAcademico = models.ForeignKey(Carrera, on_delete=models.CASCADE)

        
    def _str_(self):
        return '%s %s' % (self.dni, self.Nombres, self.Apellidos, self.Fecha_Nacimiento, self.Edad, self.sexoM, self.PeriodoAcademico)