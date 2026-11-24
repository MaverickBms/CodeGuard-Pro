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

El modelo OSI organiza las funciones de comunicación en siete capas. Es un marco conceptual para clasificar protocolos y localizar fallos, no una descripción rígida de cada implementación real.

**Práctica guiada:** Clasifica fallos sintéticos: cable desconectado, VLAN incorrecta, ruta ausente, puerto TCP cerrado y error HTTP. Justifica la capa principal y dependencias.

**Actividad independiente:** Construye una tabla de capas, función, unidad de datos y ejemplos tecnológicos.

**Criterios de aceptación:** Enumera las siete capas y utiliza el modelo como herramienta de diagnóstico.

**Errores frecuentes:** Afirmar que cada protocolo pertenece siempre a una única capa o que OSI es una pila instalada literalmente.

**Comprobación:** ¿Qué ventaja aporta separar la comunicación en capas?

### 8.2.2 — Las siete capas OSI

Las capas son física, enlace, red, transporte, sesión, presentación y aplicación. Cada una abstrae responsabilidades y utiliza servicios inferiores. En sistemas reales algunas funciones se combinan o distribuyen.

**Práctica guiada:** Clasifica Ethernet, IP, TCP, UDP, DNS, HTTP y TLS; anota cuándo la clasificación es aproximada.

**Actividad independiente:** Describe una petición HTTPS y las funciones de comunicación que intervienen en cada capa.

**Criterios de aceptación:** Ordena y explica las siete capas y reconoce clasificaciones aproximadas.

**Errores frecuentes:** Confundir sesión con inicio de sesión de usuario o presentación con interfaz gráfica.

**Comprobación:** ¿Por qué OSI sigue siendo útil si una pila no implementa siete módulos separados?

### 8.2.3 — Modelo TCP/IP

El modelo TCP/IP suele agrupar funciones en acceso a red, Internet, transporte y aplicación. Describe la arquitectura práctica de Internet; su correspondencia con OSI es aproximada, no uno a uno.

**Práctica guiada:** Asigna Ethernet, IP, TCP, UDP, DNS y HTTP a capas TCP/IP y compara la clasificación con OSI.

**Actividad independiente:** Dibuja una consulta DNS sobre UDP y una conexión HTTPS sobre TCP, anotando capas y unidades de datos.

**Criterios de aceptación:** Explica las capas del modelo elegido y la correspondencia aproximada con OSI.

**Errores frecuentes:** Confundir IP con TCP o afirmar que existe una única representación didáctica universal.

**Comprobación:** ¿Qué función aporta IP que no proporciona TCP?

### 8.2.4 — Encapsulamiento

Al descender por la pila, cada capa añade información de control a los datos. En una comunicación web, los datos de aplicación pueden quedar dentro de un segmento TCP, un paquete IP y una trama Ethernet.

**Práctica guiada:** Dibuja la encapsulación de una petición HTTP sobre TCP/IP/Ethernet y etiqueta cada encabezado.

**Actividad independiente:** Explica qué ocurre con la trama cuando el paquete atraviesa un router hacia otra LAN.

**Criterios de aceptación:** Representa el orden correcto de encapsulación y diferencia encabezados de datos de aplicación.

**Errores frecuentes:** Creer que la trama Ethernet permanece intacta de extremo a extremo a través de routers.

**Comprobación:** ¿Qué partes cambian normalmente cuando un paquete atraviesa un router?

### 8.2.5 — Desencapsulamiento

El receptor procesa los encabezados de cada capa, valida la información que corresponda y entrega la carga útil a la capa superior. Desencapsular no es lo mismo que descifrar: el cifrado depende de protocolos y claves.

**Práctica guiada:** Examina una captura de laboratorio e identifica los campos Ethernet, IP, TCP y HTTP.

**Actividad independiente:** Describe qué impediría que los datos llegaran a la aplicación: trama inválida, IP incorrecta, puerto sin escucha o error de aplicación.

**Criterios de aceptación:** Explica el orden de procesamiento y relaciona cada encabezado con su función.

**Errores frecuentes:** Suponer que desencapsulamiento equivale a descifrado TLS.

**Comprobación:** ¿Qué diferencia existe entre desencapsular y descifrar?

### 8.2.6 — Paquetes

