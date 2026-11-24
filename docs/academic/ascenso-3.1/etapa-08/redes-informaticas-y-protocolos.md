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

**Propósito y modelo.** Una LAN conecta dispositivos dentro de un ámbito limitado, como una vivienda, oficina o laboratorio. Ethernet conmutada y Wi-Fi son tecnologías habituales. El alcance físico no determina por sí solo la confianza: una LAN puede contener VLAN, controles de acceso, redes de invitados y segmentos con distintos niveles de sensibilidad.

**Ejemplo desarrollado.** En una oficina, estaciones de trabajo, impresoras y servidores pueden compartir infraestructura física, pero separarse lógicamente por VLAN y políticas de firewall. La segmentación reduce tráfico lateral y limita el impacto de una cuenta comprometida.

**Práctica guiada.** Dibuja una LAN pequeña con router, switch, punto de acceso, dos clientes y un servidor. Asigna subredes de documentación (sin configurar equipos reales) y señala qué tráfico debe permitirse entre segmentos.

**Actividad independiente.** Diseña una LAN para un aula de 20 equipos, una impresora y un servidor de archivos. Incluye direccionamiento, DHCP, Wi-Fi de invitados y controles de administración.

**Criterios de aceptación.** Diferencia alcance físico y segmentación lógica; identifica componentes y justifica el flujo autorizado.

**Errores frecuentes.** Asumir que todos los dispositivos conectados a un mismo switch deben confiar entre sí o que una LAN es segura por no ser pública.

**Comprobación.** ¿Qué ventaja de seguridad aporta separar invitados y equipos administrativos en VLAN distintas?

### 8.1.2 — Redes WAN

**Propósito y modelo.** Una WAN interconecta redes geográficamente separadas mediante enlaces de operadores, túneles, infraestructura privada o Internet. La disponibilidad, latencia, ancho de banda, redundancia y acuerdos de servicio condicionan su diseño. Una WAN no es sinónimo de Internet: puede ser privada o superpuesta.

**Ejemplo desarrollado.** Una empresa con sedes en dos ciudades puede usar enlaces del operador o túneles cifrados sobre Internet. La segunda opción reduce dependencia de circuitos dedicados, pero exige gestionar cifrado, disponibilidad y rutas.

**Práctica guiada.** Representa dos LAN remotas conectadas por una WAN. Marca routers de borde, rutas, enlaces redundantes y puntos donde aplicar cifrado y filtrado.

**Actividad independiente.** Compara enlace dedicado y VPN site-to-site sobre Internet para una empresa pequeña; evalúa costo, continuidad, confidencialidad y dependencia del proveedor.

**Criterios de aceptación.** Explica el propósito de WAN y distingue medio de transporte, servicio del operador y red lógica.

**Errores frecuentes.** Confundir una WAN con un único cable de larga distancia o asumir que una VPN resuelve disponibilidad y segmentación.

**Comprobación.** ¿Qué propiedades debe evaluar una organización además del ancho de banda al elegir un enlace WAN?

### 8.1.3 — Redes MAN

**Propósito y modelo.** Una MAN cubre un ámbito metropolitano y conecta redes de edificios o campus distribuidos en una ciudad. Puede utilizar fibra, Ethernet metropolitana o servicios del operador. La etiqueta MAN describe alcance y arquitectura general; no identifica un protocolo único.

**Ejemplo desarrollado.** Una universidad con varias sedes urbanas puede conectar sus edificios mediante fibra metropolitana y mantener subredes y políticas separadas por sede. El proveedor puede entregar un servicio Ethernet de capa 2 o una conectividad enrutada de capa 3.

**Práctica guiada.** Dibuja tres edificios conectados a través de una infraestructura metropolitana. Distingue el tramo administrado por la institución del tramo provisto por un operador.

**Actividad independiente.** Propón una MAN para tres sedes de una institución, incluyendo redundancia, segmentación y puntos de demarcación contractual.

**Criterios de aceptación.** Distingue LAN, MAN y WAN por alcance y explica que la tecnología concreta puede variar.

**Errores frecuentes.** Afirmar que MAN siempre utiliza una tecnología específica o que el proveedor y el cliente administran los mismos equipos.

**Comprobación.** ¿Qué diferencia operativa existe entre administrar la LAN de una sede y contratar la conectividad metropolitana?

