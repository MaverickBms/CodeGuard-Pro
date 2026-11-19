# Etapa 8 — Redes informáticas y protocolos de comunicación

**Estado:** borrador didáctico v0.1.0.  
**Alineación:** ASCENSO 3.1, Etapa 8.  
**Prioridad oficial:** P1 · Obligatoria.  
**Objetivo oficial:** comprender cómo se comunican los computadores y cómo funciona Internet.

## Temario oficial

### 8.1. Fundamentos de redes
Redes LAN, WAN y MAN; Internet, Intranet y Extranet; cliente-servidor; peer-to-peer; router; switch; firewall; gateway; access point.

### 8.2. Modelos de comunicación
Modelo OSI y sus siete capas; modelo TCP/IP; encapsulamiento y desencapsulamiento; paquetes; tramas; segmentos; MTU.

### 8.3. Direccionamiento
Dirección MAC; IPv4 e IPv6; IP pública y privada; máscaras; subnetting; CIDR; VLSM; gateway; broadcast; ARP; DHCP.

### 8.4. Protocolos
TCP, UDP, ICMP, DNS, HTTP, HTTPS, SSH, FTP, SFTP, SMTP, IMAP, POP3, SMB, LDAP, Kerberos y WebSockets.

### 8.5. Routing y Switching
Switching; routing; tablas de rutas; rutas estáticas y dinámicas; NAT; VLAN; trunking; segmentación; subredes.

### 8.6. Seguridad de redes
Firewalls; VPN; DMZ; ACL; segmentación; puertos abiertos; servicios expuestos; superficie de ataque; filtrado de tráfico.

### 8.7. Herramientas
Wireshark; tcpdump; Nmap; ping; traceroute; ip; ss; netstat; dig; nslookup; curl.

**Proyecto oficial:** crear una red virtual con varias máquinas, configurar direcciones IP, probar conectividad y analizar paquetes con Wireshark.

---

## Resultados de aprendizaje

Podrás explicar las redes por alcance y arquitectura; describir el recorrido de datos mediante OSI y TCP/IP; interpretar direcciones MAC e IP; diseñar subredes con CIDR/VLSM; diferenciar protocolos y sus propósitos; leer tablas de rutas; configurar una red virtual aislada; aplicar controles básicos de segmentación y filtrado; y capturar tráfico de laboratorio para analizarlo.

## 8.1 — Fundamentos de redes

### ¿Qué es una red?

Una red conecta dispositivos para intercambiar datos y compartir servicios. Sus componentes pueden incluir interfaces, medios físicos o inalámbricos, switches, routers, puntos de acceso, firewalls y servidores.

Una red funcional requiere direccionamiento, mecanismos de entrega, protocolos compatibles y configuración coherente. Que dos equipos estén conectados físicamente no garantiza que puedan comunicarse a nivel IP o aplicación.

### LAN, MAN y WAN

- **LAN:** red de área local, normalmente limitada a una vivienda, oficina, laboratorio o edificio.
- **MAN:** red metropolitana que cubre una zona urbana o metropolitana.
- **WAN:** red de área amplia que conecta ubicaciones distantes.

Estas categorías describen alcance aproximado; no determinan por sí solas la tecnología o velocidad.

### Internet, Intranet y Extranet

Internet es una red global de redes interconectadas que utiliza la suite TCP/IP. Una intranet es un entorno privado de información y servicios para una organización. Una extranet habilita acceso controlado a determinados recursos para entidades externas autorizadas.

No confundas Internet con la Web: la Web es uno de los servicios que funcionan sobre Internet.

### Cliente-servidor y peer-to-peer

En cliente-servidor, un cliente solicita un servicio a un servidor que atiende peticiones. En peer-to-peer, los participantes pueden actuar como pares y compartir recursos directamente. Los sistemas reales pueden combinar ambos modelos.

### Router, switch, firewall, gateway y access point

