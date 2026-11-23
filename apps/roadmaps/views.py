"""Vistas del módulo académico (roadmap ASCENSO).

Nota: Aplicación local, monousuario y offline-first. La identidad del usuario
actual proviene del flujo de autenticación; cuando la autenticación está
desactivada se usa el propietario local existente. No se crea identidad
implícita.
"""

from types import SimpleNamespace

from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from apps.accounts.identity import (
    get_usuario_actual,
    obtener_actor_auditoria,
    requiere_acceso,
)
from .models import (
    CriterioFinalizacion,
    CumplimientoCriterio,
    EjercicioLeccion,
    EstadoSincronizacion,
    Etapa,
    FuenteConocimiento,
    IntentoEjercicio,
    Leccion,
    PaqueteConocimientoInstalado,
    Pregunta,
    PublicacionPaqueteConocimiento,
    Quiz,
    ResultadoEvaluacion,
    VersionContenidoLeccion,
)
from .attempts import registrar_intento_ejercicio
from .services import (
    etapas_completadas,
    obtener_contenido_activo,
    iniciar_leccion,
    mapa_progreso_etapas,
    mapa_progreso_lecciones,
    mapa_progreso_modulos,
    marcar_etapa,
    marcar_leccion,
    progreso_general,
    roadmap_activo,
)
from .services_evaluacion import evaluar_quiz, registrar_cumplimiento_criterio


def _etapa_bloqueada_para_usuario(etapa, usuario) -> bool:
    """Comprueba prerrequisitos también en accesos directos a recursos."""
    completadas = etapas_completadas(usuario, etapa.roadmap) if usuario is not None else set()
    return etapa.esta_bloqueada_para(completadas)



@requiere_acceso
def evaluaciones(request):
    """Índice de evaluaciones publicadas de la ruta activa.

    Muestra únicamente quizzes/exámenes publicados, su etapa/módulo y el último
    intento del usuario. No permite enviar evaluaciones bloqueadas: el envío
    sigue validándose en ``evaluar_quiz``.
    """
    roadmap = roadmap_activo()
    if roadmap is None:
        return render(request, "roadmaps/sin_datos.html")

    usuario = get_usuario_actual(request)
    quizzes = list(
        Quiz.objects.filter(
            estado=Quiz.ESTADO_PUBLICADO,
        )
        .filter(Q(etapa__roadmap=roadmap) | Q(modulo__etapa__roadmap=roadmap))
        .select_related("etapa", "modulo__etapa")
        .prefetch_related("preguntas")
        .annotate(total_preguntas=Count("preguntas"))
        .order_by("etapa__numero", "modulo__numero", "nombre")
    )

    ultimo_resultado = {}
    if usuario is not None and quizzes:
        resultados = (
            ResultadoEvaluacion.objects.filter(usuario=usuario, quiz__in=quizzes)
            .select_related("quiz")
            .order_by("-creado_en")
        )
        for resultado in resultados:
            ultimo_resultado.setdefault(resultado.quiz_id, resultado)

    completadas = etapas_completadas(usuario, roadmap) if usuario is not None else set()
    for quiz in quizzes:
        quiz.etapa_real = quiz.modulo.etapa if quiz.modulo_id else quiz.etapa
        quiz.ultimo_resultado = ultimo_resultado.get(quiz.id)
        quiz.bloqueada = (
            quiz.etapa_real is not None
            and quiz.etapa_real.esta_bloqueada_para(completadas)
        )

    return render(
        request,
        "roadmaps/evaluaciones.html",
        {
            "roadmap": roadmap,
            "quizzes": quizzes,
            "total_publicadas": len(quizzes),
        },
    )


@requiere_acceso
def evidencias(request):
    """Portafolio local de evidencias de criterios de finalización."""
    roadmap = roadmap_activo()
    if roadmap is None:
        return render(request, "roadmaps/sin_datos.html")

    usuario = get_usuario_actual(request)
    cumplimientos = CumplimientoCriterio.objects.none()
    pendientes = CriterioFinalizacion.objects.none()

    if usuario is not None:
        cumplimientos = (
            CumplimientoCriterio.objects.filter(
                usuario=usuario,
                satisfecho=True,
                criterio__etapa__roadmap=roadmap,
            )
            .select_related("criterio__etapa")
            .order_by("-actualizado_en")
        )
        pendientes = (
            CriterioFinalizacion.objects.filter(
                etapa__roadmap=roadmap,
                obligatorio=True,
            )
            .exclude(cumplimientos__usuario=usuario, cumplimientos__satisfecho=True)
            .select_related("etapa")
            .order_by("etapa__numero", "orden", "id")[:100]
        )

    return render(
        request,
        "roadmaps/evidencias.html",
        {
            "roadmap": roadmap,
            "cumplimientos": cumplimientos,
            "pendientes": pendientes,
            "total_evidencias": cumplimientos.count(),
            "usuario_disponible": usuario is not None,
        },
    )


