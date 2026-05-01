# TP3 - 

### Grupo: WAN-PIECE
### Profesores
- Santiago Martin Henn
- Facundo Nicolas Oliva Cuneo

### Integrantes

| Nombre                  | Correo Electrónico              | 
|-------------------------|---------------------------------|
| Benavides María Candela |candela.benavides@mi.unc.edu.ar |
| Fariñas Rafael          |rafael.farinas@mi.unc.edu.ar     |
| Melia Nicolas           |nicolas.melia@mi.unc.edu.ar      |
| Salinas Joaquín         |joaquin.salinas.874@mi.unc.edu.ar|


### 1. Investigación conceptual
#### a. ¿Qué es SSH y qué problema resuelve?

SSH (Secure Shell) es un protocolo de red que permite establecer conexiones seguras entre dos equipos. Surge como reemplazo de protocolos anteriores como Telnet, rlogin o FTP, que transmitían toda la información incluyendo contraseñas y datos en texto plano, lo que los hacía vulnerables a intercepción (sniffing) y ataques de tipo man-in-the-middle.
SSH proporciona tres cosas: autenticación del servidor y del cliente, cifrado de toda la comunicación, e integridad de los datos.

#### b. Diferencias entre autenticación y cifrado

Las diferencias entre autenticación y cifrado son: 

- Autenticación: es el proceso de verificar la identidad de las partes que participan en la comunicación.
- Cifrado: es el proceso de transformar los datos en un formato ininteligible para cualquier tercero que intercepte la comunicación, garantizando la confidencialidad.

La diferencia entre ambos que la autenticación protege la suplantación de identidad, mientras que el cifrado protege contra la lectura no autorizada del contenido. 

### c. ¿Qué es una clave pública y una clave privada?

La clave pública es la que se comparte libremente y puede ser conocida por cualquiera, mientras que la clave privada es secreta y solo la posee su dueño.

Esto permite dos funciones principales: que el emisor cifre el mensaje con la clave pública del destinatario, de modo que solo este puede descifralo con su clave privada, garantizando confidencialidad. Para garantizar autenticación, el emisor cifra o firma con su clave privada, y el receptor verifica con la clave pública correspondiente que el mensaje proviene de quien dice ser.

### d. ¿Por qué la clave privada no debe compartirse?

La clave privada no debe compartirse ya que es el elemento que garantiza tanto la identidad del propietario como la confidencialidad de los mensajes dirigidos a él. En el caso que de un tercero obtuviera la clave privada, podría suplantar la identidad del propietario firmando mensajes en su nombre, así como descrifrar toda la información que haya sido cifrada con la clave pública correspondiente.

#### e. ¿Qué ventajas tienen las claves SSH frente a contraseñas?

Las claves SSH ofrecen varias ventajas frente a las contraseñas.
- Son seguras ya que consisten en pares de claves criptográficas de gran longitud, haciendo que sean imposibles de adivinar mediante ataques de fuerza bruta, a diferencia de las contraseñas que suelen ser más cortas y vulnerables a este tipo de ataques.
- La clave privada nunca se transmite por la red durante la autenticación, mientras que las contraeñas sí deben enviarse al servidor, lo que las expone a una posible interceptación.
- Eliman el factor humano de elegir contraseñas débiles o reutilizarlas en múltiples servicios.


### 2. Verificación de conexión SSH



Para establecer la conexión de froma remota y segura hacia la máquina reservada, ejecutamos el siguiente comando en la terminal local 

`ssh -i Documentos/REDES\ TP3/pc4_key pc-alumnos-4@34.63.129.61`

donde cada parámetro parámetro utilizado tiene el siguiente significado: 

* ssh: Invoca el cliente del protocolo Secure Shell para iniciar la conexión segutra 
* `-i Documentos/REDES TP3/pc4_key` : El flag `-i` (identity file) indica la ruta exactahacia nuestra clave privada. Esto es lo que nos permite autenticarnos frente a la máquina virtual de forma segura, reemplazando el uso de una contraseña tradicional. 
* `pc-alumnos-4`: Es el nombre del usuario configurado para nuestro acceso en la máquina virtual
* `34.63.129.61`: Es la dirección IP pública asignada a nuestra instancia en la nube 


<img width="673" height="217" alt="WhatsApp Image 2026-04-22 at 18 48 55" src="https://github.com/user-attachments/assets/f6f1f552-5c71-47e1-848d-04878c38b956" />


Tal como se observa en la imagen, el proceso de autenticación fue exitoso. El servidor aceptó nuestra clave privada y nos devolvió el mensaje de bienvenida (MOTD), confirmando que estamos dentro de un sistema operativo Debian GNU/Linux 


