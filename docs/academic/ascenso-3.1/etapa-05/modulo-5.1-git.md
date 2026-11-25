# Etapa 5 · Módulo 5.1 — Git

**Estado:** borrador académico desarrollado (pendiente validación editorial/técnica y ejecución).  
**Alineación:** ASCENSO 3.1, Etapa 5, Módulo 5.1. **Última actualización:** 2026-11-24

## Identificación
- **Etapa:** 5 — Git, GitHub, terminal y modularidad. **Objetivo oficial:** dominar el control de versiones y la terminal.
- **Módulo:** 5.1 — Git. **Lecciones oficiales:** 17 (5.1.1 a 5.1.17).

## Propósito
Usar Git para controlar cambios, colaborar y mantener historial confiable.

---

## Lección 5.1.1 — Inicialización
- **Oficial:** 5.1.1 — Inicialización. **Sec:** 1/17.
- **Propósito:** crear un repositorio Git.
- **Resultados:** ejecutar `git init`, entender `.git`, configurar identidad.
- **Desarrollo:** `git init` crea un repositorio en el directorio actual. Configurar `user.name` y `user.email`. No inicializar repos anidados sin intención.
```bash
git init
git config user.name "Nombre"
git config user.email "correo@ejemplo.com"
```
- **Práctica:** inicializa repo y verifica `.git`.
- **Independiente:** configura global vs local y explica diferencia.
- **Criterios:** repo creado, identidad configurada.
- **Errores:** init en directorio equivocado; credenciales incorrectas.
- **Eval:** ¿Qué crea `git init`?
- **Ref:** Git Docs. *git-init*. https://git-scm.com/docs/git-init (2026-11-24).

## Lección 5.1.2 — Staging
- **Oficial:** 5.1.2 — Staging. **Sec:** 2/17.
- **Propósito:** preparar cambios para commit.
- **Resultados:** usar `git add`, `git status`, entender staging area.
- **Desarrollo:** staging area permite seleccionar qué cambios entran al commit. `git add archivo`, `git add -p` para parcial. Revisar con `git status` y `git diff --staged`.
- **Práctica:** modifica 2 archivos, stage solo uno.
- **Independiente:** usa `git add -p` para seleccionar hunks.
- **Criterios:** stage selectivo correcto.
- **Errores:** `git add .` sin revisar; incluir secretos.
- **Eval:** ¿Qué es el staging area?
- **Ref:** Git Docs. *git-add*. https://git-scm.com/docs/git-add (2026-11-24).

## Lección 5.1.3 — Commits
- **Oficial:** 5.1.3 — Commits. **Sec:** 3/17.
- **Propósito:** registrar cambios con mensaje significativo.
- **Resultados:** crear commits atómicos, escribir buenos mensajes.
- **Desarrollo:** un commit es una instantánea con metadatos. Debe ser atómico y tener mensaje claro. Convención: imperativo, qué y por qué.
```bash
git commit -m "feat: agregar validación de email"
```
- **Práctica:** crea 2 commits atómicos.
- **Independiente:** reescribe un mensaje malo a uno claro.
- **Criterios:** commit atómico, mensaje descriptivo.
- **Errores:** commits gigantes; mensajes “fix”, “update”.
- **Eval:** ¿Qué hace un buen mensaje de commit?
- **Ref:** Git Docs. *git-commit*. https://git-scm.com/docs/git-commit (2026-11-24).

## Lección 5.1.4 — Ramas
- **Oficial:** 5.1.4 — Ramas. **Sec:** 4/17.
- **Propósito:** trabajar en líneas independientes de desarrollo.
- **Resultados:** crear, listar, cambiar y eliminar ramas.
- **Desarrollo:** ramas permiten aislar trabajo. `git branch`, `git switch -c`, `git switch`. Nombrar con convención: `feature/`, `fix/`, `docs/`.
- **Práctica:** crea rama feature, haz commit, vuelve a main.
- **Independiente:** simula flujo con 2 ramas paralelas.
- **Criterios:** ramas con nombres claros, cambios aislados.
- **Errores:** trabajar todo en main; nombres ambiguos.
- **Eval:** ¿Para qué sirve una rama?
- **Ref:** Git Docs. *git-branch*. https://git-scm.com/docs/git-branch (2026-11-24).

