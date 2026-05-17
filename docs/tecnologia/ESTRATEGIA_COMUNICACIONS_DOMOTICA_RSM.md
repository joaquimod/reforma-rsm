# Document definició de Comunicacions i Domòtica - Casa RSM

Aquest document defineix l'estratègia integral de connectivitat, infraestructura de dades i sistemes d'automatització DIY per a la reforma de la Casa RSM. L'objectiu és garantir una casa tecnològicament robusta, escalable i fàcil de mantenir.

## 1. Escomesa i connexió externa

L'entrada de serveis de telecomunicacions s'ha de dissenyar per ser invisible, segura i redundant.

### 1.1 Punt d'Entrada de Serveis (PES)
- **Ubicació:** Façana principal o límit de la parcel·la (segons normativa municipal de VNG).
- **Infraestructura:** Dos tubs corrugats de Ø40mm (un de servei i un de reserva) des de l'exterior fins a l'arqueta de registre interna.
- **Arqueta de registre:** Ubicada a la Planta Baixa (Garatge o entrada), de dimensions mínimes 30x30 cm, per facilitar el pas de cables cap a les plantes superiors.

### 1.2 Canalització cap al Rack (Traçat PB)
- **Recorregut especificat:** L'entrada de fibra seguirà el següent traçat dins de la Planta Baixa:
    1. Entrada des de la vorera cap al **Porxo (Po)**.
    2. Transició pel sostre o lateral del **Garatge (G)**.
    3. Pas pel **Distribuidor (D)** fins a l'entrada directa a la **Sala d'Instal·lacions (Ins)**.
- **Diàmetre:** Tub de Ø40mm sense corbes agudes (radi > 10 cm).
- **Independència:** Aquesta canalització no compartirà espai amb cables de potència elèctrica per evitar soroll electromagnètic.

### 1.3 Redundància de xarxa i Televisió (TDT/Sat)
- **Backup 4G/5G:** Preveure una ubicació per a una antena externa a la planta coberta (PC).
- **Televisió (TDT):** Preveure una canalització de Ø25mm des de la coberta fins a la Sala d'Instal·lacions (PB). No s'instal·larà l'antena física en fase d'obra, però es deixarà el tub preparat.
- **Canalització de backup:** Tub de Ø25mm des de la coberta fins a la Sala d'Instal·lacions (PB).
- **Objectiu:** Garantir la connectivitat del sistema domòtic i la possible recepció de TV tradicional en el futur.

---

## 2. Xarxa de dades local (LAN) i cablejat estructural

La Casa RSM ha de disposar d'una xarxa cablejada d'alt rendiment que alliberi el Wi-Fi de càrrega innecessària.

### 2.1 El Rack Central (PB)
- **Ubicació:** Planta Baixa, a la **Sala d'Instal·lacions (Ins)** de 4,58 m².
- **Especificacions de l'armari:** 
    - Rack de 19" (recomanat ja que tenim espai a la sala tècnica).
    - Mínim 12U d'alçada per encabir: Patch panel, Switch PoE, Router, SAI, Servidors i NVR de càmeres.
- **Alimentació:** 4-6 preses de corrent dedicades, connectades a un circuit protegit del quadre elèctric de la PB.

### 2.2 Cablejat estructural
- **Categoria:** Tota la instal·lació es realitzarà amb cable **Cat6a o Cat7** (S/FTP) per garantir velocitats de 10Gbps i protecció contra interferències.
- **Topologia:** Estel·lar (tots els punts van directes al Rack).
- **Punts clau de connexió RJ45:**
    - **Sala d'estar:** 4 preses (TV, Consola, Media Player, Reserva).
    - **Cuina-Menjador:** 2 preses (Aparador/Zona treball, Nevera/Forn).
    - **Dormitoris:** 2 preses per habitació (zona llit i TV).
    - **Distribuidor P2 (Zona Treball):** 2 preses RJ45 dobles a sobre de l'escriptori corregut.
    - **Sala Polivalent / Estudi (PB):** 4 preses RJ45 (zona de treball intensiva i multimèdia).
    - **Quadre Elèctric (Totes les plantes):** 1 presa per a monitorització d'energia.

---

## 3. Sistema Wi-Fi i cobertura inhàmbrica

