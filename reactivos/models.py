from django.db import models

# Create your models here.

class Reactivo(models.Model):
    nombre = models.CharField(max_length=200)
    concentracion = models.CharField(max_length=200)
    fecha_prod = models.CharField(max_length=200)
    volumen = models.IntegerField(default=0)
    unidades= models.CharField(max_length=200, default="ml")
    uso= models.TextField()
