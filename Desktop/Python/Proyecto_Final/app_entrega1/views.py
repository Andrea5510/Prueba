from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse

from app_entrega1.models import Autores, Editorial, Libros
from app_entrega1.forms import RegistroUsuarios, EditarUsuarios

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    return render(request, 'app_entrega1/posts.html')

def about_me(request):
    return render(request, 'app_entrega1/about.html')

# Modulo de Login
def iniciar_sesion(request):

    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username = usuario, password = contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "app_entrega1/", {"mensaje":f"Bienvenido {usuario}"})

            else:

                return render(request, "app_entrega1/", {"mensaje":"Error: Los datos ingresados son incorrectos"})
        
        else:
            
            return render(request, "app_entrega1/", {"mensaje":"Error: formulario erroneo"})

    else:

        form = AuthenticationForm()

        return render(request, "app_entrega1/login.html", {"form":form})


def registro(request):

    if request.method == "POST":

        form = RegistroUsuarios(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()

            return render(request, "app_entrega1/posts.html", {"mensaje":"El usuario ha sido creado exitosamente"})
        
    else:

        form = RegistroUsuarios()

    return render(request, "app_entrega1/signup.html", {"form":form})

def editar_usuario(request):

    usuario = request.user

    if request.method == "POST":
        
        miFormulario = EditarUsuarios(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            usuario.save()

            return render(request, "app_entrega1/inicio.html")
    
    else: 

        miFormulario = EditarUsuarios(initial={'email': usuario.email})

    return render(request, "app_entrega1/editarperfil.html", {"miFormulario":miFormulario, "usuario": usuario})













def autores(request):

    lista_autores = Autores.objects.all()
    print(lista_autores)

    return render(request,"app_entrega1/autores.html",{"autores":lista_autores}) 

def formulario_autores(request):
    
    if request.method == 'POST':

        miFormulario = AutorFormulario(request.POST)

        print (miFormulario)

        if miFormulario.is_valid:

            data = miFormulario.cleaned_data

            autor = Autores(data['nombre'],data['apellido'])
    
            autor.save()

        return render(request,"app_entrega1/autoresFormulario.html") 

    else:

        miFormulario = AutorFormulario()

    return render(request,"app_entrega1/autoresFormulario.html",{"miFormulario":miFormulario})    


#busqueda 
def buscar_libros2(request):
    return render(request, 'app_entrega1/buscarlibros.html')

def buscar(request):
    lib_bus=request.GET.get('libro')
    if lib_bus:
        libros= Libros.objects.filter(titulo__icontains= lib_bus)
        print("lib_bus: ", lib_bus)
        print("Libros: ", libros)
        print("type: ", type(libros))
        return render(request, 'app_entrega1/buscarlibros.html', {"libros": libros, "nombre": lib_bus})
    else: 
        respuesta="No enviaste datos"
    return render(request, 'app_entrega1/buscarlibros.html', {"respuesta": respuesta})          

def buscar_libros3(request):

    data = request.GET.get('libro', "")
    error = ""

    if data:
        try:
            libro = Libros.objects.get(titulo=data)
            return render(request, 'app_entrega1/buscarlibros.html', {"libros": libro, "nombre": data})

        except Exception as exc:
            print(exc)
            error = "No existe Libro"
    return render(request, 'app_entrega1/buscarlibros.html', {"error": error})          

def buscar_libros(request):

    data = request.GET.get('libro', "")
    error = ""

    if data:
       # try:
            libros = Libros.objects.filter(titulo__icontains= data)
            print(libros)
            if libros:
                return render(request, 'app_entrega1/buscarlibros.html', {"libros": libros, "nombre": data})
            else: 
                error = "No existe Libro"
    else: 
            error = "No ingreso ningun Libro"        
    return render(request, 'app_entrega1/buscarlibros.html', {"error": error}) 


class LibrosList(ListView):

    model = Libros
    template_name = "app_entrega1/libros_lista.html"

class LibrosDetail(DetailView):

    model = Libros
    template_name = "app_entrega1/libros_detalle.html"

class LibrosCreate(CreateView):

    model = Libros
    success_url = "/app_entrega1/libros/lista"
    fields = ['isbn','idioma','titulo','fecha_publicacion','clasificacion']

class LibrosUpdate(UpdateView):

    model = Libros
    success_url = "/app_entrega1/libros/lista"
    fields = ['idioma','titulo','fecha_publicacion','clasificacion']

class LibrosDelete(DeleteView):

    model = Libros
    success_url = "/app_entrega1/libros/lista/"


