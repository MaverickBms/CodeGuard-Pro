# CodeGuard Pro — Manual de usuario

**Producto:** CodeGuard Pro  
**Versión:** 1.0 (MVP, primer incremento)  
**SRS de referencia:** `IEEE830(1).md` v2.0

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

Ingresa tu usuario y contraseña maestra en `http://127.0.0.1:8000/accounts/login/`.

La sesión expira por inactividad tras el tiempo configurado (15 minutos por defecto). Al
cerrar sesión o al expirar, se registra un evento de auditoría.

---

## 4. Panel principal

El panel muestra:
- Tu usuario y estado de la configuración inicial.
- Los módulos disponibles del MVP (roadmap, competencias, biblioteca, evaluaciones,
  evidencias, laboratorios, administración, vigencia, ética).
- Tiempo de sesión y modo de ejecución.

En este primer incremento, los módulos académicos están en desarrollo y se desbloquearán en
los siguientes incrementos.

---

## 5. Cambio de contraseña

Desde el menú del usuario (esquina superior derecha) puedes cambiar tu contraseña maestra.
Se requiere la contraseña actual. El cambio se registra en auditoría.

---

## 6. Frase de rescate (recuperación de acceso)

Si olvidas tu contraseña, ve a `/accounts/rescate/` e ingresa tu frase de rescate. Si es
correcta y no se ha usado antes, recuperarás el acceso. La frase se invalida tras usarse.

---

## 7. Seguridad

- La aplicación solo es accesible desde tu equipo (`127.0.0.1`). Nunca se expone a la red.
- Tu contraseña y frase de rescate están hasheadas con Argon2.
- Las sesiones usan cookies seguras (HttpOnly, SameSite=Lax).
- No se envían datos a servicios externos ni hay telemetría.
- Todos los recursos estáticos (Bootstrap, HTMX) están almacenados localmente.

---

## 8. Copias de seguridad (próximos incrementos)

En futuros incrementos podrás crear y restaurar copias de seguridad en formato `tar.gz` que
incluyan la base de datos y tus archivos, con verificación de integridad mediante hash
SHA-256.

---

## 9. Límites del MVP (incremento 1)

- Las 33 etapas del roadmap ASCENSO se representarán en el incremento 2.
- La importación de PDFs y la biblioteca documental estarán disponibles en el incremento 4.
- Las evaluaciones, competencias, evidencias y laboratorios en incrementos 3 y 5.
- Los backups y la administración en el incremento 6.

Consulta `docs/PLAN_DESARROLLO.md` para el cronograma completo.
