# Documentació del sistema de dades: Casa RSM

Aquest document resumeix la infraestructura digital creada per al seguiment del Projecte Executiu (abril 2026) i la futura gestió de manteniment de l'habitatge.

## 1. Arquitectura de dades (Obsidian)
El sistema es basa en **fitxes individuals** per a cada espai de la casa (habitacions, terrasses, escales, ascensor, etc.). 

*   **Ubicació**: `docs/espais/`
*   **Format**: Cada fitxer `.md` conté propietats YAML (metadades) que el plugin **Dataview** llegeix automàticament.
*   **Atributs clau**:
    *   `planta`: PB, P1, P2, PSC, C (usat per a ordinació arquitectònica).
    *   `paviment`: Microciment (SMC), Ceràmica, Pedretes del Garraf, etc.
    *   `mobiliari_equipament`: Detalls del contingut de l'estança.
    *   `il_luminacio`, `clima`, `portes`, `color_paret`, etc.

## 2. Quadre de comandament mestre
El fitxer [**`DOC_ESPAIS_MASTER.md`**](projecte_rsm/docs/espais/DOC_ESPAIS_MASTER.md) centralitza tota la informació.
*   **Visualització**: Inclou Callouts desplegables amb els plànols de cada planta.
*   **Taula Dinàmica**: Una consulta Dataview que vincula les dades de totes les fitxes.
*   **Interactivitat**: En fer clic a la columna "Planta", s'obre la imatge del plànol corresponent.

## 3. L'ecosistema Web (Explorer)
S'ha creat una aplicació web perquè puguis consultar les dades fora d'Obsidian.

*   **Tecnologia**: Aplicació SPA (Single Page Application) construïda amb **Vite** i JavaScript modern. Utilitza **marked.js** per renderitzar el Markdown d'Obsidian en temps real al navegador.
*   **Allotjament**: Allotjat a **Surge.sh**, un servei d'allotjament estàtic d'alta velocitat (CDN).
*   **Propietat**: El compte està vinculat exclusivament al correu **`joaquim.olive@gmail.com`**. Tu ets el propietari de l'instància.
*   **Costos**: El cost del servei és de **0 euros (gratis)** de per vida per a projectes estàtics d'aquest volum. No hi ha cap subscripció activa ni càrrecs ocults.
*   **Seguretat**: 
    *   **Encriptació**: La web funciona sota protocol **HTTPS** (certificat SSL automàtic), xifrant la comunicació entre el teu mòbil i el servidor.
    *   **Clau d'accés**: S'ha implementat un pany digital (**`RSM2026`**) que s'executa al navegador per evitar l'accés de tercers.
*   **URL**: [https://casa-rsm-explorer.surge.sh](https://casa-rsm-explorer.surge.sh)
*   **Dades del compte de servei**: 
    *   Email: `joaquim.olive@gmail.com`
    *   Password servei: `RSM2026_Admin` (Vàlida per a la gestió tècnica del domini).


## 4. Com actualitzar la web
Si fas canvis a les dades al teu Obsidian, la web no s'actualitza sola. Per fer-ho:

1.  Demanar a l'assistent: **"Actualitza la web"**.
2.  L'assistent executarà el fitxer `scripts/actualitzar_web.sh` que regenera el `data.json` i el puja al servidor de Surge.

---
## Guia administrativa
*   **Regles d'estil**: Tots els títols i fitxers han de seguir el format **Sentence case** (ex: `Dormitori principal.md`).
*   **Iconografia**: Està totalment prohibit l'ús d'emojis o icones en la documentació formal per mantenir un aspecte premium i professional.

*Actualitzat el: 04 d'abril de 2026*
