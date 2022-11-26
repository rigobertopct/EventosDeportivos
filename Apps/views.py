from _datetime import date
# 2.Implemente leer y escribir bytes en la memoria
from _datetime import date
# 2.Implemente leer y escribir bytes en la memoria
from io import BytesIO

# # 1. Exportar biblioteca de Excel
import xlwt
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *


# Create your views here.
@login_required
def inicio(request):
    solicitudes = Solicitud.objects.all()
    clientes = Cliente.objects.all()
    ordenes = Orden.objects.all()
    mixtas = 0
    tcp = 0
    cna = 0
    extranjeras = 0
    estatales = 0
    contenedores = []
    buques = []
    contbuques1 = 0
    contbuques2 = 0
    contbuques3 = 0
    contbuques4 = 0
    contcont1 = 0
    contcont2 = 0
    contcont3 = 0
    contcont4 = 0
    clientes_vencidos = []
    for s in solicitudes:
        if (s.medio == 'buque'):
            if (date(2021, 1, 1) < s.fecha_Inspeccion < date(2021, 3, 31)):
                contbuques1 = contbuques1 + 1
            elif (date(2021, 4, 1) < s.fecha_Inspeccion < date(2021, 6, 30)):
                contbuques2 = contbuques2 + 1
            elif (date(2021, 7, 1) < s.fecha_Inspeccion < date(2021, 9, 30)):
                contbuques3 = contbuques3 + 1
            elif (date(2021, 10, 1) < s.fecha_Inspeccion < date(2021, 12, 31)):
                contbuques4 = contbuques4 + 1
        if (s.medio == 'contenedor'):
            if (date(2021, 1, 1) < s.fecha_Inspeccion < date(2021, 3, 31)):
                contcont1 = contcont1 + 1
            elif (date(2021, 4, 1) < s.fecha_Inspeccion < date(2021, 6, 30)):
                contcont2 = contcont2 + 1
            elif (date(2021, 7, 1) < s.fecha_Inspeccion < date(2021, 9, 30)):
                contcont3 = contcont3 + 1
            elif (date(2021, 10, 1) < s.fecha_Inspeccion < date(2021, 12, 31)):
                contcont4 = contcont4 + 1
    for c in Cliente.objects.all():
        if (c.tipo_empresa == 'Deportes Mixtas'):
            mixtas = mixtas + 1
        elif (c.tipo_empresa == 'TCP'):
            tcp = tcp + 1
        elif (c.tipo_empresa == 'CNA'):
            cna = cna + 1
        elif (c.tipo_empresa == 'Deportes 100% Cubanas'):
            estatales = estatales + 1
        elif (c.tipo_empresa == 'Empresa Extranjera'):
            extranjeras = extranjeras + 1

    client = clientes.count()
    soli = solicitudes.count()
    ord = ordenes.count()
    context = {
        'orden': ordenes,
        'Solicitud': soli,
        'Clientes': client,
        'estatales': estatales,
        'mixtas': mixtas,
        'cna': cna,
        'tcp': tcp,
        'extranjeras': extranjeras,
        'Ordenes': ord,
        'contenedores': contenedores,
        'buques': buques,
        'contbuques1': contbuques1,
        'contbuques2': contbuques2,
        'contbuques3': contbuques3,
        'contbuques4': contbuques4,
        'contcont1': contcont1,
        'contcont2': contcont2,
        'contcont3': contcont3,
        'contcont4': contcont4,
    }
    return render(request, "operaciones/inicio.html", context)

@login_required
def registro(request):
    data = {
        'form': CuastomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CuastomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            # user = authenticate(username=formulario.cleaned_data["username"],
            #                     password=formulario.cleaned_data["password1"])
            # login(request, user)
            messages.success(request, "Se ha creado el usuario correctamente")
            return redirect(to="listar_usuarios")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)
@login_required
def listar_usuarios(request):
    data={
        'usuarios':User.objects.all()
    }
    return render(request, 'registration/listar_usuarios.html', data)
