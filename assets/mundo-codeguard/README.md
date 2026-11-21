# Mundo CodeGuard — Biblioteca de personajes y criaturas

Biblioteca de recursos 2D pixel art para personajes, NPCs, fauna y criaturas de Mundo CodeGuard.

## Dirección artística

- Pixel art top-down 3/4, chibi y legible a escala reducida.
- Cuatro orientaciones base: south, west, east, north.
- Spritesheets independientes por personaje y por acción.
- PNG RGBA con transparencia real.
- Pies/pivote estables; celdas uniformes; sin texto dentro del arte.
- Los recursos conceptuales generados deben pasar revisión y normalización antes de declararse spritesheets de producción.

## Estructura

```
assets/mundo-codeguard/
  characters/
    CHR-001-mago/
      concept/
      spritesheets/
      manifest.json
  creatures/
  animals/
  shared/
  docs/
```

## Convención de nombres

`CHR-001_mago_walk_south_4f_64px.png`

Formato: `<ID>_<slug>_<action>_<direction>_<frames>_<cell-size>.png`

Direcciones: `south`, `west`, `east`, `north`, `south-west`, `south-east`, `north-west`, `north-east`.

## Primer personaje

CHR-001 — Mago. El primer paquete establece la escala, paleta, silueta, orientación, pivote y convención de manifiestos. No se considera terminado hasta validar recortes por celda, transparencia, alineación y reproducción de ciclos.

## Alcance

El catálogo se construirá personaje por personaje. Las categorías iniciales incluyen magia, civilizaciones, razas, criaturas míticas, criaturas oscuras, fauna doméstica, fauna salvaje, fauna de pantano, fauna acuática y fauna aérea.

## Integración

La biblioteca es independiente del motor. No presupone Godot, Unity ni otro motor. Los manifiestos describen celdas, FPS, anclaje y acciones para facilitar adaptadores futuros.
