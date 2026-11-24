# Etapa 3 · Módulo 3.6 — Archivos

**Estado:** borrador académico desarrollado (pendiente validación editorial/técnica y ejecución).  
**Alineación:** ASCENSO 3.1, Etapa 3, Módulo 3.6. **Última actualización:** 2026-11-24

## Identificación
- **Módulo:** 3.6 — Archivos. **Lecciones oficiales:** 6 (3.6.1 a 3.6.6).
- **Prerrequisitos:** Módulos 3.4, 3.5.

## Propósito
Leer, escribir y gestionar archivos y directorios con Java NIO.

---

## Lección 3.6.1 — Lectura
- **Lección oficial:** 3.6.1 — Lectura. **Secuencia:** 1/6.
- **Propósito:** leer contenido de archivos de forma segura.
- **Prerrequisitos:** 3.4.5, 3.5.5.
- **Resultados:** leer archivos con `Files.readString/readAllLines/BufferedReader`, manejar IOException.
- **Desarrollo:** Java NIO (`java.nio.file`) facilita lectura. `Files.readString(Path)` para archivos pequeños; `BufferedReader` para grandes/streaming.
```java
Path p = Path.of("datos.txt");
String contenido = Files.readString(p);
List<String> lineas = Files.readAllLines(p);
```
- **Práctica guiada:** leer un archivo de texto y contar líneas.
- **Actividad independiente:** leer CSV simple y mostrar registros.
- **Criterios:** maneja IOException, usa charset adecuado (UTF-8), no carga archivos enormes en memoria sin necesidad.
- **Errores:** ignorar encoding; no manejar archivo inexistente.
- **Evaluación:** ¿Cuándo usar BufferedReader en vez de readString?
- **Ref:** Oracle. *Reading, Writing, and Creating Files*. https://docs.oracle.com/javase/tutorial/essential/io/file.html (2026-11-24).

## Lección 3.6.2 — Escritura
- **Lección oficial:** 3.6.2 — Escritura. **Secuencia:** 2/6.
- **Propósito:** escribir datos en archivos.
- **Prerrequisitos:** 3.6.1.
- **Resultados:** escribir con `Files.writeString/write`, elegir modo overwrite/append.
- **Desarrollo:** `Files.writeString(path, texto)` sobrescribe por defecto. Para append: `StandardOpenOption.APPEND`. Siempre considerar permisos, ruta y encoding.
```java
Files.writeString(Path.of("salida.txt"), "Hola\n");
Files.writeString(Path.of("log.txt"), "evento\n", StandardOpenOption.CREATE, StandardOpenOption.APPEND);
```
- **Práctica guiada:** escribir lista de nombres en archivo.
- **Actividad independiente:** crear log simple que agregue líneas con timestamp.
- **Criterios:** modo correcto, manejo de errores, contenido verificable.
- **Errores:** sobrescribir sin querer; no cerrar recursos en APIs antiguas.
- **Evaluación:** ¿Qué diferencia hay entre overwrite y append?
- **Ref:** Oracle. *File I/O*. https://docs.oracle.com/javase/tutorial/essential/io/file.html (2026-11-24).

## Lección 3.6.3 — Directorios
- **Lección oficial:** 3.6.3 — Directorios. **Secuencia:** 3/6.
- **Propósito:** crear, listar y gestionar directorios.
- **Prerrequisitos:** 3.6.1.
- **Resultados:** crear directorios, listar contenido, verificar existencia.
- **Desarrollo:** `Files.createDirectories`, `Files.list`, `Files.walk`, `Files.exists/isDirectory`. Al listar, manejar streams y cerrar recursos.
```java
Path dir = Path.of("datos/reportes");
Files.createDirectories(dir);
try (var s = Files.list(Path.of("datos"))) {
    s.forEach(System.out::println);
}
```
- **Práctica guiada:** crear estructura de carpetas para un proyecto.
- **Actividad independiente:** listar archivos `.txt` en un directorio.
- **Criterios:** usa createDirectories, maneja recursos, verifica existencia.
- **Errores:** asumir que el directorio existe; no cerrar stream de `Files.list`.
- **Evaluación:** ¿Diferencia entre `createDirectory` y `createDirectories`?
- **Ref:** Oracle. *Creating and Reading Directories*. https://docs.oracle.com/javase/tutorial/essential/io/dirs.html (2026-11-24).