## Lección 5.1.5 — Merge
- **Oficial:** 5.1.5 — Merge. **Sec:** 5/17.
- **Propósito:** integrar cambios de una rama en otra.
- **Resultados:** hacer merge, entender fast-forward y merge commit.
- **Desarrollo:** `git merge` integra historial. Fast-forward mueve puntero si no hay divergencia; merge commit crea nodo de unión. Elegir según política del equipo.
- **Práctica:** merge de feature a main.
- **Independiente:** crea caso de fast-forward y uno de merge commit.
- **Criterios:** merge correcto, historial entendido.
- **Errores:** merge sin revisar; perder contexto.
- **Eval:** ¿Qué es fast-forward?
- **Ref:** Git Docs. *git-merge*. https://git-scm.com/docs/git-merge (2026-11-24).

## Lección 5.1.6 — Rebase
- **Oficial:** 5.1.6 — Rebase. **Sec:** 6/17.
- **Propósito:** re-aplicar commits sobre otra base.
- **Resultados:** usar rebase, entender diferencia con merge, riesgos.
- **Desarrollo:** rebase reescribe historial aplicando commits sobre otra base. Útil para historial lineal. **No rebasear ramas públicas compartidas** sin coordinación: reescribe hashes.
```bash
git fetch origin
git rebase origin/main
```
- **Práctica:** rebase de rama feature sobre main actualizada.
- **Independiente:** compara historial con merge vs rebase.
- **Criterios:** entiende reescritura de historial.
- **Errores:** rebase en rama compartida; perder commits por resolver mal.
- **Eval:** ¿Cuándo no usar rebase?
- **Ref:** Git Docs. *git-rebase*. https://git-scm.com/docs/git-rebase (2026-11-24).

## Lección 5.1.7 — Conflictos
- **Oficial:** 5.1.7 — Conflictos. **Sec:** 7/17.
- **Propósito:** resolver conflictos de merge/rebase.
- **Resultados:** identificar marcadores, resolver, probar y continuar.
- **Desarrollo:** conflicto ocurre cuando Git no puede combinar cambios automáticamente. Marcadores `<<<<<<<`, `=======`, `>>>>>>>`. Resolver implica entender ambas versiones, elegir/combinar, `git add`, y continuar.
- **Práctica:** crea conflicto intencional y resuélvelo.
- **Independiente:** resuelve conflicto eligiendo combinación de ambos cambios.
- **Criterios:** conflicto resuelto, sin marcadores, código funciona.
- **Errores:** aceptar “ours/theirs” sin entender; dejar marcadores.
- **Eval:** ¿Qué significan los marcadores de conflicto?
- **Ref:** Git Docs. *Resolving conflicts*. https://git-scm.com/docs/git-merge#_how_conflicts_are_presented (2026-11-24).

## Lección 5.1.8 — git stash
- **Oficial:** 5.1.8 — git stash. **Sec:** 8/17.
- **Propósito:** guardar cambios temporales sin commit.
- **Resultados:** usar stash push/pop/list/drop.
- **Desarrollo:** `git stash` guarda cambios no comprometidos. Útil para cambiar de rama rápidamente. `stash pop` reaplica; puede generar conflictos.
```bash
git stash push -m "wip: validación"
git stash list
git stash pop
```
- **Práctica:** stashear cambios, cambiar rama, volver y pop.
- **Independiente:** usa múltiples stashes y recupera uno específico.
- **Criterios:** recupera cambios correctamente.
- **Errores:** olvidar stashes; acumular basura.
- **Eval:** ¿Cuándo usar stash en vez de commit?
- **Ref:** Git Docs. *git-stash*. https://git-scm.com/docs/git-stash (2026-11-24).

