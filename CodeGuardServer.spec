# -*- mode: python ; coding: utf-8 -*-
"""PyInstaller spec del servidor Django local de CodeGuard Pro.

Genera ``dist-server/CodeGuardServer/CodeGuardServer.exe`` (Windows) o
``dist-server/CodeGuardServer/CodeGuardServer`` (Linux). Electron lo lanza como
proceso hijo y espera a que responda en 127.0.0.1.

Construir en Windows con::

    .venv\\Scripts\\pyinstaller --clean --noconfirm CodeGuardServer.spec

El resultado se copia a ``dist-server/`` y electron-builder lo incluye en
``resources/server`` mediante ``extraResources``.
"""

from pathlib import Path

from PyInstaller.utils.hooks import collect_data_files, collect_submodules

PROJECT_ROOT = Path(SPECPATH).resolve()

datas = [
    (str(PROJECT_ROOT / "apps" / "roadmaps" / "data"), "apps/roadmaps/data"),
    (str(PROJECT_ROOT / "templates"), "templates"),
    (str(PROJECT_ROOT / "static"), "static"),
]

# Traducciones y plantillas internas de Django (admin, auth, etc.).
datas += collect_data_files("django")

hiddenimports = [
    "config.settings.desktop",
    "apps.accounts",
    "apps.audit",
    "apps.core",
    "apps.roadmaps",
    "apps.roadmaps.management.commands.cargar_ascenso",
    "apps.roadmaps.management.commands.sincronizar_conocimiento",
    "apps.roadmaps.sync_client",
    "apps.roadmaps.distribution",
    "apps.roadmaps.installer",
    "argon2",
    "cryptography",
    "cryptography.hazmat.primitives.asymmetric.ed25519",
    "django",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.core.management",
    "django.db.backends",
    "django.db.backends.sqlite3",
    "whitenoise",
    "waitress",
]
hiddenimports += collect_submodules("apps")
hiddenimports += collect_submodules("django")

a = Analysis(
    ["server_entry.py"],
    pathex=[str(PROJECT_ROOT)],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        "PySide6",
        "PyQt5",
        "PyQt6",
        "tkinter",
        "matplotlib",
        "numpy",
        "pandas",
        "pytest",
        "IPython",
    ],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="CodeGuardServer",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=str(PROJECT_ROOT / "static" / "icons" / "icon.ico"),
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name="CodeGuardServer",
)
