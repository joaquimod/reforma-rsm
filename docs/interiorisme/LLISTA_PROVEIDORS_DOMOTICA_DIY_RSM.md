# Llista de proveïdors de domòtica DIY - Casa RSM

Aquesta llista recull marques de sensors, càmeres, controladors i components per a sistemes domòtics autogestionats (basats en Home Assistant, Apple Home o similars), classificats per fiabilitat i canal de compra.

## 1. Marques de fiabilitat alta (Integració robusta)
Sistemes que "funcionen sempre", amb bona documentació i integració nativa o via Zigbee2MQTT.

*   **Shelly (Bulgària)**: [shelly.com](https://www.shelly.com)
    *   Especialitat: Relès WiFi que caben darrere dels interruptors. Mesura de consum elèctric. Molt fiables i sense necessitat de núvol (local-first).
    *   On comprar: **Amazon** o **Botiga web oficial**.
*   **Aqara (Ecosistema Xiaomi)**: [aqara.com](https://www.aqara.com)
    *   Especialitat: Sensors Zigbee (moviment, temperatura, fuites d'aigua, vibració) petits, elegants i amb bateries de llarga durada.
    *   On comprar: **Amazon** (més ràpid) o **AliExpress (Aqara Official Store)** per millors preus.
*   **Philips Hue**: [philips-hue.com](https://www.philips-hue.com)
    *   Especialitat: Il·luminació Zigbee. El millor control de regulació (dimming) i qualitat de llum del mercat.
    *   On comprar: **Amazon**, **MediaMarkt** o **PC Componentes**.
*   **Ubiquiti / UniFi Protect**: [ui.com](https://ui.com)
    *   Especialitat: Càmeres de seguretat POE i WiFi de gamma professional/prosumer. Emmagatzematge local sense subscripcions.
    *   On comprar: **EuroDK** (Letònia, molt bons preus) o **Amazon**.

## 2. Marques de fiabilitat mitjana / Excel·lent preu (Ecosistema DIY)
Productes ideals per automatitzacions no crítiques o per a usuaris que els agrada "trastejar".

*   **Sonoff**: [sonoff.tech](https://sonoff.tech)
    *   Especialitat: Dispositius WiFi i Zigbee molt econòmics. Famós per ser fàcilment modificable (flashing Tasmota/ESPHome).
    *   On comprar: **AliExpress (Sonoff Official Store)** és l'opció més barata de lluny.
*   **Tuya / Smart Life**:
    *   Especialitat: L'ecosistema més gran del món. Hi ha sensors de tota mena sota mil marques diferents (Zemismart, Moes, etc.).
    *   On comprar: **AliExpress** és el regne de Tuya. Buscar sempre versions **Zigbee 3.0** per a millor fiabilitat.
*   **Reolink**: [reolink.com](https://reolink.com)
    *   Especialitat: Càmeres amb bona relació qualitat-preu que permeten integració local (RTSP/ONVIF) sense dependre del seu núvol.

## 3. Components de control i "Maker" ( DIY pur)
El "cervell" del sistema domòtic de Casa RSM.

*   **Raspberry Pi / Mini PCs (NUC)**:
    *   Funció: Hosting de **Home Assistant**. Es recomana un Mini PC (recondicionat a Amazon/eBay) per sobre de Raspberry Pi per a major estabilitat del disc (SSD).
*   **Dongles Zigbee**:
    *   Recomanació: **Sonoff Zigbee 3.0 USB Dongle Plus** (Model P o E). És l'antena estàndard per a Home Assistant.
    *   On comprar: **AliExpress** o **Amazon**.
*   **ESP32 / ESP8266**:
    *   Funció: Crear sensors propis (qualitat de l'aire, control de LEDs, etc.) amb **ESPHome**.
    *   On comprar: **AliExpress** (per quantitat) o **Diotronic / Ondaradio** (Barcelona) per compra física immediata.

## Canals de compra recomanats
1.  **AliExpress**: El millor per a sensors Zigbee (Aqara/Tuya/Sonoff) i components electrònics. Temps d'entrega: 10-15 dies (AliExpress Standard Shipping).
2.  **Amazon**: El millor per a equipament crític (Inici de projecte, Hubs, Càmeres) per la facilitat de devolució si no s'integren bé.
3.  **Diotronic (BCN)**: C/ de Muntaner, 49. Botiga física de referència per a plaques (ESP32/Raspberry) i sensors si necessites una peça avui mateix.

---
*Darrera actualització: 9 d'abril de 2026*
