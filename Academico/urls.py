from django.urls import path
from . import views

app_name = 'Academico'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('paginaPrincipal/', views.paginaPrincipal, name='paginaPrincipal'),
    path('registro_Admin/', views.registro_Admin, name="registro_Admin"),
    path('logout/', views.logout_request, name="logout"),
    path('login/', views.login_request, name='login'),
    path('crear_PeriodoAcademico/', views.crear_PeriodoAcademico, name='crear_PeriodoAcademico'),
    path('lista_form/', views.lista_form, name='lista_form'),
    path('matriculasEstudiantes/', views.matriculasEstudiantes, name='matriculasEstudiantes'),
    path('eliminarPeriodosAcademicos/<int:id>/', views.eliminarPeriodosAcademicos, name= 'eliminarPeriodosAcademicos'),
    path('editarPeriodoAcademico/<int:id>/', views.editarPeriodoAcademico, name='editarPeriodoAcademico'),
    path('lista_matriculasEstudiantes/', views.lista_matriculasEstudiantes, name='lista_matriculasEstudiantes'),
    path('inscritosCurso/<int:id>/', views.inscritosCurso, name='inscritosCurso'),
    path('eliminar_matricula/<int:id>/', views.eliminar_matricula, name='eliminar_matricula'),
    path('editar_matricula/<int:id>/', views.editar_matricula, name='editar_matricula'),
    path('RegistroMaterias/', views.RegistroMaterias, name='RegistroMaterias'),
]