#### Documentación del paso por la VM 
Para finalizar la documentación del paso por la VM, creamos un directorio con el nombre del grupo usando el comando `mkdir`. Tal como se observa en la captura, al ejecutar el comando `ls`, verificamos que la carpeta `WanPiece` se creó exitosamente en el directorio de trabajo de la máquina virtual. 
<img width="678" height="367" alt="image" src="https://github.com/user-attachments/assets/4db937f8-5ffa-43bd-838f-9ef2d99ae2f9" />


### 3. Captura del tráfico SSH 


<img width="1366" height="768" alt="WhatsApp Image 2026-04-22 at 18 45 37" src="https://github.com/user-attachments/assets/0d240537-98cf-4cfd-aae6-b7b729f64a6e" />



Para analizar la comunicación con la máquina virtual, iniciamos la captura en Wireshark y aplicamos el filtro `tcp.port == 22`. Este puerto es el que utiliza por defecto el protocolo SSH para escuchar peticiones de conexión  

Si observamos los primeros paquetes de la sesión SSH capturada, identificamos la fase de negociación criptográfica.Los paquetes muestran descripciones como "Key Exchange Init" y "Elliptic Curve Diffie-Hellman Key Exchange Reply", culminando con el mensaje de "New Keys". Esto evidencia el momento en el que el cliente local y el servidor en la nube estan acordando de forma segura las claves que usarán para proteger el resto de la sesión. 

#### Se puede decifrar el contenido?

No, no es posible descifrar el contenido a simple vista. 
Tal como se ve en la captura de Wireshark, inmediatamente después del intercambio de claves, todo el tráfico entrante y saliente ("Client" y "Server") pasa a ser etiquetado como "Encrypted packet" (paquete cifrado). A diferencia de otros protocolos donde los datos viajan en texto plano, SSH asegura que, una vez finalizado el handshake, toda la capa de aplicación viaje cifrada.Cualquier comando que tipearamos en la terminal o la respuesta que nos devuelve la MV es completamente ilegible para un atacante o sniffer que intercepte la red. 


### 4. Netcat para desplegar servidores simples y capturar tráfico. 

#### a. Montar un servidor TCP en alguno de los puertos habilitados en la VM 

##### Captura del Handshake TCP 

 Configuramos Wireshark para escuchar conexiones TCP hacia la VM que no fueran de SSH, utilizando el filtro `ip.dst == 34.60.142.134 and !ssh` 

 <img width="1366" height="768" alt="WhatsApp Image 2026-04-22 at 18 40 02" src="https://github.com/user-attachments/assets/94a0868e-d130-4d71-9d59-56b9c7c2e4fc" />

 
 En la imagen observamos el incio del handshake de tres vías del protocolo TCP.Específicamente, se identifica el primer paquete con e flag `[SYN]` yendo desde nuestra máquina local hacia el puerto 5555 de la máquina virtual 
 
 Cuando establecimos la conexión con Netcat, procedimos a enviar mensajes entra la computadora local y la VM en la nube 

En las siguientes imagenes se muestra el intercambio de tráfico. 


 <img width="1366" height="723" alt="WhatsApp Image 2026-04-22 at 18 38 16" src="https://github.com/user-attachments/assets/8bd38a58-6809-4f65-863e-345466c6def2" />



 <img width="1366" height="768" alt="WhatsApp Image 2026-04-22 at 18 40 28" src="https://github.com/user-attachments/assets/682aec32-3def-4aad-89ba-40c6ebf9ad99" />


Estos paquetes de datos se identifican con los flags `[PSH, ACK]` (Push y Acknowledgment), lo que indica que llevan carga útil o "Data payload" 


Aca el contenido es completamente descifrable el contenido. 
Si observamos la segunda imagen, en la sección que muestra el volcado hexadecimal y su traducción a ASCII, se puede leer en texto plano la frase que enviamos 

Esto demuestra que el protocolo TCP base transmite los datos en texto claro sin ninguna protección. A diferencia de lo que vimos con SSH, al no haber una capa de seguridad (como TLS/SSL) por encima, cualquier persona interceptando la red puede leer exactamente que nos estamos comunicando 

#### b. 
Para esta parte, repetimos la lógica del servidor anterior pero usando el protocolo UDP. Para esto, añadimos el flag `-u` en los comandos Netcat, tanto en el cliente como en el servidor. En las capturas adjuntas se puede observar cómo el cliente local envía exitosamente el mensaje y este es recibido por el servidor desplegado en la instancia de la nuba 
<img width="678" height="369" alt="image" src="https://github.com/user-attachments/assets/aafd26ef-7b10-40d8-8a6b-4ae3f5515fa1" />

<img width="678" height="369" alt="image" src="https://github.com/user-attachments/assets/462dcfbd-4a09-44ce-9121-b76ff033032f" />

#### c. 
Documentamos el ida y vuelta de un chat interactivo conectando dos máquinas virtuales distintas. Para esto, levantamos un servidor Netcat en el puerto 5555 de la VM 1. Luego, desde una terminal paralela conectada a la VM 5, iniciamos una conexión hacia la IP de la VM1 y enviamos los mensajes. En las imagenes se puede evidenciar la transmisión correcta de los datos entre ambas instancias virtualizadas de la nube 
<img width="1600" height="211" alt="image" src="https://github.com/user-attachments/assets/53f3f1ec-36f7-47f4-baa9-28358b95c8fa" />
(Servidor en la VM 1) 

