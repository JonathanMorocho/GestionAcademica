from django.urls import path
from . import views

app_name = 'Academico'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('registro/', views.registro, name="registro"),
    path('logout/', views.logout_request, name="logout"),
    path('login/', views.login_request, name='login'),
    path('crear_PeriodoAcademico/', views.crear_PeriodoAcademico, name='crear_PeriodoAcademico'),
    path('lista_form/', views.lista_form, name='lista_form'),
]