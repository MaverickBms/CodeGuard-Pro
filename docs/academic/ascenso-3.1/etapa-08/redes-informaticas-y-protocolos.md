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

**Laboratorio de profundización — Mapa físico y lógico de una LAN.**

1. Dibuja tres equipos, un switch y el router de salida. 2. Asigna direcciones RFC1918 ficticias dentro de una misma subred. 3. Identifica enlaces físicos, dominio de broadcast y gateway. 4. Describe qué cambiaría al separar dos grupos en VLAN distintas.

**Evidencia esperada.** El diagrama distingue topología física y lógica, switch y router, subred y dominio de broadcast.

**Seguridad y límites.** Usar direcciones de documentación o rangos privados de laboratorio; no escanear redes ajenas.

**Registro sugerido.** Anota topología, direccionamiento de laboratorio, herramientas, resultados y límites de la observación. No marques la práctica como ejecutada sin evidencia real.

### 8.1.2 — Redes WAN

**Propósito y modelo.** Una WAN interconecta redes geográficamente separadas mediante enlaces de operadores, túneles, infraestructura privada o Internet. La disponibilidad, latencia, ancho de banda, redundancia y acuerdos de servicio condicionan su diseño. Una WAN no es sinónimo de Internet: puede ser privada o superpuesta.

**Ejemplo desarrollado.** Una empresa con sedes en dos ciudades puede usar enlaces del operador o túneles cifrados sobre Internet. La segunda opción reduce dependencia de circuitos dedicados, pero exige gestionar cifrado, disponibilidad y rutas.

**Práctica guiada.** Representa dos LAN remotas conectadas por una WAN. Marca routers de borde, rutas, enlaces redundantes y puntos donde aplicar cifrado y filtrado.

**Actividad independiente.** Compara enlace dedicado y VPN site-to-site sobre Internet para una empresa pequeña; evalúa costo, continuidad, confidencialidad y dependencia del proveedor.

**Criterios de aceptación.** Explica el propósito de WAN y distingue medio de transporte, servicio del operador y red lógica.

**Errores frecuentes.** Confundir una WAN con un único cable de larga distancia o asumir que una VPN resuelve disponibilidad y segmentación.

**Comprobación.** ¿Qué propiedades debe evaluar una organización además del ancho de banda al elegir un enlace WAN?

**Laboratorio de profundización — Diseño de conectividad entre sedes.**

1. Dibuja dos LAN en ubicaciones distintas y un enlace WAN entre routers. 2. Identifica proveedor, demarcación, direccionamiento y rutas. 3. Compara conectividad privada, Internet con VPN y enlace dedicado. 4. Registra disponibilidad y redundancia esperadas.

**Evidencia esperada.** La propuesta diferencia LAN y WAN, identifica puntos de fallo y explica la necesidad de routing entre sedes.

**Seguridad y límites.** No publicar topologías, direcciones o credenciales reales de una organización.

**Registro sugerido.** Anota topología, direccionamiento de laboratorio, herramientas, resultados y límites de la observación. No marques la práctica como ejecutada sin evidencia real.

### 8.1.3 — Redes MAN

**Propósito y modelo.** Una MAN cubre un ámbito metropolitano y conecta redes de edificios o campus distribuidos en una ciudad. Puede utilizar fibra, Ethernet metropolitana o servicios del operador. La etiqueta MAN describe alcance y arquitectura general; no identifica un protocolo único.

**Ejemplo desarrollado.** Una universidad con varias sedes urbanas puede conectar sus edificios mediante fibra metropolitana y mantener subredes y políticas separadas por sede. El proveedor puede entregar un servicio Ethernet de capa 2 o una conectividad enrutada de capa 3.

**Práctica guiada.** Dibuja tres edificios conectados a través de una infraestructura metropolitana. Distingue el tramo administrado por la institución del tramo provisto por un operador.

**Actividad independiente.** Propón una MAN para tres sedes de una institución, incluyendo redundancia, segmentación y puntos de demarcación contractual.

**Criterios de aceptación.** Distingue LAN, MAN y WAN por alcance y explica que la tecnología concreta puede variar.

**Errores frecuentes.** Afirmar que MAN siempre utiliza una tecnología específica o que el proveedor y el cliente administran los mismos equipos.

**Comprobación.** ¿Qué diferencia operativa existe entre administrar la LAN de una sede y contratar la conectividad metropolitana?

**Laboratorio de profundización — Caso de interconexión metropolitana.**

1. Diseña tres edificios de una misma ciudad conectados a una red metropolitana. 2. Identifica enlaces de acceso y agregación. 3. Compara fibra, Ethernet metropolitana y enlaces inalámbricos según latencia, disponibilidad y distancia.

**Evidencia esperada.** El diseño explica alcance metropolitano y compara tecnologías mediante criterios verificables.

**Seguridad y límites.** No asumir que MAN es una tecnología específica; es una clasificación por alcance y diseño.

**Registro sugerido.** Anota topología, direccionamiento de laboratorio, herramientas, resultados y límites de la observación. No marques la práctica como ejecutada sin evidencia real.

### 8.1.4 — Internet

**Propósito y modelo.** Internet es una red global de redes autónomas que intercambian tráfico mediante IP y acuerdos de interconexión. No tiene un único propietario ni un centro de control universal. Sistemas autónomos, operadores, puntos de intercambio, DNS y protocolos de enrutamiento participan en su operación.

**Ejemplo desarrollado.** Al visitar un sitio, el dispositivo resuelve un nombre mediante DNS, obtiene una dirección IP y envía paquetes a través de routers de distintas redes. La ruta puede cambiar sin que el usuario perciba cada salto.

**Práctica guiada.** Consulta la resolución DNS de un dominio público autorizado con `dig` o `nslookup`, y observa la ruta con `traceroute` o `tracert`. Registra que algunos saltos pueden no responder a ICMP.

**Actividad independiente.** Dibuja el recorrido conceptual de una solicitud web desde una red doméstica hasta un servidor alojado en otro sistema autónomo.

**Criterios de aceptación.** Explica interconexión de redes, resolución de nombres y encaminamiento; distingue Internet de la Web.

**Errores frecuentes.** Usar Internet y Web como sinónimos o interpretar un salto sin respuesta como prueba concluyente de caída.

**Comprobación.** ¿Por qué la Web es un servicio que utiliza Internet, pero no constituye toda la infraestructura de Internet?

**Laboratorio de profundización — Ruta conceptual hacia un servicio público.**

1. Dibuja equipo, LAN, router doméstico, proveedor, redes de tránsito y servidor destino. 2. Distingue DNS, direccionamiento IP y transporte. 3. Explica dónde puede aplicarse NAT. 4. Enumera qué datos de una conexión son visibles para cada tramo.

**Evidencia esperada.** El flujo distingue resolución de nombres, encaminamiento y transporte y evita describir Internet como una sola red centralizada.

**Seguridad y límites.** No realizar captura de tráfico de terceros ni compartir direcciones públicas sensibles.

**Registro sugerido.** Anota topología, direccionamiento de laboratorio, herramientas, resultados y límites de la observación. No marques la práctica como ejecutada sin evidencia real.

### 8.1.5 — Intranet

**Propósito y modelo.** Una intranet es un entorno de servicios y contenidos de uso interno de una organización. Puede usar tecnologías web estándar, DNS interno, autenticación corporativa y controles de acceso. Que sea interna no la hace automáticamente confiable: requiere segmentación, actualizaciones, identidad y monitoreo.

**Ejemplo desarrollado.** Un portal interno de recursos humanos puede ser accesible solo desde dispositivos administrados o mediante acceso remoto autenticado. El control debe aplicarse al servicio y a los datos, no únicamente a la ubicación de red.

**Práctica guiada.** Diseña el flujo de acceso a un portal interno: resolución de nombre, autenticación, autorización, conexión cifrada y registro. No intentes acceder a intranets ajenas.

**Actividad independiente.** Define controles mínimos para publicar una aplicación interna que maneja datos personales: segmentación, MFA, TLS, roles, logs y respaldo.

**Criterios de aceptación.** Diferencia intranet de Internet y extranet; identifica controles de identidad y red.

**Errores frecuentes.** Suponer que una dirección privada o un nombre interno garantiza que el usuario esté autorizado.

**Comprobación.** ¿Por qué una intranet también necesita controles de seguridad de aplicación e identidad?

**Laboratorio de profundización — Diseño de un servicio interno.**

1. Define un portal interno para una organización ficticia. 2. Identifica usuarios autorizados, DNS interno, autenticación y segmentos de red. 3. Explica cómo se accede desde sede y VPN. 4. Define controles de registro y disponibilidad.

**Evidencia esperada.** La propuesta delimita usuarios, servicios y rutas de acceso y diferencia intranet de Internet.

**Seguridad y límites.** No publicar datos personales o documentos internos en una intranet de laboratorio.

**Registro sugerido.** Anota topología, direccionamiento de laboratorio, herramientas, resultados y límites de la observación. No marques la práctica como ejecutada sin evidencia real.

### 8.1.6 — Extranet

**Propósito y modelo.** Una extranet habilita acceso controlado a determinados recursos internos para terceros, socios o clientes. La exposición debe limitarse a servicios concretos, con identidad verificable, autorización, segmentación, monitoreo y acuerdos de uso.

**Ejemplo desarrollado.** Un proveedor puede consultar órdenes de compra en un portal externo sin obtener acceso a la red administrativa completa. El portal debe mediar las operaciones y limitar los datos visibles a la relación comercial.

**Práctica guiada.** Dibuja una DMZ con portal de socios, firewall perimetral y servicios internos. Marca qué conexiones se permiten y cuáles se prohíben.

**Actividad independiente.** Diseña una extranet para intercambio de documentos con proveedores: autenticación, MFA, permisos por organización, expiración de cuentas y auditoría.

**Criterios de aceptación.** Explica diferencia entre extranet e intranet y delimita el acceso de terceros por servicio y función.

**Errores frecuentes.** Dar a un socio acceso VPN amplio cuando solo necesita una aplicación o mantener cuentas de terceros después de finalizar el contrato.

**Comprobación.** ¿Qué principio permite que un proveedor acceda a un portal sin tener acceso a toda la LAN corporativa?

**Laboratorio de profundización — Acceso controlado de terceros.**

1. Diseña acceso de un proveedor a un portal concreto. 2. Limita identidad, recursos, horarios y protocolos. 3. Define MFA, registros y caducidad. 4. Compara extranet con VPN de acceso completo.

**Evidencia esperada.** El diseño aplica mínimo privilegio y permite revocar el acceso de terceros sin afectar a usuarios internos.

**Seguridad y límites.** No conceder acceso lateral general ni reutilizar cuentas compartidas.

**Registro sugerido.** Anota topología, direccionamiento de laboratorio, herramientas, resultados y límites de la observación. No marques la práctica como ejecutada sin evidencia real.

### 8.1.7 — Cliente-servidor

**Propósito y modelo.** El modelo cliente-servidor separa consumidores de servicios y componentes que los proporcionan. Un cliente inicia solicitudes y un servidor escucha o procesa peticiones; ambos pueden ejecutarse en equipos físicos, VMs o procesos diferentes. La distinción es lógica y no implica necesariamente una máquina por rol.

**Ejemplo desarrollado.** Un navegador solicita una página a un servidor HTTP. El servidor recibe la conexión, aplica reglas de aplicación y devuelve una respuesta; puede delegar datos a un servidor de base de datos.

**Práctica guiada.** Representa navegador, servidor web y base de datos. Identifica protocolos, puertos y direcciones de origen/destino para cada intercambio.

**Actividad independiente.** Diseña una aplicación de tres capas y establece qué conexiones son necesarias entre cliente, frontend, backend y base de datos.

**Criterios de aceptación.** Identifica roles, flujo de solicitud/respuesta y dependencias entre servicios.

**Errores frecuentes.** Confundir cliente con usuario humano o exponer directamente una base de datos a Internet cuando un backend debe mediar el acceso.

**Comprobación.** ¿Qué ventaja de seguridad ofrece colocar una API entre el cliente y la base de datos?

**Laboratorio de profundización — Secuencia de solicitud y respuesta.**

1. Modela cliente, servidor, DNS y conexión TCP. 2. Dibuja solicitud, respuesta y cierre. 3. Identifica qué componente escucha y cuál inicia conexión. 4. Añade una falla de servidor y describe los síntomas del cliente.

**Evidencia esperada.** El diagrama distingue cliente y servidor por el rol en una interacción, no por el tipo de hardware.

