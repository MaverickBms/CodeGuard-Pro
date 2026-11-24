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

Una red es un conjunto de dispositivos y medios que intercambian datos mediante reglas y protocolos. Su diseño debe considerar alcance, topología, direccionamiento, servicios, controles y requisitos de disponibilidad. Una red puede ser física, inalámbrica, virtual o una combinación.

**Práctica guiada:** dibuja dos dispositivos que intercambian datos a través de un switch y etiqueta interfaces, medio y protocolo.

**Criterio de aceptación:** diferencia dispositivos, enlaces y protocolos; explica qué recurso se comparte.

**Comprobación:** ¿qué elementos mínimos permiten que dos dispositivos intercambien información?

### 8.1.1 — Redes LAN

Una LAN conecta dispositivos en un área limitada mediante Ethernet, Wi‑Fi u otros medios. Su diseño considera topología, capacidad, segmentación y administración.

**Práctica guiada:** Dibuja dos clientes conectados a un switch y un router; identifica medio, enlaces y límite de la LAN.

**Actividad independiente:** Diseña una LAN de oficina con una red de invitados separada.

**Criterios de aceptación:** Delimita la LAN y diferencia alcance físico de segmentación lógica.

**Errores frecuentes:** Suponer que toda LAN debe ser cableada o que todos sus hosts comparten necesariamente una subred.

**Comprobación:** ¿Puede una LAN contener varias subredes o VLAN?

### 8.1.2 — Redes WAN

Una WAN interconecta redes geográficamente separadas mediante servicios de operador o infraestructura propia. Latencia, capacidad, disponibilidad, redundancia y acuerdos de servicio condicionan su diseño.

**Práctica guiada:** Dibuja dos sedes con LAN independientes unidas por una WAN; marca routers de borde y puntos de falla.

**Actividad independiente:** Compara dos opciones de conectividad para una sucursal por costo, latencia, respaldo y dependencia del proveedor.

**Criterios de aceptación:** Explica la interconexión de sedes y enumera criterios de diseño.

**Errores frecuentes:** Confundir WAN con Internet o asumir que el enlace cifra automáticamente el tráfico.

**Comprobación:** ¿Qué controles adicionales necesita una WAN para proteger sus comunicaciones?

### 8.1.3 — Redes MAN

Una MAN conecta redes dentro de un área metropolitana, como edificios o campus distribuidos en una ciudad. Es una categoría de alcance, no un protocolo único.

**Práctica guiada:** Representa tres edificios enlazados por fibra metropolitana y separa las LAN de los enlaces MAN.

**Actividad independiente:** Propón requisitos de redundancia, capacidad y seguridad para conectar sedes universitarias.

**Criterios de aceptación:** Diferencia LAN, MAN y WAN por alcance y propósito.

**Errores frecuentes:** Tratar MAN como una tecnología específica en vez de una categoría geográfica.

**Comprobación:** ¿Qué rasgo geográfico distingue una MAN de una LAN?

### 8.1.4 — Internet

Internet es una interconexión global de redes que utilizan IP y acuerdos de intercambio de tráfico. Participan proveedores, sistemas autónomos, BGP, DNS y puntos de intercambio; no existe un único operador que controle toda la red.

**Práctica guiada:** Ejecuta traceroute/tracert hacia un dominio permitido y registra saltos. Un salto sin respuesta no demuestra por sí solo una falla.

**Actividad independiente:** Dibuja cliente–ISP–redes intermedias–servidor y marca fronteras administrativas y posibles controles.

**Criterios de aceptación:** Explica Internet como red de redes y distingue conectividad IP de servicios como la Web.

**Errores frecuentes:** Usar Internet y World Wide Web como sinónimos o asumir que una traza revela siempre la ruta completa.

**Comprobación:** ¿Por qué la Web es un servicio sobre Internet y no un sinónimo de Internet?

### 8.1.5 — Intranet

Una intranet ofrece recursos privados a usuarios autorizados de una organización. Puede usar tecnologías de Internet y seguir conectada a redes externas mediante controles de identidad, segmentación y políticas.

**Práctica guiada:** Dibuja portal, DNS interno, autenticación y usuarios; marca las fronteras de confianza.

**Actividad independiente:** Define controles para empleados, contratistas y administradores, incluyendo altas, cambios y bajas de cuentas.

**Criterios de aceptación:** Distingue intranet de Internet y explica los controles de acceso.

