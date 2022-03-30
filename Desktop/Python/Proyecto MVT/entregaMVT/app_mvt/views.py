from django.shortcuts import render
from django.http import HttpResponse
from app_mvt.models import Familia

def listas_familia(request):

    lista_familia = Familia.objects.all()
    print(lista_familia)

    return render(request,"app_mvt/base.html",{"familia":lista_familia}) 