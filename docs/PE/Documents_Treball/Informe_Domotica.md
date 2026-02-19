# Informe tècnic: infraestructura per a sistema domòtic (DIY) i xarxes

**Data:** 18 de febrer de 2026
**Fase:** Projecte Executiu
**Objectiu:** Definir els espais i canalitzacions per a un sistema de control basat en Home Assistant en un edifici de 4 plantes (PB, P1, P2, PSC).

---

## 1. Topologia de la xarxa: l'estratègia vertical

Atesa la configuració de 4 plantes de la Casa RSM, la propagació de senyals sense fils (Wi-Fi/Zigbee) és crítica. Es proposa una estructura en "arbre" amb un nucli central.

### A. El Cervell (Rack Central)
*   **Ubicació recomanada:** Planta 1 (zona central o armari de serveis).
*   **Funció:** Punt d'entrada de fibra òptica, ubicació del router principal, switch PoE i hub de Home Assistant (RbPi).
*   **Requeriments:** Armari rack de 10" encastat o sobre-posat, amb ventilació passiva i 4 preses de corrent.

### B. La Columna Vertebral (Dorsal tècnica)
*   **Tub de pujada:** Cal un tub corrugat de Ø40mm que comuniqui verticalment les 4 plantes (entrant pels quadres elèctrics o patis tècnics).
*   **Funció:** Permetre passar cables de dades Cat6 entre plantes sense restriccions futures.

---

## 2. Connectivitat i cobertura

### A. Wi-Fi (Cablejat de punts d'accés)
No es pot dependre d'un sol router. Cal preveure **Punts d'Accés (AP)** a sostre alimentats per PoE (Power over Ethernet).
*   **Punts obligatoris:** Un a la P1 (cobertura PB i P1) i un altre a la P2 o PSC (cobertura P2 i PSC).
*   **Pre-instal·lació:** Caixa de mecanisme al sostre amb tub de Ø25mm fins al Rack Central.

### B. Malla Zigbee (Domòtica DIY)
*   Per garantir que els sensors de la PSC parlin amb el hub de la P1, cal crear una "malla".
*   **Requeriment:** Instal·lar com a mínim 2 dispositius Zigbee a corrent (interruptors o mòduls) per planta. Aquests dispositius repetiran el senyal automàticament.

---

## 3. Requeriments elèctrics per al PE

Aquests són els punts que han d'aparèixer al Pressupost del Projecte Executiu:

1.  **Fil Neutre a totes les caixes:** Absolutament necessari en tots els punts d'encès de llums per a la instal·lació de mòduls Zigbee/Wi-Fi (Shelly, Sonoff, etc.).
2.  **Caixes de gran profunditat:** Instal·lar caixes de paret (enllaçables o individuals) de **mínim 60mm de fons** a tota la casa (mecanismes d'il·luminació i persianes).
3.  **Dades als Quadres Elèctrics:** Tub de Ø25mm des del Rack fins a cada sub-quadre elèctric de cada planta per a la monitorització de consums.
4.  **Preses Multimèdia:** Doble presa de xarxa RJ45 darrere de cada punt de TV previst.

---

## 4. Eficiència i Seguretat (ESG)

*   **Monitorització Total:** L'arquitecte ha de preveure l'espai per a pinces amperimètriques al quadre general per llegir consums de: Clima, Cuina, i General.
*   **Integració Fotovoltaica:** Connexió per tub entre l'inversor (normalment a prop de les plaques a la PSC o PB) i el Rack Central.

---

**Resum de partides per al PE:**

| Partida | Descripció | Ubicació |
| :--- | :--- | :--- |
| **Infraestructura** | Armari Rack de dades encastat. | Planta 1 |
| **Tubs Dades** | Ø40mm vertical (Columna) + Ø25mm a sostre (Wi-Fi). | Totes les plantes |
| **Electricitat** | **Neutre** en tota la xarxa d'il·luminació. | Totes les plantes |
| **Mecanismes** | **Caixes de 60mm de fons.** | Totes les plantes |

---
