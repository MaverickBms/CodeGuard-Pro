# Etapa 5 · Módulo 5.3 — Terminal

**Estado:** borrador académico desarrollado (pendiente validación editorial/técnica y ejecución).  
**Alineación:** ASCENSO 3.1, Etapa 5, Módulo 5.3. **Última actualización:** 2026-11-24

## Identificación
- **Módulo:** 5.3 — Terminal. **Lecciones oficiales:** 7 (5.3.1 a 5.3.7).

## Propósito
Usar la terminal para navegar, manipular archivos y ejecutar tareas de desarrollo.

---

## Lección 5.3.1 — Navegación
- **Oficial:** 5.3.1 — Navegación. **Sec:** 1/7.
- **Propósito:** moverse por el sistema de archivos.
- **Resultados:** usar `pwd`, `ls`, `cd`, rutas relativas/absolutas.
- **Desarrollo:** `pwd` muestra directorio actual, `ls` lista, `cd` cambia. Rutas absolutas empiezan en `/`; relativas dependen del directorio actual. `..` sube un nivel.
- **Práctica:** navega a un proyecto y lista archivos.
- **Independiente:** crea script de comandos para llegar a una ruta.
- **Criterios:** usa rutas correctamente.
- **Errores:** confundir relativa/absoluta.
- **Eval:** ¿Qué hace `cd ..`?
- **Ref:** GNU Coreutils. https://www.gnu.org/software/coreutils/manual/ (2026-11-24).

## Lección 5.3.2 — Manipulación de archivos
- **Oficial:** 5.3.2 — Manipulación de archivos. **Sec:** 2/7.
- **Propósito:** crear, copiar, mover y eliminar archivos/directorios.
- **Resultados:** usar `touch`, `mkdir`, `cp`, `mv`, `rm`.
- **Desarrollo:** `mkdir -p` crea jerarquía; `cp -r` copia directorios; `rm -r` elimina recursivamente (peligroso). Verificar antes de borrar.
- **Práctica:** crea estructura de proyecto con mkdir/touch.
- **Independiente:** copia backup y verifica contenido.
- **Criterios:** comandos correctos, sin borrado accidental.
- **Errores:** `rm -rf` sin verificar; sobrescribir archivos.
- **Eval:** ¿Qué riesgo tiene `rm -rf`?
- **Ref:** GNU Coreutils. https://www.gnu.org/software/coreutils/manual/ (2026-11-24).

## Lección 5.3.3 — Permisos
- **Oficial:** 5.3.3 — Permisos. **Sec:** 3/7.
- **Propósito:** entender permisos de archivos en Linux.
- **Resultados:** leer permisos `rwx`, usar `chmod`, `chown` con criterio.
- **Desarrollo:** permisos para usuario/grupo/otros. `chmod 755` o `chmod u+x`. Principio de menor privilegio. No usar `777` como solución rápida.
- **Práctica:** inspecciona permisos con `ls -l` y modifica uno.
- **Independiente:** explica por qué 777 es riesgoso.
- **Criterios:** interpreta rwx, aplica cambio mínimo.
- **Errores:** `chmod 777`; cambiar propietario sin necesidad.
- **Eval:** ¿Qué significa `rwxr-xr-x`?
- **Ref:** Linux man-pages. *chmod(1)*. https://man7.org/linux/man-pages/man1/chmod.1.html (2026-11-24).

## Lección 5.3.4 — Pipes y redirecciones
- **Oficial:** 5.3.4 — Pipes y redirecciones. **Sec:** 4/7.
- **Propósito:** encadenar comandos y redirigir entrada/salida.
- **Resultados:** usar `|`, `>`, `>>`, `<`, `2>`.
- **Desarrollo:** pipe pasa salida de un comando a otro. `>` sobrescribe, `>>` agrega. `2>` redirige errores. Permite componer herramientas pequeñas.
```bash
cat logs.txt | grep ERROR | wc -l
```
- **Práctica:** filtra líneas con grep y cuenta con wc.
- **Independiente:** guarda errores en archivo separado.
- **Criterios:** pipe correcto, redirección adecuada.
- **Errores:** sobrescribir archivo con `>` accidentalmente.
- **Eval:** ¿Diferencia entre `>` y `>>`?
- **Ref:** GNU Bash Manual. https://www.gnu.org/software/bash/manual/ (2026-11-24).

## Lección 5.3.5 — Scripts básicos
- **Oficial:** 5.3.5 — Scripts básicos. **Sec:** 5/7.
- **Propósito:** automatizar tareas con scripts shell.
- **Resultados:** crear script bash, shebang, permisos de ejecución, variables.
- **Desarrollo:** script empieza con `#!/bin/bash`. Dar permisos `chmod +x`. Usar variables, comillas, y `set -euo pipefail` con criterio para mayor robustez.
```bash
#!/bin/bash
set -euo pipefail
echo "Hola $USER"
```
- **Práctica:** crea script que cree estructura de directorios.
- **Independiente:** script que reciba argumento y lo valide.
- **Criterios:** script ejecutable, maneja argumentos.
- **Errores:** no citar variables; ignorar códigos de salida.
- **Eval:** ¿Qué hace el shebang?
- **Ref:** GNU Bash Manual. https://www.gnu.org/software/bash/manual/ (2026-11-24).

## Lección 5.3.6 — Variables de entorno
- **Oficial:** 5.3.6 — Variables de entorno. **Sec:** 6/7.
- **Propósito:** configurar comportamiento de programas mediante entorno.
- **Resultados:** leer/definir/exportar variables, usar `.env` con cuidado.
- **Desarrollo:** variables de entorno configuran procesos. `export VAR=valor`, `echo $VAR`. Secretos no deben commitearse; usar `.env` ignorado por git o gestores de secretos.
- **Práctica:** define variable y úsala en script.
- **Independiente:** configura variable de entorno para entorno dev/test.
- **Criterios:** no expone secretos, usa export correctamente.
- **Errores:** commitear `.env`; hardcodear secretos.
- **Eval:** ¿Diferencia entre variable shell y variable de entorno?
- **Ref:** GNU Bash Manual. https://www.gnu.org/software/bash/manual/ (2026-11-24).

## Lección 5.3.7 — Procesos
- **Oficial:** 5.3.7 — Procesos. **Sec:** 7/7.
- **Propósito:** inspeccionar y gestionar procesos.
- **Resultados:** usar `ps`, `top/htop`, `kill`, `&`, jobs.
- **Desarrollo:** proceso es programa en ejecución. `ps aux` lista, `top` monitorea, `kill PID` envía señal (SIGTERM preferible antes de SIGKILL). `command &` ejecuta en background.
- **Práctica:** lista procesos y encuentra uno por nombre.
- **Independiente:** ejecuta proceso en background y finalízalo con gracia.
- **Criterios:** usa SIGTERM antes de SIGKILL.
- **Errores:** `kill -9` como primer recurso; matar proceso equivocado.
- **Eval:** ¿Qué diferencia hay entre SIGTERM y SIGKILL?
- **Ref:** Linux man-pages. *kill(1)*. https://man7.org/linux/man-pages/man1/kill.1.html (2026-11-24).