L'objectiu és tenir una cobertura del 100% en totes les plantes i terrasses amb *roaming* transparent (sense canvis de xarxa manuals).

### 3.1 Punts d'Accés (AP) professionals
- **Tecnologia:** Punts d'accés alimentats per PoE (Power over Ethernet) per eliminar cables d'alimentació vistos.
- **Ubicacions obligatòries:**
    - **Planta 1:** Un AP central al sostre del distribuïdor.
    - **Planta 2:** Un AP central al sostre del passadís (cobertura P2 i PSC).
    - **Terrassa 1:** Un punt de xarxa per a un AP d'exterior (IP67).
- **Gestió:** Controlador centralitzat (software o hardware tipus UniFi Cloud Key) per a la gestió de potències i canals.

### 3.2 Segregació de xarxes (VLANs)
- **Xarxa Corporativa:** Accés total (mòbils, portàtils, NAS).
- **Xarxa IoT:** Exclusiva per a dispositius domòtics Wi-Fi. Aïllada per Firewall perquè els dispositius barats no puguin espiar la xarxa principal.
- **Xarxa Guest:** Accés a Internet limitat i temporal per a convidats.

---

## 4. Cervell domòtic (El servidor central)

La intel·ligència de la Casa RSM es centralitza en un servidor local per garantir la privacitat i el funcionament sense Internet.

### 4.1 Maquinari de control
- **Servidor Principal:** Raspberry Pi 4 (8GB RAM).
- **Emmagatzematge:** Disc SSD de 256GB connectat via USB 3.0 (Arrencada directa des de SSD).
- **Comunicació Zigbee:** Sonoff Zigbee 3.0 USB Dongle Plus.
- **Alimentació:** Alimentador oficial a 230V (connectat al SAI del Rack).
- **Sistema Operatiu:** Home Assistant OS (HAOS).

### 4.2 Seguretat i resiliència
- **SAI (UPS):** El servidor domòtic ha d'estar connectat a un SAI que permeti un apagament controlat en cas de tall elèctric llarg.
- **Backups:** Còpia diària incremental i xifrada enviada a un servidor extern i a un repositori local (NAS).
- **Accés Remot:** Implementació de VPN (WireGuard) per a l'accés des de l'exterior sense obertura de ports vulnerables.

---

## 5. Protocols de comunicació domòtica

L'estratègia de Casa RSM es basa en protocols oberts, locals i sense dependència del núvol (Cloud-free).

### 5.1 Zigbee 3.0 (La xarxa de malla)
- **Funció:** Protocol principal per a sensors (temperatura, humitat, presència) i actuadors.
- **Exclusió de Bluetooth:** Es descarta l'ús de dispositius Bluetooth (BLE) per a sensors i funcions crítiques a causa del seu abast limitat i la manca d'estructures mesh estables en un habitatge de 4 plantes.
- **Topologia:** Xarxa de malla (Mesh) on cada dispositiu alimentat a 230V actua com a repetidor (Router).
- **Gestió:** Controlat via **Zigbee2MQTT** per a una compatibilitat total amb milers de dispositius (Aqara, Sonoff, IKEA, etc.).

### 5.2 ESPHome (Control a mida)
- **Funció:** Per a projectes personalitzats i sensors complexos (Qualitat de l'aire, control de dipòsits, pantalles d'estat).
- **Comunicació:** Wi-Fi local amb integració nativa d'alt rendiment a Home Assistant.

### 5.3 Bluetooth Proxy
- **Funció:** Utilitzarem els APs o microcontroladors distribuïts per fer de "repetidors Bluetooth" per a sensors de proximitat, raspalls de dents intel·ligents o termòmetres Bluetooth.

---

## 6. Subsistemes de control

### 6.1 Il·luminació i Persianes
- **Filosofia:** Control híbrid. La casa ha de ser funcional amb els interruptors físics convencionals encara que el sistema domòtic estigui apagat.
- **Hardware:** Mòduls ocults (Shelly/Aqara) darrere dels mecanismes.
- **Automatització solar:** Les persianes actuaran com a sistema de protecció tèrmica passiva, baixant automàticament quan la radiació solar a la façana sigui excessiva.
- **Accés al Garatge:** Integració del motor de la porta del garatge a Home Assistant per permetre l'obertura remota i automatitzacions per proximitat (geofencing).