**Seguridad y límites.** No exponer servicios de prueba en interfaces públicas sin autenticación ni firewall.

**Registro sugerido.** Anota topología, direccionamiento de laboratorio, herramientas, resultados y límites de la observación. No marques la práctica como ejecutada sin evidencia real.

### 8.1.8 — Peer-to-peer

**Propósito y modelo.** En una arquitectura peer-to-peer, los nodos pueden actuar como clientes y servidores según el intercambio. Puede distribuir carga y evitar un punto central único, pero complica descubrimiento, confianza, control de acceso, actualización y auditoría.

**Ejemplo desarrollado.** En una red P2P de distribución de archivos, cada nodo comparte fragmentos y descarga otros. La integridad debe comprobarse con hashes o firmas y el origen del contenido debe evaluarse por separado.

**Práctica guiada.** Dibuja una red de cuatro pares y marca quién ofrece y consume datos. Compara qué ocurre si un nodo deja de participar frente a una arquitectura centralizada.

**Actividad independiente.** Evalúa un diseño P2P para distribuir actualizaciones en una organización; incluye autenticidad del paquete, control de versiones, revocación y límites de ancho de banda.

**Criterios de aceptación.** Explica simetría de roles, ventajas y riesgos; distingue distribución descentralizada de confianza automática.

**Errores frecuentes.** Asumir que un archivo recibido de varios pares es auténtico o que descentralización elimina todos los puntos de falla.

**Comprobación.** ¿Por qué la verificación criptográfica sigue siendo necesaria en una red P2P?

**Laboratorio de profundización — Modelo P2P y confianza.**

1. Dibuja cinco nodos que consumen y ofrecen recursos. 2. Identifica descubrimiento, transferencia y verificación de integridad. 3. Compara centralización de índices y distribución total. 4. Describe riesgos de identidad y disponibilidad.

**Evidencia esperada.** La comparación explica roles simultáneos de pares y diferencia el modelo P2P de cliente-servidor.

**Seguridad y límites.** No compartir archivos protegidos ni utilizar redes P2P para distribuir material no autorizado.

**Registro sugerido.** Anota topología, direccionamiento de laboratorio, herramientas, resultados y límites de la observación. No marques la práctica como ejecutada sin evidencia real.

### 8.1.9 — Router

**Propósito y modelo.** Un router reenvía paquetes IP entre redes usando una tabla de rutas. Selecciona la ruta más específica aplicable y, en caso de empate, aplica métricas y políticas del sistema. Puede ejecutar funciones adicionales como NAT, firewall o VPN, pero estas no definen su función básica de capa 3.

**Ejemplo desarrollado.** Un equipo con una ruta conectada a su LAN y una ruta por defecto hacia el gateway envía destinos remotos al siguiente salto. Si existe una ruta más específica, puede preferirse sobre la ruta por defecto.

**Práctica guiada.** Consulta tabla de rutas con `ip route` o `route print`. Identifica red conectada, gateway por defecto e interfaz. No cambies rutas en el host.

**Actividad independiente.** Dibuja dos subredes conectadas por un router y describe el siguiente salto para tres destinos, incluyendo uno sin ruta específica.

**Criterios de aceptación.** Explica reenvío IP, ruta más específica y gateway por defecto.

**Errores frecuentes.** Confundir router con switch o pensar que el gateway siempre es la dirección más alta/baja de una subred.

**Comprobación.** ¿Por qué una ruta más específica suele prevalecer sobre la ruta por defecto?

**Laboratorio de profundización — Decisión de reenvío de paquetes.**

1. Construye una tabla de rutas ficticia con redes conectadas, ruta específica y ruta por defecto. 2. Determina el siguiente salto para tres destinos. 3. Explica qué sucede si no hay coincidencia. 4. Distingue plano de control y plano de reenvío.

**Evidencia esperada.** Las decisiones seleccionan la ruta más específica y reconocen gateway de siguiente salto.

**Seguridad y límites.** No cambiar rutas del host o router productivo durante la práctica.

**Registro sugerido.** Anota topología, direccionamiento de laboratorio, herramientas, resultados y límites de la observación. No marques la práctica como ejecutada sin evidencia real.

### 8.1.10 — Switch

**Propósito y modelo.** Un switch Ethernet aprende direcciones MAC de origen y mantiene una tabla de reenvío para decidir por qué puerto enviar tramas. En redes modernas puede soportar VLAN, enlaces troncales, STP, PoE y controles de capa 2. La tabla MAC no es una tabla de rutas IP.

**Ejemplo desarrollado.** Si el destino MAC es conocido, el switch reenvía la trama al puerto asociado; si es desconocido, puede inundarla dentro de la VLAN correspondiente, excluyendo el puerto de entrada.

**Práctica guiada.** Dibuja un switch con tres hosts y registra cómo aprende MAC al recibir tramas. Consulta la tabla MAC en un equipo de laboratorio administrado si tienes autorización.

**Actividad independiente.** Diseña VLAN separadas para usuarios, servidores y administración; identifica puertos de acceso y enlaces troncales.

**Criterios de aceptación.** Distingue conmutación MAC de enrutamiento IP y explica aprendizaje e inundación.

**Errores frecuentes.** Confundir la tabla MAC con ARP o conectar equipos no confiables a puertos de acceso corporativos sin control.

**Comprobación.** ¿Qué información utiliza un switch de capa 2 para seleccionar el puerto de salida?

**Laboratorio de profundización — Aprendizaje de direcciones MAC.**

1. Dibuja un switch con cuatro puertos. 2. Simula tramas entrantes con MAC origen y destino. 3. Actualiza una tabla CAM ficticia. 4. Explica flooding de unicast desconocido y broadcast.

**Evidencia esperada.** La tabla aprende MAC origen por puerto y explica cómo se reenvía una trama según destino.

**Seguridad y límites.** No conectar equipos de laboratorio a una red productiva para generar tráfico de prueba.

**Registro sugerido.** Anota topología, direccionamiento de laboratorio, herramientas, resultados y límites de la observación. No marques la práctica como ejecutada sin evidencia real.

### 8.1.11 — Firewall

**Propósito y modelo.** Un firewall aplica políticas sobre tráfico que atraviesa un punto de control. Puede filtrar por dirección, protocolo, puerto, estado de conexión, aplicación o identidad, según el producto. La política debe ser explícita, mínima y coherente con la arquitectura; reglas de entrada y salida tienen efectos distintos.

**Ejemplo desarrollado.** Una aplicación web pública puede aceptar TCP 443 desde Internet, pero solo permitir que el servidor web se comunique con la base de datos en un puerto interno concreto. El firewall no reemplaza autenticación ni validación de la aplicación.

**Práctica guiada.** Lee una tabla de reglas de laboratorio y clasifica origen, destino, protocolo, puerto, dirección y acción. No cambies el firewall de producción ni deshabilites protecciones para probar conectividad.

**Actividad independiente.** Construye una matriz de flujos para una aplicación de tres capas y convierte cada flujo necesario en una regla mínima.

**Criterios de aceptación.** Identifica cinco atributos de una regla y explica denegación por defecto y mínimo privilegio.

**Errores frecuentes.** Crear reglas Any/Any, olvidar tráfico de administración o considerar el firewall como sustituto de controles de aplicación.

**Comprobación.** ¿Qué riesgo introduce permitir cualquier origen hacia todos los puertos de un servidor?

**Laboratorio de profundización — Política de mínimo acceso.**

1. Define tres flujos requeridos entre cliente, servidor web y base de datos. 2. Redacta reglas por origen, destino, protocolo y puerto. 3. Añade una regla de denegación por defecto. 4. Explica cómo registrar bloqueos sin capturar datos sensibles.

**Evidencia esperada.** Las reglas permiten solo los flujos necesarios y describen orden, dirección y alcance.

**Seguridad y límites.** No desactivar firewalls ni crear reglas Any/Any para facilitar una demostración.

**Registro sugerido.** Anota topología, direccionamiento de laboratorio, herramientas, resultados y límites de la observación. No marques la práctica como ejecutada sin evidencia real.

### 8.1.12 — Gateway

**Propósito y modelo.** Gateway es un término contextual para un punto que conecta redes o traduce entre protocolos y dominios. En una LAN IP, el gateway por defecto suele ser la dirección del router al que se envía tráfico destinado a redes no locales. No todos los gateways son routers IP convencionales.

**Ejemplo desarrollado.** Un host consulta su máscara para decidir si el destino es local; si no lo es, entrega el paquete al siguiente salto configurado como gateway. Una dirección DNS no es automáticamente el gateway.

**Práctica guiada.** Consulta `ip route` o `ipconfig /all` e identifica gateway y DNS por separado. No cambies configuración de red del equipo.

**Actividad independiente.** Dado un host, máscara, destino y gateway, determina si el destino está en la subred local y si el tráfico requiere siguiente salto.

**Criterios de aceptación.** Diferencia gateway por defecto, router y servidor DNS; justifica el siguiente salto.

**Errores frecuentes.** Confundir puerta de enlace con DNS o configurar como gateway una dirección que no es alcanzable en el enlace local.

**Comprobación.** ¿Qué papel cumple el gateway cuando el destino no pertenece a la subred local?

**Laboratorio de profundización — Resolución de tráfico fuera de subred.**

1. Asigna una IP, máscara y gateway a un host ficticio. 2. Calcula si dos destinos son locales o remotos. 3. Describe cuándo se usa ARP para resolver la MAC del gateway. 4. Explica el papel del gateway por defecto.

**Evidencia esperada.** El estudiante determina correctamente cuándo el host entrega una trama al destino local o al router.

**Seguridad y límites.** No modificar el gateway real del equipo durante esta práctica.

**Registro sugerido.** Anota topología, direccionamiento de laboratorio, herramientas, resultados y límites de la observación. No marques la práctica como ejecutada sin evidencia real.

### 8.1.13 — Access Point

**Propósito y modelo.** Un punto de acceso conecta estaciones Wi-Fi con una red de distribución, habitualmente Ethernet. Publica uno o más SSID y aplica seguridad inalámbrica, aislamiento de clientes y segmentación. El SSID identifica una red anunciada, no constituye por sí solo una barrera de seguridad.

**Ejemplo desarrollado.** Una red de invitados puede utilizar un SSID distinto y mapearse a una VLAN aislada. Ocultar el SSID no sustituye WPA2/WPA3, autenticación robusta ni segmentación.

**Práctica guiada.** Inspecciona la configuración de un AP de laboratorio: SSID, banda, cifrado, canal, VLAN y aislamiento de clientes. No cambies parámetros de una red que no administras.

**Actividad independiente.** Diseña Wi-Fi corporativo, invitados e IoT con SSID/VLAN, autenticación, controles de acceso y política de actualización.

**Criterios de aceptación.** Distingue AP de router, SSID de autenticación y segmentación lógica de ocultación del nombre.

**Errores frecuentes.** Usar cifrado obsoleto, compartir la contraseña corporativa con invitados o asumir que ocultar SSID evita accesos no autorizados.

**Comprobación.** ¿Por qué una red Wi-Fi de invitados debe estar aislada de los sistemas internos aunque utilice un SSID diferente?

## 8.2 — Modelos de comunicación

**Laboratorio de profundización — Diseño de cobertura y seguridad Wi-Fi.**

1. Dibuja un punto de acceso y tres clientes. 2. Define SSID, banda, canal y ubicación. 3. Compara WPA2-AES y WPA3 según compatibilidad. 4. Separa red de invitados y red administrativa.

**Evidencia esperada.** El diseño contempla cobertura, interferencia, autenticación y segmentación de clientes.

**Seguridad y límites.** No utilizar redes abiertas para información sensible ni probar contraseñas contra redes ajenas.

**Registro sugerido.** Anota topología, direccionamiento de laboratorio, herramientas, resultados y límites de la observación. No marques la práctica como ejecutada sin evidencia real.

### 8.2.1 — Modelo OSI

**Propósito y modelo.** El modelo OSI es un marco conceptual de siete capas que ayuda a separar funciones de comunicación y localizar problemas. No es una pila de protocolos que todos los sistemas implementen literalmente. Cada capa ofrece servicios a la superior y utiliza servicios de la inferior.

**Ejemplo desarrollado.** Al abrir una página, la aplicación utiliza HTTP; las capas inferiores aportan transporte, direccionamiento y acceso al medio. Un problema puede estar en DNS, transporte, enrutamiento, enlace o aplicación, por lo que el modelo organiza el diagnóstico.

