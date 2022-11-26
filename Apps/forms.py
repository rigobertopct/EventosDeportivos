from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from django.forms import widgets
from django.forms.widgets import DateInput, Select, TextInput
from .models import *

class CuastomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password1","password2"]

class ClienteForm(forms.ModelForm):      
    numero_contrato=forms.CharField(widget=TextInput(attrs={"class":"form-control"}))
    class Meta:
        model=Cliente
        fields='__all__'
class EmpresaForm(forms.ModelForm):
    class Meta:
        model=Empresa
        fields='__all__'

class SolicitudForm(forms.ModelForm):
    class Meta:
        model=Solicitud
        fields='__all__'

class ContenedorForm(forms.ModelForm):
    class Meta:
        model=Contenedor
        fields='__all__'

class BuqueForm(forms.ModelForm):
    class Meta:
        model=Buque
        fields='__all__'

class ServicioForm(forms.ModelForm):
    class Meta:
        model=Servicios
        fields='__all__'

class OrdenForm(forms.ModelForm):
    class Meta:
        model=Orden
        fields='__all__'
class CompradorForm(forms.ModelForm):
    class Meta:
        model=Comprador
        fields='__all__'
class VendedorForm(forms.ModelForm):
    class Meta:
        model=Vendedor
        fields='__all__'
class ReceptorForm(forms.ModelForm):
    class Meta:
        model=Receptor
        fields='__all__'
class PersonaForm(forms.ModelForm):
    class Meta:
        model=Persona
        fields='__all__'
class ImagenesForm(forms.ModelForm):
    class Meta:
        model=Imagenes
        fields='__all__'
class PersonaForm(forms.ModelForm):
    class Meta:
        model=Persona
        fields='__all__'
class DeporteForm(forms.ModelForm):
    class Meta:
        model=Deporte
        fields='__all__'

class AtletaForm(forms.ModelForm):
    class Meta:
        model = Deporte
        fields = '__all__'

class ClaseDForm(forms.ModelForm):
    class Meta:
        model = ClaseDeportiva
        fields = '__all__'