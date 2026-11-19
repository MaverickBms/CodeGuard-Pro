# Mundo CodeGuard — Aldea del Método

**Estado:** prototipo vertical jugable, integrado en CodeGuard Pro.  
**Rama:** `feature/mundo-codeguard`  
**Base:** `release/1.0.0`  
**Alcance:** una región explorable, tres NPC, dos misiones narrativas, un minijuego validado en servidor y persistencia local.

> El mundo es una capa de gamificación motivacional. **No aprueba lecciones,
> no modifica notas ni sustituye el progreso académico de ASCENSO 3.1.**

## 1. Arquitectura

| Capa | Archivos | Responsabilidad |
|---|---|---|
| Motor y bucle | `static/js/mundo/game.js` | Entrada, movimiento, cámara, render, diálogos, misiones, HUD, audio, guardado y limpieza |
| Modelo puro | `static/js/mundo/model.js` | Colisiones, cámara, distancia, interactuables, utilidades; probado con Node |
| Datos del mapa | `static/js/mundo/world.js` | Mapa 36×24, tiles, NPC y objetos de la Aldea del Método |
| Sprites | `static/js/mundo/sprites.js` | Pixel art procedural con Canvas; sin recursos externos |
| Vista | `templates/gamification/mundo.html` | Canvas, HUD, diálogos, misiones, inventario y controles accesibles |
| Estilos | `static/css/mundo.css` | Integración con las variables de los 12 temas, responsive y movimiento reducido |
| Dominio | `apps/gamification/mundo.py` | Región, misiones, interacciones, validación y recompensas idempotentes |
| Persistencia | `EstadoMundo` | Posición, banderas, misiones, inventario, XP y preferencia de audio |
| Endpoints | `apps/gamification/views.py` | Guardar posición, interactuar y completar misión |

No se añadieron dependencias JavaScript ni imágenes de terceros.

## 2. Primera versión jugable incluida

- Región **Aldea del Método** de 36×24 tiles, con río, puente, plaza, casas, árboles y decoración.
- Personaje con movimiento WASD/flechas, colisiones, cámara con seguimiento y animación de dos frames.
- Tres NPC: **Mentora Ada**, **Bibliotecario Byte** y **Guardián del Error**.
- Objetos interactivos: terminal, tres estanterías, cartel y cofre.
- Misión principal **El método de Ada** (hablar, practicar y volver).
- Misión secundaria **Fuentes con criterio** (tres estanterías y regreso con Byte).
- Minijuego **El error en la terminal**: tres preguntas de depuración validadas en el servidor; no se aprueba por azar.
- Recompensas: objetos de inventario, XP y monedas internas idempotentes.
- Guardado de posición, tiempo, audio, misiones e inventario en SQLite.
- Pausa, silencio de audio, controles táctiles y enlace a la etapa 0 real del roadmap.

## 3. Controles

| Acción | Teclado | Táctil |
|---|---|---|
| Mover | WASD o flechas | D-pad |
| Interactuar / avanzar diálogo | E o Enter | Botón E |
| Pausa | Esc o espacio | Botón Ⅱ |
| Silenciar | M | Botón de audio |

El canvas tiene foco y etiqueta ARIA. Los diálogos usan HTML y `textContent`,
no `innerHTML` con datos del servidor.

## 4. Persistencia y límites de confianza

`EstadoMundo` guarda únicamente estado del juego. El endpoint de guardado
**no acepta misiones ni inventario del cliente**: solo región, posición, dirección,
tiempo y preferencia de audio, con validación de tipos y límites del mapa.

Las interacciones se registran contra una lista cerrada de objetos. Las misiones
se validan en servidor:

- requisitos de banderas de interacción;
- minijuego con respuestas correctas privadas;
- recompensa de moneda idempotente por `referencia`;
- objeto de inventario idempotente por `origen`.

El mundo no escribe en `Progreso`, `ResultadoEvaluacion`, `CumplimientoCriterio`
ni en ningún modelo académico.

## 5. Integración con ASCENSO 3.1

La región piloto se asocia a la **etapa 0** del roadmap activo mediante su número
real. La vista muestra el título y un enlace a la etapa; si no hay roadmap
cargado, lo indica sin inventar relaciones. Las misiones del juego son narrativas
y no se presentan como aprobación de lecciones.

Para ampliar el mundo:

1. Añadir una región en `REGIONES` con su etapa real.
2. Añadir mapa y entidades en `world.js`.
3. Definir misiones con requisitos verificables.
4. Mantener las recompensas como gamificación, nunca como nota.
5. Añadir pruebas de servidor y de modelo puro.

## 6. Pruebas

- `apps/gamification/tests/test_mundo.py`: vista, guardado, límites, permisos,
  misión principal, idempotencia y validación del minijuego.
- `static/js/mundo/model.test.js`: mapa, colisiones, cámara, interactuables,
  direcciones, tiempo y unicidad de objetos.
- Verificación manual en Electron: carga del canvas, diálogo con Ada, movimiento,
  misión principal, apertura del minijuego, respuestas correctas y recompensa.
- `manage.py check` y migraciones deben ejecutarse en CI.

## 7. Limitaciones actuales

- Una sola región y un mapa prototipo; no es un mundo completo.
- No hay spritesheets externos ni música; el audio es un tono sintetizado mínimo.
- El guardado no sincroniza entre equipos (offline-first).
- Los diálogos y misiones están en español y son contenido narrativo original.
- No hay editor visual de mapas ni integración con paquetes de conocimiento.
- La aceptación en Windows físico y la ampliación de contenido académico siguen
  fuera del alcance de esta entrega.

## 8. Ejecución local

```bash
CODEGUARD_DATA_DIR=/tmp/cg-game \
DJANGO_SETTINGS_MODULE=config.settings.development \
python manage.py migrate

CODEGUARD_DATA_DIR=/tmp/cg-game \
DJANGO_SETTINGS_MODULE=config.settings.development \
python manage.py cargar_ascenso

npm start
```

Abre **Mundo CodeGuard** en la barra lateral o entra desde Gamificación.
