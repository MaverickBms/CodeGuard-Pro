# CodeGuard Pro — Manual de usuario

**Producto:** CodeGuard Pro  
**Versión:** 2.0 (Incremento 1 + Fase 2 parcialmente implementada)  
**SRS de referencia:** `IEEE830(1).md` v2.0

> **Nota:** El sistema de autenticación está temporalmente desactivado
> (`AUTH_DISABLED = True`). La aplicación se abre directamente en el panel principal
> sin solicitar usuario ni contraseña. Los flujos de login, registro, rescate,
> restablecimiento y cierre de sesión se conservan íntegros y pueden reactivarse con
> autorización expresa del propietario del proyecto. Ver `docs/MODO_SIN_AUTENTICACION.md`.

---

## 1. ¿Qué es CodeGuard Pro?

CodeGuard Pro es una plataforma educativa personal, monousuario, local y offline-first. Te
permite organizar tu formación técnica, gestionar el roadmap ASCENSO, administrar una
biblioteca de documentos PDF, construir una base de conocimiento, realizar evaluaciones,
desarrollar ejercicios y proyectos, ejecutar laboratorios guiados, registrar evidencias y
generar copias de seguridad.

No requiere conexión a Internet para sus funcionalidades esenciales.

---

## 2. Primer arranque y apertura de la aplicación

Al iniciar la aplicación por primera vez:

1. Se abre directamente el **panel principal** (autenticación temporalmente desactivada).
2. Si el roadmap ASCENSO aún no está cargado, ejecuta:
   ```bash
   python manage.py cargar_ascenso
   ```
3. Accederás al panel principal con el resumen de progreso, próximas actividades y módulos
   disponibles.

No se solicita usuario ni contraseña mientras la autenticación esté desactivada.

---

## 3. Panel principal

El panel muestra datos reales de la base de datos:

- Tu usuario y estado de la configuración inicial.
- Tiempo de sesión y modo de ejecución.
- Progreso académico: porcentaje de avance, etapas completadas, módulos y lecciones
  completadas.
- Próxima actividad sugerida (etapa o lección para continuar).
- Actividad reciente (últimos progresos registrados).
- Módulos disponibles del MVP (roadmap, competencias, biblioteca, evaluaciones,
  evidencias, laboratorios, administración, vigencia, ética).

En este incremento, los módulos académicos están en desarrollo y se desbloquearán en
los siguientes incrementos.

---

## 4. Temas visuales

CodeGuard Pro incluye 12 temas con las 12 paletas oficiales (P01–P12). Cada tema conserva
exactamente sus códigos HEX originales y se asigna a roles semánticos según su luminancia
para garantizar accesibilidad:

- Claro Diurno → P01 Coral y vino
- Oscuro Nocturno → P02 Ciruela y malva
- Alto Contraste → P04 Monocromática
- Retro Pixel → P05 Rosa y frambuesa
- Cyberpunk → P03 Violeta eléctrico
- Reino Fantasía → P07 Rosa empolvado
- Ciencia Ficción → P08 Pizarra
- Guerrero → P06 Fuego y naranja
- Mago → P09 Violeta y dorado
- Pícaro → P10 Verde petróleo
- Paladín → P11 Azul y turquesa
- Oscuro Mago → P12 Tierra y madera

Para cambiar el tema:

1. Haz clic en el botón **Tema** (icono de paleta) en la parte superior derecha de la ventana.
2. Se desplegará un panel con las 12 opciones disponibles.
3. Selecciona el tema deseado. Se aplica inmediatamente y se recuerda para la próxima sesión.

El tema también se puede cambiar desde el menú de Electron → **Ver → Tema**.

Todos los temas cumplen **WCAG AA (4.5:1)** para texto normal y **3:1** para componentes
gráficos. Se respeta `prefers-reduced-motion` y no se usa `transition: all`.

---

## 5. Roadmap ASCENSO

El roadmap ASCENSO 3.1 incluye las **33 etapas oficiales** (0 a 32) con filtros (bloque,
prioridad, búsqueda), detalle de etapa (módulos, lecciones, proyecto, criterios,
prerrequisitos) y marcado de lecciones y etapas completas con recalculo automático de
porcentaje.

Para cargar o actualizar el roadmap:

```bash
python manage.py cargar_ascenso
```

