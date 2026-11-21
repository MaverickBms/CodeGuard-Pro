"""Render seguro de texto académico con un subconjunto de Markdown.

El contenido editable no se marca como HTML confiable. Primero se escapa todo
y solo después se convierten negritas, código, listas y párrafos. Así el editor
puede escribir texto legible sin abrir una vía de XSS.
"""

from __future__ import annotations

import re

from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()

_BOLD = re.compile(r"\*\*(.+?)\*\*")
_CODE = re.compile(r"`([^`]+)`")
_ORDERED = re.compile(r"^\d+\.\s+")


def _inline(texto: str) -> str:
    texto = escape(texto)
    texto = _BOLD.sub(r"<strong>\1</strong>", texto)
    texto = _CODE.sub(r"<code>\1</code>", texto)
    return texto.replace("\n", "<br>")


@register.filter
def academico(value) -> str:
    """Convierte párrafos, listas, negritas y código en HTML escapado."""
    if value is None:
        return ""
    texto = str(value).strip()
    if not texto:
        return ""
    bloques = re.split(r"\n\s*\n", texto)
    salida = []
    for bloque in bloques:
        lineas = [linea.strip() for linea in bloque.splitlines() if linea.strip()]
        if not lineas:
            continue
        if all(linea.startswith("- ") for linea in lineas):
            items = "".join(f"<li>{_inline(linea[2:])}</li>" for linea in lineas)
            salida.append(f"<ul>{items}</ul>")
        elif all(_ORDERED.match(linea) for linea in lineas):
            items = "".join(
                f"<li>{_inline(_ORDERED.sub('', linea))}</li>" for linea in lineas
            )
            salida.append(f"<ol>{items}</ol>")
        else:
            salida.append(f"<p>{_inline(bloque.strip())}</p>")
    return mark_safe("\n".join(salida))
