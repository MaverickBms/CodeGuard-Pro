# Etapa 8 — Redes informáticas y protocolos de comunicación

**Estado de trabajo:** BASE DE TRABAJO ACTIVA · v0.1.0.  
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

### 8.1.1 — Redes LAN

Conecta dispositivos en un área local como vivienda, oficina o laboratorio.

### 8.1.2 — Redes WAN

Conecta redes o ubicaciones geográficamente distantes.

### 8.1.3 — Redes MAN

Cubre una zona metropolitana. Estas categorías describen alcance aproximado, no una tecnología única.

### 8.1.4 — Internet

Red global de redes interconectadas que utiliza TCP/IP; no es sinónimo de Web.

### 8.1.5 — Intranet

Entorno privado de información y servicios para una organización.

### 8.1.6 — Extranet

Acceso controlado a recursos para entidades externas autorizadas.

### 8.1.7 — Cliente-servidor

Un cliente solicita un servicio a un servidor.

### 8.1.8 — Peer-to-peer

Los participantes pueden actuar como pares y compartir recursos directamente.

### 8.1.9 — Router

Interconecta redes IP y reenvía paquetes según tablas de rutas.

### 8.1.10 — Switch

Conecta dispositivos locales y reenvía tramas según direcciones MAC.

### 8.1.11 — Firewall

Aplica reglas para permitir o bloquear tráfico.

### 8.1.12 — Gateway

Punto de salida o intermediación hacia otra red; el gateway predeterminado suele ser un router.

### 8.1.13 — Access Point

Proporciona conectividad inalámbrica a una red.

## 8.2 — Modelos de comunicación

### 8.2.1 — Modelo OSI

Modelo conceptual que organiza funciones de comunicación en siete capas.

### 8.2.2 — Las siete capas OSI

| Capa | Nombre | Función |
|---:|---|---|
| 7 | Aplicación | servicios de red |
| 6 | Presentación | representación y codificación |
| 5 | Sesión | gestión de diálogos |
| 4 | Transporte | puertos y control extremo a extremo |
| 3 | Red | direccionamiento y routing |
| 2 | Enlace | tramas y entrega local |
| 1 | Física | señales y medio |

### 8.2.3 — Modelo TCP/IP

El modelo TCP/IP suele describirse en cuatro capas: aplicación, transporte, Internet y acceso a red. Algunas fuentes separan enlace y física y presentan cinco capas. Explica siempre qué convención estás utilizando.

Relación aproximada:
- aplicación TCP/IP: agrupa funciones de aplicación, presentación y sesión de OSI;
- transporte: TCP y UDP;
- Internet: IP e ICMP;
- acceso a red: tecnologías de enlace y transmisión.

### 8.2.4 — Encapsulamiento

Cada capa agrega información de control, como cabeceras y tráileres.

### 8.2.5 — Desencapsulamiento

El receptor procesa la información en sentido inverso y retira las cabeceras.

### 8.2.6 — Paquetes

Un paquete IP transporta información de capa de red, con direcciones origen/destino y campos de control.

### 8.2.7 — Tramas

Una trama transporta datos en un enlace local e incluye información propia de la tecnología de enlace.

### 8.2.8 — Segmentos

Un segmento TCP es una unidad de datos de transporte; UDP utiliza datagramas, no segmentos TCP.

### 8.2.9 — MTU

La MTU es el tamaño máximo de unidad de datos que puede transportarse en un enlace sin fragmentación a ese nivel. La MTU depende de la tecnología y configuración. En Ethernet convencional suele utilizarse una MTU IP de 1500 bytes, pero no asumas que todas las rutas o redes tienen el mismo valor.

Una MTU inconsistente puede causar problemas de conectividad, especialmente cuando la detección de MTU de ruta o los mensajes ICMP necesarios están bloqueados.

## 8.3 — Direccionamiento

### 8.3.1 — Dirección MAC

Identifica una interfaz en tecnologías de enlace como Ethernet; puede modificarse por software y no garantiza autenticidad.

### 8.3.2 — IPv4

Utiliza direcciones de 32 bits, representadas normalmente en decimal punteado.

### 8.3.3 — IPv6

Utiliza direcciones de 128 bits y representación hexadecimal abreviada.

### 8.3.4 — IP pública

Es globalmente enrutable, aunque el acceso depende de políticas y filtros. No publiques direcciones reales.

### 8.3.5 — IP privada

Los rangos privados IPv4 se reservan para redes internas y no se enrutan globalmente.

### 8.3.6 — Máscaras

Indican qué bits de IPv4 corresponden al prefijo de red.

### 8.3.7 — Subnetting

Divide un bloque en redes menores. Un prefijo /p deja 32-p bits de host.

### 8.3.8 — CIDR

Representa el prefijo con una barra, por ejemplo /24. 192.0.2.0/24 contiene 256 direcciones totales.

### 8.3.9 — VLSM

Permite utilizar máscaras de distinta longitud; asigna bloques mayores primero y comprueba solapamientos.

### 8.3.10 — Gateway

Permite enviar tráfico a destinos fuera de la red local.

### 8.3.11 — Broadcast

IPv4 broadcast dirige paquetes a todos los hosts del dominio; IPv6 utiliza multicast, no broadcast.

### 8.3.12 — ARP

Resuelve direcciones IPv4 de siguiente salto a direcciones de enlace en la LAN.

### 8.3.13 — DHCP

Asigna parámetros como IP, prefijo, gateway y DNS mediante concesiones.

## 8.4 — Protocolos

### 8.4.1 — TCP

Transporte fiable y orientado a conexión con secuencias, confirmaciones y retransmisiones.

### 8.4.2 — UDP

