from django.http import JsonResponse
from django.shortcuts import render
from .models import Material

# Create your views here.

def materiales(request):
    data=list(Material.objects.values())
    response=JsonResponse(data, status=200, safe=False)
    return response