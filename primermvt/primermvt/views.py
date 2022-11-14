from django.http import HttpResponse
from django.template import Template, Context, loader
from familiares.models import Familia

def familia(request):

    plantilla = loader.get_template('familia.html')
    documento = plantilla.render()
    return HttpResponse(documento)