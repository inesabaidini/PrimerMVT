# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from familia.models import Familia

def familia(request):
    lista_familia = Familia.objects.all()
    tabla = {'lista_familia': lista_familia}
    plantilla = loader.get_template('plantilla.html')
    documento = plantilla.render(tabla)
    return HttpResponse(documento)