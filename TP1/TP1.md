# Redes de Computadoras - Trabajo Práctico N°1

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


## 1. Identificación de dispositivos y armado de la topología
En el marco del laboratorio, nuestro grupo representó al Router 3, identificado con la dirección MAC  AC:45:70. La función nuestra como router consistía en el reenvío de paquetes entre redes, operando nodo a nodo de interconexión. Según la topología, el Router 3 se encontraba conectado directamente a:
- Router 1 (AA:43:80) y Router 2 (AA:45:92), con quienes intercambió información de ruteo y realizó el proceso de ARP para descubrir sus MACs
- Las redes 10.16.0.0/24, 10.10.0.0/24 y 10.5.0.0/24, que tenía conectadas directamente.

El objetivo general del laboratorio fue simular de manera física el comportamiento de una red IP real en la que  cada participante asumió la identidad de un dispositivo de red y se siguió el proceso completo de envió de paquetes, desde que un host origen construye su frame Ethernet hasta que el paquete llega al host destino.


![Diagrama de topología](./Img/Diagrama-topología.drawio.png)
> Fig 1. Diagrama de topología de red

## 2. Armado de topología
Una vez armada la topología, cada router construyó su tabla de ruteo indicando, para cada red destino, si estaba conectada directamente a una de las interfaces o si se debía reenviar el paquete hacia otro router (next hop).

| Red Destino    | Next Hop          | 
|----------------|-------------------| 
|  10.16.0.0/24  | Conexión directa  |
|  10.10.0.0/24  | Conexión directa  |
|  10.5.0.0/24   | Conexión directa  |
|  10.13.0.0/24  | Router 1          |
|  10.6.0.0/24   | Router 1          |
|  10.12.0.0/24  | Router 1          |
|  10.19.0.0/24  | Router 2          |
|  10.9.0.0/24   | Router 2          |
|  10.11.0.0/24  | Router 2          |

> Tabla de ruteo

## 3 y 4.Conformación de paquetes y simulación de transmiciónes y recepciones
Nuestro grupo al ser Router, no generamos paquetes, nuestra función era reenviar los paquetes que nos llegaban. Por cada paquete recibido se realizaba el siguiente proceso.
1. Se recibía el frame Ethernet entrante, con MAC destino correspondiente a nuestra interfaz (AC:45:70).
2. Se desencapsuló el frame y se examinó el paquete IP anterior.
3. Se decrementó el TTL en 1.
4. Se consultó la tabla de ruteo para determinar el siguiente salto según la IP destino.
5. Se resolvió mediante ARP la MAC del siguiente salto.
6. Se reencapsuló el paquete IP en un nuevo frame Ethernet con la nueva MAC destino y MAC origen AC:45:70, y se reenvió.

## 5. Reflexiones y documentación
a. La IP destino se mantiene constante mientras que la MAC cambia en cada salto debido a que son dos niveles de direccionamiento con propósitos distintos. La IP identifica al destino final de extremo a extremo y no tiene por qué cambiar en ningún momento del recorrido. Por otro lado, la MAC es un direccionamiento físico que solo tiene sentido dentro de un enlace local, es decir, cada vez que el paquete pasa de un router al siguiente, se construye un frame nuevo para ese tramo específico, con las MACs de los dos dispositivos que están en ese enlace.


b. El host busca la MAC del gateway porque ARP solo funciona dentro de la misma red local. Un host no puede enviar un ARP request a una red remota, ese broadcast no cruza routers. Entonces lo que hace es mandarle el paquete a su gateway, que sí está en su misma LAN y cuya MAC puede resolver.


c. El modelo de ruteo hop-by-hop tiene como ventaja que cada router solo necesita conocer su entorno inmediato, no el mapa completo de Internet, haciendo que la red sea escalable: si cambia una ruta en algún lado, solo se actualizan los routers afectados, no todos. A su vez, permite redundancia, ya que si un camino cae, cada router puede redirigir por otro sin que el resto de la red lo sepa.


d. Es necesario reconstruir el frame Ethernet en cada salto ya que tiene alcance local, es decir, que la función es entregar el paquete en un tramo específico entre dos dispositivos directamente conectaods. Una vez que el paquete llega al router destino, ese frame se descarta y el router construye frame Ethernet para el siguiente tramo, con las MACs correspondientes a ese enlace.
Si un router intentara reenviar exactamente el mismo frame, la MAC destino seguiría siendo la suya propia y ningún otro dispositivo la aceptaría o llegaría a un dispositivo equivocado.


