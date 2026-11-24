"""Vistas de la biblioteca documental local."""

from __future__ import annotations

import re
from pathlib import Path

from django.db import IntegrityError, transaction

from django.contrib import messages
from django.core.paginator import Paginator
from django.http import FileResponse, Http404, HttpResponse, StreamingHttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.http import content_disposition_header
from django.views.decorators.http import require_POST, require_safe

from apps.accounts.identity import (
    get_usuario_actual,
    obtener_actor_auditoria,
    requiere_acceso,
)
from apps.audit.services import registrar_evento

from .forms import DocumentoBibliotecaForm
from .models import DocumentoBiblioteca

RANGO_RE = re.compile(r"^bytes=(\d*)-(\d*)$")
BLOQUE_LECTURA = 64 * 1024


@requiere_acceso
def lista(request):
    """Listado con búsqueda, filtro por categoría y paginación."""
    busqueda = (request.GET.get("q") or "").strip()[:120]
    categoria = (request.GET.get("categoria") or "").strip()
    estado = (request.GET.get("estado") or "activo").strip()
    if estado not in {"activo", "archivado", "todos"}:
        estado = "activo"

    documentos = DocumentoBiblioteca.objects.all()
    if estado != "todos":
        documentos = documentos.filter(estado=estado)
    if categoria in dict(DocumentoBiblioteca.CATEGORIAS):
        documentos = documentos.filter(categoria=categoria)
    if busqueda:
        from django.db.models import Q

        documentos = documentos.filter(
            Q(titulo__icontains=busqueda)
            | Q(autor__icontains=busqueda)
            | Q(descripcion__icontains=busqueda)
            | Q(etiquetas__icontains=busqueda)
        )

    paginator = Paginator(documentos.order_by("-creado_en", "-id"), 20)
    pagina = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "library/lista.html",
        {
            "pagina": pagina,
            "documentos": pagina.object_list,
            "busqueda": busqueda,
            "categoria_seleccionada": categoria,
            "estado_seleccionado": estado,
            "categorias": DocumentoBiblioteca.CATEGORIAS,
            "total": paginator.count,
        },
    )


@requiere_acceso
def importar(request):
    """Importa un PDF con validación de firma, tamaño y duplicados."""
    formulario = DocumentoBibliotecaForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and formulario.is_valid():
        sha256 = formulario._sha256
        existente = DocumentoBiblioteca.objects.filter(sha256=sha256).first()
        if existente is not None:
            formulario.add_error(
                "archivo",
                f"Ya existe un documento con el mismo contenido: «{existente.titulo}».",
            )
        else:
            documento = formulario.save(commit=False)
            documento.subido_por = get_usuario_actual(request)
            try:
                # La consulta previa ofrece un mensaje amigable; la restricción
                # UNIQUE de SQLite es la autoridad ante dos importaciones
                # simultáneas que superen esa consulta al mismo tiempo.
                with transaction.atomic():
                    documento.save()
            except IntegrityError:
                # No ocultar otros errores de integridad: solo traducimos el
                # conflicto cuando la restricción de hash ya tiene ganador.
                if not DocumentoBiblioteca.objects.filter(sha256=sha256).exists():
                    raise
                # FileField escribe el archivo antes del INSERT. Si la base de
                # datos rechazó el hash duplicado, retiramos el archivo huérfano.
                if documento.archivo and documento.archivo.name:
                    documento.archivo.storage.delete(documento.archivo.name)
                formulario.add_error(
                    "archivo",
                    "Ya existe un documento con el mismo contenido. No se creó una copia.",
                )
            else:
                registrar_evento(
                    "documento_biblioteca_importado",
                    usuario=obtener_actor_auditoria(request),
                    descripcion=(
                        f"Documento «{documento.titulo}» importado "
                        f"({documento.tamano_bytes} bytes, sha256 {documento.sha256[:12]}…)."
                    ),
                )
                messages.success(request, f"Documento importado: {documento.titulo}.")
                return redirect("library:detalle", pk=documento.pk)

    return render(
        request,
        "library/form.html",
        {"formulario": formulario, "categorias": DocumentoBiblioteca.CATEGORIAS},
    )


@requiere_acceso
def detalle(request, pk):
    documento = get_object_or_404(DocumentoBiblioteca, pk=pk)
    return render(
        request,
        "library/detalle.html",
        {"documento": documento, "archivo_disponible": documento.archivo_existe()},
    )


