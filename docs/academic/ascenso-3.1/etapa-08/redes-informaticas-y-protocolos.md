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

**Propósito y modelo.** El modelo OSI es un marco conceptual de siete capas que ayuda a separar funciones de comunicación y localizar problemas. No es una pila de protocolos que todos los sistemas implementen literalmente. Cada capa ofrece servicios a la superior y utiliza servicios de la inferior.

**Ejemplo desarrollado.** Al abrir una página, la aplicación utiliza HTTP; las capas inferiores aportan transporte, direccionamiento y acceso al medio. Un problema puede estar en DNS, transporte, enrutamiento, enlace o aplicación, por lo que el modelo organiza el diagnóstico.

**Práctica guiada.** Clasifica DNS, TCP, IP, Ethernet y HTTP en la capa OSI más habitual, explicando cualquier simplificación o dependencia de implementación.

**Actividad independiente.** Construye una tabla con las siete capas, función, PDU orientativa, dirección/identificador asociado y un protocolo o tecnología representativa.

**Criterios de aceptación.** Describe el propósito del modelo y ubica tecnologías sin afirmar que el modelo determina exactamente todas las implementaciones.

**Errores frecuentes.** Tratar OSI como una implementación real obligatoria o memorizar capas sin relacionarlas con el flujo de datos.

**Comprobación.** ¿Cómo ayuda la separación por capas a aislar una falla de conectividad?

### 8.2.2 — Las siete capas OSI

**Propósito y modelo.** Las capas OSI se organizan desde la capa 1 Física, 2 Enlace, 3 Red, 4 Transporte, 5 Sesión, 6 Presentación y 7 Aplicación. Las funciones pueden combinarse o distribuirse de manera distinta en protocolos reales; el modelo sirve para describir responsabilidades y diagnosticar.

**Ejemplo desarrollado.** Un enlace Ethernet caído pertenece al ámbito físico/enlace; una ruta IP ausente corresponde a red; un puerto TCP que no escucha pertenece a transporte/servicio; una respuesta HTTP 500 se observa en aplicación.

**Práctica guiada.** Clasifica cinco incidentes sintéticos por capa probable y anota qué evidencia recopilarías antes de confirmar la causa.

**Actividad independiente.** Prepara un mapa de capas con ejemplo de falla y herramienta de diagnóstico para cada una.

**Criterios de aceptación.** Nombra y ordena las siete capas y justifica la ubicación de al menos cinco incidentes.

**Errores frecuentes.** Asignar una falla a una sola capa sin considerar dependencias o confundir capa de aplicación con interfaz gráfica.

**Comprobación.** ¿Por qué un error visible en una aplicación puede originarse en una capa inferior?

### 8.2.3 — Modelo TCP/IP

**Propósito y modelo.** El modelo TCP/IP agrupa funciones en capas de acceso a red, Internet, transporte y aplicación (las denominaciones pueden variar entre fuentes). Es una descripción práctica de la arquitectura de Internet y no coincide uno a uno con OSI.

**Ejemplo desarrollado.** HTTP pertenece a aplicación, TCP a transporte, IP a Internet y Ethernet o Wi-Fi al acceso a red. DNS es aplicación aunque resuelva nombres que luego se usan en IP.

**Práctica guiada.** Mapea HTTP, DNS, TCP, UDP, IPv4, IPv6, Ethernet y Wi-Fi al modelo TCP/IP. Compara la agrupación con la tabla OSI.

**Actividad independiente.** Describe el flujo de una solicitud HTTPS utilizando las capas TCP/IP y señala dónde se producen resolución DNS, establecimiento TCP y negociación TLS.

**Criterios de aceptación.** Identifica las cuatro capas y explica al menos dos diferencias de agrupación respecto a OSI.

**Errores frecuentes.** Afirmar que OSI y TCP/IP tienen idéntico número de capas o colocar DNS en la capa de transporte.

**Comprobación.** ¿Por qué TCP/IP es una arquitectura de protocolos y OSI se utiliza principalmente como modelo de referencia?