**Errores frecuentes:** Asumir que una red privada es segura solo por no ser pública.

**Comprobación:** ¿Qué riesgos persisten en una intranet privada?

### 8.1.6 — Extranet

Una extranet comparte recursos específicos con terceros autorizados. Debe limitar datos y operaciones al mínimo necesario y aplicar autenticación, autorización, monitoreo y responsabilidades contractuales.

**Práctica guiada:** Dibuja usuarios externos, zona de publicación y sistemas internos protegidos; identifica controles entre zonas.

**Actividad independiente:** Construye una matriz de permisos para clientes y proveedores y un procedimiento de revocación.

**Criterios de aceptación:** Distingue extranet de intranet y aplica mínimo privilegio a terceros.

**Errores frecuentes:** Entregar cuentas compartidas o conectar directamente la red del proveedor a la LAN interna.

**Comprobación:** ¿Por qué la extranet no debe otorgar acceso general a la red corporativa?

### 8.1.7 — Cliente-servidor

El cliente solicita un servicio y el servidor procesa y responde. Los roles son lógicos: un servidor web puede actuar como cliente de una base de datos y un equipo puede desempeñar distintos roles simultáneamente.

**Práctica guiada:** Representa una petición HTTP y su respuesta; identifica iniciador, protocolo, puerto y datos.

**Actividad independiente:** Diseña una aplicación de tres capas y define cada comunicación cliente-servidor.

**Criterios de aceptación:** Identifica iniciador, proveedor y límites de confianza.

**Errores frecuentes:** Creer que cliente y servidor siempre son equipos físicos distintos.

**Comprobación:** ¿Puede un servidor ser cliente de otro servicio?

### 8.1.8 — Peer-to-peer

En P2P los nodos pueden actuar como clientes y servidores entre sí. La coordinación puede ser centralizada o distribuida; la arquitectura exige controles de identidad, integridad y disponibilidad.

**Práctica guiada:** Compara un diagrama centralizado con uno P2P y analiza qué ocurre si un nodo se desconecta.

**Actividad independiente:** Evalúa ventajas y riesgos de distribuir archivos legítimos entre sedes.

**Criterios de aceptación:** Explica el rol dual de los pares y distingue descentralización de ausencia de coordinación.

**Errores frecuentes:** Asumir que P2P es siempre anónimo, seguro o totalmente descentralizado.

**Comprobación:** ¿Qué problemas de confianza aparecen cuando los pares comparten recursos directamente?

### 8.1.9 — Router

Un router reenvía paquetes IP entre redes según su tabla de encaminamiento, prefijos y métricas. Puede ofrecer NAT o filtrado, pero esas funciones no definen el enrutamiento.

**Práctica guiada:** Consulta `ip route` o `route print`; identifica destino, gateway, interfaz y ruta por defecto.

**Actividad independiente:** Diseña tres subredes conectadas por un router e indica rutas necesarias.

**Criterios de aceptación:** Explica el reenvío entre redes y lee una ruta por defecto.

**Errores frecuentes:** Confundir router con switch o asumir que el gateway está siempre disponible.

**Comprobación:** ¿Qué hace el router si el destino no pertenece a una red conectada directamente?

### 8.1.10 — Switch

Un switch de capa 2 aprende MAC de origen y crea una tabla de reenvío. Si desconoce la MAC destino, puede inundar la trama dentro de la VLAN, excepto por el puerto de entrada. Los switches multicapa también pueden enrutar.

**Práctica guiada:** Simula el aprendizaje de dos MAC en cuatro puertos y explica el destino de una trama desconocida.

**Actividad independiente:** Compara hub, switch L2 y router por dominio de colisión, difusión y decisión de reenvío.

**Criterios de aceptación:** Explica aprendizaje MAC y diferencia reenvío L2 de enrutamiento L3.

**Errores frecuentes:** Afirmar que un switch siempre envía cada trama a todos los puertos.

**Comprobación:** ¿Qué información aprende el switch al recibir una trama?

### 8.1.11 — Firewall

Un firewall aplica reglas según origen, destino, protocolo, puerto, dirección y estado de conexión. Puede operar en host o red; su eficacia depende de reglas, ubicación, mantenimiento y monitoreo.

**Práctica guiada:** Analiza reglas ficticias y determina qué tráfico permiten sin cambiar el firewall del equipo.

