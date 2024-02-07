from django.db import models

# Create your models here.



class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    codigo_inv= models.CharField(max_length=50)
    estado= models.CharField(max_length=50)
    cantidad= models.IntegerField(default=0)
    descripcion= models.TextField()
    