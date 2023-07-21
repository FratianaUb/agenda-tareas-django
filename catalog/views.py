
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.http import HttpResponse
from .forms import formularioTarea
from .models import tarea
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# mis vistas
def home(request):
    return render(request, 'home.html')


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })

    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                # Registrar
                user = User.objects.create_user(
                    username=request.POST["username"], password=request.POST["password1"])
                # Guarda el usuario en la base da datoss
                user.save()
                login(request, user)
                return redirect("tareas")
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'El nombre de usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'La contraseña no cooincide'
        })


def signout(request):
    logout(request)
    return redirect('home')

@login_required
def tareas(request):
    tareas = tarea.objects.filter(user=request.user, Fecha_completada__isnull=True) #devolver tareas de base de datos solo del usuario filtrado
    return render(request, 'Tareas.html', {"tareas": tareas})

@login_required
def tareas_listas(request):
    tareas1 = tarea.objects.filter(user=request.user, Fecha_completada__isnull=False) #devolver tareas de base de datos solo del usuario filtrado
    return render(request, 'Tareas.html', {"tareas": tareas1})

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        User = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if User is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o la contraseña no coinciden'
            })
        else:
            login(request, User)#guardar la sesion
            return redirect('tareas')
            #
            
@login_required            
def crear_tareas(request):
    
    if request.method == "GET":
        
        return render(request, 'Crear_tareas.html', {
         'form': formularioTarea   
        })
        
    else:
        try:
            form = formularioTarea(request.POST) 
            nueva_tarea = form.save(commit=False)
            nueva_tarea.user = request.user
            nueva_tarea.save()
            return redirect('tareas')  
        except ValueError:
            return render(request, 'Crear_tareas.html', {
                'form': formularioTarea,
                'error': "Los datos no son válidos"
            })

@login_required 
def info_tarea(request, tarea_id):
    print(tarea_id)
    if request.method == "GET":
        tarea1 = get_object_or_404(tarea, id=tarea_id, user=request.user)
        form = formularioTarea(instance=tarea1)
        return render(request, 'tarea_info.html', {"tarea": tarea1, 'form': form}) 
    else:
        try:
                 
            tarea1 = get_object_or_404(tarea, id=tarea_id, user=request.user)
            form = formularioTarea(request.POST, instance=tarea1)
            form.save()
            
            return redirect('tareas') 
        except ValueError: 
            return render(request, 'tarea_info.html', {"tarea": tarea1, 'form': form, 'error': 'Error actualizando la tarea'})

@login_required    
def tareas_completadas(request, tarea_id):
    print(tarea_id)
    tarea1 = get_object_or_404(tarea, id=tarea_id, user=request.user)
    if request.method == "POST":
        tarea1.Fecha_completada = timezone.now()
        tarea1.save()
    return redirect('tareas') 

@login_required  
def eliminar_tarea(request, tarea_id):
    print(tarea_id)
    tarea1 = get_object_or_404(tarea, id=tarea_id, user=request.user)
    if request.method == "POST":
        tarea1.delete()
    return redirect('tareas')   