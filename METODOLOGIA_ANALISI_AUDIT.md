# Metodologia d'Anàlisi Tècnica - Projecte Bàsic RSM

Aquest document descriu el funcionament de l'**Orquestrador d'Anàlisi Tècnica**, l'eina automàtica dissenyada per auditar la qualitat, coherència i compliment normatiu del Projecte Bàsic de la Casa RSM.

## Com funciona l'Orquestrador?

L'orquestrador és un script en Python (`orchestrator.py`) que actua com un auditor automàtic. El seu procés és:
1.  **Llegeix**: Obre tots els PDFs de la versió especificada (Memòria, Plànols, EBSS) i n'extreu tot el text accessible.
2.  **Consulta Regles**: Carrega el fitxer `config/audit_rules.yaml` on hi ha els paràmetres tècnics (Passivhaus, CTE, Normativa VNG).
3.  **Cerca Patrons**: Utilitza "Expressions Regulars" (Regex) per buscar conceptes clau, dimensions i materials dins del text del projecte.
4.  **Avalua i Puntua**: Compara el que troba amb les regles i genera alertes (Findings) i puntuacions (KPIs).

---

## Punts de Control Analitzats

L'orquestrador verifica automàticament els següents aspectes crítics del Projecte Bàsic:

### 1. Estàndard EnerPHit (Eficiència Energètica)
*   **Objectiu:** Garantir especificacions d'aïllament tèrmic d'alt rendiment per a la certificació Passivhaus.
*   **Mètode de Cerca:**
    *   Rastreja paraules clau: `SATE`, `Llana Mineral`, `XPS`, `EPS`, `Passivhaus`.
    *   Busca gruixos associats: Ex. "16 cm", "160 mm".
    *   Verifica sistemes de ventilació: Busca mencions a `VMC`, `Recuperador de calor` o `Ventilació Mecànica`.
*   **Criteri d'Alerta:** Si no troba materials aïllants explícits o gruixos < 15cm (o la seva equivalència en U-valor), aixeca una alerta. La manca de VMC és alerta crítica.

### 2. Habitabilitat (Decret 141/2012)
*   **Objectiu:** Compliment de dimensions mínimes per a la dignitat de l'habitatge i cèdula de Segona Ocupació - Reforma.
*   **Mètode de Cerca:**
    *   **Alçada Lliure**: Busca cotes o textos que indiquin alçades inferiors a **2.50m** (estances) o **2.20m** (cuines/banys).
    *   **Superfícies**: Verifica les dimensions mínimes (6 m² per habitació, 20 m² per estar-menjador-cuina).

### 3. Accessibilitat (Normativa VNG + CTE)
*   **Objectiu:** Garantir que l'habitatge és "Practicable" i adaptable, segons requisits locals estrictes.
*   **Mètode de Cerca:**
    *   **Ascensor**: Busca mencions a l'`Espai de Reserva` obligatori (mínim **1.60x1.60m**) o la instal·lació efectiva.
    *   **Portes**: Busca referències a portes de pas estret (ex: `70 cm`, `72 cm`) en lloc del mínim de **0.80m** per a l'entrada i estances principals.
    *   **Passadissos**: Busca amplades de pas inferiors a **1.00m** en l'itinerari accessible principal.
    *   **Gir**: Busca mencions als cercles de maniobra de **1.20m** (practicable) o **1.50m** (adaptat) davant de portes i a la cuina/bany.

### 4. Finances i Ajuts (Next Generation)
*   **Objectiu:** Assegurar els elements administratius necessaris per cobrar les subvencions.
*   **Mètode de Cerca:**
    *   Busca mencions al **Certificat Energètic (CEE)** de l'estat actual ("Existent", "Abans de l'obra").
    *   Busca l'objectiu d'estalvi necessari: Mencions a **"Estalvi"**, **"Energia Primària"**, **"30%"** (Requisit IRPF/NextGen).

### 5. Urbanisme Vilanova (Nucli Antic)
*   **Objectiu:** Integració estètica i normativa local.
*   **Mètode de Cerca:**
    *   **Materials Prohibits**: Alerta si troba `PVC`, `Alumini sense RPT` o `Acabats plàstics/acrílics` en façana.
    *   **Instal·lacions**: Busca elements prohibits en façana com `Split`, `Unitat exterior` o `Compressor` a la vista.
    *   **Volades**: Verifica que els balcons no superin la volada màxima (ex. 45cm) segons l'amplada del carrer.

---

## Càlcul dels KPI (Puntuació)

El Dashboard mostra dos grans percentatges que resumeixen l'estat del projecte. El càlcul és penalitzador: parteix de la perfecció i resta punts per cada incertesa o risc detectat.

### 1. KPI EnerPHit (Eficiència)
*   **Base:** 100 punts.
*   **Penalització:** Resta **15 punts** per cada "Alerta" detectada (ex: falta gruix aïllament, falta VMC).
*   *Interpretació:* Un 85% significa normalment 1 alerta detectada. Un 70% serien 2 alertes.

### 2. KPI Normativa (Urbanisme + Habitabilitat + Accessibilitat)
*   **Base:** 100 punts.
*   **Penalització:** Resta **10 punts** per cada "Alerta" en aquestes categories.
*   *Interpretació:* Un 80% sol indicar 2 alertes menors (probablement temes d'accessibilitat o alçades puntuals).
