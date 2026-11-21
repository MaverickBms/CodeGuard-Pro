"""Biblioteca documental local (Fase 4 del plan maestro).

Los documentos se guardan bajo ``MEDIA_ROOT`` (perfil del usuario), nunca
dentro del directorio de instalación. Solo se aceptan PDF verificados por
firma, tamaño y extensión; no se procesa su contenido ni se ejecuta nada.
"""

from __future__ import annotations

import hashlib
import uuid
from pathlib import Path

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.text import get_valid_filename


def documento_upload_to(instance, filename: str) -> str:
    """Genera una ruta segura sin confiar en el nombre enviado por el cliente."""
    nombre = get_valid_filename(Path(filename or "").name)[:120] or "documento.pdf"
    return f"biblioteca/{timezone.now():%Y/%m}/{uuid.uuid4().hex[:12]}-{nombre}"


class DocumentoBiblioteca(models.Model):
    """Metadatos y archivo de un PDF importado por el propietario local."""

    CATEGORIAS = [
        ("libro", "Libro"),
        ("articulo", "Artículo"),
        ("apunte", "Apunte"),
        ("manual", "Manual"),
        ("referencia", "Referencia"),
        ("otro", "Otro"),
    ]
    ESTADOS = [
        ("activo", "Activo"),
        ("archivado", "Archivado"),
    ]

    titulo = models.CharField(max_length=200, verbose_name="título")
    autor = models.CharField(max_length=160, blank=True, verbose_name="autor")
    categoria = models.CharField(
        max_length=20, choices=CATEGORIAS, default="referencia", verbose_name="categoría"
    )
    descripcion = models.TextField(blank=True, verbose_name="descripción")
    etiquetas = models.CharField(
        max_length=240,
        blank=True,
        verbose_name="etiquetas",
        help_text="Separa las etiquetas con comas.",
    )
    archivo = models.FileField(
        upload_to=documento_upload_to,
        max_length=255,
        verbose_name="archivo PDF",
    )
    nombre_original = models.CharField(max_length=255, blank=True, verbose_name="nombre original")
    sha256 = models.CharField(max_length=64, blank=True, verbose_name="SHA-256 del archivo")
    tamano_bytes = models.PositiveBigIntegerField(default=0, verbose_name="tamaño (bytes)")
    mime_type = models.CharField(
        max_length=80, default="application/pdf", verbose_name="tipo MIME"
    )
    estado = models.CharField(
        max_length=20, choices=ESTADOS, default="activo", verbose_name="estado"
    )
    subido_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="documentos_biblioteca",
        verbose_name="subido por",
    )
    creado_en = models.DateTimeField(auto_now_add=True, verbose_name="creado en")
    actualizado_en = models.DateTimeField(auto_now=True, verbose_name="actualizado en")

    class Meta:
        verbose_name = "documento de biblioteca"
        verbose_name_plural = "documentos de biblioteca"
        ordering = ["-creado_en", "-id"]
        indexes = [
            models.Index(fields=["estado", "categoria"]),
            models.Index(fields=["sha256"]),
        ]

    def __str__(self) -> str:
        return self.titulo

    def clean(self) -> None:
        super().clean()
        if not self.titulo or not self.titulo.strip():
            raise ValidationError({"titulo": "El documento necesita un título."})
        if self.sha256 and (
            len(self.sha256) != 64
            or any(caracter not in "0123456789abcdef" for caracter in self.sha256)
        ):
            raise ValidationError({"sha256": "El SHA-256 no es válido."})

    @property
    def tamano_mb(self) -> float:
        return round(self.tamano_bytes / (1024 * 1024), 2)

    @property
    def etiquetas_lista(self) -> list[str]:
        return [
            etiqueta.strip()
            for etiqueta in (self.etiquetas or "").split(",")
            if etiqueta.strip()
        ]

    def archivo_existe(self) -> bool:
        try:
            return bool(self.archivo and self.archivo.storage.exists(self.archivo.name))
        except Exception:
            return False


MAX_PDF_BYTES = 50 * 1024 * 1024
PDF_MAGIC = b"%PDF-"


def calcular_sha256(archivo) -> str:
    """Calcula el hash sin cargar el archivo completo en memoria."""
    posicion = archivo.tell() if hasattr(archivo, "tell") else 0
    hasher = hashlib.sha256()
    try:
        archivo.seek(0)
        while True:
            bloque = archivo.read(1024 * 1024)
            if not bloque:
                break
            hasher.update(bloque)
    finally:
        try:
            archivo.seek(posicion)
        except (OSError, ValueError):
            pass
    return hasher.hexdigest()
