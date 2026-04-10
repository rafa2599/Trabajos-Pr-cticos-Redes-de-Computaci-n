# Redes de Computadoras - Trabajo Práctico N°2

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

## Parte 1: Armado y verificación de cables Cat5/Cat5e bajo estándar T568B

### 1. Investigación: Pasos para armar un cable T568B

Para construir un cable de red bajo la norma T568B, se siguieron los siguientes pasos:

1. Pelar la cubierta exterior del cable aproximadamente 2-3 cm desde el extremo, con cuidado de no dañar los pares internos.
2. Desenredar los cuatro pares trenzados y ordenar los ocho conductores según el estándar T568B.
3. Alinear y aplanar los conductores en el orden correcto.
4. Cortar los extremos de forma pareja para que todos queden a la misma longitud.
5. Insertar los conductores en el conector RJ-45, verificando que cada uno llegue hasta el fondo del conector y que el orden de colores sea correcto visto desde la parte metálica.
6. Apretar con la pinza hasta escuchar el clic de fijación.
7. Repetir el proceso en el otro extremo con **el mismo orden** (T568B), ya que el cable es de tipo directo.

### 2. Construcción del cable

El grupo construyó un cable de aproximadamente **1 metro** de longitud, usando el estándar **T568B**.

El orden de los conductores utilizado en ambos extremos fue:

| Pin | Color          |
|-----|----------------|
| 1   | Blanco Naranja |
| 2   | Naranja        |
| 3   | Blanco Verde   |
| 4   | Azul           |
| 5   | Blanco Azul    |
| 6   | Verde          |
| 7   | Blanco Marrón  |
| 8   | Marrón         |

Durante la construcción se presentó una dificultad inicial: los conductores no entraban correctamente en la ficha RJ-45 en los primeros intentos, por lo que fue necesario repetir el proceso de armado varias veces hasta lograr un resultado correcto.

### 3. Verificación del cable

El cable construido fue entregado al grupo **CDT** para su verificación. A su vez, nuestro grupo verificó el cable del grupo **CDT**.

#### a) Inspección visual — cable del grupo CDT

El cable del grupo CDT presentó buena calidad constructiva: los conductores estaban correctamente ordenados y visibles a través del conector, la cubierta exterior llegaba hasta dentro del conector proveyendo alivio de tensión, y los extremos estaban cortados de forma pareja. No se detectaron defectos visuales significativos.

#### b) Verificación eléctrica — resultado del tester ethernet

Ambos cables fueron verificados con el tester para cables ethernet. En los dos casos los 8 pines presentaron continuidad correcta en orden directo (1-1, 2-2, 3-3, 4-4, 5-5, 6-6, 7-7, 8-8), sin inversiones ni cortocircuitos.

| Pin | Resultado |
|-----|-----------|
| 1   | ✓         |
| 2   | ✓         |
| 3   | ✓         |
| 4   | ✓         |
| 5   | ✓         |
| 6   | ✓         |
| 7   | ✓         |
| 8   | ✓         |

