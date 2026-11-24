# Etapa 1 · Módulo 1.2 — Representación de información

**Estado de trabajo:** BASE DE TRABAJO ACTIVA · v0.1.0.  
**Alineación:** ASCENSO 3.1, Etapa 1, apartado 1.2.  
**Temas oficiales:** sistema binario, sistema decimal, sistema hexadecimal, bits y bytes, ASCII, Unicode, UTF-8, representación de enteros y números de punto flotante.

## Objetivo

Comprender cómo se representan números, caracteres y valores numéricos dentro de un computador y realizar conversiones básicas entre sistemas de numeración.

## Resultados de aprendizaje

Podrás convertir números enteros entre decimal, binario y hexadecimal; interpretar bits y bytes; explicar la diferencia entre ASCII, Unicode y UTF-8; reconocer representaciones de enteros con y sin signo; y explicar por qué los números de punto flotante pueden tener errores de precisión.

## 1.2.1 — Sistema binario

En un sistema posicional, el valor de cada dígito depende de su posición y de la base. El sistema binario utiliza base 2 y los dígitos 0 y 1. Cada posición representa una potencia de 2.

Ejemplo: (1101_2=1\cdot8+1\cdot4+0\cdot2+1\cdot1=13_{10}).

Para convertir un número binario a decimal, multiplica cada bit por la potencia de 2 que corresponde a su posición, empezando por (2^0) a la derecha.

Ejemplo: (10110_2=1\cdot16+0\cdot8+1\cdot4+1\cdot2+0=22_{10}).

## 1.2.2 — Sistema decimal

El sistema decimal utiliza base 10 y los dígitos 0–9. Cada posición representa una potencia de 10.

Ejemplo: (472_{10}=4\cdot10^2+7\cdot10^1+2\cdot10^0).

Para convertir un entero decimal a binario, divide sucesivamente entre 2 y registra los restos. Lee los restos desde el último al primero.

Ejemplo: (13_{10})
- 13 ÷ 2 = 6, resto 1
- 6 ÷ 2 = 3, resto 0
- 3 ÷ 2 = 1, resto 1
- 1 ÷ 2 = 0, resto 1

Resultado: (1101_2).

## 1.2.3 — Sistema hexadecimal

El sistema hexadecimal utiliza base 16 y los símbolos 0–9 y A–F, donde A=10, B=11, …, F=15.

Ejemplo: (2F_{16}=2\cdot16+15=47_{10}).

Cada dígito hexadecimal corresponde exactamente a cuatro bits:
- 0000 = 0
- 1001 = 9
- 1010 = A
- 1111 = F

Ejemplo: (1101\ 1010_2 = DA_{16}). Agrupa desde la derecha en bloques de cuatro; agrega ceros a la izquierda si hace falta.

**Errores frecuentes:** leer restos en orden incorrecto; olvidar que la primera posición vale (b^0); confundir el número de dígitos con el valor; interpretar A–F como letras sin valor numérico.

## 1.2.4 — Bits y bytes

Un bit (b) es una unidad binaria que puede tomar dos valores. Un byte (B) está formado por ocho bits. La distinción entre b y B importa: Mb/s suele expresar megabits por segundo; MB/s, megabytes por segundo.

Las unidades decimales y binarias no son idénticas:
- 1 kB = 1.000 bytes; 1 KiB = 1.024 bytes.
- 1 MB = 1.000.000 bytes; 1 MiB = 1.048.576 bytes.

En contextos comerciales se usan con frecuencia unidades decimales; algunos sistemas operativos muestran unidades binarias o etiquetas aproximadas. Comprueba siempre qué unidad se está utilizando.

**Ejercicio:** convierte 3 KiB a bytes y 24 bits a bytes.  
Solución: (3\times1024=3072) bytes; (24/8=3) bytes.

## 1.2.5 — ASCII

**ASCII** es un código histórico de 7 bits que asigna valores a letras latinas básicas, dígitos, signos y caracteres de control. Los valores ASCII originales van de 0 a 127.

## 1.2.6 — Unicode

**Unicode** define un repertorio de caracteres y puntos de código para representar sistemas de escritura y símbolos de muchas lenguas. Un punto de código se escribe, por ejemplo, como U+0041 para la letra A. Unicode no es por sí mismo una codificación de bytes.

## 1.2.7 — UTF-8

**UTF-8** es una codificación de Unicode de longitud variable: un punto de código se representa usando entre uno y cuatro bytes. Los primeros 128 valores coinciden con ASCII, lo que permite compatibilidad con texto ASCII básico.

Ejemplos:
- A: U+0041 → UTF-8 `41` hexadecimal.
- ñ: U+00F1 → UTF-8 `C3 B1`.
- €: U+20AC → UTF-8 `E2 82 AC`.

No confundas:
- carácter: unidad abstracta del texto;
- punto de código: número asignado por Unicode;
- unidad de código: unidad usada por una codificación;
- byte: octeto almacenado o transmitido.

Un carácter percibido por el usuario puede estar formado por varios puntos de código (por ejemplo, una letra más una marca combinante). Por eso «un carácter siempre ocupa un byte» es falso.

## 1.2.8 — Representación de enteros

Un entero sin signo de (n) bits puede representar desde 0 hasta (2^n-1). Por ejemplo, con 8 bits: 0 a 255.