En este contexto, paquete suele referirse a una unidad de datos IP con encabezado y carga útil. Los routers utilizan campos IP para reenviar paquetes; fragmentación, tamaño y tratamiento dependen de versión y camino.

**Práctica guiada:** Inspecciona un paquete IP en una captura de laboratorio y localiza direcciones, TTL, protocolo y longitud.

**Actividad independiente:** Compara paquete IP y trama Ethernet y explica el alcance de MAC e IP.

**Criterios de aceptación:** Identifica campos principales y distingue paquete, segmento y trama.

**Errores frecuentes:** Usar paquete, trama y segmento como sinónimos o asumir que las MAC permanecen iguales a través de Internet.

**Comprobación:** ¿Qué información utiliza un router para decidir el siguiente salto?

### 8.2.7 — Tramas

Una trama es la unidad de datos de enlace para una tecnología concreta, como Ethernet. Incluye direcciones de enlace y campos de control; en Ethernet puede incorporar FCS. Los routers suelen terminar una trama y construir otra para el siguiente enlace.

**Práctica guiada:** Examina una captura Ethernet y localiza MAC origen/destino, EtherType y longitud; considera que FCS puede no aparecer en la captura.

**Actividad independiente:** Explica qué campos de enlace cambian cuando el paquete atraviesa un router.

**Criterios de aceptación:** Identifica función de MAC y EtherType y diferencia trama de paquete IP.

**Errores frecuentes:** Suponer que FCS siempre aparece en capturas o que MAC identifica el host extremo a través de toda la ruta.

**Comprobación:** ¿Por qué el router construye una nueva trama para el siguiente enlace?

### 8.2.8 — Segmentos

En TCP, un segmento incluye encabezado TCP y datos. Puertos, secuencias, reconocimientos y flags permiten comunicación fiable y ordenada. UDP transporta datagramas; no ofrece las mismas garantías de TCP.

**Práctica guiada:** Examina una captura TCP de laboratorio y localiza puertos, SYN/ACK/FIN y números de secuencia.

**Actividad independiente:** Representa el establecimiento TCP de tres vías y explica la función de cada mensaje.

**Criterios de aceptación:** Identifica campos TCP básicos y diferencia segmento TCP de datagrama UDP.

**Errores frecuentes:** Afirmar que cada segmento equivale a un mensaje de aplicación o que TCP conserva límites de mensajes.

**Comprobación:** ¿Por qué TCP se considera un flujo de bytes?

### 8.2.9 — MTU

La MTU es el tamaño máximo de la unidad de datos que puede transportar un enlace sin fragmentación en esa capa. Ethernet estándar suele usar 1500 bytes de carga IP, pero túneles y encapsulación pueden reducir la MTU de camino.

**Práctica guiada:** Consulta MTU con `ip link` o `netsh interface ipv4 show subinterfaces`; registra interfaz y valor sin modificarlo.

**Actividad independiente:** Explica por qué una aplicación puede fallar con ciertos tamaños de transferencia si Path MTU Discovery no funciona correctamente.

**Criterios de aceptación:** Distingue MTU de enlace y MTU de camino y relaciona encapsulación con tamaño disponible.

**Errores frecuentes:** Confundir MTU con ancho de banda o asumir que 1500 aplica a todas las interfaces.

**Comprobación:** ¿Cómo puede una MTU incorrecta afectar solo algunos tamaños de tráfico?

## 8.3 — Direccionamiento

### 8.3.1 — Dirección MAC

Una dirección MAC identifica una interfaz en una tecnología de enlace como Ethernet. Las direcciones pueden ser universales o administradas localmente; la MAC de destino se utiliza dentro del enlace y puede cambiar al atravesar routers.

**Práctica guiada:** Consulta interfaces con `ip link` o `getmac` y registra MAC de una interfaz propia. Distingue interfaz física, virtual y dirección asignada.

**Actividad independiente:** Explica por qué un paquete IP puede conservar su dirección destino mientras la trama de cada salto utiliza MAC distintas.

**Criterios de aceptación:** Identifica MAC origen/destino y limita su alcance al enlace correspondiente.

**Errores frecuentes:** Confundir MAC con dirección IP o tratarla como identidad inmutable y universal del dispositivo.

**Comprobación:** ¿Por qué cambia normalmente la MAC destino al pasar por un router?

