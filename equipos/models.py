from django.db import models

# Create your models here.



class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100, default='N/A')
    modelo = models.CharField(max_length=100)
    codigo_inv= models.CharField(max_length=100)
    estado= models.CharField(max_length=100)
    cantidad= models.IntegerField(default=0)
    descripcion= models.TextField()
    