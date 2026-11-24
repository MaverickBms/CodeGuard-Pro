"""Vistas del espacio editorial local.

Permiten al propietario local editar contenido, crear snapshots, ejecutar las
transiciones editoriales y gestionar fuentes y videos. No publican nada de
forma implícita: cada transición exige una acción explícita y queda auditada
por los servicios existentes.
"""

from __future__ import annotations

from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from apps.accounts.identity import get_usuario_actual, obtener_actor_auditoria, requiere_acceso
from apps.audit.services import registrar_evento

from .coverage import calcular_cobertura, detalle_editorial, invalidar_cache_cobertura, mapa_estados
from .forms import (
    ContenidoLeccionForm,
    FuenteConocimientoForm,
    RecursoAudiovisualForm,
    RevisionLicenciaForm,
)
from .knowledge import (
    aprobar_version_contenido,
    crear_version_contenido_leccion,
    enviar_version_a_revision,
    publicar_version_contenido,
    retirar_version_publicada,
    revisar_licencia_fuente,
)
from .models import (
    ContenidoLeccion,
    Etapa,
    FuenteConocimiento,
    Leccion,
    RecursoAudiovisual,
    VersionContenidoLeccion,
)
from .services import roadmap_activo


def _actor(request):
    return get_usuario_actual(request)


def _sin_roadmap(request):
    return render(request, "roadmaps/sin_datos.html")


@requiere_acceso
def editorial(request):
    """Listado de lecciones con su estado editorial y cobertura."""
    actor = _actor(request)
    if actor is None or not actor.is_staff:
        messages.error(request, "Se requieren permisos editoriales locales.")
        return redirect("core:panel")
    roadmap = roadmap_activo()
    if roadmap is None:
        return _sin_roadmap(request)

    estados = mapa_estados(roadmap)
    lecciones = list(
        Leccion.objects.filter(modulo__etapa__roadmap=roadmap)
        .select_related("modulo__etapa")
        .order_by("modulo__etapa__numero", "modulo__orden", "orden", "id")
    )
    etapa_filtro = request.GET.get("etapa", "").strip()
    estado_filtro = request.GET.get("estado", "").strip()
    busqueda = request.GET.get("q", "").strip()[:120]

    if etapa_filtro.isdigit():
        lecciones = [item for item in lecciones if item.modulo.etapa.numero == int(etapa_filtro)]
    if estado_filtro in {
        "pendiente", "en_desarrollo", "borrador", "revision", "aprobada", "publicada"
    }:
        lecciones = [
            item for item in lecciones
            if estados.get(item.id, {}).get("estado") == estado_filtro
        ]
    if busqueda:
        termino = busqueda.lower()
        lecciones = [
            item for item in lecciones
            if termino in item.titulo.lower()
            or termino in item.modulo.titulo.lower()
            or termino in item.modulo.etapa.titulo.lower()
        ]

    for leccion in lecciones:
        datos = estados.get(leccion.id, {})
        leccion.estado_editorial = datos.get("estado", "pendiente")
        leccion.estado_editorial_etiqueta = datos.get("etiqueta", "Pendiente")
        leccion.version_editorial = datos.get("version")
        leccion.contenido_editorial = datos.get("contenido")
        leccion.tiene_video = datos.get("tiene_video", False)
        leccion.tiene_fuentes = datos.get("tiene_fuentes", False)

    paginator = Paginator(lecciones, 40)
    pagina = paginator.get_page(request.GET.get("page"))
    cobertura = calcular_cobertura(roadmap)
    etapas = list(roadmap.etapas.order_by("numero"))

    return render(
        request,
        "roadmaps/editorial.html",
        {
            "roadmap": roadmap,
            "pagina": pagina,
            "lecciones": pagina.object_list,
            "cobertura": cobertura,
            "etapas": etapas,
            "etapa_filtro": etapa_filtro,
            "estado_filtro": estado_filtro,
            "busqueda": busqueda,
            "total_filtrado": paginator.count,
        },
    )