### 8.3.2 — IPv4

IPv4 utiliza direcciones de 32 bits representadas habitualmente en cuatro octetos decimales. La dirección se interpreta junto con una máscara o prefijo que separa parte de red y host. Algunas direcciones tienen usos especiales, como loopback, multicast y rangos privados.

**Práctica guiada:** Consulta dirección y prefijo con `ip addr` o `ipconfig`. Identifica dirección, máscara, interfaz y gateway sin modificar la configuración.

**Actividad independiente:** Clasifica direcciones de ejemplo en privadas, públicas, loopback, link-local y multicast usando rangos documentados.

**Criterios de aceptación:** Interpreta 32 bits, notación decimal y prefijo y reconoce rangos especiales.

**Errores frecuentes:** Asumir que toda dirección IPv4 es enrutable públicamente o que la máscara puede omitirse al diseñar subredes.

**Comprobación:** ¿Qué información aporta el prefijo junto a una dirección IPv4?

### 8.3.3 — IPv6

IPv6 utiliza direcciones de 128 bits escritas en hexadecimal y admite abreviación de ceros. Incluye unicast, multicast y anycast; no utiliza broadcast. La autoconfiguración SLAAC, DHCPv6 y Neighbor Discovery forman parte de su operación.

**Práctica guiada:** Consulta direcciones IPv6 con `ip -6 addr` o `ipconfig /all`; distingue link-local, global y loopback si están presentes.

**Actividad independiente:** Diseña un esquema IPv6 de documentación para dos subredes y explica cómo se asignarían prefijos.

**Criterios de aceptación:** Interpreta notación hexadecimal y distingue tipos de dirección y ausencia de broadcast.

**Errores frecuentes:** Tratar IPv6 como IPv4 con más dígitos o suponer que todas las direcciones globales son automáticamente seguras.

**Comprobación:** ¿Qué mecanismo cumple funciones de descubrimiento de vecinos en IPv6?

### 8.3.4 — IP pública

Una IP pública es una dirección globalmente enrutable dentro del esquema de asignación de Internet, sujeta a políticas de enrutamiento y filtrado. Una dirección pública no implica que un servicio sea alcanzable: firewall, NAT, rutas y políticas del proveedor también intervienen.

**Práctica guiada:** Compara la dirección configurada en tu interfaz con la dirección de salida observada por un servicio confiable, sin publicar datos personales ni realizar escaneos.

**Actividad independiente:** Explica por qué una dirección pública puede no aceptar conexiones entrantes.

**Criterios de aceptación:** Distingue dirección pública de accesibilidad efectiva y explica el papel de los controles perimetrales.

**Errores frecuentes:** Asumir que tener IP pública significa que todos los puertos están abiertos o que el host está expuesto directamente.

**Comprobación:** ¿Qué condiciones además de la IP determinan si un servicio es alcanzable desde Internet?

### 8.3.5 — IP privada

Los rangos privados IPv4 definidos por RFC 1918 son 10.0.0.0/8, 172.16.0.0/12 y 192.168.0.0/16. No se enrutan globalmente en Internet y suelen utilizar NAT o gateways para acceder a redes externas. Las direcciones privadas pueden repetirse en redes aisladas.

**Práctica guiada:** Identifica si direcciones de ejemplo pertenecen a RFC 1918 y consulta la dirección privada de una interfaz propia.

**Actividad independiente:** Diseña dos LAN aisladas que reutilicen rangos privados y explica qué conflicto surgiría al interconectarlas sin renumeración o traducción.

**Criterios de aceptación:** Reconoce los tres rangos privados y explica el alcance de su enrutamiento.

**Errores frecuentes:** Confundir todo 172.x.x.x con privado o asumir que una dirección privada impide cualquier comunicación externa.

**Comprobación:** ¿Por qué dos organizaciones pueden utilizar la misma dirección privada sin conflicto mientras sus redes estén aisladas?

### 8.3.6 — Máscaras

Una máscara IPv4 indica qué bits pertenecen al prefijo de red y cuáles al identificador de host. En notación CIDR, el número tras la barra expresa la cantidad de bits de prefijo. La máscara permite determinar si un destino está en la misma subred.

**Práctica guiada:** Convierte máscaras comunes (/24, /26, /30) a notación decimal y binaria con una tabla de bits.