**Práctica guiada.** Clasifica DNS, TCP, IP, Ethernet y HTTP en la capa OSI más habitual, explicando cualquier simplificación o dependencia de implementación.

**Actividad independiente.** Construye una tabla con las siete capas, función, PDU orientativa, dirección/identificador asociado y un protocolo o tecnología representativa.

**Criterios de aceptación.** Describe el propósito del modelo y ubica tecnologías sin afirmar que el modelo determina exactamente todas las implementaciones.

**Errores frecuentes.** Tratar OSI como una implementación real obligatoria o memorizar capas sin relacionarlas con el flujo de datos.

**Comprobación.** ¿Cómo ayuda la separación por capas a aislar una falla de conectividad?

**Laboratorio de profundización — Mapeo de una comunicación a capas.**

1. Elige una consulta HTTPS. 2. Asocia aplicación, transporte, red, enlace y físico con funciones OSI. 3. Explica dónde actúan TLS, TCP, IP y Ethernet. 4. Señala que el modelo es una herramienta conceptual.

**Evidencia esperada.** El mapeo es consistente y reconoce que las correspondencias entre modelos no siempre son uno a uno.

**Seguridad y límites.** No afirmar que cada protocolo real pertenece exclusivamente a una única capa sin matices.

**Registro sugerido.** Anota topología, direccionamiento de laboratorio, herramientas, resultados y límites de la observación. No marques la práctica como ejecutada sin evidencia real.

### 8.2.2 — Las siete capas OSI

**Propósito y modelo.** Las capas OSI se organizan desde la capa 1 Física, 2 Enlace, 3 Red, 4 Transporte, 5 Sesión, 6 Presentación y 7 Aplicación. Las funciones pueden combinarse o distribuirse de manera distinta en protocolos reales; el modelo sirve para describir responsabilidades y diagnosticar.

**Ejemplo desarrollado.** Un enlace Ethernet caído pertenece al ámbito físico/enlace; una ruta IP ausente corresponde a red; un puerto TCP que no escucha pertenece a transporte/servicio; una respuesta HTTP 500 se observa en aplicación.

**Práctica guiada.** Clasifica cinco incidentes sintéticos por capa probable y anota qué evidencia recopilarías antes de confirmar la causa.

**Actividad independiente.** Prepara un mapa de capas con ejemplo de falla y herramienta de diagnóstico para cada una.

**Criterios de aceptación.** Nombra y ordena las siete capas y justifica la ubicación de al menos cinco incidentes.

**Errores frecuentes.** Asignar una falla a una sola capa sin considerar dependencias o confundir capa de aplicación con interfaz gráfica.

**Comprobación.** ¿Por qué un error visible en una aplicación puede originarse en una capa inferior?

**Laboratorio de profundización — Diagnóstico por capas.**

1. Recibe un escenario: equipo conectado al Wi-Fi sin acceso a una web. 2. Formula una prueba por capa desde enlace físico hasta aplicación. 3. Ordena pruebas para aislar el fallo. 4. Explica qué evidencia confirmaría o descartaría cada hipótesis.

**Evidencia esperada.** La secuencia avanza de conectividad local a aplicación y separa síntomas de causa raíz.

**Seguridad y límites.** No cambiar varias configuraciones simultáneamente ni utilizar datos de usuarios reales.

**Registro sugerido.** Anota topología, direccionamiento de laboratorio, herramientas, resultados y límites de la observación. No marques la práctica como ejecutada sin evidencia real.

### 8.2.3 — Modelo TCP/IP

**Propósito y modelo.** El modelo TCP/IP agrupa funciones en capas de acceso a red, Internet, transporte y aplicación (las denominaciones pueden variar entre fuentes). Es una descripción práctica de la arquitectura de Internet y no coincide uno a uno con OSI.

**Ejemplo desarrollado.** HTTP pertenece a aplicación, TCP a transporte, IP a Internet y Ethernet o Wi-Fi al acceso a red. DNS es aplicación aunque resuelva nombres que luego se usan en IP.

**Práctica guiada.** Mapea HTTP, DNS, TCP, UDP, IPv4, IPv6, Ethernet y Wi-Fi al modelo TCP/IP. Compara la agrupación con la tabla OSI.

**Actividad independiente.** Describe el flujo de una solicitud HTTPS utilizando las capas TCP/IP y señala dónde se producen resolución DNS, establecimiento TCP y negociación TLS.

**Criterios de aceptación.** Identifica las cuatro capas y explica al menos dos diferencias de agrupación respecto a OSI.

**Errores frecuentes.** Afirmar que OSI y TCP/IP tienen idéntico número de capas o colocar DNS en la capa de transporte.

**Comprobación.** ¿Por qué TCP/IP es una arquitectura de protocolos y OSI se utiliza principalmente como modelo de referencia?

**Laboratorio de profundización — Correspondencia TCP/IP y OSI.**

1. Clasifica DNS, TCP, IP y Ethernet en el modelo TCP/IP. 2. Relaciónalos con capas OSI. 3. Explica cómo se transporta una consulta DNS sobre UDP o TCP. 4. Documenta un caso que use TLS sobre TCP.

**Evidencia esperada.** El estudiante reconoce el modelo de cuatro capas y sus correspondencias aproximadas con OSI.

**Seguridad y límites.** Evitar memorizar equivalencias rígidas cuando la arquitectura real incluye protocolos transversales.

**Registro sugerido.** Anota topología, direccionamiento de laboratorio, herramientas, resultados y límites de la observación. No marques la práctica como ejecutada sin evidencia real.

### 8.2.4 — Encapsulamiento

**Propósito y modelo.** El encapsulamiento añade información de control al dato al descender por las capas: cabeceras y, en ciertos niveles, tráileres. Una aplicación genera datos; transporte añade información de puertos y control; IP incorpora direcciones; enlace agrega direcciones MAC y verificación de trama.

**Ejemplo desarrollado.** Un segmento TCP viaja dentro de un paquete IP que se transmite en una trama Ethernet. Cada router procesa la cabecera de enlace entrante y crea una nueva para el siguiente enlace, mientras la información IP normalmente conserva sus extremos salvo traducciones o túneles.

**Práctica guiada.** Dibuja los datos de una petición HTTP encapsulados en TCP, IP y Ethernet. Etiqueta puertos, direcciones IP y MAC, sin usar direcciones reales sensibles.

**Actividad independiente.** Explica qué campos cambian al cruzar un router y cuáles suelen mantenerse en una ruta sin NAT.

**Criterios de aceptación.** Describe orden de encapsulamiento y diferencia cabeceras de transporte, red y enlace.

**Errores frecuentes.** Afirmar que la dirección MAC de origen/destino permanece igual en todos los saltos o confundir puerto TCP con puerto físico.

**Comprobación.** ¿Por qué un router reemplaza la trama de enlace al reenviar un paquete por otra interfaz?

**Laboratorio de profundización — Seguimiento de cabeceras.**

1. Parte de datos de aplicación. 2. Añade conceptualmente cabecera de transporte, IP y Ethernet. 3. Identifica puertos, IP origen/destino y MAC del siguiente salto. 4. Explica qué cabecera cambia al atravesar un router.

**Evidencia esperada.** El esquema muestra el orden de encapsulamiento y diferencia direcciones de enlace, red y transporte.

**Seguridad y límites.** No capturar payloads reales que contengan credenciales o información personal.

**Registro sugerido.** Anota topología, direccionamiento de laboratorio, herramientas, resultados y límites de la observación. No marques la práctica como ejecutada sin evidencia real.

### 8.2.5 — Desencapsulamiento

**Propósito y modelo.** El desencapsulamiento es el proceso inverso en el receptor: cada capa interpreta y retira la información de control correspondiente y entrega la carga a la capa superior. La validación puede incluir integridad de trama, destino IP, puerto, estado de transporte y formato de aplicación.

**Ejemplo desarrollado.** La NIC recibe una trama, la capa de red procesa el paquete IP y TCP entrega el flujo al socket asociado al puerto. Finalmente la aplicación interpreta los datos según el protocolo utilizado.

**Práctica guiada.** Utiliza un diagrama de una trama Ethernet que contiene IPv4, TCP y datos HTTP. Identifica qué componente consume cada cabecera al recibirla.

**Actividad independiente.** Describe qué ocurre si la trama llega correctamente pero el puerto de destino no tiene un proceso escuchando.

**Criterios de aceptación.** Explica el orden de procesamiento y distingue recepción de enlace, entrega IP y demultiplexación de transporte.

**Errores frecuentes.** Suponer que recibir una trama garantiza que la aplicación recibirá datos o que cada capa valida la misma información.

**Comprobación.** ¿Qué sucede si el paquete IP llega al host, pero no existe un socket asociado al puerto TCP de destino?

**Laboratorio de profundización — Lectura de una trama hasta la aplicación.**

1. Recibe una trama ficticia con Ethernet, IP, TCP y datos de aplicación. 2. Identifica qué campos permiten entregar cada PDU a la capa superior. 3. Describe comprobaciones de longitud y protocolo. 4. Compara con el proceso inverso de encapsulamiento.

**Evidencia esperada.** El estudiante explica la extracción ordenada de cabeceras y la demultiplexación por protocolo/puerto.

**Seguridad y límites.** No asumir que todos los paquetes llegan sin fragmentación, pérdida, retransmisión o cifrado.

**Registro sugerido.** Anota topología, direccionamiento de laboratorio, herramientas, resultados y límites de la observación. No marques la práctica como ejecutada sin evidencia real.

### 8.2.6 — Paquetes

**Propósito y modelo.** En redes IP, paquete suele referirse a la unidad de datos de la capa de red (datagrama IP). Contiene cabecera con direcciones y campos de control, además de una carga que puede transportar un segmento TCP, datagrama UDP u otro protocolo. El tamaño y fragmentación dependen de MTU y versión IP.

**Ejemplo desarrollado.** Un paquete IP puede atravesar varios routers y cambiar su encapsulamiento de enlace en cada salto. La dirección IP de destino orienta el encaminamiento, mientras la MAC identifica el siguiente salto en la red local.

**Práctica guiada.** Examina una captura de laboratorio en Wireshark y localiza un paquete IPv4 o IPv6. Identifica origen, destino, protocolo superior y longitud.

**Actividad independiente.** Explica cómo un router decide el siguiente salto sin necesitar conocer el puerto TCP de la aplicación.

**Criterios de aceptación.** Diferencia paquete IP de trama Ethernet y segmento TCP; identifica campos esenciales.

**Errores frecuentes.** Usar paquete, trama y segmento como sinónimos o asumir que las direcciones MAC identifican extremos de Internet.

**Comprobación.** ¿Qué dirección utiliza el router para tomar una decisión de encaminamiento IP?

**Laboratorio de profundización — Diferencia entre PDU y paquete IP.**

1. Analiza un ejemplo con cabecera IPv4, protocolo, TTL, origen y destino. 2. Distingue paquete IP de segmento TCP y trama Ethernet. 3. Explica qué campos cambian en un router. 4. Relaciona TTL con prevención de bucles.

**Evidencia esperada.** Se usan correctamente los términos paquete, segmento y trama en cada capa.

**Seguridad y límites.** No inferir contenido de aplicación a partir de metadatos de red cifrada.

**Registro sugerido.** Anota topología, direccionamiento de laboratorio, herramientas, resultados y límites de la observación. No marques la práctica como ejecutada sin evidencia real.

### 8.2.7 — Tramas

**Propósito y modelo.** Una trama es una unidad de datos de enlace que transporta un paquete o carga superior sobre un medio local. En Ethernet incluye direcciones MAC, tipo/longitud, datos y secuencia de verificación FCS. La trama se interpreta dentro del dominio de enlace y puede cambiar en cada salto enrutado.

**Ejemplo desarrollado.** Un host envía una trama Ethernet a la MAC del gateway cuando el destino IP está fuera de su subred. El router recibe la trama, procesa el paquete IP y genera otra trama para la interfaz de salida.

**Práctica guiada.** En una captura de Wireshark filtra tráfico Ethernet y localiza MAC de origen/destino y tipo EtherType. Relaciona la carga con el paquete IP transportado.

**Actividad independiente.** Dibuja dos tramas distintas para el mismo paquete IP antes y después de cruzar un router, indicando qué campos cambian.

**Criterios de aceptación.** Diferencia trama de paquete y explica el alcance local de las direcciones MAC.

**Errores frecuentes.** Suponer que la MAC del equipo remoto aparece directamente en todas las tramas del camino.

