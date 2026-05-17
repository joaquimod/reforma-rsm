# Informe tècnic: selecció d'enllumenat Lux Light (PE)

**Data:** 15 de maig de 2026.
**Fase:** Projecte Executiu (Definitiu).
**Objectiu:** Especificació tècnica de les lluminàries Lux Light i la seva integració amb Home Assistant per a un minimalisme total.

---

## 1. Conceptes generals i Criteris de Disseny

En un estil minimalista modern, la llum no és un accessori, sinó part de l'arquitectura. S'ha adoptat la marca **Lux Light** com a estàndard per a tot l'habitatge.

*   **Temperatura de Color (CCT):** **3000K** (Blanc Càlid) com a estàndard general per garantir la calidesa sobre el roure i la ceràmica sorra.
*   **Reproducció Cromàtica:** Exigència de **CRI > 90** en tots els models per a una visualització realista dels materials.
*   **Regulació:** Tots els models principals són **Dimmable (Triac)** per a la seva integració amb Home Assistant.
*   **Tecnologia Trimless:** Ús de perfils encastats a ras de pladur que queden totalment anivellats amb la paret/sostre.

---

## 2. Selecció Tècnica: Catàleg Lux Light

S'han seleccionat els següents models base per a l'execució del projecte:

### A. Il·luminació General (DLIGHT)
*   **Aplicació:** Cuina, Menjador i Banys.
*   **Característiques:** Downlight LED amb baix enlluernament (UGR < 19). Potències de 10W a 15W segons l'alçada del sostre.

### B. Espais Tècnics i Sotacoberta (FLAT / SLIM)
*   **Aplicació:** Zones amb fals sostre limitat pel gruix de l'aïllament tèrmic.
*   **Característiques:** Perfil ultra-fí amb tecnologia 3CCT (selector de temperatura manual).

### C. Zones de Descans (CONFORT 24)
*   **Aplicació:** Dormitoris i zones de relax.
*   **Característiques:** Òptica profunda per evitar l'enlluernament directe des del llit. Màxim confort visual.

### D. Il·luminació d'Accent (Carril Magnètic)
*   **Aplicació:** Sala polivalent i zones de treball.
*   **Característiques:** Sistema flexible que permet intercanviar focus d'accent per mòduls difusos segons l'activitat.

---

## 3. Definició per espais

### A. Planta Baixa (Zonificació tècnica i flexible)
*   **Garatge i Sala de Màquines:** Il·luminació funcional lineal (perfils estancs IP44) de muntatge en superfície. A la sala de màquines s'activa per interruptor de porta.
*   **Sala Polivalent:** Instal·lació de **carril magnètic encastat** minimalista. Permet intercanviar focus d'accent (ús taller) per mòduls difusos (ús dormitori).
*   **Safareig i Bany PB:** Plafons LED extraplans circulars encastats.

### B. Planta 1 i 2 (Hàbitat i cortesia)
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