- **Switch:** conecta dispositivos en una red local y reenvía tramas según direcciones MAC.
- **Router:** interconecta redes IP y reenvía paquetes según tablas de rutas.
- **Firewall:** aplica reglas para permitir o bloquear tráfico.
- **Gateway:** punto de salida o intermediación hacia otra red o sistema; en una LAN, el gateway predeterminado suele ser un router.
- **Access Point:** proporciona conectividad inalámbrica a una red.

Un mismo equipo doméstico puede integrar router, switch, firewall y punto de acceso, aunque sean funciones diferentes.

## 8.2 — Modelos de comunicación

### Modelo OSI

El modelo OSI organiza conceptualmente la comunicación en siete capas:

| Capa | Nombre | Función orientativa |
|---:|---|---|
| 7 | Aplicación | servicios de red utilizados por aplicaciones |
| 6 | Presentación | representación, codificación y transformaciones |
| 5 | Sesión | establecimiento y gestión de diálogos |
| 4 | Transporte | comunicación extremo a extremo, puertos y control |
| 3 | Red | direccionamiento lógico y encaminamiento |
| 2 | Enlace de datos | tramas y entrega en el enlace local |
| 1 | Física | transmisión de señales por el medio |

El modelo es una herramienta conceptual. Las implementaciones y protocolos reales no siempre encajan perfectamente en una sola capa.

### Modelo TCP/IP

El modelo TCP/IP suele describirse en cuatro capas: aplicación, transporte, Internet y acceso a red. Algunas fuentes separan enlace y física y presentan cinco capas. Explica siempre qué convención estás utilizando.

Relación aproximada:
- aplicación TCP/IP: agrupa funciones de aplicación, presentación y sesión de OSI;
- transporte: TCP y UDP;
- Internet: IP e ICMP;
- acceso a red: tecnologías de enlace y transmisión.

### Encapsulamiento y desencapsulamiento

Al enviar datos, cada capa agrega información de control (cabeceras y, según protocolo, tráileres). El receptor procesa la información en sentido inverso y retira las cabeceras correspondientes.

Nombres habituales de unidades:
- datos de aplicación;
- segmento TCP o datagrama UDP;
- paquete IP;
- trama de enlace;
- bits/señales en el medio.

No uses «paquete», «trama» y «segmento» como sinónimos cuando describas capas distintas.

### MTU

La MTU es el tamaño máximo de unidad de datos que puede transportarse en un enlace sin fragmentación a ese nivel. La MTU depende de la tecnología y configuración. En Ethernet convencional suele utilizarse una MTU IP de 1500 bytes, pero no asumas que todas las rutas o redes tienen el mismo valor.

Una MTU inconsistente puede causar problemas de conectividad, especialmente cuando la detección de MTU de ruta o los mensajes ICMP necesarios están bloqueados.

## 8.3 — Direccionamiento

### Dirección MAC

Una dirección MAC identifica una interfaz en el contexto de tecnologías de enlace como Ethernet. Tiene un formato definido por la tecnología y puede ser modificada o aleatorizada por software en ciertos escenarios. No es una identidad personal ni garantiza por sí sola autenticidad.

### IPv4 e IPv6

IPv4 utiliza direcciones de 32 bits, representadas normalmente en decimal punteado. IPv6 utiliza 128 bits y una representación hexadecimal abreviada. IPv6 no es simplemente «IPv4 más larga»: incorpora mecanismos y consideraciones diferentes de configuración y operación.

### IP pública y privada

Las direcciones privadas IPv4 se reservan para redes internas y no se enrutan globalmente en Internet. Una IP pública es globalmente enrutable, aunque el acceso real depende de políticas y filtros. IPv6 también dispone de rangos de uso local y direcciones globales.

No publiques la dirección real de tu hogar o laboratorio en capturas o documentación abierta. Sustituye datos sensibles por rangos de documentación reservados cuando prepares ejemplos.

### Máscaras, subnetting y CIDR

Una máscara indica qué bits de una dirección IPv4 corresponden al prefijo de red. CIDR representa el tamaño del prefijo mediante una barra, por ejemplo /24. Subnetting divide un bloque en redes más pequeñas.

