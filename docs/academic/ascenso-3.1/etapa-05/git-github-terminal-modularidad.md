# Etapa 5 — Git, GitHub, terminal y modularidad

**Estado de trabajo:** BASE DE TRABAJO ACTIVA · v0.1.0.  
**Alineación:** ASCENSO 3.1, Etapa 5.  
**Prioridad:** P1 · Obligatoria.  
**Objetivo oficial:** comenzar a trabajar como un desarrollador que forma parte de un equipo.

## Temario oficial

- **5.1 Git:** repositorios, working directory, staging area, commits, branches, merge, rebase, clone, pull, push, fetch, diff, log, stash, reset, revert y cherry-pick.
- **5.2 GitHub:** repositorios públicos y privados, README, Issues, Pull Requests, forks, releases, GitHub Projects, Code Review y branch protection.
- **5.3 Terminal:** shell, comandos, rutas absolutas y relativas, PATH, variables de entorno, redirecciones y pipes.
- **5.4 Modularidad:** módulos, imports, exports, namespaces, paquetes, dependencias, gestores de paquetes, versionado semántico y archivos de bloqueo de dependencias.

**Proyecto oficial:** convertir uno de tus proyectos anteriores en un repositorio organizado, modular y documentado.

## Resultados de aprendizaje

Podrás explicar el flujo de cambios de Git, crear ramas y commits comprensibles, sincronizar repositorios con seguridad, resolver conflictos, colaborar mediante GitHub, documentar y revisar cambios, utilizar la terminal para navegar y automatizar tareas y dividir un programa en módulos con dependencias controladas.

## 5.1 — Git

### 5.1.1 — Repositorios

Git es un sistema de control de versiones distribuido. Un repositorio conserva objetos y referencias que permiten reconstruir la historia del proyecto.

### 5.1.2 — Working directory

El working directory es el directorio de trabajo que contiene los archivos del proyecto. Aquí editas y creas archivos antes de preparar cambios.

### 5.1.3 — Staging area

La staging area (índice) es la selección de cambios que formarán el próximo commit. El comando `git status` permite conocer el estado actual. Ejecutarlo con frecuencia evita confundir archivos modificados, preparados o sin seguimiento.

### 5.1.4 — Commits

Un commit registra un conjunto de cambios con autoría, fecha, mensaje y referencia al estado anterior. Un commit debe representar una unidad lógica coherente.

Buenas prácticas:
- mensajes claros que expliquen el propósito;
- cambios pequeños y revisables;
- no incluir archivos generados, secretos o datos personales;
- revisar el diff antes de confirmar;
- no utilizar un commit como sustituto de pruebas.

Flujo básico:

```bash
git status
git diff
git add src/
git diff --staged
git commit -m "feat: agregar consulta de productos"
```

Revisa las rutas antes de ejecutar `git add`; evita `git add .` a ciegas en proyectos con archivos sensibles o generados.

### 5.1.5 — Branches

Una rama es una referencia móvil a un commit. Permite desarrollar una funcionalidad o corrección sin alterar directamente la línea principal.

```bash
git switch -c feature/consulta-productos
# editar y probar
git status
git add src/
git commit -m "feat: implementar consulta de productos"
```

Las ramas deben tener propósito y alcance definidos. No mantengas ramas abandonadas indefinidamente.

### 5.1.8 — Clone

`clone` crea una copia local inicial de un repositorio remoto.

### 5.1.11 — Fetch

`fetch` descarga referencias y objetos remotos sin integrar automáticamente los cambios en tu rama actual.

### 5.1.9 — Pull

`pull` obtiene cambios y los integra según la configuración (frecuentemente fetch + merge o rebase).

### 5.1.10 — Push

`push` publica commits locales en un remoto.

Antes de hacer push, verifica remoto, rama y contenido. Nunca publiques secretos, credenciales, archivos de entorno o datos privados.

### 5.1.6 — Merge

**Merge** integra historias y puede crear un commit de merge. Conserva la estructura de ambas líneas de desarrollo.

### 5.1.7 — Rebase

**Rebase** reaplica commits sobre una base diferente y cambia sus identificadores. Puede producir una historia lineal, pero reescribe commits.

Regla de colaboración: evita reescribir historia compartida sin coordinación. No hagas rebase de una rama que otras personas estén usando salvo que exista un acuerdo claro.

### 5.1.12 — Diff

`git diff` muestra diferencias entre estados. Revisa los cambios antes de integrarlos y utiliza opciones para limitar archivos o commits cuando el diff sea grande.

```bash
git diff
git diff --staged
```

### 5.1.13 — Log

`git log` permite recorrer la historia del repositorio.

```bash
git log --oneline --decorate --graph -15
git show --stat HEAD
```

### 5.1.14 — Stash

