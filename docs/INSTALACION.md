# CodeGuard Pro — Instalación

**Producto:** CodeGuard Pro  
**Versión:** 1.0 (MVP, primer incremento)  
**Entorno validado:** Fedora Linux 44 Workstation, Python 3.14.8, SQLite 3.51.2 (con FTS5)

---

## 1. Requisitos del sistema

| Componente | Requisito | Validado en |
|---|---|---|
| Python | 3.12+ | 3.14.8 |
| SQLite | con FTS5 | 3.51.2 (FTS5 confirmado) |
| Memoria | bajo consumo objetivo | ~1.3 GB libres observados |
| Disco | ~2 GB libres para la app | 108 GB disponibles |
| Red | no requerida (offline-first) | N/A |

---

## 2. Pasos de instalación

```bash
# 1. Entrar al directorio del proyecto
cd /home/mvxbms/Documentos/Estrada/CodeGuard

# 2. Crear entorno virtual (no instalar globalmente)
python3 -m venv .venv
source .venv/bin/activate

# 3. Instalar dependencias (versiones fijadas)
pip install --upgrade pip
pip install -r requirements.txt

# 4. Copiar variables de entorno y ajustar
cp .env.example .env
# Editar .env: definir DJANGO_SECRET_KEY (al menos 50 caracteres aleatorios)

# 5. Aplicar migraciones (crea la base de datos SQLite desde cero)
python manage.py migrate

# 6. Crear el usuario inicial (primera vez)
python manage.py shell
>>> from apps.accounts.services import crear_usuario_inicial
>>> u, frase = crear_usuario_inicial("admin", "TU_CONTRASEÑA_MAESTRA")
>>> print("FRASE DE RESCATE (guardarla, una sola vez):", frase)

# 7. Arrancar el servidor WSGI local (Waitress + WhiteNoise; solo en localhost)
python server_entry.py        # o: ./run.sh (prepara entorno e inicia Electron, el que arranca Django)
```

El servidor escucha exclusivamente en `127.0.0.1` (nunca `0.0.0.0`) en el puerto definido
por `CODEGUARD_PORT` (por defecto `8000`).

> **Nota (hardening):** el modelo de usuario activo es el custom `accounts.Usuario`
> (`AUTH_USER_MODEL = "accounts.Usuario"`). El usuario único persiste en la tabla
> `accounts_usuario` de la base de datos SQLite (`data/db.sqlite3`). La transición desde
> el usuario por defecto fue migrada sin pérdida de datos (ver `docs/DECISIONES_PENDIENTES.md`).

Luego abrir en el navegador: `http://127.0.0.1:8000/`

---

## 3. Configuración sensible (`.env`)

| Variable | Valor por defecto | Nota |
|---|---|---|
| `DJANGO_SECRET_KEY` | (obligatorio cambiar) | Clave secreta de Django |
| `DJANGO_DEBUG` | `False` | Nunca `True` en ejecución habitual |
| `DJANGO_ALLOWED_HOSTS` | `localhost,127.0.0.1,[::1]` | Solo localhost |
| `DJANGO_SESSION_TIMEOUT_MINUTES` | `15` | Inactividad antes de expirar |
| `DJANGO_LOG_LEVEL` | `INFO` | Nivel de logging |

---

## 4. Verificación de la instalación

Después de arrancar, comprobar:

1. `http://127.0.0.1:8000/` redirige a `/accounts/login/` (302).
2. El login con credenciales válidas accede al panel (200).
3. El servidor escucha solo en `127.0.0.1` (`ss -ltnp | grep 8000`).
4. No hay referencias a CDN en el código fuente de las páginas.
5. Las migraciones aplican desde una base de datos vacía (`python manage.py migrate`).

---

## 5. Modo desarrollo vs ejecución habitual

- **Desarrollo:** `DJANGO_DEBUG=True` (solo para depurar).
- **Ejecución habitual:** `DJANGO_DEBUG=False`, `DJANGO_SECRET_KEY` definida, servidor en `127.0.0.1`.

No activar `DEBUG` en producción local.

---

## 6. Limitaciones del entorno

- La partición principal está protegida con LUKS (cifrado en reposo con dispositivo apagado).
  Los backups trasladados a otro dispositivo no quedan automáticamente protegidos (ver
  `docs/SEGURIDAD.md`, RS-015).
- La memoria libre observada es menor de lo indicado en el SRS (~1.3 GB vs ~2.9 GiB). Se
  diseña para bajo consumo (1 worker, sin servicios innecesarios).
