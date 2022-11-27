from django.urls import path
from .views import *

urlpatterns = [
    path('registro/', registro, name="registro"),
    path('listar_usuarios/', listar_usuarios, name="listar_usuarios"),
    path('eliminar_usuario/<id>/', eliminar_usuario, name='eliminar_usuario'),
    path('modificar_usuario/<id>/', modificar_usuario, name='modificar_usuario'),
    path('', inicio, name="inicio"),

    path('nueva_disciplina/', nueva_disciplina, name="nueva_disciplina"),
    path('listar_cliente/', listar_cliente, name="listar_cliente"),
    path('eliminar_cliente/<id>/', eliminar_cliente, name='eliminar_cliente'),
    path('modificar_cliente/<id>/', modificar_cliente, name='modificar_cliente'),
    path('cliente_reporte/', cliente_reporte, name='cliente_reporte'),

    path('listar_contenedor/', listar_contenedor, name="listar_contenedor"),
    path('eliminar_contenedor/<id>/', eliminar_contenedor, name='eliminar_contenedor'),
    path('modificar_contenedor/<id>/', modificar_contenedor, name='modificar_contenedor'),
    path('nuevo_contenedor/', nuevo_contenedor, name='nuevo_contenedor'),

    path('listar_servicios/', listar_servicios, name="listar_servicios"),
    path('nuevo_servicio/', nuevo_servicio, name="nuevo_servicio"),
    path('modificar_servicio/<id>/', modificar_servicio, name='modificar_servicio'),
    path('eliminar_servicio/<id>/', eliminar_servicio, name='eliminar_servicio'),

    path('listar_ordenes/', listar_ordenes, name="listar_ordenes"),
    path('nueva_orden/', nueva_orden, name="nueva_orden"),
    path('modificar_orden/<id>/', modificar_orden, name='modificar_orden'),
    path('eliminar_orden/<id>/', eliminar_orden, name='eliminar_orden'),

    path('listar_deportes/', listar_deportes, name="listar_deportes"),
    path('nuevo_deporte/', nuevo_deporte, name="nuevo_deporte"),
    path('modificar_deportes/<id>/', modificar_deporte, name='modificar_deportes'),
    path('eliminar_deportes/<id>/', eliminar_deporte, name='eliminar_deporte'),

    path('listar_clases/', listar_clases, name="listar_clases"),
    path('nueva_clase/', nueva_clase, name="nueva_clase"),
    path('modificar_clase/<id>/', modificar_clase, name='modificar_clase'),
    path('eliminar_clase/<id>/', eliminar_clase, name='eliminar_clase'),

    path('listar_buques/', listar_buques, name="listar_buques"),
    path('modificar_buque/<id>/', modificar_buque, name='modificar_buque'),
    path('eliminar_buque/<id>/', eliminar_buque, name='eliminar_buque'),
    path('nuevo_buque/', nuevo_buque, name='nuevo_buque'),

    path('parte/', parte, name='parte')

]
