from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Solicitudes_Epps, Solicitudes_Retiro, Solicitudes_Material
from .forms import SolicitudEppsForm, SolicitudRetiroForm, SolicitudMaterialForm
from django.http import HttpResponse
from django.contrib import messages  # Importa el módulo de mensajes de Django
from openpyxl import Workbook


def solicitudes_retiro(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SolicitudRetiroForm(request.POST, request.FILES)
            if form.is_valid():
                solicitud = form.save(commit=False)
                solicitud.id_usuario = request.user  # Asignar el objeto usuario
                solicitud.tipo_usuario = request.user.tipo_usuario
                solicitud.save()
                messages.success(request, 'Solicitud enviada correctamente.')
                return redirect('Solicitudes_Retiro')
        else:
            form = SolicitudRetiroForm()
        
        solicitudes_retiro = Solicitudes_Retiro.objects.all()
        return render(request, "solicitudes/solicitudes_retiro.html", {"solicitudes_retiro": solicitudes_retiro, "form": form})
    else:
        return redirect('Bloqueado')

def solicitudes_epps(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SolicitudEppsForm(request.POST, request.FILES)
            if form.is_valid():
                solicitud = form.save(commit=False)
                solicitud.id_usuario = request.user  # Asignar el objeto usuario
                solicitud.tipo_usuario = request.user.tipo_usuario
                solicitud.save()
                messages.success(request, 'Solicitud enviada correctamente.')
                return redirect('Solicitudes_Epps')
        else:
            form = SolicitudEppsForm()
        
        solicitudes_epps = Solicitudes_Epps.objects.all()
        return render(request, "solicitudes/solicitudes_epps.html", {"solicitudes_epps": solicitudes_epps, "form": form})
    else:
        return redirect('Bloqueado')

def solicitudes_material(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SolicitudMaterialForm(request.POST, request.FILES)
            if form.is_valid():
                solicitud = form.save(commit=False)
                solicitud.id_usuario = request.user  # Asignar el objeto usuario
                solicitud.tipo_usuario = request.user.tipo_usuario
                solicitud.save()
                messages.success(request, 'Solicitud enviada correctamente.')
                return redirect('Solicitudes_Material')
        else:
            form = SolicitudMaterialForm()
        
        solicitudes_material = Solicitudes_Material.objects.all()
        return render(request, "solicitudes/solicitudes_material.html", {"solicitudes_material": solicitudes_material, "form": form})
    else:
        return redirect('Bloqueado')

@login_required(login_url='Bloqueado')
def exportar_solicitudes_excel(request):
    # Obtener todas las solicitudes de retiro, EPPs y material
    solicitudes_retiro = Solicitudes_Retiro.objects.all()
    solicitudes_epps = Solicitudes_Epps.objects.all()
    solicitudes_material = Solicitudes_Material.objects.all()

    # Crear el nombre del archivo Excel con un nombre único
    filename = 'export_solicitudes.xlsx'

    # Crear un libro de trabajo de Excel y seleccionar la primera hoja
    wb = Workbook()
    ws = wb.active
    ws.title = "Solicitudes"

    # Escribir encabezados
    ws.append(['Usuario', 'Tipo de Solicitud', 'Fecha de Realización', 'Descripción', 'Estado', 'Cantidad', 'Tipo de Material'])

    # Escribir las solicitudes de retiro
    for solicitud in solicitudes_retiro:
        fecha_realizacion = solicitud.fecha_realizarR.strftime('%Y-%m-%d') if solicitud.fecha_realizarR else ''
        ws.append([
            solicitud.id_usuario.username,
            'Solicitud de Retiro',
            fecha_realizacion,
            solicitud.descripcionRetiro,
            'Verificado' if solicitud.estadoRetiro else 'No verificado',
            solicitud.cantidadRetiro,
            solicitud.tipo_materialRetiro
        ])

    # Escribir las solicitudes de EPPs
    for solicitud in solicitudes_epps:
        fecha_realizacion = solicitud.fecha_realizarEP.strftime('%Y-%m-%d') if solicitud.fecha_realizarEP else ''
        ws.append([
            solicitud.id_usuario.username,
            'Solicitud de EPPs',
            fecha_realizacion,
            solicitud.descripcionEpps,
            'Verificado' if solicitud.estadoEpps else 'No verificado',
            '',  # No hay cantidad en EPPs según el modelo proporcionado
            solicitud.tipo_materialEpps
        ])

    # Escribir las solicitudes de Material
    for solicitud in solicitudes_material:
        fecha_realizacion = solicitud.fecha_realizarM.strftime('%Y-%m-%d') if solicitud.fecha_realizarM else ''
        ws.append([
            solicitud.id_usuario.username,
            'Solicitud de Material',
            fecha_realizacion,
            solicitud.descripcionMaterial,
            'Verificado' if solicitud.estadoMaterial else 'No verificado',
            solicitud.cantidadMaterial,
            solicitud.tipo_material
        ])

    # Crear una respuesta HTTP con el archivo Excel adjunto
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    # Guardar el libro de trabajo y escribirlo en la respuesta HTTP
    wb.save(response)

    return response