Para IPv4, si un prefijo es /p, quedan 32-p bits de host. El número total de direcciones del bloque es 2^(32-p). En subredes tradicionales, las direcciones de red y broadcast no se asignan a hosts; hay excepciones de diseño como /31 para enlaces punto a punto y /32 para una sola dirección.

Ejemplo didáctico: 192.0.2.0/24 es un bloque reservado para documentación. Contiene 256 direcciones; en una subred convencional de hosts se reservan red y broadcast, dejando 254 direcciones utilizables.

### VLSM

VLSM permite utilizar máscaras de distinta longitud dentro de un plan de direccionamiento para asignar bloques según necesidades. Diseña primero las subredes más grandes y alinea cada bloque con su tamaño. Comprueba que no haya solapamientos y que cada rango quede dentro del bloque padre.

### Gateway y broadcast

El gateway predeterminado permite enviar tráfico a destinos que no pertenecen a la red local. Broadcast IPv4 dirige un paquete a todos los hosts de una subred broadcast. IPv6 no utiliza broadcast; emplea multicast y otros mecanismos.

### ARP y DHCP

ARP resuelve direcciones IPv4 de siguiente salto a direcciones de enlace en una LAN. No atraviesa routers como una solicitud broadcast normal.

DHCP asigna parámetros de red como dirección IP, máscara/prefijo, gateway y DNS mediante un proceso de concesión. Una dirección DHCP puede cambiar según la duración de concesión y la configuración del servidor.

## 8.4 — Protocolos

| Protocolo | Propósito | Consideración |
|---|---|---|
| TCP | transporte fiable y orientado a conexión | secuencia, retransmisión y control de flujo/congestión |
| UDP | transporte de datagramas sin conexión | no garantiza entrega ni orden |
| ICMP | mensajes de control y diagnóstico IP | ping utiliza mensajes ICMP en muchos entornos |
| DNS | resolución de nombres | puede utilizar UDP o TCP y otros transportes según el caso |
| HTTP | transferencia de recursos web | protocolo de aplicación |
| HTTPS | HTTP protegido mediante TLS | protege confidencialidad e integridad del canal si se valida correctamente |
| SSH | acceso remoto seguro y túneles | verifica identidad del servidor y protege credenciales |
| FTP | transferencia tradicional de archivos | no cifra credenciales ni datos por defecto |
| SFTP | transferencia de archivos sobre SSH | no es una variante cifrada de FTP; es un protocolo distinto |
| SMTP | envío y retransmisión de correo | no equivale a leer el buzón |
| IMAP | acceso y sincronización de buzones | conserva organización del correo en servidor según configuración |
| POP3 | recuperación de mensajes | modelo distinto de sincronización |
| SMB | compartición de archivos/recursos | restringe versiones y acceso según configuración segura |
| LDAP | acceso a servicios de directorio | requiere controles de autenticación y transporte |
| Kerberos | autenticación mediante tickets | depende de infraestructura y sincronización temporal |
| WebSockets | comunicación bidireccional persistente | comienza con un handshake HTTP en el uso web habitual |

Los puertos habituales pueden servir de referencia, pero no identifican de manera infalible un servicio: los administradores pueden configurar puertos diferentes y un puerto abierto no demuestra qué aplicación lo atiende.

### TCP y UDP

TCP establece una conexión lógica y ofrece entrega ordenada y fiable mediante secuencias, confirmaciones y retransmisiones. UDP envía datagramas sin establecer una conexión de transporte ni garantizar entrega u orden. UDP no es automáticamente más rápido en toda aplicación: el comportamiento depende del protocolo superior y de la red.

### DNS

DNS traduce nombres a registros como A, AAAA, MX, CNAME y otros. El proceso puede involucrar cachés, resolvers recursivos y servidores autoritativos. Una respuesta almacenada en caché puede no reflejar inmediatamente un cambio reciente debido a TTL.

### HTTP y HTTPS