@requiere_acceso
@require_POST
def cambiar_estado(request, pk):
    documento = get_object_or_404(DocumentoBiblioteca, pk=pk)
    accion = (request.POST.get("accion") or "").strip()
    if accion == "archivar":
        documento.estado = "archivado"
        mensaje = "Documento archivado. Puedes restaurarlo desde el filtro Archivados."
    elif accion == "restaurar":
        documento.estado = "activo"
        mensaje = "Documento restaurado en la biblioteca activa."
    else:
        messages.error(request, "Acción no reconocida.")
        return redirect("library:detalle", pk=documento.pk)
    documento.save(update_fields=["estado", "actualizado_en"])
    registrar_evento(
        "documento_biblioteca_estado",
        usuario=obtener_actor_auditoria(request),
        descripcion=f"Documento «{documento.titulo}» → {documento.estado}.",
    )
    messages.success(request, mensaje)
    return redirect("library:detalle", pk=documento.pk)


def _ruta_pdf(documento: DocumentoBiblioteca) -> Path:
    if not documento.archivo:
        raise Http404("El documento no tiene archivo.")
    try:
        ruta = Path(documento.archivo.path).resolve()
        base = Path(documento.archivo.storage.location).resolve()
    except (ValueError, NotImplementedError, OSError) as exc:
        raise Http404("El archivo no está disponible.") from exc
    if not ruta.is_relative_to(base) or not ruta.is_file():
        raise Http404("El archivo no está disponible.")
    return ruta


def _cabeceras_pdf(respuesta, documento: DocumentoBiblioteca):
    respuesta["Content-Type"] = "application/pdf"
    respuesta["X-Content-Type-Options"] = "nosniff"
    respuesta["Content-Disposition"] = content_disposition_header(
        False, documento.nombre_original or f"documento-{documento.pk}.pdf"
    )
    respuesta["Accept-Ranges"] = "bytes"
    respuesta["Cache-Control"] = "private, no-store"
    # Permite que la ficha del documento incruste este PDF del mismo origen.
    respuesta._cg_allow_same_origin_frame = True
    return respuesta


@requiere_acceso
@require_safe
def archivo(request, pk):
    """Sirve el PDF localmente con soporte de rangos para el visor integrado."""
    documento = get_object_or_404(DocumentoBiblioteca, pk=pk)
    ruta = _ruta_pdf(documento)
    tamano = ruta.stat().st_size
    if tamano <= 0:
        raise Http404("El archivo está vacío.")

    rango = (request.headers.get("Range") or "").strip()
    coincidencia = RANGO_RE.match(rango) if rango else None
    if coincidencia is None:
        respuesta = FileResponse(
            open(ruta, "rb"), content_type="application/pdf"
        )
        respuesta["Content-Length"] = str(tamano)
        return _cabeceras_pdf(respuesta, documento)

    inicio_texto, fin_texto = coincidencia.groups()
    if (
        (inicio_texto and len(inicio_texto) > 20)
        or (fin_texto and len(fin_texto) > 20)
        or (not inicio_texto and not fin_texto)
    ):
        respuesta = HttpResponse(status=416)
        respuesta["Content-Range"] = f"bytes */{tamano}"
        return respuesta

    try:
        inicio_solicitado = int(inicio_texto) if inicio_texto else None
        fin_solicitado = int(fin_texto) if fin_texto else None
    except ValueError:
        respuesta = HttpResponse(status=416)
        respuesta["Content-Range"] = f"bytes */{tamano}"
        return respuesta

    if inicio_solicitado is None:
        longitud = fin_solicitado
        if longitud <= 0:
            respuesta = HttpResponse(status=416)
            respuesta["Content-Range"] = f"bytes */{tamano}"
            return respuesta
        inicio = max(tamano - longitud, 0)
        fin = tamano - 1
    else:
        inicio = inicio_solicitado
        fin = fin_solicitado if fin_solicitado is not None else tamano - 1
        if inicio >= tamano or fin < inicio:
            respuesta = HttpResponse(status=416)
            respuesta["Content-Range"] = f"bytes */{tamano}"
            return respuesta
        fin = min(fin, tamano - 1)

    longitud = fin - inicio + 1

    def leer_bloques():
        with open(ruta, "rb") as stream:
            stream.seek(inicio)
            restante = longitud
            while restante > 0:
                bloque = stream.read(min(BLOQUE_LECTURA, restante))
                if not bloque:
                    break
                restante -= len(bloque)
                yield bloque

    respuesta = StreamingHttpResponse(
        leer_bloques(), status=206, content_type="application/pdf"
    )
    respuesta["Content-Length"] = str(longitud)
    respuesta["Content-Range"] = f"bytes {inicio}-{fin}/{tamano}"
    return _cabeceras_pdf(respuesta, documento)
