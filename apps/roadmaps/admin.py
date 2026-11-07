"""Administración del módulo académico."""

from django.contrib import admin

from .models import (
    Actividad,
    CriterioFinalizacion,
    Etapa,
    Leccion,
    Modulo,
    Prerrequisito,
    Progreso,
    Roadmap,
)


class ModuloInline(admin.TabularInline):
    model = Modulo
    extra = 0
    fields = ("numero", "titulo", "orden")


@admin.register(Roadmap)
class RoadmapAdmin(admin.ModelAdmin):
    list_display = ("nombre", "edicion", "activo", "fecha_consolidacion")
    list_filter = ("activo", "edicion")
    search_fields = ("nombre", "fuente")


@admin.register(Etapa)
class EtapaAdmin(admin.ModelAdmin):
    list_display = ("numero", "titulo", "prioridad", "desarrollada_en_mvp", "roadmap")
    list_filter = ("prioridad", "desarrollada_en_mvp", "bloque", "roadmap")
    search_fields = ("titulo", "objetivo", "proyecto")
    ordering = ("roadmap", "numero")
    inlines = [ModuloInline]


@admin.register(Modulo)
class ModuloAdmin(admin.ModelAdmin):
    list_display = ("numero", "titulo", "etapa")
    list_filter = ("etapa__roadmap", "etapa__prioridad")
    search_fields = ("titulo", "numero")


@admin.register(Leccion)
class LeccionAdmin(admin.ModelAdmin):
    list_display = ("titulo", "modulo", "tipo", "orden")
    list_filter = ("tipo", "modulo__etapa__roadmap")
    search_fields = ("titulo", "descripcion")


@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ("titulo", "leccion", "tipo", "obligatoria")
    list_filter = ("tipo", "obligatoria")


@admin.register(Prerrequisito)
class PrerrequisitoAdmin(admin.ModelAdmin):
    list_display = ("etapa", "etapa_requerida", "documentado")
    list_filter = ("documentado",)
    search_fields = ("etapa__titulo", "etapa_requerida__titulo")


@admin.register(CriterioFinalizacion)
class CriterioFinalizacionAdmin(admin.ModelAdmin):
    list_display = ("etapa", "titulo", "tipo", "obligatorio")
    list_filter = ("tipo", "obligatorio")


@admin.register(Progreso)
class ProgresoAdmin(admin.ModelAdmin):
    list_display = ("usuario", "etapa", "estado", "porcentaje", "fecha_actualizacion")
    list_filter = ("estado", "etapa__roadmap")
    search_fields = ("usuario__username", "etapa__titulo")
