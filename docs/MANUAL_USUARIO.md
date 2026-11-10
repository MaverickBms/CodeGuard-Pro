# CodeGuard Pro — Manual de usuario

**Producto:** CodeGuard Pro  
**Versión:** 1.0 (MVP, primer incremento)  
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

## 2. Primer arranque y configuración inicial

Al iniciar la aplicación por primera vez:

1. Se te pedirá crear un **usuario** y una **contraseña maestra** (mínimo 8 caracteres).
2. Se generará una **frase de rescate** de alta entropía. Esta frase se muestra **una sola
   vez**. Cópiala y guárdala en un lugar seguro.
3. Acepta los términos de uso y el código de ética.
4. Accederás al panel principal.

La frase de rescate se almacena como hash (nunca en texto plano) y es de un solo uso: si la
usas para recuperar el acceso, se invalida.

---

## 3. Inicio de sesión

Ingresa tu usuario y contraseña maestra en la ventana de la aplicación (el servidor local
escucha en `127.0.0.1` en el puerto definido por `CODEGUARD_PORT`, por defecto `8000`).

La sesión expira por inactividad tras el tiempo configurado (15 minutos por defecto). Al
cerrar sesión o al expirar, se registra un evento de auditoría.

**Bloqueo por intentos fallidos (RS-017):** tras 5 intentos fallidos consecutivos, la cuenta
se bloquea durante 15 minutos. El contador se reinicia tras un inicio de sesión exitoso.

El cierre de sesión se hace desde la aplicación con el botón **"Cerrar sesión"** (esquina
superior derecha). Requiere envío POST y mantiene la protección CSRF.

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

## 5. Panel principal

El panel muestra datos reales de la base de datos:

- Tu usuario y estado de la configuración inicial.
- Tiempo de sesión y modo de ejecución.
- Progreso académico: porcentaje de avance, etapas completadas, módulos y lecciones
  completadas.
- Próxima actividad sugerida (etapa o lección para continuar).
- Actividad reciente (últimos progresos registrados).
- Módulos disponibles del MVP (roadmap, competencias, biblioteca, evaluaciones,
  evidencias, laboratorios, administración, vigencia, ética).

En este primer incremento, los módulos académicos están en desarrollo y se desbloquearán en
los siguientes incrementos.

---

## 6. Cambio de contraseña

Desde el menú del usuario (esquina superior derecha) puedes cambiar tu contraseña maestra.
Se requiere la contraseña actual. La nueva contraseña no puede ser idéntica a la actual y
debe superar los validadores de Django (mínimo 8 caracteres, no reutilización, similitud,
etc.). El cambio se registra en auditoría.

---

## 7. Recuperación de acceso (frase de rescate)

Si olvidas tu contraseña, el proceso tiene dos pasos:

**Paso 1 — Validar frase:** ve a `/accounts/rescate/` e ingresa tu frase de rescate. Si es
correcta y no se ha usado antes, avanzas al paso 2. **La frase no se consume al validar.**

**Paso 2 — Establecer nueva contraseña:** en `/accounts/rescate/resetear/` introduces la
frase, la nueva contraseña y su confirmación. Se aplican los validadores de Django y la
nueva contraseña no puede ser idéntica a la actual. Solo al completar exitosamente el cambio,
la frase se invalida y la contraseña se actualiza.

Si el cambio falla en cualquier punto, la frase no se consume y la contraseña no cambia.

---

## 8. Seguridad

- La aplicación solo es accesible desde tu equipo (`127.0.0.1`). Nunca se expone a la red.
- Tu contraseña y frase de rescate están hasheadas con Argon2.
- Las sesiones usan cookies seguras (HttpOnly, SameSite=Lax).
- No se envían datos a servicios externos ni hay telemetría.
- Todos los recursos estáticos (Bootstrap, HTMX) están almacenados localmente.

---

## 9. Copias de seguridad (próximos incrementos)

En futuros incrementos podrás crear y restaurar copias de seguridad en formato `tar.gz` que
incluyan la base de datos y tus archivos, con verificación de integridad mediante hash
SHA-256.

---

## 10. Límites del MVP (incremento 1)

- Las 33 etapas del roadmap ASCENSO se representarán en el incremento 2.
- La importación de PDFs y la biblioteca documental estarán disponibles en el incremento 4.
- Las evaluaciones, competencias, evidencias y laboratorios en incrementos 3 y 5.
- Los backups y la administración en el incremento 6.

Consulta `docs/PLAN_DESARROLLO.md` para el cronograma completo.
