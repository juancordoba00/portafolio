from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Contacto

# Create your views here.

def index(request):
    return render(request, 'portafolio/index.html')

def regitrarContacto(request):
    if request.method == 'POST':
        query = Contacto(
            nombre = request.POST['nombre'],
            correo = request.POST['correo'],
            asunto = request.POST['asunto'],
            mensaje = request.POST['mensaje']
        )
    query.save()
    return HttpResponseRedirect(reverse('portafolio:index', args=() ))