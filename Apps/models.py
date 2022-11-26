from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

from .listas import tipo_empresas, dimenciones, tipo_solicitud, tipo_servicios, tipo_incidencia


# Create your models here.

class Empresa(models.Model):
    nombre=models.CharField(max_length=50, unique=True)
    direccion=models.CharField(max_length=100)
    codigo_one=models.IntegerField(ForeignKey)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name='Empresa'
        verbose_name_plural='Deportes'
class Persona(models.Model):
    ci=models.BigIntegerField(ForeignKey)
    nombre=models.CharField(max_length=10)
    apellidos=models.CharField(max_length=20)
    cargo=models.CharField(max_length=25)
    telefono=models.BigIntegerField()
    correo=models.EmailField(max_length=25)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name='Persona'
        verbose_name_plural='Personas'
class Cliente(models.Model):
    numero_contrato=models.TextField(max_length=7)
    fechafirma=models.DateField()
    periodo=models.IntegerField()
    monto=models.DecimalField(max_digits=9, decimal_places=2)
    tipo_empresa=models.TextField(choices=tipo_empresas)
    empresa=models.OneToOneField(Empresa, on_delete=models.CASCADE)
    def __str__(self):
        return self.empresa.nombre
    def toJSON(self):
        item=model_to_dict(self)
        return item
    class Meta:
        verbose_name='Cliente'
        verbose_name_plural='Clientes'

class Comprador(models.Model):
    empresa=models.OneToOneField(Empresa, on_delete=models.CASCADE)
    def __str__(self):
        return self.empresa.nombre
    class Meta:
        verbose_name='Comprador'
        verbose_name_plural='Compradores'

class Vendedor(models.Model):
    empresa=models.OneToOneField(Empresa, on_delete=models.CASCADE)
    def __str__(self):
        return self.empresa.nombre
    class Meta:
        verbose_name='Vendedor'
        verbose_name_plural='Vendedores'

class Receptor(models.Model):
    empresa=models.OneToOneField(Empresa, on_delete=models.CASCADE)
    def __str__(self):
        return self.empresa.nombre
    class Meta:
        verbose_name='Receptor'
        verbose_name_plural='Receptores'

class Servicios(models.Model):
    nombre=models.CharField(max_length=60)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name='Servicio'
        verbose_name_plural='Servicios'


class Sello(models.Model):
    no_sello=models.CharField(max_length=15)
    material=models.CharField(max_length=15)

class Solicitud(models.Model):
    tipo_solicitud=models.TextField(choices=tipo_solicitud, null=True)
    medio=models.TextField(choices=tipo_servicios, default='Buques')
    contrato=models.CharField(verbose_name='Contrato', max_length=15)
    fecha_Solicitud=models.DateField(verbose_name='Fecha de la Solicitud')
    fecha_Inspeccion=models.DateField(verbose_name='Fecha de la Inspeccion')
    id_cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente')
    vendedor=models.CharField(max_length=60)
    comprador=models.CharField(max_length=60)
    receptor=models.CharField(max_length=60)
    servicio=models.ManyToManyField(Servicios, verbose_name='Servicios')
    def __str__(self):
        return self.id_cliente.empresa.nombre
    class Meta:
        verbose_name='Solicitud'
        verbose_name_plural='Solicitudes'
class Contenedor(models.Model):
    numero=models.CharField(max_length=10)
    dimenciones=models.TextField(choices=dimenciones)
    cantidad=models.BigIntegerField()
    peso=models.DecimalField(max_digits=9, decimal_places=2)
    embalaje=models.TextField(max_length=150)
    estiba=models.TextField(max_length=150)
    marca=models.TextField(max_length=150)
    mercancia=models.CharField(max_length=15)
    solicitud=models.ForeignKey(Solicitud, on_delete=CASCADE)

    def __str__(self):
        return self.numero
    class Meta:
        verbose_name='Contenedor'
        verbose_name_plural='Contenedores'

class Buque(models.Model):
    nombre=models.CharField(max_length=15)
    catidad=models.DecimalField(decimal_places=2, max_digits=11)
    producto=models.CharField(max_length=15)
    bl=models.CharField(max_length=20)
    manifiesto=models.CharField(max_length=15)
    solicitud=models.ForeignKey(Solicitud, on_delete=CASCADE)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name='Buque'
        verbose_name_plural='Buques'


class Orden(models.Model):
    solicitud=models.OneToOneField(Solicitud, on_delete=CASCADE)
    no_orden=models.CharField(ForeignKey, max_length=15)
    def __str__(self):
        return self.no_orden
    class Meta:
        verbose_name='Orden'
        verbose_name_plural='Ordenes'

class Incidencia(models.Model):
    tipo_incidencia=models.TextField(choices=tipo_incidencia)
    cantidad=models.IntegerField()
    descripcion=models.TextField()
    orden=models.ForeignKey(Orden, on_delete=CASCADE)

class Imagenes(models.Model):
    orden=models.ForeignKey(Orden, related_name='images', on_delete=CASCADE)
    image = models.ImageField(upload_to='operaciones')

    def __unicode__(self, ):
        return str(self.image)
class Deporte(models.Model):
    nombre = models.CharField(max_length=250, verbose_name="Nombre del deporte")
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Deporte'
        verbose_name_plural = 'Deportes'
        db_table = 'deportes'


class Disciplina(models.Model):
    deporte = models.OneToOneField(
        Deporte,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    nombre = models.CharField(max_length=250, verbose_name="Nombre de la disciplina")
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'disciplina'
        db_table = 'disciplinas'