**Actividad independiente:** Redacta política de entrada para un servidor web con administración restringida y registros.

**Criterios de aceptación:** Interpreta reglas y aplica mínimo privilegio y denegación por defecto cuando corresponda.

**Errores frecuentes:** Considerar el firewall sustituto de autenticación, parcheado o protección de endpoint.

**Comprobación:** ¿Qué diferencia hay entre filtrar tráfico y autenticar a quien lo origina?

### 8.1.12 — Gateway

Gateway es un punto de interconexión o traducción. En IP, la puerta de enlace predeterminada suele ser el router al que se envía tráfico destinado a redes no locales; el término también se usa en aplicaciones.

**Práctica guiada:** Consulta `ip route` o `route print`; localiza ruta por defecto, gateway e interfaz.

**Actividad independiente:** Explica qué ocurre si el gateway está mal configurado o no es alcanzable.

**Criterios de aceptación:** Diferencia gateway, DNS y dirección IP del destino.

**Errores frecuentes:** Configurar el servidor DNS como gateway o creer que el gateway resuelve nombres.

**Comprobación:** ¿Qué tráfico se envía normalmente a la puerta de enlace predeterminada?

### 8.1.13 — Access Point

Un AP conecta clientes inalámbricos con una red de distribución. Cobertura, bandas, canales, potencia, autenticación y cifrado afectan capacidad y seguridad. Un AP no es necesariamente un router, aunque equipos domésticos integren ambas funciones.

**Práctica guiada:** Inspecciona SSID, banda y canal de una red propia mediante herramientas autorizadas; no accedas a redes ajenas.

**Actividad independiente:** Diseña cobertura Wi‑Fi de oficina considerando interferencia, roaming, invitados y WPA2/WPA3.

**Criterios de aceptación:** Diferencia AP y router y justifica cobertura y controles de acceso.

**Errores frecuentes:** Aumentar potencia como única solución o mantener cifrado obsoleto sin evaluar riesgo.

**Comprobación:** ¿Por qué una señal fuerte no garantiza calidad ni seguridad Wi‑Fi?

## 8.2 — Modelos de comunicación

### 8.2.1 — Modelo OSI

El modelo OSI es un marco conceptual de siete capas para razonar sobre funciones de comunicación; no es una pila de protocolos que se instale literalmente. **Práctica:** ubica Ethernet, IP, TCP y HTTP en el modelo como aproximación didáctica. **Evidencia:** justifica la capa y explica que algunas tecnologías abarcan varias funciones.

### 8.2.2 — Las siete capas OSI

Las capas OSI describen funciones: física, enlace, red, transporte, sesión, presentación y aplicación. Las fronteras no siempre coinciden exactamente con implementaciones modernas. **Práctica:** analiza una solicitud web y asigna ejemplos de función a cada capa. **Evidencia:** describe qué pregunta responde cada capa sin memorizar solo nombres.

### 8.2.3 — Modelo TCP/IP

TCP/IP agrupa funciones en acceso a red, Internet, transporte y aplicación, aunque los modelos de referencia varían en número de capas. **Práctica:** mapea Ethernet, IP, TCP y DNS/HTTP al modelo usado en el curso. **Evidencia:** compara una capa OSI con su correspondencia aproximada en TCP/IP.

### 8.2.4 — Encapsulamiento

El encapsulamiento añade información de control al dato al descender por las capas: cabeceras y, según el protocolo, tráileres. **Práctica:** representa datos de aplicación dentro de un segmento TCP, paquete IP y trama Ethernet. **Evidencia:** identifica direcciones de cada capa y explica por qué cambian en cada salto.

### 8.2.5 — Desencapsulamiento

El desencapsulamiento retira y procesa la información de protocolo al recibir datos, verificando campos y entregando la carga a la capa superior. **Práctica:** dibuja el recorrido inverso de una trama Ethernet recibida. **Evidencia:** explica cómo una MAC de destino, una IP y un puerto cumplen funciones diferentes.

### 8.2.6 — Paquetes

Un paquete suele referirse a la unidad de datos de capa de red, por ejemplo un datagrama IP, que contiene direcciones y campos de control. **Práctica:** inspecciona un paquete IP en una captura de laboratorio. **Evidencia:** identifica IP origen/destino, protocolo superior y TTL o Hop Limit.

### 8.2.7 — Tramas