**Actividad independiente:** Dado IP y prefijo, determina identificador de red, rango de hosts y broadcast para una subred válida.

**Criterios de aceptación:** Calcula red y tamaño de subred con el prefijo correcto.

**Errores frecuentes:** Confundir cantidad de bits de host con cantidad de hosts utilizables o asumir que todas las subredes reservan dos direcciones de la misma manera.

**Comprobación:** ¿Qué significa /26 en una dirección IPv4?

### 8.3.7 — Subnetting

Subnetting divide un bloque IP en subredes más pequeñas mediante prefijos más largos. Permite segmentar dominios de broadcast, organizar direccionamiento y aplicar políticas. El diseño debe considerar cantidad de hosts, crecimiento, enlaces punto a punto y direcciones especiales.

**Práctica guiada:** Divide un bloque de documentación /24 en cuatro subredes iguales; verifica límites, prefijos y ausencia de solapamiento.

**Actividad independiente:** Diseña un plan de direccionamiento para usuarios, servidores, invitados y administración con tamaños distintos.

**Criterios de aceptación:** Presenta subredes no solapadas que satisfacen necesidades y justifican reservas.

**Errores frecuentes:** Asignar rangos superpuestos o elegir tamaños sin contar hosts y crecimiento.

**Comprobación:** ¿Qué ocurre con la cantidad de hosts disponibles cuando se aumenta la longitud del prefijo?

### 8.3.8 — CIDR

CIDR representa redes mediante prefijos de longitud variable y permite agregación de rutas. Un prefijo como /20 indica cuántos bits iniciales identifican la red; la agregación reduce tamaño de tablas cuando los bloques son contiguos y están correctamente asignados.

**Práctica guiada:** Interpreta varios prefijos (/16, /20, /24, /27) y calcula cuántos bits quedan para hosts.

**Actividad independiente:** Determina si dos redes pueden agregarse en un prefijo común sin incluir bloques ajenos.

**Criterios de aceptación:** Interpreta prefijo y explica agregación sin solapamiento indebido.

**Errores frecuentes:** Asumir que cualquier par de redes consecutivas puede resumirse en una ruta menor.

**Comprobación:** ¿Qué condiciones deben cumplirse para agregar dos prefijos en una ruta resumida?

### 8.3.9 — VLSM

VLSM permite asignar subredes de distintos tamaños dentro de un bloque, ajustando el prefijo a la cantidad de hosts requerida. El diseño suele comenzar por la subred mayor y asignar bloques alineados para evitar desperdicio y solapamientos.

**Práctica guiada:** Con un bloque de documentación, asigna subredes para 50, 20, 10 y 2 hosts. Calcula prefijos y verifica límites.

**Actividad independiente:** Crea un plan VLSM para departamentos y enlaces punto a punto, dejando reserva para crecimiento.

**Criterios de aceptación:** Todas las subredes cumplen capacidad, alineación y no se solapan.

**Errores frecuentes:** Asignar primero las redes pequeñas y fragmentar el espacio de forma que la subred mayor ya no quepa.

**Comprobación:** ¿Por qué conviene asignar primero las subredes que requieren más direcciones?

### 8.3.10 — Gateway

La puerta de enlace es el siguiente salto al que un host envía paquetes destinados a redes no locales. En IPv4/IPv6 se configura por interfaz o mediante mecanismos automáticos. Debe ser alcanzable en el enlace y coherente con rutas y políticas.

**Práctica guiada:** Consulta ruta por defecto con `ip route`/`ip -6 route` o `route print`; registra interfaz y siguiente salto.

**Actividad independiente:** Diagnostica un caso donde el host tiene IP correcta pero gateway incorrecto o inaccesible.

**Criterios de aceptación:** Explica siguiente salto y diferencia gateway de DNS y servidor DHCP.

**Errores frecuentes:** Asumir que gateway y DNS son el mismo servicio o que cualquier dirección de router puede utilizarse desde cualquier subred.

**Comprobación:** ¿Qué sucede con tráfico no local si no existe una ruta por defecto ni una ruta más específica?

### 8.3.11 — Broadcast

Broadcast IPv4 entrega un datagrama a todos los hosts del dominio de broadcast correspondiente. La dirección de broadcast dirigida depende del prefijo; 255.255.255.255 es broadcast limitado. Los routers normalmente no reenvían broadcasts dirigidos por defecto. IPv6 utiliza multicast en lugar de broadcast.

