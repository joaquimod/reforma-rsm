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

---

## 3. Infraestructura General Domòtica (DIY)

### Quadre Elèctric:
*   **Espai reserva:** Deixar espai per a un mesurador de consum per carril DIN (ex: Shelly EM) per monitoritzar l'eficiència EnerPHit.
*   **Protecció:** Diferencial específic per a la línia electrònica/informàtica.

### Persianes i Mallorquines:
*   **Motorització:** Portar alimentació (3 fils) a cada caixa de persiana/mallorquina.
*   **Control:** Tubs amples cap als interruptors de paret per permetre la instal·lació de micromòduls domòtics (ex: Shelly 2.5 o Sonoff Dual).

### Sensors (Zigbee/Thread):
*   **Ubicació:** No requereixen tubs (funcionen a bateria), però cal preveure una bona cobertura WiFi/Zigbee situant el Hub (Raspberry Pi/Mini PC) en una posició central (prop de l'estudi o la sala).

---

## 4. Requisits per al Projectista / Electricista

1.  **Tubs Corrugats:** Totes les canalitzacions de dades han de ser independents de les d'electricitat per evitar interferències.
2.  **Profunditat de Caixes:** Utilitzar caixes de mecanisme de 50mm de profunditat per facilitar la instal·lació de mòduls domòtics darrere els interruptors originals.
3.  **Xarxa:** El cablejat de dades ha de ser **UTP Cat6** com a mínim, certificat per a 1Gbps.

---
*Document generat per Antigravity per al Projecte de Reforma Casa RSM - Gener 2026*