@requiere_acceso
def lista(request):
    """Listado de las 33 etapas con filtros, avance y estado de bloqueo."""
    roadmap = roadmap_activo()
    if roadmap is None:
        return render(request, "roadmaps/sin_datos.html")

    usuario = get_usuario_actual(request)

    etapas = list(
        roadmap.etapas.prefetch_related(
            "prerrequisitos__etapa_requerida", "modulos__lecciones"
        )
    )

    bloque = request.GET.get("bloque", "").strip()
    prioridad = request.GET.get("prioridad", "").strip()
    busqueda = request.GET.get("q", "").strip()

    if bloque:
        etapas = [etapa for etapa in etapas if etapa.bloque == bloque]
    if prioridad:
        etapas = [etapa for etapa in etapas if etapa.prioridad == prioridad]
    if busqueda:
        termino = busqueda.lower()
        etapas = [
            etapa
            for etapa in etapas
            if termino in etapa.titulo.lower()
            or termino in etapa.objetivo.lower()
            or any(
                termino in modulo.titulo.lower()
                or any(termino in leccion.titulo.lower() for leccion in modulo.lecciones.all())
                for modulo in etapa.modulos.all()
            )
        ]

    completadas = etapas_completadas(usuario, roadmap)
    progresos = mapa_progreso_etapas(usuario, roadmap)

    for etapa in etapas:
        etapa.progreso_actual = progresos.get(etapa.id)
        etapa.completada = etapa.numero in completadas
        etapa.bloqueada = etapa.esta_bloqueada_para(completadas)
        etapa.total_lecciones_cache = sum(
            len(modulo.lecciones.all()) for modulo in etapa.modulos.all()
        )

    resumen = {
        "total_etapas": roadmap.total_etapas,
        "total_modulos": roadmap.total_modulos,
        "total_lecciones": roadmap.total_lecciones,
        "total_proyectos": roadmap.total_proyectos,
        "por_prioridad": {
            fila["prioridad"]: fila["total"]
            for fila in roadmap.etapas.values("prioridad").annotate(total=Count("id"))
        },
    }
    avance = progreso_general(usuario, roadmap)
    bloques = list(
        roadmap.etapas.values_list("bloque", flat=True).distinct().order_by("bloque")
    )

    return render(
        request,
        "roadmaps/lista.html",
        {
            "roadmap": roadmap,
            "etapas": etapas,
            "resumen": resumen,
            "avance": avance,
            "bloques": bloques,
            "bloque_seleccionado": bloque,
            "prioridad_seleccionada": prioridad,
            "busqueda": busqueda,
        },
    )


