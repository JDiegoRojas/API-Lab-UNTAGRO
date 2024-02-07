from django.db import models

# Create your models here.

class Material(models.Model):
    nombre = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    cantidad = models.IntegerField(default=0)
    capacidad= models.IntegerField(default=0)
    unidades= models.CharField(max_length=200, default="ml")
    uso= models.TextField()