### 8.2.4 — Encapsulamiento

**Propósito y modelo.** El encapsulamiento añade información de control al dato al descender por las capas: cabeceras y, en ciertos niveles, tráileres. Una aplicación genera datos; transporte añade información de puertos y control; IP incorpora direcciones; enlace agrega direcciones MAC y verificación de trama.

**Ejemplo desarrollado.** Un segmento TCP viaja dentro de un paquete IP que se transmite en una trama Ethernet. Cada router procesa la cabecera de enlace entrante y crea una nueva para el siguiente enlace, mientras la información IP normalmente conserva sus extremos salvo traducciones o túneles.

**Práctica guiada.** Dibuja los datos de una petición HTTP encapsulados en TCP, IP y Ethernet. Etiqueta puertos, direcciones IP y MAC, sin usar direcciones reales sensibles.

**Actividad independiente.** Explica qué campos cambian al cruzar un router y cuáles suelen mantenerse en una ruta sin NAT.

**Criterios de aceptación.** Describe orden de encapsulamiento y diferencia cabeceras de transporte, red y enlace.

**Errores frecuentes.** Afirmar que la dirección MAC de origen/destino permanece igual en todos los saltos o confundir puerto TCP con puerto físico.

**Comprobación.** ¿Por qué un router reemplaza la trama de enlace al reenviar un paquete por otra interfaz?

### 8.2.5 — Desencapsulamiento

**Propósito y modelo.** El desencapsulamiento es el proceso inverso en el receptor: cada capa interpreta y retira la información de control correspondiente y entrega la carga a la capa superior. La validación puede incluir integridad de trama, destino IP, puerto, estado de transporte y formato de aplicación.

**Ejemplo desarrollado.** La NIC recibe una trama, la capa de red procesa el paquete IP y TCP entrega el flujo al socket asociado al puerto. Finalmente la aplicación interpreta los datos según el protocolo utilizado.

**Práctica guiada.** Utiliza un diagrama de una trama Ethernet que contiene IPv4, TCP y datos HTTP. Identifica qué componente consume cada cabecera al recibirla.

**Actividad independiente.** Describe qué ocurre si la trama llega correctamente pero el puerto de destino no tiene un proceso escuchando.

**Criterios de aceptación.** Explica el orden de procesamiento y distingue recepción de enlace, entrega IP y demultiplexación de transporte.

**Errores frecuentes.** Suponer que recibir una trama garantiza que la aplicación recibirá datos o que cada capa valida la misma información.

**Comprobación.** ¿Qué sucede si el paquete IP llega al host, pero no existe un socket asociado al puerto TCP de destino?

### 8.2.6 — Paquetes

**Propósito y modelo.** En redes IP, paquete suele referirse a la unidad de datos de la capa de red (datagrama IP). Contiene cabecera con direcciones y campos de control, además de una carga que puede transportar un segmento TCP, datagrama UDP u otro protocolo. El tamaño y fragmentación dependen de MTU y versión IP.

**Ejemplo desarrollado.** Un paquete IP puede atravesar varios routers y cambiar su encapsulamiento de enlace en cada salto. La dirección IP de destino orienta el encaminamiento, mientras la MAC identifica el siguiente salto en la red local.

**Práctica guiada.** Examina una captura de laboratorio en Wireshark y localiza un paquete IPv4 o IPv6. Identifica origen, destino, protocolo superior y longitud.

**Actividad independiente.** Explica cómo un router decide el siguiente salto sin necesitar conocer el puerto TCP de la aplicación.

**Criterios de aceptación.** Diferencia paquete IP de trama Ethernet y segmento TCP; identifica campos esenciales.

**Errores frecuentes.** Usar paquete, trama y segmento como sinónimos o asumir que las direcciones MAC identifican extremos de Internet.

**Comprobación.** ¿Qué dirección utiliza el router para tomar una decisión de encaminamiento IP?

### 8.2.7 — Tramas

