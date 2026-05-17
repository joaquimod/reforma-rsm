# Especificacions tècniques de comunicacions i domòtica per al Projecte Executiu

**Projecte:** Reforma Casa RSM de Vilanova i la Geltrú
**Data:** 12 de maig de 2026    
**Objectiu:** Definició de la infraestructura passiva, xarxa de dades i requeriments elèctrics per a la domòtica integrada.

---

## 1. Infraestructura general i vertical tècnica

Tota la xarxa i el control domòtic es centralitzaran en un únic punt per garantir el manteniment i fiabilitat del sistema.

### 1.1 Ubicació del rack central
- **Espai reservat:** Sala d'instal·lacions (PB).
- **Equipament:** Armari rack de 19" (dimensions mínimes 60x60x60 cm).
- **Alimentació:** 6 preses de corrent en circuit independent protegit.
- **Ventilació:** Cal garantir la circulació d'aire a la sala tècnica per evitar el sobreescalfament dels equips actius (servidor, switch PoE i SAI).

### 1.2 Escomeses i canalitzacions exteriors
- **Punt d'entrada de serveis (PES):** Ubicat a la façana principal segons normativa de Vilanova i la Geltrú.
- **Escomesa de fibra:** Tub de Ø40mm des del PES fins al rack central, amb un traçat que passi pel porxo, sostre del garatge o del vestíbol i distribuïdor de la PB. Els tubs de Ø40mm han de tenir un radi de curvatura superior a 10 cm per permetre el pas de la fibra sense danys.
- **Arqueta de registre interna:** Preveure una arqueta de dimensions mínimes 30x30 cm a la Planta Baixa (Garatge o entrada) per facilitar el registre i distribució cap al rack i plantes superiors.
- **Escomesa TV/Sat:** Tub de Ø25mm des de la planta coberta (PC) fins al rack per a futura instal·lació d'antena.
- **Redundància de dades:** Tub de Ø25mm des de la planta coberta (PC) fins al rack per a possible antena 5G o Starlink.

### 1.3 Dorsal vertical
- **Canalització principal:** Tub de Ø40mm que comuniqui directament el rack central (PB) amb totes les plantes (P1, P2 i PSC).
- **Interconnexió de quadres:** Preveure comunicació mitjançant tub de Ø25mm entre el rack i els subquadres elèctrics de cada planta.

---

## 2. Requeriments elèctrics per a la domòtica

L'estratègia es basa en el control híbrid (físic i digital) mitjançant micromòduls ocults darrere dels mecanismes convencionals.

### 2.1 Cablejat i connexió
- **Fil neutre obligatori:** Cal portar el fil neutre a tots els punts d'encès (interruptors, commutadors, polsadors) i a totes les preses de corrent de l'obra. Sense excepció.
- **Caixes de mecanismes:** Totes les caixes d'encastament han de ser de **60mm de profunditat mínima** per permetre l'allotjament dels micromòduls de control Zigbee.

### 2.2 Previsió per a il·luminació ambiental i serveis
- **Endolls de servei:** Instal·lació de preses de corrent a les zones previstes per a mobiliari integrat (llibreries, estanteries, capçals de llit) per permetre la instal·lació posterior de tires LED gestionades domòticament.
- **Quadres elèctrics:** Preveure una reserva del 20% d'espai lliure en rail DIN i un tub de dades amb presa RJ45 a cada quadre per a la monitorització de consums.

---

## 3. Xarxa de dades i distribució de senyal

La casa disposarà d'una xarxa local cablejada per minimitzar la càrrega del Wi-Fi.

### 3.1 Punts de xarxa RJ45 (Categoria 6a/7)
- **Sala d'estar:** 4 preses (TV, Consola, Media Player, Reserva).
- **Cuina-menjador:** 2 preses (Zona de treball/Aparador).
- **Dormitoris:** 2 preses per habitació (zona llit i zona TV).
- **Distribuidor P2 (Zona Treball):** 2 preses dobles a sobre l'escriptori.
- **Sala polivalent / Estudi (PB):** 4 preses RJ45 per a ús intensiu de dades.
- **Quadre General (QGCP):** 1 presa RJ45 per a la monitorització d'energia (Smart Meter).
- **Unitats tècniques:** Punts de xarxa per a l'inversor solar, carregador de vehicle elèctric, aerotèrmia i VMC.