---

## 6. Contenido académico y flujo editorial (Fase 2)

Cada lección puede contar con contenido académico estructurado:

- **Teoría técnica** y **explicación sencilla**.
- **Objetivos de aprendizaje** y notas.
- **Ejemplos guiados** con código, lenguaje y salida esperada.
- **Ejercicios** con enunciado, instrucciones, nivel, código inicial y pistas.

El flujo editorial permite crear snapshots versionados de una lección, enviarlos a revisión,
aprobarlos, publicarlos, sustituirlos o retirarlos. Las operaciones se ejecutan mediante
comandos de gestión (no hay panel de administración):

| Comando | Propósito |
|---|---|
| `crear_version_leccion --leccion <id>` | Genera un snapshot versionado borrador de una lección |
| `gestionar_version_leccion enviar-revision --version-id <id> --usuario <editor>` | Envía una versión a revisión |
| `gestionar_version_leccion aprobar --version-id <id> --usuario <revisor>` | Aprueba una versión en revisión |
| `gestionar_version_leccion publicar --version-id <id> --usuario <publicador>` | Publica una versión aprobada |
| `gestionar_version_leccion retirar --version-id <id> --usuario <revisor> --motivo <texto>` | Retira una versión publicada (exige motivo) |
| `registrar_fuente_conocimiento --publicador <org> --titulo <título> --url <https://...>` | Registra una fuente documental |
| `revisar_licencia_fuente --fuente-id <id> --usuario <editor> --estado <estado>` | Registra una decisión editorial de licencia |
| `importar_paquete_contenido --directorio <ruta> --confirmar --usuario <editor>` | Importa un lote validado como borradores |
| `validar_paquete_contenido --directorio <ruta>` | Valida documentos académicos sin escribir datos |

Una versión publicada es inmutable: no se edita, se crea una nueva versión. Solo puede haber
una versión publicada por lección.

---

## 7. Cambio de contraseña

Cuando la autenticación está reactivada (`AUTH_DISABLED = False`), desde el menú del usuario
(esquina superior derecha) puedes cambiar tu contraseña maestra. Se requiere la contraseña
actual. La nueva contraseña no puede ser idéntica a la actual y debe superar los validadores
de Django (mínimo 8 caracteres, no reutilización, similitud, etc.). El cambio se registra en
auditoría.

---

## 8. Recuperación de acceso (frase de rescate)

Si olvidas tu contraseña (autenticación reactivada), el proceso tiene dos pasos:

**Paso 1 — Validar frase:** ve a `/accounts/rescate/` e ingresa tu frase de rescate. Si es
correcta y no se ha usado antes, avanzas al paso 2. **La frase no se consume al validar.**

**Paso 2 — Establecer nueva contraseña:** en `/accounts/rescate/resetear/` introduces la
frase, la nueva contraseña y su confirmación. Se aplican los validadores de Django y la
nueva contraseña no puede ser idéntica a la actual. Solo al completar exitosamente el cambio,
la frase se invalida y la contraseña se actualiza.

Si el cambio falla en cualquier punto, la frase no se consume y la contraseña no cambia.

---

## 9. Seguridad

- La aplicación solo es accesible desde tu equipo (`127.0.0.1`). Nunca se expone a la red.
- Tu contraseña y frase de rescate están hasheadas con Argon2.
- Las sesiones usan cookies seguras (HttpOnly, SameSite=Lax).
- No se envían datos a servicios externos ni hay telemetría.
- Todos los recursos estáticos (Bootstrap, HTMX) están almacenados localmente.

---

## 10. Copias de seguridad (próximos incrementos)

En futuros incrementos podrás crear y restaurar copias de seguridad en formato `tar.gz` que
incluyan la base de datos y tus archivos, con verificación de integridad mediante hash
SHA-256.

---

## 11. Límites del MVP (incremento 1)

- Las 33 etapas del roadmap ASCENSO se representan en el incremento 2 (ya implementado en la
  rama de trabajo).
- La importación de PDFs y la biblioteca documental estarán disponibles en el incremento 4.
- Las evaluaciones, competencias, evidencias y laboratorios en incrementos 3 y 5.
- Los backups y la administración en el incremento 6.

Consulta `docs/PLAN_DESARROLLO.md` para el cronograma completo.