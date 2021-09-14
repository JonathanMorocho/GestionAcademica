from django.contrib import admin
from Academico.models import *
# Register your models here.
admin.site.register(Carrera)
admin.site.register(Estudiante)

# class AcademicoAdmin(admin.ModelAdmin):

#     fieldsets = [
#         ("codigo/Periodo_Academico/Fecha_inicio_Periodo", {"fields": ["codigo", "Periodo_Academcio","Fecha_inicio_Periodo"]}),
#         ("Duracion_Ciclo", {"fields": ["Duracion_Ciclo"]})
#     ]



# admin.site.register(Academico, AcademicoAdmin)