**Comprobación.** ¿Por qué la MAC destino de una trama puede ser la del router y no la del servidor remoto?

**Laboratorio de profundización — Análisis de trama Ethernet.**

1. Dibuja destino MAC, origen MAC, EtherType y carga útil. 2. Explica FCS y su función de detección de errores. 3. Distingue una trama unicast, multicast y broadcast. 4. Identifica qué direcciones se reemplazan al pasar por un router.

**Evidencia esperada.** El diagrama identifica campos y diferencia dirección MAC de dirección IP.

**Seguridad y límites.** Usar tramas sintéticas o capturas de laboratorio autorizadas.

**Registro sugerido.** Anota topología, direccionamiento de laboratorio, herramientas, resultados y límites de la observación. No marques la práctica como ejecutada sin evidencia real.

### 8.2.8 — Segmentos

**Propósito y modelo.** En TCP, un segmento contiene cabecera TCP y datos de aplicación. Incluye puertos, números de secuencia y acuse, flags, ventana y checksum. En UDP la unidad se denomina datagrama, aunque algunos materiales usan términos genéricos. La segmentación permite transportar flujos y controlar entrega ordenada.

**Ejemplo desarrollado.** Un flujo TCP puede dividir datos en varios segmentos; el receptor utiliza números de secuencia para reordenar y detectar pérdidas. Un segmento no equivale a un mensaje completo de aplicación.

**Práctica guiada.** Examina una captura TCP de laboratorio y localiza puertos, flags SYN/ACK, números de secuencia y longitud. No captures tráfico de terceros sin autorización.

**Actividad independiente.** Explica el establecimiento TCP de tres vías y representa cómo un segmento perdido puede provocar retransmisión.

**Criterios de aceptación.** Identifica campos TCP y diferencia segmento, paquete y trama.

**Errores frecuentes.** Suponer que cada segmento corresponde a una sola llamada de escritura de la aplicación o que TCP conserva límites de mensajes.

**Comprobación.** ¿Por qué TCP es un flujo de bytes y no un protocolo que preserve automáticamente los límites de mensajes?

**Laboratorio de profundización — Análisis de segmento TCP.**

1. Identifica puertos origen/destino, números de secuencia y confirmación, flags y ventana. 2. Describe SYN, SYN-ACK y ACK. 3. Explica cómo se reensambla el flujo y qué hace una retransmisión.

**Evidencia esperada.** El estudiante interpreta los campos principales y diferencia segmento TCP de datagrama UDP.

**Seguridad y límites.** No interpretar una captura parcial como prueba suficiente de un fallo o ataque.

**Registro sugerido.** Anota topología, direccionamiento de laboratorio, herramientas, resultados y límites de la observación. No marques la práctica como ejecutada sin evidencia real.

### 8.2.9 — MTU

**Propósito y modelo.** La MTU define el tamaño máximo de unidad de datos que puede transportar una interfaz o enlace sin fragmentación a ese nivel. En Ethernet común se utiliza frecuentemente MTU IP de 1500 bytes, pero existen otros valores. Túneles, VPN y encapsulamientos reducen el espacio disponible para la carga.

**Ejemplo desarrollado.** Si un paquete excede la MTU de un enlace, IPv4 puede fragmentarse según DF y comportamiento de la ruta; IPv6 no fragmenta routers intermedios y depende de Path MTU Discovery y del origen. Una MTU incoherente puede causar fallos selectivos.

**Práctica guiada.** Consulta MTU de interfaces con `ip link` o `netsh interface ipv4 show subinterfaces`. No cambies valores en una red productiva. Compara el MTU configurado con el tamaño de ping permitido por tu sistema.

**Actividad independiente.** Analiza una VPN con sobrecarga de encapsulamiento y explica por qué una página pequeña carga pero una transferencia grande se bloquea.

**Criterios de aceptación.** Define MTU, diferencia fragmentación IPv4/IPv6 y relaciona túneles con sobrecarga.

**Errores frecuentes.** Confundir MTU con ancho de banda o reducirla arbitrariamente sin medir la ruta.

**Comprobación.** ¿Cómo puede una MTU incorrecta provocar fallos que parecen intermitentes en aplicaciones?

## 8.3 — Direccionamiento


**Laboratorio de profundización — Diagnóstico de MTU y fragmentación.**

1. Registra la MTU de una interfaz de laboratorio. 2. Explica el efecto de una MTU menor en el camino. 3. Diseña pruebas controladas con paquetes de tamaño variable y DF cuando la plataforma lo permita. 4. Relaciona ICMP necesario con Path MTU Discovery.

**Evidencia esperada.** El diagnóstico explica fragmentación IPv4, comportamiento IPv6 y fallos de PMTUD con evidencia controlada.

**Seguridad y límites.** No saturar enlaces ni modificar MTU de interfaces productivas.

**Registro sugerido.** Anota topología, direccionamiento de laboratorio, herramientas, resultados y límites de la observación. No marques la práctica como ejecutada sin evidencia real.
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

**Propósito y modelo.** TCP ofrece un flujo de bytes orientado a conexión con entrega ordenada, detección de pérdida, retransmisión y control de flujo/congestión. Utiliza puertos para multiplexar aplicaciones, números de secuencia y ACK. No conserva límites de mensajes de la aplicación.

**Ejemplo desarrollado.** El establecimiento habitual usa SYN, SYN-ACK y ACK. Al perderse un segmento, TCP puede retransmitirlo; una aplicación puede recibir los bytes en lecturas de tamaños distintos a los de escritura del emisor.

**Práctica guiada.** Analiza una captura TCP de laboratorio y localiza handshake, puertos, flags y retransmisiones si las hay. Usa únicamente tráfico propio o autorizado.

**Actividad independiente.** Dibuja el handshake y explica qué evidencia buscarías ante conexión rechazada, timeout y conexión establecida sin respuesta de aplicación.

**Criterios de aceptación.** Explica conexión, secuencia, ACK y diferencia flujo TCP de datagramas UDP.

**Errores frecuentes.** Decir que TCP garantiza que la aplicación procese la información o que un puerto abierto garantiza que el servicio sea seguro.

**Comprobación.** ¿Qué problema resuelve el número de secuencia en un flujo TCP?

### 8.4.2 — UDP

**Propósito y modelo.** UDP transporta datagramas sin establecer una conexión de transporte ni garantizar entrega, orden o retransmisión. Tiene baja sobrecarga y conserva límites de datagrama. Las aplicaciones pueden implementar sus propios mecanismos de confiabilidad y control.

**Ejemplo desarrollado.** DNS suele utilizar UDP para consultas comunes, aunque puede usar TCP en determinados escenarios. Una respuesta perdida puede provocar reintento en la aplicación; UDP por sí mismo no lo realiza.

**Práctica guiada.** Captura una consulta DNS propia y observa puertos UDP origen/destino y longitud del datagrama. No captures consultas de otros usuarios.

**Actividad independiente.** Compara UDP y TCP para voz en tiempo real, transferencia de archivos y consulta DNS; justifica latencia, confiabilidad y manejo de pérdida.

**Criterios de aceptación.** Distingue datagrama UDP de segmento TCP y explica que la confiabilidad puede residir en la aplicación.

**Errores frecuentes.** Afirmar que UDP siempre es más rápido o inseguro; el resultado depende del servicio y de los controles de aplicación.

**Comprobación.** ¿Por qué una aplicación de voz puede preferir UDP aun cuando algunos paquetes se pierdan?

### 8.4.3 — ICMP

**Propósito y modelo.** ICMP comunica errores y condiciones de operación de IP. Incluye mensajes como Echo Request/Reply, Destination Unreachable y Time Exceeded. No es un protocolo de transporte de aplicaciones y puede ser filtrado por políticas sin que todo el tráfico IP esté caído.

**Ejemplo desarrollado.** ping utiliza ICMP Echo para comprobar respuesta, pero un host puede bloquear Echo y seguir ofreciendo HTTPS. traceroute aprovecha respuestas ICMP o mecanismos equivalentes para inferir saltos.

**Práctica guiada.** Ejecuta ping hacia un host de laboratorio y compara resultado con una conexión TCP al servicio autorizado. Registra que una prueba no sustituye a la otra.

**Actividad independiente.** Analiza tres escenarios: Echo bloqueado, puerto TCP cerrado y ruta sin respuesta. Determina qué puede concluirse y qué no.

**Criterios de aceptación.** Identifica función de ICMP y límites de ping como prueba de disponibilidad.

**Errores frecuentes.** Concluir que un host está apagado porque no responde a Echo o bloquear todo ICMP sin analizar dependencias de diagnóstico y Path MTU.

**Comprobación.** ¿Por qué un ping fallido no demuestra necesariamente que un servidor web esté fuera de servicio?

### 8.4.4 — DNS

**Propósito y modelo.** DNS traduce nombres de dominio a registros como A, AAAA, CNAME, MX y TXT. La resolución suele involucrar stub resolver, recursor y servidores autoritativos; cachés y TTL afectan cuándo se observa un cambio. DNS no valida por sí solo la identidad del servicio ni cifra necesariamente la consulta.

**Ejemplo desarrollado.** Un registro A devuelve IPv4 y AAAA devuelve IPv6; un CNAME apunta a otro nombre. Un TTL determina cuánto tiempo puede conservarse una respuesta en caché, sujeto al comportamiento del resolver.

**Práctica guiada.** Consulta registros de un dominio público con `dig A`, `dig AAAA` y `dig MX` o `nslookup`. Registra servidor consultado y TTL; no realices transferencias de zona ni enumeración no autorizada.

**Actividad independiente.** Diseña la zona DNS de un dominio ficticio con web, correo y subdominio de API. Explica registros y riesgos de configuraciones incorrectas.

**Criterios de aceptación.** Diferencia recursor y autoritativo; interpreta A, AAAA, CNAME, MX y TTL.

**Errores frecuentes.** Confundir DNS con registro de dominios, asumir que el cambio se propaga instantáneamente o considerar TXT como un tipo único de autenticación.

**Comprobación.** ¿Por qué un cambio DNS puede tardar en reflejarse en todos los clientes?

### 8.4.5 — HTTP

**Propósito y modelo.** HTTP es un protocolo de aplicación basado en mensajes de solicitud y respuesta. Métodos, rutas, cabeceras, códigos de estado y cuerpo definen interacción. HTTP no cifra el contenido por sí mismo; HTTPS combina HTTP con TLS para proteger el canal.

**Ejemplo desarrollado.** GET solicita una representación; POST suele enviar datos para procesamiento; 404 indica recurso no encontrado y 500 error interno del servidor. El significado preciso depende de semántica y contrato de la API.

**Práctica guiada.** Usa `curl -i https://example.com/` o un endpoint de laboratorio para observar línea de estado y cabeceras. No envíes datos sensibles a servicios externos.

**Actividad independiente.** Diseña una API mínima con GET y POST; define códigos 200, 201, 400, 401, 404 y 500 para escenarios específicos.

**Criterios de aceptación.** Identifica método, ruta, estado, cabeceras y cuerpo; distingue HTTP de transporte TCP/QUIC.

**Errores frecuentes.** Usar GET para operaciones destructivas o interpretar todo código 2xx como idéntico.

**Comprobación.** ¿Qué diferencia conceptual existe entre un código 401 y uno 403?

### 8.4.6 — HTTPS

**Propósito y modelo.** HTTPS es HTTP protegido mediante TLS. TLS negocia parámetros criptográficos, autentica el servidor mediante certificados y protege confidencialidad e integridad del canal. La seguridad depende de validación de certificados, versiones y suites, gestión de claves y configuración del servidor.

**Ejemplo desarrollado.** Un certificado válido para un nombre no es suficiente si el cliente no verifica cadena de confianza, vigencia y coincidencia del hostname. Un candado en la interfaz no garantiza que la aplicación no tenga fallas lógicas.

**Práctica guiada.** Consulta el certificado de un sitio público mediante el navegador o `openssl s_client -connect host:443 -servername host` en un contexto autorizado. No desactives la validación TLS para resolver errores.

**Actividad independiente.** Explica handshake TLS a alto nivel y lista controles para renovar certificados y proteger claves privadas.

**Criterios de aceptación.** Diferencia cifrado de autenticación, explica certificado y hostname y reconoce límites de HTTPS.

**Errores frecuentes.** Ignorar advertencias de certificado, almacenar claves privadas junto al código o considerar HTTPS sustituto de autorización.

**Comprobación.** ¿Qué propiedad se pierde si un cliente acepta cualquier certificado sin validar identidad?

### 8.4.7 — SSH