**Práctica guiada:** Calcula la dirección de broadcast de varias subredes de ejemplo y compara con multicast IPv6.

**Actividad independiente:** Explica por qué dividir una LAN en VLAN/subredes limita el alcance de broadcast.

**Criterios de aceptación:** Calcula broadcast correctamente y diferencia broadcast limitado, dirigido y multicast.

**Errores frecuentes:** Suponer que un broadcast IPv4 atraviesa routers o que IPv6 utiliza broadcast.

**Comprobación:** ¿Qué mecanismo utiliza IPv6 en lugar de broadcast?

### 8.3.12 — ARP

ARP resuelve una dirección IPv4 local a una dirección MAC dentro del enlace. El host consulta caché ARP y, si es necesario, difunde una solicitud; el equipo correspondiente responde. ARP no se utiliza para resolver direcciones IPv6, donde actúa Neighbor Discovery.

**Práctica guiada:** Consulta la caché con `ip neigh` o `arp -a` en un equipo propio. Relaciona una entrada con interfaz y estado.

**Actividad independiente:** Dibuja el intercambio ARP cuando un host envía tráfico a otro de su misma subred y cuando el destino está en otra red.

**Criterios de aceptación:** Explica que para destino remoto el host resuelve la MAC del gateway, no la MAC del host remoto.

**Errores frecuentes:** Creer que ARP resuelve nombres DNS o que el router consulta ARP para la dirección IP final de Internet.

**Comprobación:** ¿Qué dirección MAC busca un host cuando el destino IP está fuera de su subred?

### 8.3.13 — DHCP

DHCP asigna parámetros de red como dirección IP, máscara/prefijo, gateway, DNS y tiempo de concesión. En IPv4, el intercambio típico se describe como Discover, Offer, Request y Acknowledge. DHCP requiere controles frente a servidores no autorizados y agotamiento de pools.

**Práctica guiada:** Consulta parámetros de red obtenidos automáticamente en tu equipo y distingue dirección, gateway, DNS y duración de concesión si está disponible.

**Actividad independiente:** Dibuja DORA y explica cómo un relay permite atender clientes en otra subred.

**Criterios de aceptación:** Identifica los cuatro mensajes y los parámetros que recibe el cliente.

**Errores frecuentes:** Confundir DHCP con DNS o asumir que la asignación automática garantiza que la dirección sea correcta y segura.

**Comprobación:** ¿Qué función cumple DHCP relay cuando el servidor está en otra subred?

## 8.4 — Protocolos

### 8.4.1 — TCP

TCP es un protocolo de transporte orientado a conexión que ofrece flujo de bytes fiable y ordenado, control de flujo y control de congestión. Utiliza puertos, secuencias, ACK y retransmisiones. No conserva límites de mensajes de la aplicación.

**Práctica guiada:** Analiza una captura de laboratorio y localiza handshake SYN/SYN-ACK/ACK, puertos y números de secuencia.

**Actividad independiente:** Explica cómo TCP detecta pérdida y por qué una aplicación debe definir su propio encuadre de mensajes.

**Criterios de aceptación:** Describe establecimiento, fiabilidad y flujo de bytes.

**Errores frecuentes:** Afirmar que cada llamada de escritura equivale a un segmento o mensaje recibido.

**Comprobación:** ¿Qué problema resuelve el número de secuencia en TCP?

### 8.4.2 — UDP

UDP es un protocolo de transporte sin conexión que envía datagramas con encabezado reducido. No garantiza entrega, orden ni retransmisión; las aplicaciones pueden implementar mecanismos propios. Es útil cuando latencia, simplicidad o semántica de la aplicación justifican esas propiedades.

**Práctica guiada:** Inspecciona una captura UDP autorizada e identifica puertos, longitud y checksum cuando esté disponible.

**Actividad independiente:** Compara un caso de voz en tiempo real y una transferencia de archivo; justifica cuándo podría elegirse UDP o TCP.

**Criterios de aceptación:** Diferencia datagrama UDP de segmento TCP y explica qué garantías no ofrece UDP.

**Errores frecuentes:** Tratar UDP como inseguro por definición o asumir que no puede transportar aplicaciones fiables.