@requiere_acceso
def detalle(request, numero):
    """Detalle de una etapa: módulos, lecciones, proyecto y prerrequisitos."""
    roadmap = roadmap_activo()
    if roadmap is None:
        return render(request, "roadmaps/sin_datos.html")

    usuario = get_usuario_actual(request)

    etapa = get_object_or_404(Etapa, roadmap=roadmap, numero=numero)
    etapas_ordenadas = list(
        roadmap.etapas.only("id", "numero", "titulo").order_by("orden", "numero")
    )
    indice_etapa = next(
        (indice for indice, item in enumerate(etapas_ordenadas) if item.pk == etapa.pk),
        None,
    )
    etapa_anterior = (
        etapas_ordenadas[indice_etapa - 1]
        if indice_etapa is not None and indice_etapa > 0
        else None
    )
    etapa_siguiente = (
        etapas_ordenadas[indice_etapa + 1]
        if indice_etapa is not None and indice_etapa + 1 < len(etapas_ordenadas)
        else None
    )
    modulos = list(etapa.modulos.prefetch_related("lecciones"))

    completadas = etapas_completadas(usuario, roadmap)
    progreso = mapa_progreso_etapas(usuario, roadmap).get(etapa.id)
    progresos_lecciones = mapa_progreso_lecciones(usuario, etapa)
    progresos_modulos = mapa_progreso_modulos(usuario, etapa)

    for modulo in modulos:
        modulo.lecciones_lista = list(modulo.lecciones.all())
        modulo.quizzes_publicados = list(
            modulo.quizzes.filter(estado=Quiz.ESTADO_PUBLICADO).order_by("id")
        )
        modulo.progreso_modulo = progresos_modulos.get(modulo.id)
        for leccion in modulo.lecciones_lista:
            leccion.progreso_actual = progresos_lecciones.get(leccion.id)
            leccion.completada = bool(
                leccion.progreso_actual
                and leccion.progreso_actual.estado == "completado"
            )

    examenes_etapa = list(
        Quiz.objects.filter(
            etapa=etapa, modulo__isnull=True, estado=Quiz.ESTADO_PUBLICADO
        ).order_by("id")
    )

    criterios = list(etapa.criterios.all())
    cumplimientos = {}
    if usuario is not None:
        cumplimientos = {
            c.criterio_id: c
            for c in CumplimientoCriterio.objects.filter(usuario=usuario, criterio__etapa=etapa)
        }
    for criterio in criterios:
        criterio.cumplimiento_actual = cumplimientos.get(criterio.id)
        criterio.satisfecho = bool(
            criterio.cumplimiento_actual and criterio.cumplimiento_actual.satisfecho
        )

    return render(
        request,
        "roadmaps/detalle.html",
        {
            "roadmap": roadmap,
            "etapa": etapa,
            "etapa_anterior": etapa_anterior,
            "etapa_siguiente": etapa_siguiente,
            "modulos": modulos,
            "progreso": progreso,
            "completada": etapa.numero in completadas,
            "completadas": completadas,
            "bloqueada": etapa.esta_bloqueada_para(completadas),
            "prerrequisitos": etapa.prerrequisitos.select_related("etapa_requerida"),
            "desbloquea": etapa.desbloquea.select_related("etapa"),
            "criterios": criterios,
            "examenes_etapa": examenes_etapa,
        },
    )


@requiere_acceso
@require_POST
def marcar_etapa_view(request, numero):
    """Marca o reabre una etapa completa (POST)."""
    roadmap = roadmap_activo()
    if roadmap is None:
        return redirect("roadmaps:lista")

    usuario = get_usuario_actual(request)
    if usuario is None:
        messages.error(
            request,
            "No hay un propietario local configurado. No se puede guardar el progreso.",
        )
        return redirect("roadmaps:detalle", numero=numero)

    etapa = get_object_or_404(Etapa, roadmap=roadmap, numero=numero)
    completada = request.POST.get("completada") == "1"

    try:
        marcar_etapa(
            usuario,
            etapa,
            completada=completada,
            actor_auditoria=obtener_actor_auditoria(request),
        )
    except ValueError as exc:
        messages.error(request, str(exc))
    else:
        if completada:
            messages.success(request, f"Etapa {etapa.numero} marcada como completada.")
        else:
            messages.info(request, f"Etapa {etapa.numero} reabierta.")

    return redirect("roadmaps:detalle", numero=etapa.numero)


@requiere_acceso
@require_POST
def marcar_leccion_view(request, leccion_id):
    """Marca o desmarca una lección (POST)."""
    usuario = get_usuario_actual(request)
    if usuario is None:
        messages.error(
            request,
            "No hay un propietario local configurado. No se puede guardar el progreso.",
        )
        return redirect("roadmaps:detalle", numero=1)

    leccion = get_object_or_404(
        Leccion.objects.select_related("modulo__etapa"), pk=leccion_id
    )
    completada = request.POST.get("completada") == "1"
    if completada:
        messages.warning(
            request,
            "Una lección no puede completarse manualmente. "
            "La finalización se habilitará cuando se verifiquen sus actividades.",
        )
        return redirect("roadmaps:leccion_detalle", leccion_id=leccion.id)

    marcar_leccion(
        usuario,
        leccion,
        completada=False,
        actor_auditoria=obtener_actor_auditoria(request),
    )
    messages.info(request, f"Lección reabierta: {leccion.titulo}")
    return redirect("roadmaps:detalle", numero=leccion.modulo.etapa.numero)