`git stash` guarda temporalmente cambios locales para permitir cambiar de contexto. No es una copia de seguridad ni sustituye commits.

```bash
git stash push -m "trabajo temporal en formulario"
git stash list
git stash apply
```

Comprueba el estado después de aplicar el stash: pueden aparecer conflictos. No borres un stash hasta confirmar que los cambios están recuperados.

### 5.1.15 — Reset

`reset` mueve una referencia de rama y puede cambiar el índice/directorio de trabajo según el modo. `--hard` descarta cambios y puede provocar pérdida de trabajo.

### 5.1.16 — Revert

`revert` crea un nuevo commit que revierte los cambios de otro commit; suele ser más seguro para historia compartida.

### 5.1.17 — Cherry-pick

`cherry-pick` aplica los cambios introducidos por commits seleccionados sobre la rama actual; puede generar conflictos y nuevos commits.

**Regla de seguridad:** no ejecutes `git reset --hard`, `git clean -fd`, force-push ni eliminación de ramas sobre trabajo real sin revisar estado, destino y recuperación. Practica primero en un repositorio desechable.

## 5.2 — GitHub

### 5.2.1 — Repositorios públicos y privados

Un repositorio público permite que otras personas consulten su contenido según las condiciones de la plataforma y licencia. Uno privado restringe acceso a colaboradores autorizados, pero no convierte en seguro un secreto que se haya comprometido.

Nunca subas contraseñas, tokens, claves privadas, certificados sensibles, datos personales ni archivos de configuración local. Si un secreto se publica por error, eliminar el archivo no basta: debe revocarse/rotarse y evaluarse la exposición del historial.

### 5.2.2 — README

El README debe explicar:
- propósito y alcance;
- requisitos;
- instalación y ejecución;
- configuración sin secretos;
- uso básico;
- pruebas;
- estructura del proyecto;
- limitaciones;
- licencia y contribución, cuando corresponda.

Debe reflejar el estado real. No anuncies características que no estén implementadas y verificadas.

### 5.2.3 — Issues

Los Issues permiten registrar errores, tareas, propuestas y preguntas. Un buen issue incluye contexto, pasos reproducibles, resultado esperado/real, entorno, criterios de aceptación y evidencias sin datos sensibles.

### 5.2.4 — Pull Requests

Un Pull Request propone integrar cambios entre ramas. Debe explicar:
- problema que resuelve;
- alcance;
- decisiones técnicas;
- pruebas ejecutadas y resultado real;
- capturas o evidencias si aportan valor;
- riesgos y tareas pendientes.

Un PR no demuestra por sí solo que el cambio sea correcto. Requiere revisión, pruebas y controles del repositorio.

### 5.2.5 — Forks

Un fork es una copia de un repositorio bajo otro espacio de usuario u organización. Facilita contribuir cuando no se tiene permiso de escritura en el original. Debes respetar licencias, atribución y políticas de seguridad.

### 5.2.6 — Releases

Un release identifica una entrega concreta, normalmente asociada a un tag, notas y artefactos. No publiques releases por cada commit. Verifica versión, cambios, artefactos, integridad, documentación y limitaciones antes de distribuir.

### 5.2.7 — GitHub Projects

Permite organizar trabajo en vistas y campos. Las tareas deben tener responsable, prioridad, estado y criterios de finalización claros. Un tablero ordenado no sustituye la verificación técnica.

### 5.2.8 — Code Review

La revisión de código busca defectos, riesgos, falta de claridad, deuda técnica y oportunidades de mejora. Los comentarios deben ser específicos, respetuosos y accionables.

Revisa especialmente:
- comportamiento y casos límite;
- seguridad y privacidad;
- errores y manejo de excepciones;
- pruebas;
- rendimiento cuando sea relevante;
- legibilidad y consistencia;
- compatibilidad y migraciones.

### 5.2.9 — Branch protection

Las reglas de protección pueden exigir revisiones, checks, firmas, historial lineal u otras condiciones antes de integrar cambios. La configuración disponible depende del plan y del repositorio.

No desactives controles para hacer que un PR pase. Si una regla bloquea una integración legítima, documenta la causa y solicita el cambio por el proceso autorizado.

## 5.3 — Terminal

### 5.3.1 — Shell

La terminal es una interfaz de texto para ejecutar comandos. La shell interpreta órdenes y permite combinarlas. Bash, Zsh y PowerShell comparten conceptos, pero no siempre sintaxis ni comandos.

### 5.3.2 — Comandos

Comandos básicos en Bash:

```bash
pwd
ls -la
cd proyecto
mkdir documentos
cp origen.txt copia.txt
mv antiguo.txt nuevo.txt
cat README.md
```

Equivalentes de PowerShell pueden tener nombres y parámetros diferentes. Consulta la ayuda de la shell activa en lugar de asumir compatibilidad exacta.

### 5.3.3 — Rutas absolutas y relativas