**Propósito y modelo.** SSH proporciona acceso remoto cifrado y canales para ejecución de comandos, transferencia y túneles. La autenticación puede usar claves públicas, certificados o contraseña; la verificación de host protege frente a servidores suplantados. La seguridad requiere limitar usuarios, algoritmos, forwarding y exposición.

**Ejemplo desarrollado.** En una conexión SSH el cliente verifica la clave de host y luego autentica al usuario. Una clave privada protegida por passphrase reduce riesgo de uso no autorizado si el archivo se copia.

**Práctica guiada.** En una VM propia consulta `ssh -V`, inspecciona `~/.ssh/known_hosts` sin publicar contenido y revisa huella del servidor de laboratorio por canal confiable.

**Actividad independiente.** Diseña acceso administrativo SSH con claves, usuarios nominativos, MFA si está disponible, restricciones de origen y registro.

**Criterios de aceptación.** Distingue clave de host y clave de usuario; explica confidencialidad y verificación de identidad.

**Errores frecuentes.** Desactivar StrictHostKeyChecking sin control o compartir una misma clave privada entre todo el equipo.

**Comprobación.** ¿Qué riesgo evita verificar la clave de host antes de introducir credenciales?

### 8.4.8 — FTP

**Propósito y modelo.** FTP transfiere archivos mediante canales de control y datos separados. En su forma clásica, credenciales y datos no están cifrados; modos activo y pasivo difieren en cómo se establece el canal de datos. Debe evitarse en redes no confiables salvo que esté encapsulado y protegido apropiadamente.

**Ejemplo desarrollado.** En modo activo el servidor inicia la conexión de datos hacia el cliente; en pasivo el cliente inicia ambas conexiones, lo que suele facilitar atravesar NAT/firewalls. Esto no cifra la sesión.

**Práctica guiada.** Analiza un diagrama de sesión FTP y marca canal de control y canal de datos. No envíes credenciales reales ni pruebes servidores ajenos.

**Actividad independiente.** Propón una migración de FTP clásico a SFTP o FTPS, considerando compatibilidad, certificados/claves y automatizaciones existentes.

**Criterios de aceptación.** Diferencia FTP, FTPS y SFTP y explica canales activo/pasivo.

**Errores frecuentes.** Llamar SFTP a FTP pasivo o asumir que FTPS y SFTP utilizan el mismo protocolo.

**Comprobación.** ¿Por qué FTP clásico expone credenciales en una red sin cifrado?

### 8.4.9 — SFTP

**Propósito y modelo.** SFTP es un protocolo de transferencia de archivos que opera sobre SSH. No es FTP con cifrado TLS. Reutiliza autenticación y canal SSH, normalmente con el subsistema SFTP del servidor. Los permisos del sistema de archivos y la configuración de chroot o directorios restringidos determinan el alcance del usuario.

**Ejemplo desarrollado.** Un usuario puede autenticarse por SSH y tener acceso SFTP limitado a una carpeta; la política puede impedir shell interactiva aunque permita transferencia.

**Práctica guiada.** En un laboratorio autorizado consulta `sftp usuario@host-lab` y ejecuta comandos de navegación no destructivos como pwd y ls. No transfieras información real ni uses hosts de terceros.

**Actividad independiente.** Diseña una cuenta de intercambio que solo pueda cargar y descargar archivos en un directorio asignado.

**Criterios de aceptación.** Explica que SFTP funciona sobre SSH y diferencia el modelo de FTPS.

**Errores frecuentes.** Usar el puerto o la configuración de FTP clásico como si SFTP fuera el mismo servicio.

**Comprobación.** ¿Qué capa de seguridad aporta SSH al canal SFTP?

### 8.4.10 — SMTP

**Propósito y modelo.** SMTP transporta y retransmite correo entre clientes y servidores o entre servidores. El envío suele usar puertos 25 para transferencia entre servidores y  submission autenticado en 587 o 465 según configuración y práctica actual. TLS, autenticación, SPF, DKIM y DMARC cumplen funciones distintas.

**Ejemplo desarrollado.** SMTP acepta un mensaje y lo retransmite; IMAP/POP3 permiten al destinatario acceder al buzón. SPF evalúa servidores autorizados para un dominio, DKIM verifica una firma y DMARC publica política y alineación.

**Práctica guiada.** Inspecciona cabeceras de un correo de prueba recibido y reconoce Received, From, Message-ID y resultados de autenticación si aparecen. Oculta direcciones y datos privados.

**Actividad independiente.** Dibuja flujo de envío desde cliente hasta servidor destinatario e identifica dónde se aplica autenticación y cifrado.

**Criterios de aceptación.** Diferencia SMTP de protocolos de acceso al buzón y explica propósito general de SPF, DKIM y DMARC.

**Errores frecuentes.** Confundir el campo From visible con identidad autenticada o considerar SPF como firma criptográfica del contenido.

**Comprobación.** ¿Por qué SMTP y IMAP cumplen funciones diferentes en el correo electrónico?

### 8.4.11 — IMAP

**Propósito y modelo.** IMAP permite consultar y administrar mensajes almacenados en un servidor, sincronizando carpetas, banderas y estado entre clientes. TLS protege el canal y la autenticación identifica al usuario; permisos y políticas del servidor limitan el buzón accesible.

**Ejemplo desarrollado.** Al marcar un mensaje como leído en un cliente IMAP, el estado puede sincronizarse con otros dispositivos. Esto difiere de descargar y retirar mensajes del servidor como en configuraciones POP tradicionales.

**Práctica guiada.** Dibuja sincronización de una cuenta de prueba entre dos clientes. Identifica qué estado permanece en el servidor y qué controles protegen la sesión.

**Actividad independiente.** Compara IMAP y POP3 para una persona que usa varios dispositivos y justifica la elección según sincronización y retención.

**Criterios de aceptación.** Explica sincronización y distingue acceso al buzón de transporte SMTP.

**Errores frecuentes.** Confundir IMAP con el protocolo de envío o almacenar contraseñas en clientes sin protección.

**Comprobación.** ¿Qué ventaja ofrece mantener el estado del buzón en el servidor cuando se utilizan varios dispositivos?

### 8.4.12 — POP3

**Propósito y modelo.** POP3 permite recuperar mensajes desde un servidor de correo. Según configuración, el cliente puede descargar y borrar mensajes o conservar copias. POP3 es más simple que IMAP y no proporciona el mismo modelo de sincronización de carpetas y estado.

**Ejemplo desarrollado.** Un cliente POP puede descargar correo en un equipo y, si se configura para eliminarlo del servidor, los demás dispositivos no lo encontrarán. TLS protege el transporte, pero no define por sí solo la política de retención.

**Práctica guiada.** Compara en un esquema las operaciones de recuperación POP3 con sincronización IMAP. No configures clientes con credenciales reales para el ejercicio.

**Actividad independiente.** Recomienda POP3 o IMAP para tres escenarios y explica las consecuencias de borrar o conservar mensajes en servidor.

**Criterios de aceptación.** Describe recuperación y retención y diferencia POP3 de IMAP y SMTP.

**Errores frecuentes.** Asumir que POP3 sincroniza carpetas o que TLS hace segura cualquier política de almacenamiento.

**Comprobación.** ¿Qué problema puede causar una configuración POP3 que elimina del servidor los mensajes descargados?

### 8.4.13 — SMB

**Propósito y modelo.** SMB permite compartir archivos, impresoras y otros recursos en redes, especialmente en entornos Windows. La seguridad depende de autenticación, firma y cifrado cuando corresponde, ACL del sistema de archivos y permisos de recurso compartido. SMBv1 es obsoleto y debe evitarse salvo necesidad excepcional controlada.

**Ejemplo desarrollado.** Un usuario puede tener permiso NTFS de lectura y permiso de recurso compartido de solo lectura; el acceso remoto queda limitado por ambos. SMB moderno puede cifrar el transporte según versión y configuración.

**Práctica guiada.** En un laboratorio consulta recursos compartidos con `Get-SmbShare` o herramientas del sistema y revisa la versión/protocolo permitido. No enumeres shares de redes ajenas.

**Actividad independiente.** Diseña un recurso compartido por departamento con permisos de grupo, acceso mínimo, auditoría y política de SMB seguro.

**Criterios de aceptación.** Diferencia permisos SMB y NTFS y explica por qué SMBv1 no debe habilitarse sin justificación excepcional.

**Errores frecuentes.** Compartir con Everyone Control total, confundir share con carpeta local o habilitar SMBv1 por compatibilidad sin evaluar riesgo.

**Comprobación.** ¿Cómo se determina el acceso remoto efectivo cuando coexisten permisos SMB y NTFS?

### 8.4.14 — LDAP

**Propósito y modelo.** LDAP es un protocolo para consultar y modificar servicios de directorio organizados en entradas y atributos. Los nombres distinguidos (DN), unidades organizativas, filtros y esquemas describen objetos. LDAP no es sinónimo de Active Directory, aunque AD DS ofrece una implementación compatible con LDAP y extensiones propias.

**Ejemplo desarrollado.** Una búsqueda puede localizar usuarios dentro de una OU mediante un filtro; el alcance depende de base DN, permisos y alcance de búsqueda. En producción se debe proteger el canal mediante TLS o mecanismos seguros equivalentes.

**Práctica guiada.** Interpreta un DN sintético y construye un filtro conceptual para usuarios activos. No consultes directorios corporativos sin autorización.

**Actividad independiente.** Diseña una estructura de directorio para usuarios, grupos y equipos con delegación por unidad organizativa.

**Criterios de aceptación.** Identifica DN, atributos, filtros y diferencia protocolo LDAP de producto de directorio.

**Errores frecuentes.** Exponer consultas anónimas, enviar credenciales por LDAP sin protección o usar filtros construidos con entrada sin escapar.

**Comprobación.** ¿Qué papel cumple el DN al delimitar una búsqueda LDAP?

### 8.4.15 — Kerberos

**Propósito y modelo.** Kerberos es un protocolo de autenticación basado en tickets y un tercero de confianza (KDC). En Active Directory, el KDC forma parte del controlador de dominio. El cliente obtiene un Ticket-Granting Ticket y solicita tickets de servicio, reduciendo la necesidad de enviar la contraseña a cada servicio.

**Ejemplo desarrollado.** La autenticación requiere sincronización horaria razonable, resolución DNS y disponibilidad del KDC. Un desfase de reloj puede provocar errores aunque la contraseña sea correcta.

**Práctica guiada.** Dibuja AS-REQ/AS-REP, TGS-REQ/TGS-REP y acceso al servicio a nivel conceptual. En un dominio de laboratorio consulta tickets con `klist`; no intentes extraer credenciales.

**Actividad independiente.** Analiza un caso sintético de fallo Kerberos por hora, DNS o SPN y ordena las comprobaciones seguras.

**Criterios de aceptación.** Explica KDC, TGT y ticket de servicio y reconoce dependencias de tiempo/DNS.

**Errores frecuentes.** Confundir Kerberos con LDAP o asumir que obtener un ticket significa que la autorización a un recurso está concedida.

**Comprobación.** ¿Qué diferencia existe entre autenticación Kerberos y autorización de acceso a un archivo?

### 8.4.16 — WebSockets

**Propósito y modelo.** WebSocket establece un canal bidireccional persistente entre cliente y servidor, normalmente iniciado mediante un handshake HTTP que cambia el protocolo. Permite mensajes en ambos sentidos sin abrir una nueva solicitud HTTP por cada actualización. La seguridad requiere WSS, autenticación, autorización por mensaje, validación de origen y límites de recursos.

**Ejemplo desarrollado.** Un panel de monitoreo puede recibir actualizaciones de estado mediante WebSocket. La conexión autenticada al inicio no garantiza que cada operación posterior esté autorizada para todos los objetos.

**Práctica guiada.** Inspecciona un handshake WebSocket de una aplicación propia o un ejemplo local y distingue HTTP Upgrade, conexión establecida y frames. No captures sesiones ajenas.

**Actividad independiente.** Diseña un canal WebSocket para notificaciones y define autenticación, control de origen, autorización por evento, límites y cierre de sesión.

**Criterios de aceptación.** Explica handshake, bidireccionalidad y diferencia HTTP request/response de WebSocket.

**Errores frecuentes.** Validar permisos solo al abrir la conexión, aceptar cualquier Origin o no limitar tamaño/frecuencia de mensajes.

**Comprobación.** ¿Por qué la autorización debe verificarse también para las acciones enviadas por un canal WebSocket?