### 6.2 Climatització i VMC (Estratègia Passivhaus)
- **Integració VMC:** Control de cabals basat en sensors de CO2 situats als dormitoris i sala d'estar.
- **Clima:** Control centralitzat de les unitats interiors via passarel·la de dades o controladors WiFi locals.

### 6.3 Gestió Energètica i de Recursos (ESG)
- **Fotovoltaica:** Lectura directa de l'inversor via Modbus TCP.
- **Sistema V2H (Bidireccional):** Integració del vehicle elèctric com a bateria de l'habitatge. Requereix Smart Meter al QGCP i connexió Ethernet Cat6a al carregador.
- **Monitorització Clima:** Lectura de dades de l'Aerotèrmia i VMC via Ethernet/Modbus per al càlcul del COP real i la qualitat de l'aire.
- **Mesura de consums:** Monitorització individual de circuits crítics i de l'escomesa d'aigua general.
- **Optimització d'excedents:** Lògica de "Solar Dump" per aprofitar els moments de màxima producció per a tasques d'alta demanda (carrega de cotxe o aigua calenta).
- **Gestió d'Aigües Pluvials:** Monitorització del nivell del dipòsit de 10.000L mitjançant sensor ultrasònic integrat per ESPHome (DIY).
- **Reg Automatitzat (Pati):** Sistema de reg gota a gota intel·ligent per al pati mediterrani. Lògica basada en l'evapotranspiració local (estació meteo) i disponibilitat d'aigua de pluja. Control mitjançant electrovàlvules de 24V gestionades per Home Assistant.

