# Redes de Computadoras - Trabajo Práctico N°4

### Grupo: WAN-PIECE
### Profesores
- Santiago Martin Henn
- Facundo Nicolas Oliva Cuneo

### Integrantes

| Nombre                  | Correo Electrónico               |
|-------------------------|----------------------------------|
| Benavides María Candela |candela.benavides@mi.unc.edu.ar                  |
| Fariñas Rafael          | rafael.farinas@mi.unc.edu.ar     |
| Melia Nicolas           | nicolas.melia@unc.edu.ar      |
| Salinas Joaquín         | joaquin.salinas.874@mi.unc.edu.ar|

---

### 1) Sabemos que la información viaja a través de internet “empaquetada” según el protocolo de capa de transporte que utilicemos. Sin embargo, dentro de la carga útil de estos paquetes, la información debe estar organizada para poder realizar una interpretación correcta de su significado.
#### a) ¿Qué es la serialización en redes de computadoras?
La serialización es el proceso de convertir una estructura de datos en memoria a un formato lineal de bytes que pueda transmitirse por la red y luego reconstruirse en el destino. Es necesaria porque la memoria de cada máquina organiza los datos de forma diferente, por lo que no se puede "copiar" lo de la RAM y que se mande. La serialización estabalece un formato común que emisor y receptor entienden, independientemente de la arquitectura o lenguaje de programación.
#### b) ¿Cuál es la diferencia entre serialización binaria y no binaria? Buscar ejemplos, ventajas y desventajas
de cada una.
Las diferencias entre la serialización binaria y no binaria son:
- Binaria: los datos se codifican directamente en bytes según un esquema compacto, no legible.
Las ventajas que presenta es que es mucho más compacta y eficiente en ancho de banda, más rápida de serializar/deserializar. Las desventajas que presenta es que no es legible sin herramientas específicas, requiere un esquema compartido y es más compleja de depurar.
Ejemplos: Protocol Buffers(Google), MessagePack, CBOR.
- No binaria: los datos se presentan como texto legible por humanos.
Las ventajas que presenta es que es legible y depurable a simple vista, independiente de plataforma y fácil de inspeccionar. Mientras que las desventajas son que es mayor tamaño, más lento de parsear y no es apto para datos muy grandes o de alto rendimiento.
Ejemplos: JSON, XML, YAML. 

---
### 2) Servidor TCP multi-hilo

Se desplegó un servidor TCP multi-hilo en Python, escuchando en el puerto 5000. Utilizando PacketSender, se envió un mensaje JSON con la estructura requerida (group y payload) a través de una conexión TCP persistente hacia 127.0.0.1:5000. El servidor recibió el mensaje, lo deserializó correctamente y mostró por consola el grupo y la carga útil.
enter
![](/TP4/Img/PacketSender.jpeg)
![](/TP4/Img/Terminal.jpeg)

### 3) Programación de una aplicación de cliente
En este punto, para automatizar la comunicación cliente-servidor, usamos como base el script en python proporcionado por el profesor. Este establece un canal de transmisión fiable utlizando el protocolo TCP (Transmission Control Protocol). 
A diferencia de usar herramientas manuales, el script nos permite controlar automáticamente cómo se envían los datos. Creamos una conexión segura y directa con el servidor usando un "socket TCP", lo que garantiza que los paquetes lleguen a destino en el orden correcto y sin errores. 

#### Serialización 
La información se transmite utilizando serialización en formato JSON. La serialización es el proceso de convertir un objeto estructurado (en nuestro caso un diccionario de Python) en un formato de bytes que pueda ser transportado por la red y reconstruido en el extremo receptor. Usamo JSON porque es un formato de texto leeegible,ligero y universalmente compatible, facilitando la interpretación semántica del mensaje `group` y `payload` por parte del servidor multi-hilo implementado 

<img width="1437" height="1148" alt="image" src="https://github.com/user-attachments/assets/9883c2be-fbbc-458b-9452-56a7164ffae3" />


### 4) Implementación de una técnica de encriptación 