@requiere_acceso
@require_POST
def enviar_intento_view(request, ejercicio_id):
    """Registra y evalúa una entrega sin ejecutar código arbitrario."""
    roadmap = roadmap_activo()
    if roadmap is None:
        return redirect("roadmaps:lista")

    ejercicio = get_object_or_404(
        EjercicioLeccion.objects.select_related("leccion__modulo__etapa"),
        pk=ejercicio_id,
        leccion__modulo__etapa__roadmap=roadmap,
    )
    destino = f"{reverse('roadmaps:leccion_detalle', args=[ejercicio.leccion_id])}#ejercicio-{ejercicio.id}"
    usuario = get_usuario_actual(request)
    if usuario is None:
        messages.error(
            request,
            "No hay un propietario local configurado. No se puede guardar el intento.",
        )
        return redirect(destino)

    try:
        intento = registrar_intento_ejercicio(
            usuario,
            ejercicio,
            request.POST.get("respuesta", ""),
            actor_auditoria=obtener_actor_auditoria(request),
        )
    except ValidationError as exc:
        mensaje = exc.messages[0] if getattr(exc, "messages", None) else str(exc)
        messages.error(request, mensaje)
    else:
        if intento.resultado == "aprobado":
            messages.success(request, f"Ejercicio aprobado: {ejercicio.titulo}.")
        elif intento.resultado == "no_aprobado":
            messages.warning(request, "El intento quedó registrado. Revisa la retroalimentación y vuelve a intentarlo.")
        else:
            messages.info(request, "La entrega quedó guardada y pendiente de revisión/configuración.")

    return redirect(destino)


@requiere_acceso
def leccion_detalle(request, leccion_id):
    """Vista de estudio con teoría, explicación sencilla, ejemplos y ejercicios."""
    roadmap = roadmap_activo()
    if roadmap is None:
        return render(request, "roadmaps/sin_datos.html")

    leccion = get_object_or_404(
        Leccion.objects.select_related("modulo__etapa__roadmap")
        .prefetch_related("ejemplos", "ejercicios"),
        pk=leccion_id,
        modulo__etapa__roadmap=roadmap,
    )
    usuario = get_usuario_actual(request)
    etapa_leccion = leccion.modulo.etapa
    if _etapa_bloqueada_para_usuario(etapa_leccion, usuario):
        messages.warning(
            request,
            "Esta lección está bloqueada. Completa primero los prerrequisitos de la etapa.",
        )
        return redirect("roadmaps:detalle", numero=etapa_leccion.numero)

    progreso = None
    if usuario is not None:
        progreso = iniciar_leccion(
            usuario,
            leccion,
            actor_auditoria=obtener_actor_auditoria(request),
        )

    contenido_activo = obtener_contenido_activo(
        leccion, permitir_borrador=True
    )
    origen = contenido_activo["origen"]
    contenido = contenido_activo["contenido"]
    ejemplos = contenido_activo["ejemplos"]
    ejercicios = contenido_activo["ejercicios"]
    version_contenido_activa = contenido_activo["version"]
    paquete_contenido_activo = contenido_activo["paquete"]
    fuentes_contenido = []
    if version_contenido_activa is not None:
        for referencia in version_contenido_activa.referencias.select_related("fuente"):
            fuente = referencia.fuente
            fuentes_contenido.append(
                {
                    "publicador": fuente.publicador,
                    "titulo": fuente.titulo,
                    "url": fuente.url_canonica,
                    "edicion": fuente.edicion,
                    "licencia": fuente.get_estado_revision_licencia_display(),
                    "uso": referencia.get_uso_declarado_display(),
                    "localizador": referencia.localizador,
                    "nota": referencia.nota_atribucion,
                }
            )
    elif paquete_contenido_activo is not None:
        for fuente in paquete_contenido_activo.fuentes_catalogo.all():
            metadatos = fuente.metadatos if isinstance(fuente.metadatos, dict) else {}
            fuentes_contenido.append(
                {
                    "publicador": metadatos.get("publicador", ""),
                    "titulo": metadatos.get("titulo", "Fuente del paquete"),
                    "url": metadatos.get("url_canonica", ""),
                    "edicion": metadatos.get("edicion", ""),
                    "licencia": metadatos.get("estado_revision_licencia", ""),
                    "uso": metadatos.get("uso_declarado", ""),
                    "localizador": metadatos.get("localizador", ""),
                    "nota": metadatos.get("nota_atribucion", ""),
                }
            )
    ejercicios_modelo = list(leccion.ejercicios.all())

    if origen in ("paquete", "editorial"):
        leccion.titulo = contenido_activo["titulo"]
        leccion.descripcion = contenido_activo["descripcion"]
        leccion.tipo = contenido_activo["tipo"]

    intentos_por_ejercicio = {}
    if usuario is not None and ejercicios:
        filas = IntentoEjercicio.objects.filter(
            usuario=usuario, ejercicio__in=ejercicios_modelo
        ).order_by("-creado_en", "-id")
        for intento in filas:
            lista_intentos = intentos_por_ejercicio.setdefault(
                intento.ejercicio_id, []
            )
            if len(lista_intentos) < 3:
                lista_intentos.append(intento)

    evaluaciones_leccion = list(
        Quiz.objects.filter(
            estado=Quiz.ESTADO_PUBLICADO,
            preguntas__leccion=leccion,
        )
        .distinct()
        .order_by("nombre")
    )

    ejercicios_por_id = {item.id: item for item in ejercicios_modelo}
    for ejercicio in ejercicios:
        actual = ejercicios_por_id.get(ejercicio.id)
        ejercicio.intentos_usuario = (
            intentos_por_ejercicio.get(ejercicio.id, []) if actual else []
        )
        ejercicio.evaluacion_disponible = bool(
            actual and actual.configuraciones_evaluacion.filter(activo=True).exists()
        )

    return render(
        request,
        "roadmaps/leccion.html",
        {
            "roadmap": roadmap,
            "etapa": leccion.modulo.etapa,
            "modulo": leccion.modulo,
            "leccion": leccion,
            "contenido": contenido,
            "contenido_es_borrador": contenido_activo["es_borrador"],
            "estado_editorial": contenido_activo["estado_editorial"],
            "estado_editorial_etiqueta": {
                "pendiente": "Pendiente",
                "en_desarrollo": "En desarrollo",
                "borrador": "Borrador",
                "revision": "En revisión",
                "aprobada": "Aprobada",
                "publicada": "Publicada",
            }.get(contenido_activo["estado_editorial"], contenido_activo["estado_editorial"]),
            "ejemplos": ejemplos,
            "ejercicios": ejercicios,
            "videos": contenido_activo.get("videos", []),
            "progreso": progreso,
            "version_contenido_activa": version_contenido_activa,
            "paquete_contenido_activo": paquete_contenido_activo,
            "fuentes_contenido": fuentes_contenido,
            "evaluaciones_leccion": evaluaciones_leccion,
            "fuentes_paquete": list(paquete_contenido_activo.fuentes_catalogo.all()) if paquete_contenido_activo else [],
        },
    )


