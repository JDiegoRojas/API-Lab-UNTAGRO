from django.http import JsonResponse
from django.shortcuts import render
from .models import Reactivo

# Create your views here.
def reactivos(request):
    data=list(Reactivo.objects.values())
    response=JsonResponse(data, status=200, safe=False)
    return response
from django.http import HttpResponse

def materiales(request):
    return HttpResponse("This is the reactivos view.")