## Lección 3.6.4 — Paths
- **Lección oficial:** 3.6.4 — Paths. **Secuencia:** 4/6.
- **Propósito:** manipular rutas de forma portable y segura.
- **Prerrequisitos:** 3.6.3.
- **Resultados:** usar `Path`/`Paths`, resolver, normalizar y obtener nombres.
- **Desarrollo:** `Path` representa rutas independiente del SO. `resolve`, `normalize`, `getFileName`, `toAbsolutePath`. Evitar concatenar rutas con strings.
```java
Path base = Path.of("data");
Path archivo = base.resolve("in/report.csv");
System.out.println(archivo.normalize());
```
- **Práctica guiada:** construir rutas a partir de base + nombre de archivo.
- **Actividad independiente:** normalizar una ruta con `..` y explicar el resultado.
- **Criterios:** no concatena strings para rutas, usa Path.
- **Errores:** hardcodear separadores `/` o `\`; path traversal no validado.
- **Evaluación:** ¿Por qué `Path` es mejor que concatenar strings?
- **Ref:** Oracle. *Path Operations*. https://docs.oracle.com/javase/tutorial/essential/io/pathOps.html (2026-11-24).

## Lección 3.6.5 — Archivos de texto
- **Lección oficial:** 3.6.5 — Archivos de texto. **Secuencia:** 5/6.
- **Propósito:** trabajar con archivos de texto estructurados y no estructurados.
- **Prerrequisitos:** 3.6.1, 3.6.2.
- **Resultados:** leer/escribir texto, manejar encoding, procesar línea a línea.
- **Desarrollo:** archivos de texto deben tener encoding definido (UTF-8 recomendado). Para CSV/TSV simples, parsear con cuidado; para formatos complejos usar librerías. Manejar líneas vacías y finales de línea.
```java
List<String> lineas = Files.readAllLines(Path.of("notas.txt"), StandardCharsets.UTF_8);
for (String l : lineas) {
    if (!l.isBlank()) System.out.println(l.trim());
}
```
- **Práctica guiada:** leer archivo y generar otro con líneas numeradas.
- **Actividad independiente:** procesar un CSV simple y calcular un total.
- **Criterios:** encoding explícito, manejo de líneas vacías.
- **Errores:** asumir ASCII; ignorar BOM o encoding mixto.
- **Evaluación:** ¿Por qué especificar UTF-8 explícitamente?
- **Ref:** Oracle. *File I/O*. https://docs.oracle.com/javase/tutorial/essential/io/file.html (2026-11-24).

## Lección 3.6.6 — Serialización básica
- **Lección oficial:** 3.6.6 — Serialización básica. **Secuencia:** 6/6.
- **Propósito:** comprender la serialización y sus riesgos básicos.
- **Prerrequisitos:** 3.6.1, 3.6.2.
- **Resultados:** explicar serialización, usar `Serializable` a nivel básico, reconocer riesgos.
- **Desarrollo:** serialización convierte un objeto en bytes para almacenarlo/transmitirlo. Java ofrece serialización nativa con `Serializable`, pero tiene riesgos de seguridad al deserializar datos no confiables. Para datos de intercambio, preferir JSON/formatos explícitos.
```java
class Usuario implements Serializable {
    private static final long serialVersionUID = 1L;
    String nombre;
}
```
- **Práctica guiada:** serializar y deserializar un objeto simple en archivo local controlado.
- **Actividad independiente:** explicar por qué no deserializar datos no confiables.
- **Criterios:** entiende concepto, reconoce riesgo, no usa en datos no confiables.
- **Errores:** deserializar entrada no confiable; usar serialización Java para APIs públicas.
- **Evaluación:** ¿Qué riesgo tiene la deserialización de datos no confiables?
- **Ref:** Oracle. *Java Object Serialization*. https://docs.oracle.com/en/java/javase/21/docs/specs/serialization/index.html (2026-11-24). OWASP. *Deserialization Cheat Sheet*. https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html (2026-11-24).