Una trama es la unidad de datos de enlace que se transmite sobre un medio local y contiene direcciones de enlace y mecanismos de detección de errores según la tecnología. **Práctica:** localiza cabecera Ethernet y tipo EtherType en Wireshark. **Evidencia:** distingue MAC origen/destino de direcciones IP.

### 8.2.8 — Segmentos

Un segmento suele designar la unidad de datos de TCP; UDP utiliza el término datagrama. TCP incorpora puertos, números de secuencia, confirmaciones y control de flujo. **Práctica:** examina una conexión TCP de laboratorio y localiza puertos y flags. **Evidencia:** explica SYN, ACK y FIN a nivel básico.

### 8.2.9 — MTU

MTU es el tamaño máximo de unidad de transmisión de una interfaz o enlace; no debe confundirse con el tamaño máximo de carga de aplicación. Explica fragmentación IPv4 y Path MTU Discovery en términos generales. **Práctica:** consulta MTU de interfaces con `ip link`. **Evidencia:** predice qué puede ocurrir si un paquete supera el MTU del camino.

## 8.3 — Direccionamiento

### 8.3.1 — Dirección MAC

Una dirección MAC identifica una interfaz en el ámbito de enlace y se utiliza para entregar tramas en una red local; puede ser modificada o aleatorizada por software. **Práctica:** consulta MAC de una interfaz con `ip link` o `getmac`. **Evidencia:** diferencia MAC de IP y explica por qué los routers no reenvían la trama Ethernet original de extremo a extremo.

### 8.3.2 — IPv4

IPv4 utiliza direcciones de 32 bits representadas habitualmente en cuatro octetos decimales. Explica dirección de red, host, prefijo y límites de subred. **Práctica:** identifica red y broadcast para `192.0.2.34/27` usando una calculadora o cálculo binario. **Evidencia:** muestra máscara, rango utilizable y justificación.

### 8.3.3 — IPv6

IPv6 utiliza direcciones de 128 bits, notación hexadecimal y reglas de compresión; incorpora tipos como global unicast, link-local y multicast. **Práctica:** expande y comprime una dirección IPv6 válida y reconoce `fe80::/10`. **Evidencia:** explica por qué IPv6 no utiliza broadcast y para qué sirve Neighbor Discovery.

### 8.3.4 — IP pública

Una IP pública es enrutable globalmente bajo políticas de Internet y asignación de registros; no implica que un servicio sea alcanzable desde cualquier origen. **Práctica:** compara la dirección de una interfaz local con la dirección observada por un servicio externo solo en tu propio entorno. **Evidencia:** explica NAT y filtrado como causas de diferencia.

### 8.3.5 — IP privada

Los rangos privados IPv4 definidos para redes internas no se enrutan globalmente en Internet. Conoce los bloques 10/8, 172.16/12 y 192.168/16. **Práctica:** clasifica tres direcciones y detecta si pertenecen a esos rangos. **Evidencia:** explica por qué la conectividad externa suele requerir NAT o un mecanismo de borde.

### 8.3.6 — Máscaras

Una máscara o prefijo determina qué bits identifican la red y cuáles quedan para hosts. Relaciona máscara decimal con longitud de prefijo CIDR. **Práctica:** convierte `/24`, `/26` y `/30` a máscaras y calcula direcciones totales. **Evidencia:** muestra el procedimiento binario y diferencia direcciones totales de hosts asignables.

### 8.3.7 — Subnetting

Subnetting divide un bloque IP en subredes más pequeñas para organizar dominios de broadcast, direccionamiento y políticas. **Práctica:** divide `192.0.2.0/24` en cuatro subredes iguales y calcula red, broadcast y rango. **Evidencia:** presenta las cuatro subredes sin solapamiento.

### 8.3.8 — CIDR

CIDR expresa redes mediante prefijo, por ejemplo `/24`, y permite asignación y agregación sin depender de clases tradicionales. **Práctica:** interpreta `198.51.100.64/26` y determina el bloque que cubre. **Evidencia:** calcula inicio, fin y cantidad de direcciones.

### 8.3.9 — VLSM

VLSM asigna subredes de tamaños distintos dentro de un bloque, ajustando cada prefijo a la cantidad de hosts requerida. **Práctica:** asigna subredes a tres segmentos de laboratorio con diferentes necesidades, ordenando de mayor a menor. **Evidencia:** demuestra que los bloques están alineados y no se superponen.

### 8.3.10 — Gateway