@requiere_acceso
def editorial_leccion(request, leccion_id):
    """Edita una lección y ejecuta transiciones editoriales explícitas."""
    leccion = get_object_or_404(
        Leccion.objects.select_related("modulo__etapa__roadmap"),
        pk=leccion_id,
    )
    roadmap = leccion.modulo.etapa.roadmap
    actor = _actor(request)
    if actor is None or not actor.is_staff:
        messages.error(request, "Se requieren permisos editoriales locales.")
        return redirect("core:panel")

    contenido = getattr(leccion, "contenido", None)
    formulario = ContenidoLeccionForm(instance=contenido)
    video_form = RecursoAudiovisualForm()
    detalle = detalle_editorial(leccion)

    if request.method == "POST":
        accion = (request.POST.get("accion") or "").strip()
        try:
            if accion == "guardar_contenido":
                formulario = ContenidoLeccionForm(request.POST, instance=contenido)
                if not formulario.is_valid():
                    messages.error(request, "Revisa los campos del contenido; se conservan los datos enviados.")
                else:
                    contenido = formulario.save(commit=False)
                    contenido.leccion = leccion
                    contenido.publicado = False
                    contenido.save()
                    registrar_evento(
                        "contenido_leccion_editado",
                        usuario=obtener_actor_auditoria(request),
                        descripcion=f"Contenido editado para la lección {leccion.id}.",
                    )
                    messages.success(request, "Contenido guardado como borrador editable.")
                    invalidar_cache_cobertura(roadmap.id)
                    return redirect("roadmaps:editorial_leccion", leccion_id=leccion.id)

            elif accion == "crear_version":
                fuente_ids = [
                    int(valor) for valor in request.POST.getlist("fuentes") if str(valor).isdigit()
                ]
                fuentes = list(FuenteConocimiento.objects.filter(pk__in=fuente_ids, activa=True))
                if not fuentes:
                    raise ValidationError("Selecciona al menos una fuente activa.")
                version = crear_version_contenido_leccion(
                    leccion,
                    resumen_cambios=(request.POST.get("resumen") or "").strip(),
                    fuentes=[
                        (fuente, "principal", "", "Fuente asociada desde el editor local.", "original")
                        for fuente in fuentes
                    ],
                )
                messages.success(request, f"Versión {version.pk} creada en borrador.")
                invalidar_cache_cobertura(roadmap.id)
                return redirect("roadmaps:editorial_leccion", leccion_id=leccion.id)

            elif accion in {"enviar_revision", "aprobar", "publicar", "retirar"}:
                version_id = int(request.POST.get("version_id") or 0)
                version = get_object_or_404(VersionContenidoLeccion, pk=version_id, leccion=leccion)
                if accion == "enviar_revision":
                    enviar_version_a_revision(version.pk, actor=actor)
                    messages.success(request, "Versión enviada a revisión.")
                elif accion == "aprobar":
                    aprobar_version_contenido(version.pk, actor=actor)
                    messages.success(request, "Versión aprobada.")
                elif accion == "publicar":
                    publicar_version_contenido(version.pk, actor=actor)
                    messages.success(request, "Versión publicada y activada para el estudiante.")
                else:
                    motivo = (request.POST.get("motivo") or "").strip()
                    retirar_version_publicada(version.pk, actor=actor, motivo=motivo)
                    messages.success(request, "Versión publicada retirada.")
                invalidar_cache_cobertura(roadmap.id)
                return redirect("roadmaps:editorial_leccion", leccion_id=leccion.id)

            elif accion == "crear_video":
                video_form = RecursoAudiovisualForm(request.POST)
                if not video_form.is_valid():
                    messages.error(request, "Revisa los datos del video.")
                else:
                    recurso = video_form.save(commit=False)
                    recurso.leccion = leccion
                    recurso.save()
                    messages.success(request, "Video añadido en revisión; no se mostrará hasta aprobarlo.")
                    invalidar_cache_cobertura(roadmap.id)
                    return redirect("roadmaps:editorial_leccion", leccion_id=leccion.id)

            elif accion == "revisar_video":
                video_id = str(request.POST.get("video_id") or "")
                if not video_id.isdigit():
                    raise ValidationError("Identificador de video no válido.")
                recurso = get_object_or_404(
                    RecursoAudiovisual, pk=int(video_id), leccion=leccion
                )
                decision = (request.POST.get("decision") or "").strip()
                if decision not in {"aprobado", "rechazado", "retirado"}:
                    raise ValidationError("Decisión de video no válida.")
                recurso.estado_revision = decision
                recurso.notas_verificacion = (request.POST.get("notas_verificacion") or "").strip()
                if decision == "aprobado":
                    if not recurso.notas_verificacion:
                        raise ValidationError(
                            "Documenta cómo verificaste título, idioma, audio y relación con el objetivo."
                        )
                    from django.utils import timezone

                    recurso.verificado_en = timezone.now()
                    recurso.verificado_por = actor
                    recurso.disponible = True
                recurso.save()
                messages.success(request, f"Video marcado como {recurso.get_estado_revision_display().lower()}.")
                invalidar_cache_cobertura(roadmap.id)
                return redirect("roadmaps:editorial_leccion", leccion_id=leccion.id)

            elif accion == "revisar_video_pedagogico":
                video_id = str(request.POST.get("video_id") or "")
                if not video_id.isdigit():
                    raise ValidationError("Identificador de video no válido.")
                recurso = get_object_or_404(
                    RecursoAudiovisual, pk=int(video_id), leccion=leccion
                )
                decision = (request.POST.get("decision_pedagogica") or "").strip()
                if decision not in {"pendiente", "aprobado", "rechazado"}:
                    raise ValidationError("Decisión pedagógica no válida.")
                notas = (request.POST.get("notas_pedagogicas") or "").strip()
                if decision == "aprobado":
                    if recurso.estado_revision != "aprobado":
                        raise ValidationError(
                            "Verifica primero el enlace y los metadatos del video."
                        )
                    if not notas:
                        raise ValidationError(
                            "Documenta la correspondencia temática, el nivel y la utilidad didáctica."
                        )
                    from django.utils import timezone

                    recurso.revisado_pedagogicamente_en = timezone.now()
                    recurso.revisado_pedagogicamente_por = actor
                elif decision == "pendiente":
                    recurso.revisado_pedagogicamente_en = None
                    recurso.revisado_pedagogicamente_por = None
                else:
                    from django.utils import timezone

                    recurso.revisado_pedagogicamente_en = timezone.now()
                    recurso.revisado_pedagogicamente_por = actor
                recurso.estado_pedagogico = decision
                recurso.notas_pedagogicas = notas
                recurso.save()
                messages.success(
                    request,
                    "Revisión pedagógica actualizada; no modifica la verificación técnica.",
                )
                return redirect("roadmaps:editorial_leccion", leccion_id=leccion.id)

            else:
                messages.error(request, "Acción editorial no reconocida.")
        except ValidationError as exc:
            mensajes = exc.messages if getattr(exc, "messages", None) else [str(exc)]
            for mensaje in mensajes:
                messages.error(request, mensaje)
        except (ValueError, TypeError) as exc:
            messages.error(request, f"No se pudo completar la acción: {exc}")

    fuentes_disponibles = FuenteConocimiento.objects.filter(activa=True).order_by(
        "publicador", "titulo"
    )
    detalle = detalle_editorial(leccion)
    return render(
        request,
        "roadmaps/editorial_leccion.html",
        {
            "roadmap": roadmap,
            "leccion": leccion,
            "etapa": leccion.modulo.etapa,
            "modulo": leccion.modulo,
            "contenido": contenido,
            "formulario": formulario,
            "video_form": video_form,
            "fuentes_disponibles": fuentes_disponibles,
            "detalle": detalle,
            "videos": detalle["videos"],
            "fuentes_version": detalle["fuentes"],
            "versiones": list(
                VersionContenidoLeccion.objects.filter(leccion=leccion).order_by(
                    "-numero_version"
                )
            ),
        },
    )


