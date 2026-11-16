"""Ventana principal de la aplicación desktop CodeGuard Pro.

Utiliza PySide6 con QWebEngineView para renderizar la interfaz de Django
dentro de una ventana nativa, sin que el usuario deba abrir un navegador.
"""

import sys

from PySide6.QtCore import QUrl, Qt
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView

from desktop.django_server import DjangoServer


class CodeGuardMainWindow(QMainWindow):
    """Ventana principal de la aplicación desktop."""

    def __init__(self, server_url: str, parent=None):
        super().__init__(parent)
        self.setWindowTitle("CodeGuard Pro — Plataforma Educativa Offline")
        self.setMinimumSize(1200, 800)
        self.resize(1400, 900)

        # Vista web que renderiza la interfaz de Django
        self.web_view = QWebEngineView()
        self.web_view.setUrl(QUrl(server_url))
        self.setCentralWidget(self.web_view)

        # Barra de estado
        self.statusBar().showMessage(f"Servidor local: {server_url}")
        self.statusBar().setStyleSheet("color: #6b7280; font-size: 11px;")

    def closeEvent(self, event):
        """Limpieza al cerrar la ventana."""
        event.accept()


def launch_desktop(server_url: str):
    """Lanza la aplicación desktop con PySide6."""
    app = QApplication(sys.argv)
    app.setApplicationName("CodeGuard Pro")
    app.setOrganizationName("CodeGuard Pro")
    app.setOrganizationDomain("localhost")

    # Estilo de aplicación (fusione para aspecto nativo moderno)
    app.setStyle("Fusion")

    window = CodeGuardMainWindow(server_url)
    window.show()

    sys.exit(app.exec())
