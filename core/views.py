from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import *
# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Las contraseñas no coinciden'
        })

def lista(request):
    lista = Empleado.objects.all()
    return render(request, 'lista_usuarios.html', {'lista': lista})

def miPerfil(request):
    miPerfil = Empleado.objects.last()
    return render(request, 'miPerfil.html', {'miPerfil':miPerfil })

def eliminarUser(request):
    eliminarUser = Empleado.objects.last()
    return render(request, 'eliminarUser.html', {'eliminarUser':eliminarUser })

def verUsuario(request):
    return render(request, 'usuarios.html')

def variables(request):
    return render(request, 'variables.html')

def editUsuario(request):
    return render(request, 'editUsuario.html')

def addUser(request):
    return render(request,"addUser.html")

def signout(request):
    logout(request)
    return redirect('signin')



def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('home')

def vacaciones(request):
    return render(request, 'vacaciones.html')