**Comprobación:** ¿Qué responsabilidades debe asumir una aplicación si necesita fiabilidad sobre UDP?

### 8.4.3 — ICMP

ICMP comunica errores y diagnósticos relacionados con IP. ping utiliza mensajes Echo Request/Reply, mientras traceroute aprovecha respuestas asociadas a TTL/Hop Limit y otros mecanismos. Filtrado ICMP puede afectar diagnóstico y descubrimiento de MTU.

**Práctica guiada:** Ejecuta ping hacia un destino propio o autorizado y registra pérdida y latencia. No interpretes ausencia de respuesta como prueba única de indisponibilidad.

**Actividad independiente:** Explica cómo traceroute identifica saltos y por qué algunos routers no responden.

**Criterios de aceptación:** Identifica función de ICMP y diferencia mensaje de control de protocolo de transporte.

**Errores frecuentes:** Confundir ICMP con TCP/UDP o concluir que un host está caído solo porque bloquea Echo Reply.

**Comprobación:** ¿Por qué un servicio puede funcionar aunque ping no reciba respuesta?

### 8.4.4 — DNS

DNS traduce nombres de dominio a registros como A, AAAA, MX, CNAME y TXT mediante una jerarquía distribuida y cachés. Los resolvers recursivos consultan servidores autoritativos; TTL controla cuánto tiempo puede conservarse una respuesta en caché.

**Práctica guiada:** Consulta un dominio propio o público con `dig` o `nslookup`; identifica tipo de registro, servidor consultado y TTL.

**Actividad independiente:** Diagnostica un caso donde una IP responde pero el nombre no resuelve; distingue problema de DNS de conectividad.

**Criterios de aceptación:** Explica resolver, zona, servidor autoritativo, caché y registros básicos.

**Errores frecuentes:** Confundir DNS con gateway o asumir que cambiar un registro se refleja instantáneamente por caché y TTL.

**Comprobación:** ¿Qué diferencia existe entre un resolver recursivo y un servidor autoritativo?

### 8.4.5 — HTTP

HTTP es un protocolo de aplicación de solicitud/respuesta utilizado para transferir recursos. Define métodos, URI, encabezados, códigos de estado y semántica de caché. HTTP por sí solo no cifra el tráfico ni autentica criptográficamente al servidor.

**Práctica guiada:** Consulta un endpoint público permitido con `curl -I` y registra método, código de estado y encabezados relevantes.

**Actividad independiente:** Diseña una petición GET y una POST ficticias; explica diferencias de semántica, idempotencia y exposición de datos.

**Criterios de aceptación:** Interpreta solicitud, respuesta, método y códigos de estado sin confundirlos.

**Errores frecuentes:** Asumir que POST siempre es seguro o que un código 200 demuestra que la lógica de negocio fue correcta.

**Comprobación:** ¿Qué información aporta el código de estado HTTP y qué no garantiza?

### 8.4.6 — HTTPS

HTTPS es HTTP protegido por TLS. TLS proporciona confidencialidad, integridad y autenticación del servidor mediante certificados y validación de nombre/cadena. La seguridad depende de configuración, versiones, certificados y verificación del cliente.

**Práctica guiada:** Ejecuta `curl -I https://example.com` o consulta un sitio permitido y observa el resultado de la validación TLS. No desactives la verificación del certificado.

**Actividad independiente:** Explica qué valida el cliente en el certificado y qué riesgo existe al ignorar advertencias TLS.

**Criterios de aceptación:** Distingue HTTP de HTTPS y describe autenticación, cifrado e integridad provistos por TLS.

**Errores frecuentes:** Tratar el candado como garantía de legitimidad del sitio o usar opciones que deshabilitan validación en producción.

**Comprobación:** ¿Qué protege TLS y qué tipo de fraude no evita por sí solo?

### 8.4.7 — SSH

SSH proporciona acceso remoto seguro y canales cifrados para administración y transferencia. La autenticación puede usar claves o contraseñas; la verificación de la clave del host ayuda a detectar suplantación. La configuración debe limitar usuarios, algoritmos y exposición.

**Práctica guiada:** Inspecciona la versión cliente con `ssh -V` y revisa una configuración de ejemplo sin conectarte a sistemas ajenos.

