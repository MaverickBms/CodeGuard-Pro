# Etapa 1 · Módulo 1.2 — Representación de información

**Estado:** borrador académico desarrollado (pendiente validación editorial externa y verificación técnica formal).  
**Alineación:** ASCENSO 3.1, Etapa 1, Módulo 1.2.  
**Última actualización:** 2026-11-24

## Identificación del módulo
- **Etapa:** 1 — Fundamentos de computación y arquitectura del computador.
- **Módulo:** 1.2 — Representación de información.
- **Lecciones oficiales:** 9 (1.2.1 a 1.2.9).
- **Prerrequisitos:** Módulo 1.1 recomendado; aritmética básica.

## Propósito del módulo
Explicar cómo los computadores representan números, texto y valores numéricos mediante bits. El módulo conecta matemáticas básicas con informática práctica: conversiones, codificación de caracteres, enteros y punto flotante.

## Resultados de aprendizaje del módulo
1. Convertir entre sistemas binario, decimal y hexadecimal.
2. Explicar la relación entre bits, bytes y unidades de información.
3. Distinguir ASCII, Unicode y UTF-8.
4. Explicar representación de enteros con y sin signo.
5. Comprender por qué el punto flotante puede producir aproximaciones.

---

## Lección 1.2.1 — Sistema binario

### Identificación
- **Etapa:** 1 · **Módulo:** 1.2 · **Lección oficial:** 1.2.1 — Sistema binario.
- **Secuencia:** 1 de 9.

### Propósito de aprendizaje
Comprender el sistema binario como base de la representación digital.

### Conocimientos previos
- Potencias básicas (2^0, 2^1, 2^2...).
- Suma y multiplicación básicas.

### Resultados de aprendizaje
- Definir sistema binario y base 2.
- Convertir números binarios a decimal y decimal a binario.
- Explicar por qué el binario se adapta a circuitos digitales.
- Identificar errores comunes de conversión.

### Desarrollo conceptual
El sistema binario es un sistema de numeración posicional de base 2. Solo usa dos dígitos: 0 y 1. Cada posición representa una potencia de 2, igual que en decimal cada posición representa una potencia de 10.

Ejemplo: `1011₂ = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 8 + 0 + 2 + 1 = 11₁₀`.

Los computadores usan binario porque los circuitos digitales pueden representar dos estados estables con fiabilidad: presencia/ausencia de voltaje, encendido/apagado, carga/descarga. Esto no significa que el computador “piense en ceros y unos” como una persona; significa que su hardware físico opera con estados binarios que se interpretan como información.

Para convertir decimal a binario se puede usar división sucesiva entre 2 y leer los restos de abajo hacia arriba. Para convertir binario a decimal se suman las potencias de 2 donde hay un bit en 1.

### Ejemplo técnico desarrollado
**Convertir 26₁₀ a binario:**

| División | Cociente | Resto |
|---|---:|---:|
| 26 ÷ 2 | 13 | 0 |
| 13 ÷ 2 | 6 | 1 |
| 6 ÷ 2 | 3 | 0 |
| 3 ÷ 2 | 1 | 1 |
| 1 ÷ 2 | 0 | 1 |

Leyendo restos de abajo hacia arriba: `11010₂`.

**Verificación:** `16 + 8 + 2 = 26`. Correcto.

### Práctica guiada
- **Objetivo:** convertir valores simples.
- **Procedimiento:** convierte a binario: 5, 13, 32. Convierte a decimal: `111`, `10000`, `10101`.
- **Resultado esperado:** 5=`101`, 13=`1101`, 32=`100000`; `111`=7, `10000`=16, `10101`=21.
- **Verificación:** comprueba cada resultado sumando potencias de 2.

### Actividad independiente
Crea 5 números decimales entre 1 y 100, conviértelos a binario y verifica con la operación inversa. Documenta el proceso.

### Criterios de aceptación
- Conversiones correctas.
- Muestra el procedimiento, no solo el resultado.
- Verifica al menos un resultado con conversión inversa.

