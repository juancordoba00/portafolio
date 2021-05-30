from django.contrib import admin

# Register your models here.
from .models import Contacto

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'asunto', 'mensaje', )

admin.site.register(Contacto,ContactoAdmin)