**Actividad independiente:** Diseña acceso administrativo con claves, passphrase, registro, cuentas nominativas y restricción por red.

**Criterios de aceptación:** Explica cifrado del canal, autenticación del usuario y verificación del host.

**Errores frecuentes:** Aceptar una nueva host key sin verificarla o compartir claves privadas entre administradores.

**Comprobación:** ¿Qué diferencia hay entre la clave del host y la clave privada del usuario?

### 8.4.8 — FTP

FTP transfiere archivos mediante un canal de control y canales de datos, con modos activo y pasivo. El FTP clásico no cifra credenciales ni contenido, por lo que no debe utilizarse para transferencias sensibles en redes no confiables.

**Práctica guiada:** Analiza un diagrama de conexión FTP activo y pasivo; no transmitas credenciales reales ni habilites un servidor expuesto.

**Actividad independiente:** Compara FTP clásico con SFTP y FTPS por canal, cifrado, puertos y administración.

**Criterios de aceptación:** Explica canales de control/datos y riesgos de FTP sin cifrado.

**Errores frecuentes:** Confundir FTP con SFTP o pensar que el modo pasivo añade cifrado.

**Comprobación:** ¿Qué información sensible puede quedar expuesta al usar FTP clásico?

### 8.4.9 — SFTP

SFTP es un protocolo de transferencia de archivos que funciona sobre SSH; no es simplemente FTP con TLS. Utiliza el canal SSH autenticado y cifrado, y su acceso depende de las cuentas y permisos del servidor.

**Práctica guiada:** Consulta documentación del cliente SFTP instalado y representa una sesión con un servidor de laboratorio autorizado. No uses credenciales ajenas.

**Actividad independiente:** Diseña una cuenta de transferencia restringida a un directorio y explica permisos y registro necesarios.

**Criterios de aceptación:** Diferencia SFTP, FTP y FTPS y explica su relación con SSH.

**Errores frecuentes:** Asumir que SFTP utiliza los mismos puertos y mecanismos de FTP clásico.

**Comprobación:** ¿Sobre qué protocolo se transporta SFTP?

### 8.4.10 — SMTP

SMTP transfiere correo entre clientes y servidores o entre servidores de correo. La entrega puede involucrar relay, autenticación, políticas antispam y TLS oportunista o requerido. La recepción de correo suele utilizar protocolos distintos, como IMAP o POP3.

**Práctica guiada:** Identifica registros MX de un dominio con `dig MX` y dibuja el flujo desde cliente de envío hasta servidor destinatario.

**Actividad independiente:** Explica diferencias entre envío SMTP, almacenamiento del buzón y lectura por IMAP/POP3.

**Criterios de aceptación:** Describe el papel de SMTP y reconoce la función de MX y relay.

**Errores frecuentes:** Confundir SMTP con el protocolo de lectura del buzón o asumir que TLS está siempre configurado de igual forma.

**Comprobación:** ¿Por qué SMTP no suele ser el protocolo que utiliza el usuario para leer su buzón?

### 8.4.11 — IMAP

IMAP permite acceder y administrar mensajes almacenados en el servidor, sincronizando carpetas y estados entre clientes. TLS protege la sesión cuando está correctamente configurado. Las políticas del servidor determinan almacenamiento, cuotas y retención.

**Práctica guiada:** Compara conceptualmente una cuenta IMAP en dos dispositivos y registra qué estados deben sincronizarse. No introduzcas credenciales en herramientas de terceros.

**Actividad independiente:** Diseña una política de buzón compartido con permisos, retención y autenticación reforzada.

**Criterios de aceptación:** Explica sincronización de mensajes y carpetas y distingue IMAP de SMTP.

**Errores frecuentes:** Tratar IMAP como protocolo de envío o almacenar contraseñas de correo en texto plano.

**Comprobación:** ¿Qué ventaja ofrece IMAP frente a descargar y eliminar mensajes del servidor?

### 8.4.12 — POP3

POP3 es un protocolo de acceso al correo con un modelo tradicional de descarga de mensajes. Las opciones de conservar copia en servidor dependen del cliente y servidor. POP3 no ofrece la misma sincronización de carpetas y estados que IMAP.

**Práctica guiada:** Compara los flujos conceptuales POP3 e IMAP sin introducir credenciales reales ni conectarte a servidores ajenos.

