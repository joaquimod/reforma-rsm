# Sistema de Seguiment i Suport: Reforma Casa RSM
**Fase: Projecte Bàsic (PB)**
**Versió:** 1.0 (Gener 2026)

Aquest document detalla el protocol d'auditoria forense i suport tècnic dissenyat per assegurar l'èxit de la reforma integral de la Casa RSM, garantint el compliment del Decret d'Habitabilitat de Catalunya, el Codi Tècnic de l'Edificació (CTE) i l'estàndard Passivhaus (EnerPHit).

---

## 1. Components del Sistema de Suport
El sistema es basa en una arquitectura **Local-First** per protegir la confidencialitat del projecte:

1.  **Orquestrador (Python):** Script d'automatització que creua dades entre la memòria (PDF), els amidaments (Excel) i les regles de normativa (`config/audit_rules.yaml`).
2.  **Validador de Fitxers:** Verifica que la documentació rebuda de l'arquitecte sigui processable (PDF vectorial, Excel estructurat).
3.  **Model d'IA Local (LM Studio):** Utilitzem el model `gpt-oss-safeguard-20b-mlx` per analitzar dades sensibles de física de l'edifici sense enviar-les al núvol.
4.  **Base de Coneixement (NotebookLM):** Conté tota la normativa de Vilanova i la Geltrú i el CTE per a consultes ràpides.
5.  **Dashboard Visual:** Interfície per compartir els resultats amb els stakeholders d'una manera clara i no confrontativa.

---

## 2. Protocol d'Execució i Revisió
Quan es rebi la nova versió del Projecte Bàsic (PB), s'ha de seguir aquest ordre:

### Pas 1: Preparació
*   Col·locar els fitxers a `docs/PB/V1_RSM_PROPERA_SETMANA/`.
*   Executar `python3 scripts/pdf_validator.py` per confirmar que el PDF no és una imatge escanejada.

### Pas 2: Processament Automatitzat
*   Executar l'orquestrador: `python3 scripts/orchestrator.py --version V1_RSM_PROPERA_SETMANA`.
*   Això generarà l'informe d'auditoria i el **Prompt** per al càlcul tèrmic local.

### Pas 3: Validació de Física i Materials
*   Obrir el fitxer `PROMPT_LM_STUDIO_thermal.txt`.
*   Copiar el contingut a **LM Studio** per obtenir una validació de les transmitàncies (U-values) proposades per l'arquitecte.

### Pas 4: Revisió de Llicència Urbanística
*   Contrastar els materials de façana amb la `docs/normativa/LLISTA_VERIFICACIÓ_URBANÍSTICA_VNG.md`.
*   Verificar que no s'inclogui PVC ni acabats acrílics prohibits al Nucli Antic.

---

## 3. Consells per Iterar sobre el Projecte Bàsic (PB)
La fase de PB és el moment de fer canvis sense costos d'obra. Aquí tens consells per a la teva relació amb l'estudi d'arquitectura:

### A. El Llindar del 25% (CTE DB-HE)
*   **Consell:** Com que és una reforma integral, segurament superarem el 25% de l'envolupant modificada. Això obliga a l'arquitecte a presentar càlculs globals de consum (HE0) i de transmitància global K (HE1).
*   **Acció:** Demana si el projecte compleix el CTE per la "via simplificada" (materials sueltos) o per la "via global". Si vols Passivhaus, exigueix la via global.

### B. El Dilema de la Ventilació (HS3)
*   **Consell:** No acceptis ventilar només per finestres (airejadors). Amb un aïllament d'alta densitat, tindries condensacions.
*   **Acció:** Itera el projecte per incloure la **Ventilació Mecànica Controlada (VMC)** amb recuperació de calor al PB, per evitar haver de fer forats en fases posteriors.

### C. Gestió de la "Tensió Tècnica"
*   Usa el **Dashboard** com a eina de diàleg. En lloc de dir "això està malament", enfoca-ho com a **"Oportunitats d'Optimització per assegurar la Certificació"**.
*   Si l'arquitecte proposa PVC, recorda-li la **Carta de Colors de Vilanova** preventivament per evitar un KO de l'Ajuntament que retardaria la llicència 3 mesos.

### D. Geometries vs Memòries
*   L'error més comú és que la memòria digui "Aïllament de 15cm" i el detall de l'amidament en digui "8cm".
*   **Acció:** L'orquestrador detectarà aquestes puncions. Revisa sempre les unitats de l'Excel amb lupa.

---
**Proper pas:** Un cop validat el PB, iniciarem el full de ruta cap al **Projecte Executiu (PE)**, on el sistema d'IA s'integrarà amb el seguiment d'obra i el control de facturació.