Una ruta absoluta identifica una ubicación desde la raíz o unidad. Una ruta relativa se interpreta desde el directorio actual o desde una base definida.

- `.`: directorio actual.
- `..`: directorio padre.
- `~/proyecto`: ruta bajo el directorio personal en shells compatibles.

Antes de borrar, copiar o sobrescribir, muestra el directorio actual y verifica la ruta completa. Una ruta relativa puede apuntar a un lugar distinto si cambia el directorio de trabajo.

### 5.3.4 — PATH

`PATH` es una variable de entorno que contiene directorios donde la shell busca ejecutables. Si un comando no se reconoce, puede faltar la instalación o la ruta.

No agregues directorios desconocidos al PATH ni ejecutes binarios descargados sin verificar origen e integridad.

### 5.3.5 — Variables de entorno

Permiten configurar procesos sin incrustar valores en el código. Pueden contener rutas, opciones y credenciales; por eso nunca deben imprimirse indiscriminadamente ni registrarse en logs.

Bash:
```bash
export APP_MODE=development
printf '%s\n' "$APP_MODE"
```

PowerShell:
```powershell
$env:APP_MODE = "development"
$env:APP_MODE
```

Los cambios de entorno normalmente afectan al proceso actual y a los procesos hijos, no modifican mágicamente toda la configuración del sistema.

### 5.3.6 — Redirecciones

- `>` redirige salida y normalmente sobrescribe el archivo.
- `>>` añade salida al final.
- `2>` redirige errores estándar.

Ejemplo:
```bash
printf '%s\\n' "uno" "dos" "tres" > lista.txt
```

No redirijas salidas sobre archivos importantes sin verificar el destino.

### 5.3.7 — Pipes

El operador `|` conecta la salida de un comando con la entrada del siguiente.

```bash
grep "dos" lista.txt
cat lista.txt | grep "tres"
```

En shell, las comillas y la expansión de comodines pueden cambiar qué archivos recibe un comando.

## 5.4 — Modularidad

### 5.4.1 — Módulos

Un módulo agrupa código con una responsabilidad o API definida. En Java, el sistema de módulos (JPMS) puede declarar qué paquetes se exportan; en JavaScript, los módulos ECMAScript agrupan funcionalidad.

### 5.4.2 — Imports

Los imports permiten utilizar elementos expuestos por otros módulos. La sintaxis y resolución dependen del lenguaje y del sistema de módulos.

### 5.4.3 — Exports

Los exports declaran qué elementos de un módulo pueden consumir otros módulos. Expón solo la API necesaria y evita acoplar consumidores a detalles internos.

### 5.4.4 — Namespaces

Los namespaces reducen colisiones de nombres y organizan símbolos. Su sintaxis y alcance dependen del lenguaje.

### 5.4.5 — Paquetes

En Java se utilizan paquetes para organizar clases y controlar nombres. Otros lenguajes ofrecen espacios de nombres o módulos con reglas diferentes.

Una estructura clara refleja el dominio y las responsabilidades, no una jerarquía excesivamente profunda.

### 5.4.6 — Dependencias

Una dependencia es un componente externo o interno que un módulo necesita. Antes de incorporarla, evalúa:
- mantenimiento y actividad;
- licencia;
- vulnerabilidades conocidas;
- tamaño y dependencias transitivas;
- compatibilidad;
- necesidad real;
- política de actualización.

Evita añadir paquetes por una tarea que el lenguaje ya resuelve de forma sencilla.

### 5.4.7 — Gestores de paquetes

Automatizan descarga, resolución y configuración de dependencias. Ejemplos:
- Java: Maven o Gradle;
- JavaScript: npm, pnpm o Yarn;
- Python: pip y herramientas de gestión de entornos.

El gestor y su archivo de configuración deben corresponder al proyecto. No mezcles gestores sin una razón documentada.

### 5.4.8 — Versionado semántico

SemVer utiliza la forma MAJOR.MINOR.PATCH:
- MAJOR: cambios incompatibles en la API pública;
- MINOR: funcionalidad compatible;
- PATCH: correcciones compatibles.

El significado depende de que el proyecto declare una API pública y siga la convención. Un número de versión por sí solo no demuestra compatibilidad.

### 5.4.9 — Archivos de bloqueo de dependencias

Los lockfiles registran versiones resueltas y, según el gestor, integridad y dependencias transitivas. Permiten instalaciones reproducibles dentro de las condiciones declaradas.

No borres ni regeneres un lockfile para «arreglar» una instalación sin entender el cambio. En proyectos de aplicación suele versionarse el lockfile según las recomendaciones del gestor y el equipo.

## Laboratorio — Git y terminal en un proyecto propio

