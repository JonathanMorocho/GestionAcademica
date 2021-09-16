from django.db import models

# Create your models here.
class Carrera(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    Periodo_Academico = models.CharField(max_length=25)
    Fecha_inicio_Periodo = models.DateField()
    Duracion_Ciclo = models.CharField(max_length=25)
    
    def __str__(self):
        return self.Periodo_Academico

class Estudiante(models.Model):
    dni = models.CharField(max_length=10, primary_key=True)
    Nombres = models.CharField(max_length=25)
    Apellidos = models.CharField(max_length=25)
    Fecha_Nacimiento = models.DateField()
    Edad = models.IntegerField()
    # sexos = [
    #     ('H', 'Masculino'),
    #     ('F', 'Femenino')
    # ]
    sexoM = models.BooleanField("Masculino", default=False)
    sexoF = models.BooleanField("Femenino", default=False)
    # sexoM = models.CharField(max_length=1, choices=sexos, default='H')
    PeriodoAcademico = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)

    def nombreCompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.Nombres, self.Apellidos)
        
    def _str_(self):
        return '%s %s' % (self.dni, self.Nombres, self.Apellidos, self.Fecha_Nacimiento, self.Edad, self.sexo, self.PeriodoAcademico)