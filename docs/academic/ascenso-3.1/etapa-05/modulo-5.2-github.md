# Etapa 5 · Módulo 5.2 — GitHub

**Estado:** borrador académico desarrollado (pendiente validación editorial/técnica y ejecución).  
**Alineación:** ASCENSO 3.1, Etapa 5, Módulo 5.2. **Última actualización:** 2026-11-24

## Identificación
- **Módulo:** 5.2 — GitHub. **Lecciones oficiales:** 9 (5.2.1 a 5.2.9).

## Propósito
Usar GitHub para colaborar, revisar código y automatizar flujos.

---

## Lección 5.2.1 — Repositorios remotos
- **Oficial:** 5.2.1 — Repositorios remotos. **Sec:** 1/9.
- **Propósito:** conectar repos locales con remotos.
- **Resultados:** usar `git remote add`, `origin`, push/pull.
- **Desarrollo:** remoto es una copia alojada en servidor. `origin` es convención. `git remote -v` lista remotos. HTTPS/SSH son opciones de autenticación.
- **Práctica:** clona repo, agrega remoto, push.
- **Independiente:** explica diferencia local/remoto.
- **Criterios:** remoto configurado correctamente.
- **Errores:** credenciales hardcodeadas; confundir fork y clone.
- **Eval:** ¿Qué es origin?
- **Ref:** GitHub Docs. *About remote repositories*. https://docs.github.com/en/get-started/git-basics/about-remote-repositories (2026-11-24).

## Lección 5.2.2 — Pull Requests
- **Oficial:** 5.2.2 — Pull Requests. **Sec:** 2/9.
- **Propósito:** proponer cambios para revisión antes de integrar.
- **Resultados:** crear PR, describir cambios, responder revisión.
- **Desarrollo:** PR es una solicitud de merge con discusión, revisión y checks. Debe incluir contexto, alcance, pruebas y riesgos. No mezclar cambios no relacionados.
- **Práctica:** crea PR con descripción completa.
- **Independiente:** revisa un PR y deja comentarios constructivos.
- **Criterios:** PR claro, pequeño, con contexto.
- **Errores:** PR gigante; sin descripción.
- **Eval:** ¿Qué debe incluir una buena PR?
- **Ref:** GitHub Docs. *About pull requests*. https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests (2026-11-24).

## Lección 5.2.3 — Issues
- **Oficial:** 5.2.3 — Issues. **Sec:** 3/9.
- **Propósito:** registrar trabajo, bugs y mejoras.
- **Resultados:** crear issues con contexto, pasos, resultado esperado.
- **Desarrollo:** una issue debe ser accionable: título claro, contexto, pasos de reproducción, resultado esperado/actual, evidencia. Etiquetas y asignación ayudan a priorizar.
- **Práctica:** crea issue de bug con plantilla.
- **Independiente:** convierte una solicitud vaga en issue accionable.
- **Criterios:** issue reproducible y clara.
- **Errores:** issues sin contexto; mezclar múltiples problemas.
- **Eval:** ¿Qué hace una issue accionable?
- **Ref:** GitHub Docs. *Issues*. https://docs.github.com/en/issues (2026-11-24).

## Lección 5.2.4 — Fork
- **Oficial:** 5.2.4 — Fork. **Sec:** 4/9.
- **Propósito:** copiar un repo a tu cuenta para contribuir o experimentar.
- **Resultados:** fork, sync upstream, PR desde fork.
- **Desarrollo:** fork crea copia en tu cuenta. Mantener sincronizado con upstream. Útil en open source. Diferente de clone: fork es copia en servidor.
- **Práctica:** haz fork, crea rama, abre PR.
- **Independiente:** sincroniza fork con upstream.
- **Criterios:** flujo fork correcto.
- **Errores:** trabajar en main del fork sin rama.
- **Eval:** ¿Diferencia entre fork y clone?
- **Ref:** GitHub Docs. *Fork a repo*. https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo (2026-11-24).

