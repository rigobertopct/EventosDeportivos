from _datetime import date
# 2.Implemente leer y escribir bytes en la memoria
from _datetime import date
# 2.Implemente leer y escribir bytes en la memoria
from io import BytesIO

# # 1. Exportar biblioteca de Excel
import xlwt
from django.contrib import messages
from django.contrib.admin.templatetags.admin_list import results
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
    data = {
        'usuarios': User.objects.all()
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
def nueva_disciplina(request):
    data = {
        'form': DisciplinaForm()
    }
    if request.method == 'POST':
        formulario = DisciplinaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha creado la Disciplina correctamente")
            return redirect(to="listar_disciplinas")
        data = {
            "form": formulario,
        }
    return render(request, 'operaciones/Disciplinas/Nueva_Disciplina.html', data)


@login_required
def listar_disciplinas(request):
    data = {
        "discilplinas": Disciplina.objects.all(),
    }
    return render(request, 'operaciones/Disciplinas/Listar_Disciplinas.html', data)


@login_required
def modificar_disciplina(request, id):
    disciplina = get_object_or_404(Disciplina, id=id)
    data = {
        "form": DisciplinaForm(instance=disciplina)
    }
    if request.method == 'POST':
        formulario = DisciplinaForm(data=request.POST, instance=disciplina)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha actualizado la Disciplina")
            return redirect(to="listar_disciplinas")
        data["form"] = formulario
    return render(request, 'operaciones/Disciplinas/Modificar_Disciplinas.html', data)


@login_required
def eliminar_disciplina(request, id):
    disciplina = get_object_or_404(Disciplina, id=id)
    disciplina.delete()
    return redirect(to="listar_disciplinas")


@login_required
def listar_atletas(request):
    data = {
        "atletas": Atleta.objects.all()
    }
    return render(request, 'operaciones/Atletas/Listar_Atletas.html', data)


@login_required
def nuevo_atleta(request):
    data = {
        'form': AtletaForm()
    }
    if request.method == 'POST':
        formulario = AtletaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha creado el atleta correctamente")
            return redirect(to="listar_atletas")
        data = {
            "form": formulario
        }
    return render(request, 'operaciones/Atletas/Nuevo_Atleta.html', data)


@login_required
def eliminar_atleta(request, id):
    atleta = get_object_or_404(Atleta, id=id)
    atleta.delete()
    return redirect(to="listar_atletas")


@login_required
def modificar_atleta(request, id):
    atleta = get_object_or_404(Atleta, id=id)
    data = {
        "form": AtletaForm(instance=atleta)
    }
    if request.method == 'POST':
        formulario = AtletaForm(data=request.POST, instance=atleta)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha actualizado el atleta")
            return redirect(to="listar_atletas")
        data["form"] = formulario
    return render(request, 'operaciones/Atletas/Modificar_Atleta.html', data)


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
        formulario = ClaseDForm(data=request.POST, instance=clase)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha actualizado la clase deportiva")
            return redirect(to="listar_clases")
        data["form"] = formulario
    return render(request, 'operaciones/ClaseD/Modificar_ClaseD.html', data)


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
    sheet.write(0, 0, 'Numero de Orden', style_heading)
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
