from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from app_entrega1.models import Autores
from app_entrega1.forms import AutorFormulario

# Create your views here.

def autor(request):

      if request.method == 'POST':

            miFormulario = AutorFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  autor = Autores (nombre=informacion['nombre'], apellido=informacion['apellido']) 

                  autor.save()

                  return render(request, "app_entrega1/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= AutorFormulario() #Formulario vacio para construir el html

      return render(request, "app_entrega1/autores.html", {"miFormulario":miFormulario})