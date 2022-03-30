from django.shortcuts import render
from django.http import HttpResponse
from app_mvt.models import Familia

def familia(request):

    familia = Familia.objects.all()

    return render(request,"app_mvt/familia.html")