### Errores frecuentes y recomendaciones
- **Error:** leer restos de arriba hacia abajo. **Recomendación:** escribir “de abajo hacia arriba”.
- **Error:** confundir posición con valor. **Recomendación:** etiquetar potencias de 2.
- **Error:** olvidar el bit más a la derecha como 2^0. **Recomendación:** empezar siempre por la derecha.

### Evaluación de comprensión
1. ¿Por qué el binario es adecuado para hardware digital?
2. Convierte `11001₂` a decimal.
3. ¿Qué error ocurre si lees los restos en orden inverso?

### Referencias
- NIST. *Guide for the Use of the International System of Units (SI)*, SP 811. https://www.nist.gov/pml/special-publication-811. Consultado: 2026-11-24.
- Khan Academy. *Binary number system* (recurso educativo complementario; no primario normativo). https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:digital-information/xcae6f4a7ff015e7d:binary-numbers/a/bits-and-binary. Consultado: 2026-11-24.

---

## Lección 1.2.2 — Sistema decimal

### Identificación
- **Etapa:** 1 · **Módulo:** 1.2 · **Lección oficial:** 1.2.2 — Sistema decimal.
- **Secuencia:** 2 de 9.

### Propósito de aprendizaje
Consolidar la comprensión del sistema decimal como sistema posicional de referencia para entender otras bases.

### Conocimientos previos
- Aritmética básica.
- Lección 1.2.1.

### Resultados de aprendizaje
- Explicar el sistema decimal como base 10.
- Descomponer un número decimal en potencias de 10.
- Usar el decimal como referencia para conversiones.
- Reconocer que la “naturalidad” del decimal es cultural/práctica, no técnica.

### Desarrollo conceptual
El sistema decimal usa base 10 y dígitos 0 al 9. Su valor posicional se basa en potencias de 10: unidades (10^0), decenas (10^1), centenas (10^2), etc.

Ejemplo: `4.372 = 4×10³ + 3×10² + 7×10¹ + 2×10⁰`.

Este sistema es habitual en la vida humana, posiblemente por la convención histórica y el conteo con dedos, pero no es el más conveniente para circuitos digitales. Comprender bien el decimal ayuda a entender binario y hexadecimal, porque la lógica posicional es la misma: cambia la base.

En informática, el decimal se usa para entrada/salida humana, documentación, medidas y muchas interfaces, mientras que internamente la representación física es binaria.

### Ejemplo técnico desarrollado
**Descomposición:** `5.209₁₀`

- 5 × 1000 = 5000
- 2 × 100 = 200
- 0 × 10 = 0
- 9 × 1 = 9
- Total = 5209

**Interpretación:** al convertir a binario, el valor es el mismo; cambia la representación.

### Práctica guiada
- **Objetivo:** hacer explícito el valor posicional.
- **Procedimiento:** descompón 308, 1.245 y 90.001 en potencias de 10.
- **Resultado esperado:** descomposiciones correctas.
- **Verificación:** suma los términos y confirma el número original.

### Actividad independiente
Explica por qué `09` y `9` tienen el mismo valor en decimal, pero el cero a la izquierda puede importar en otros contextos (códigos, formatos, relleno).

### Criterios de aceptación
- Descompone correctamente números en potencias de 10.
- Relaciona decimal con otras bases por lógica posicional.
- Identifica un contexto donde la representación importa.

### Errores frecuentes y recomendaciones
- **Error:** pensar que decimal es “el sistema real” y binario “artificial”. **Recomendación:** ambos son representaciones; cambia la base.
- **Error:** confundir valor numérico con formato. **Recomendación:** distinguir valor, representación y codificación.

### Evaluación de comprensión
1. ¿Qué significa que decimal sea posicional?
2. ¿Qué cambia y qué se conserva al convertir 13₁₀ a binario?
3. Da un ejemplo donde el formato decimal importe aunque el valor sea el mismo.

### Referencias
- NIST. *SI Units and Prefixes*. https://www.nist.gov/pml/owm/metric-si/si-units. Consultado: 2026-11-24.
- Ifrah, G. *The Universal History of Numbers*. Wiley. Referencia histórica complementaria.

---