La representación de complemento a dos es habitual para enteros con signo. Con (n) bits, el rango es (-2^{n-1}) a (2^{n-1}-1). En 8 bits: −128 a 127.

Ejemplo de 8 bits:
- (+5): `00000101`
- para obtener −5, invierte los bits de +5 y suma 1: `11111010 + 1 = 11111011`.

El ancho es importante. Si un resultado excede el rango representable, puede ocurrir desbordamiento (overflow), truncamiento o una excepción, según lenguaje y operación.

**Ejercicio:** indica el rango de un entero sin signo de 16 bits y de uno con signo en complemento a dos de 16 bits.  
Solución: 0 a 65.535; −32.768 a 32.767.

## 1.2.9 — Números de punto flotante

Los números de punto flotante representan un conjunto amplio de valores mediante signo, exponente y significando (mantisa en terminología tradicional). El estándar IEEE 754 define formatos y operaciones ampliamente utilizados.

Muchos valores decimales no tienen representación binaria finita. Por ello, operaciones como (0.1+0.2) pueden producir un resultado cercano, pero no exactamente igual a 0.3 en formatos binarios comunes.

Conceptos:
- **precisión:** cantidad de información significativa;
- **rango:** magnitud de valores representables;
- **redondeo:** aproximación al valor representable;
- **overflow:** resultado fuera del rango;
- **underflow:** resultado demasiado pequeño para representarse normalmente;
- **NaN e infinito:** valores especiales en formatos IEEE 754.

No compares números de punto flotante con igualdad exacta cuando el cálculo puede acumular error. En aplicaciones numéricas suele utilizarse una tolerancia definida según el problema. Para dinero, normalmente se usan enteros en unidades mínimas o tipos decimales apropiados, no `float` binario sin analizar las consecuencias.

## Laboratorio — Codificador de datos

Crea un pequeño programa local (en el lenguaje que prefieras) que:
1. convierta enteros decimales a binario y hexadecimal;
2. convierta binario y hexadecimal a decimal;
3. muestre la representación de un byte;
4. codifique y decodifique texto UTF-8 mostrando bytes hexadecimales;
5. valide rangos de enteros de 8 y 16 bits con y sin signo;
6. muestre un ejemplo de aproximación de punto flotante y explique el resultado.

**Casos mínimos de prueba**
- 0, 1, 13, 127, 128, 255;
- 256 fuera del rango de un entero sin signo de 8 bits;
- −1, −128 y 128 para entero con signo de 8 bits;
- texto: `ASCII`, `año`, `café`, `€`;
- (0.1+0.2) y comparación con 0.3 usando tolerancia.

**Criterios:** conversiones correctas, límites explícitos, tratamiento de entradas inválidas, salida documentada y pruebas reproducibles. No se declara el laboratorio verificado hasta ejecutar el programa y registrar lenguaje/versión.

## Ejercicios progresivos

1. Convierte (45_{10}) a binario y hexadecimal.  
2. Convierte (101101_2) a decimal.  
3. Convierte (3A_{16}) a decimal.  
4. ¿Cuántos bits hay en 5 bytes?  
5. ¿Cuántos bytes UTF-8 ocupa normalmente el texto «Año»?  
6. ¿Por qué Unicode y UTF-8 no son sinónimos?  
7. ¿Cuál es el rango de un entero con signo de 8 bits en complemento a dos?  
8. ¿Por qué 0.1 no suele representarse exactamente en punto flotante binario?

**Respuestas:** 45 = (101101_2=2D_{16}); (101101_2=45); (3A_{16}=58); 40 bits; «Año» ocupa 4 bytes en UTF-8 (A=1, ñ=2, o=1); Unicode asigna puntos de código y UTF-8 los codifica en bytes; −128 a 127; porque la fracción binaria es periódica y se aproxima a una cantidad finita de bits.

## Autoevaluación

Explica con tus propias palabras:
- por qué se usan bases 2 y 16 en computación;
- qué diferencia hay entre bit, byte, kB y KiB;
- cómo se relacionan ASCII, Unicode y UTF-8;
- cómo se detecta un overflow en un rango de bits definido;
- por qué la precisión numérica es una decisión de diseño.

## Recursos audiovisuales

No se incluye video en esta versión: no se ha verificado una pieza cuyo audio hablado sea español y que enseñe con precisión conversiones de bases, codificación UTF-8, enteros y punto flotante. No se sustituye esa verificación con un video genérico de informática.

## Referencias

- Unicode Consortium, **The Unicode Standard**: https://www.unicode.org/standard/standard.html
- Unicode Consortium, **UTF-8** (FAQ): https://www.unicode.org/faq/utf_bom.html
- IETF, **RFC 3629 — UTF-8, a transformation format of ISO 10646**: https://www.rfc-editor.org/rfc/rfc3629
- IEEE, **IEEE 754 floating-point arithmetic** (standard overview): https://standards.ieee.org/ieee/754/6210/
- NIST, **Guide for the Use of the International System of Units (SI)**, unidades y prefijos: https://www.nist.gov/pml/special-publication-811

**Consulta de fuentes:** 2026-11-19.  
**Verificación práctica:** ejercicios calculados manualmente; laboratorio de software propuesto, no ejecutado.  
**Estado editorial:** en desarrollo; no aprobado ni publicado.