### 8.1.4 — Internet

**Propósito y modelo.** Internet es una red global de redes autónomas que intercambian tráfico mediante IP y acuerdos de interconexión. No tiene un único propietario ni un centro de control universal. Sistemas autónomos, operadores, puntos de intercambio, DNS y protocolos de enrutamiento participan en su operación.

**Ejemplo desarrollado.** Al visitar un sitio, el dispositivo resuelve un nombre mediante DNS, obtiene una dirección IP y envía paquetes a través de routers de distintas redes. La ruta puede cambiar sin que el usuario perciba cada salto.

**Práctica guiada.** Consulta la resolución DNS de un dominio público autorizado con `dig` o `nslookup`, y observa la ruta con `traceroute` o `tracert`. Registra que algunos saltos pueden no responder a ICMP.

**Actividad independiente.** Dibuja el recorrido conceptual de una solicitud web desde una red doméstica hasta un servidor alojado en otro sistema autónomo.

**Criterios de aceptación.** Explica interconexión de redes, resolución de nombres y encaminamiento; distingue Internet de la Web.

**Errores frecuentes.** Usar Internet y Web como sinónimos o interpretar un salto sin respuesta como prueba concluyente de caída.

**Comprobación.** ¿Por qué la Web es un servicio que utiliza Internet, pero no constituye toda la infraestructura de Internet?

### 8.1.5 — Intranet

**Propósito y modelo.** Una intranet es un entorno de servicios y contenidos de uso interno de una organización. Puede usar tecnologías web estándar, DNS interno, autenticación corporativa y controles de acceso. Que sea interna no la hace automáticamente confiable: requiere segmentación, actualizaciones, identidad y monitoreo.

**Ejemplo desarrollado.** Un portal interno de recursos humanos puede ser accesible solo desde dispositivos administrados o mediante acceso remoto autenticado. El control debe aplicarse al servicio y a los datos, no únicamente a la ubicación de red.

**Práctica guiada.** Diseña el flujo de acceso a un portal interno: resolución de nombre, autenticación, autorización, conexión cifrada y registro. No intentes acceder a intranets ajenas.

**Actividad independiente.** Define controles mínimos para publicar una aplicación interna que maneja datos personales: segmentación, MFA, TLS, roles, logs y respaldo.

**Criterios de aceptación.** Diferencia intranet de Internet y extranet; identifica controles de identidad y red.

**Errores frecuentes.** Suponer que una dirección privada o un nombre interno garantiza que el usuario esté autorizado.

**Comprobación.** ¿Por qué una intranet también necesita controles de seguridad de aplicación e identidad?

### 8.1.6 — Extranet

**Propósito y modelo.** Una extranet habilita acceso controlado a determinados recursos internos para terceros, socios o clientes. La exposición debe limitarse a servicios concretos, con identidad verificable, autorización, segmentación, monitoreo y acuerdos de uso.

**Ejemplo desarrollado.** Un proveedor puede consultar órdenes de compra en un portal externo sin obtener acceso a la red administrativa completa. El portal debe mediar las operaciones y limitar los datos visibles a la relación comercial.

**Práctica guiada.** Dibuja una DMZ con portal de socios, firewall perimetral y servicios internos. Marca qué conexiones se permiten y cuáles se prohíben.

**Actividad independiente.** Diseña una extranet para intercambio de documentos con proveedores: autenticación, MFA, permisos por organización, expiración de cuentas y auditoría.

**Criterios de aceptación.** Explica diferencia entre extranet e intranet y delimita el acceso de terceros por servicio y función.

**Errores frecuentes.** Dar a un socio acceso VPN amplio cuando solo necesita una aplicación o mantener cuentas de terceros después de finalizar el contrato.

**Comprobación.** ¿Qué principio permite que un proveedor acceda a un portal sin tener acceso a toda la LAN corporativa?

### 8.1.7 — Cliente-servidor

**Propósito y modelo.** El modelo cliente-servidor separa consumidores de servicios y componentes que los proporcionan. Un cliente inicia solicitudes y un servidor escucha o procesa peticiones; ambos pueden ejecutarse en equipos físicos, VMs o procesos diferentes. La distinción es lógica y no implica necesariamente una máquina por rol.

