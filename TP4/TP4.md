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

![](/TP4/Img/PacketSender.jpeg)
![](/TP4/Img/Terminal.jpeg)