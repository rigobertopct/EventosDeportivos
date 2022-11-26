from django.contrib import admin
from .models import Solicitud,Orden,Imagenes, Empresa, Cliente, Vendedor, Receptor, Comprador, Contenedor, Persona, Servicios, Buque
# Register your models here.
admin.site.register(Solicitud)
admin.site.register(Empresa)
admin.site.register(Cliente)
admin.site.register(Vendedor)
admin.site.register(Receptor)
admin.site.register(Comprador)
admin.site.register(Contenedor)
admin.site.register(Persona)
admin.site.register(Servicios)
admin.site.register(Buque)
admin.site.register(Orden)
admin.site.register(Imagenes)