Transporte de datagramas sin garantía de entrega ni orden.

### 8.4.3 — ICMP

Mensajes de control y diagnóstico IP. Ping suele utilizar ICMP.

### 8.4.4 — DNS

Resuelve nombres mediante registros como A, AAAA, MX y CNAME; cachés y TTL afectan propagación.

### 8.4.5 — HTTP

Define semántica de solicitudes y respuestas web; no cifra el canal por sí solo.

### 8.4.6 — HTTPS

HTTP protegido mediante TLS con validación de certificados. No garantiza que el sitio sea honesto.

### 8.4.7 — SSH

Canal seguro para acceso remoto; verifica la clave del servidor.

### 8.4.8 — FTP

Protocolo tradicional de transferencia que no cifra credenciales ni datos por defecto.

### 8.4.9 — SFTP

Protocolo de transferencia sobre SSH, distinto de FTP y FTPS.

### 8.4.10 — SMTP

Envío y retransmisión de correo.

### 8.4.11 — IMAP

Acceso y sincronización de buzones.

### 8.4.12 — POP3

Recuperación de mensajes con un modelo distinto de IMAP.

### 8.4.13 — SMB

Compartición de archivos y recursos; restringe versiones y acceso.

### 8.4.14 — LDAP

Acceso a servicios de directorio; requiere autenticación y transporte protegidos.

### 8.4.15 — Kerberos

Autenticación basada en tickets que depende de infraestructura y sincronización temporal.

### 8.4.16 — WebSockets

Comunicación bidireccional persistente; autentica, autoriza y valida cada operación.

## 8.5 — Routing y Switching

### 8.5.1 — Switching

El switch aprende MAC de origen y asocia direcciones con puertos.

### 8.5.2 — Routing

El router consulta su tabla para determinar siguiente salto o interfaz de salida.

### 8.5.3 — Tablas de rutas

Registran prefijos, siguiente salto, interfaz y métricas. La ruta predeterminada se usa cuando no hay una más específica.

Un router consulta su tabla de rutas para determinar el siguiente salto o interfaz de salida. La selección suele considerar prefijo más específico y métricas/prioridades según el protocolo y sistema.

### 8.5.4 — Rutas estáticas

Se configuran manualmente y requieren mantenimiento.

### 8.5.5 — Rutas dinámicas

Se aprenden mediante protocolos de routing.

### 8.5.6 — NAT

NAT modifica información de direcciones y, en algunas variantes, puertos. Se utiliza comúnmente para permitir que varios dispositivos compartan una dirección IPv4 pública. NAT no es por sí solo un firewall ni una garantía de seguridad.

### 8.5.7 — VLAN

Crea un dominio lógico de capa 2 separado.

### 8.5.8 — Trunking

Transporta varias VLAN mediante etiquetado; un enlace access suele transportar una VLAN.

### 8.5.9 — Segmentación

Separa sistemas para limitar movimiento lateral y reducir exposición.

### 8.5.10 — Subredes

Una subred es una porción lógica de un bloque IP; diseña prefijos sin solapamiento.

## 8.6 — Seguridad de redes

### 8.6.1 — Firewalls

### 8.6.2 — VPN

### 8.6.3 — DMZ

### 8.6.4 — ACL

### 8.6.5 — Puertos abiertos

### 8.6.6 — Servicios expuestos

### 8.6.7 — Superficie de ataque

### 8.6.8 — Filtrado de tráfico

### 8.6.9 — Políticas de filtrado

## 8.7 — Herramientas

### 8.7.1 — Wireshark

Captura y analiza paquetes visualmente. Los archivos pueden contener credenciales, cookies y datos privados.

### 8.7.2 — tcpdump

Captura tráfico desde terminal. Limita interfaz, duración y filtros.

### 8.7.3 — Nmap

Descubre hosts y servicios. Utilízalo solo contra VMs propias o sistemas autorizados.

### 8.7.4 — ping

Comprueba respuesta ICMP; su bloqueo no demuestra que un host esté apagado.

### 8.7.5 — traceroute

Observa saltos de una ruta; routers intermedios pueden no responder.

### 8.7.6 — ip

Consulta interfaces, direcciones y rutas Linux.

### 8.7.7 — ss

Lista sockets y puertos en Linux.

### 8.7.8 — netstat

Muestra estadísticas y conexiones; está obsoleto o ausente en algunas distribuciones modernas.

### 8.7.9 — dig

Realiza consultas DNS detalladas.

### 8.7.10 — nslookup

Consulta DNS con una interfaz sencilla.

### 8.7.11 — curl

Realiza solicitudes a servicios y URLs. Evita incluir secretos en argumentos o historial.

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
**Estado editorial:** en desarrollo; no aprobado ni publicado.


## Registro de revisión editorial interna — 2026-11-24

**Alcance:** cotejo de las entradas oficiales del roadmap, precisión conceptual, secuencia, ejemplos, prácticas, evaluación, seguridad y referencias.

**Resultado:** revisión documental interna realizada con los ajustes y hallazgos siguientes: Se ordenaron los encabezados de seguridad de redes según el roadmap. Se revisaron modelos, direccionamiento, protocolos, segmentación y herramientas; se mantienen restricciones de escaneo autorizado y protección de capturas. Pendiente: resolver ejercicios de subnetting de forma independiente, validar topología en laboratorio aislado y comprobar comandos por sistema operativo/versión.

**Límite de validación:** no se ejecutaron laboratorios, scripts, servicios, bases de datos, máquinas virtuales ni capturas de red en esta revisión. No se declara aprobación académica externa. La etapa continúa en desarrollo hasta completar las pruebas reproducibles y la segunda revisión.
