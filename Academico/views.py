from django.shortcuts import render
from Academico.forms import RegistroForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import Carrera, Estudiante
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib import messages

# Create your views here.
#Pagina Inicial
def homepage(request):
    return render(request, "plantillas/inicio.html")

def paginaPrincipal(request):
    return render(request, "plantillas/paginaPrincipal.html")

#Registrar un Adminsitrativo
def registro(request):

    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            nombre_usuario = form.cleaned_data.get('username')
            messages.success(request, f"Nueva Cuenta Creada : {nombre_usuario}")
            login(request, usuario)
            messages.info(request, f"Has sido logeado")
            return redirect("Academico:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = UserCreationForm 
    return render(request, "plantillas/registro_user.html", {"form":form})

#Ingresar
def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username = usuario, password = contraseña)

            if user is not None:
                login(request, user)
                messages.info(request, f"Estas logeado como {usuario}")
                return redirect("Academico:paginaPrincipal")
            else:
                messages.info(request, f"Usuario o contraseña incorrecta")
        else:
            messages.info(request, f"Usuario o contraseña incorrecta")

    form = AuthenticationForm()
    return render(request, "plantillas/login.html", {"form": form})

#Cerrar Seccion
def logout_request(request):
    logout(request)
    return redirect("Academico:paginaPrincipal")

#Nuevo Periodo Academico
def crear_PeriodoAcademico(request):
    form = RegistroForm() 
    if request.method == 'POST':
        form = RegistroForm (request.POST)
        if form.is_valid():
            form.save()
            return redirect('Academico:lista_form')
        else: 
            context = {
                'forms': form
            }
            return redirect(request, "plantillas/registro_periodo.html", context)
    context = {
        'forms': form
    }
    return render(request, "plantillas/registro_periodo.html", context)

#Lista de Periodos Academcios
def lista_form(request):    
    academico = Carrera.objects.all()
    context = {
        'Academico': academico
    }
    print(academico)
    return render(request, "plantillas/listas.html", context)

#Eliminar Periodo
# def eliminarCurso(request,id):
#     academico = Carrera.objects.get(codigo = id)
#     academico.delete()
#     return redirect('Academico:lista_form')