e. El campo TTL previene que un paquete quede circulando indefinidamente en la red. Se podría dar el caso en el cuál por error las tablas de ruteo formen un ciclo y el paquete quedaría rebotando para siempre consumiendo ancho de banda. Con ayuda del campo TTL, cada router lo decrementa en 1 y cuando llega a 0 el paquete se descarta y se notifica al origen. Sin este mecanismo, un solo ciclo de ruteo mal configurado podría satura enlaces enteros con paquetes que nunca llegan a destino.


### Parte 2. Inyección y detección de errores 
En esta segunda parte del trabajo práctico estudiamos e implementamos técnicas de Detección y Corrección de Errores (EDAC).El flujo de datos en las redes de computadoras esta sujeto a diversos factores de interferencias que pueden alterar la información original, por ello, es necesario comprender como los dispositivos (finales o intermedios) interactúan con la **payload** (carga útil) de los paquetes 

 #### Definiciones 

 **EDAC(Error Detection and Corretion)* : Es el conjunto de técnicas utilizadas para garantizar la integridad de los datos (garantía de que la información recibida es idéntica a la enviada) durante su transmisión a través de canales no confiables 
 - Detección: permite saber si el mensaje llegó alterado
 - Corrección: permite reconstruir el mensaje original sin pedir el reenvío, esto se logra mediante bits de redundancia 
   
**Gateway*: es un dispositivo que conecta redes con arquitecturas o protocolos diferentes, es el encargado de hacer una "traducción" de protocolos en las capas superiores 

 - Default Gateway: es la dirección del router al que un host envía los paquetes cuando la dirección de destino no esta en su propia red local.
 - Router No Default Gateway: router intermedio que solo encamina paquetes entre subredes internas, sin gestionar la salida directa de los dispositivos finales(host).
   Sin LAN debajo: significa que no tiene computadoras conectadas directamente a sus puertos de usuario. Solo tiene conexiones hacia otros routers 

#### Desarrollo de la actividad

Durante la realización de la actividad, eramos 4 grupos (entre los que nos mandamos los paquetes) y el profesor cumplió el rol de Router no default gateway, quien podía "romper" algun paquete, modificando uno o más bit de la payload

El rol de los grupos era enviar y recibir mensajes e identificar si ese paquete fue modificado o no. La IP de nuestro grupo era `10.0.4.0` y para enviar el paquete usamos como técnica de EDAC como la técnica de Paridad Par o Técnica de Redundancia por XOR (LRC).
A nuestro grupo le tocó implementar la técnica de Paridad Par para el envio del paquete. Para lo que dividimos nuestro payload `a382` en nibbles, quedando como `1010- 0011-1000-0010`, dandonos que nuestro EDAC es 3, siendo 3 el resultado de la suma de paridad de cada nibble. Para completar el envio, pusimos en el mensaje (papel), la IP de nuestro grupo y la de destino, el payload y el EDAC. Armado el mensaje, fue enviado al Router No Default Gateway (profesor).

Luego, otro de los grupos, nos enviaron un paquete, el cual teniamos que verificar que sea legitimo el payload. Para esto, usamos la Técnica de Redundancia por XOR. 
El payload recibido fue `E520` y el `EDAC 1000`, para comprobar que el paquete no haya sido corrompido, lo pasamos a binario, quedando: `1110-0101-0010-0000`. Para aplicar la técnica anteriormente mencionada, agarramos el primer nibble XOR con el segundo nibble, al resultado aplicamos XOR con el tercer nibble y asi sucesivamente.  
##### Resultado de la Técnica de Redundancia por XOR 
payload: 

         E `1110`

         5 `0101`
         
         2 `0010`
         
         0 `0000` 
         
EDAC : 1000 
Tabla XOR 

|Entrada A|Entrada B|Resultado XOR|
|:---:|:---:|:---:| 
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|0| 


**Aplicación de la técnica* : 

|Pasos|Operación | A | B| Rsultado
|:---:|:---:|:---:|:---:|:---:|   
|1|nibble 1 XOR nibble 2|1110|0101|1011|
|2|resultado XOR nibble3|1011|010| 1001|
|3|resultado XOR nibble 4|1001|0000 |**1001**|


**Análisis del resultado* 
|EDAC|Resultado de la técnica|Conclusión|
|:---:|:---:|:---:|
|1000|1001| Paquete corrompido (alteración en la carga útil)|

Al comparar el EDAC recibido con el resultado de la técnica calculada, pudimos observar que los valores no coinciden por lo que podemos concluir que la payload fue alterada durante su pasaje por el Router, perdiendo su integridad original. 

Como conclusión llegamos a que el desarrollo de este laboratorio nos permitió comprobar la importancia de los mecanismos de integridad de datos en una red. Mediante la implementación de técnicas de EDAC(Paridad Par y XOR), logrando validar que el canal de transmisión no es 100% confiable. Sin estas herramientas, las modificaciones en los bits pasarian inadvertidas, comprometiendo la validez de la información final 