@requiere_acceso
def conocimiento(request):
    """Panel de solo lectura del flujo editorial y la distribución local.

    No publica, aprueba ni modifica contenido. Expone el estado real de fuentes,
    versiones, paquetes y sincronización para que el propietario pueda auditar
    el proceso sin confundir borradores con contenido publicado.
    """
    roadmap = roadmap_activo()
    if roadmap is None:
        return render(request, "roadmaps/sin_datos.html")

    versiones = VersionContenidoLeccion.objects.filter(
        leccion__modulo__etapa__roadmap=roadmap
    ).select_related("leccion__modulo__etapa")
    estados_version = {
        fila["estado"]: fila["total"]
        for fila in versiones.values("estado").annotate(total=Count("id"))
    }
    fuentes = FuenteConocimiento.objects.all().order_by("publicador", "titulo")[:200]
    paquetes = list(
        PaqueteConocimientoInstalado.objects.all().order_by("channel", "-sequence")[:20]
    )
    sincronizacion = list(
        EstadoSincronizacion.objects.select_related("active_package").order_by("channel")
    )
    publicaciones = list(
        PublicacionPaqueteConocimiento.objects.all().order_by("channel", "-sequence")[:20]
    )

    from .coverage import calcular_cobertura

    return render(
        request,
        "roadmaps/conocimiento.html",
        {
            "roadmap": roadmap,
            "cobertura": calcular_cobertura(roadmap),
            "fuentes": fuentes,
            "total_fuentes": FuenteConocimiento.objects.count(),
            "versiones": list(versiones.order_by("-publicada_en", "-id")[:50]),
            "estados_version": estados_version,
            "total_versiones": versiones.count(),
            "paquetes": paquetes,
            "sincronizacion": sincronizacion,
            "publicaciones": publicaciones,
            "lecciones_publicadas": versiones.filter(
                estado="publicada"
            ).values("leccion_id").distinct().count(),
        },
    )


