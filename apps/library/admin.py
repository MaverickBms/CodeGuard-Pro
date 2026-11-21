"""Registro opcional de la biblioteca en el admin de desarrollo."""

from django.contrib import admin

from .models import DocumentoBiblioteca


@admin.register(DocumentoBiblioteca)
class DocumentoBibliotecaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "categoria", "estado", "tamano_bytes", "creado_en")
    list_filter = ("estado", "categoria")
    search_fields = ("titulo", "autor", "descripcion", "etiquetas")
    readonly_fields = ("sha256", "tamano_bytes", "nombre_original", "creado_en", "actualizado_en")
