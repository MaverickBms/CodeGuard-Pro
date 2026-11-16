# Estructura del repositorio

**Referencia:** `main`, 16-11-2026.  
**Objetivo:** separar aplicación, recursos, automatización, documentación y datos versionados sin alterar el comportamiento del producto.

```text
CodeGuard-Pro/
├── apps/                       # Aplicaciones Django por dominio
│   ├── accounts/               # Identidad y autenticación local
│   ├── audit/                  # Auditoría de eventos
│   ├── challenges/             # Desafíos y minijuegos
│   ├── core/                   # Panel y navegación principal
│   ├── gamification/           # Recompensas, misiones, avatar
│   ├── roadmaps/               # Roadmap, progreso, contenido y sincronización
│   │   └── data/               # JSON académico versionado (no datos runtime)
│   └── tutoring/               # Tutor IA local
├── config/                     # Configuración, middleware y entrada WSGI/ASGI
├── electron/                   # Proceso principal y preload de Electron
├── templates/                  # Plantillas Django organizadas por dominio
├── static/                     # CSS, JS, fuentes e iconos locales
├── scripts/                    # Utilidades y pruebas smoke de empaquetado
├── docs/                       # Arquitectura, planes, operación, QA y ADR
│   ├── ADR/
│   ├── INFORMES_ACEPTACION/
│   ├── archivo/
│   └── referencias/
├── legacy/                     # Código histórico preservado, fuera del build activo
├── .env.example                # Plantilla sin secretos
├── CodeGuardServer.spec        # Especificación PyInstaller activa
├── server_entry.py             # Entrada del servidor empaquetado
├── manage.py                   # CLI Django
├── requirements.txt            # Dependencias Python fijadas
├── package.json                # Scripts y configuración Electron Builder
├── package-lock.json           # Lockfile npm; instalar con npm ci
├── build_windows.bat           # Orquestador de build Windows
├── run.sh                      # Lanzador Linux existente (sujeto a QA)
└── README.md                   # Presentación y acceso rápido
```

## Reglas de ubicación

- Una aplicación Django nueva vive en `apps/<dominio>/` e incluye modelos, servicios, URLs, migraciones y pruebas de su dominio.
- La configuración transversal vive en `config/`; no duplicar settings dentro de las apps.
- Los recursos servidos por Django viven en `static/`; las vistas en `templates/`.
- El proceso de escritorio vive en `electron/`; no mezclar lógica Django con el proceso principal de Electron.
- Los scripts de mantenimiento/build/test viven en `scripts/` o en la raíz solo cuando son entrypoints del sistema operativo.
- La documentación técnica y de producto vive en `docs/`; el control oficial permanece en la raíz.
- `apps/roadmaps/data/` contiene fuentes académicas versionadas. Los datos del estudiante, SQLite, logs, media y claves viven fuera del repositorio en el directorio de datos runtime.
- `legacy/` conserva implementaciones históricas para consulta; no importarlas desde el producto activo ni incluirlas en el empaquetado.

## Convenciones

- Nombres descriptivos en español para documentación y comandos de dominio; nombres Python en snake_case.
- No crear nuevos documentos de planificación en la raíz.
- Mantener un índice en cada carpeta documental con varias piezas relacionadas.
- No duplicar manuales: enlazar el documento canónico.
- No borrar migraciones, fuentes académicas, ADR ni evidencias de aceptación antiguas; marcarlas como históricas cuando corresponda.
