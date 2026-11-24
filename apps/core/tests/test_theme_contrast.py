"""Regresión de los 12 temas: HEX oficiales y contraste WCAG.

Los colores oficiales de cada paleta no se modifican. Las variables derivadas
(texto, botones, bordes y focus) deben cumplir los umbrales declarados:

- texto, texto sobre superficie, texto de botón y texto secundario: 4.5:1 (AA)
- bordes y anillo de focus: 3:1 (componentes gráficos)
"""
import re
from pathlib import Path

from django.test import SimpleTestCase

CSS_THEMES = Path(__file__).resolve().parents[3] / "static" / "css" / "themes.css"

TEMAS_ESPERADOS = {
    "light": ("#FFBB94", "#FB9590", "#DC586D", "#A33757"),
    "dark": ("#190019", "#2B124C", "#522B5B", "#854F6C"),
    "high-contrast": ("#000000", "#111111", "#FFFF00", "#00FFFF"),
    "retro-pixel": ("#101820", "#1E2B36", "#00E5A8", "#FFCB47"),
    "cyberpunk": ("#080B1A", "#141A32", "#FF2E88", "#00E5FF"),
    "fantasy": ("#F4EFE2", "#FFFAF0", "#7952A1", "#B88943"),
    "sci-fi": ("#071723", "#0E2939", "#00BCD4", "#67E8F9"),
    "warrior": ("#1B1C1A", "#292C28", "#B68B4A", "#D05A3A"),
    "mage": ("#F0EDFF", "#FAF8FF", "#7555D9", "#3E8CAA"),
    "rogue": ("#101318", "#1B2028", "#6D8B74", "#C6A56B"),
    "paladin": ("#F5F2E7", "#FFFDF5", "#A78636", "#6C9B88"),
    "dark-mage": ("#100C1C", "#211631", "#9B6BDF", "#3F9CB0"),
}

PARES_TEXTO = (
    ("--cg-text", "--cg-bg"),
    ("--cg-text-on-surface", "--cg-surface"),
    ("--cg-on-primary", "--cg-primary"),
    ("--cg-text-secondary", "--cg-bg"),
)

PARES_GRAFICOS = (
    ("--cg-border", "--cg-bg"),
    ("--cg-border-focus", "--cg-bg"),
)


def _bloques(css: str) -> dict[str, dict[str, str]]:
    temas = {}
    patron = re.compile(
        r'(:root|\[data-theme="([a-z-]+)"\])\s*\{(.*?)\n\}', re.S
    )
    for coincidencia in patron.finditer(css):
        nombre = coincidencia.group(2) or "light"
        cuerpo = coincidencia.group(3)
        variables = dict(
            re.findall(r"(--cg-[a-z0-9-]+)\s*:\s*([^;]+);", cuerpo)
        )
        if "--cg-bg" in variables:
            temas[nombre] = variables
    return temas


def _color(valor: str, variables: dict[str, str]) -> tuple[int, int, int]:
    valor = valor.strip()
    hexa = re.fullmatch(r"#([0-9a-fA-F]{6})", valor)
    if hexa:
        codigo = hexa.group(1)
        return tuple(int(codigo[i : i + 2], 16) for i in (0, 2, 4))

    mezcla = re.fullmatch(
        r"color-mix\(in srgb,\s*(#[0-9a-fA-F]{6})\s+(\d+)%,\s*(#[0-9a-fA-F]{6})\s*\)",
        valor,
    )
    if mezcla:
        primero = _color(mezcla.group(1), variables)
        segundo = _color(mezcla.group(3), variables)
        proporcion = int(mezcla.group(2)) / 100
        return tuple(
            round(primero[i] * proporcion + segundo[i] * (1 - proporcion))
            for i in range(3)
        )

    mezcla_var = re.fullmatch(
        r"color-mix\(in srgb,\s*var\((--cg-[a-z0-9-]+)\)\s+(\d+)%,\s*"
        r"var\((--cg-[a-z0-9-]+)\)\s*\)",
        valor,
    )
    if mezcla_var:
        primero = _color(variables[mezcla_var.group(1)], variables)
        segundo = _color(variables[mezcla_var.group(3)], variables)
        proporcion = int(mezcla_var.group(2)) / 100
        return tuple(
            round(primero[i] * proporcion + segundo[i] * (1 - proporcion))
            for i in range(3)
        )

    raise AssertionError(f"Color no soportado por la prueba: {valor!r}")


def _luminancia(color: tuple[int, int, int]) -> float:
    def canal(valor: int) -> float:
        normalizado = valor / 255
        if normalizado <= 0.03928:
            return normalizado / 12.92
        return ((normalizado + 0.055) / 1.055) ** 2.4

    rojo, verde, azul = (canal(valor) for valor in color)
    return 0.2126 * rojo + 0.7152 * verde + 0.0722 * azul


def _contraste(primero, segundo) -> float:
    mayor, menor = sorted(
        (_luminancia(primero), _luminancia(segundo)), reverse=True
    )
    return (mayor + 0.05) / (menor + 0.05)


class ThemeContrastTests(SimpleTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.temas = _bloques(CSS_THEMES.read_text(encoding="utf-8"))

    def test_existen_los_doce_temas(self):
        self.assertEqual(set(self.temas), set(TEMAS_ESPERADOS))

    def test_conserva_los_hex_oficiales(self):
        for nombre, (bg, surface, primary, accent) in TEMAS_ESPERADOS.items():
            with self.subTest(tema=nombre):
                variables = self.temas[nombre]
                self.assertEqual(variables["--cg-bg"].upper(), bg.upper())
                self.assertEqual(variables["--cg-surface"].upper(), surface.upper())
                self.assertEqual(variables["--cg-primary"].upper(), primary.upper())
                self.assertEqual(variables["--cg-accent"].upper(), accent.upper())

    def test_pares_de_texto_cumplen_wcag_aa(self):
        for nombre, variables in self.temas.items():
            for primer_var, segunda_var in PARES_TEXTO:
                with self.subTest(tema=nombre, par=(primer_var, segunda_var)):
                    ratio = _contraste(
                        _color(variables[primer_var], variables),
                        _color(variables[segunda_var], variables),
                    )
                    self.assertGreaterEqual(
                        ratio,
                        4.5,
                        f"{nombre}: {primer_var}/{segunda_var} = {ratio:.2f}",
                    )

    def test_bordes_y_focus_cumplen_3_a_1(self):
        for nombre, variables in self.temas.items():
            for primer_var, segunda_var in PARES_GRAFICOS:
                with self.subTest(tema=nombre, par=(primer_var, segunda_var)):
                    ratio = _contraste(
                        _color(variables[primer_var], variables),
                        _color(variables[segunda_var], variables),
                    )
                    self.assertGreaterEqual(
                        ratio,
                        3.0,
                        f"{nombre}: {primer_var}/{segunda_var} = {ratio:.2f}",
                    )
