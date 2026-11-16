# ADR-010 — Tutor IA local para Fase 3

**Estado:** Aprobado  
**Fecha:** 16 de noviembre de 2026  
**Decisor:** Orquestador / CodeGuard Pro Tech Lead  
**Fase:** Fase 3 — Tutor inteligente local  
**Relacionado:** `docs/PLAN_MAESTRO_CODEGUARD.md` (sección Fase 3), `apps/tutoring/`

## Contexto

La Fase 3 del plan maestro requiere un tutor inteligente local que acompañe al estudiante sin resolver los ejercicios por él. El tutor debe:

- Explicar errores de sintaxis, lógica y enfoque.
- Analizar el intento y relacionarlo con el objetivo del ejercicio.
- Proporcionar orientación gradual (máximo 3 pistas por ejercicio).
- No revelar la solución completa ni entregar el código final.
- Funcionar localmente siempre que sea posible.
- No confiar en la IA para decidir una aprobación académica.

La evaluación determinista del ejercicio debe ser la fuente de verdad; el tutor explica el resultado.

## Problema

Necesitamos un componente de IA que:

1. Sea local (sin depender de servicios externos de pago).
2. No ejecute código del estudiante (seguridad por diseño).
3. Sea transparente: el estudiante debe saber cuándo una respuesta procede del tutor vs. un validador automático.
4. Respete el límite de 3 pistas por ejercicio sin reinicios para evadir el límite.
5. No altere directamente las calificaciones ni la progresión académica.

## Alternativas consideradas

| Alternativa | Ventajas | Desventajas | Decisión |
|---|---|---|---|
| 1. Servicio de IA externo (OpenAI, Anthropic, etc.) | Modelos potentes, sin infraestructura local. | Requiere conexión permanente, clave de API, costo recurrente, envía código del estudiante a terceros. Rompe el principio offline-first y privacidad. | **Descartada**. |
| 2. Modelo local con Transformers + PyTorch | Totalmente local, sin costes recurrentes. | Requiere mucha RAM/CPU (~1.3 GB libre en el equipo objetivo), modelo grande, complejidad de despliegue. | **Descartada para v1**. |
| 3. Modelo local vía Ollama | Local, modelos ligeros (1-2 GB), API REST simple, ya instalado en el equipo. | Depende de que Ollama esté instalado y corriendo; si no está disponible, el tutor se degrada graciosamente (modo sin IA). | **Adoptada**. |
| 4. Tutor basado en reglas estáticas (sin IA) | Sin dependencias externas, predecible. | Limitado en capacidad de explicación, no se adapta al nivel del estudiante. | **Complementaria** (usada como fallback). |

## Decisión adoptada

Implementar el tutor IA local usando **Ollama** con el modelo `qwen2.5-coder:1.5b` (o `llama3.2:1b` como fallback), expuesto a través de una app Django `apps/tutoring` que:

- Llama a la API REST local de Ollama (`http://localhost:11434/api/chat`).
- No envía datos personales del estudiante, solo el enunciado del ejercicio, el intento y el contexto pedagógico.
- Implementa un límite de 3 pistas por ejercicio, persistido en la base de datos.
- Se degrada graciosamente si Ollama no está disponible (respuesta basada en reglas estáticas).
- Nunca ejecuta código del estudiante; solo analiza texto.
- La evaluación determinista sigue siendo la fuente de verdad para la aprobación.

## Justificación

- Mantiene el principio offline-first: el tutor funciona sin Internet una vez descargado el modelo.
- No introduce dependencias de pago ni servicios externos.
- Ollama ya está instalado en el equipo objetivo.
- El modelo `qwen2.5-coder:1.5b` es adecuado para tareas de programación y explicación.
- La degradación graciosa garantiza que la aplicación siga funcionando sin el tutor.

## Consecuencias

Positivas:
- Tutor local, privado, sin costes recurrentes.
- No ejecuta código del estudiante (seguridad).
- Transparente: se indica claramente cuándo una respuesta es del tutor.
- Límite de 3 pistas persistido en BD.

Negativas / costes aceptados:
- Requiere que Ollama esté instalado y el modelo descargado (~1 GB).
- Si Ollama no está disponible, el tutor opera en modo reglas estáticas (capacidad reducida).
- La calidad de las explicaciones depende del modelo local (1.5B parámetros).

## Implicaciones futuras

- El modelo se puede actualizar cambiando la configuración sin cambiar el código.
- Se puede añadir un selector de modelo en la configuración del sistema.
- Si en el futuro se necesita un modelo más potente, se puede cambiar a uno mayor (7B) si el hardware lo permite.

## Verificación pendiente

- Ejecutar `ollama pull qwen2.5-coder:1.5b` (ya disponible).
- Probar la API de Ollama localmente.
- Implementar pruebas unitarias que mockeen la respuesta de Ollama.
- Verificar degradación graciosa cuando Ollama no responde.

---
*ADR registrado. La implementación requiere crear `apps/tutoring/` con modelos, servicios y vistas.*