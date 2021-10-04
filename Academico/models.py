from django.db import models
# from django import forms
from multiselectfield import MultiSelectField

# Create your models here.
class Carrera(models.Model):
    Periodo_Academico = models.CharField(max_length=25)
    Fecha_inicio_Periodo = models.DateField()
    Duracion_Ciclo = models.CharField(max_length=25)
    
    def __str__(self):
        return self.Periodo_Academico



class Estudiante(models.Model):
    sexos = (('Masculino', 'Masculino'),('Femenino', 'Femenino'))
    periodos = (('P.Ciclo','Primer Ciclo'),('S.Ciclo','SegundO Ciclo'),('T.Ciclo','Tercer Ciclo'))
    materiasPrimer = (('P.1','Legislacion'),('P.1','Matematicas'),('T.Ciclo','Tercer Ciclo'))
    materiasSegun = (('P.1','Legislacion'),('P.1','Matematicas'),('T.Ciclo','Tercer Ciclo'))
    MateriasPrimerCiclo = (
    ('Matemáticas Discretas','Matemáticas Discretas'),
    ('Introducción al Desarrollo de Software','Introducción al Desarrollo de Software'),
    ('Fundamentos de la Programación','Fundamentos de la Programación'),
    ('Análisis y Diseño de Sistemas','Análisis y Diseño de Sistemas'),
    ('Ingles I','Ingles I'),
    ('Desarrollo del Pensamiento','Desarrollo del Pensamiento')
    )
    MateriasSegundoCiclo = (
    ('Algebra y Trigonometría','Algebra y Trigonometría'),
    ('Base de Datos','Base de Datos'),
    ('Programación Orientada a Objetos','Programación Orientada a Objetos'),
    ('Metodologías de Desarrollo de Software','Metodologías de Desarrollo de Software'),
    ('Ingles II','Ingles II'),
    ('Lenguaje y Comunicación','Lenguaje y Comunicación')
    )
    MateriasTercerCiclo = (
    ('Cálculo Diferencial e Integral','Algebra y Trigonometría'),
    ('Fundamentos de la Administración','Base de Datos'),
    ('Programación Visual','Programación Orientada a Objetos'),
    ('Base de Datos Avanzada','Base de Datos Avanzada'),
    ('Diseño de Interfaz','Diseño de Interfaz'),
    ('Ingles III','Ingles III'),
    )
    MateriasCuartoCiclo = (
    ('Estadística Descriptiva','Estadística Descriptiva'),
    ('Legislación Informática','Legislación Informática'),
    ('Programación de Aplicaciones Web','Programación de Aplicaciones Web'),
    ('Desarrollo de Aplicaciones Moviles','Desarrollo de Aplicaciones Moviles'),
    ('Ingles IV','Ingles IV'),
    ('Diversidad Cultural','Diversidad Cultural'),
    )
    MateriasQuintoCiclo = (
    ('Proyecto de Titulación','Proyecto de Titulación'),
    ('Emprendimientos','Emprendimientos'),
    ('Auditoria Informática','Auditoria Informática'),
    ('Tendencias Actuales de Programación','Tendencias Actuales de Programación'),
    ('Calidad de Software','Calidad de Software'),
    ('Fundamentos de Software y Conectividad','Fundamentos de Software y Conectividad'),
    ('Ética Profesional','Ética Profesional'),
    )
    dni = models.CharField(max_length=10)
    Nombres = models.CharField(max_length=25)
    Apellidos = models.CharField(max_length=25)
    Fecha_Nacimiento = models.DateField()
    Edad = models.IntegerField()
    sexoM = models.CharField(max_length=10, choices=sexos)
    PeriodoAcademico = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    PrimerCiclo = MultiSelectField(max_length=1000, max_choices=7, choices=MateriasPrimerCiclo, default=False)
    SegundoCiclo = MultiSelectField(max_length=1000, max_choices=7, choices=MateriasSegundoCiclo, default=False)
    TercerCiclo = MultiSelectField(max_length=1000, max_choices=7, choices=MateriasTercerCiclo, default=False)
    CuartoCiclo = MultiSelectField(max_length=1000, max_choices=7, choices=MateriasCuartoCiclo, default=False)
    QuintoCiclo = MultiSelectField(max_length=1000, max_choices=7, choices=MateriasQuintoCiclo, default=False)
    # CicloEstudii = models.CharField(max_length=1000, choices=periodos)
    # MateriasPrimerC = models.BooleanField(choices=materiasPrimer, default=False)
    # MateriasSegunC = models.BooleanField(choices=materiasSegun,default=False)

        
    def _str_(self):
        return '%s %s' (self.dni, self.Nombres, self.Apellidos, self.Fecha_Nacimiento, self.Edad, self.sexoM, self.PeriodoAcademico, self.PrimerCiclo, self.SegundoCiclo, self.TercerCiclo, self.CuartoCiclo, self.QuintoCiclo)    