**Ejemplo desarrollado.** Un navegador solicita una página a un servidor HTTP. El servidor recibe la conexión, aplica reglas de aplicación y devuelve una respuesta; puede delegar datos a un servidor de base de datos.

**Práctica guiada.** Representa navegador, servidor web y base de datos. Identifica protocolos, puertos y direcciones de origen/destino para cada intercambio.

**Actividad independiente.** Diseña una aplicación de tres capas y establece qué conexiones son necesarias entre cliente, frontend, backend y base de datos.

**Criterios de aceptación.** Identifica roles, flujo de solicitud/respuesta y dependencias entre servicios.

**Errores frecuentes.** Confundir cliente con usuario humano o exponer directamente una base de datos a Internet cuando un backend debe mediar el acceso.

**Comprobación.** ¿Qué ventaja de seguridad ofrece colocar una API entre el cliente y la base de datos?

### 8.1.8 — Peer-to-peer

**Propósito y modelo.** En una arquitectura peer-to-peer, los nodos pueden actuar como clientes y servidores según el intercambio. Puede distribuir carga y evitar un punto central único, pero complica descubrimiento, confianza, control de acceso, actualización y auditoría.

**Ejemplo desarrollado.** En una red P2P de distribución de archivos, cada nodo comparte fragmentos y descarga otros. La integridad debe comprobarse con hashes o firmas y el origen del contenido debe evaluarse por separado.

**Práctica guiada.** Dibuja una red de cuatro pares y marca quién ofrece y consume datos. Compara qué ocurre si un nodo deja de participar frente a una arquitectura centralizada.

**Actividad independiente.** Evalúa un diseño P2P para distribuir actualizaciones en una organización; incluye autenticidad del paquete, control de versiones, revocación y límites de ancho de banda.

**Criterios de aceptación.** Explica simetría de roles, ventajas y riesgos; distingue distribución descentralizada de confianza automática.

**Errores frecuentes.** Asumir que un archivo recibido de varios pares es auténtico o que descentralización elimina todos los puntos de falla.

**Comprobación.** ¿Por qué la verificación criptográfica sigue siendo necesaria en una red P2P?

### 8.1.9 — Router

**Propósito y modelo.** Un router reenvía paquetes IP entre redes usando una tabla de rutas. Selecciona la ruta más específica aplicable y, en caso de empate, aplica métricas y políticas del sistema. Puede ejecutar funciones adicionales como NAT, firewall o VPN, pero estas no definen su función básica de capa 3.

**Ejemplo desarrollado.** Un equipo con una ruta conectada a su LAN y una ruta por defecto hacia el gateway envía destinos remotos al siguiente salto. Si existe una ruta más específica, puede preferirse sobre la ruta por defecto.

**Práctica guiada.** Consulta tabla de rutas con `ip route` o `route print`. Identifica red conectada, gateway por defecto e interfaz. No cambies rutas en el host.

**Actividad independiente.** Dibuja dos subredes conectadas por un router y describe el siguiente salto para tres destinos, incluyendo uno sin ruta específica.

**Criterios de aceptación.** Explica reenvío IP, ruta más específica y gateway por defecto.

**Errores frecuentes.** Confundir router con switch o pensar que el gateway siempre es la dirección más alta/baja de una subred.

**Comprobación.** ¿Por qué una ruta más específica suele prevalecer sobre la ruta por defecto?

### 8.1.10 — Switch

**Propósito y modelo.** Un switch Ethernet aprende direcciones MAC de origen y mantiene una tabla de reenvío para decidir por qué puerto enviar tramas. En redes modernas puede soportar VLAN, enlaces troncales, STP, PoE y controles de capa 2. La tabla MAC no es una tabla de rutas IP.

**Ejemplo desarrollado.** Si el destino MAC es conocido, el switch reenvía la trama al puerto asociado; si es desconocido, puede inundarla dentro de la VLAN correspondiente, excluyendo el puerto de entrada.

**Práctica guiada.** Dibuja un switch con tres hosts y registra cómo aprende MAC al recibir tramas. Consulta la tabla MAC en un equipo de laboratorio administrado si tienes autorización.

**Actividad independiente.** Diseña VLAN separadas para usuarios, servidores y administración; identifica puertos de acceso y enlaces troncales.