**Propósito y modelo.** Una trama es una unidad de datos de enlace que transporta un paquete o carga superior sobre un medio local. En Ethernet incluye direcciones MAC, tipo/longitud, datos y secuencia de verificación FCS. La trama se interpreta dentro del dominio de enlace y puede cambiar en cada salto enrutado.

**Ejemplo desarrollado.** Un host envía una trama Ethernet a la MAC del gateway cuando el destino IP está fuera de su subred. El router recibe la trama, procesa el paquete IP y genera otra trama para la interfaz de salida.

**Práctica guiada.** En una captura de Wireshark filtra tráfico Ethernet y localiza MAC de origen/destino y tipo EtherType. Relaciona la carga con el paquete IP transportado.

**Actividad independiente.** Dibuja dos tramas distintas para el mismo paquete IP antes y después de cruzar un router, indicando qué campos cambian.

**Criterios de aceptación.** Diferencia trama de paquete y explica el alcance local de las direcciones MAC.

**Errores frecuentes.** Suponer que la MAC del equipo remoto aparece directamente en todas las tramas del camino.

**Comprobación.** ¿Por qué la MAC destino de una trama puede ser la del router y no la del servidor remoto?

### 8.2.8 — Segmentos

**Propósito y modelo.** En TCP, un segmento contiene cabecera TCP y datos de aplicación. Incluye puertos, números de secuencia y acuse, flags, ventana y checksum. En UDP la unidad se denomina datagrama, aunque algunos materiales usan términos genéricos. La segmentación permite transportar flujos y controlar entrega ordenada.

**Ejemplo desarrollado.** Un flujo TCP puede dividir datos en varios segmentos; el receptor utiliza números de secuencia para reordenar y detectar pérdidas. Un segmento no equivale a un mensaje completo de aplicación.

**Práctica guiada.** Examina una captura TCP de laboratorio y localiza puertos, flags SYN/ACK, números de secuencia y longitud. No captures tráfico de terceros sin autorización.

**Actividad independiente.** Explica el establecimiento TCP de tres vías y representa cómo un segmento perdido puede provocar retransmisión.

**Criterios de aceptación.** Identifica campos TCP y diferencia segmento, paquete y trama.

**Errores frecuentes.** Suponer que cada segmento corresponde a una sola llamada de escritura de la aplicación o que TCP conserva límites de mensajes.

**Comprobación.** ¿Por qué TCP es un flujo de bytes y no un protocolo que preserve automáticamente los límites de mensajes?

### 8.2.9 — MTU

**Propósito y modelo.** La MTU define el tamaño máximo de unidad de datos que puede transportar una interfaz o enlace sin fragmentación a ese nivel. En Ethernet común se utiliza frecuentemente MTU IP de 1500 bytes, pero existen otros valores. Túneles, VPN y encapsulamientos reducen el espacio disponible para la carga.

**Ejemplo desarrollado.** Si un paquete excede la MTU de un enlace, IPv4 puede fragmentarse según DF y comportamiento de la ruta; IPv6 no fragmenta routers intermedios y depende de Path MTU Discovery y del origen. Una MTU incoherente puede causar fallos selectivos.

**Práctica guiada.** Consulta MTU de interfaces con `ip link` o `netsh interface ipv4 show subinterfaces`. No cambies valores en una red productiva. Compara el MTU configurado con el tamaño de ping permitido por tu sistema.

**Actividad independiente.** Analiza una VPN con sobrecarga de encapsulamiento y explica por qué una página pequeña carga pero una transferencia grande se bloquea.

**Criterios de aceptación.** Define MTU, diferencia fragmentación IPv4/IPv6 y relaciona túneles con sobrecarga.

**Errores frecuentes.** Confundir MTU con ancho de banda o reducirla arbitrariamente sin medir la ruta.

**Comprobación.** ¿Cómo puede una MTU incorrecta provocar fallos que parecen intermitentes en aplicaciones?

## 8.3 — Direccionamiento

### 8.3.1 — Dirección MAC