![image](https://hackmd.io/_uploads/HkB12O3obl.png)
![image](https://hackmd.io/_uploads/S1Vfn_noWe.png)

### 4. Documentación del intercambio

| Acción                           | Grupo |
|----------------------------------|-------|
| Verificamos el cable de          | CDT   |
| Nuestro cable fue verificado por | CDT   |

---

## Parte 2: Equipamiento físico, verificación y utilización de equipos de red

### 1. Características principales del Switch Cisco Catalyst 2950 Series

El switch utilizado en el laboratorio pertenece a la familia **Cisco Catalyst 2950 Series** (modelo WS-C2950-24). A continuación se resumen sus características principales según el datasheet oficial:

**Puertos y conectividad**

- 24 puertos Fast Ethernet con conectores RJ-45
- Puerto de consola RJ-45 para administración fuera de banda con adaptador RJ-45 a DB-9 para conexión a PC
- Soporte de VLANs y troncales entre switches

**Rendimiento**

- Fabric de switching: 8.8 Gbps
- Ancho de banda máximo de reenvío: 4.8 Gbps
- Tasa de reenvío wire-speed: 3.6 Mpps (paquetes de 64 bytes)
- Tabla de direcciones MAC: hasta 8000 entradas
- 8 MB de memoria de buffer compartida entre todos los puertos
- 16 MB de DRAM y 8 MB de Flash

**Software y administración**

- Cisco IOS Standard Image (SI)
- Administración por CLI vía consola serie (9600 baudios), Telnet y SNMP
- Soporte de SSHv2 para administración cifrada
- Cisco Device Manager (interfaz web embebida)
- SNMPv1, v2 y v3

**Estándares soportados**

- IEEE 802.1D (STP), 802.1w (RSTP), 802.1s (MSTP)
- IEEE 802.1Q (VLANs), 802.1p (QoS/CoS)
- IEEE 802.1x (autenticación por puerto)
- IEEE 802.3 (10BASE-T), 802.3u (100BASE-TX), 802.3ad (LACP/EtherChannel)

**Características físicas**

- Factor de forma: 1 RU
- Dimensiones: 4.36 × 44.45 × 24.18 cm
- Peso: 3.0 kg
- Consumo máximo: 30 W
- Temperatura de operación: 0 a 45 °C
- MTBF: 398.240 horas
- Garantía limitada de por vida

> Fuente: Cisco Catalyst 2950 Series Switches with Standard Image Software — Data Sheet (2004)

### 2. Checklists de procedimientos

#### a) Conectar una PC al puerto de consola del switch a 9600 baudios con PuTTY (Linux)

1. Conectar el cable serie (RJ-45 a DB-9) entre el puerto **CONSOLE** del switch y el adaptador Serie-USB de la PC.
2. Identificar el puerto serie asignado por el sistema operativo:
   ```bash
   dmesg | grep tty
   ```
   El dispositivo suele aparecer como `/dev/ttyUSB0` o `/dev/ttyS0`.
3. Dar permisos de acceso al puerto si es necesario:
   ```bash
   sudo chmod 666 /dev/ttyUSB0
   ```
4. Abrir PuTTY:
   ```bash
   sudo putty
   ```
5. En la ventana de PuTTY, seleccionar **Connection type: Serial** y configurar:
   - Serial line: `/dev/ttyUSB0` (o el puerto asignado)
   - Speed: `9600`
   - Data bits: `8`
   - Stop bits: `1`
   - Parity: `None`
   - Flow control: `None`
6. Hacer clic en **Open**.
7. Presionar **Enter** en la terminal para activar la consola del switch.

#### b) Acceder a opciones de administración y verificar la configuración

Una vez conectados a la consola, se verificó la configuración del switch con el comando:

```
Switch# show running-config
```

La configuración relevante obtenida fue la siguiente:

```
ip subnet-zero

spanning-tree mode pvst
no spanning-tree optimize bpdu transmission
spanning-tree extend system-id

interface FastEthernet0/7
 switchport access vlan 2
 switchport mode access
 spanning-tree portfast

interface FastEthernet0/8
 switchport access vlan 2
 switchport mode access
 spanning-tree portfast

interface FastEthernet0/10
 switchport access vlan 2
 switchport mode access

interface FastEthernet0/11
 switchport access vlan 2
 switchport mode access

interface FastEthernet0/12
 switchport mode trunk

interface FastEthernet0/15
 switchport access vlan 2
 switchport mode access

interface FastEthernet0/18
 switchport access vlan 2
 switchport mode access

interface Vlan1
 ip address 192.168.1.2 255.255.255.0
 no ip route-cache
 shutdown

interface Vlan2
 ip address 192.168.2.10 255.255.255.0
 no ip route-cache

ip default-gateway 192.168.1.1

monitor session 1 source interface Fa0/7 , Fa0/10
monitor session 1 destination interface Fa0/11
monitor session 2 destination interface Fa0/8
```

El switch ya se encontraba configurado de antemano. La VLAN activa era la **VLAN 2**, con dirección IP de administración `192.168.2.10/24`. La VLAN 1 estaba deshabilitada (`shutdown`). Los puertos asignados a la VLAN 2 y sus IPs de host fueron:

| Puerto  | IP del host conectado |
|---------|-----------------------|
| Fa0/7   | 192.168.2.14          |
| Fa0/8   | 192.168.2.13          |
| Fa0/15  | 192.168.2.12          |
| Fa0/18  | 192.168.2.11          |

Adicionalmente, el puerto Fa0/12 estaba en modo trunk, y se configuraron sesiones SPAN para captura de tráfico entre puertos.

#### c) Conectar computadoras al switch, configurar una red y testear conectividad

Las computadoras de los distintos grupos se conectaron al switch mediante los cables construidos en la Parte 1, utilizando los puertos de la VLAN 2. Se asignaron IPs estáticas dentro de la red `192.168.2.0/24` en cada equipo.

**Configuración de red utilizada:**

| Puerto switch | IP Asignada    | Máscara       |
|---------------|----------------|---------------|
| Fa0/7         | 192.168.2.14   | 255.255.255.0 |
| Fa0/8         | 192.168.2.13   | 255.255.255.0 |
| Fa0/15        | 192.168.2.12   | 255.255.255.0 |
| Fa0/18        | 192.168.2.11   | 255.255.255.0 |
| Switch (VLAN2)| 192.168.2.10   | 255.255.255.0 |

### 3. Verificación de conectividad entre grupos

Los grupos conectados al switch realizaron pruebas de conectividad mediante el comando `ping`. Nuestro grupo ejecutó un ping continuo hacia el host `192.168.2.11`:

```
C:\Users\ignac>ping -t 192.168.2.11

Haciendo ping a 192.168.2.11 con 32 bytes de datos:
Respuesta desde 192.168.2.11: bytes=32 tiempo=1ms TTL=64
Respuesta desde 192.168.2.11: bytes=32 tiempo=7ms TTL=64
Respuesta desde 192.168.2.11: bytes=32 tiempo=1ms TTL=64
Respuesta desde 192.168.2.11: bytes=32 tiempo=1ms TTL=64
Respuesta desde 192.168.2.11: bytes=32 tiempo=6ms TTL=64
Respuesta desde 192.168.2.11: bytes=32 tiempo=2ms TTL=64
...
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Respuesta desde 192.168.2.14: Host de destino inaccesible.
Tiempo de espera agotado para esta solicitud.
...
Respuesta desde 192.168.2.11: bytes=32 tiempo=1ms TTL=64
Respuesta desde 192.168.2.11: bytes=32 tiempo=1ms TTL=64
```

La conectividad fue exitosa en la mayoría de los paquetes, con tiempos de respuesta de entre 1 ms y 7 ms. Se observaron algunos timeouts y un mensaje de "host de destino inaccesible" proveniente de `192.168.2.14` durante un período intermedio. Esto puede atribuirse a una desconexión momentánea de algún cable o a la reconvergencia del protocolo Spanning Tree al conectar o desconectar equipos durante la práctica. La conectividad se restableció automáticamente.

![image](https://hackmd.io/_uploads/HJ_r2unsWx.png)