## Lección 1.2.3 — Sistema hexadecimal

### Identificación
- **Etapa:** 1 · **Módulo:** 1.2 · **Lección oficial:** 1.2.3 — Sistema hexadecimal.
- **Secuencia:** 3 de 9.

### Propósito de aprendizaje
Usar hexadecimal como representación compacta de datos binarios.

### Conocimientos previos
- Lecciones 1.2.1 y 1.2.2.

### Resultados de aprendizaje
- Definir sistema hexadecimal (base 16).
- Convertir entre hexadecimal, binario y decimal.
- Explicar por qué se usa en informática.
- Interpretar valores hexadecimales simples en contextos técnicos.

### Desarrollo conceptual
El sistema hexadecimal usa base 16. Sus dígitos son 0-9 y A-F, donde A=10, B=11, C=12, D=13, E=14, F=15. Cada dígito hexadecimal representa exactamente 4 bits, lo que lo hace muy conveniente para representar binario de forma compacta.

Por ejemplo, `1111₂ = F₁₆` y `1010₂ = A₁₆`. Un byte (8 bits) se representa con dos dígitos hexadecimales.

El hexadecimal se usa en direcciones de memoria, colores web, dumps de memoria, MACs, hashes, codificación de bytes y depuración. No es “otro tipo de dato”, sino otra forma de representar valores.

### Ejemplo técnico desarrollado
**Convertir `2F₁₆` a decimal y binario:**

- `2F₁₆ = 2×16¹ + 15×16⁰ = 32 + 15 = 47₁₀`.
- `2 = 0010₂`, `F = 1111₂`, entonces `2F₁₆ = 00101111₂`.

**Verificación:** `00101111₂ = 32+8+4+2+1 = 47₁₀`.

### Práctica guiada
- **Objetivo:** convertir hexadecimales comunes.
- **Procedimiento:** convierte `A`, `1F`, `FF`, `100` a decimal. Convierte `10101100₂` a hex.
- **Resultado esperado:** 10, 31, 255, 256; `AC`.
- **Verificación:** usa conversión por bloques de 4 bits.

### Actividad independiente
Encuentra tres usos reales de hexadecimal en informática (por ejemplo, color CSS, dirección, hash) y explica qué representa cada uno.

### Criterios de aceptación
- Convierte correctamente entre hex, binario y decimal.
- Explica la relación 1 dígito hex = 4 bits.
- Identifica usos reales.

### Errores frecuentes y recomendaciones
- **Error:** tratar A-F como letras sin valor. **Recomendación:** memorizar A=10 hasta F=15.
- **Error:** agrupar binario desde la izquierda. **Recomendación:** agrupar desde la derecha en bloques de 4.
- **Error:** confundir prefijo `0x` con parte del valor. **Recomendación:** `0x` indica notación hexadecimal en muchos lenguajes.

### Evaluación de comprensión
1. ¿Por qué hexadecimal es cómodo para representar bytes?
2. Convierte `7B₁₆` a decimal.
3. ¿Qué significa `0xFF` en muchos contextos de programación?

### Referencias
- RFC 4648. *The Base16, Base32, and Base64 Data Encodings*. https://www.rfc-editor.org/rfc/rfc4648. Consultado: 2026-11-24. (Base16/hex como representación; útil como referencia formal de codificación.)
- Unicode Consortium. *Glossary*. https://www.unicode.org/glossary/. Consultado: 2026-11-24.

---

## Lección 1.2.4 — Bits y bytes

### Identificación
- **Etapa:** 1 · **Módulo:** 1.2 · **Lección oficial:** 1.2.4 — Bits y bytes.
- **Secuencia:** 4 de 9.

### Propósito de aprendizaje
Comprender unidades básicas de información digital y sus múltiplos.

### Conocimientos previos
- Lecciones 1.2.1 a 1.2.3.

### Resultados de aprendizaje
- Definir bit y byte.
- Diferenciar b/B y prefijos decimales/binarios (kB/KiB, MB/MiB).
- Calcular conversiones simples de unidades.
- Interpretar especificaciones de almacenamiento y red con cuidado.