**Propósito y modelo.** Una dirección MAC identifica una interfaz en una tecnología de enlace como Ethernet o Wi-Fi. En Ethernet tradicional tiene 48 bits y suele expresarse en hexadecimal. Puede ser globalmente administrada o localmente administrada; sistemas modernos también pueden usar direcciones aleatorias para privacidad.

**Ejemplo desarrollado.** En una LAN, el host necesita conocer la MAC del siguiente salto para construir una trama. Si el destino IP está fuera de la subred, normalmente resuelve la MAC del gateway, no la del servidor remoto.

**Práctica guiada.** Consulta interfaces con `ip link`, `ipconfig /all` o `getmac`. Identifica formato, interfaz y estado; evita publicar MAC de redes personales.

**Actividad independiente.** Dibuja un intercambio ARP entre dos hosts de una misma subred y explica qué ocurre cuando el destino está en otra red.

**Criterios de aceptación.** Identifica longitud y formato de MAC y diferencia identificador de enlace de dirección IP.

**Errores frecuentes.** Tratar la MAC como identificador permanente de una persona o asumir que nunca puede cambiarse o aleatorizarse.

**Comprobación.** ¿Por qué la MAC de destino de una trama suele corresponder al siguiente salto local?

### 8.3.2 — IPv4

**Propósito y modelo.** IPv4 utiliza direcciones de 32 bits representadas normalmente en cuatro octetos decimales. La dirección y la máscara determinan la porción de red y host; el enrutamiento utiliza prefijos. Direcciones privadas, públicas, loopback, link-local y reservadas tienen alcances distintos.

**Ejemplo desarrollado.** En 192.0.2.10/24, la red es 192.0.2.0/24 y la dirección de host se interpreta dentro de ese prefijo. 192.0.2.0/24 está reservado para documentación y no debe tratarse como un rango público de producción.

**Práctica guiada.** Interpreta direcciones de documentación de RFC 5737 y calcula red, broadcast y rango de host para prefijos /24 y /26. No escanees rangos públicos.

**Actividad independiente.** Diseña un plan IPv4 para tres VLAN con tamaños diferentes y reserva espacio para crecimiento.

**Criterios de aceptación.** Reconoce 32 bits, interpreta CIDR y distingue rangos privados y de documentación.

**Errores frecuentes.** Asumir que toda dirección no privada es enrutable globalmente o usar rangos de documentación en producción.

**Comprobación.** ¿Qué información aporta el prefijo junto a una dirección IPv4?

### 8.3.3 — IPv6

**Propósito y modelo.** IPv6 utiliza direcciones de 128 bits, expresadas en grupos hexadecimales y comprimibles mediante reglas de ceros. Incluye unicast, multicast y anycast; no utiliza broadcast. Neighbor Discovery sustituye funciones que en IPv4 se asocian a ARP. La configuración puede ser estática, SLAAC o DHCPv6 según red.

**Ejemplo desarrollado.** 2001:db8::10 es una dirección de documentación. El prefijo /64 es habitual en redes LAN, pero el diseño depende de la arquitectura y políticas del entorno.

**Práctica guiada.** Practica expansión y compresión de direcciones IPv6 y reconoce ::1, :: y 2001:db8::/32. Consulta interfaces con `ip -6 addr` o `ipconfig`.

**Actividad independiente.** Diseña un esquema IPv6 para tres segmentos y explica cómo se asignan prefijos y se anuncia el router.

**Criterios de aceptación.** Interpreta 128 bits, comprime correctamente direcciones y diferencia link-local, loopback y global unicast.

**Errores frecuentes.** Escribir más de un :: en una dirección o suponer que IPv6 elimina la necesidad de firewall.

**Comprobación.** ¿Por qué IPv6 utiliza multicast y Neighbor Discovery en lugar de broadcast y ARP?

### 8.3.4 — IP pública

**Propósito y modelo.** Una dirección IP pública es globalmente enrutable en el contexto de Internet, sujeta a asignación y políticas de operadores. No garantiza que un servicio sea alcanzable: pueden existir filtros, NAT, firewalls, rutas ausentes o restricciones del proveedor. La geolocalización IP es aproximada y no identifica con precisión a una persona.