def _preguntas_seguras(quiz: Quiz):
    """Devuelve preguntas sin exponer respuestas correctas al cliente."""
    preguntas = []
    for pregunta in quiz.preguntas.all():
        datos = pregunta.datos_respuesta if isinstance(pregunta.datos_respuesta, dict) else {}
        if pregunta.formato == Pregunta.FORMATO_SELECCION:
            opciones = []
            for idx, opcion in enumerate(datos.get("opciones", []) or []):
                if isinstance(opcion, dict):
                    opciones.append(
                        {
                            "indice": idx,
                            "texto": opcion.get("texto", opcion.get("valor", str(idx))),
                        }
                    )
            datos_publicos = {"opciones": opciones}
        elif pregunta.formato == Pregunta.FORMATO_RESPUESTA:
            datos_publicos = {}
        else:
            datos_publicos = {
                "criterios_count": len(datos.get("criterios", []) or [])
                if isinstance(datos.get("criterios"), list)
                else 0
            }
        preguntas.append(
            {
                "id": pregunta.id,
                "orden": pregunta.orden,
                "formato": pregunta.formato,
                "formato_display": pregunta.get_formato_display(),
                "enunciado": pregunta.enunciado,
                "leccion": pregunta.leccion,
                "datos": datos_publicos,
            }
        )
    return preguntas


@requiere_acceso
def quiz_detalle(request, quiz_id):
    """Muestra un quiz publicado y procesa su envío."""
    roadmap = roadmap_activo()
    if roadmap is None:
        return render(request, "roadmaps/sin_datos.html")
    quiz = get_object_or_404(
        Quiz.objects.select_related("modulo__etapa__roadmap", "etapa__roadmap").prefetch_related(
            "preguntas__leccion"
        ).filter(Q(modulo__etapa__roadmap=roadmap) | Q(etapa__roadmap=roadmap)),
        pk=quiz_id,
        estado=Quiz.ESTADO_PUBLICADO,
    )
    usuario = get_usuario_actual(request)
    etapa_acceso = quiz.modulo.etapa if quiz.modulo_id else quiz.etapa
    if etapa_acceso is not None and _etapa_bloqueada_para_usuario(etapa_acceso, usuario):
        messages.warning(
            request,
            "Esta evaluación está bloqueada. Completa primero los prerrequisitos de la etapa.",
        )
        return redirect("roadmaps:detalle", numero=etapa_acceso.numero)

    if request.method == "POST":
        if usuario is None:
            messages.error(
                request,
                "No hay un propietario local configurado. No se puede guardar el resultado.",
            )
            return redirect("roadmaps:quiz_detalle", quiz_id=quiz.id)

        respuestas = {}
        for pregunta in quiz.preguntas.all():
            clave = f"respuesta_{pregunta.id}"
            if pregunta.formato == Pregunta.FORMATO_SELECCION:
                valor = request.POST.get(clave)
                if valor is not None and valor != "":
                    respuestas[str(pregunta.id)] = (
                        int(valor) if str(valor).isdigit() else valor
                    )
            else:
                valor = request.POST.get(clave, "")
                respuestas[str(pregunta.id)] = valor

        try:
            resultado = evaluar_quiz(usuario, quiz, respuestas)
        except ValidationError as exc:
            mensaje = exc.messages[0] if getattr(exc, "messages", None) else str(exc)
            messages.error(request, mensaje)
            return redirect("roadmaps:quiz_detalle", quiz_id=quiz.id)

        if resultado.aprobado:
            messages.success(request, "Evaluación aprobada.")
        elif resultado.requiere_revision:
            messages.info(request, "Evaluación enviada. Algunas respuestas requieren revisión controlada.")
        else:
            messages.warning(request, "Evaluación registrada. Revisa los temas sugeridos para repaso.")
        return redirect("roadmaps:quiz_resultado", quiz_id=quiz.id, resultado_id=resultado.id)

    resultados_usuario = []
    if usuario is not None:
        resultados_usuario = list(
            ResultadoEvaluacion.objects.filter(quiz=quiz, usuario=usuario).order_by("-creado_en")[:10]
        )

    etapa_quiz = quiz.modulo.etapa if quiz.modulo_id else quiz.etapa
    return render(
        request,
        "roadmaps/quiz_detalle.html",
        {
            "quiz": quiz,
            "modulo": quiz.modulo,
            "etapa": etapa_quiz,
            "preguntas": _preguntas_seguras(quiz),
            "resultados_usuario": resultados_usuario,
        },
    )


