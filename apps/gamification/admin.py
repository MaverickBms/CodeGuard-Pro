from django.contrib import admin

from .models import ItemInventario, Logro, LogroObtenido, PerfilGamificacion, TransaccionMoneda


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
