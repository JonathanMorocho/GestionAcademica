from django.urls import path
from . import views

app_name = 'Academico'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('paginaPrincipal/', views.paginaPrincipal, name='paginaPrincipal'),
    path('registro/', views.registro, name="registro"),
    path('logout/', views.logout_request, name="logout"),
    path('login/', views.login_request, name='login'),
    path('crear_PeriodoAcademico/', views.crear_PeriodoAcademico, name='crear_PeriodoAcademico'),
    path('lista_form/', views.lista_form, name='lista_form'),
    # path('eliminarCurso/<int:id>/', views.eliminarCurso, name= 'eliminarCurso'),
    path('matriculasEstudiantes/', views.matriculasEstudiantes, name='matriculasEstudiantes'),
    path('eliminarCurso/<int:id>/', views.eliminarCurso, name= 'eliminarCurso'),
    path('lista_matriculasEstudiantes/', views.lista_matriculasEstudiantes, name='lista_matriculasEstudiantes'),
]