**Actividad independiente:** Explica qué ocurre cuando dos dispositivos acceden a una cuenta configurada para descargar y eliminar mensajes.

**Criterios de aceptación:** Diferencia modelo de descarga POP3 y sincronización IMAP.

**Errores frecuentes:** Afirmar que POP3 siempre elimina mensajes o que no puede operar protegido por TLS.

**Comprobación:** ¿Qué limitación presenta POP3 para usuarios que consultan el correo desde varios dispositivos?

### 8.4.13 — SMB

SMB permite compartir archivos, impresoras y otros recursos en redes Windows y también en otros sistemas mediante implementaciones compatibles. La seguridad depende de autenticación, firma/cifrado según versión, permisos de recurso compartido y ACL del sistema de archivos.

**Práctica guiada:** Inspecciona recursos compartidos de un laboratorio autorizado y distingue permiso SMB de permiso NTFS. No enumeres equipos ajenos.

**Actividad independiente:** Diseña una carpeta compartida con grupos de lectura/escritura y acceso mínimo; define auditoría y cifrado según el entorno.

**Criterios de aceptación:** Explica negociación, autenticación y combinación de permisos compartidos/NTFS.

**Errores frecuentes:** Habilitar SMBv1 sin necesidad o conceder permisos amplios para solucionar un problema puntual.

**Comprobación:** ¿Cómo se determina el acceso efectivo cuando se combinan permisos SMB y NTFS?

### 8.4.14 — LDAP

LDAP es un protocolo para consultar y modificar servicios de directorio mediante entradas organizadas jerárquicamente y atributos. Define operaciones de búsqueda, bind y modificación. La seguridad requiere TLS/StartTLS, autenticación adecuada y control de permisos; LDAP no equivale a Active Directory aunque AD lo implemente.

**Práctica guiada:** Examina un esquema LDIF ficticio y localiza DN, atributos y clases de objeto; no consultes directorios reales sin autorización.

**Actividad independiente:** Diseña una estructura de directorio para usuarios y grupos y especifica quién puede leer o modificar cada atributo.

**Criterios de aceptación:** Interpreta DN y atributos y explica operaciones básicas de LDAP.

**Errores frecuentes:** Confundir LDAP con una base de datos relacional o enviar credenciales en claro mediante una conexión no protegida.

**Comprobación:** ¿Qué representa el DN de una entrada LDAP?

### 8.4.15 — Kerberos

Kerberos es un protocolo de autenticación de red basado en tickets y un tercero de confianza (KDC). En entornos de dominio, los tickets permiten demostrar identidad sin enviar la contraseña a cada servicio. La sincronización horaria, protección de claves y configuración del realm son importantes.

**Práctica guiada:** Dibuja cliente, KDC, servicio y flujo simplificado de TGT y ticket de servicio; utiliza un escenario conceptual, no intentes extraer tickets reales.

**Actividad independiente:** Explica por qué la sincronización horaria y la protección de cuentas privilegiadas son críticas para Kerberos.

**Criterios de aceptación:** Identifica KDC, TGT y ticket de servicio y explica autenticación mutua en términos generales.

**Errores frecuentes:** Confundir Kerberos con cifrado de todo el tráfico de aplicación o compartir tickets como si fueran credenciales inocuas.

**Comprobación:** ¿Qué función cumple el TGT en el flujo de autenticación?

### 8.4.16 — WebSockets

WebSocket proporciona un canal de comunicación bidireccional persistente entre cliente y servidor, iniciado normalmente mediante un handshake HTTP Upgrade. Es útil para interacción en tiempo real; requiere autenticación, autorización por mensaje, validación de origen y límites de recursos.

**Práctica guiada:** Identifica en una captura o documentación el handshake Upgrade y diferencia una conexión WebSocket de solicitudes HTTP independientes.

**Actividad independiente:** Diseña un canal de notificaciones en tiempo real y define autorización, validación de mensajes, límites y cierre de sesión.

**Criterios de aceptación:** Explica handshake, comunicación bidireccional y controles de seguridad necesarios.

**Errores frecuentes:** Suponer que abrir el socket autentica cada operación o que HTTPS elimina la necesidad de validar mensajes.

**Comprobación:** ¿Qué riesgo aparece si el servidor autoriza la conexión pero no valida cada mensaje recibido?

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