### Desarrollo conceptual
Un **bit** es la unidad mínima de información en sistemas binarios: puede representar 0 o 1. Un **byte** son 8 bits. Los bytes se usan para representar caracteres, valores numéricos, instrucciones y otros datos.

Los prefijos pueden causar confusión:
- **Decimal (SI):** kB=1000 bytes, MB=10^6 bytes, GB=10^9 bytes.
- **Binario (IEC):** KiB=1024 bytes, MiB=1024^2 bytes, GiB=1024^3 bytes.

Fabricantes de almacenamiento suelen usar unidades decimales; algunos sistemas operativos muestran valores que el usuario interpreta como GB pero se calculan con base binaria. No es que “falte espacio” mágicamente: suele ser diferencia de unidades.

También hay que distinguir bits y bytes en redes: 100 Mbps son megabits por segundo, no megabytes por segundo.

### Ejemplo técnico desarrollado
**Caso:** conexión de 100 Mbps.

- 100 megabits/segundo = 12.5 megabytes/segundo teóricos (100/8).
- En la práctica, el rendimiento real es menor por overhead, latencia, protocolo y condiciones.

**Interpretación:** confundir Mb con MB lleva a expectativas incorrectas.

### Práctica guiada
- **Objetivo:** convertir unidades.
- **Procedimiento:** calcula: 32 bits a bytes; 4 KiB a bytes; 200 Mbps a MB/s teóricos.
- **Resultado esperado:** 4 bytes; 4096 bytes; 25 MB/s teóricos.
- **Verificación:** mostrar operación.

### Actividad independiente
Toma una captura o nota de una especificación de disco y otra de red. Explica qué unidades usa cada una y qué significan.

### Criterios de aceptación
- Diferencia bit y byte correctamente.
- Realiza conversiones correctas.
- Explica la diferencia entre prefijos decimales y binarios.

### Errores frecuentes y recomendaciones
- **Error:** usar B y b indistintamente. **Recomendación:** escribir la unidad completa.
- **Error:** asumir que 1 GB siempre son 1024^3 bytes. **Recomendación:** verificar contexto SI/IEC.
- **Error:** esperar velocidad de red igual al valor comercial sin overhead. **Recomendación:** distinguir teórico de real.

### Evaluación de comprensión
1. ¿Cuántos bits hay en 16 bytes?
2. ¿Por qué un disco de “500 GB” puede mostrarse con menos GiB?
3. ¿Qué diferencia hay entre Mbps y MB/s?

### Referencias
- NIST. *Prefixes for binary multiples*. https://physics.nist.gov/cuu/Units/binary.html. Consultado: 2026-11-24.
- IEC. *International Standard IEC 60027-2* (referencia de prefijos binarios; consultar edición aplicable).

---

## Lección 1.2.5 — ASCII

### Identificación
- **Etapa:** 1 · **Módulo:** 1.2 · **Lección oficial:** 1.2.5 — ASCII.
- **Secuencia:** 5 de 9.

### Propósito de aprendizaje
Comprender ASCII como codificación histórica de caracteres y sus limitaciones.

### Conocimientos previos
- Lecciones 1.2.1 y 1.2.4.

### Resultados de aprendizaje
- Definir ASCII y su rango básico.
- Relacionar caracteres con códigos numéricos.
- Identificar limitaciones de ASCII para idiomas y símbolos.
- Explicar por qué surgieron codificaciones más amplias.

### Desarrollo conceptual
ASCII (American Standard Code for Information Interchange) es un esquema de codificación de caracteres que asigna valores numéricos a letras inglesas básicas, dígitos, signos de puntuación y caracteres de control. El ASCII original usa 7 bits, con valores de 0 a 127.

Por ejemplo, `A` es 65 (41 hex), `a` es 97 (61 hex), `0` es 48 (30 hex). Los caracteres de control incluyen salto de línea, tabulación, etc.

ASCII fue fundamental, pero es limitado: no cubre adecuadamente acentos, eñes, alfabetos no latinos, emojis y muchos símbolos. Extensiones de 8 bits intentaron resolverlo parcialmente, pero generaron incompatibilidades. Por eso Unicode se convirtió en el enfoque moderno.

