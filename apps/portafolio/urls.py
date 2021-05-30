from django.urls import path
from . import views

app_name = 'portafolio'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('registrarContacto', views.regitrarContacto, name = 'registrarContacto'),
]