Para garantizar la confidencialidad y la integridad de la comunicación frente a posibles interceptaciones en redes no confiables, agregamos una capa de cifrado en el cliente 



#### Técnica de Cifrado 
Implementamos la técnica de cifrado simétrico utilizando el algoritmo AES(Advanced Encryption Standard), el cual es un estándar reconocido por su robustez y eficiencia. Especificamente, se utilizó la biblioteca `Fernet`, que es una implementación de alto nivel que aplica AES en modo CBC (Cipher Block Chaining),lo que hace este modo es que antes de cifrar cada bloque, este se combina (mediante una XOR) con el resultado del bloque anterior. Esto evita dar pistas a un atacante sobre el contenido. 
La criptografía simétrica se basa en el uso de una única clave secreta compartida entre el cliente y el servidor, lo que hace al proceso eficiente y seguro para el intercambio de datos entre extremos confiables. 
El cifrado fue aplicado unicamente sobre la carga útil `payload` del mensaje JSON, manteniendo el resto de la estructura en texto plana para permitir la identificación del emisor.  


#### Análisis de la implementación 
1. Generación de la clave
Creamos un script aulixiar `generar_clave.py` para establecer el secreto compartido

```
from cryptography.fernet import Fernet
clave = Fernet.generate_key()
with open("clave.key", "wb") as key_file:
    key_file.write(clave)
print("Clave generada y guardada en 'clave.key'")

```
Este genera una clave aleatoria y la almacena en un archivo binario `clave.key`. Este archivo es esencial para que tanto el emisor como el receptor puedan realizar operaciones de cifrado y descifrado de manera consistente

2. Carga de la clave secreta
   
Para aplicar el cifrado de forma efectiva en el cliente, se añadió el siguiente bloque de código
```
with open("clave.key", "rb") as key_file:
    clave = key_file.read()
cipher = Fernet(clave)

```
Este abre el archivo donde esta la llave compartida en modod binario `rb`. Al cargarla en el objeto `Fernet`, habilitamos el motor criptográfico necesario para realizar el cifrado y descifrado.

2. Proceso de cifrado del playload
    
```
texto_a_cifrar = message["payload"].encode("utf-8")
message["payload"] = cipher.encrypt(texto_a_cifrar).decode("utf-8")

```
Primero, convertimos el mensaje a formato bytes para que el algoritmo pueda procesarlo. Luego, la función `encrypt` transforma el contenido en una cadena cifrada ilegible, la cual reemplaza al texto plano original antes de que el objeto JSON sea enviado. De esta forma, el `payload` es transformado, cumpliendo con el principio de confidencialidad sin afectar la estructura 

#### Implementación 

##### Preparación del entorno 


<img width="1444" height="843" alt="image" src="https://github.com/user-attachments/assets/4ff73d52-bb42-4e20-a9b3-b7c7b3ba50c9" />


En este paso, se intalaron las dependencias necesarios en un entorno virtual aislado `(venv)`, ya que ubuntu no deja la instalación sin un entrono virtaul para proteger al sistema de instalaciones de paquetes globales con `pip`. 
Además, se observa en la imagen la generación de la clave secreta `clave.key`. Este paso es crítico para asegurar que el sistema criptográfico cuente con los recursos y la llave única necesaria para el cifrado 


##### Cifrado en el Cliente 

Una vez preparado el entrono, la siguiete  imagen muestra que el script carga la clave secreta y procesa el mensaje, cifrado el payload antes de preparar el paquete JSON para su envio 
<img width="1600" height="221" alt="image" src="https://github.com/user-attachments/assets/4c5004e2-a5c8-4029-ac65-080aa02e9447" />


##### Transmisión y Recepción 
Como ultimo paso, en la imagen se muestra la recepción del paquete en el servidor. El campo `payload ` presenta una cadena de caracteres ilegibles confirmando que el cifrado se mantiene correctamente durante el tránsito en la red, protegiendo asi la confidencialidad de la información. 
<img width="1600" height="444" alt="image" src="https://github.com/user-attachments/assets/057ad878-8671-4258-9241-2f5b41804ee4" />