## Lección 5.2.5 — GitHub Actions
- **Oficial:** 5.2.5 — GitHub Actions. **Sec:** 5/9.
- **Propósito:** automatizar CI/CD con workflows.
- **Resultados:** entender workflow, job, step, trigger.
- **Desarrollo:** Actions ejecuta workflows YAML en eventos (push, PR). Útil para tests, lint, build. Secretos deben ir en GitHub Secrets, no en YAML.
```yaml
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm test
```
- **Práctica:** lee un workflow y explica sus triggers.
- **Independiente:** diseña workflow simple para tests.
- **Criterios:** entiende trigger/job/step.
- **Errores:** exponer secretos; confiar en acciones no verificadas.
- **Eval:** ¿Qué es un workflow?
- **Ref:** GitHub Docs. *Actions*. https://docs.github.com/en/actions (2026-11-24).

## Lección 5.2.6 — Releases
- **Oficial:** 5.2.6 — Releases. **Sec:** 6/9.
- **Propósito:** publicar versiones empaquetadas.
- **Resultados:** crear tag/release, notas de versión.
- **Desarrollo:** release asocia tag, binarios/notas y changelog. Usar versionado semántico cuando aplique. No publicar releases sin validación.
- **Práctica:** redacta release notes para una versión.
- **Independiente:** identifica diferencia entre tag y release.
- **Criterios:** versión, notas y artefactos claros.
- **Errores:** release sin pruebas; notas vagas.
- **Eval:** ¿Qué es un tag?
- **Ref:** GitHub Docs. *Releases*. https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases (2026-11-24).

## Lección 5.2.7 — Wikis
- **Oficial:** 5.2.7 — Wikis. **Sec:** 7/9.
- **Propósito:** documentar conocimiento del proyecto.
- **Resultados:** crear/organizar páginas wiki.
- **Desarrollo:** wiki es útil para documentación complementaria. Debe mantenerse actualizada. Para docs versionadas junto al código, preferir docs en repo.
- **Práctica:** crea estructura de wiki para proyecto.
- **Independiente:** compara wiki vs docs en repo.
- **Criterios:** documentación clara, mantenible.
- **Errores:** wiki obsoleta; duplicar docs sin fuente única.
- **Eval:** ¿Cuándo usar wiki?
- **Ref:** GitHub Docs. *Wikis*. https://docs.github.com/en/communities/documenting-your-project-with-wikis (2026-11-24).

## Lección 5.2.8 — GitHub Pages
- **Oficial:** 5.2.8 — GitHub Pages. **Sec:** 8/9.
- **Propósito:** publicar sitios estáticos desde repo.
- **Resultados:** configurar Pages, entender límites.
- **Desarrollo:** Pages sirve contenido estático. Útil para docs, portafolio, demos. No usar para secretos ni backend dinámico. Configurar rama/carpeta fuente.
- **Práctica:** publica página estática simple.
- **Independiente:** evalúa si Pages es adecuado para un caso.
- **Criterios:** sitio publicado, sin secretos.
- **Errores:** publicar datos sensibles; asumir backend.
- **Eval:** ¿Qué tipo de contenido sirve Pages?
- **Ref:** GitHub Docs. *Pages*. https://docs.github.com/en/pages (2026-11-24).

## Lección 5.2.9 — Seguridad en GitHub
- **Oficial:** 5.2.9 — Seguridad en GitHub. **Sec:** 9/9.
- **Propósito:** aplicar controles básicos de seguridad en repos.
- **Resultados:** usar 2FA, branch protection, secrets, Dependabot.
- **Desarrollo:** habilitar 2FA, proteger ramas principales, revisar permisos, usar secretos, activar alertas de dependencias. No commitear tokens. Revisar acciones de terceros.
- **Práctica:** configura checklist de seguridad para repo.
- **Independiente:** audita un repo de ejemplo y lista mejoras.
- **Criterios:** medidas concretas y priorizadas.
- **Errores:** secretos en repo; branch protection desactivada.
- **Eval:** ¿Por qué no commitear secretos?
- **Ref:** GitHub Docs. *Security*. https://docs.github.com/en/code-security (2026-11-24).