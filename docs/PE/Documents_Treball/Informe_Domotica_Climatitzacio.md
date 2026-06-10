# Integració de la climatització a la domòtica (Home Assistant)

Aquest informe tècnic descriu els mètodes de connexió, control i integració de les unitats de climatització (bombes de calor aire-aire i aire-aigua) de la marca Panasonic amb el sistema de domòtica basat en Home Assistant previst per a la Casa RSM. L'objectiu és aconseguir una gestió local de les temperatures, velocitats i modes de funcionament per optimitzar el confort i coordinar-ho amb la generació d'excedents fotovoltaics.

---

## 1. Mètodes d'integració de les unitats de climatització Panasonic

Les unitats previstes (CS-Z35UD3EAW per a conductes i CS-Z35ZKEW per a split de paret) disposen de diferents passarel·les per comunicar-se amb Home Assistant, classificades segons la seva dependència de la xarxa:

### 1.1. Integració oficial per núvol: Panasonic Comfort Cloud

És el mètode natiu que utilitza el Wi-Fi integrat de sèrie a les màquines de climatització domèstiques de Panasonic.

*   **Connexió física:** La màquina es connecta directament al Wi-Fi de l'habitatge i es registra a l'aplicació oficial de Panasonic.
*   **Integració lògica:** Home Assistant es connecta mitjançant el component de la comunitat **Panasonic Comfort Cloud** (instal·lat a través de HACS) usant les credencials del compte de Panasonic del propietari.
*   **Prestacions:** Permet controlar la temperatura de consigna, el mode (calor, fred, deshumidificació, ventilació, auto), la velocitat de ventilació, l'adreça de les reixetes i activar la tecnologia de purificació de l'aire nanoe™ X.
*   **Limitació tècnica:** Depèn al 100% de la connexió a internet i dels servidors externs de Panasonic. Qualsevol caiguda del servei de Panasonic o canvi a la seva API bloqueja temporalment el control des de Home Assistant, la qual cosa no s'ajusta del tot a l'enfocament *Local-First* de la Casa RSM.

### 1.2. Integració local directa: Interfície ESP32 sobre port CN-CNT (100% local i DIY)

Totes les unitats interiors residencials i comercials de Panasonic disposen d'un connector intern a la seva placa electrònica anomenat **CN-CNT** (port de comunicació sèrie de 5V de 5 pins).

*   **Connexió física:** Es connecta una placa electrònica amb un microcontrolador **ESP32** (o ESP8266) acompanyat d'un convertidor de nivell lògic de 5V a 3,3V. Aquesta placa es connecta directament al port CN-CNT de la placa mare de la unitat interior i s'alimenta dels mateixos 5V que ofereix el connector de Panasonic.
*   **Integració lògica:** Es programa l'ESP32 amb el firmware **ESPHome** utilitzant el component personalitzat `panasonic_ac`. L'ESP32 es comunica de forma directa en xarxa local amb Home Assistant mitjançant el protocol API natiu d'ESPHome.
*   **Prestacions:** Control en temps real (temps de resposta inferior a 500 ms), lliure de núvol, estable davant de caigudes d'internet i capaç de llegir directament codis d'error tècnics de les màquines, la temperatura ambient real mesurada pel sensor de retorn de la màquina i el consum elèctric (en models compatibles).
*   **Requisit físic:** Cal allotjar la petita placa ESP32 a l'interior de la carcassa de la unitat interior o en una caixa de derivació a prop de la unitat de conductes/split.

### 1.3. Integració per maquinari professional local: IntesisBox / Modbus

Opció industrial molt robusta de tercers.

*   **Connexió física:** S'instal·la una interfície de paret específica de la marca *Intesis* (per exemple, Intesis Panasonic AC to Modbus RTU/TCP). Aquest dispositiu es connecta al port CN-CNT de la màquina i exposa una connexió de xarxa per cable.
*   **Integració lògica:** Home Assistant es comunica amb la interfície a través del component **Modbus TCP** natriu.
*   **Avantatges:** Connexió per cable Ethernet per a màxima estabilitat (evita el Wi-Fi) i integració local directa.
*   **Limitació:** Cost elevat (aproximadament 200-300 € per cada unitat interior).

---

## 2. Casos d'ús i automatitzacions en Home Assistant

La integració local de les bombes de calor permet dissenyar escenes de confort avançades i optimitzar l'ús de l'electricitat:

### 2.1. Climatització intel·ligent per excedents fotovoltaics (Solar Dump)

*   **Lògica de control:** Quan el comptador general de dades (**Smart Meter**) i l'inversor solar indiquen que hi ha una exportació a la xarxa d'excedents fotovoltaics superior a 1,5 kW (per exemple, a les 12:00 h a l'estiu), Home Assistant encén de forma automàtica la climatització per conductes a la planta primera o segona.
*   **Objectiu:** Utilitzar l'energia sobrant per pre-refredar o pre-escalfar l'estructura física de la casa (inèrcia tèrmica dels materials), evitant haver d'activar el clima durant les hores de nit (quan no hi ha producció de plaques solars).

### 2.2. Apagat automàtic per obertura de fusteries exteriors

*   **Lògica de control:** Si el sensor magnètic cablejat d'una finestra d'un dormitori (P2) detecta que està oberta durant més de 3 minuts, Home Assistant apaga automàticament la unitat de conductes de la P2 o envia una alerta sonora. No es torna a permetre l'encesa automàtica del clima fins que totes les finestres de la zona estiguin totalment tancades.

### 2.3. Coordinació circadiana amb nanoe™ X

*   **Lògica de control:** Tot i que la climatització estigui apagada per temperatura, Home Assistant pot activar periòdicament el mode "només ventilació" a velocitat mínima per fer funcionar la tecnologia **nanoe™ X** de purificació de l'aire, purificant l'ambient d'al·lèrgens i virus en hores seleccionades de màxima ocupació familiar.

---

## 3. Requisits per al Projecte Executiu (PE)

Per permetre la integració d'aquest control en fase d'obra, cal verificar que el PE contempli:

1.  **Espai per a electrònica de control:** Deixar una caixa de derivació buida de Ø80 mm a prop del registre de la màquina de conductes de la planta primera i segona per poder allotjar de forma accessible la placa ESP32 d'integració sèrie.
2.  **Presa de corrent local de servei:** Preveure alimentació a 230V a la zona dels plenums de conductes, independentment de la línia elèctrica de potència de les màquines de clima, per alimentar controladors de comportes de reixetes motoritzades si es realitza zonificació DIY.
3.  **Fil de comunicació apantallat:** Canalització des de l'interior de les màquines cap a la zona del comandament de paret per permetre cablejats de bus de comunicació apantallats de recanvi.

---
*Document de treball per a la integració domòtica de la climatització en Home Assistant.*
