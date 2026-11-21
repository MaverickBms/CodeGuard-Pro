"""Formularios del espacio editorial local."""

from __future__ import annotations

from django import forms

from .models import ContenidoLeccion, FuenteConocimiento, RecursoAudiovisual


class ContenidoLeccionForm(forms.ModelForm):
    class Meta:
        model = ContenidoLeccion
        fields = [
            "objetivos_aprendizaje",
            "conocimientos_previos",
            "introduccion",
            "teoria_tecnica",
            "explicacion_sencilla",
            "conceptos_fundamentales",
            "aplicaciones_practicas",
            "errores_frecuentes",
            "evaluacion_aprendizaje",
            "bibliografia_complementaria",
            "nivel_dificultad",
            "notas",
        ]
        widgets = {
            "objetivos_aprendizaje": forms.Textarea(attrs={"rows": 3}),
            "conocimientos_previos": forms.Textarea(attrs={"rows": 3}),
            "introduccion": forms.Textarea(attrs={"rows": 5}),
            "teoria_tecnica": forms.Textarea(attrs={"rows": 14}),
            "explicacion_sencilla": forms.Textarea(attrs={"rows": 8}),
            "conceptos_fundamentales": forms.Textarea(attrs={"rows": 8}),
            "aplicaciones_practicas": forms.Textarea(attrs={"rows": 7}),
            "errores_frecuentes": forms.Textarea(attrs={"rows": 6}),
            "evaluacion_aprendizaje": forms.Textarea(attrs={"rows": 7}),
            "bibliografia_complementaria": forms.Textarea(attrs={"rows": 3}),
            "notas": forms.Textarea(attrs={"rows": 3}),
        }


class FuenteConocimientoForm(forms.ModelForm):
    class Meta:
        model = FuenteConocimiento
        fields = [
            "publicador",
            "titulo",
            "url_canonica",
            "edicion",
            "identificador_licencia",
            "url_licencia",
            "notas",
        ]
        widgets = {
            "notas": forms.Textarea(attrs={"rows": 3}),
        }


class RevisionLicenciaForm(forms.Form):
    fuente_id = forms.IntegerField(widget=forms.HiddenInput)
    estado = forms.ChoiceField(
        choices=[
            ("compatible", "Reutilización compatible"),
            ("solo_referencia", "Solo consulta; contenido original"),
            ("requiere_permiso", "Requiere permiso"),
            ("no_reutilizable", "No reutilizable"),
        ]
    )
    evidencia = forms.URLField(assume_scheme="https", max_length=1000)
    alcance = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 2}))
    nota = forms.CharField(widget=forms.Textarea(attrs={"rows": 2}))


class RecursoAudiovisualForm(forms.ModelForm):
    class Meta:
        model = RecursoAudiovisual
        fields = [
            "titulo",
            "canal",
            "url",
            "subtitulos",
            "duracion_segundos",
            "objetivo_aprendizaje",
            "descripcion",
            "orden",
        ]
        widgets = {
            "objetivo_aprendizaje": forms.Textarea(attrs={"rows": 3}),
            "descripcion": forms.Textarea(attrs={"rows": 3}),
        }

    def save(self, commit=True):
        recurso = super().save(commit=False)
        recurso.idioma = "es"
        recurso.estado_revision = "en_revision"
        recurso.disponible = True
        if commit:
            recurso.save()
        return recurso