### 6.4 Seguretat i CCTV
- **Videovigilància:** Càmeres IP amb alimentació PoE a exteriors i punts clau interiors (Vestíbol, Garatge, Sala d'Estar). Gravació 24/7 en disc local (NVR o NAS) protegit dins del Rack, eliminant qualsevol enviament de vídeo al núvol (Cloud-free).
- **Alarma Local (Anti-inhibició):** El sistema substitueix les alarmes propietàries (tipus Verisure) mitjançant una xarxa de sensors cablejats i càmeres PoE, immune a inhibidors de freqüència.
- **Detecció d'Incendis:** Detectors de fum Zigbee interconnectats a cada planta.
- **Protocol d'Emergència d'Incendis:** En cas de detecció de fum, el sistema executarà:
    1. Aturada immediata de la VMC (tall d'oxigen).
    2. Obertura total de totes les persianes motoritzades (evacuació).
    3. Enllumenat de pànic (llums al 100% per a visibilitat en el fum).
    4. Notificació crítica als telèfons de la família.
- **Control d'Accés:** Pany intel·ligent a la porta principal (PB) i garatge, integrat amb el sistema d'identificació de Home Assistant.
- **Sensors d'Obertura Integrats:** Instal·lació de contactes magnètics (Reed switches) **encastats i cablejats** en tots els marcs de les portes i finestres exteriors. Invisibilitat total i màxima fiabilitat sense bateries.
- **Alarmes Tècniques:** Sensors de fuita d'aigua en zones crítiques (Cuina, Banys, Bugaderia) amb electrovàlvula de tall automàtic de l'entrada d'aigua general.
- **Sirena d'Alarma:** Sirena Zigbee/Cablejada per a dissuasió acústica en cas d'intrusió o emergència tècnica.

### 6.5 Estació Meteorològica DIY
- **Funció:** Estació meteorològica a la terrassa de la P2 (anemòmetre, pluviòmetre, radiació solar).
- **Integració:** Connexió via cable (RJ45) o Wi-Fi dedicada al Rack Central per a la gestió intel·ligent de persianes i clima Passivhaus.

---

## 7. Requeriments d'instal·lació física (Per al PE)

Aquests punts són d'obligat compliment per a l'arquitecte i els instal·ladors durant la fase d'obra.

### 7.1 Canalitzacions i Tubs
- **Vertical Tècnica (Dorsal):** Tub de Ø40mm que comuniqui el Rack Central (PB) amb tots els subquadres elèctrics (P1, P2) i la PSC.
- **Punts de Wi-Fi (PoE):** Caixa de sostre amb tub de Ø25mm directe al Rack.
- **Pantalles de Control:** Punts a 1,45m d'alçada a cada planta (PB, P1, P2) amb tub de Ø25mm al Rack per a dashboards PoE.
- **CCTV (PoE):** Tubs de Ø25mm des del Rack fins a les ubicacions de càmeres exteriors a totes les plantes (PB, P1, P2).
- **Ascensor:** Tub de Ø25mm i presa RJ45 Cat6a a la sala de màquines per a comunicació d'emergència i monitorització d'estat.
- **Infraestructura TV:** Un tub coaxial des del Rack fins a la presa de TV de la **Sala d'Estar** i de la **Cuina-Menjador**. No se preveu coaxial als dormitoris (distribució via IPTV/RJ45).
- **Telefonia:** S'elimina totalment la previsió de telefonia fixa (RJ11). Totes les comunicacions de veu seran via xarxa de dades (IP/WiFi).
- **Sensors de Fusteria:** Tub de Ø16/20mm des de cada marc de finestra/porta exterior fins a la caixa de registre més propera per a la interconnexió del cablejad de seguretat.
- **Aigües Pluvials:** Tub de Ø25mm des del Rack fins al dipòsit d'aigües pluvials (pati).
- **Estació Meteorològica:** Tub de Ø25mm des del Rack fins a la terrassa de la P2 (punt elevat).
- **Escomesa de Fibra:** Tub de Ø40mm des del PES fins al Rack.

### 7.2 Electricitat i Mecanismes
- **Fil Neutre Obligatori:** Cal portar el fil neutre (blau) a **totes i cadascuna** de les caixes de mecanismes (interruptors, commutadors i endolls). Sense excepció.
- **Caixes de gran profunditat:** Instal·lació de caixes de mecanismes de **mínim 60mm de fons** a tota l'obra. Això és crític per allotjar mòduls Zigbee/Wi-Fi (Shelly/Sonoff) que controlaran tant els llums de sostre com els encastats.
- **Endolls de servei per a mobiliari:** Preveure endolls a les zones previstes per a llibreries, estanteries i capçals de llit per permetre la instal·lació futura de tires LED i il·luminació ambiental gestionada per controladors Zigbee locals.
- **Quadres Elèctrics:** Reserva del 20% d'espai lliure en rail DIN. Tub de dades RJ45 dins de cada quadre.

### 7.3 Espai per al Rack Central (PB)
- **Ubicació:** Sala d'Instal·lacions (PB).
- **Dimensions de reserva:** Espai per a armari Rack de 19" (60x60x60 cm aprox).
- **Ventilació:** Aprofitar la ventilació de la sala tècnica per evitar sobreescalfament del servidor i switch PoE.
- **Alimentació:** 6 preses de corrent dedicades en circuit protegit.

---

## 8. Divisió de responsabilitats: PE vs DIY

Per optimitzar costos i garantir la flexibilitat del sistema, el projecte es divideix en dues capes de responsabilitat:

### 8.1 Responsabilitat de l'arquitecte i constructora (Fase d'obra)
Es tracta de la infraestructura passiva i elèctrica bàsica que no es pot canviar un cop tancades les parets:
- **Obra civil:** Tubs, canalitzacions, rases i arquetes.
- **Electricitat:** Fil neutre en tot l'habitatge i caixes de 60mm de fons.
- **Instal·lació de mòduls domòtics:** L'electricista de l'obra realitzarà el cablejat i la instal·lació física dels mòduls Zigbee/Wi-Fi (subministrats pel propietari) darrere dels mecanismes.
- **Telecomunicacions:** Cablejat Cat6a/7 i instal·lació de preses RJ45 i mecanismes convencionals.
- **Pre-instal·lació de seguretat:** Sensors magnètics encastats a les portes i finestres (només hardware i cablejat fins a caixa).

### 8.2 Responsabilitat del propietari (Fase d'implementació DIY)
Es tracta de la capa activa i la intel·ligència del sistema:
- **Subministrament de hardware:** Compra dels mòduls domòtics, Raspberry Pi, SSD, SAI, Switch PoE i APs.
- **Software:** Instal·lació de Home Assistant, configuració de xarxes VLAN i seguretat remota.
- **Configuració domòtica:** Emparellament (pairing) dels mòduls ja instal·lats per l'electricista i creació d'automatitzacions.

---
*Darrera actualització: 12 de maig de 2026 - Document de Disseny*