## 8.5 — Routing y Switching

### 8.5.1 — Switching

**Propósito y modelo.** Switching reenvía tramas dentro de una red de capa 2 usando información de direcciones MAC y VLAN. El switch aprende MAC de origen por puerto, filtra tráfico conocido e inunda destinos desconocidos dentro de la VLAN. STP y variantes previenen bucles de capa 2 en topologías redundantes.

**Ejemplo desarrollado.** Si una MAC se mueve de puerto, la tabla CAM puede actualizarse al recibir tramas de origen desde la nueva ubicación. Una tormenta de broadcast puede saturar el segmento si existe un bucle o una mala configuración.

**Práctica guiada.** Dibuja cuatro switches con enlaces redundantes y explica por qué se necesita un mecanismo de prevención de bucles. Consulta tabla MAC en un switch de laboratorio administrado.

**Actividad independiente.** Diseña dos VLAN con switches de acceso y distribución; especifica puertos de acceso, enlaces troncales y controles contra bucles.

**Criterios de aceptación.** Explica aprendizaje MAC, dominios de broadcast, VLAN y propósito de STP.

**Errores frecuentes.** Conectar enlaces redundantes sin control de bucles o creer que una VLAN equivale a una subred IP en todos los diseños.

**Comprobación.** ¿Qué puede ocurrir en una red Ethernet conmutada si se forma un bucle de capa 2?

### 8.5.2 — Routing

**Propósito y modelo.** Routing selecciona el siguiente salto para un paquete IP a partir de una tabla de rutas. Las rutas pueden ser conectadas, estáticas o aprendidas dinámicamente. La selección suele considerar el prefijo más largo y después métricas/administrative distance según plataforma.

**Ejemplo desarrollado.** Una ruta /24 prevalece sobre una ruta por defecto /0 para un destino dentro de ese bloque. Si dos rutas tienen el mismo prefijo, la métrica y política determinan cuál se utiliza.

**Práctica guiada.** Lee una tabla de rutas de ejemplo y selecciona la ruta para tres destinos. Consulta `ip route` en tu equipo sin modificarla.

**Actividad independiente.** Diseña rutas entre tres subredes conectadas por dos routers y documenta rutas de ida y retorno.

**Criterios de aceptación.** Aplica longest-prefix match y diferencia ruta estática de ruta aprendida.

**Errores frecuentes.** Suponer que una ruta de ida garantiza ruta de retorno o elegir por menor número de saltos sin considerar métricas.

**Comprobación.** ¿Por qué una ruta de retorno ausente puede romper una conexión aunque la ida funcione?

### 8.5.3 — Tablas de rutas

**Propósito y modelo.** La tabla de rutas relaciona prefijos destino con siguiente salto, interfaz, métrica y origen de ruta. Los hosts también tienen tablas de rutas; no son exclusivas de routers dedicados. Las rutas conectadas y la ruta por defecto suelen estar presentes en una configuración básica.

**Ejemplo desarrollado.** Una entrada 0.0.0.0/0 indica ruta por defecto IPv4; ::/0 cumple función equivalente en IPv6. Una ruta más específica tiene precedencia para destinos que coinciden.

**Práctica guiada.** Ejecuta `ip route`, `ip -6 route` o `route print`. Identifica prefijo, gateway, interfaz y métrica. No ejecutes comandos de modificación.

**Actividad independiente.** Dada una tabla de rutas sintética, determina qué ruta se usa para cinco direcciones destino y explica el criterio.

**Criterios de aceptación.** Interpreta ruta conectada, estática y por defecto y calcula coincidencia de prefijos.

**Errores frecuentes.** Confundir gateway con interfaz o asumir que una ruta por defecto se utiliza cuando existe una ruta más específica.

**Comprobación.** ¿Qué campos mínimos necesitas para comprender por dónde se enviará un paquete?

### 8.5.4 — Rutas estáticas

**Propósito y modelo.** Una ruta estática es configurada manualmente por un administrador y define destino, prefijo y siguiente salto o interfaz. Es predecible y útil en topologías pequeñas o rutas específicas, pero requiere mantenimiento y puede fallar si cambia la topología.

**Ejemplo desarrollado.** Una ruta a 198.51.100.0/24 vía 192.0.2.1 indica que el siguiente salto debe alcanzarse por la red local. Las direcciones se reservan para documentación.

**Práctica guiada.** Analiza comandos de ejemplo para Linux y Windows, pero no los ejecutes en el host. Identifica destino, máscara/prefijo, gateway e interfaz y describe cómo verificar y revertir.

**Actividad independiente.** Diseña rutas estáticas para conectar dos sucursales y documenta rutas de retorno y ruta de respaldo.

**Criterios de aceptación.** Construye una ruta coherente en papel y explica riesgo de rutas obsoletas.

**Errores frecuentes.** Configurar un gateway no alcanzable o olvidar la ruta de retorno; cambiar rutas remotas sin acceso alternativo.

**Comprobación.** ¿Qué procedimiento de reversión debe prepararse antes de modificar la tabla de rutas de un equipo remoto?

### 8.5.5 — Rutas dinámicas

**Propósito y modelo.** Los protocolos de routing dinámico intercambian información de alcanzabilidad y calculan rutas. OSPF es un protocolo de estado de enlace dentro de un sistema autónomo; BGP intercambia rutas entre sistemas autónomos y también puede usarse internamente. Cada protocolo tiene métricas, políticas y requisitos propios.

**Ejemplo desarrollado.** OSPF calcula rutas a partir de una base de estado de enlace y costo; BGP selecciona rutas según atributos y políticas, no simplemente por menor distancia física.

**Práctica guiada.** Compara conceptualmente OSPF y BGP en un diagrama con tres routers y dos sistemas autónomos. No establezcas sesiones de routing en redes ajenas.

**Actividad independiente.** Selecciona routing estático u OSPF para una red interna pequeña y justifica convergencia, complejidad, redundancia y operación.

**Criterios de aceptación.** Diferencia routing interior y exterior y explica por qué las políticas afectan selección de rutas.

**Errores frecuentes.** Tratar BGP como un protocolo que elige siempre la ruta más corta o habilitar vecinos sin filtros y autenticación donde aplique.

**Comprobación.** ¿Por qué la selección BGP depende de políticas además de la alcanzabilidad?

### 8.5.6 — NAT

**Propósito y modelo.** NAT modifica información de direcciones IP y, en variantes como PAT/NAPT, puertos de transporte para permitir que varias direcciones privadas compartan una dirección externa. No es un control de autenticación ni reemplaza firewall; puede complicar trazabilidad y conectividad extremo a extremo.

**Ejemplo desarrollado.** Un router traduce origen privado 192.168.1.10:50000 a una dirección WAN y puerto asignado. La tabla de traducción mantiene asociación para devolver respuestas.

**Práctica guiada.** Dibuja una traducción NAT/PAT con direcciones de documentación y registra tuplas antes/después. No configures NAT en equipos de producción.

**Actividad independiente.** Diseña conectividad saliente para una LAN privada y explica qué controles adicionales requiere publicar un servicio entrante.

**Criterios de aceptación.** Distingue NAT estático, dinámico y PAT a nivel conceptual; explica límites de seguridad.

**Errores frecuentes.** Afirmar que NAT es equivalente a firewall o exponer servicios sin limitar puertos y orígenes.

**Comprobación.** ¿Qué información mantiene PAT para asociar una respuesta al host interno correcto?

### 8.5.7 — VLAN

**Propósito y modelo.** Una VLAN crea un dominio lógico de capa 2 independiente sobre infraestructura conmutada compartida. La etiqueta IEEE 802.1Q identifica VLAN en enlaces troncales; puertos de acceso suelen transportar una VLAN sin etiqueta hacia el equipo final. La comunicación entre VLAN requiere routing de capa 3 y políticas.

**Ejemplo desarrollado.** Usuarios en VLAN 10 y servidores en VLAN 20 no se comunican directamente a través de capa 2; el router o switch capa 3 enruta entre ellas y aplica ACL/firewall según diseño.

**Práctica guiada.** Dibuja dos VLAN en un switch y un enlace a un router o switch capa 3. Identifica puertos access y trunk. No cambies VLAN de un switch productivo.

**Actividad independiente.** Diseña VLAN para usuarios, invitados, servidores y administración con subredes y flujos permitidos.

**Criterios de aceptación.** Explica dominio de broadcast, tagging 802.1Q y necesidad de routing inter-VLAN.

**Errores frecuentes.** Considerar VLAN como cifrado o permitir todas las VLAN en trunks sin necesidad.

**Comprobación.** ¿Por qué una VLAN no impide por sí sola que dos segmentos se comuniquen mediante un router?

### 8.5.8 — Trunking

**Propósito y modelo.** Un enlace trunk transporta tráfico de varias VLAN entre switches, routers o hipervisores, normalmente mediante etiquetas 802.1Q. La VLAN nativa y la lista de VLAN permitidas deben configurarse de forma coherente en ambos extremos. Un trunk mal configurado puede filtrar o exponer tráfico.

**Ejemplo desarrollado.** Un trunk entre switches puede transportar VLAN 10, 20 y 99; permitir VLAN adicionales innecesarias amplía el dominio de exposición. La VLAN nativa debe coincidir para evitar comportamientos inesperados.

**Práctica guiada.** Interpreta una configuración de trunk de laboratorio e identifica modo, VLAN nativa y VLAN permitidas. No modifiques enlaces de producción.

**Actividad independiente.** Diseña un trunk entre switch de acceso y distribución con solo las VLAN requeridas y un plan de validación.

**Criterios de aceptación.** Diferencia access/trunk y explica etiquetas, VLAN nativa y lista permitida.

**Errores frecuentes.** Dejar todas las VLAN permitidas o usar la VLAN nativa como red de usuarios sin evaluar riesgo.

**Comprobación.** ¿Qué riesgo reduce limitar explícitamente las VLAN permitidas en un trunk?

### 8.5.9 — Segmentación

**Propósito y modelo.** La segmentación divide una red en zonas con diferentes niveles de confianza o función. Puede implementarse con VLAN, subredes, firewalls, ACL, VRF y controles de identidad. La segmentación efectiva requiere definir flujos necesarios y bloquear el resto; separar direcciones sin aplicar políticas no basta.

**Ejemplo desarrollado.** Una aplicación de tres capas separa frontend, backend y base de datos. Solo el frontend acepta tráfico de usuarios; backend permite conexión desde frontend; base de datos solo acepta conexiones del backend.

**Práctica guiada.** Construye una matriz de origen/destino/servicio/justificación para tres zonas. Identifica reglas que deben denegarse.

**Actividad independiente.** Diseña segmentación para una organización con usuarios, servidores, invitados, IoT y administración; incluye monitoreo y excepciones documentadas.

**Criterios de aceptación.** Define zonas, flujos permitidos y denegación por defecto; justifica controles de capa 2/3/4.

**Errores frecuentes.** Crear VLAN sin ACL intersegmento o permitir administración desde la red de invitados.

**Comprobación.** ¿Cómo se demuestra que una segmentación funciona y no es solo una separación lógica de direcciones?

### 8.5.10 — Subredes

**Propósito y modelo.** Una subred es un bloque de direcciones IP definido por un prefijo. La división en subredes organiza rutas, dominios de broadcast IPv4 y políticas de acceso. El tamaño debe responder al número de hosts, crecimiento, servicios y necesidades de resiliencia.

**Ejemplo desarrollado.** Un /27 contiene 32 direcciones IPv4 totales; en una subred convencional, 30 son asignables a hosts. Las excepciones de punto a punto y protocolos deben tratarse según diseño.

**Práctica guiada.** Resuelve una subred /27 con direcciones de documentación y determina red, broadcast, rango asignable y gateway posible.

**Actividad independiente.** Asigna subredes a cinco áreas con tamaños distintos, sin solapamiento y con reserva para crecimiento.

**Criterios de aceptación.** Calcula límites, evita solapamientos y distingue subred de VLAN.

**Errores frecuentes.** Tratar VLAN y subred como equivalentes absolutos o asignar un gateway fuera del prefijo.

**Comprobación.** ¿Qué relación existe entre una VLAN y una subred IP, y por qué no son el mismo concepto?

## 8.6 — Seguridad de redes

### 8.6.1 — Firewalls

**Propósito y modelo.** Un firewall controla tráfico que cruza un límite de seguridad mediante reglas de origen, destino, protocolo, puerto, estado y, en algunos productos, aplicación o identidad. Puede ser de red, host, nube o aplicación. Su efectividad depende de política, orden, inspección, logging y mantenimiento.

