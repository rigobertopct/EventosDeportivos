from django.urls import path
from .views import *

urlpatterns = [
    path('registro/', registro, name="registro"),
    path('listar_usuarios/', listar_usuarios, name="listar_usuarios"),
    path('eliminar_usuario/<id>/', eliminar_usuario, name='eliminar_usuario'),
    path('modificar_usuario/<id>/', modificar_usuario, name='modificar_usuario'),
    path('', inicio, name="inicio"),

    path('nueva_disciplina/', nueva_disciplina, name="nueva_disciplina"),
    path('listar_disciplinas/', listar_disciplinas, name="listar_disciplinas"),
    path('eliminar_disciplina/<id>/', eliminar_disciplina, name='eliminar_disciplina'),
    path('modificar_disciplina/<id>/', modificar_disciplina, name='modificar_disciplina'),

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

    path('listar_atletas/', listar_atletas, name="listar_atletas"),
    path('modificar_atleta/<id>/', modificar_atleta, name='modificar_atleta'),
    path('eliminar_atleta/<id>/', eliminar_atleta, name='eliminar_atleta'),
    path('nuevo_atleta/', nuevo_atleta, name='nuevo_atleta'),

    path('parte/', parte, name='parte')

]
