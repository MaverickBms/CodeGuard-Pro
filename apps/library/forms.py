"""Formulario de importación de documentos PDF."""

from __future__ import annotations

from pathlib import Path

from django import forms
from django.core.exceptions import ValidationError

from .models import (
    MAX_PDF_BYTES,
    PDF_MAGIC,
    DocumentoBiblioteca,
    calcular_sha256,
)


class DocumentoBibliotecaForm(forms.ModelForm):
    class Meta:
        model = DocumentoBiblioteca
        fields = ["titulo", "autor", "categoria", "descripcion", "etiquetas", "archivo"]
        widgets = {
            "descripcion": forms.Textarea(attrs={"rows": 4, "maxlength": 5000}),
            "titulo": forms.TextInput(attrs={"maxlength": 200, "autofocus": True}),
            "autor": forms.TextInput(attrs={"maxlength": 160}),
            "etiquetas": forms.TextInput(attrs={"maxlength": 240}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["archivo"].widget.attrs["accept"] = "application/pdf,.pdf"
        self._sha256 = ""

    def clean_titulo(self):
        titulo = (self.cleaned_data.get("titulo") or "").strip()
        if not titulo:
            raise ValidationError("El documento necesita un título.")
        return titulo

    def clean_etiquetas(self):
        return (self.cleaned_data.get("etiquetas") or "").strip()

    def clean_archivo(self):
        archivo = self.cleaned_data.get("archivo")
        if not archivo:
            raise ValidationError("Selecciona un archivo PDF.")

        nombre = Path(getattr(archivo, "name", "") or "").name
        if not nombre.lower().endswith(".pdf"):
            raise ValidationError("Solo se admiten archivos con extensión .pdf.")

        tamano = getattr(archivo, "size", None)
        if tamano is None or tamano <= 0:
            raise ValidationError("El archivo está vacío.")
        if tamano > MAX_PDF_BYTES:
            raise ValidationError(
                f"El PDF supera el límite de {MAX_PDF_BYTES // (1024 * 1024)} MB."
            )

        try:
            archivo.seek(0)
            cabecera = archivo.read(len(PDF_MAGIC))
            archivo.seek(0)
        except (OSError, ValueError) as exc:
            raise ValidationError("No se pudo leer el archivo seleccionado.") from exc

        if cabecera != PDF_MAGIC:
            raise ValidationError("El archivo no es un PDF válido (firma %PDF- ausente).")

        self._sha256 = calcular_sha256(archivo)
        return archivo

    def save(self, commit: bool = True):
        documento = super().save(commit=False)
        archivo = self.cleaned_data.get("archivo")
        if archivo is not None:
            documento.nombre_original = Path(archivo.name).name[:255]
            documento.tamano_bytes = archivo.size
            documento.sha256 = self._sha256 or calcular_sha256(archivo)
            documento.mime_type = "application/pdf"
        if commit:
            documento.save()
            self.save_m2m()
        return documento