@requiere_acceso
def quiz_resultado(request, quiz_id, resultado_id):
    """Muestra el resultado de un intento de quiz del usuario."""
    roadmap = roadmap_activo()
    if roadmap is None:
        return render(request, "roadmaps/sin_datos.html")
    quiz = get_object_or_404(
        Quiz.objects.select_related("modulo__etapa", "etapa").filter(
            Q(modulo__etapa__roadmap=roadmap) | Q(etapa__roadmap=roadmap)
        ),
        pk=quiz_id,
        estado=Quiz.ESTADO_PUBLICADO,
    )
    usuario = get_usuario_actual(request)
    if usuario is None:
        messages.error(request, "No hay un propietario local configurado.")
        return redirect("roadmaps:quiz_detalle", quiz_id=quiz.id)

    resultado = get_object_or_404(
        ResultadoEvaluacion.objects.prefetch_related("preguntas_resultados__pregunta"),
        pk=resultado_id,
        quiz=quiz,
        usuario=usuario,
    )
    etapa_quiz = quiz.modulo.etapa if quiz.modulo_id else quiz.etapa
    return render(
        request,
        "roadmaps/quiz_resultado.html",
        {
            "quiz": quiz,
            "modulo": quiz.modulo,
            "etapa": etapa_quiz,
            "resultado": resultado,
            "preguntas_resultados": list(resultado.preguntas_resultados.all()),
        },
    )


@requiere_acceso
def quiz_historial(request, quiz_id):
    """Muestra el historial de resultados del usuario para un quiz."""
    roadmap = roadmap_activo()
    if roadmap is None:
        return render(request, "roadmaps/sin_datos.html")
    quiz = get_object_or_404(
        Quiz.objects.select_related("modulo__etapa", "etapa").filter(
            Q(modulo__etapa__roadmap=roadmap) | Q(etapa__roadmap=roadmap)
        ),
        pk=quiz_id,
        estado=Quiz.ESTADO_PUBLICADO,
    )
    usuario = get_usuario_actual(request)
    resultados = []
    if usuario is not None:
        resultados = list(
            ResultadoEvaluacion.objects.filter(quiz=quiz, usuario=usuario).order_by("-creado_en")
        )
    etapa_quiz = quiz.modulo.etapa if quiz.modulo_id else quiz.etapa
    return render(
        request,
        "roadmaps/quiz_resultado.html",
        {
            "quiz": quiz,
            "modulo": quiz.modulo,
            "etapa": etapa_quiz,
            "resultado": None,
            "preguntas_resultados": [],
            "historial": resultados,
            "es_historial": True,
        },
    )


@requiere_acceso
@require_POST
def registrar_criterio_view(request, numero, criterio_id):
    """Registra evidencia/cumplimiento de un criterio de finalización (local)."""
    roadmap = roadmap_activo()
    if roadmap is None:
        return redirect("roadmaps:lista")

    usuario = get_usuario_actual(request)
    if usuario is None:
        messages.error(request, "No hay un propietario local configurado.")
        return redirect("roadmaps:detalle", numero=numero)

    etapa = get_object_or_404(Etapa, roadmap=roadmap, numero=numero)
    criterio = get_object_or_404(CriterioFinalizacion, pk=criterio_id, etapa=etapa)

    evidencia = (request.POST.get("evidencia") or "").strip()
    origen = (request.POST.get("origen") or "manual").strip() or "manual"
    if origen not in {"manual", "evidencia", "proyecto"}:
        origen = "manual"

    try:
        registrar_cumplimiento_criterio(
            usuario,
            criterio,
            evidencia=evidencia,
            origen=origen,
            referencia="ui:detalle_etapa",
        )
    except ValidationError as exc:
        mensaje = exc.messages[0] if getattr(exc, "messages", None) else str(exc)
        messages.error(request, mensaje)
    else:
        messages.success(request, f"Criterio registrado: {criterio.titulo}.")

    return redirect("roadmaps:detalle", numero=numero)