El gateway predeterminado es el siguiente salto utilizado cuando la tabla de rutas no contiene una ruta más específica. **Práctica:** inspecciona `ip route` o `route print` y localiza la ruta por defecto. **Evidencia:** interpreta destino, máscara/prefijo, siguiente salto y métrica.

### 8.3.11 — Broadcast

Broadcast IPv4 entrega un datagrama a todos los hosts de una subred; se distingue broadcast limitado y dirigido, este último sujeto a restricciones de seguridad. IPv6 utiliza multicast en lugar de broadcast. **Práctica:** calcula la dirección broadcast de una subred pequeña. **Evidencia:** explica qué hosts la reciben y por qué no debe confundirse con multicast.

### 8.3.12 — ARP

ARP resuelve una dirección IPv4 local a una dirección de enlace para enviar una trama dentro de la LAN. Explica caché ARP, solicitud broadcast y respuesta, así como riesgos de suplantación. **Práctica:** consulta la tabla con `ip neigh` o `arp -a` tras comunicarte con un host de laboratorio. **Evidencia:** identifica IP, MAC y estado de la entrada.

### 8.3.13 — DHCP

DHCP asigna parámetros de red como dirección IP, máscara, gateway, DNS y tiempo de concesión. Explica el intercambio DORA en DHCPv4 y la diferencia entre reserva y asignación dinámica. **Práctica:** inspecciona la concesión de tu VM sin alterar el servidor. **Evidencia:** registra servidor, duración y opciones recibidas.

## 8.4 — Protocolos

### 8.4.1 — TCP

TCP ofrece un flujo de bytes fiable y ordenado con establecimiento de conexión, retransmisión y control de congestión. **Práctica:** observa el handshake de tres vías en una captura propia. **Evidencia:** identifica SYN, SYN-ACK y ACK y explica qué no garantiza TCP sobre la aplicación.

### 8.4.2 — UDP

UDP ofrece datagramas sin establecimiento de conexión ni garantía de entrega u orden; las aplicaciones gestionan las necesidades adicionales. **Práctica:** identifica tráfico UDP en una captura de DNS de laboratorio. **Evidencia:** compara overhead y garantías frente a TCP.

### 8.4.3 — ICMP

ICMP comunica errores y condiciones de red, y también sustenta herramientas de diagnóstico como ping. No es un protocolo de transporte para aplicaciones. **Práctica:** interpreta una respuesta Echo y un mensaje Destination Unreachable en capturas de laboratorio. **Evidencia:** diferencia diagnóstico de garantía de disponibilidad.

### 8.4.4 — DNS

DNS traduce nombres a registros como A, AAAA, MX, TXT y CNAME mediante consultas recursivas e iterativas. **Práctica:** consulta un dominio propio o de documentación con `dig`. **Evidencia:** identifica tipo, TTL, servidor consultado y diferencia entre respuesta autoritativa y recursiva.

### 8.4.5 — HTTP

HTTP define semántica de solicitudes y respuestas, métodos, códigos de estado, cabeceras y representación de recursos. **Práctica:** consulta una URL pública de documentación con `curl -I`. **Evidencia:** interpreta método, estado y cabeceras principales sin asumir que un 200 garantiza corrección funcional.

### 8.4.6 — HTTPS

HTTPS es HTTP protegido mediante TLS, que aporta confidencialidad, integridad y autenticación del servidor según validación de certificados. **Práctica:** inspecciona certificado y versión TLS de un sitio propio o autorizado. **Evidencia:** explica cadena de confianza, nombre del servidor y por qué cifrado no equivale a que el sitio sea legítimo.

### 8.4.7 — SSH

SSH proporciona acceso remoto seguro y canales cifrados, normalmente mediante autenticación por clave o contraseña. **Práctica:** conecta dos VMs propias en una red aislada y verifica la huella de host antes de confiar. **Evidencia:** distingue autenticación del servidor y del usuario.

### 8.4.8 — FTP

FTP transfiere archivos mediante un canal de control y otro de datos; el protocolo clásico no cifra credenciales ni contenido. **Práctica:** analiza conceptualmente puertos activo/pasivo y explica por qué FTP sin cifrar no debe utilizarse en redes no confiables. **Evidencia:** compara sus riesgos con SFTP.

### 8.4.9 — SFTP