### 3.2 Cobertura Wi-Fi i pantalles de control
- **Punts d'accés (AP):** Preveure caixa de mecanisme a sostre o paret amb tub de Ø25mm directe al rack al distribuïdor P1, passadís P2 i terrassa exterior. Alimentació via PoE.
- **Dashboards de control:** Caixa de mecanisme a 1,45m d'alçada en un punt central de cada planta (PB, P1, P2) amb tub de Ø25mm directe al rack per a pantalles tàctils amb alimentació PoE.

### 3.3 Televisió i telefonia
- **Televisió:** Només s'instal·larà presa de TV coaxial a la sala d'estar i a la cuina-menjador. La resta de la casa utilitzarà distribució IP.
- **Telefonia:** Es prescindeix de la telefonia fixa. No cal instal·lar cap presa RJ11. L'ascensor utilitzarà un telèfon d'emergència IP (RJ45).

---

## 4. Seguretat i sensors integrats

El sistema substitueix les alarmes convencionals per una solució integrada immune a inhibidors.

### 4.1 Videovigilància (CCTV PoE)
- **Punts de càmera:** Tub de Ø25mm i presa RJ45 Cat6a des del rack fins a:
    - Vestíbol d'entrada i garatge (PB).
    - Sala d'estar (P1).
    - Ubicacions perimetrals exteriors a totes les plantes.

### 4.2 Sensors de fusteria i seguretat tècnica
- **Contactes de fusteria:** Tub de Ø16/20mm des del marc de cada porta i finestra exterior fins a la caixa de registre més propera. S'instal·laran sensors magnètics (reed switches) encastats i cablejats.
- **Control d'accés:** Tub de Ø20mm des del rack fins al marc de la porta principal per a pany intel·ligent.
- **Motor porta garatge:** Tub de Ø25mm des del rack fins al motor de la porta del garatge per al control d'obertura remot.
- **Sirena d'alarma:** Tub de Ø20mm des del rack fins a un punt elevat de la façana per a la instal·lació de la sirena acústica.
- **Alarmes tècniques:** Preveure sensors de fuita d'aigua en zones humides amb electrovàlvula de tall automàtic a l'entrada general.

### 4.3 Protecció contra incendis
- **Protocol d'emergència:** En cas de detecció de fum, el sistema domòtic ha d'executar l'aturada de la VMC, l'obertura total de les persianes motoritzades i l'encesa de l'enllumenat de pànic al 100%.

---

## 5. Integració de sistemes i monitorització

### 5.1 Gestió de recursos i energia
- **Inversor fotovoltaic:** Cal garantir la connexió de dades (RJ45 Cat6a) de l'inversor al rack central per al monitoratge en temps real de la producció i consum via Modbus TCP o API local. El sistema ha de permetre la gestió d'excedents ("Solar Dump") per a la càrrega del vehicle elèctric o producció d'ACS.
- **Vehicle elèctric (V2H):** El carregador ha de ser obligatòriament compatible amb la tecnologia bidireccional **V2H (Vehicle-to-Home)** per permetre l'ús de la bateria del vehicle com a suport energètic de l'habitatge. Requereix connexió de dades mitjançant tub de Ø25mm i cable Cat6a fins al rack central.
- **Aigües pluvials:** Tub de Ø25mm des del rack fins al dipòsit de 10.000L per a sensor de nivell.
- **Reg automatitzat:** Tub de Ø25mm des del rack fins a l'arqueta de reg al pati.
- **Comptadors:** Tub de Ø25mm des del rack fins a l'escomesa d'aigua general per a lectura de consum mitjançant protocol d'impulsos o digital.
- **Climatització:** Connexió Ethernet a l'aerotèrmia i VMC per a control de dades i rendiment.

### 5.2 Estació meteorològica
- **Ubicació:** Terrassa de la P2 (punt elevat).
- **Infraestructura:** Tub de Ø25mm directe al rack per a la gestió de persianes segons radiació solar i vent.

---

## 6. Divisió de responsabilitats

### 6.1 Responsabilitat de l'arquitecte i instal·ladors (Fase d'obra)
- Execució de tota l'obra civil (tubs, canalitzacions, arquetes).
- Instal·lació elèctrica amb fil neutre i caixes de 60mm.
- Cablejat estructural (RJ45 i coaxial) i certificació de punts.
- Instal·lació física dels sensors magnètics a la fusteria.
- Instal·lació física dels mòduls domòtics (subministrats pel propietari) darrere dels mecanismes.

### 6.2 Responsabilitat del propietari (Fase DIY)
- Subministrament de tot el maquinari actiu (rack, servidor, switch, APs, mòduls).
- Configuració del software (Home Assistant), VLANs i seguretat.
- Programació d'escenes i automatitzacions.

