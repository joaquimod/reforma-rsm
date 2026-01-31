# Guia de Preinstal·lació Domòtica i Audiovisual | Casa RSM

Aquest document detalla els requisits tècnics de preinstal·lació (tubs, preses i xarxa) necessaris per implementar el sistema de **Laser TV** i la domòtica **DIY (Home Assistant)** durant la fase de reforma.

---

## 1. Zona Sala d'Estar (Laser TV & Mural Digital)

El punt crític és el moble baix de roure on s'ubicarà el projector UST (Ultra Short Throw).

### Preses de Corrent i Dades (Darrere el moble):
*   **Corrent:** Mínim 4 preses de corrent (Projector, Receptor AV/Barra so, Hub domòtic, Router/Switch).
*   **Dades:** 2 preses RJ45 (Categoria 6 o superior). Una per al projector i una per al hub de Home Assistant. *Evitar dependre del WiFi per a streaming 4K.*
*   **HDMI:** Si es preveu un sistema de so extern o reproductor en un prestatge separat, preinstal·lar un tub de 40mm per a cable HDMI 2.1.

### Il·luminació (Fussa de sostre):
*   **Punt de corrent al sostre:** Dins de la fussa perimetral per a la font d'alimentació de les tires LED RGBW.
*   **Espai per a controlador:** Preveure espai discret per a controladors Zigbee/WiFi (ex: Shelly RGBW2) per gestionar les escenes d'atmosfera.

---

## 2. Zona Oficina / Estudi (Hub Tecnològic)

### Estacions de Treball:
*   **Digital/Art/DIY:** Cada taula ha de disposar de 4-6 preses de corrent.
*   **Xarxa:** Mínim 2 preses RJ45 a la zona del Mac Studio.
*   **Canalització:** Tubs corrugats de 32mm entre taules per a una gestió de cables neta (Under-desk cable management).

### Preinstal·lació per a Futur Dormitori:
Per permetre la reconversió en habitacle per a cuidador/a, preveure professionalment:
*   **Punt de TV:** Preinstal·lar tub per a antena i presa de corrent a la paret de les prestatgeries (enrasat).
*   **Capçal de Llit:** Preveure preses de corrent i commutats a 60cm d'alçada en la paret on s'ubicaria el llit, actualment coincident amb la zona artística.
*   **Armari:** Deixar punts de llum al sostre preparats per a la il·luminació interior d'un futur armari rober.

---

## 3. Zona Sotacoberta (Refugi Passivhaus)

La sotacoberta requereix una planificació específica per mantenir l'estanquitat a l'aire i garantir el confort tèrmic i lumínic.

### Il·luminació i Alimentació:
*   **Perfils LED Perimetrals:** Preveure canalització per a tira LED en tot el perímetre de la trobada entre sostre inclinada i paret.
*   **Caixes de Registre:** Ubicar drivers i controladors en una zona accessible però integrada (ex: darrere el mobiliari de roure baix).
*   **Control Circadiari:** Grups de llum amb control **Dual White (CCT)** per canviar de llum blanca estimulant (matí) a llum càlida (relaxació nocturna).

### Climatització i Eficiència:
*   **Ventilació Mecànica:** Preveure pas de tubs per al sistema de renovació d'aire VMC (Ventilació Mecànica Controlada) necessari en un espai estanc EnerPHit.
*   **Sensors:** Instal·lació de sensor de qualitat d'aire (CO2, Humitat, VOC) per automatitzar la renovació d'aire.

---

## 4. Infraestructura General Domòtica (DIY)

### Quadre Elèctric:
*   **Espai reserva:** Deixar espai per a un mesurador de consum per carril DIN (ex: Shelly EM) per monitoritzar l'eficiència EnerPHit.
*   **Protecció:** Diferencial específic per a la línia electrònica/informàtica.

### Persianes i Mallorquines:
*   **Motorització:** Portar alimentació (3 fils) a cada caixa de persiana/mallorquina.
*   **Control:** Tubs amples cap als interruptors de paret per permetre la instal·lació de micromòduls domòtics (ex: Shelly 2.5 o Sonoff Dual).

### Sensors (Zigbee/Thread):
*   **Ubicació:** No requereixen tubs (funcionen a bateria), però cal preveure una bona cobertura WiFi/Zigbee situant el Hub en una posició central.

---

## 4. Configuració Hub Home Assistant (DIY)

Per garantir la sobirania de dades i el control local total sense dependre del núvol, es recomana la següent configuració:

### Hardware Recomanat:
*   **Servidor:** Home Assistant Green o una Raspberry Pi 5 (8GB) amb disc SSD (evitar targetes SD per fiabilitat).
*   **Connexió:** Ubicar prop del router a la **Sala d'Estar** o l'**Estudi**, connectat sempre per cable Ethernet (RJ45).
*   **Ràdio Multiprotocol:** Adaptador USB (ex: *Home Assistant SkyConnect*) per donar suport nadiu a **Zigbee**, **Thread** i **Matter**.

### Estratègia de Protocols:
1.  **WiFi (Local):** Per a actuadors potents i mesura de consum (Shelly). Requereix un router robust que suporti >30 dispositius.
2.  **Zigbee 3.0:** Per a tota la resta (sensors de porta, temperatura, presència i il·luminació). Crea una xarxa de malla (*mesh*) altament fiable.
3.  **BT Proxy:** Utilitzar dispositius Shelly Plus com a proxies Bluetooth per estendre la cobertura de sensors Bluetooth (ex: SwitchBot o monitors de plantes).

---

## 5. Control de la Il·luminació LED (Fosses i Prestatges)

L'ADN del projecte depèn de la creació d'atmosferes. La instal·lació dels LEDs no ha de ser "on/off" tradicional.

### Components Tècnics:
*   **Tires LED:** Recomanat **RGBW** (Color + Blanc Calç) o **CCT** (Blanc Dinàmic).
*   **Controladors:** 
    *   **Opció Pro (Zigbee):** Controladors tipus *Gledopto* o *QuinLED* (ESPHome) integrats directament a Home Assistant.
    *   **Opció Estàndard (WiFi):** *Shelly RGBW2*.
*   **Drivers (Fonts d'alimentació):** Han de ser de tensió constant (12V o 24V) i dimensionades un 20% per sobre del consum de la tira.

### Instruccions per a l'Electricista:
1.  **Centralització de Drivers:** Ubicar les fonts d'alimentació en registres ventilats o dins del propi moble/fossa per facilitar el manteniment.
2.  **Cablejat de Baixa Tensió:** Des del controlador fins a la tira, utilitzar cables de secció adequada (min 1.5mm²) per evitar caigudes de tensió en trams llargs.
3.  **Sense Polsacions:** Els polsadors de paret que controlen aquests LEDs han de ser connectats a les **entrades de control** (Inputs) del controlador domòtic, no tallar la corrent del driver. Permetrem així que el llum estigui sempre "viu" per a les automatitzacions.

---

## 4. Requisits per al Projectista / Electricista

1.  **Tubs Corrugats:** Totes les canalitzacions de dades han de ser independents de les d'electricitat per evitar interferències.
2.  **Profunditat de Caixes:** Utilitzar caixes de mecanisme de 50mm de profunditat per facilitar la instal·lació de mòduls domòtics darrere els interruptors originals.
3.  **Xarxa:** El cablejat de dades ha de ser **UTP Cat6** com a mínim, certificat per a 1Gbps.

---
*Document generat per Antigravity per al Projecte de Reforma Casa RSM - Gener 2026*