SFTP es un protocolo de transferencia de archivos que funciona sobre SSH y no es simplemente FTP protegido por TLS. **Práctica:** describe una sesión SFTP hacia un servidor de laboratorio y las operaciones de listar, subir y descargar. **Evidencia:** identifica el canal SSH y los permisos que limitan acceso.

### 8.4.10 — SMTP

SMTP transporta y retransmite correo entre clientes y servidores o entre servidores; el envío autenticado suele utilizar extensiones y TLS según configuración. **Práctica:** dibuja el flujo desde cliente de correo hasta servidor receptor. **Evidencia:** distingue SMTP de protocolos de acceso como IMAP y POP3.

### 8.4.11 — IMAP

IMAP permite acceder y sincronizar mensajes almacenados en el servidor, carpetas y estados entre varios clientes. **Práctica:** compara una cuenta de prueba configurada con IMAP frente a un modelo de descarga local. **Evidencia:** explica sincronización, carpetas y almacenamiento remoto.

### 8.4.12 — POP3

POP3 está orientado a recuperar mensajes desde el servidor, con comportamientos de descarga y conservación que dependen del cliente. **Práctica:** compara un flujo POP3 con IMAP en un diagrama. **Evidencia:** justifica cuál se adapta mejor a varios dispositivos y qué limitaciones operativas tiene.

### 8.4.13 — SMB

SMB permite compartir archivos, impresoras y otros recursos en redes, especialmente en entornos Windows. Explica autenticación, permisos compartidos y NTFS, y versiones del protocolo. **Práctica:** inspecciona un recurso compartido en una red de laboratorio. **Evidencia:** calcula el acceso efectivo considerando ambos niveles de permisos.

### 8.4.14 — LDAP

LDAP es un protocolo de acceso y consulta a servicios de directorio mediante entradas, atributos y nombres distinguidos. **Práctica:** interpreta un DN y un filtro LDAP de ejemplo sin consultar directorios ajenos. **Evidencia:** identifica base de búsqueda, atributo y alcance.

### 8.4.15 — Kerberos

Kerberos es un protocolo de autenticación basado en tickets y un tercero de confianza, común en dominios Windows/Active Directory. Explica KDC, TGT, tickets de servicio y dependencia de sincronización horaria. **Práctica:** dibuja el intercambio de autenticación sin incluir secretos reales. **Evidencia:** explica por qué la contraseña no se envía al servicio en cada solicitud.

### 8.4.16 — WebSockets

WebSocket mantiene un canal bidireccional persistente entre cliente y servidor tras un handshake iniciado sobre HTTP. **Práctica:** compara una aplicación de chat por polling con otra basada en WebSocket. **Evidencia:** identifica cuándo conviene cada enfoque y qué controles de autenticación/origen siguen siendo necesarios.

## 8.5 — Routing y Switching

### 8.5.1 — Switching

Switching reenvía tramas dentro de una red de capa 2 usando una tabla de direcciones MAC y dominios de broadcast. **Práctica:** simula el aprendizaje de MAC en una topología con tres hosts. **Evidencia:** explica flooding, aprendizaje y filtrado.

### 8.5.2 — Routing

Routing selecciona caminos para reenviar paquetes entre redes mediante prefijos y métricas. Distingue plano de control y plano de datos a nivel introductorio. **Práctica:** interpreta una tabla de rutas de una VM. **Evidencia:** explica la regla de prefijo más específico.

### 8.5.3 — Tablas de rutas

Una tabla de rutas asocia destinos con siguiente salto, interfaz, métrica y origen de la ruta. **Práctica:** ejecuta `ip route` o `route print` en un equipo de laboratorio. **Evidencia:** identifica ruta conectada, ruta por defecto y ruta más específica para un destino.

### 8.5.4 — Rutas estáticas

Una ruta estática es configurada explícitamente por un administrador y no se adapta automáticamente a cambios de topología. **Práctica:** redacta la configuración conceptual para alcanzar una subred de laboratorio a través de un router conocido; no alteres rutas del host principal. **Evidencia:** indica destino, prefijo y siguiente salto.

### 8.5.5 — Rutas dinámicas

Los protocolos de routing dinámico intercambian información para calcular rutas y responder a cambios; ejemplos incluyen OSPF y BGP con ámbitos y objetivos distintos. **Práctica:** compara OSPF dentro de un sistema autónomo con BGP entre sistemas autónomos. **Evidencia:** describe qué problema resuelve cada uno sin equipararlos.

