# Código histórico preservado

Este directorio contiene componentes de una arquitectura anterior basada en PySide6/PyInstaller que ya no forma parte del arranque activo.

- `desktop/`: implementación histórica de la ventana y del servidor embebido.
- `CodeGuard.spec`: especificación PyInstaller correspondiente a esa implementación.

La aplicación de escritorio vigente utiliza Electron + Django/Waitress y se empaqueta mediante `CodeGuardServer.spec` y `package.json`.

Estos archivos se conservan para trazabilidad y recuperación histórica. No importarlos desde el código activo ni incluirlos en builds nuevos. Su eliminación definitiva requiere una revisión independiente y autorización.
