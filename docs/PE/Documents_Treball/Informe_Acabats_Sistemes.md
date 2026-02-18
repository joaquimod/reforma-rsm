# Informe tècnic: envolupant, mecanismes i sistemes de seguretat

**Data:** 18 de febrer de 2026
**Fase:** Projecte Executiu
**Objectiu:** Definir l'acabat exterior de la casa, la sèrie de mecanismes elèctrics i la infraestructura de seguretat i gestió d'aigua.

---

## 1. Envolupant exterior: el look & feel de la façana

Atesa la solució constructiva i la integració en el conjunt arquitectònic, es proposen els següents acabats per a la Casa RSM:

*   **Acabat:** Morter acrílic/siloxànic de gra fi. Repel·leix l'aigua i la contaminació, clau en l'entorn de Vilanova.
*   **Color de la façana del carrer:** **Gris**, per mantenir la coherència estètica amb les altres tres cases del grup.
*   **Col·locació del SATE (Façana carrer):** L'aïllament tèrmic exterior se situarà en les parets que queden a l'interior de les terrasses i balcons.
*   **Color de la façana posterior:** Es proposa l'ús del **Blanc** per maximitzar la lluminositat i el confort tèrmic en la zona privada.
*   **Zòcol inferior:** Revestiment de protecció en planta baixa (primers 50cm) mitjançant el mateix gres porcelànic del terra interior o pedra natural grisa. Evita el deteriorament per salpicadures de pluja i trànsit del carrer.

---

## 2. Mecanismes elèctrics (estètica i domòtica)

La selecció de mecanismes ha de ser coherent amb el minimalisme de la casa i la compatibilitat amb el sistema DIY (Home Assistant).

*   **Marques de referència:** Jung (Sèrie LS 990), Simon (100) o Bticino (Living Now).
*   **Acabat:** Blanc mat. Fugir de materials brillants o marcs complexos.
*   **Infraestructura:** Requisit de caixes de mecanisme de 60mm de profunditat a totes les estances per allotjar els micro-mòduls Zigbee/Wi-Fi (Shelly, etc.).

---

## 3. Seguretat i control d'accés

Disseny d'un sistema obert i centralitzable a la Raspberry Pi.

*   **Vídeo-porter IP:** Instal·lació de sistema basat en IP (standard SIP/ONVIF) compatible amb Home Assistant.
*   **Porta d'accés:** Instal·lació de pany amb bombí de seguretat de doble embragatge. Cal preveure un tub de dades/corrent que arribi fins al pany des del Rack Central per a futurs panys intel·ligents alimentats (Nuki/Tedee).
*   **Circuït tancat de TV (CCTV):** Pre-instal·lació de 3 punts de dades (Cat6 PoE) en cantonades exteriors estratègiques.

---

## 4. Gestió integral de l'aigua

Es defineix un sistema circular per maximitzar la qualitat de l'aigua interior i la sostenibilitat exterior.

### A. Qualitat de l'aigua de consum (xarxa municipal)
*   **Descalcificador general:** Instal·lació d'un equip de descalcificació per intercanvi iònic immediatament després del comptador (normalment a la Sala de Màquines de la PB).
    *   **Objectiu:** Protegir les canonades, l'aerotèrmia i els electrodomèstics de la calç de Vilanova.
*   **Òsmosi a la cuina:** Instal·lació d'un equip d'òsmosi inversa sota l'aigüera de la P1, amb aixeta de servei independent.

### B. Recuperació d'aigües pluvials
S'aprofitarà el potencial de recollida de la coberta i les terrasses intermèdies.
*   **Dipòsit existent:** Es rehabilitarà el pou ja existent al subsol del pati posterior.
    *   **Acció:** Cal projectar el nou recobriment d'estanquitat i sanejament d'aquest espai.
*   **Xarxa de pluvials:** Canalització de totes les baixants de la teulada i terrasses cap a aquest dipòsit de recuperació.
*   **Reg i usos externs:** Instal·lació d'una bomba submergida o equip d'aspiració connectat al sistema de reg automàtic i a la presa d'aigua del pati per a neteja.

---

**Resum operatiu:**

1.  **Façana:** Color gris al carrer i blanc a la part posterior. SATE a l'interior de les terrasses del carrer.
2.  **Mecanismes:** Jung LS 990 blanc mat (o similar) amb caixes de fons extra.
3.  **Seguretat:** Punts de dades PoE per a càmeres i porter IP.
4.  **Aigua:** Preveure espai per a descalcificador (PB), equip d'òsmosi (cuina) i projectar la rehabilitació de l'aljub de pluvials existent.

---
