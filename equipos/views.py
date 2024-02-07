from django.http import JsonResponse
from django.shortcuts import render
from .models import Equipo
# Create your views here.

def equipos(request):
    data=list(Equipo.objects.values())
    response=JsonResponse(data, status=200, safe=False)

    return response 