## Lección 5.1.9 — git log
- **Oficial:** 5.1.9 — git log. **Sec:** 9/17.
- **Propósito:** inspeccionar historial de commits.
- **Resultados:** usar `git log`, `--oneline`, `--graph`, filtros.
- **Desarrollo:** `git log` muestra historial. Opciones útiles: `--oneline --graph --decorate --all`, `--author`, `--since`, `-p`.
- **Práctica:** encuentra commit que introdujo un cambio.
- **Independiente:** usa `git log -- path` para ver historial de archivo.
- **Criterios:** encuentra información en historial.
- **Errores:** no usar log antes de operaciones riesgosas.
- **Eval:** ¿Qué muestra `git log --oneline --graph`?
- **Ref:** Git Docs. *git-log*. https://git-scm.com/docs/git-log (2026-11-24).

## Lección 5.1.10 — git diff
- **Oficial:** 5.1.10 — git diff. **Sec:** 10/17.
- **Propósito:** comparar cambios entre estados.
- **Resultados:** usar diff para working tree, staged, commits.
- **Desarrollo:** `git diff` (no staged), `git diff --staged` (staged), `git diff A..B` (entre commits/ramas). Esencial antes de commit.
- **Práctica:** revisa diff antes de hacer commit.
- **Independiente:** compara dos ramas con diff.
- **Criterios:** identifica cambios correctamente.
- **Errores:** commitear sin revisar diff.
- **Eval:** ¿Diferencia entre `git diff` y `git diff --staged`?
- **Ref:** Git Docs. *git-diff*. https://git-scm.com/docs/git-diff (2026-11-24).

## Lección 5.1.11 — git reset
- **Oficial:** 5.1.11 — git reset. **Sec:** 11/17.
- **Propósito:** mover HEAD y ajustar staging/working tree.
- **Resultados:** distinguir `--soft`, `--mixed`, `--hard`.
- **Desarrollo:** `reset --soft` mueve HEAD, mantiene staged; `--mixed` (default) quita de staged; `--hard` descarta cambios (peligroso). **Nunca usar `--hard` sin estar seguro**.
- **Práctica:** usa `reset --soft` para rehacer un commit.
- **Independiente:** explica riesgo de `reset --hard`.
- **Criterios:** elige modo correcto, no pierde trabajo.
- **Errores:** `reset --hard` en trabajo no guardado.
- **Eval:** ¿Qué hace `git reset --soft HEAD~1`?
- **Ref:** Git Docs. *git-reset*. https://git-scm.com/docs/git-reset (2026-11-24).

## Lección 5.1.12 — git revert
- **Oficial:** 5.1.12 — git revert. **Sec:** 12/17.
- **Propósito:** deshacer un commit creando otro commit inverso.
- **Resultados:** usar revert en historial compartido.
- **Desarrollo:** `git revert` no reescribe historial; crea un commit que invierte cambios. Seguro para ramas compartidas. Preferirlo sobre reset en historial público.
- **Práctica:** revierte un commit y verifica historial.
- **Independiente:** compara revert vs reset.
- **Criterios:** usa revert en caso apropiado.
- **Errores:** usar reset en rama compartida.
- **Eval:** ¿Por qué revert es más seguro en ramas compartidas?
- **Ref:** Git Docs. *git-revert*. https://git-scm.com/docs/git-revert (2026-11-24).

## Lección 5.1.13 — git cherry-pick
- **Oficial:** 5.1.13 — git cherry-pick. **Sec:** 13/17.
- **Propósito:** aplicar un commit específico en otra rama.
- **Resultados:** usar cherry-pick con cuidado.
- **Desarrollo:** `git cherry-pick <hash>` aplica el cambio de un commit como nuevo commit. Útil para hotfixes, pero puede duplicar cambios si luego se hace merge. Usar con criterio.
- **Práctica:** cherry-pick de un commit de fix a otra rama.
- **Independiente:** explica cuándo cherry-pick puede causar duplicación.
- **Criterios:** hash correcto, conflicto resuelto si aparece.
- **Errores:** cherry-pick masivo sin entender historial.
- **Eval:** ¿Qué hace cherry-pick?
- **Ref:** Git Docs. *git-cherry-pick*. https://git-scm.com/docs/git-cherry-pick (2026-11-24).