HTTP define semántica de solicitudes y respuestas. HTTPS utiliza TLS para proteger el canal y autenticar el servidor mediante certificados validados. TLS no garantiza que el sitio sea honesto ni que el equipo cliente esté libre de malware: protege el transporte y la identidad criptográfica del extremo según la validación.

### SSH, FTP y SFTP

SSH proporciona un canal seguro para acceso remoto y otras funciones. Verifica la clave del servidor y utiliza autenticación configurada. FTP tradicional transmite datos y credenciales sin cifrado por defecto. SFTP es un protocolo de transferencia que funciona sobre SSH y no debe confundirse con FTPS.

### Correo y directorio

SMTP se utiliza para enviar/retransmitir correo; IMAP y POP3 permiten acceder a mensajes. LDAP consulta y administra información de directorio. Kerberos proporciona autenticación basada en tickets. En todos los casos deben protegerse credenciales, limitar privilegios y utilizar configuraciones actuales.

### WebSockets

WebSockets permite comunicación bidireccional sobre una conexión persistente. Debe protegerse el origen, autenticar usuarios, autorizar cada operación, validar mensajes y limitar recursos para evitar abusos.

## 8.5 — Routing y Switching

### Switching y tablas MAC

Un switch aprende direcciones MAC observando las tramas entrantes y asocia direcciones con puertos. Reenvía tramas según su tabla. Los broadcasts de capa 2 se propagan dentro del dominio de broadcast correspondiente, salvo segmentación.

### Routing y tablas de rutas

Un router consulta su tabla de rutas para determinar el siguiente salto o interfaz de salida. La selección suele considerar prefijo más específico y métricas/prioridades según el protocolo y sistema.

Las rutas estáticas son configuradas manualmente. Las dinámicas se aprenden mediante protocolos de routing. No confundas ruta predeterminada con una ruta hacia una red específica.

### NAT

NAT modifica información de direcciones y, en algunas variantes, puertos. Se utiliza comúnmente para permitir que varios dispositivos compartan una dirección IPv4 pública. NAT no es por sí solo un firewall ni una garantía de seguridad.

### VLAN, trunking y segmentación

Una VLAN crea un dominio lógico de capa 2 separado. Un enlace access suele transportar una VLAN; un trunk transporta varias VLAN mediante etiquetado, según la tecnología y configuración.

La segmentación separa sistemas para limitar movimiento lateral y reducir exposición. Requiere routing y reglas controladas cuando se necesita comunicación entre segmentos.

## 8.6 — Seguridad de redes

### Firewalls y ACL

Un firewall aplica políticas de tráfico según dirección, interfaz, origen, destino, protocolo, puerto, estado u otros atributos. Una ACL es una lista de reglas de control de acceso en un dispositivo o servicio. El orden y política predeterminada importan.

Diseña reglas con mínimo privilegio: permite solo flujos necesarios, limita orígenes y destinos, documenta propietario y propósito, y revisa reglas obsoletas.

### VPN y DMZ

Una VPN crea un canal protegido entre extremos o redes, según tecnología. No convierte automáticamente en confiable todo dispositivo conectado; se requiere autenticación, autorización, actualización y segmentación.

Una DMZ aloja servicios que necesitan cierta exposición, separándolos de redes internas sensibles. Debe limitarse el tráfico desde y hacia la DMZ y monitorearse su actividad.

### Puertos abiertos, servicios expuestos y superficie de ataque

Un puerto abierto indica que hay un servicio escuchando o una respuesta de red compatible, pero no prueba por sí solo vulnerabilidad. Cada servicio expuesto añade una posible vía de entrada y debe justificarse, actualizarse, autenticarse y monitorearse.

La superficie de ataque incluye servicios, interfaces, credenciales, configuraciones y rutas de acceso. Reducirla implica deshabilitar lo innecesario, limitar exposición y mantener inventario.

### Filtrado de tráfico

El filtrado puede aplicarse en host, router, firewall perimetral, nube o aplicación. Comprueba tráfico entrante y saliente. Evita reglas amplias como permitir todo desde cualquier origen cuando basta con permitir un flujo específico.

