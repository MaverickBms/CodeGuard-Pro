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
   almacena como hash Argon2. Nunca en texto plano. Es de un solo uso.
3. Tras el setup, se accede a `/accounts/login/` con usuario y contraseña maestra (Argon2).
4. La sesión es server-side con timeout de inactividad (defecto 15 min, configurable).
5. Al cerrar sesión o expirar por inactividad, se registra evento de auditoría.
6. Todas las vistas protegidas requieren autenticación (`@login_required`).

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

## 8. Próximos incrementos

- Incremento 2: Roadmap ASCENSO (33 etapas, dependencias, progreso).
- Incremento 3: Competencias y evaluaciones.
- Incremento 4: Biblioteca documental (PDF, FTS5) y base de conocimiento.
- Incremento 5: Evidencias y laboratorios.
- Incremento 6: Administración, backups y vigencia.
