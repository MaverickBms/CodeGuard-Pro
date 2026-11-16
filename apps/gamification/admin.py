from django.contrib import admin

from .models import (
    AvatarPerfil,
    DecisionEvolutiva,
    ItemInventario,
    Logro,
    LogroObtenido,
    Mision,
    MisionProgreso,
    PerfilGamificacion,
    PersonajeGuia,
    TransaccionMoneda,
    ZonaMundo,
)


@admin.register(PerfilGamificacion)
class PerfilGamificacionAdmin(admin.ModelAdmin):
    list_display = ("usuario", "saldo_monedas", "racha_dias", "mejor_racha_dias", "actualizado_en")
    search_fields = ("usuario__username", "usuario__email")


@admin.register(Logro)
class LogroAdmin(admin.ModelAdmin):
    list_display = ("clave", "nombre", "recompensa_monedas", "activo")
    list_filter = ("activo",)
    search_fields = ("clave", "nombre")


@admin.register(LogroObtenido)
class LogroObtenidoAdmin(admin.ModelAdmin):
    list_display = ("usuario", "logro", "obtenido_en", "origen")
    search_fields = ("usuario__username", "logro__nombre", "origen")


@admin.register(TransaccionMoneda)
class TransaccionMonedaAdmin(admin.ModelAdmin):
    list_display = ("usuario", "tipo", "monto", "saldo_resultante", "concepto", "creada_en")
    list_filter = ("tipo",)
    search_fields = ("usuario__username", "concepto", "referencia")


@admin.register(ItemInventario)
class ItemInventarioAdmin(admin.ModelAdmin):
    list_display = ("usuario", "nombre", "rareza", "cantidad", "obtenido_en")
    list_filter = ("rareza",)
    search_fields = ("usuario__username", "nombre", "origen")


@admin.register(ZonaMundo)
class ZonaMundoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "etapa", "orden", "activo")
    list_filter = ("activo",)
    search_fields = ("nombre", "etapa__titulo")


@admin.register(PersonajeGuia)
class PersonajeGuiaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "zona", "rol", "activo")
    list_filter = ("activo",)
    search_fields = ("nombre", "rol")


@admin.register(AvatarPerfil)
class AvatarPerfilAdmin(admin.ModelAdmin):
    list_display = ("usuario", "nombre_avatar", "especie", "clase", "actualizado_en")
    search_fields = ("usuario__username", "nombre_avatar", "especie", "clase")


@admin.register(DecisionEvolutiva)
class DecisionEvolutivaAdmin(admin.ModelAdmin):
    list_display = ("avatar", "clave", "valor", "registrada_en")
    search_fields = ("clave", "valor", "avatar__usuario__username")


@admin.register(Mision)
class MisionAdmin(admin.ModelAdmin):
    list_display = ("clave", "nombre", "tipo", "objetivo", "recompensa_monedas", "activo")
    list_filter = ("tipo", "activo")
    search_fields = ("clave", "nombre")


@admin.register(MisionProgreso)
class MisionProgresoAdmin(admin.ModelAdmin):
    list_display = ("usuario", "mision", "progreso", "completada", "completada_en")
    list_filter = ("completada",)
    search_fields = ("usuario__username", "mision__nombre")