**Ejemplo desarrollado.** Un router doméstico puede tener una dirección pública en su interfaz WAN y utilizar direcciones privadas en la LAN mediante NAT. CGNAT puede hacer que la dirección observada externamente no esté asignada directamente al router del cliente.

**Práctica guiada.** Distingue dirección WAN del router y dirección LAN en una configuración propia. No publiques datos de tu conexión ni realices escaneos externos.

**Actividad independiente.** Explica por qué un servidor doméstico puede no aceptar conexiones entrantes aunque un servicio de consulta muestre una IP pública.

**Criterios de aceptación.** Define alcance global y diferencia dirección pública de servicio expuesto o accesible.

**Errores frecuentes.** Confundir IP pública con IP fija o atribuir identidad personal precisa mediante geolocalización.

**Comprobación.** ¿Qué factores, además de la dirección pública, determinan si un servicio puede recibir conexiones?

### 8.3.5 — IP privada

**Propósito y modelo.** IPv4 define rangos privados para redes internas: 10.0.0.0/8, 172.16.0.0/12 y 192.168.0.0/16. No se enrutan globalmente en Internet y suelen traducirse mediante NAT para acceder a redes públicas. Su reutilización entre organizaciones exige evitar solapamientos al conectar redes.

**Ejemplo desarrollado.** Dos sedes que utilizan 192.168.1.0/24 pueden tener conflictos al unirse por VPN; será necesario renumerar o utilizar mecanismos de traducción cuidadosamente diseñados.

**Práctica guiada.** Clasifica direcciones de ejemplo como privadas o no privadas y reconoce que 169.254.0.0/16 es link-local, no rango privado RFC1918.

**Actividad independiente.** Diseña rangos privados no solapados para sede central, sucursal y laboratorio, reservando espacio para expansión.

**Criterios de aceptación.** Reconoce los tres bloques RFC1918 y explica el problema de solapamiento.

**Errores frecuentes.** Considerar todo lo que no es público como RFC1918 o usar rangos idénticos en redes que deben interconectarse.

**Comprobación.** ¿Por qué dos redes privadas con el mismo prefijo pueden impedir una VPN site-to-site sencilla?

### 8.3.6 — Máscaras

**Propósito y modelo.** La máscara IPv4 identifica qué bits de una dirección pertenecen al prefijo de red y cuáles al identificador de host. Puede escribirse en decimal punteado o como longitud CIDR. La operación AND bit a bit entre IP y máscara obtiene la dirección de red.

**Ejemplo desarrollado.** /26 equivale a 255.255.255.192: los primeros 26 bits representan red y quedan 6 bits de host. En una subred IPv4 convencional, dos direcciones se reservan para red y broadcast; hay excepciones como /31 en enlaces punto a punto.

**Práctica guiada.** Convierte /24, /26, /27 y /30 a máscara decimal. Calcula la red para una dirección de laboratorio usando AND binario.

**Actividad independiente.** Resuelve cinco ejercicios de IP/prefijo e incluye red, broadcast y rango asignable, indicando los supuestos de subred convencional.

**Criterios de aceptación.** Convierte prefijo a máscara y calcula dirección de red con operaciones binarias.

**Errores frecuentes.** Contar bits desde cero o aplicar la regla de dos direcciones reservadas sin considerar casos especiales.

**Comprobación.** ¿Qué significa que una máscara tenga 26 bits a uno consecutivos?

### 8.3.7 — Subnetting

**Propósito y modelo.** Subnetting divide un bloque IP en subredes más pequeñas mediante prefijos más largos. Permite separar dominios de broadcast IPv4, asignar direcciones según necesidad y aplicar controles de red. El diseño debe considerar crecimiento, gateways, reservas y rutas.

**Ejemplo desarrollado.** Dividir 192.0.2.0/24 en cuatro subredes iguales requiere tomar dos bits adicionales y produce cuatro /26. Los rangos de documentación evitan confundir el ejercicio con redes reales.