### Ejemplo técnico desarrollado
**Codificación de “Hi”:**

| Carácter | Decimal | Hex | Binario (7/8 bits) |
|---|---:|---:|---|
| H | 72 | 48 | 01001000 |
| i | 105 | 69 | 01101001 |

**Interpretación:** un texto simple se almacena como secuencia de códigos numéricos.

### Práctica guiada
- **Objetivo:** codificar y decodificar ASCII básico.
- **Procedimiento:** codifica “ABC” y decodifica 67, 111, 100, 101.
- **Resultado esperado:** ABC = 65,66,67; 67,111,100,101 = “Code”.
- **Verificación:** usar tabla ASCII confiable.

### Actividad independiente
Explica por qué ASCII no es suficiente para representar correctamente “canción”, “José” o “привет”.

### Criterios de aceptación
- Define ASCII correctamente.
- Codifica/decodifica ejemplos simples.
- Explica limitaciones con ejemplos reales.

### Errores frecuentes y recomendaciones
- **Error:** creer que ASCII cubre todos los idiomas. **Recomendación:** distinguir ASCII de Unicode.
- **Error:** confundir código ASCII con fuente/tipografía. **Recomendación:** separar codificación de representación visual.
- **Error:** asumir que un byte siempre es un carácter en cualquier codificación. **Recomendación:** esperar hasta UTF-8 para matizar.

### Evaluación de comprensión
1. ¿Qué rango cubre ASCII de 7 bits?
2. ¿Por qué ASCII es insuficiente para texto multilingüe?
3. ¿Qué representa el número 65 en ASCII?

### Referencias
- IANA. *Character Sets*. https://www.iana.org/assignments/character-sets/character-sets.xhtml. Consultado: 2026-11-24.
- The Unicode Consortium. *Unicode and ASCII*. https://www.unicode.org/standard/translations/es.html (referencia de apoyo; verificar sección aplicable). Consultado: 2026-11-24.

---

## Lección 1.2.6 — Unicode

### Identificación
- **Etapa:** 1 · **Módulo:** 1.2 · **Lección oficial:** 1.2.6 — Unicode.
- **Secuencia:** 6 de 9.

### Propósito de aprendizaje
Comprender Unicode como estándar universal de identificación de caracteres.

### Conocimientos previos
- Lección 1.2.5.

### Resultados de aprendizaje
- Definir Unicode y punto de código.
- Distinguir carácter, punto de código y codificación.
- Explicar por qué Unicode facilita interoperabilidad.
- Reconocer que Unicode no es lo mismo que UTF-8.

### Desarrollo conceptual
Unicode es un estándar que asigna un identificador único, llamado **punto de código**, a caracteres y símbolos de múltiples sistemas de escritura. Los puntos de código se escriben como `U+` seguido de un valor hexadecimal, por ejemplo `U+0041` para `A`, `U+00F1` para `ñ`.

Unicode busca cubrir textos de distintas lenguas y símbolos comunes, permitiendo que sistemas intercambien texto de forma consistente. Sin embargo, Unicode define el repertorio y propiedades; no especifica por sí solo cómo se almacenan los bytes en un archivo. Eso lo hacen codificaciones como UTF-8, UTF-16 y UTF-32.

También es importante distinguir entre carácter percibido por el usuario y punto de código. Algunos grafemas pueden representarse con combinaciones de puntos de código.

### Ejemplo técnico desarrollado
**Ejemplo:** “canción”

- `c` = U+0063
- `a` = U+0061
- `n` = U+006E
- `c` = U+0063
- `i` = U+0069
- `ó` = U+00F3
- `n` = U+006E

**Interpretación:** Unicode identifica cada carácter; la codificación decidirá cuántos bytes usar.

### Práctica guiada
- **Objetivo:** identificar puntos de código.
- **Procedimiento:** busca los puntos de código para `A`, `ñ`, `€`, `Ω`.
- **Resultado esperado:** U+0041, U+00F1, U+20AC, U+03A9.
- **Verificación:** consultar tabla Unicode oficial.

