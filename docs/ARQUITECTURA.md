# CodeGuard Pro — Documentación de arquitectura

**Producto:** CodeGuard Pro  
**Versión:** 1.0 (MVP, primer incremento)  
**Estado:** Implementado y verificado (incremento 1)  
**SRS de referencia:** `IEEE830(1).md` v2.0

---

## 1. Visión general

CodeGuard Pro es un **monolito modular** basado en Django (patrón MVT), ejecutado localmente
en `127.0.0.1`, sin dependencia de Internet, diseñado para un único usuario en un equipo con
recursos limitados (HP 240 G10, i3-N305, ~1.3 GB RAM libre, Fedora 44).

La arquitectura prioriza: bajo consumo de memoria/CPU, pocas dependencias, arranque rápido,
fácil mantenimiento y funcionamiento 100% offline.

---

## 2. Estructura de carpetas

```text
codeguard-pro/
├── manage.py
├── requirements.txt          # dependencias fijadas (versiones exactas)
├── .env.example              # variables de entorno (sin secretos reales)
├── .gitignore
├── README.md
│
├── config/                   # configuración del proyecto Django
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py           # settings base
│   │   └── development.py    # settings de desarrollo local
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── middleware.py         # middlewares de seguridad y sesión
│
├── apps/                     # aplicaciones Django (monolito modular)
│   ├── __init__.py
│   ├── core/                 # panel principal, navegación, configuración sistema
│   ├── accounts/             # identidad y acceso (login, setup, frase rescate, contraseña)
│   └── audit/                # registro de eventos de seguridad y acceso
│   [apps académicos pendientes: roadmaps, competencies, library, ...]
│
├── templates/                # plantillas base y por app (Django MVT)
├── static/                   # recursos estáticos locales (sin CDN)
│   ├── css/                  # Bootstrap 5.3.3 + estilos propios
│   └── js/                   # HTMX 2.0.4 + Bootstrap bundle
│
├── media/                    # archivos subidos (fuera del web root)
├── data/                     # datos adicionales
├── logs/                     # registros de ejecución
├── scripts/                  # scripts de utilidad
├── tests/                    # pruebas automatizadas
└── docs/                     # documentación del proyecto
```

Cada aplicación Django tiene responsabilidades delimitadas y evita acoplamiento entre módulos.

---

## 3. Componentes principales

| Componente | Responsabilidad | Estado |
|---|---|---|
| `apps.core` | Panel principal, navegación, configuración global (singleton) | Implementado (inc. 1) |
| `apps.accounts` | Identidad y acceso: login, logout, setup inicial, frase de rescate, cambio de contraseña | Implementado (inc. 1) |
| `apps.audit` | Registro de eventos de seguridad y acceso (auditoría) | Implementado (inc. 1) |
| `config.middleware` | Sesión por inactividad, cabeceras de seguridad, redirección setup inicial | Implementado (inc. 1) |
| `config.settings` | Configuración Django (base + desarrollo) | Implementado (inc. 1) |

Las aplicaciones académicas (`roadmaps`, `competencies`, `library`, `knowledge`, `assessments`,
`evidence`, `labs`, `progress`, `backups`, `vigencia`, `ethics`) se irán añadiendo en los
incrementos siguientes sin modificar el núcleo ya implementado.

---

## 4. Flujo de autenticación

1. **Primera vez:** no existe usuario → redirección a `/accounts/setup/` (configuración inicial:
   usuario, contraseña maestra ≥8 caracteres, aceptación de términos).
2. La frase de rescate se genera (alta entropía ≥128 bits), se muestra **una sola vez** y se
   almacena como hash Argon2. Nunca en texto plano. Es de un solo uso: **no se consume al
   validar**, solo al completar exitosamente el cambio de contraseña (flujo atómico en
   `cambiar_contrasena_por_frase`). Si el cambio falla, la frase no se consume.
3. Tras el setup, se accede a `/accounts/login/` con usuario y contraseña maestra (Argon2).
4. La sesión es server-side con timeout de inactividad (defecto 15 min, configurable).
5. El cierre de sesión exige **POST** (protegido por CSRF). GET devuelve 405.
6. Al cerrar sesión o expirar por inactividad, se registra evento de auditoría.
7. **Recuperación:** `/accounts/rescate/` valida la frase y redirige a
   `/accounts/rescate/resetear/` para establecer una nueva contraseña (con confirmación,
   validadores de Django y regla de no-reutilización de la actual).
8. Todas las vistas protegidas requieren autenticación (`@login_required`).
9. El middleware de inactividad comprueba la expiración **antes** de ejecutar la vista; una
   sesión vencida nunca modifica el progreso académico.

---

## 5. Seguridad por diseño

- **Bind exclusivo:** `127.0.0.1` (nunca `0.0.0.0`).
- **CSP:** `default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self'; frame-ancestors 'none'; base-uri 'self';`
- **Cabeceras:** `X-Frame-Options: DENY`, `X-Content-Type-Options: nosniff`,
  `Referrer-Policy: no-referrer`, `Permissions-Policy` restrictiva.
- **CSRF:** token en todas las peticiones que cambian estado.
- **Contraseñas:** Argon2 como hasher principal (`AUTH_PASSWORD_HASHERS`).
- **No secretos en logs ni en el repositorio:** `.env.example` sin valores reales, `.gitignore`
  excluye `.env`.
- **DEBUG:** `False` por defecto; `True` solo en desarrollo explícito.
- **Recursos estáticos:** servidos localmente, sin CDN, sin dependencia de Internet.

