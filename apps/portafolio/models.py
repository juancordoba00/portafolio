from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length=30, null=False, blank=False)
    correo = models.EmailField()
    asunto = models.CharField(max_length=100, null=False, blank=False)
    mensaje = models.TextField()

    def __str__(self):
        return '{0}'.format(self.nombre)