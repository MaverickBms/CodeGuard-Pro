"""Punto de entrada de la aplicación desktop CodeGuard Pro.

Inicia el servidor Django embebido en 127.0.0.1 y abre la ventana nativa de
PySide6. El usuario no necesita abrir un navegador web.
"""

import sys
import os

# Asegurar que el directorio del proyecto esté en el path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from desktop.django_server import DjangoServer
from desktop.main_window import launch_desktop


def main():
    server = DjangoServer(host="127.0.0.1", port=0)
    actual_port = server.start()
    print(f"[CodeGuard Pro] Servidor Django iniciado en 127.0.0.1:{actual_port}")
    print(f"[CodeGuard Pro] URL interna: {server.url}")
    print("[CodeGuard Pro] Abriendo ventana de aplicación...")

    try:
        launch_desktop(server.url)
    finally:
        server.stop()
        print("[CodeGuard Pro] Servidor detenido. Aplicación cerrada.")


if __name__ == "__main__":
    main()