### Actividad independiente
Explica la diferencia entre “soportar Unicode” y “guardar en UTF-8”.

### Criterios de aceptación
- Define punto de código.
- Distingue Unicode de codificación.
- Usa ejemplos correctos.

### Errores frecuentes y recomendaciones
- **Error:** decir “archivo Unicode” sin especificar codificación. **Recomendación:** indicar UTF-8/UTF-16/UTF-32.
- **Error:** asumir que todo carácter visible es un solo punto de código. **Recomendación:** mencionar grafemas combinados.
- **Error:** confundir Unicode con fuente. **Recomendación:** fuente renderiza; Unicode identifica.

### Evaluación de comprensión
1. ¿Qué es un punto de código?
2. ¿Por qué Unicode no es lo mismo que UTF-8?
3. ¿Qué problema resuelve Unicode frente a ASCII?

### Referencias
- Unicode Consortium. *The Unicode Standard*. https://www.unicode.org/standard/standard.html. Consultado: 2026-11-24.
- Unicode Consortium. *Glossary of Unicode Terms*. https://www.unicode.org/glossary/. Consultado: 2026-11-24.

---

## Lección 1.2.7 — UTF-8

### Identificación
- **Etapa:** 1 · **Módulo:** 1.2 · **Lección oficial:** 1.2.7 — UTF-8.
- **Secuencia:** 7 de 9.

### Propósito de aprendizaje
Comprender UTF-8 como codificación de Unicode ampliamente usada en sistemas y web.

### Conocimientos previos
- Lecciones 1.2.5 y 1.2.6.

### Resultados de aprendizaje
- Definir UTF-8.
- Explicar codificación de longitud variable.
- Reconocer compatibilidad con ASCII.
- Interpretar implicaciones prácticas de UTF-8 en archivos y APIs.

### Desarrollo conceptual
UTF-8 es una codificación de Unicode de longitud variable. Representa puntos de código usando 1 a 4 bytes. Los caracteres ASCII (U+0000 a U+007F) se codifican en 1 byte con el mismo valor, lo que da compatibilidad con ASCII.

Esta propiedad hizo a UTF-8 muy popular en web, sistemas operativos, protocolos y archivos de texto. Sin embargo, longitud variable implica que el número de bytes no siempre es igual al número de caracteres percibidos. Operaciones como “cortar el string en el byte 10” pueden romper caracteres si no se hace con cuidado.

UTF-8 también evita ciertos problemas de orden de bytes (endianness) que pueden aparecer en UTF-16/UTF-32, aunque puede existir BOM en algunos contextos; su uso no siempre es recomendable.

### Ejemplo técnico desarrollado
**Codificación UTF-8:**

| Carácter | Punto de código | Bytes UTF-8 (hex) |
|---|---|---|
| A | U+0041 | 41 |
| ñ | U+00F1 | C3 B1 |
| € | U+20AC | E2 82 AC |

**Interpretación:** “Año€” tiene 4 caracteres visibles, pero ocupa 7 bytes en UTF-8.

### Práctica guiada
- **Objetivo:** observar longitud en bytes.
- **Procedimiento:** en Python, ejecuta: `len('Año€'.encode('utf-8'))` y `len('Año€')`.
- **Resultado esperado:** bytes mayor que número de caracteres.
- **Verificación:** comparar salida.

### Actividad independiente
Explica por qué un sistema que asume “1 carácter = 1 byte” puede fallar con UTF-8.

### Criterios de aceptación
- Define UTF-8 correctamente.
- Explica longitud variable y compatibilidad ASCII.
- Muestra ejemplo con bytes.
- Identifica una implicación práctica.

### Errores frecuentes y recomendaciones
- **Error:** confundir UTF-8 con Unicode. **Recomendación:** Unicode es estándar; UTF-8 es codificación.
- **Error:** cortar bytes sin considerar límites de caracteres. **Recomendación:** usar funciones de texto conscientes de codificación.
- **Error:** guardar/leer con codificaciones distintas. **Recomendación:** declarar UTF-8 explícitamente.