### 8.5.6 — NAT

NAT modifica direcciones o puertos en el tránsito entre redes; PAT permite compartir una dirección pública mediante puertos. **Práctica:** dibuja una conexión desde dos hosts privados hacia un servidor externo. **Evidencia:** explica traducción de origen y por qué NAT no sustituye un firewall.

### 8.5.7 — VLAN

Una VLAN segmenta lógicamente una infraestructura de capa 2 en dominios separados. Explica etiquetado 802.1Q y la necesidad de routing para comunicar VLAN distintas. **Práctica:** diseña VLAN de usuarios y servidores con subredes separadas. **Evidencia:** identifica qué tráfico queda aislado y qué equipo permitiría comunicación controlada.

### 8.5.8 — Trunking

Trunking transporta tráfico de varias VLAN por un enlace, normalmente mediante etiquetas 802.1Q. Distingue puerto access y trunk y el riesgo de VLAN nativa mal configurada. **Práctica:** representa dos switches conectados por trunk y dos VLAN. **Evidencia:** indica qué tramas llevan etiqueta y cómo se preserva la segmentación.

### 8.5.9 — Segmentación

La segmentación divide una red en zonas con políticas distintas para reducir movimiento lateral y limitar exposición. **Práctica:** separa usuarios, servidores y administración en un diagrama de laboratorio. **Evidencia:** define flujos necesarios y denegaciones por defecto.

### 8.5.10 — Subredes

Una subred es una partición lógica de un espacio IP identificada por prefijo. Relaciona subnetting con límites de broadcast IPv4 y diseño de rutas. **Práctica:** calcula una subred para una cantidad dada de hosts y comprueba que no se solape con otra. **Evidencia:** entrega red, prefijo, broadcast y rango.

## 8.6 — Seguridad de redes

### 8.6.1 — Firewalls

Los firewalls pueden filtrar por paquetes, estado, aplicación o identidad, según su arquitectura. **Práctica:** diseña reglas para permitir HTTPS desde clientes a un servidor y bloquear administración desde redes de usuario. **Evidencia:** especifica origen, destino, protocolo, puerto y dirección.

### 8.6.2 — VPN

Una VPN crea un túnel protegido sobre una red subyacente y puede conectar usuarios o sitios. Distingue acceso remoto y site-to-site, y explica que el cifrado no elimina riesgos del endpoint. **Práctica:** dibuja los extremos y rutas de una VPN de acceso remoto. **Evidencia:** identifica autenticación, cifrado y redes alcanzables.

### 8.6.3 — DMZ

Una DMZ aloja servicios que deben ser accesibles desde redes menos confiables, separados de la red interna sensible. **Práctica:** diseña una zona DMZ para un servidor web con acceso mínimo a una base de datos. **Evidencia:** justifica reglas y demuestra que la DMZ no equivale a confiar plenamente en el servidor.

### 8.6.4 — ACL

Una ACL define condiciones que permiten o deniegan tráfico o acceso a recursos, según el dispositivo y el contexto. **Práctica:** redacta una ACL conceptual que permita solo DNS y HTTPS entre segmentos de laboratorio. **Evidencia:** explica orden de evaluación, coincidencias y regla implícita final cuando aplique.

### 8.6.5 — Puertos abiertos

Un puerto abierto indica que un proceso acepta conexiones en una interfaz, no que el servicio sea necesariamente vulnerable. **Práctica:** consulta sockets de escucha de tu propia VM con `ss -lntup`. **Evidencia:** asocia puerto, protocolo, proceso y dirección de escucha.

### 8.6.6 — Servicios expuestos

Un servicio expuesto es una función accesible desde una zona de red; su riesgo depende de versión, configuración, autenticación y superficie alcanzable. **Práctica:** inventaría servicios de una VM propia y clasifícalos por necesidad y alcance. **Evidencia:** propone reducir exposición sin deshabilitar servicios críticos a ciegas.

### 8.6.7 — Superficie de ataque

La superficie de ataque reúne interfaces, servicios, identidades, dependencias y rutas por las que un actor podría interactuar con un sistema. **Práctica:** crea un inventario de activos y puntos de entrada para una VM de laboratorio. **Evidencia:** prioriza tres reducciones de superficie y explica el riesgo asociado.

### 8.6.8 — Filtrado de tráfico