**Criterios de aceptación.** Distingue conmutación MAC de enrutamiento IP y explica aprendizaje e inundación.

**Errores frecuentes.** Confundir la tabla MAC con ARP o conectar equipos no confiables a puertos de acceso corporativos sin control.

**Comprobación.** ¿Qué información utiliza un switch de capa 2 para seleccionar el puerto de salida?

### 8.1.11 — Firewall

**Propósito y modelo.** Un firewall aplica políticas sobre tráfico que atraviesa un punto de control. Puede filtrar por dirección, protocolo, puerto, estado de conexión, aplicación o identidad, según el producto. La política debe ser explícita, mínima y coherente con la arquitectura; reglas de entrada y salida tienen efectos distintos.

**Ejemplo desarrollado.** Una aplicación web pública puede aceptar TCP 443 desde Internet, pero solo permitir que el servidor web se comunique con la base de datos en un puerto interno concreto. El firewall no reemplaza autenticación ni validación de la aplicación.

**Práctica guiada.** Lee una tabla de reglas de laboratorio y clasifica origen, destino, protocolo, puerto, dirección y acción. No cambies el firewall de producción ni deshabilites protecciones para probar conectividad.

**Actividad independiente.** Construye una matriz de flujos para una aplicación de tres capas y convierte cada flujo necesario en una regla mínima.

**Criterios de aceptación.** Identifica cinco atributos de una regla y explica denegación por defecto y mínimo privilegio.

**Errores frecuentes.** Crear reglas Any/Any, olvidar tráfico de administración o considerar el firewall como sustituto de controles de aplicación.

**Comprobación.** ¿Qué riesgo introduce permitir cualquier origen hacia todos los puertos de un servidor?

### 8.1.12 — Gateway

**Propósito y modelo.** Gateway es un término contextual para un punto que conecta redes o traduce entre protocolos y dominios. En una LAN IP, el gateway por defecto suele ser la dirección del router al que se envía tráfico destinado a redes no locales. No todos los gateways son routers IP convencionales.

**Ejemplo desarrollado.** Un host consulta su máscara para decidir si el destino es local; si no lo es, entrega el paquete al siguiente salto configurado como gateway. Una dirección DNS no es automáticamente el gateway.

**Práctica guiada.** Consulta `ip route` o `ipconfig /all` e identifica gateway y DNS por separado. No cambies configuración de red del equipo.

**Actividad independiente.** Dado un host, máscara, destino y gateway, determina si el destino está en la subred local y si el tráfico requiere siguiente salto.

**Criterios de aceptación.** Diferencia gateway por defecto, router y servidor DNS; justifica el siguiente salto.

**Errores frecuentes.** Confundir puerta de enlace con DNS o configurar como gateway una dirección que no es alcanzable en el enlace local.

**Comprobación.** ¿Qué papel cumple el gateway cuando el destino no pertenece a la subred local?

### 8.1.13 — Access Point

**Propósito y modelo.** Un punto de acceso conecta estaciones Wi-Fi con una red de distribución, habitualmente Ethernet. Publica uno o más SSID y aplica seguridad inalámbrica, aislamiento de clientes y segmentación. El SSID identifica una red anunciada, no constituye por sí solo una barrera de seguridad.

**Ejemplo desarrollado.** Una red de invitados puede utilizar un SSID distinto y mapearse a una VLAN aislada. Ocultar el SSID no sustituye WPA2/WPA3, autenticación robusta ni segmentación.

**Práctica guiada.** Inspecciona la configuración de un AP de laboratorio: SSID, banda, cifrado, canal, VLAN y aislamiento de clientes. No cambies parámetros de una red que no administras.

**Actividad independiente.** Diseña Wi-Fi corporativo, invitados e IoT con SSID/VLAN, autenticación, controles de acceso y política de actualización.

**Criterios de aceptación.** Distingue AP de router, SSID de autenticación y segmentación lógica de ocultación del nombre.

**Errores frecuentes.** Usar cifrado obsoleto, compartir la contraseña corporativa con invitados o asumir que ocultar SSID evita accesos no autorizados.

**Comprobación.** ¿Por qué una red Wi-Fi de invitados debe estar aislada de los sistemas internos aunque utilice un SSID diferente?

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