**Ejemplo desarrollado.** Una política de denegación por defecto permite solo HTTPS hacia el frontend y una conexión específica del frontend hacia backend. La administración se limita a una red de gestión y se registra.

**Práctica guiada.** Lee un conjunto de reglas sintéticas y determina qué flujo coincide primero. Identifica regla redundante, excesiva y faltante sin modificar firewalls reales.

**Actividad independiente.** Construye política para una aplicación de tres capas, con entradas, salidas y administración mínimas.

**Criterios de aceptación.** Explica dirección, estado, orden y denegación por defecto; justifica cada excepción.

**Errores frecuentes.** Crear reglas Any/Any, no revisar reglas obsoletas o considerar que el firewall evita errores de autorización de aplicación.

**Comprobación.** ¿Por qué una política permisiva de salida también puede representar un riesgo?

### 8.6.2 — VPN

**Propósito y modelo.** Una VPN crea un túnel lógico sobre una red subyacente para proteger tráfico o conectar redes. Puede ser acceso remoto o site-to-site, y operar en capa 2 o 3 según tecnología. Cifrado, autenticación de pares, gestión de claves, rutas, DNS y segmentación determinan su seguridad.

**Ejemplo desarrollado.** Una VPN de acceso remoto puede permitir a un empleado alcanzar solo aplicaciones corporativas, no toda la LAN. El túnel cifrado protege el tránsito, pero el dispositivo final y las credenciales aún deben estar protegidos.

**Práctica guiada.** Dibuja una VPN de acceso remoto y una site-to-site. Identifica extremos, redes anunciadas, autenticación y rutas. No configures túneles contra redes ajenas.

**Actividad independiente.** Diseña acceso remoto con MFA, postura de dispositivo, segmentación por rol, registro y procedimiento de revocación.

**Criterios de aceptación.** Diferencia tipos de VPN y explica qué protege y qué no protege el túnel.

**Errores frecuentes.** Considerar VPN como anonimato total o permitir acceso amplio sin revisar rutas y políticas.

**Comprobación.** ¿Por qué una VPN cifrada no garantiza que el usuario solo acceda a los recursos que necesita?

### 8.6.3 — DMZ

**Propósito y modelo.** Una DMZ es una zona de red intermedia que aloja servicios que necesitan comunicación con redes externas, separándolos de sistemas internos sensibles. El diseño establece flujos explícitos entre Internet, DMZ y LAN; no basta con crear una subred etiquetada como DMZ.

**Ejemplo desarrollado.** Un servidor web público reside en DMZ; solo puede iniciar conexiones necesarias hacia un backend específico. La base de datos permanece en una zona interna y no acepta conexiones directas desde Internet.

**Práctica guiada.** Dibuja tres zonas y escribe matriz de flujos: Internet→web, web→backend, backend→base de datos y administración desde red de gestión. Marca el resto como denegado.

**Actividad independiente.** Diseña una DMZ para portal web y servidor de correo, con límites de confianza, monitoreo, parcheo y acceso administrativo.

**Criterios de aceptación.** Explica el propósito de DMZ y define flujos entre zonas con mínimo privilegio.

**Errores frecuentes.** Permitir DMZ→LAN sin restricción o alojar base de datos expuesta en la misma zona que el servidor público.

**Comprobación.** ¿Qué debe ocurrir con el tráfico desde la DMZ hacia la red interna que no esté expresamente autorizado?

### 8.6.4 — ACL

**Propósito y modelo.** Una ACL es una lista de reglas que permite o deniega tráfico o acceso a recursos según criterios definidos. En redes, puede filtrar direcciones, protocolos y puertos en interfaces; en sistemas, controla acceso a objetos. La ubicación, orden y semántica de evaluación son específicas de plataforma.

**Ejemplo desarrollado.** Una ACL extendida puede permitir TCP desde una subred de usuarios a un servidor en puerto 443 y denegar otros flujos hacia esa zona. Debe existir una regla final coherente con la política.

**Práctica guiada.** Interpreta una ACL sintética línea por línea. Para cada paquete de ejemplo identifica la primera regla coincidente y el resultado.

**Actividad independiente.** Diseña una ACL para permitir administración SSH solo desde una subred de gestión y bloquear el resto de orígenes.

**Criterios de aceptación.** Identifica criterios, orden y acción; explica el efecto de una regla implícita de denegación cuando aplique.

**Errores frecuentes.** Colocar reglas específicas después de una regla general o asumir que todas las plataformas procesan ACL de forma idéntica.

**Comprobación.** ¿Por qué el orden de reglas puede cambiar el resultado de una ACL?

### 8.6.5 — Puertos abiertos

**Propósito y modelo.** Un puerto abierto indica que un proceso o dispositivo acepta conexiones en una combinación de dirección, protocolo y puerto. Un puerto TCP en escucha no demuestra vulnerabilidad por sí mismo; debe identificarse servicio, versión, exposición, autenticación y necesidad de negocio. UDP no utiliza el mismo concepto de handshake, por lo que la detección es distinta.

**Ejemplo desarrollado.** Un servicio puede escuchar solo en loopback y no ser accesible desde la red, aunque aparezca en una lista local. Otro puede escuchar en todas las interfaces y quedar expuesto por firewall o router.

**Práctica guiada.** En un host propio consulta sockets con `ss -lntup` o `Get-NetTCPConnection -State Listen`. Registra protocolo, dirección local y proceso; no escanees terceros.

**Actividad independiente.** Construye inventario de servicios esperados y compara con puertos en escucha de una VM de laboratorio.

**Criterios de aceptación.** Diferencia escucha local, exposición de red y accesibilidad efectiva; identifica proceso propietario.

**Errores frecuentes.** Cerrar puertos a ciegas o concluir que un puerto es accesible desde Internet solo porque escucha localmente.

**Comprobación.** ¿Qué diferencia existe entre un puerto en escucha en 127.0.0.1 y uno en 0.0.0.0?

### 8.6.6 — Servicios expuestos

**Propósito y modelo.** Un servicio expuesto es una aplicación o función accesible desde una zona de red determinada. La exposición se evalúa por interfaz de escucha, rutas, NAT, firewall, balanceadores, autenticación, versión y datos procesados. Inventariar exposición es una actividad continua, no una fotografía única.

**Ejemplo desarrollado.** Un panel de administración puede estar protegido por contraseña, pero si se expone a Internet aumenta la superficie de ataque y debe limitarse por VPN, IP de gestión o proxy con controles robustos.

**Práctica guiada.** Revisa una arquitectura ficticia e identifica servicios públicos, internos y administrativos. Para cada uno registra propietario, puerto, propósito y control de acceso.

**Actividad independiente.** Crea un registro de exposición con clasificación de criticidad, justificación comercial, responsable, fecha de revisión y plan de retirada.

**Criterios de aceptación.** Distingue servicio necesario de servicio accidentalmente expuesto y propone mitigaciones proporcionadas.

**Errores frecuentes.** Mantener interfaces de administración públicas o asumir que un servicio está protegido solo porque usa HTTPS.

**Comprobación.** ¿Qué preguntas deben responderse antes de publicar un nuevo servicio en Internet?

### 8.6.7 — Superficie de ataque

**Propósito y modelo.** La superficie de ataque comprende interfaces, servicios, identidades, dependencias, rutas de red y funciones que un adversario podría intentar utilizar. Se reduce eliminando componentes innecesarios, limitando privilegios, segmentando, parcheando y monitoreando. No se mide solo contando puertos.

**Ejemplo desarrollado.** Un servidor con SSH, panel de administración, base de datos y agente de monitoreo tiene distintas rutas de acceso y dependencias. Retirar un servicio no usado puede reducir exposición, siempre que se valide que no sea dependencia de otro componente.

**Práctica guiada.** Sobre un diagrama de laboratorio, enumera activos, interfaces, cuentas, servicios y dependencias. Clasifica cada elemento por exposición y sensibilidad.

**Actividad independiente.** Prioriza cinco medidas de reducción de superficie usando impacto, esfuerzo y riesgo operativo.

**Criterios de aceptación.** Define superficie de ataque y justifica medidas con relación a activos y amenazas.

**Errores frecuentes.** Confundir vulnerabilidad con superficie de ataque o deshabilitar servicios críticos sin análisis de dependencia.

**Comprobación.** ¿Por qué reducir componentes innecesarios puede disminuir riesgo aunque no se haya descubierto una vulnerabilidad concreta?

### 8.6.8 — Filtrado de tráfico

**Propósito y modelo.** El filtrado de tráfico aplica reglas a paquetes o flujos según origen, destino, protocolo, puerto, estado y zona. Puede ocurrir en host, router, firewall, nube o aplicación. El filtrado stateful mantiene contexto de conexiones; stateless evalúa cada paquete según reglas sin mantener estado de sesión equivalente.

**Ejemplo desarrollado.** Un firewall stateful puede permitir respuestas de una conexión saliente ya establecida sin crear una regla de entrada general. Una ACL stateless puede requerir reglas explícitas para tráfico de retorno.

**Práctica guiada.** Clasifica flujos sintéticos y determina qué regla permite o deniega cada uno. Explica diferencia entre filtrado stateful y stateless.

**Actividad independiente.** Construye reglas para tráfico web entrante y DNS saliente de un segmento, con logging de denegaciones relevantes.

**Criterios de aceptación.** Identifica atributos del flujo y diferencia evaluación stateful/stateless.

**Errores frecuentes.** Permitir rangos amplios para simplificar reglas o no considerar el tráfico de retorno y los protocolos auxiliares.

**Comprobación.** ¿Qué contexto conserva un firewall stateful que un filtro stateless no mantiene de la misma forma?

### 8.6.9 — Políticas de filtrado

**Propósito y modelo.** Una política de filtrado traduce requisitos de negocio y seguridad en reglas ordenadas, revisables y verificables. Debe establecer zonas, propietarios, flujos autorizados, denegación por defecto, logging, excepciones temporales, revisión y proceso de cambio. Las reglas huérfanas y duplicadas degradan la claridad y el control.

**Ejemplo desarrollado.** Una regla temporal de soporte debe incluir responsable, origen limitado, servicio, fecha de expiración y ticket. Sin caducidad, una excepción puntual puede convertirse en exposición permanente.

**Práctica guiada.** Audita una política ficticia y marca reglas sin propietario, Any/Any, solapadas, sin justificación o sin fecha de expiración.

**Actividad independiente.** Redacta una política para una red corporativa con usuarios, servidores, invitados y administración. Incluye proceso de aprobación y revisión trimestral.

**Criterios de aceptación.** Produce reglas justificadas, trazables y con vencimiento para excepciones; distingue política de implementación.

**Errores frecuentes.** Dejar reglas temporales indefinidas, no registrar cambios o utilizar nombres ambiguos que impiden auditar.

**Comprobación.** ¿Qué información mínima permite revisar y retirar una excepción de firewall de forma segura?

## 8.7 — Herramientas

### 8.7.1 — Wireshark

**Propósito y modelo.** Wireshark captura y analiza paquetes mediante una interfaz gráfica y disectores de protocolos. Permite filtrar captura y visualización, reconstruir conversaciones y examinar cabeceras. La captura puede contener credenciales, cookies, datos personales o contenido confidencial; debe limitarse a interfaces y redes autorizadas y protegerse como evidencia sensible.

**Ejemplo desarrollado.** Un filtro de visualización `dns` muestra paquetes DNS ya capturados; un filtro de captura limita lo que se almacena desde el inicio. Son sintaxis y momentos de aplicación distintos.

**Práctica guiada.** Abre una captura de ejemplo o genera tráfico propio en loopback/laboratorio. Filtra DNS y TCP, identifica origen, destino, puertos y protocolo. No captures redes de terceros.

**Actividad independiente.** Documenta una conversación TCP con handshake, datos y cierre; redacta hallazgos sin incluir secretos ni payloads sensibles.

**Criterios de aceptación.** Distingue captura de visualización, identifica campos y conserva evidencia con fecha, interfaz y alcance autorizado.

**Errores frecuentes.** Compartir archivos PCAP sin sanitizar o creer que un filtro de visualización impide capturar datos sensibles.

**Comprobación.** ¿Por qué un archivo PCAP debe tratarse como información potencialmente confidencial?

### 8.7.2 — tcpdump

**Propósito y modelo.** tcpdump captura y muestra paquetes desde interfaces mediante filtros BPF. Permite observar tráfico en sistemas sin interfaz gráfica y guardar PCAP para análisis posterior. Requiere privilegios elevados en muchos sistemas; la captura debe tener alcance mínimo, duración definida y autorización.

