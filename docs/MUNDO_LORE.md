# Mundo CodeGuard — universo, narrativa y personajes

**Estado:** documento de diseño y dirección; no todo lo descrito está implementado.  
**Implementado hoy:** Aldea del Método, Biblioteca de la Aldea, Salón de las Leyendas, cuatro NPC y cuatro misiones.  
**No implementado:** territorios futuros, combate, jefes y personajes marcados como conceptuales.

## 1. Premisa

El mundo de CodeGuard nace alrededor de la **Chispa del Conocimiento**, una
energía que mantiene unidos los oficios, las academias y las rutas de las
civilizaciones. Durante generaciones, sus habitantes aprendieron a resolver
problemas con método: observar, preguntar, probar y corregir. La Chispa no es
magia arbitraria: es la metáfora de la curiosidad sostenida por la evidencia.

Una fractura silenciosa, **la Ruptura**, está separando los conocimientos de sus
fuentes. Bibliotecas que olvidan autores, caminos que dejan de conectar aldeas y
criaturas que repiten errores antiguos. La amenaza no es un ejército: es la
pérdida de criterio. La aventura consiste en reconstruir esas conexiones sin
inventar respuestas.

## 2. Civilizaciones y facciones

| Facción | Territorio | Valores | Estado |
|---|---|---|---|
| Aldea del Método | Región inicial | Aprendizaje activo, evidencia y depuración | Implementada |
| Biblioteca de la Aldea | Interior inicial | Fuentes, licencias y trazabilidad | Implementada |
| Salón de las Leyendas | Interior inicial | Memoria de hazañas y colecciones | Implementada |
| Reino de los Sabios | Academias y consejos | Debate, pedagogía y gobierno | Futuro |
| Clanes del Norte | Tierras frías | Resistencia, runas y trabajo comunitario | Futuro |
| Corte de los Reyes | Castillos y ciudades | Historia, alianzas y responsabilidad | Futuro |
| Círculo de Magos | Torres y santuarios | Abstracción, algoritmos y ética | Futuro |
| Guardianes de Dragones | Montañas | Custodia de reliquias y equilibrio | Futuro |
| Orcos de las Ruinas | Ruinas antiguas | Memoria oral y reconstrucción | Futuro |

Las facciones no son buenas o malas por naturaleza. Cada una tiene una
motivación comprensible y una tensión con las demás.

## 3. Personajes implementados

### Mentora Ada
Guía de la Aldea del Método. Enseña recuperación activa, método y evidencia.
No entrega respuestas: devuelve preguntas.

### Bibliotecario Byte
Custodio de la biblioteca. Distingue documentación oficial, tutoriales y foros;
exige fecha, versión y alcance.

### Guardián del Error
Guardián del reto de depuración. Plantea errores reproducibles y exige
evidencia; no acepta soluciones por azar.

### Nexo, mentor de lógica
Mentor del reto de condiciones. Trabaja con operadores, listas vacías y pruebas
de regresión.

### Cronista Elyra
Cronista del Salón de las Leyendas. Conserva trofeos, reliquias y hazañas, y
recuerda que el progreso académico se consulta fuera del museo.

## 4. Personajes conceptuales para expansión

> **No implementados.** Se documentan para mantener coherencia futura; no deben
> aparecer como disponibles en la aplicación.

- **Rey Alaric** — monarca del Reino de los Sabios; protector de archivos.
- **Reina Mira** — diplomática; impulsa consejos abiertos.
- **Princesa Lyra** — estudiante de cartografía y lenguajes antiguos.
- **Caballero Ragnar** — defensor de los caminos del norte.
- **Maga Selene** — investigadora de patrones y algoritmos.
- **Grum, orco cartógrafo** — reconstruye mapas de las ruinas.
- **Vael, dragón anciano** — guardián de una reliquia de conocimiento.
- **La Ruptura** — antagonista abstracto; no un villano con ejército.

## 5. Arco narrativo previsto

1. **Aldea del Método:** el jugador aprende a estudiar y a depurar.
2. **Biblioteca:** descubre que las fuentes deben verificarse.
3. **Salón:** comprende que las hazañas se recuerdan y se coleccionan.
4. **Reino de los Sabios:** primeros conflictos entre interpretaciones.
5. **Tierras del Norte:** una ruta de conocimiento se rompe; hay que restaurarla.
6. **Bosque de los Misterios:** criaturas que repiten errores sin contexto.
7. **Dominio de los Dragones:** una reliquia exige una prueba de criterio.
8. **Ruptura:** el jugador demuestra que el conocimiento se reconstruye con
   evidencia, no con autoridad.

La historia admite expansiones porque la amenaza es estructural, no un jefe
único. Cada región resuelve una parte y deja una pregunta abierta.

## 6. Integración con ASCENSO 3.1

- Una misión puede enlazar a la etapa 0 real ya implementada.
- Las misiones educativas futuras deben referenciar UUID reales del roadmap.
- Las recompensas del mundo son cosméticas/motivacionales; no acreditan
  lecciones ni exámenes.
- Las misiones no deben convertirse en lecciones escolares encubiertas: el
  contenido educativo aparece cuando la aventura lo necesita.

## 7. Reglas de contenido

- No inventar UUID, lecciones ni títulos curriculares.
- No declarar territorios futuros como jugables.
- No usar imágenes de referencia como assets distribuibles.
- No introducir personajes conceptuales en el mapa sin sprite, diálogo,
  misión y pruebas.
- Toda rareza de trofeo debe tener un criterio explícito y auditable.

## 8. Relación con el Salón de las Leyendas

El Salón convierte el progreso del juego en objetos visibles:

- misiones completadas → medallas y trofeos;
- minijuegos superados → reliquias;
- objetos de alta rareza → armería;
- logros académicos existentes → galería de logros, sin duplicar su fuente.

La fuente de verdad sigue siendo `EstadoMundo`, `ItemInventario`,
`LogroObtenido` y el sistema académico. El Salón es una representación, no un
segundo sistema de progreso.
