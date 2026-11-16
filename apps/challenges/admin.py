from django.contrib import admin

from .models import Desafio, ResultadoDesafio


@admin.register(Desafio)
class DesafioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipo", "competencia", "dificultad", "etapa", "activo")
    list_filter = ("tipo", "dificultad", "activo")
    search_fields = ("nombre", "competencia", "descripcion")


@admin.register(ResultadoDesafio)
class ResultadoDesafioAdmin(admin.ModelAdmin):
    list_display = ("desafio", "usuario", "puntuacion", "completado", "creado_en")
    list_filter = ("completado",)
    search_fields = ("desafio__nombre", "usuario__username")
