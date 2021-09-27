from django.shortcuts import render
from Academico.forms import RegistroForm, MatriculasForm, InscripcionForm, InscripcionEditarForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import Carrera, Estudiante
from sys import prefix
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib import messages

# Create your views here.
#Pagina de Inico ISTL
def homepage(request):
    return render(request, "plantillas/inicio.html")

#Pagina Principal Logeado
def paginaPrincipal(request):
    return render(request, "plantillas/paginaPrincipal.html", {"Academico": Carrera.objects.all})

#Registrar un Adminsitrativo
def registro_Admin(request):

    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            nombre_usuario = form.cleaned_data.get('username')
            messages.success(request, f"Nueva Cuenta Creada : {nombre_usuario}")
            login(request, usuario)
            messages.info(request, f"Has sido logeado")
            return redirect("Academico:paginaPrincipal")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = UserCreationForm 
    return render(request, "plantillas/registro_user.html", {"form":form})

#Ingresar Login
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
    return redirect("Academico:homepage")

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

# Matriculas De Estudiantes
def matriculasEstudiantes(request):
    form = InscripcionForm() 
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Academico:paginaPrincipal')
        else: 
            context = {
                'forms': form
            }
            return redirect(request, "plantillas/registroEstudiantes.html", context)
    context = {
        'forms': form
    }
    return render(request, "plantillas/registroEstudiantes.html", context)

#Eliminar Periodos Academicos
def eliminarPeriodosAcademicos(request,id):
    curso = Carrera.objects.get(id = id)
    curso.delete()
    return redirect('Academico:lista_form')

#Editar Periodos Academicos
def editarPeriodoAcademico(request,id):
    curso = Carrera.objects.get(id = id)
    print(curso)
    form = RegistroForm(instance = curso)
    if request.method == 'POST':
        form = RegistroForm(request.POST, instance= curso)
        if form.is_valid():
            form.save()
            messages.info(request, f"Curso editado correctamente")
            return redirect('Academico:lista_form')
    contexto = {
            'form': form
        }
    return render(request, "plantillas/Editar_registro_periodo.html", contexto)

#Lista de Periodos Academcios
def lista_matriculasEstudiantes(request):    
    academico = Estudiante.objects.all()
    context = {
        'Academico': academico
    }
    print(academico)
    return render(request, "plantillas/lista_matriculasEstudiantes.html", context)


#LA DE LAS CARDS
def inscritosCurso(request, id):
    academico = Carrera.objects.get(id=id)
    EstudiantesIns = Estudiante.objects.filter(PeriodoAcademico = academico)
    contexto = {
        'Periodo': academico,
        'Academico': EstudiantesIns, 
    }
    print(academico, EstudiantesIns)
    return render(request, 'plantillas/lista_matriculasEstudiantes.html', contexto)

#eliminar estudiantes
def eliminar_matricula(request,id):
    inscripcion = Estudiante.objects.get(id = id)
    inscripcion.delete()
    return redirect('Academico:lista_matriculasEstudiantes')

#Editar_matricula
def editar_matricula(request,id):
    curso = Estudiante.objects.get(id = id)
    print(curso)
    form = InscripcionEditarForm(instance = curso)
    if request.method == 'POST':
        form = InscripcionEditarForm(request.POST, instance= curso)
        if form.is_valid():
            form.save()
            messages.info(request, f"Estudiante editado correctamente")
            return redirect('Academico:lista_matriculasEstudiantes')
    contexto = {
            'form': form
        }
    return render(request, "plantillas/Editar_matricula_estudiante.html", contexto)