## Lección 5.1.14 — git reflog
- **Oficial:** 5.1.14 — git reflog. **Sec:** 14/17.
- **Propósito:** recuperar referencias locales perdidas.
- **Resultados:** usar reflog para encontrar commits tras reset/rebase.
- **Desarrollo:** reflog registra movimientos de HEAD localmente. Es una red de seguridad local (no se comparte por defecto). Útil para recuperar trabajo tras error.
```bash
git reflog
git reset --hard HEAD@{1}
```
- **Práctica:** simula pérdida por reset y recupera con reflog.
- **Independiente:** documenta un flujo de recuperación.
- **Criterios:** recupera commit correctamente.
- **Errores:** asumir que reflog es backup remoto.
- **Eval:** ¿Qué guarda reflog?
- **Ref:** Git Docs. *git-reflog*. https://git-scm.com/docs/git-reflog (2026-11-24).

## Lección 5.1.15 — .gitignore
- **Oficial:** 5.1.15 — .gitignore. **Sec:** 15/17.
- **Propósito:** excluir archivos que no deben versionarse.
- **Resultados:** crear `.gitignore`, entender patrones.
- **Desarrollo:** `.gitignore` evita rastrear archivos generados, secretos, dependencias, builds. No elimina archivos ya rastreados; para eso `git rm --cached`.
```gitignore
node_modules/
.env
dist/
*.log
```
- **Práctica:** crea .gitignore para proyecto Java/Node.
- **Independiente:** quita un archivo ya rastreado con `git rm --cached`.
- **Criterios:** ignora correctamente, no ignora fuente necesaria.
- **Errores:** commitear `.env`; ignorar archivos ya rastreados sin desrastrear.
- **Eval:** ¿.gitignore afecta archivos ya rastreados?
- **Ref:** Git Docs. *gitignore*. https://git-scm.com/docs/gitignore (2026-11-24).

## Lección 5.1.16 — Hooks
- **Oficial:** 5.1.16 — Hooks. **Sec:** 16/17.
- **Propósito:** automatizar acciones en eventos de Git.
- **Resultados:** entender hooks pre-commit/pre-push, crear hook simple.
- **Desarrollo:** hooks son scripts en `.git/hooks`. Útiles para lint, tests, formato. Pre-commit puede bloquear commits de mala calidad. No confiar en hooks como única seguridad (pueden saltarse con `--no-verify`).
- **Práctica:** crea hook pre-commit que ejecute un check simple.
- **Independiente:** evalúa riesgos de `--no-verify`.
- **Criterios:** hook funciona, propósito claro.
- **Errores:** hooks lentos; asumir que hooks reemplazan CI.
- **Eval:** ¿Dónde viven los hooks?
- **Ref:** Git Docs. *githooks*. https://git-scm.com/docs/githooks (2026-11-24).

## Lección 5.1.17 — Submódulos
- **Oficial:** 5.1.17 — Submódulos. **Sec:** 17/17.
- **Propósito:** incluir repositorios dentro de otro repositorio.
- **Resultados:** entender submódulos, comandos básicos, tradeoffs.
- **Desarrollo:** `git submodule add` referencia otro repo en un commit específico. Útil para dependencias versionadas, pero agrega complejidad operativa. Alternativas: paquetes, monorepo.
```bash
git submodule add https://example.com/lib.git libs/lib
git submodule update --init --recursive
```
- **Práctica:** agrega y actualiza un submódulo de prueba.
- **Independiente:** compara submódulo vs paquete vs monorepo.
- **Criterios:** entiende pin a commit, actualización.
- **Errores:** olvidar `--init --recursive`; actualizar sin revisar.
- **Eval:** ¿Qué tradeoff tienen los submódulos?
- **Ref:** Git Docs. *git-submodule*. https://git-scm.com/docs/git-submodule (2026-11-24).