@login_required
def eliminar_usuario(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    messages.success(request, "Usuario eliminado")
    return redirect(to="listar_usuarios")
def modificar_usuario(request, id):
    user = get_object_or_404(User, id=id)
    data = {
        "form": CuastomUserCreationForm(instance=user)
    }
    if request.method == 'POST':
        formulario = CuastomUserCreationForm(data=request.POST, instance=user)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha actualizado el usuario")
            return redirect(to="listar_usuarios")
        data["form"] = formulario
    return render(request, 'operaciones/Clientes/modificar_usuario.html', data)

@login_required
def nuevo_cliente(request):
    data = {
        'form': ClienteForm()
    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha creado el cliente correctamente")
            return redirect(to="listar_cliente")
        data = {
            "form": formulario,
        }

    return render(request, 'operaciones/Clientes/Nuevo_Cliente.html', data)
@login_required
def listar_cliente(request):
    data = {
        "empresas": Empresa.objects.all(),
        "clientes": Cliente.objects.all(),
    }
    return render(request, 'operaciones/Clientes/Listar_Clientes.html', data)
@login_required
def cliente_reporte(request):
    data = {
        "clientes": Cliente.objects.all(),
    }
    return render(request, 'reportes/clientes.html', data)
@login_required
def modificar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    data = {
        "form": ClienteForm(instance=cliente)
    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha actualizado el cliente")
            return redirect(to="listar_cliente")
        data["form"] = formulario
    return render(request, 'operaciones/Clientes/Modificar_Cliente.html', data)
@login_required
def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return redirect(to="listar_cliente")

@login_required
def listar_buques(request):
    data = {
        "buques": Buque.objects.all()
    }
    return render(request, 'operaciones/Buques/Listar_Buques.html', data)
@login_required
def nuevo_buque(request):
    data = {
        'form': BuqueForm()
    }
    if request.method == 'POST':
        formulario = BuqueForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha creado el buque correctamente")
            return redirect(to="listar_buques")
        data = {
            "form": formulario
        }

    return render(request, 'operaciones/Buques/Nuevo_Buque.html', data)
@login_required
def eliminar_buque(request, id):
    servicio = get_object_or_404(Buque, id=id)
    servicio.delete()
    return redirect(to="listar_buques")
@login_required
def modificar_buque(request, id):
    buque = get_object_or_404(Buque, id=id)
    data = {
        "form": BuqueForm(instance=buque)
    }
    if request.method == 'POST':
        formulario = BuqueForm(data=request.POST, instance=buque)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha actualizado el buque")
            return redirect(to="listar_buques")
        data["form"] = formulario
    return render(request, 'operaciones/Buques/Modificar_Buque.html', data)


@login_required
def listar_contenedor(request):
    data = {
        "contenedores": Contenedor.objects.all()
    }
    return render(request, 'operaciones/Contenedores/Listar_Contenedores.html', data)
@login_required
def modificar_contenedor(request, id):
    contenedor = get_object_or_404(Contenedor, id=id)
    data = {
        'form': ContenedorForm(instance=contenedor)
    }
    if request.method == 'POST':
        formulario = ContenedorForm(data=request.POST, instance=contenedor)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha actualizado el contenedor")
            return redirect(to="listar_contenedor")
        data = {
            "form": formulario
        }

    return render(request, 'operaciones/Contenedores/Modificar_Contenedor.html', data)

@login_required
def nuevo_contenedor(request):
    data = {
        'form': ContenedorForm()
    }
    if request.method == 'POST':
        formulario = ContenedorForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha creado el contenedor correctamente")
            return redirect(to="listar_contenedor")
        data = {
            "form": formulario
        }

    return render(request, 'operaciones/Contenedores/Nuevo_Contenedor.html', data)
@login_required
def eliminar_contenedor(request, id):
    var = get_object_or_404(Contenedor, id=id)
    var.delete()
    return redirect(to="listar_contenedor")


@login_required
def listar_personas(request):
    data = {
        "personas": Persona.objects.all()
    }
    return render(request, 'operaciones/Personas/Listar_Personas.html', data)
@login_required
def eliminar_persona(request, id):
    persona = get_object_or_404(Persona, ci=id)
    persona.delete()
    return redirect(to="listar_personas")
@login_required
def nueva_persona(request):
    data = {
        'form': PersonaForm()
    }
    if request.method == 'POST':
        formulario = PersonaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha creado la persona correctamente")
            return redirect(to="listar_personas")
        data = {
            "form": formulario
        }

    return render(request, 'operaciones/Personas/Nueva_Persona.html', data)
@login_required
def modificar_persona(request, id):
    persona = get_object_or_404(Persona, ci=id)
    data = {
        "form": PersonaForm(instance=persona)
    }
    if request.method == 'POST':
        formulario = PersonaForm(data=request.POST, instance=persona)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha actualizado la persona")
            return redirect(to="listar_personas")
        data["form"] = formulario
    return render(request, 'operaciones/Personas/Modificar_Personas.html', data)


@login_required
def listar_servicios(request):
    data = {
        "servicios": Servicios.objects.all()
    }
    return render(request, 'operaciones/Servicios/Listar_Servicios.html', data)
@login_required
def eliminar_servicio(request, id):
    servicio = get_object_or_404(Servicios, id=id)
    servicio.delete()
    return redirect(to="listar_servicios")
@login_required
def nuevo_servicio(request):
    data = {
        'form': ServicioForm()
    }
    if request.method == 'POST':
        formulario = ServicioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha creado el servicio correctamente")
            return redirect(to="listar_servicios")
        data = {
            "form": formulario
        }

    return render(request, 'operaciones/Servicios/Nuevo_Servicio.html', data)
@login_required
def modificar_servicio(request, id):
    servicio = get_object_or_404(Servicios, id=id)
    data = {
        "form": ServicioForm(instance=servicio)
    }
    if request.method == 'POST':
        formulario = ServicioForm(data=request.POST, instance=servicio)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha actualizado el servicio")
            return redirect(to="listar_servicios")
        data["form"] = formulario
    return render(request, 'operaciones/Servicios/Modificar_Servicio.html', data)


@login_required
def listar_ordenes(request):
    data = {
        "ordenes": Orden.objects.all()
    }
    return render(request, 'operaciones/Ordenes/Listar_Ordenes.html', data)
@login_required
def nueva_orden(request):
    data = {
        'form': OrdenForm()
    }
    if request.method == 'POST':
        formulario = OrdenForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha creado la orden correctamente")
            return redirect(to="listar_ordenes")
        data = {
            "form": formulario
        }
    return render(request, 'operaciones/Ordenes/Nueva_orden.html', data)
@login_required
def eliminar_orden(request, id):
    orden = get_object_or_404(Orden, id=id)
    orden.delete()
    return redirect(to="listar_ordenes")
@login_required
def modificar_orden(request, id):
    orden = get_object_or_404(Orden, id=id)
    data = {
        "form": OrdenForm(instance=orden)
    }
    if request.method == 'POST':
        formulario = OrdenForm(data=request.POST, instance=orden)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha actualizado la orden")
            return redirect(to="listar_ordenes")
        data["form"] = formulario
    return render(request, 'operaciones/Ordenes/Modificar_Orden.html', data)


@login_required
def listar_deportes(request):
    data = {
        "deportes": Deporte.objects.all()
    }
    return render(request, 'operaciones/Deportes/Listar_Deportes.html', data)
@login_required
def eliminar_deporte(request, id):
    deporte = get_object_or_404(Deporte, id=id)
    deporte.delete()
    return redirect(to="listar_deportes")
@login_required
def nuevo_deporte(request):
    data = {
        'form': DeporteForm()
    }
    if request.method == 'POST':
        formulario = DeporteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha creado el deporte correctamente")
            return redirect(to="listar_deportes")
        data = {
            "form": formulario
        }

    return render(request, 'operaciones/Deportes/Nuevo_Deporte.html', data)
@login_required
def modificar_deporte(request, id):
    deporte = get_object_or_404(Deporte, id=id)
    data = {
        "form": DeporteForm(instance=deporte)
    }
    if request.method == 'POST':
        formulario = DeporteForm(data=request.POST, instance=deporte)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha actualizado el deporte")
            return redirect(to="listar_deportes")
        data["form"] = formulario
    return render(request, 'operaciones/Deportes/Modificar_Deportes.html', data)

@login_required
def listar_clases(request):
    data = {
        "clases": ClaseDeportiva.objects.all()
    }
    return render(request, 'operaciones/claseD/Listar_ClaseD.html', data)
@login_required
def eliminar_clase(request, id):
    clase = get_object_or_404(ClaseDeportiva, id=id)
    clase.delete()
    return redirect(to="listar_clases")
@login_required
def nueva_clase(request):
    data = {
        'form': ClaseDForm()
    }
    if request.method == 'POST':
        formulario = ClaseDForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha creado una nueva clase deportiva correctamente")
            return redirect(to="listar_clases")
        data = {
            "form": formulario
        }

    return render(request, 'operaciones/ClaseD/Nuevo_ClaseD.html', data)
@login_required
def modificar_clase(request, id):
    clase = get_object_or_404(ClaseDeportiva, id=id)
    data = {
        "form": ClaseDForm(instance=clase)
    }
    if request.method == 'POST':
        formulario =ClaseDForm(data=request.POST, instance=clase)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha actualizado la clase deportiva")
            return redirect(to="listar_clases")
        data["form"] = formulario
    return render(request, 'operaciones/ClaseD/Modificar_ClaseD.html', data)


@login_required
def listar_solicitud(request):
    data = {
        "solicitudes": Solicitud.objects.all(),
        'barcos': Buque.objects.all(),
        'contenedores': Contenedor.objects.all()
    }
    return render(request, 'operaciones/Solicitudes/Listar_Solicitudes.html', data)


@login_required
def eliminar_solicitud(request, id):
    solicitud = get_object_or_404(Solicitud, id=id)
    solicitud.delete()
    return redirect(to="listar_servicios")


@login_required
def nueva_solicitud(request):
    data = {
        'form': SolicitudForm(),
    }
    if request.method == 'POST':
        formulario = SolicitudForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha creado la solicitud correctamente")
            return redirect(to="listar_solicitud")
        data = {
            "form": formulario,
        }

    return render(request, 'operaciones/Solicitudes/Nueva_Solicitud.html', data)


@login_required
def modificar_solicitud(request, id):
    solicitud = get_object_or_404(Solicitud, id=id)
    data = {
        "form": SolicitudForm(instance=solicitud)
    }
    if request.method == 'POST':
        formulario = SolicitudForm(data=request.POST, instance=solicitud)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha actualizado la solicitud")
            return redirect(to="listar_solicitudes")
        data["form"] = formulario
    return render(request, 'operaciones/Solicitudes/Modificar_Solicitud.html', data)


@login_required
def subir_imagenes(request):
    data = {
        'form': ImagenesForm()
    }
    if request.method == 'POST':
        form = ImagenesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Se ha cargado la imagen")
            return redirect(to="listar_ordenes")
            messages.success(request, "Se ha cargado las imagenes correctamente")
        data = {
            "form": form
        }
    return render(request, 'operaciones/Ordenes/subir_imagenes.html', data)


def ver_imagenes(request, no_orden):
   imagenes=get_object_or_404(Imagenes, orden=no_orden)
   orden=no_orden
   data = {
        "no_orden": orden,
        "imagen": imagenes
    }
   return render(request, 'operaciones/Operaciones/ver_imagenes.html', data)


@login_required
def nuevo_vendedor(request):
    data = {
        'form': VendedorForm(),
    }
    if request.method == 'POST':
        formulario = VendedorForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha creado el vendedor correctamente")
            return redirect(to="listar_solicitud")
        data = {
            "form": formulario,
        }

    return render(request, 'operaciones/Solicitudes/Nuevo_Vendedor.html', data)


@login_required
def nuevo_comprador(request):
    data = {
        'form': CompradorForm(),
    }
    if request.method == 'POST':
        formulario = CompradorForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha creado el comprador correctamente")
            return redirect(to="listar_solicitud")
        data = {
            "form": formulario,
        }

    return render(request, 'operaciones/Solicitudes/Nuevo_Comprador.html', data)


@login_required
def nuevo_receptor(request):
    data = {
        'form': ReceptorForm(),
    }
    if request.method == 'POST':
        formulario = ReceptorForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha creado el receptor correctamente")
            return redirect(to="listar_solicitud")
        data = {
            "form": formulario,
        }

    return render(request, 'operaciones/Solicitudes/Nueva_Solicitud.html', data)

def parte(request):
    # Establecer el tipo de HTTPResponse
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=order.xls'
    # Crear un objeto de archivo
    wb = xlwt.Workbook(encoding='utf8')
    # Crear un objeto de hoja
    sheet = wb.add_sheet('order-sheet')

    # Establezca el estilo del encabezado del archivo. Esto no es necesario. Puede cambiarlo según sus necesidades.
    style_heading = xlwt.easyxf("""
              font:
                  name Arial,
                  colour_index white,
                  bold on,
                  height 0xA0;
              align:
                  wrap off,
                  vert center,
                  horiz center;
              pattern:
                  pattern solid,
                  fore-colour 0x19;
              borders:
                  left THIN,
                  right THIN,
                  top THIN,
                  bottom THIN;
              """)

    # Escribe el título del archivo
    sheet.write(0,0, 'Numero de Orden', style_heading)
    sheet.write(0, 1, 'Cliente', style_heading)
    sheet.write(0, 2, 'Fecha de la inspeccion', style_heading)
    sheet.write(0, 3, 'Medio de Carga', style_heading)

    # Escribir datos
    data_row = 1
    # UserTable.objects.all () Esta es una condición de consulta, que se puede ajustar de acuerdo con sus necesidades reales.
    for result in Orden.objects.all():
    # Formato de fecha y hora
        fecha = result.solicitud.fecha_Inspeccion.strftime('%Y-%m-%d')
        sheet.write(data_row, 0, result.no_orden)
        sheet.write(data_row, 1, result.solicitud.id_cliente.empresa.nombre)
        sheet.write(data_row, 2, fecha)
        sheet.write(data_row, 3, result.solicitud.medio)
        data_row = data_row + 1

    # Escribe a IO
    output = BytesIO()
    wb.save(output)
    # Reposición al principio
    output.seek(0)
    response.write(output.getvalue())
    return response
