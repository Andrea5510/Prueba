from django.db import models

class Familia(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    cantidad_hijos = models.IntegerField()
    id = models.AutoField(primary_key=True)