**Ejemplo desarrollado.** `tcpdump -i lo -nn port 53` limita la observación a loopback y tráfico del puerto DNS. `-w` escribe un archivo de captura, que puede contener datos sensibles.

**Práctica guiada.** En una VM propia captura una consulta DNS de laboratorio en loopback o interfaz aislada, con duración breve. Identifica interfaz, filtro y número de paquetes. No captures tráfico de terceros.

**Actividad independiente.** Redacta un plan de captura con objetivo, interfaz, filtro, tiempo, permisos, almacenamiento y borrado seguro.

**Criterios de aceptación.** Explica interfaz, filtro BPF, salida en pantalla y PCAP; justifica minimización de datos.

**Errores frecuentes.** Capturar en todas las interfaces indefinidamente o guardar PCAP en carpetas compartidas sin control de acceso.

**Comprobación.** ¿Qué diferencia hay entre seleccionar una interfaz y definir un filtro BPF?

### 8.7.3 — Nmap

**Propósito y modelo.** Nmap descubre hosts y caracteriza servicios en redes bajo autorización. Las técnicas pueden generar tráfico detectable y afectar sistemas frágiles; el alcance debe limitarse a activos propios o expresamente autorizados, con ventana y tasa apropiadas. Un resultado «open», «closed» o «filtered» describe observación de red, no certifica vulnerabilidad.

**Ejemplo desarrollado.** Un escaneo de un host de laboratorio con un conjunto limitado de puertos puede mostrar si el puerto responde como abierto, cerrado o filtrado. El resultado depende de firewall, ruta y técnica de sondeo.

**Práctica guiada.** Utiliza únicamente un objetivo local o una VM propia aislada. Ejecuta un escaneo básico limitado a un único host de laboratorio y pocos puertos; registra fecha, objetivo autorizado y parámetros. No escanees rangos públicos ni redes ajenas.

**Actividad independiente.** Elabora un informe de exposición para una VM propia y contrasta cada puerto con el inventario de servicios esperado. Define cómo cerrar o justificar cada exposición, sin explotar servicios.

**Criterios de aceptación.** Diferencia descubrimiento, estado de puerto y evaluación de vulnerabilidades; documenta autorización y alcance exacto.

**Errores frecuentes.** Escanear direcciones fuera del alcance, interpretar filtered como closed o afirmar que un puerto abierto implica vulnerabilidad.

**Comprobación.** ¿Qué evidencia adicional se necesita para determinar si un servicio expuesto es vulnerable?

### 8.7.4 — ping

**Propósito y modelo.** ping envía mensajes ICMP Echo para comprobar si un destino responde y medir tiempo de ida y vuelta aproximado. El resultado depende de rutas, firewall, priorización y configuración del destino; no mide por sí solo la calidad de una aplicación ni demuestra que todos los servicios funcionen.

**Ejemplo desarrollado.** Un servidor puede responder ping pero tener HTTPS caído; otro puede bloquear Echo y ofrecer SSH correctamente. La pérdida observada puede deberse a filtrado o limitación de ICMP.

**Práctica guiada.** Ejecuta ping hacia loopback y una VM propia. Compara respuesta con una comprobación de servicio TCP autorizada.

**Actividad independiente.** Interpreta tres resultados: respuesta estable, pérdida parcial y timeout completo. Indica qué hipótesis y pruebas adicionales corresponden.

**Criterios de aceptación.** Explica RTT, pérdida y límites de ICMP Echo; no infiere disponibilidad de aplicación solo por ping.

**Errores frecuentes.** Concluir que un host está apagado cuando no responde o comparar RTT de pruebas realizadas en condiciones distintas sin contexto.

**Comprobación.** ¿Qué demuestra una respuesta Echo y qué no demuestra sobre un servicio web?

### 8.7.5 — traceroute

**Propósito y modelo.** traceroute/tracert infiere saltos de una ruta utilizando TTL IPv4 o Hop Limit IPv6 y respuestas de routers. Las técnicas varían entre sistemas (UDP, ICMP o TCP). Algunos dispositivos no responden o filtran sondas, por lo que los asteriscos no prueban pérdida de tránsito.

**Ejemplo desarrollado.** Un salto intermedio puede no responder a la sonda y el destino final sí responder. El tráfico de aplicación puede seguir una ruta distinta por políticas, balanceo o rutas asimétricas.

**Práctica guiada.** Ejecuta traceroute hacia un destino público común o una VM propia, respetando políticas locales. Registra saltos y latencias sin interpretar cada silencio como fallo.

**Actividad independiente.** Compara dos trazas realizadas en momentos diferentes y explica cambios posibles por balanceo, rutas dinámicas y filtrado ICMP.

**Criterios de aceptación.** Explica TTL/Hop Limit y límites de visibilidad de la ruta.

**Errores frecuentes.** Tratar traceroute como mapa exacto de todos los routers o asumir que un salto sin respuesta está descartando tráfico de usuario.

**Comprobación.** ¿Por qué un router puede reenviar tráfico correctamente y no responder a las sondas de traceroute?

### 8.7.6 — ip

**Propósito y modelo.** La utilidad ip de iproute2 administra y consulta interfaces, direcciones, vecinos, rutas y túneles en Linux. Permite observar configuración con subcomandos como `ip addr`, `ip link`, `ip route` e `ip neigh`. Los subcomandos de modificación pueden interrumpir conectividad y deben probarse en VM aislada.

**Ejemplo desarrollado.** `ip addr show` consulta direcciones; `ip route` muestra rutas. `ip link set` cambia estado de interfaz y no debe ejecutarse en un equipo remoto sin acceso alternativo.

**Práctica guiada.** Ejecuta solo consultas `ip addr`, `ip link`, `ip route` e `ip neigh` en una VM propia. Registra interfaz, dirección, gateway y vecinos.

**Actividad independiente.** Diagnostica un caso sintético de host sin conectividad ordenando comprobaciones de enlace, dirección, ruta, vecino y DNS.

**Criterios de aceptación.** Diferencia subcomandos de consulta y modificación y explica qué capa de información presenta cada uno.

**Errores frecuentes.** Ejecutar cambios de interfaz sobre una sesión remota sin consola o confundir configuración IP con resolución DNS.

**Comprobación.** ¿Qué información ofrece `ip neigh` que no aparece en `ip route`?

### 8.7.7 — ss

**Propósito y modelo.** ss consulta sockets y estadísticas de red en Linux. Permite listar conexiones TCP/UDP, puertos en escucha, estados y procesos asociados cuando se dispone de permisos. La salida representa una instantánea y debe interpretarse con dirección local/remota y estado.

**Ejemplo desarrollado.** `ss -lntp` muestra sockets TCP en escucha con información de proceso cuando está disponible; `ss -tunap` ofrece una vista más amplia de sockets TCP/UDP.

**Práctica guiada.** Ejecuta `ss -lnt` y registra puertos TCP en escucha de tu VM. Compara una escucha en loopback con una en todas las interfaces. No cierres procesos.

**Actividad independiente.** Relaciona puertos en escucha con inventario de servicios y prioriza los que no tienen justificación.

**Criterios de aceptación.** Identifica protocolo, estado y direcciones; distingue escucha de conexión establecida.

**Errores frecuentes.** Suponer que un puerto en escucha es accesible desde Internet o terminar el proceso sin verificar dependencias.

**Comprobación.** ¿Qué significa que un servicio escuche en 127.0.0.1 en lugar de 0.0.0.0?

### 8.7.8 — netstat

**Propósito y modelo.** netstat es una herramienta tradicional para consultar conexiones, puertos, estadísticas y rutas; en Linux ha sido reemplazada en gran medida por ss, aunque sigue disponible en diversos sistemas. Las opciones y salidas difieren entre Windows, Linux y otros entornos.

**Ejemplo desarrollado.** En Windows `netstat -ano` muestra conexiones y PID; en Linux `netstat -tulpen` puede mostrar sockets y procesos si está instalado. El PID debe correlacionarse con el proceso antes de actuar.

**Práctica guiada.** En un sistema propio consulta conexiones y puertos en escucha con las opciones apropiadas para ese sistema. No termines procesos ni publiques direcciones internas.

**Actividad independiente.** Compara netstat y ss para una misma VM Linux: campos, velocidad, disponibilidad y utilidad actual.

**Criterios de aceptación.** Identifica plataforma y opciones, interpreta local/remoto/estado/PID y explica limitaciones.

**Errores frecuentes.** Copiar opciones de Linux en Windows o asumir que netstat es un analizador de paquetes.

**Comprobación.** ¿Por qué se recomienda conocer la plataforma antes de utilizar opciones de netstat?

### 8.7.9 — dig

**Propósito y modelo.** dig consulta servidores DNS y presenta respuestas detalladas, autoridad, secciones adicionales y tiempos. Permite especificar tipo de registro, resolver y opciones de diagnóstico. Las consultas deben limitarse a dominios y servidores para los que se tiene autorización cuando se realizan pruebas avanzadas.

**Ejemplo desarrollado.** `dig example.com A` consulta un registro A; `dig +short` reduce la salida. `dig @servidor nombre tipo` selecciona explícitamente el resolver.

**Práctica guiada.** Consulta A, AAAA y MX de un dominio de prueba. Identifica status, flags, answer y TTL. No realices AXFR ni enumeración de zonas sin autorización explícita.

**Actividad independiente.** Diagnostica un escenario sintético donde un cliente usa un resolver incorrecto o recibe una respuesta obsoleta en caché.

**Criterios de aceptación.** Interpreta tipo, TTL, servidor consultado y código de respuesta; diferencia NXDOMAIN de timeout.

**Errores frecuentes.** Confundir respuesta vacía con NXDOMAIN o concluir que el servidor autoritativo está caído porque un resolver no responde.

**Comprobación.** ¿Qué diferencia hay entre NXDOMAIN y SERVFAIL?

### 8.7.10 — nslookup

**Propósito y modelo.** nslookup es una herramienta de consulta DNS disponible en Windows y otros sistemas. Permite resolver nombres, consultar tipos de registro y seleccionar servidor DNS. Su salida es más simple que dig en ciertos escenarios, pero resulta útil para diagnósticos básicos y entornos Windows.

**Ejemplo desarrollado.** `nslookup example.com` consulta el resolver configurado; `nslookup -type=MX example.com` solicita registros MX. La respuesta muestra servidor consultado y datos devueltos.

**Práctica guiada.** Consulta un dominio de documentación y sus registros A, AAAA y MX. Compara el resultado con `dig` si está disponible.

**Actividad independiente.** Redacta una secuencia para distinguir error de resolución, respuesta NXDOMAIN y problema de conectividad hacia el servidor DNS.

**Criterios de aceptación.** Identifica servidor, nombre, tipo de registro y respuesta; explica limitaciones de la herramienta.

**Errores frecuentes.** Interpretar «Server: Unknown» como prueba automática de fallo DNS o asumir que una resolución exitosa prueba conectividad a la aplicación.

**Comprobación.** ¿Qué indica nslookup cuando muestra una respuesta DNS válida pero el sitio no abre?

### 8.7.11 — curl

**Propósito y modelo.** curl transfiere datos mediante protocolos como HTTP, HTTPS, FTP y otros, según compilación. En HTTP permite inspeccionar cabeceras, códigos, redirecciones y tiempos; también puede enviar datos y modificar estado. Las opciones deben usarse con cuidado para no transmitir secretos ni ejecutar operaciones destructivas.

**Ejemplo desarrollado.** `curl -I https://example.com` solicita cabeceras; `curl -i` muestra cabeceras y cuerpo. `-k` desactiva validación TLS y no debe utilizarse como solución permanente.

**Práctica guiada.** Consulta un endpoint público de prueba con `curl -I` y registra código de estado, servidor y cabeceras relevantes. No incluyas tokens ni datos personales.

**Actividad independiente.** Diseña pruebas de API para respuesta 200, 401, 404 y timeout; define qué opción de curl usarías y qué evidencia guardarías.

**Criterios de aceptación.** Distingue método, cabeceras, cuerpo y código; explica por qué no se debe desactivar la validación TLS.

**Errores frecuentes.** Pegar tokens en historial de shell, seguir redirecciones sin revisar destino o enviar POST de prueba a servicios reales sin autorización.

**Comprobación.** ¿Qué información aporta `curl -I` y qué limitación tiene frente a una solicitud completa?

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