1. Selecciona un proyecto de las etapas anteriores.
2. Revisa que no contenga secretos ni datos privados.
3. Inicializa o clona un repositorio y define una estructura clara.
4. Crea un README que describa el estado real.
5. Divide el trabajo en una rama de funcionalidad.
6. Realiza cambios pequeños y revisa `git diff`.
7. Crea commits con mensajes descriptivos.
8. Sincroniza con un remoto privado o público según la sensibilidad del proyecto.
9. Abre un Pull Request de práctica y solicita revisión.
10. Organiza tareas en Issues o Projects.
11. Separa el código en módulos con imports/exports o paquetes coherentes.
12. Declara dependencias y conserva el archivo de bloqueo cuando corresponda.

**No uses un repositorio público para código con secretos, información personal o datos del centro de estudios.** Si el proyecto no debe compartirse, usa un repositorio privado o una práctica local.

### Entregables

- URL del repositorio o evidencia local redactada;
- README;
- árbol de directorios;
- historial de commits;
- rama de trabajo y PR de práctica;
- lista de Issues y criterios de aceptación;
- evidencia de revisión de código;
- mapa de módulos y dependencias;
- registro de comandos utilizados;
- reflexión sobre decisiones de privacidad y licencia.

### Rúbrica (100 puntos)

| Criterio | Puntos |
|---|---:|
| Uso de Git y estados | 20 |
| Ramas e integración segura | 15 |
| README, Issues y Pull Request | 15 |
| Code Review y protección | 10 |
| Uso de terminal | 15 |
| Modularidad y dependencias | 15 |
| Privacidad, trazabilidad y calidad | 10 |

## Ejercicios y respuestas orientativas

1. ¿Qué diferencia hay entre working directory, staging area y repository?  
   **Respuesta:** cambios de trabajo, selección para el siguiente commit e historial/objetos versionados.

2. ¿Qué diferencia existe entre fetch y pull?  
   **Respuesta:** fetch descarga referencias/objetos; pull además integra cambios en la rama actual según configuración.

3. ¿Cuándo es preferible revert a reset en una rama compartida?  
   **Respuesta:** revert crea un commit inverso y conserva el historial publicado; reset mueve la referencia y puede reescribir historia.

4. ¿Qué riesgo tiene rebase en commits ya compartidos?  
   **Respuesta:** cambia identificadores y puede obligar a otros colaboradores a reconciliar historias divergentes.

5. ¿Qué debe incluir un Pull Request de calidad?  
   **Respuesta:** contexto, alcance, decisiones, pruebas reales, riesgos y criterios de revisión.

6. ¿Qué diferencia hay entre redirección y pipe?  
   **Respuesta:** redirección envía una salida a un archivo o descriptor; pipe conecta procesos.

7. ¿Qué problema resuelve PATH?  
   **Respuesta:** permite localizar ejecutables en directorios configurados.

8. ¿Por qué se conserva un lockfile?  
   **Respuesta:** para fijar la resolución de dependencias y hacer instalaciones más reproducibles.

9. ¿Qué significa un cambio MINOR en SemVer?  
   **Respuesta:** añade funcionalidad compatible con la API pública declarada.

10. ¿Por qué un repositorio privado no justifica almacenar contraseñas sin protección?  
    **Respuesta:** el acceso puede ampliarse, filtrarse o comprometerse; los secretos deben gestionarse fuera del historial y rotarse si se exponen.

## Autoevaluación

Realiza el laboratorio sin copiar comandos a ciegas. Antes de cada comando explica qué cambia y qué podría perderse. Debes poder recuperar el estado del repositorio, explicar el diff y demostrar que el remoto y la rama de destino son los correctos.

## Recursos audiovisuales

No se incluye video en esta versión: no se ha validado una pieza concreta con audio hablado en español que cubra de forma fiel Git, GitHub, terminal y modularidad como un conjunto. Los videos de cada herramienta se curarán por subtema y versión, evitando recomendar cursos sin comprobar su contenido.

## Referencias

- Git, **Documentation**: https://git-scm.com/doc
- GitHub Docs, **Repositories**: https://docs.github.com/en/repositories
- GitHub Docs, **About pull requests**: https://docs.github.com/en/pull-requests
- GitHub Docs, **About protected branches**: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- GNU Bash Manual: https://www.gnu.org/software/bash/manual/
- Microsoft Learn, **PowerShell Documentation**: https://learn.microsoft.com/en-us/powershell/
- Semantic Versioning 2.0.0: https://semver.org/
- npm Docs, **package-lock.json**: https://docs.npmjs.com/cli/configuring-npm/package-lock-json
- Apache Maven, **Introduction to the Dependency Mechanism**: https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html

**Consulta de fuentes:** 2026-11-19.  
**Verificación práctica:** comandos y laboratorio propuestos; no ejecutados en un entorno de terminal real.  
**Estado editorial:** en desarrollo; no aprobado ni publicado..
