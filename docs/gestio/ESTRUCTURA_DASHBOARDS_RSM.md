# Estructura de Dashboards - Casa RSM

**Document creat: 21 de maig de 2026**

El projecte Casa RSM utilitza dos panells de control (dashboards) complementaris per gestionar i comunicar la informació de la reforma integral. Cadascun d'aquests espais té un públic objectiu, una estètica i un propòsit específic.

---

## 1. Dashboard Executiu (Presentació del Projecte)

Aquest és l'aparador principal del projecte, dissenyat per oferir una visió global, atractiva i sintètica de la reforma. Està pensat per a la comunicació amb parts interessades de perfil menys tècnic, com ara familiars, entitats bancàries o per a una presentació d'alt nivell.

*   **Fitxer font:** `index.html` (ubicat a l'arrel del repositori)
*   **URL pública (GitHub Pages):** [joaquimod.github.io/reforma-rsm/](https://joaquimod.github.io/reforma-rsm/)
*   **Títol:** Definició del projecte de reforma
*   **Seguretat:** Accés protegit mitjançant clau d'autenticació.

### Característiques principals:
*   **Estètica immersiva:** Utilitza un tema fosc (Dark Mode) de disseny "premium" basat en Tailwind CSS i animacions fluides amb GSAP.
*   **Visió estratègica:** Mostra un resum visual de les dades clau, incloent imatges destacades del concepte arquitectònic (renders o fotografies de l'estat actual i futur).
*   **Indicadors d'estat (KPIs):** Resumeix en un cop d'ull aspectes globals, com l'estat de les validacions (p. ex., "EnerPHit Pass", "VNG Review").
*   **Mapa de fases:** Presenta el full de ruta general (bàsic, executiu, construcció).

---

## 2. Dashboard Operatiu / Explorer (El "Digital Twin")

Aquest segon entorn és l'espai de treball diari per a la gestió de la informació tècnica del projecte. Conegut com el "bessó digital" (*digital twin*) documental, s'adreça al Promotor, Arquitectes i Industrials per centralitzar totes les decisions preses durant el procés de disseny i execució.

*   **Fitxer font:** `web/index.html`
*   **URL pública (Surge):** [casa-rsm-explorer.surge.sh](https://casa-rsm-explorer.surge.sh/)
*   **Títol:** CASA RSM | Explorer
*   **Seguretat:** Accés protegit mitjançant clau d'autenticació.

### Característiques principals:
*   **Estètica funcional:** Presenta un disseny lluminós (Light Mode), net i molt estructurat, similar a un gestor documental, per facilitar la lectura intensiva.
*   **Navegació arquitectònica:** L'eix vertebrador és l'estructura de la casa. Permet accedir a la informació filtrant per plantes: Planta Baixa (PB), Planta Primera (P1), Planta Segona (P2), Sotacoberta (PSC) i Coberta (C).
*   **Documentació tècnica organitzada:** La barra lateral actua com a índex per consultar en qualsevol moment la informació estratègica:
    *   **Estratègia i Guies:** Conceptes base, manteniment, estratègia d'interiorisme.
    *   **Organització:** Informes d'espais complexos (Garatge, Pati, Bugaderia).
    *   **Proveïdors:** Llistes de marques analitzades per a electrodomèstics, tecnologia, climatització i tancaments.
    *   **Proveïdors: mobiliari i banys:** Llistats d'adreces de botigues i catàlegs recomanats.
    *   **Anàlisi per estança:** Fitxes que detallen les necessitats i decisions de mobiliari concretes per a la Sala d'estar, Dormitoris, Cuina, etc.
*   **Actualització dinàmica:** Tota la informació prové de fitxers de text pla (Markdown) agrupats en un paquet de dades (`docs_bundle.js`), la qual cosa permet una actualització àgil i constant per part del Promotor a mesura que avança el projecte Executiu.

---

**Resum per a l'ús de les eines:**
Si necessites explicar **què és** la Casa RSM a algú extern de forma ràpida i atractiva, envia l'enllaç del **Dashboard Executiu**.
Si necessites consultar **com s'està resolent** tècnicament o quina decisió de proveïdor es va prendre per a un espai, obre el **Dashboard Operatiu (Explorer)**.