### Evaluación de comprensión
1. ¿Cuántos bytes puede usar UTF-8 para un punto de código?
2. ¿Por qué UTF-8 es compatible con ASCII?
3. ¿Qué problema práctico causa la longitud variable?

### Referencias
- RFC 3629. *UTF-8, a transformation format of ISO 10646*. https://www.rfc-editor.org/rfc/rfc3629. Consultado: 2026-11-24.
- Unicode Consortium. *UTF-8, UTF-16, UTF-32 & BOM*. https://www.unicode.org/faq/utf_bom.html. Consultado: 2026-11-24.

---

## Lección 1.2.8 — Representación de enteros

### Identificación
- **Etapa:** 1 · **Módulo:** 1.2 · **Lección oficial:** 1.2.8 — Representación de enteros.
- **Secuencia:** 8 de 9.

### Propósito de aprendizaje
Comprender cómo se representan enteros con y sin signo en memoria.

### Conocimientos previos
- Lecciones 1.2.1 y 1.2.4.

### Resultados de aprendizaje
- Diferenciar enteros con signo y sin signo.
- Explicar complemento a dos a nivel básico.
- Calcular rangos según número de bits.
- Identificar overflow/underflow.

### Desarrollo conceptual
Un entero sin signo usa todos los bits para representar valores no negativos. Con *n* bits, el rango es `0` a `2^n - 1`. Por ejemplo, 8 bits sin signo: 0 a 255.

Un entero con signo necesita representar negativos. La representación más común es **complemento a dos**. Con *n* bits, el rango es `-2^(n-1)` a `2^(n-1)-1`. Para 8 bits: -128 a 127.

En complemento a dos, el bit más significativo indica signo en la interpretación, pero la operación se realiza con aritmética binaria consistente. Para obtener el negativo de un número: invertir bits y sumar 1 (dentro del ancho de bits).

El **overflow** ocurre cuando un resultado no cabe en el rango representable. Su comportamiento depende del lenguaje/hardware: puede envolver, lanzar excepción, producir comportamiento indefinido o saturar.

### Ejemplo técnico desarrollado
**8 bits complemento a dos: +5 y -5**

- +5 = `00000101`
- invertir bits: `11111010`
- sumar 1: `11111011` = -5

**Rango 8 bits con signo:** -128 a 127. Si sumas `127 + 1` en un entero de 8 bits con signo, hay overflow.

### Práctica guiada
- **Objetivo:** calcular rangos.
- **Procedimiento:** calcula rango de 4 bits sin signo, 4 bits con signo, 16 bits sin signo.
- **Resultado esperado:** 0–15; -8–7; 0–65535.
- **Verificación:** aplicar fórmulas.

### Actividad independiente
Explica un caso real donde elegir entero sin signo sea riesgoso (por ejemplo, restas que pueden dar negativo).

### Criterios de aceptación
- Calcula rangos correctamente.
- Explica complemento a dos.
- Identifica overflow.

### Errores frecuentes y recomendaciones
- **Error:** creer que con signo solo “agrega un signo” sin cambiar rango. **Recomendación:** usar fórmulas de rango.
- **Error:** ignorar ancho de bits. **Recomendación:** siempre preguntar cuántos bits.
- **Error:** asumir que overflow se comporta igual en todos los lenguajes. **Recomendación:** verificar semántica del lenguaje.

### Evaluación de comprensión
1. ¿Cuál es el rango de 8 bits sin signo?
2. ¿Cómo se obtiene -3 en complemento a dos de 8 bits?
3. ¿Por qué el overflow es peligroso?

### Referencias
- Intel. *Intel® 64 and IA-32 Architectures Software Developer Manuals*. https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html. Consultado: 2026-11-24.
- Bryant, R. E., & O'Hallaron, D. R. *Computer Systems: A Programmer's Perspective*. Pearson.

---

## Lección 1.2.9 — Números de punto flotante

### Identificación
- **Etapa:** 1 · **Módulo:** 1.2 · **Lección oficial:** 1.2.9 — Números de punto flotante.
- **Secuencia:** 9 de 9.

