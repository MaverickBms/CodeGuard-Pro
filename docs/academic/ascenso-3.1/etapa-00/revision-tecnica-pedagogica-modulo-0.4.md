# Revisión de escritorio — Módulo 0.4 «Depuración»

**Fecha:** 2026-11-24  
**Tipo:** revisión documental, lógica del laboratorio y correspondencia curricular; no equivale a ejecución ni certificación técnica.  
**Estado del registro:** vigente como revisión de escritorio; no constituye aprobación independiente ni validación experimental.

## Alcance

Se revisaron los siete temas canónicos: debugging, breakpoints, stack traces, logs, hipótesis, reproducción de errores y análisis de causas. También se inspeccionó el laboratorio Python de cálculo de factura, sus pruebas de aceptación, pruebas unitarias y rúbrica.

El código y las pruebas se analizaron estáticamente; no se ejecutaron Python, unittest, VS Code ni el depurador. No se evaluó a estudiantes.

## Resultado ejecutivo

- Temas curriculares presentes: **7/7**.
- Procedimientos y actividades identificables: **7/7**.
- Laboratorio con defecto deliberado, contrato, hipótesis y pruebas de frontera: **presente**.
- Coherencia aritmética del caso de factura: **correcta por inspección** para las tres entradas indicadas.
- Ejecución de laboratorio/pruebas: **0**.
- Revisión independiente: **0**.
- Videos verificados: **0**.

## Matriz por tema

| Tema | Evidencia esperada | Hallazgo | Pendiente |
|---|---|---|---|
| 0.4.1 Debugging | Informe que separa síntoma, defecto, hipótesis, corrección y verificación | Se presenta un procedimiento repetible y un modelo de causalidad | Validar con un caso real de principiante y comprobar que no se salta a cambiar código |
| 0.4.2 Breakpoints | Registro de valores/flujo observado y conclusión | Se enseña inspección del estado y uso de puntos de interrupción | Ejecutar pasos en VS Code y verificar diferencias de configuración por lenguaje |
| 0.4.3 Stack traces | Lectura de excepción, frames y contexto relevante | Se advierte que el último frame no necesariamente es la causa raíz | Comprobar ejemplos con trazas reales y separar frames de librería y código propio |
| 0.4.4 Logs | Eventos útiles, nivel, contexto y sanitización | Se advierte que no deben registrarse tokens ni datos sensibles | Añadir revisión de retención, acceso y volumen de logs en el entorno objetivo |
| 0.4.5 Hipótesis | Dos hipótesis, predicciones y prueba discriminante | Ejemplo del límite de descuento aísla una condición | Validar que estudiantes distingan hipótesis de explicación retrospectiva |
| 0.4.6 Reproducción | Caso mínimo con entorno, entrada, pasos y resultado esperado/real | Se solicita fijar condiciones y declarar lo que falta | Ejecutar reproducción en una segunda máquina/entorno |
| 0.4.7 Análisis de causas | Prueba que falla antes y pasa después, más regresión | El criterio exige causa, corrección, pruebas vecinas y registro | Ejecutar suite y revisión independiente para confirmar cobertura real |

## Revisión estática del laboratorio

Contrato declarado: descuento del 10 % cuando subtotal ≥ 100; sin descuento cuando subtotal < 100.

| Entrada | Cálculo esperado | Resultado especificado |
|---:|---:|---:|
| 99.99 | 99.99 × 1.00 | 99.99 |
| 100.00 | 100.00 × 0.90 | 90.00 |
| 100.01 | 100.01 × 0.90 | 90.009 |

La condición inicial `subtotal > 100` no aplica descuento en el límite exacto. Cambiarla a `subtotal >= 100` es coherente con el contrato. La prueba unitaria utiliza `assertAlmostEqual`, apropiado para evitar una comparación exacta de representaciones binarias de punto flotante en este ejemplo.

**Límites del modelo:** no representa redondeo monetario, impuestos, moneda, validación de tipos ni reglas comerciales reales. El propio documento indica que esos aspectos quedan fuera del contrato. La extensión pide definirlos antes de implementarlos.

## Riesgos y mejoras

1. Ejecutar solo en un directorio de práctica; no utilizar archivos o datos reales de clientes.
2. Explicar que una salida esperada no es evidencia de ejecución: la entrega debe contener salida real, fecha, versión y comando usado.
3. Añadir el resultado de la prueba antes de corregir y después de corregir, para que el alumno demuestre la regresión.
4. Validar que la versión de Python requerida y los comandos funcionen en los sistemas soportados por el curso.
5. Revisar la consistencia de nombres de archivo/importación en la prueba (`factura.py` y `from factura import calcular_total`).
6. Mantener el lenguaje de «causa raíz» condicionado a evidencia, no a mera coincidencia temporal.
7. Verificar la política de sanitización, acceso y retención antes de introducir logs en proyectos reales.

## Criterios de salida para revisión independiente

- Ejecutar el caso inicial y confirmar que el test del límite falla.
- Aplicar únicamente el cambio propuesto y confirmar que los tres tests pasan.
- Ejecutar la prueba desde el directorio indicado y registrar versiones/salida.
- Probar entradas adicionales solo después de acordar contrato y límites.
- Verificar instrucciones de breakpoint en VS Code y al menos un entorno alternativo si forma parte del alcance.
- Revisar claridad para principiantes, accesibilidad y privacidad.
- Registrar revisor, fecha, resultado y correcciones.

## Límites y estado

No se ejecutó el código ni se observó una sesión de depuración. La comprobación aritmética es estática; no demuestra que el archivo corra sin errores ni que el entorno esté correctamente configurado. El módulo es la base de trabajo activa. No se declara el laboratorio probado, el módulo aprobado ni contenido publicado.

**Estado final:** módulo en base de trabajo activa; 0/7 temas con validación práctica independiente; 0 pruebas ejecutadas; 0 videos verificados; 0 aprobaciones y 0 publicaciones.
