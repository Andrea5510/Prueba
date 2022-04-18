from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Libros(models.Model):

    isbn = models.IntegerField(primary_key=True)
    idioma = models.CharField(max_length=40)
    titulo = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    clasificacion = models.CharField(max_length=40)

class Autores(models.Model):
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

class Editorial(models.Model):
    
    nombre = models.CharField(max_length=100)
    web = models.CharField(max_length=40)
    pais_origen = models.CharField(max_length=40)
    id = models.AutoField(primary_key=True)

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to = 'avatares', null = True, blank = True)