**Práctica guiada.** Divide 198.51.100.0/24 en cuatro /26 y calcula para cada una red, broadcast y hosts utilizables.

**Actividad independiente.** Asigna subredes de tamaños distintos a tres departamentos y un segmento de servidores, dejando margen para crecimiento.

**Criterios de aceptación.** Calcula número de subredes, tamaño de bloque y rangos sin solapamiento.

**Errores frecuentes.** Crear subredes que se superponen, olvidar gateway/reservas o asignar el broadcast a un host.

**Comprobación.** ¿Qué cambia en una subred cuando el prefijo pasa de /24 a /26?

### 8.3.8 — CIDR

**Propósito y modelo.** CIDR representa redes mediante una dirección y un prefijo de longitud variable, evitando depender de clases A/B/C. Permite agregación de rutas y asignación más flexible. La selección de ruta utiliza el prefijo más largo que coincide con el destino.

**Ejemplo desarrollado.** 203.0.113.0/24 resume 256 direcciones de documentación. Una ruta /25 más específica puede prevalecer sobre una /24 para la mitad del bloque.

**Práctica guiada.** Interpreta /20, /24, /27 y /30; calcula número de direcciones totales y compara dos rutas que coinciden con una IP de destino.

**Actividad independiente.** Resume un conjunto de subredes contiguas en un prefijo agregado cuando sea posible y demuestra que no incluyes direcciones ajenas.

**Criterios de aceptación.** Explica prefijo, agregación y longest-prefix match.

**Errores frecuentes.** Confundir número de hosts con total de direcciones o resumir rangos no contiguos en un prefijo demasiado amplio.

**Comprobación.** ¿Por qué un router elige una ruta /25 frente a una ruta /24 que también coincide?

### 8.3.9 — VLSM

**Propósito y modelo.** VLSM permite asignar prefijos de longitudes diferentes dentro de un bloque mayor, ajustando el tamaño de cada subred a su necesidad. Para evitar solapamientos, se asignan primero las redes más grandes y se alinean los bloques en límites válidos.

**Ejemplo desarrollado.** Una red que necesita 50 hosts requiere al menos 6 bits de host en una subred convencional IPv4, por lo que un /26 ofrece 62 direcciones utilizables. Un segmento de 10 hosts puede utilizar /28, con 14 utilizables.

**Práctica guiada.** Distribuye 192.0.2.0/24 para 50, 20, 10 y 2 hosts. Asigna bloques desde el mayor al menor y verifica límites y solapamiento.

**Actividad independiente.** Resuelve un diseño VLSM para cuatro departamentos y dos enlaces punto a punto; justifica las excepciones de enlaces /31 si las utilizas.

**Criterios de aceptación.** Selecciona prefijos según capacidad, alinea bloques y comprueba que todos caben en el bloque padre.

**Errores frecuentes.** Asignar primero las redes pequeñas, iniciar un bloque en dirección no alineada o olvidar crecimiento.

**Comprobación.** ¿Por qué conviene asignar primero la subred de mayor tamaño?

### 8.3.10 — Gateway

**Propósito y modelo.** En una red IP, el gateway por defecto es el siguiente salto usado cuando la tabla de rutas no contiene una ruta más específica. Debe ser alcanzable por una interfaz local y pertenecer a un segmento adecuado. Un host puede tener varios gateways o rutas según la política y el sistema operativo.

**Ejemplo desarrollado.** Un equipo 192.0.2.10/24 envía tráfico a 192.0.2.20 directamente en su LAN; para 198.51.100.10 utiliza el gateway de su subred. Las direcciones son de documentación.

**Práctica guiada.** Consulta rutas con `ip route` o `route print`. Identifica ruta conectada y ruta por defecto. No agregues rutas en el equipo anfitrión.

**Actividad independiente.** Dadas tres direcciones destino, determina si el host las alcanza directamente o utiliza el gateway, justificando con prefijo.

**Criterios de aceptación.** Explica siguiente salto y diferencia gateway de DNS y servidor proxy.