@requiere_acceso
def editorial_fuentes(request):
    """Registra fuentes y documenta decisiones de licencia."""
    actor = _actor(request)
    if actor is None or not actor.is_staff:
        messages.error(request, "Se requieren permisos editoriales locales.")
        return redirect("core:panel")

    if request.method == "POST":
        accion = (request.POST.get("accion") or "").strip()
        if accion == "crear_fuente":
            formulario = FuenteConocimientoForm(request.POST)
            if formulario.is_valid():
                fuente = formulario.save(commit=False)
                fuente.estado_revision_licencia = "pendiente"
                fuente.consultada_en = None
                fuente.save()
                messages.success(request, "Fuente registrada; revisa su licencia antes de usarla.")
                invalidar_cache_cobertura()
                return redirect("roadmaps:editorial_fuentes")
            messages.error(request, "Revisa los datos de la fuente.")
            revision_form = RevisionLicenciaForm()
        elif accion == "revisar_fuente":
            revision_form = RevisionLicenciaForm(request.POST)
            if revision_form.is_valid():
                fuente = get_object_or_404(
                    FuenteConocimiento, pk=revision_form.cleaned_data["fuente_id"]
                )
                try:
                    revisar_licencia_fuente(
                        fuente.pk,
                        actor=actor,
                        estado=revision_form.cleaned_data["estado"],
                        evidencia=revision_form.cleaned_data["evidencia"],
                        alcance=revision_form.cleaned_data["alcance"],
                        nota=revision_form.cleaned_data["nota"],
                    )
                    messages.success(request, "Decisión de licencia registrada.")
                    invalidar_cache_cobertura()
                except ValidationError as exc:
                    mensajes = exc.messages if getattr(exc, "messages", None) else [str(exc)]
                    for mensaje in mensajes:
                        messages.error(request, mensaje)
                return redirect("roadmaps:editorial_fuentes")
            messages.error(request, "Revisa la decisión de licencia; se conservan los datos enviados.")
            formulario = FuenteConocimientoForm()
        else:
            messages.error(request, "Acción de fuente no reconocida.")
            formulario = FuenteConocimientoForm()
            revision_form = RevisionLicenciaForm()
    else:
        formulario = FuenteConocimientoForm()
        revision_form = RevisionLicenciaForm()

    fuentes = list(
        FuenteConocimiento.objects.all().order_by("estado_revision_licencia", "publicador", "titulo")
    )
    return render(
        request,
        "roadmaps/editorial_fuentes.html",
        {
            "fuentes": fuentes,
            "formulario": formulario,
            "revision_form": revision_form,
        },
    )


@requiere_acceso
def cobertura(request):
    """Informe de cobertura editorial por etapa y estado."""
    roadmap = roadmap_activo()
    if roadmap is None:
        return _sin_roadmap(request)
    cobertura_actual = calcular_cobertura(roadmap)
    return render(
        request,
        "roadmaps/cobertura.html",
        {"roadmap": roadmap, "cobertura": cobertura_actual},
    )