Ver `docs/SEGURIDAD.md` para el detalle completo.

---

## 6. Base de datos

SQLite con FTS5 verificado en el entorno real (SQLite 3.51.2). Las migraciones de Django se
aplican desde una base de datos vacía. Ver `docs/MODELO_DATOS.md`.

---

## 7. Despliegue y ejecución

**Servidor empaquetado (Electron):** `server_entry.py` arranca el WSGI de Django mediante
**Waitress** en `127.0.0.1:<CODEGUARD_PORT>` con **WhiteNoise** para servir los recursos
estáticos locales. No se usa `runserver --insecure`.

**Desarrollo:** `python manage.py runserver 127.0.0.1:8000` (solo desarrollo, `DEBUG=True`).

No se usan contenedores, máquinas virtuales ni servicios adicionales (RNF-001, restricciones de
hardware).

---

## 8. Sistema de diseño y 12 paletas

El frontend adopta un sistema visual unificado basado en variables CSS semánticas definidas
en `static/css/themes.css`. Cada tema consume exclusivamente sus propias variables; no
existen colores de marca hardcodeados fuera de dicho archivo.

### 8.1 Variables semánticas

`--cg-bg`, `--cg-surface`, `--cg-surface-hover`, `--cg-surface-elevated`,
`--cg-primary`, `--cg-primary-hover`, `--cg-primary-dark`, `--cg-accent`,
`--cg-text`, `--cg-text-secondary`, `--cg-text-muted`, `--cg-text-inverse`,
`--cg-border`, `--cg-border-focus`, `--cg-success`, `--cg-warning`,
`--cg-danger`, `--cg-info`, `--cg-shadow`, `--cg-radius`, `--cg-transition`.

Las transiciones usan propiedades concretas (no `all`). Se respeta `prefers-reduced-motion`.

### 8.2 Asignación de paletas oficiales a los 12 temas

Cada paleta utiliza exactamente los seis códigos HEX oficiales, mapeados en orden a
fondo, superficie, superficie-hover, superficie-elevada, primario, acento y texto.

| Tema | Paleta oficial | Códigos HEX |
|---|---|---|
| `light` | P01 — Coral y vino | `#FFBB94`, `#FB9590`, `#852E4E`, `#FB9590`, `#DC586D`, `#A33757`, `#4C1D3D` |
| `dark` | P02 — Ciruela y malva | `#190019`, `#2B124C`, `#DFB6B2`, `#2B124C`, `#522B5B`, `#854F6C`, `#FBE4DB` |
| `high-contrast` | P04 — Monocromática | `#000000`, `#1A1A1A`, `#333333`, `#000000`, `#FFFFFF`, `#D9D9D9`, `#FFFFFF` |
| `retro-pixel` | P05 — Rosa y frambuesa | `#E11D48`, `#F472B6`, `#FDE1E7`, `#F472B6`, `#FB7185`, `#FDBA74`, `#FFF7F9` |
| `cyberpunk` | P03 — Violeta eléctrico | `#0B0720`, `#25134D`, `#D1B8FF`, `#25134D`, `#6A2FC8`, `#9D71E8`, `#F2E9FF` |
| `fantasy` | P07 — Rosa empolvado | `#4B0F1F`, `#7A3F56`, `#F7EFEF`, `#7A3F56`, `#B78793`, `#E8C9D0`, `#FFFCFA` |
| `sci-fi` | P08 — Pizarra | `#0F172A`, `#334155`, `#E2E8F0`, `#334155`, `#64748B`, `#94A3B8`, `#F8FAFC` |
| `warrior` | P06 — Fuego y naranja | `#7F1D1D`, `#DC2626`, `#FFE4C7`, `#DC2626`, `#F97316`, `#FDBA74`, `#FFF7ED` |
| `mage` | P09 — Violeta y dorado | `#1A1A1F`, `#2D2B55`, `#F0D9B5`, `#2D2B55`, `#6A5ACD`, `#A678B9`, `#F4A62A` |
| `rogue` | P10 — Verde petróleo | `#0A0F14`, `#0F3D3E`, `#EADCC8`, `#0F3D3E`, `#2E6F73`, `#7FB3B8`, `#C6601F` |
| `paladin` | P11 — Azul y turquesa | `#0B132B`, `#1C2541`, `#F4D6B0`, `#1C2541`, `#3A506B`, `#5BC0BE`, `#D97706` |
| `dark-mage` | P12 — Tierra y madera | `#1A120E`, `#3A2418`, `#D5C4AE`, `#3A2418`, `#6B4A2E`, `#A88462`, `#4A4A46` |

Los identificadores de tema (`data-theme`, `localStorage`, menú de Electron) se conservan
sin cambios.

### 8.3 Accesibilidad cromática

- WCAG AA para texto normal en todos los temas.
- Alto contraste funcional en `high-contrast` (fondo negro, texto blanco, bordes blancos).
- Estados de foco visibles (`focus-visible` con `outline` en `--cg-border-focus`).
- No se depende exclusivamente del color para comunicar estados (etiquetas de texto,
  iconos y patrones complementan el código de color).

## 9. Próximos incrementos

- Incremento 2: Roadmap ASCENSO (33 etapas, dependencias, progreso).
- Incremento 3: Competencias y evaluaciones.
- Incremento 4: Biblioteca documental (PDF, FTS5) y base de conocimiento.
- Incremento 5: Evidencias y laboratorios.
- Incremento 6: Administración, backups y vigencia.
