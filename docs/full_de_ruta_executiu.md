# Full de Ruta: Evolució del Sistema d'Auditoria per al Projecte Executiu (PE)

Aquest document detalla les millores proposades per a l'evolució de l'agent d'Antigravity vers la fase de Projecte Executiu de la Casa RSM, centrant-se en la visualització, gestió tècnica i coordinació.

## 1. Visualització i Presentació d'Impacte
Per passar de dades brutes a comunicació efectiva amb l'arquitecte i futurs constructors:

*   **Dashboards de Control (Web Local):** Creació d'una interfície visual (HTML/CSS premium) que llegeixi els resultats de l'auditoria. Permetria veure d'un cop d'ull el percentatge de compliment EnerPHit i normatiu.
*   **Diagrames i Infografies Automàtiques:** Ús d'extensions (Mermaid.js o SVG) per generar automàticament esquemes de l'envolupant tèrmica, comparant les propostes de l'arquitecte amb els requeriments del promotor.
*   **Contingut Multimèdia:** Integració de NotebookLM per a la generació d'Audio Overviews per a tercers, i exploració d'APIs de vídeo per visualitzar detalls constructius complexos.

## 2. Gestió Tècnica Avançada del PE
El Projecte Executiu augmenta la densitat de dades significativament:

*   **Integració Nativa amb Google Drive (MCP):** Connectar Antigravity directament al Drive per eliminar la descàrrega manual. L'agent monitoritzarà versions noves de plànols i amidaments en temps real.
*   **Base de Dades Forense de Materials (SQLite):** Migració dels Excels d'amidaments a una base de dades local. Això permetrà fer consultes SQL complexes (ex: "Suma total de ponts tèrmics detallats en la secció de fusteria").
*   **Auditoria de Pressupost i Amidaments:** Eines per comparar l'evolució econòmica entre el PB i el PE, detectant desviacions en quantitats de materials crítics (aïllaments, vidres d'altes prestacions).

## 3. Coordinació i Project Management (PM)
Gestió del flux de treball i presa de decisions:

*   **Sistema d'Alertes Intel·ligents:** Configuració de notificacions (Slack o Telegram/WhatsApp MCP) per avisar el promotor quan s'introdueixi un canvi que posi en risc la certificació Passivhaus.
*   **Registre de Decisions de Disseny:** Automatització d'un log que vinculi cada decisió de l'arquitecte amb la normativa de Vilanova o els criteris EnerPHit, servint de base per a la negociació final.
*   **Privadesa i Seguretat:** Continuïtat en l'ús de models locals com `gpt-oss-safeguard-20b-mlx` per a l'anàlisi de costos i dades sensibles, garantint que la propietat intel·lectual del projecte es mantingui en l'entorn del promotor.

---
*Aquest document serveix de guia estratègica per a la propera fase del projecte RSM.*