Toda prueba de escaneo o captura debe realizarse en redes propias o con autorización expresa. No escanees direcciones públicas de terceros.

## 8.7 — Herramientas

| Herramienta | Uso principal | Ejercicio seguro |
|---|---|---|
| Wireshark | captura y análisis visual de paquetes | analizar tráfico generado por tus VMs |
| tcpdump | captura desde terminal | filtrar tráfico de laboratorio |
| Nmap | descubrimiento y auditoría de servicios | escanear solo una VM propia autorizada |
| ping | comprobar respuesta ICMP | probar conectividad entre VMs |
| traceroute | observar saltos de una ruta | comparar rutas desde el laboratorio |
| ip | interfaces, direcciones y rutas Linux | consultar configuración local |
| ss | sockets y puertos | listar sockets del propio sistema |
| netstat | estadísticas y conexiones (herramienta heredada en algunos sistemas) | comparar con ss |
| dig | consultas DNS detalladas | consultar un dominio de prueba |
| nslookup | consulta DNS | comparar respuestas |
| curl | solicitudes a servicios y URLs | consultar un servidor de laboratorio |

La salida de las herramientas depende de permisos, sistema operativo, firewall y topología. Un ping fallido no demuestra necesariamente que el host esté apagado: ICMP puede estar filtrado.

### Wireshark y tcpdump

Una captura puede contener credenciales, cookies, tokens, nombres, direcciones y contenido privado. Captura solo el tráfico necesario, en una red autorizada, protege los archivos y redacta datos antes de compartirlos. HTTPS cifra el contenido de aplicación, pero metadatos de conexión pueden seguir visibles.

### Nmap

Nmap permite descubrir hosts y servicios. Es una herramienta de auditoría dual: puede ser útil para inventario autorizado y también invasiva si se usa contra terceros. En esta etapa, limita el objetivo a direcciones privadas de tus VMs y registra el alcance autorizado. No intentes evadir controles ni escanear redes ajenas.

## Proyecto oficial — Red virtual de varias máquinas

### Objetivo

Crear una red aislada con varias máquinas virtuales, configurar direccionamiento IP, probar conectividad y analizar paquetes con Wireshark.

### Diseño

1. Dibuja la topología: host, red virtual, VMs, interfaces y gateway.
2. Define si el laboratorio utilizará NAT, Host-only o una combinación controlada.
3. Reserva un bloque de documentación para ejemplos y define subredes sin solapamiento.
4. Asigna direcciones, prefijos, gateways y DNS.
5. Documenta direcciones MAC e IP ficticias o privadas del laboratorio; no publiques datos de la red doméstica.
6. Establece qué VM ofrecerá servicios de prueba y qué VM actuará como cliente.
7. Aplica firewall de mínimo privilegio.

### Ejecución

- Verifica interfaces y rutas en cada VM.
- Comprueba conectividad local y entre subredes cuando corresponda.
- Prueba resolución DNS.
- Realiza una solicitud HTTP/HTTPS a un servicio de laboratorio.
- Captura tráfico propio con Wireshark.
- Identifica tramas, paquetes, segmentos, puertos, DNS y handshake TCP.
- Compara un flujo TCP con uno UDP.
- Realiza un escaneo Nmap únicamente contra las VMs del laboratorio.
- Documenta reglas de firewall y confirma que los servicios no se exponen fuera del entorno.

### Entregables

1. diagrama de topología;
2. tabla de direccionamiento;
3. cálculo de subnetting/CIDR y justificación;
4. configuración de interfaces y rutas;
5. pruebas de ping, DNS y aplicación;
6. capturas Wireshark con filtros y anotaciones;
7. explicación de encapsulamiento en una comunicación observada;
8. inventario de puertos/servicios del laboratorio;
9. reglas de firewall/ACL;
10. análisis de riesgos y plan de aislamiento;
11. bitácora de errores y correcciones.

### Rúbrica (100 puntos)