# class Materias(models.Model):
    MateriasPrimerCiclo = (
    ('Matemáticas Discretas','Matemáticas Discretas'),
    ('Introducción al Desarrollo de Software','Introducción al Desarrollo de Software'),
    ('Fundamentos de la Programación','Fundamentos de la Programación'),
    ('Análisis y Diseño de Sistemas','Análisis y Diseño de Sistemas'),
    ('Ingles I','Ingles I'),
    ('Desarrollo del Pensamiento','Desarrollo del Pensamiento')
    )
    MateriasSegundoCiclo = (
    ('Algebra y Trigonometría','Algebra y Trigonometría'),
    ('Base de Datos','Base de Datos'),
    ('Programación Orientada a Objetos','Programación Orientada a Objetos'),
    ('Metodologías de Desarrollo de Software','Metodologías de Desarrollo de Software'),
    ('Ingles II','Ingles II'),
    ('Lenguaje y Comunicación','Lenguaje y Comunicación')
    )
    MateriasTercerCiclo = (
    ('Cálculo Diferencial e Integral','Algebra y Trigonometría'),
    ('Fundamentos de la Administración','Base de Datos'),
    ('Programación Visual','Programación Orientada a Objetos'),
    ('Base de Datos Avanzada','Base de Datos Avanzada'),
    ('Diseño de Interfaz','Diseño de Interfaz'),
    ('Ingles III','Ingles III'),
    )
    MateriasCuartoCiclo = (
    ('Estadística Descriptiva','Estadística Descriptiva'),
    ('Legislación Informática','Legislación Informática'),
    ('Programación de Aplicaciones Web','Programación de Aplicaciones Web'),
    ('Desarrollo de Aplicaciones Moviles','Desarrollo de Aplicaciones Moviles'),
    ('Ingles IV','Ingles IV'),
    ('Diversidad Cultural','Diversidad Cultural'),
    )
    MateriasQuintoCiclo = (
    ('Proyecto de Titulación','Proyecto de Titulación'),
    ('Emprendimientos','Emprendimientos'),
    ('Auditoria Informática','Auditoria Informática'),
    ('Tendencias Actuales de Programación','Tendencias Actuales de Programación'),
    ('Calidad de Software','Calidad de Software'),
    ('Fundamentos de Software y Conectividad','Fundamentos de Software y Conectividad'),
    ('Ética Profesional','Ética Profesional'),
    )
    PrimerCiclo = MultiSelectField(max_length=1000, choices=MateriasPrimerCiclo, default=False)
    SegundoCiclo = MultiSelectField(max_length=1000, choices=MateriasSegundoCiclo, default=False)
    TercerCiclo = MultiSelectField(max_length=1000, choices=MateriasTercerCiclo, default=False)
    CuartoCiclo = MultiSelectField(max_length=1000, choices=MateriasCuartoCiclo, default=False)
    QuintoCiclo = MultiSelectField(max_length=1000, choices=MateriasQuintoCiclo, default=False)

    def __str__(self):
        return self.PrimerCiclo, self.SegundoCiclo, self.TercerCiclo, self.CuartoCiclo, self.QuintoCiclo
    

    