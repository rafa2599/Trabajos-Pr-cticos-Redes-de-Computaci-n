# TP3 - 

### Grupo: WAN-PIECE
### Profesores
- Santiago Martin Henn
- Facundo Nicolas Oliva Cuneo

### Integrantes

| Nombre                  | Correo Electrónico              | 
|-------------------------|---------------------------------|
| Benavides María Candela | candela.benavides@mi.unc.edu.ar |
| Fariñas Rafael          |                                 |
| Melia Nicolas           |                                 |
| Salinas Joaquín         |joaquin.salinas.874@mi.unc.edu.ar|








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




