# Fase 2 — Sistema de aprendizaje interactivo

**Producto:** CodeGuard Pro  
**Estado:** Primer incremento implementado; validación local pendiente.  
**Línea base:** rama `main`.

## 1. Objetivo

Convertir cada lección del Roadmap ASCENSO en una unidad de estudio navegable y estructurada, sin confundir la existencia de una ficha académica con el dominio demostrado del contenido.

## 2. Alcance del primer incremento

Cada lección dispone ahora de una ruta propia y de una estructura de contenido separada del catálogo ASCENSO:

- **Contenido de lección:** objetivos de aprendizaje, teoría técnica, explicación sencilla, notas y estado de publicación.
- **Ejemplos guiados:** contexto, lenguaje, código, salida esperada y explicación paso a paso.
- **Ejercicios:** enunciado, instrucciones, lenguaje, nivel, código inicial, obligatoriedad y hasta tres campos de pistas.
- **Vista de estudio:** organiza las secciones anteriores y conserva navegación de regreso a la etapa.

La información fuente del Roadmap ASCENSO continúa siendo el catálogo de etapas, módulos y títulos de lecciones. El contenido pedagógico se almacena en entidades relacionadas, de modo que enriquecer una lección no modifica ni duplica los datos oficiales del roadmap.

## 3. Modelo de datos

```mermaid
erDiagram
    LECCION ||--o| CONTENIDO_LECCION : contiene
    LECCION ||--o{ EJEMPLO_LECCION : demuestra
    LECCION ||--o{ EJERCICIO_LECCION : practica
    LECCION ||--o{ PROGRESO : registra

    LECCION {
        bigint id PK
        bigint modulo_id FK
        string titulo
        text descripcion
        string tipo
        int orden
    }
    CONTENIDO_LECCION {
        bigint id PK
        bigint leccion_id FK
        text objetivos_aprendizaje
        text teoria_tecnica
        text explicacion_sencilla
        boolean publicado
    }
    EJEMPLO_LECCION {
        bigint id PK
        bigint leccion_id FK
        string titulo
        string lenguaje
        text codigo
        text salida_esperada
        text explicacion
        int orden
    }
    EJERCICIO_LECCION {
        bigint id PK
        bigint leccion_id FK
        string titulo
        text enunciado
        string nivel
        text codigo_inicial
        text pista_1
        text pista_2
        text pista_3
        boolean obligatorio
    }
```

## 4. Decisiones y límites

1. Abrir una lección registra el estado «En progreso» (5 % inicial); nunca la marca como completada.
2. La vista muestra solamente contenidos y ejercicios publicados.
3. Los ejercicios de este incremento son material didáctico; todavía no reciben código enviado ni se califican.
4. El editor, el envío de intentos y la evaluación reproducible pertenecen a la Fase 2. El tutor local y sus pistas progresivas pertenecen a la Fase 3.
5. Los tres campos de pistas fijan un máximo estructural de tres pistas por ejercicio. La entrega secuencial y el contador de pistas se implementarán junto al sistema de intentos del tutor.
6. La ruta antigua de marcado manual ya rechaza solicitudes para completar una lección. La finalización verificable se conectará cuando existan intentos y criterios de evaluación.
7. El modelo de progreso existente se conserva para no perder compatibilidad con los registros actuales.

## 5. Flujo previsto

```mermaid
flowchart TD
    A[Roadmap ASCENSO] --> B[Seleccionar lección]
    B --> C[Vista de estudio]
    C --> D[Teoría técnica]
    C --> E[Explicación sencilla]
    C --> F[Ejemplos guiados]
    C --> G[Ejercicios]
    G --> H[Editor y envío de intento — Fase 2]
    H --> I[Evaluación reproducible — Fase 2]
    I --> J[Tutor IA y pistas — Fase 3]
    J --> K[Criterios de dominio]
    K --> L[Completar lección automáticamente]
```

## 6. Próximos incrementos de la Fase 2

- Definir la plantilla editorial para que cada lección mantenga rigor técnico, explicación accesible y ejemplos suficientes.
- Diseñar e incorporar un mecanismo versionado para cargar y mantener grandes volúmenes de contenido sin editar directamente la base de datos.
- Implementar la navegación anterior/siguiente y el índice de secciones de la lección.
- Definir estados de lectura y progreso parcial sin permitir finalización manual.
- Implementar el contrato de intentos y evaluación reproducible de ejercicios, y conectar sus resultados con los criterios de finalización automática de lecciones.
- Añadir pruebas de integración y validar migraciones en una copia de la base de datos local.

## 7. Validación antes de considerar estable este incremento

Desde la carpeta local del proyecto:

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py migrate
python manage.py test apps.roadmaps
```

Luego iniciar CodeGuard Pro con `./run.sh`, abrir una etapa y entrar en una lección. La comprobación visual debe repetirse con los temas principales y en escritorio/móvil.

> No se considera completada la Fase 2 con este incremento. Se ha establecido el primer bloque de arquitectura y navegación; falta cargar contenido pedagógico real, implementar interacción con ejercicios y conectar los criterios de finalización.

## 8. Estado de autoría de contenidos

Los modelos y la vista de estudio ya están preparados, pero el repositorio todavía no contiene teoría, ejemplos y ejercicios editoriales para todas las lecciones. Tampoco debe asumirse que existe un editor disponible en la aplicación: `django.contrib.admin` no está instalado en la configuración actual. La autoría y publicación masiva de contenidos se resolverán mediante un flujo versionado de datos y revisión editorial antes de activar el material para estudiantes.

La ruta de estudio muestra un estado explícito de «Contenido en preparación» cuando una lección no tiene contenido publicado. No se presenta texto vacío como si fuera una lección terminada.

## 9. Auditoría y centralización de reglas de progreso — incremento en curso**Rama de trabajo:** `phase-2/progress-domain-rules`

Se detectó que las vistas impedían completar manualmente una lección, pero el servicio `marcar_leccion()` todavía aceptaba `completada=True`. De forma similar, `marcar_etapa()` permitía aprobar una etapa si sus prerrequisitos estaban satisfechos. Esto dejaba una vía interna para conceder progreso sin evidencia académica.

Correcciones realizadas en esta rama:

- `marcar_leccion()` rechaza la finalización manual y conserva únicamente la operación de reapertura.
- `marcar_etapa()` rechaza la aprobación manual y conserva únicamente la operación de reapertura; primero informa si faltan prerrequisitos.
- `recalcular_progreso_etapa()` calcula el porcentaje de cobertura, pero no convierte automáticamente el 100 % de lecciones registradas en aprobación de etapa.
- La aprobación de etapa queda reservada para un futuro servicio que valide evaluaciones y criterios obligatorios.
- Las pruebas se actualizaron para verificar el rechazo desde los servicios y desde la vista.

**Límite importante:** este incremento aún no incorpora un mecanismo autorizado para aprobar lecciones o etapas a partir de intentos/evaluaciones, porque ese modelo de evidencia todavía no existe. Tampoco sustituye una auditoría de todos los posibles puntos de escritura directa sobre el modelo `Progreso`. La validación local debe ejecutarse antes de integrar esta rama.


