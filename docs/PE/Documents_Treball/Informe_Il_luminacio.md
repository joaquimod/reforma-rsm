# Informe tècnic: estratègia d'il·luminació arquitectònica i automatitzada

**Data:** 18 de febrer de 2026
**Fase:** Projecte Executiu
**Objectiu:** Definir un sistema d'il·luminació minimalista, integrat en l'obra i totalment automatitzable per Home Assistant (DIY), cobrint espais interiors i exteriors.

---

## 1. Conceptes generals: la llum integrada

En un estil minimalista modern, la llum no és un accessori, sinó part de l'arquitectura.

*   **Il·luminació Indirecta (Fosos de llum):** Ús de perfils d'alumini ocults en falsos sostres, mobles o cortiners. La llum "banya" les superfícies.
*   **Perfileria Trimless (Sense marcs):** Ús de perfils encastats a ras de pladur que queden totalment anivellats amb la paret/sostre. Quan estan apagats, són pràcticament invisibles.
*   **Temperatura de color:**
    *   **3000K (Blanc Càlid):** Estàndard per a tota la casa.
    *   **2700K (Molt Càlid):** Per a zones de relaxació (dormitoris).
    *   **CRI > 90:** Exigència mínima per garantir que els tons de la fusta natural i materials es vegin realistes.

---

## 2. Definició per espais

### A. Planta Baixa (Zonificació tècnica i flexible)
*   **Garatge i Sala de Màquines:** Il·luminació funcional lineal (perfils estancs IP44) de muntatge en superfície. A la sala de màquines s'activa per interruptor de porta.
*   **Sala Polivalent:** Instal·lació de **carril magnètic encastat** minimalista. Permet intercanviar focus d'accent (ús taller) per mòduls difusos (ús dormitori).
*   **Safareig i Bany PB:** Plafons LED extraplans circulars encastats.

### B. Planta 1 i 2 (Hàbitat i Cortesia)
*   **Cuina i Despensa:**
    *   Cuina: Llum de treball sota mobles alts (Tira LED oculta).
    *   Despensa: Il·luminació lineal integrada en el prestatge superior o sostre, activada per sensor d'obertura.
*   **Bany de Cortesia (P1):** Il·luminació decorativa. Retroil·luminació del mirall i bany de paret vertical (wall-washer) ocult per accentuar la textura del revestiment.
*   **Sala d'estar:** Il·luminació perimetral i control de preses de corrent per a llums de peu/taula mitjançant domòtica.
*   **Escales:** "Step-lights" (baixa alçada) cada un o dos esglaons. Activació nocturna tènue.

### C. Exteriors (Entrada, Pati i Terrasses)
*   **Façana i Entrada:** Aplics de paret amb emissió doble (Up/Down) de geometria simple.
*   **Pati i Terrassa posterior:** Il·luminació lineal integrada en el paviment o sota bancs. Focos d'estaca (estil minimalista) per il·luminar plantes o elements arquitectònics.
*   **Protecció:** Ús de sistemes **IP67** en zones de terra i **IP65** en parets.

---

## 3. Requeriments per a la Domòtica (DIY)

Atès que el sistema es controlarà amb Home Assistant, es demana a l'arquitecte i electricista:

1.  **Centralització de Drivers:** Tots els transformadors LED han d'estar en punts accessibles i ventilats (no perduts en falsos sostres).
2.  **Mòduls de Control:** Preveure espai dins dels quadres elèctrics o caixes de registre per a mòduls **Zigbee/Wi-Fi (tipus Shelly o Gledopto)**.
3.  **Fil Neutre:** Present en tot el cablatge de l'enllumenat (per als interruptors intel·ligents).
4.  **Sensors:** Preveure caixes de sostre en passadissos i banys per a detectors de presència (tipus "ull de bou" cec).

---

## 4. Anàlisi de sostenibilitat i cicle de vida

*   **Eficiència:** Reducció del consum energètic mitjançant l'atenuació automàtica i l'apagada per falta de presència.
*   **Deteriorament:** Els perfils d'alumini actuen com a dissipador de calor, doblant la vida útil de les tires LED respecte a les que s'instal·len soles.
*   **Contaminació lumínica:** Disseny que evita la llum fugaç cap al cel, protegint l'entorn nocturn del nucli urbà de Vilanova.

---

**Conclusió:** Una il·luminació invisible i automatitzada no només millora l'estètica minimalista de la Casa RSM, sinó que redueix el manteniment i el consum energètic dràsticament.