**Errores frecuentes.** Configurar gateway fuera del enlace local o creer que el gateway es siempre un servidor DNS.

**Comprobación.** ¿Cómo decide un host si debe enviar un paquete directamente o entregarlo al gateway?

### 8.3.11 — Broadcast

**Propósito y modelo.** En IPv4, la dirección de broadcast de una subred convencional identifica el destino para entregar una trama IP a todos los hosts del segmento. La dirección dirigida de broadcast se calcula poniendo a uno los bits de host. Los routers suelen bloquear su reenvío por defecto para evitar amplificación. IPv6 no utiliza broadcast.

**Ejemplo desarrollado.** En 192.0.2.0/26, la dirección de red es .0 y el broadcast dirigido es .63. Los hosts convencionales utilizables van de .1 a .62.

**Práctica guiada.** Calcula broadcast de /24, /26 y /28 con rangos de documentación. Verifica los resultados con una calculadora local o una operación binaria independiente.

**Actividad independiente.** Explica la diferencia entre broadcast de capa 2, broadcast IPv4 y multicast IPv6, incluyendo alcance.

**Criterios de aceptación.** Calcula broadcast y diferencia su función de multicast y unicast.

**Errores frecuentes.** Asignar broadcast a un host o asumir que broadcast IPv4 atraviesa routers de forma general.

**Comprobación.** ¿Por qué IPv6 utiliza multicast en lugar de broadcast?

### 8.3.12 — ARP

**Propósito y modelo.** ARP resuelve una dirección IPv4 de siguiente salto a una dirección MAC en un enlace local. Las solicitudes suelen difundirse en el segmento y las respuestas identifican la MAC asociada. ARP no atraviesa routers como una consulta de extremo a extremo; cada enlace tiene su propio contexto.

**Ejemplo desarrollado.** Si 192.0.2.10 necesita enviar a 198.51.100.20 y el gateway es 192.0.2.1, resuelve la MAC de 192.0.2.1. No busca la MAC del host remoto.

**Práctica guiada.** Consulta caché ARP/neighbor con `ip neigh` o `arp -a`. Identifica IP, MAC y estado. No realices envenenamiento ARP ni pruebas de suplantación fuera de laboratorio autorizado.

**Actividad independiente.** Dibuja solicitud y respuesta ARP para un destino local y compara con destino remoto a través del gateway.

**Criterios de aceptación.** Explica solicitud broadcast, respuesta y alcance local; diferencia ARP de DNS.

**Errores frecuentes.** Suponer que ARP resuelve nombres de dominio o que la MAC del destino remoto se aprende en la LAN de origen.

**Comprobación.** ¿Qué dirección MAC consulta un host cuando el destino IP está fuera de su subred?

### 8.3.13 — DHCP

**Propósito y modelo.** DHCP asigna parámetros de red como dirección IP, máscara/prefijo, gateway, DNS y tiempo de concesión. En IPv4 el intercambio típico se describe como Discover, Offer, Request, Acknowledge (DORA). Los servidores y relay agents deben configurarse para evitar asignaciones no autorizadas y conflictos.

**Ejemplo desarrollado.** Un cliente que inicia en una VLAN emite DHCP Discover; un servidor o relay permite localizar una oferta. Las reservas vinculan una asignación con un identificador del cliente, que no siempre debe asumirse idéntico a una MAC en todos los entornos.

**Práctica guiada.** Consulta concesión y servidor DHCP con `ipconfig /all` o `nmcli`/herramientas del sistema. No levantes un servidor DHCP en una LAN compartida.

**Actividad independiente.** Diseña un ámbito DHCP para una VLAN con rango, exclusiones, reservas, duración y opciones de gateway/DNS.

**Criterios de aceptación.** Describe DORA y diferencia servidor DHCP, relay y configuración estática.

**Errores frecuentes.** Crear un servidor DHCP no autorizado, solapar rangos estáticos y dinámicos o asignar DNS/gateway incorrectos.

**Comprobación.** ¿Qué función cumple un relay DHCP cuando el servidor está en otra subred?

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
