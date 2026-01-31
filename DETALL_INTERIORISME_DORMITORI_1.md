# Detall d'Interiorisme: Dormitori 1 | Casa RSM

Aquest document detalla les especificacions tècniques i estètiques per a la personalització del dormitori principal, integrant l'ADN artístic de la propietat amb la tecnologia domòtica i els criteris de confort EnerPHit.

---

## 1. Memòria de materials i acabats

| Element | Especificació | Referència / Proveïdor |
| :--- | :--- | :--- |
| **Parets** | Estuc de calç artesanal de gran fi. Color Blanc Trencat (os). | *Cales de Pescador / Revestimientos Naturales* |
| **Paviment** | Microciment continu gris seda (silk grey). Tacte càlid i alta inèrcia. | *Topciment / Microdeck* |
| **Sostre** | Placa de guix laminat amb fussa perimetral per a cortines i LED. | *Pladur / Knauf* |
| **Mobiliari** | Roure massís natural amb tractament d'oli incolor (mat). | *Hannun / Decowood / Mobel.Store* |
| **Tèxtils** | Lli rentat de gran format. Colors: Cru (sorra) i Blau Mediterrani. | *Torres Novas / Zara Home (Linen Collection)* |

---

## 2. Esquema d'il·luminació (Home Assistant)

L'il·luminació es gestiona íntegrament mitjançant **Home Assistant**, evitant la llum zenital directa sobre el llit per afavorir el ritme circadià.

### Punts de llum:
1.  **Cova Perimetral (Indirecta):** Tira LED RGBW (CRI > 90) oculta a la fussa del sostre sobre el capçal. Permet banyar la paret d'estuc amb colors atmosfèrics.
2.  **Llum de lectura:** Aplic de paret o penjant minimalista a cada costat del llit. Estil nòrdic en fusta de roure o metall negre mat (*Lights of Scandinavia*).
3.  **Il·luminació d'accentuació:** No s'instal·len focus d'accentuació; la puresa de l'estuc de calç és l'únic focus visual.

### Escenes programades:
*   **🌅 Matinada Suau:** Pujada progressiva (30 min) de la intensitat LED en tons càlids (2000K) i obertura automàtica de la persiana al 20%.
*   **💤 Escena Repòs:** Apagat total de totes les llums, tancament de persianes i activació de la climatització en mode "Nit" (Silenci). El color LED passa a un vermell molt tènue si es detecta moviment al bany durant la nit per no desvetllar.
*   **🎨 Escena Mediterrània:** Els LED de la fussa perimetral adopten el to *Blau Mediterrani*, banyant la textura natural de les parets nues.

---

## 3. L'ADN artístic: Optimitització de l'Espai Estret

El disseny se subordina a la **geometria estreta** de l'habitació, prioritzant la fluïdesa cap a l'exterior i la nuesa de materials.

*   **Configuració del Llit:** **Llit individual**, situat **arrambat a la paret del fons** i orientat de forma **perpendicular** a la porta de sortida a la terrassa. Aquesta disposició és la que marca el plànol original per optimitzar l'espai estret.
*   **Accessos:** La porta d'entrada al dormitori (fusta de roure clar) s'ubica a l'esquerra segons s'entra. A la dreta hi ha una **única porta doble** de sortida a la terrassa.
*   **Mobiliari Minimalista:** Una única **tauleta de nit volant** de fusta de roure al costat del llit.
*   **Puresa Mural:** Parets d'**estuc de calç** totalment nues, sense quadres, ressaltades per la llum indirecta.
*   **Plantes d'interior:** Una Kentia prop del finestral de la terrassa.

---

## 4. Confort tèrmic (EnerPHit)

*   **Ventilació:** Difusor de ventilació de doble flux amb recuperació de calor, totalment silenciós, situat discretament per evitar corrents d'aire sobre el llit.
*   **Hermeticitat:** Tancament de roure amb triple vidre i sistemes de protecció solar exterior automatitzats (Mallorquines o persianes graduables).

---
*Document generat per Antigravity per al Projecte Executiu Casa RSM - Gener 2026*