<img width="678" height="369" alt="image" src="https://github.com/user-attachments/assets/ab7e5164-cfe2-40ef-a2f3-7f71188fcb3a" />
(Cliente en la VM 5).

### 5.

#### Despliegue y acceso 
Desplegamos un servidor HTTP utilizando Python. Como podemos ver en la primera captura del navegador, logramos acceder exitosamente introduciendo la IP pública de nuestra VM y el puerto elegido `34.63.129.61:5555` en la barra de direcciones. En la pantalla esta nuestro archivo `index.html` personalizado 

<img width="1361" height="681" alt="image" src="https://github.com/user-attachments/assets/a5174843-4881-4a6d-9f3b-4ff427a88dab" />

#### Captura de tráfico 
En paralelo, capturamos el tráfico con Wireshark. Al observar los paquetes, identificamos claramente la petición `GET / HTTP/1.1` generada por nuestro navegador al solicitar la página.

<img width="1366" height="724" alt="image" src="https://github.com/user-attachments/assets/2795d4b9-709b-4eec-a430-18aaa795db7c" />
(Paquetes en Wireshark) y 


<img width="1366" height="724" alt="image" src="https://github.com/user-attachments/assets/954d38ca-7a21-4232-a9c5-4d498303d676" />


El contenido es completamente descifrable e intervenible. Como vemos en la segunda captura. Esto demuestra que el protocolo HTTP transmite la información en texto plano y no posee seguridad inherente. Todo el código fuente HTML viaja expuesto, lo que significa que cualquier atacante interceptando la red podría leerlo con facilidad o incluso modificarlo antes de que llegue al navegador destino. 

### 6. The Silicon Heist: Hacking Apple Pay for $10,000

El video presenta un experimento de ciberseguridad donde se logra **extraer 10,000 dólares de un iPhone bloqueado** mediante una vulnerabilidad técnica. Este ataque de tipo "man-in-the-middle" aprovecha la función **Express Transit Mode**, engañando al dispositivo para que procese transacciones de alto valor sin requerir biometría o contraseñas. El fallo ocurre específicamente al combinar el sistema operativo de **Apple con tarjetas Visa**, ya que estas últimas no siempre exigen una firma criptográfica adicional en transacciones en línea. A pesar de que este riesgo se hizo público en 2021, las empresas involucradas argumentan que el fraude a gran escala es **improbable en el mundo real** y ofrecen reembolsos como solución. Por ello, los expertos recomiendan a los usuarios **desactivar el modo de tránsito rápido** o utilizar proveedores distintos para mitigar cualquier riesgo financiero.

Técnicamente, el ataque de "hombre en el medio" (Man-in-the-Middle o MITM) descrito en las fuentes funciona interceptando y alterando la comunicación inalámbrica entre un teléfono y un terminal de pago a través de un campo magnético compartido.

De esta manera l video muestra un ataque MITM real que conecta directamente con lo trabajado en los tres TPs
En el trabajo práctico 1 se nos  enseñó que los paquetes viajan hop a hop sin visión global del camino, y que un dispositivo intermedio puede interceptarlos. El Proxmark hace exactamente eso; se inserta entre el iPhone y el terminal como un "router malicioso" en la cadena.
En el TP 2 se demostró con Wireshark que cualquier dispositivo en el medio puede capturar tráfico. El Proxmark es el equivalente NFC de ponerse en escucha en un switch.

Por último en el TP 3 el experimento con netcat mostró que el tráfico sin cifrar es completamente legible y modificable en tránsito, igual que los bits de la transacción Visa. El servidor HTTP demostró que incluso el contenido puede intervenirse. SSH, en cambio, hacía el tráfico ininteligible es exactamente lo que le falta al canal NFC de Visa.

 **b) Principio de confidencialidad**
Los laboratorios demostraron que el tráfico no cifrado es tráfico público. Netcat y HTTP demostraron que cualquier observador en el camino (o en la misma red) puede leer y modificar el contenido. Esto aplica a cualquier protocolo que no cifre: HTTP, FTP, Telnet, y como muestra el video, ciertas implementaciones de pagos NFC. Por eso cifrar no es suficiente si no hay autenticación. Para ello se implementa la SSH, que  cifra el contenido y autentica que el otro extremo es quien dice ser mediante clave pública/privada.En el video, Visa en modo online omite la segunda parte, y eso es suficiente para que el ataque funcione.

Por lo tanto, la solución para esto es usar protocolos que cifren y autentiquen (SSH, TLS/HTTPS, y en pagos, esquemas con firma criptográfica asimétrica como los que usa MasterCard)