| Criterio | Puntos |
|---|---:|
| Fundamentos y modelos de red | 15 |
| Direccionamiento y subnetting | 20 |
| Protocolos y diagnóstico | 15 |
| Routing, switching y VLAN | 15 |
| Seguridad, filtrado y segmentación | 15 |
| Captura y análisis de paquetes | 15 |
| Documentación y autorización del laboratorio | 5 |

## Ejercicios de comprensión

1. ¿Qué diferencia hay entre LAN y WAN?  
   **Respuesta:** describen alcances distintos; LAN es local y WAN conecta ubicaciones distantes.

2. ¿Qué diferencia hay entre switch y router?  
   **Respuesta:** el switch reenvía tramas en una red local; el router interconecta redes IP.

3. ¿Qué representa cada capa OSI?  
   **Respuesta:** desde transmisión física, enlace, red y transporte hasta sesión, presentación y aplicación.

4. ¿Qué diferencia hay entre segmento, paquete y trama?  
   **Respuesta:** son unidades de datos asociadas habitualmente a transporte, red y enlace.

5. ¿Cuántas direcciones contiene un bloque IPv4 /26?  
   **Respuesta:** 2^(32-26) = 64 direcciones totales; en una subred convencional quedan 62 direcciones de host.

6. ¿Qué diferencia hay entre TCP y UDP?  
   **Respuesta:** TCP ofrece transporte fiable y ordenado; UDP no garantiza entrega ni orden.

7. ¿Qué diferencia hay entre FTP y SFTP?  
   **Respuesta:** FTP tradicional no cifra por defecto; SFTP es un protocolo distinto que opera sobre SSH.

8. ¿NAT es un firewall?  
   **Respuesta:** no; puede modificar direcciones/puertos, pero no sustituye una política de filtrado.

9. ¿Qué es una DMZ?  
   **Respuesta:** segmento separado para servicios que requieren exposición controlada.

10. ¿Qué debes hacer antes de usar Nmap?  
    **Respuesta:** confirmar autorización y limitar el alcance a sistemas propios o expresamente autorizados.

## Autoevaluación práctica

Debes poder explicar una captura real de tu laboratorio: identificar la comunicación, direcciones origen/destino, protocolo, puertos, encapsulamiento y resultado. También debes calcular una subred, justificar gateway y reglas de filtrado y demostrar que la red virtual no expone servicios accidentalmente.

## Recursos audiovisuales

No se incluyen videos en esta versión. La etapa contiene direccionamiento, protocolos, routing, switching, seguridad y herramientas de captura; se añadirán recursos por subtema solo cuando se confirme audio hablado en español y correspondencia técnica directa. No se recomendarán demostraciones de escaneo contra objetivos ajenos.

## Referencias oficiales y técnicas

- IETF RFC Editor: https://www.rfc-editor.org/
- RFC 791 — Internet Protocol: https://www.rfc-editor.org/rfc/rfc791
- RFC 8200 — Internet Protocol, Version 6: https://www.rfc-editor.org/rfc/rfc8200
- RFC 9293 — Transmission Control Protocol: https://www.rfc-editor.org/rfc/rfc9293
- RFC 768 — User Datagram Protocol: https://www.rfc-editor.org/rfc/rfc768
- RFC 1034 y RFC 1035 — Domain Names: https://www.rfc-editor.org/
- Wireshark User's Guide: https://www.wireshark.org/docs/wsug_html_chunked/
- Nmap Reference Guide: https://nmap.org/book/man.html
- tcpdump documentation: https://www.tcpdump.org/manpages/tcpdump.1.html
- Cloudflare Learning Center (material de consulta general): https://www.cloudflare.com/learning/
- Cisco Networking Basics (material de consulta del fabricante): https://www.cisco.com/

**Consulta de fuentes:** 2026-11-19.  
**Verificación práctica:** topología, comandos y laboratorio propuestos; no ejecutados ni capturados en VMs durante esta sesión.  
**Estado editorial:** borrador.
