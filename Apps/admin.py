from django.contrib import admin
#from .models import Solicitud,Orden,Imagenes, Empresa, Cliente, Vendedor, Receptor, Comprador, Contenedor, Persona, Servicios, Buque
from .models import *
# Register your models here.
admin.site.register(ClaseDeportiva)
admin.site.register(Deporte)
admin.site.register(Disciplina)
admin.site.register(Atleta)

