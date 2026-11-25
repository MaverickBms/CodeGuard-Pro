# Etapa 4 · Módulo 4.5 — UML

**Estado:** borrador académico desarrollado (pendiente validación editorial/técnica y ejecución).  
**Alineación:** ASCENSO 3.1, Etapa 4, Módulo 4.5. **Última actualización:** 2026-11-24

## Identificación
- **Módulo:** 4.5 — UML. **Lecciones oficiales:** 6 (4.5.1 a 4.5.6).

## Propósito
Usar UML básico para comunicar diseño de software.

---

## Lección 4.5.1 — Diagramas de clases
- **Oficial:** 4.5.1 — Diagramas de clases. **Sec:** 1/6.
- **Propósito:** representar clases, atributos, métodos y relaciones.
- **Resultados:** leer y crear diagramas de clases básicos.
- **Desarrollo:** diagrama de clases muestra clases con nombre, atributos y métodos, y relaciones entre ellas. Visibilidad: `+` public, `-` private, `#` protected. Útil para diseño y comunicación.
- **Práctica:** dibuja diagrama de clases para Producto, Pedido, Cliente.
- **Independiente:** convierte un código Java simple en diagrama de clases.
- **Criterios:** clases, atributos, métodos y relaciones correctas.
- **Errores:** diagramar todo sin criterio; confundir asociación y dependencia.
- **Eval:** ¿Qué significa `- saldo: double`?
- **Ref:** OMG. *UML 2.5*. https://www.omg.org/spec/UML/ (2026-11-24).

## Lección 4.5.2 — Diagramas de casos de uso
- **Oficial:** 4.5.2 — Diagramas de casos de uso. **Sec:** 2/6.
- **Propósito:** representar actores e interacciones con el sistema.
- **Resultados:** identificar actores, casos de uso y límites del sistema.
- **Desarrollo:** caso de uso describe una funcionalidad desde la perspectiva del actor. No detalla implementación interna. Útil para requisitos.
- **Práctica:** crea diagrama de casos de uso para app de biblioteca.
- **Independiente:** define 5 casos de uso para sistema de tickets.
- **Criterios:** actores claros, casos de uso orientados a objetivo.
- **Errores:** casos de uso demasiado técnicos; confundir con flujo interno.
- **Eval:** ¿Qué es un actor?
- **Ref:** OMG UML. https://www.omg.org/spec/UML/ (2026-11-24).

## Lección 4.5.3 — Diagramas de secuencia
- **Oficial:** 4.5.3 — Diagramas de secuencia. **Sec:** 3/6.
- **Propósito:** mostrar interacción temporal entre objetos.
- **Resultados:** leer/crear secuencias simples con mensajes.
- **Desarrollo:** muestra objetos en el tiempo, mensajes enviados y orden. Útil para entender flujos como login, compra, validación.
- **Práctica:** diagrama de secuencia para login.
- **Independiente:** modela flujo de checkout con validación de pago.
- **Criterios:** orden temporal correcto, participantes claros.
- **Errores:** demasiados detalles; omitir mensajes clave.
- **Eval:** ¿Qué representa el eje vertical?
- **Ref:** OMG UML. https://www.omg.org/spec/UML/ (2026-11-24).

## Lección 4.5.4 — Diagramas de actividad
- **Oficial:** 4.5.4 — Diagramas de actividad. **Sec:** 4/6.
- **Propósito:** modelar flujos de trabajo y decisiones.
- **Resultados:** representar inicio, acciones, decisiones, fin.
- **Desarrollo:** similar a diagrama de flujo pero orientado a actividades/procesos. Útil para workflows, reglas de negocio y procesos.
- **Práctica:** diagrama de actividad para solicitud de vacaciones.
- **Independiente:** modela proceso de registro con verificación de email.
- **Criterios:** decisiones completas, flujo legible.
- **Errores:** caminos sin fin; decisiones sin salida.
- **Eval:** ¿Cuándo usar diagrama de actividad vs secuencia?
- **Ref:** OMG UML. https://www.omg.org/spec/UML/ (2026-11-24).

## Lección 4.5.5 — Diagramas de estados
- **Oficial:** 4.5.5 — Diagramas de estados. **Sec:** 5/6.
- **Propósito:** modelar estados de un objeto y transiciones.
- **Resultados:** identificar estados, eventos, transiciones.
- **Desarrollo:** útil para objetos con ciclo de vida claro: pedido (creado, pagado, enviado, entregado), ticket, usuario. Evita transiciones inválidas.
- **Práctica:** diagrama de estados para Pedido.
- **Independiente:** modela estados de una cuenta de usuario (activa, bloqueada, suspendida).
- **Criterios:** estados válidos, transiciones etiquetadas.
- **Errores:** estados ambiguos; transiciones imposibles.
- **Eval:** ¿Qué es una transición?
- **Ref:** OMG UML. https://www.omg.org/spec/UML/ (2026-11-24).

## Lección 4.5.6 — Diagramas de componentes
- **Oficial:** 4.5.6 — Diagramas de componentes. **Sec:** 6/6.
- **Propósito:** representar componentes de alto nivel y sus dependencias.
- **Resultados:** identificar componentes, interfaces y dependencias.
- **Desarrollo:** útil para arquitectura: frontend, API, DB, servicio externo. Muestra cómo se organizan piezas del sistema sin entrar a detalle de clases.
- **Práctica:** diagrama de componentes para app web simple.
- **Independiente:** modela sistema con API, DB y servicio de pagos.
- **Criterios:** componentes claros, dependencias justificadas.
- **Errores:** confundir componente con clase; demasiado detalle.
- **Eval:** ¿Qué nivel de abstracción tiene un diagrama de componentes?
- **Ref:** OMG UML. https://www.omg.org/spec/UML/ (2026-11-24).