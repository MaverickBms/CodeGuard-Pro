"""Servidor Django embebido para la aplicación desktop CodeGuard Pro.

Inicia Django como servidor WSGI en 127.0.0.1 dentro de un hilo separado,
sin exponer la aplicación a la red local ni a Internet. La interfaz se
renderiza en una ventana nativa de PySide6 (QWebEngineView), por lo que el
usuario nunca necesita abrir un navegador web.
"""

import os
import sys
import threading
from wsgiref.simple_server import make_server, WSGIServer

from django.contrib.staticfiles.handlers import StaticFilesHandler
from django.core.wsgi import get_wsgi_application


class DjangoServer:
    """Servidor Django embebido que escucha en 127.0.0.1 exclusivamente."""

    def __init__(self, host: str = "127.0.0.1", port: int = 0):
        self.host = host
        self.port = port
        self._server: WSGIServer | None = None
        self._thread: threading.Thread | None = None
        self._actual_port: int | None = None

    def start(self) -> int:
        """Inicia el servidor en un hilo daemon. Devuelve el puerto asignado."""
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

        # Aplicación WSGI con soporte para archivos estáticos (modo desarrollo).
        base_application = get_wsgi_application()
        application = StaticFilesHandler(base_application)

        # Puerto 0 deja que el SO elija uno libre.
        self._server = make_server(self.host, self.port, application)
        self._actual_port = self._server.server_address[1]

        self._thread = threading.Thread(target=self._server.serve_forever, daemon=True)
        self._thread.start()
        return self._actual_port

    def stop(self) -> None:
        """Detiene el servidor de forma ordenada."""
        if self._server is not None:
            self._server.shutdown()
            self._server.server_close()

    @property
    def url(self) -> str:
        return f"http://{self.host}:{self._actual_port}/" if self._actual_port else ""