### Propósito de aprendizaje
Comprender la representación aproximada de números reales en computadores y sus implicaciones.

### Conocimientos previos
- Lecciones 1.2.1, 1.2.4, 1.2.8.

### Resultados de aprendizaje
- Explicar por qué muchos decimales no se representan exactamente en binario.
- Describir los componentes básicos de punto flotante (signo, exponente, mantisa/significando).
- Reconocer errores de precisión, redondeo y comparación.
- Aplicar buenas prácticas básicas al comparar valores flotantes.

### Desarrollo conceptual
Los números de punto flotante representan valores reales de forma aproximada usando una estructura similar a notación científica: signo, significando/mantisa y exponente. El estándar IEEE 754 define formatos comunes como binary32 (float) y binary64 (double).

Muchos valores decimales finitos, como 0.1, no tienen representación binaria finita exacta. Por eso, en binario se almacenan aproximaciones. Esto puede producir resultados como `0.1 + 0.2 != 0.3` en ciertos lenguajes.

Los errores de punto flotante no son “bugs” del lenguaje, sino consecuencia de representar un conjunto infinito de reales con un número finito de bits. Para cálculos financieros, a menudo se usan enteros en centavos o tipos decimales. Para comparaciones, se usa tolerancia (epsilon) adecuada al dominio.

### Ejemplo técnico desarrollado
**Python:**

```python
a = 0.1 + 0.2
print(a)            # 0.30000000000000004
print(a == 0.3)     # False
epsilon = 1e-9
print(abs(a - 0.3) < epsilon)  # True
```

**Interpretación:** la representación interna es binaria aproximada; la comparación debe considerar tolerancia cuando corresponda.

### Práctica guiada
- **Objetivo:** observar aproximación.
- **Procedimiento:** ejecuta el ejemplo en Python o JavaScript. Prueba también `0.5 + 0.25`.
- **Resultado esperado:** 0.1+0.2 muestra aproximación; 0.5+0.25 es exacto en binario.
- **Verificación:** explicar por qué 0.5 y 0.25 sí son exactos (potencias negativas de 2).

### Actividad independiente
Diseña una regla para comparar precios en una aplicación: ¿usarías float, decimal o enteros en centavos? Justifica.

### Criterios de aceptación
- Explica causa de la aproximación.
- Diferencia valor decimal humano y representación binaria.
- Aplica comparación con tolerancia o alternativa adecuada.
- Justifica decisión para datos monetarios.

### Errores frecuentes y recomendaciones
- **Error:** comparar floats con `==` sin considerar precisión. **Recomendación:** usar tolerancia o tipos adecuados.
- **Error:** usar float para dinero. **Recomendación:** usar enteros/decimal según dominio.
- **Error:** creer que double “elimina” el problema. **Recomendación:** reduce error, no lo elimina conceptualmente.

### Evaluación de comprensión
1. ¿Por qué 0.1+0.2 puede no ser exactamente 0.3?
2. ¿Qué componentes tiene un número de punto flotante?
3. ¿Qué alternativa usarías para valores monetarios?

### Referencias
- IEEE. *IEEE 754-2019 Standard for Floating-Point Arithmetic*. https://standards.ieee.org/ieee/754/6210/. Consultado: 2026-11-24.
- Goldberg, D. *What Every Computer Scientist Should Know About Floating-Point Arithmetic*. ACM Computing Surveys, 1991. https://dl.acm.org/doi/10.1145/103162.103163. Consultado: 2026-11-24.
- Python Docs. *Floating Point Arithmetic: Issues and Limitations*. https://docs.python.org/3/tutorial/floatingpoint.html. Consultado: 2026-11-24.

---

## Cierre del módulo

### Evaluación integradora
1. Convierte 156 decimal a binario y hexadecimal.
2. Explica la diferencia entre Unicode y UTF-8.
3. Calcula el rango de un entero con signo de 16 bits.
4. Justifica por qué no usar float para dinero.

### Criterio de aprobación del módulo
El estudiante responde correctamente al menos 75% de la evaluación y puede demostrar conversiones y explicaciones sin depender de memoria mecánica.