El filtrado de tráfico aplica políticas sobre paquetes y flujos según origen, destino, protocolo, puerto, estado o contenido. **Práctica:** analiza una regla de firewall de laboratorio y predice su efecto sobre tres flujos. **Evidencia:** documenta permitido, bloqueado y no coincidente.

### 8.6.9 — Políticas de filtrado

Una política de filtrado establece objetivos, zonas, reglas, excepciones, registro y revisión periódica. **Práctica:** redacta una política de denegación por defecto con excepciones justificadas para una red pequeña. **Evidencia:** incluye propietario, propósito, pruebas y procedimiento de reversión.

## 8.7 — Herramientas

### 8.7.1 — Wireshark

Wireshark captura y analiza paquetes, decodificando protocolos y permitiendo filtros de captura y visualización. **Práctica:** captura tráfico generado por tu propia VM y filtra DNS o TCP. **Evidencia:** identifica interfaz, filtro y campos relevantes; elimina o anonimiza datos sensibles antes de compartir la captura.

### 8.7.2 — tcpdump

`tcpdump` captura tráfico desde interfaz y permite filtros BPF para limitar lo observado. **Práctica:** captura unos pocos paquetes ICMP o DNS en una interfaz de laboratorio con permisos adecuados. **Evidencia:** documenta comando, interfaz, filtro y límite de paquetes; no captures tráfico de terceros.

### 8.7.3 — Nmap

Nmap descubre hosts y servicios mediante técnicas de sondeo; su uso debe limitarse a sistemas propios o con autorización explícita. **Práctica:** escanea únicamente la VM objetivo de tu laboratorio aislado y un puerto que hayas habilitado deliberadamente. **Evidencia:** registra alcance, comando, hora y resultado, y explica límites de detección.

### 8.7.4 — ping

`ping` envía solicitudes ICMP Echo para comprobar respuesta y estimar latencia, pero un bloqueo ICMP no demuestra que el host esté caído. **Práctica:** ejecuta un número limitado de solicitudes a otra VM propia. **Evidencia:** interpreta pérdida, RTT y posibles causas de ausencia de respuesta.

### 8.7.5 — traceroute

`traceroute` o `tracert` infiere saltos de una ruta mediante TTL/Hop Limit y respuestas de red; firewalls y balanceo pueden alterar resultados. **Práctica:** ejecuta la herramienta hacia un destino autorizado y limita el número de saltos. **Evidencia:** explica asteriscos y por qué cada salto no necesariamente revela toda la ruta.

### 8.7.6 — ip

`ip` administra y consulta interfaces, direcciones, vecinos y rutas en Linux. **Práctica:** utiliza `ip addr`, `ip link` e `ip route` en modo lectura. **Evidencia:** documenta interfaz, dirección, estado, MAC y gateway sin ejecutar cambios de configuración.

### 8.7.7 — ss

`ss` muestra sockets y conexiones; opciones como `-l`, `-t`, `-u`, `-n` y `-p` filtran escuchas, protocolos y procesos. **Práctica:** consulta sockets TCP en escucha de tu VM. **Evidencia:** identifica dirección local, puerto, estado y proceso cuando los permisos lo permiten.

### 8.7.8 — netstat

`netstat` muestra conexiones, rutas y estadísticas en sistemas donde está disponible; en Linux moderno suele preferirse `ss`. **Práctica:** compara la salida equivalente de ambas herramientas en un entorno que tenga las dos. **Evidencia:** explica qué información coincide y cuál depende de opciones o implementación.

### 8.7.9 — dig

`dig` consulta DNS y presenta respuesta, autoridad, información adicional y tiempos. **Práctica:** consulta registros A, AAAA y MX de un dominio público de documentación. **Evidencia:** identifica servidor, tipo, TTL y sección de respuesta.

### 8.7.10 — nslookup

`nslookup` permite consultar servidores DNS de forma interactiva o directa; su presentación varía por plataforma. **Práctica:** consulta un nombre y una dirección inversa en un entorno de prueba. **Evidencia:** compara el resultado con `dig` y explica diferencias de formato.

### 8.7.11 — curl

`curl` realiza solicitudes a URLs y permite inspeccionar cabeceras, métodos, códigos y cuerpos; no es solo una herramienta de descarga. **Práctica:** usa `curl -I` y una solicitud GET a una API pública de prueba o servicio propio. **Evidencia:** registra URL, método, estado y cabeceras sin enviar credenciales.

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
