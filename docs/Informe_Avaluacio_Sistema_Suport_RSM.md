## Informe d’avaluació del sistema de seguiment del Projecte RSM

**Projecte:** Casa RSM – Raval de Santa Magdalena, 30, Vilanova i la Geltrú  
**Data de l’informe:** març 2026  
**Abast:** Revisió del sistema de documents, dashboards i scripts de suport per al projecte de reforma integral (PB, PE, interiorisme i control tècnic).

---

## 1. Objectiu de l’informe

Aquest informe sintetitza una anàlisi externa del conjunt d’eines i documents que has creat per gestionar la Casa RSM:

- Estructura de dashboards (`index.html`, `PORTAL_SIMULACIONS_RSM.html`, `PROPOSTA_INTERIORISME_RSM.html`, `view.html`).
- Documentació estratègica i tècnica (`Dossier_Plantejament_PE_Promotor.md`, informes temàtics de PE, informes d’anàlisi PB, estudis d’interiorisme).
- Scripts d’auditoria (`scripts/orchestrator.py`, verificadors d’habitabilitat i accessibilitat).

L’objectiu és:

- **Validar fortaleses** del sistema, tant des del punt de vista d’arquitectura i interiorisme com de control tècnic.
- **Detectar riscos o punts febles**, sobretot en la manera com un tercer (arquitecte, enginyer, tècnic municipal) pot llegir i entendre tot aquest material.
- **Proposar millores concretes** perquè el sistema sigui més clar, jeràrquic i útil al llarg de tot el cicle: PB → PE → obra.

---

## 2. Resum del sistema actual

### 2.1 Capes principals

1. **Dashboard principal (`index.html`)**
   - Vista **PB**: mostra KPIs d’EnerPHit i Normativa VNG, enllaça a `Informe_Analisi_PB_RSM_V1.md` i al resum del sistema de suport PB.
   - Vista **PE**: targeta central pel `Dossier_Plantejament_PE_Promotor.md` i accés ràpid als informes temàtics (instal·lacions, domòtica, cuina, paviments, banys, acabats, ascensor, fusteries, escales, tancaments interiors).
   - Vista **Visió/Conceptes**: integra interiorisme, sostenibilitat, benestar i dimensió familiar amb passarel·les a estudis específics (aigua, vegetació, il·luminació tàctica, domòtica, etc.).

2. **Portal visual de simulacions**
   - `PORTAL_SIMULACIONS_RSM.html`: selector d’espais per planta (PB, P1, P2, sotacoberta, exterior) amb filtres.
   - `PROPOSTA_INTERIORISME_RSM.html`: comparatives abans/després per façana, vestíbul, estudi PB, pati, cuina-menjador, sala, distribuidor P2, dormitori principal, bany principal, escala i variants cromàtiques.

3. **Visor de documents (`view.html`)**
   - Carrega fitxers `.md` i `.txt` tant per HTTP com en mode local (`file://`), amb maquetació cuidada.
   - Permet llegir fàcilment informes llargs sense sortir de l’ecosistema RSM.

4. **Bloc d’anàlisi tècnica PB**
   - `scripts/orchestrator.py`:
     - Llegeix PDFs i Excel del PB (`docs/PB/V1`).
     - Aplica regles definides a `config/audit_rules.yaml`.
     - Genera informe (`Informe_Analisi_PB_RSM_V1.md`).
     - Actualitza KPIs i alguns textos al dashboard (`index.html`).
   - Scripts auxiliars:
     - `check_habitability.py`: cerca referències al Decret 141/2012 i criteris de flexibilitat d’habitabilitat.
     - `check_accessibility.py`: escaneja accessibilitat (itinerari practicable, ascensor, rampes, cercles de gir, etc.).

5. **Bloc PE i interiorisme**
   - `docs/PE/Dossier_Plantejament_PE_Promotor.md`: peça mestra de criteris del promotor per al PE (envolupant, clima i energia, domòtica, interiorisme, il·luminació, paviments, escales, ascensor, banys i cuina).
   - Informes temàtics en `docs/PE/Documents_Treball/`:
     - Clima i energia, domòtica, cuina, revestiments interiors, il·luminació, banys, paviments, ascensor, fusteries exteriors, escales, tancaments interiors, acabats de façana i sistemes.
   - Estudis de visió i experiència:
     - `ESTUDI_AVANCAT_INTERIORISME_RSM.md`, estudis sobre gestió d’aigua, vegetació, bioclimàtica, il·luminació tàctica, habitatge intergeneracional, etc.

---

## 3. Fortaleses principals

### 3.1 Estructura per fases molt ben pensada

- **Separació neta PB / PE / Visió** al dashboard:
  - PB: control de base normativa i estàndard EnerPHit.
  - PE: zona de treball i criteris del promotor per a l’arquitecte.
  - Visió: traducció de la tècnica a experiència d’usuari i interiorisme.
- Això reflecteix una cultura de projecte madura: es respecta la seqüència lògica i es dona a cada fase la seva eina específica.

### 3.2 Connexió profunda entre interiorisme i tècnica

- Els informes d’interiorisme i acabats no són només estètics; incorporen:
  - **Requisits Passivhaus/EnerPHit** (hermeticitat, VMC, gruixos i materials).
  - **Salut i benestar** (pintures minerals, il·luminació rasant, acústica, ergonomia).
  - **Domòtica DIY** (Home Assistant, escenes, sensors i integració AV).
- El resultat és un llenguatge molt coherent: materials, colors i llum estan alineats amb la física de l’edifici i l’ús quotidià.

### 3.3 Motor d’auditoria tècnica avançat per a PB

- `orchestrator.py` i els seus informes:
  - Controlen **aïllaments**, **habitabilitat**, **accessibilitat**, **urbanisme VNG** i **finances (CEE, estalvi >30%)**.
  - Generen un informe entenedor en `.md` i actualitzen KPIs al dashboard.
- L’enfoc és intel·ligent:
  - Primer mira Excel d’amidaments; si no hi ha prou dades, fa “fallback” a text del PB.
  - És paramètric (configurable via `audit_rules.yaml`) i adaptable a altres versions del projecte.

### 3.4 Interfície pròpia de “bessó digital” del projecte

- El conjunt `index.html` + `PORTAL_SIMULACIONS_RSM.html` + `PROPOSTA_INTERIORISME_RSM.html` + `view.html` funciona com un **bessó digital del projecte**, local-first i privat.
- Per un promotor/arquitecte és una eina molt superior a un simple paquet de PDFs:
  - Navegació per espais amb simulacions abans/després.
  - Enllaços directes a documents tècnics rellevants per cada tema.
  - Control visual de l’estat del PB i del sistema de suport.

---

## 4. Punts febles i riscos detectats

### 4.1 Densitat informativa elevada per a tercers

- Per a tu, el sistema és clar; però per a un arquitecte que entra per primer cop:
  - Hi ha molts informes llargs amb **nivell d’abstracció alt** i força repeticions parcials (clima, VMC, EnerPHit, VNG) entre PB, anàlisi PB, Dossier PE i informes temàtics.
  - Falta una **peça de síntesi molt curta** que expliqui en 2–4 pàgines “qui és la Casa RSM”, quins són els seus objectius i quins són els límits de joc (pressupost, rangs de qualitat, no negociables).
- Risc: el professional pot sentir que necessita massa temps per “desxifrar” el teu ecosistema i això pot rebaixar la seva implicació o generar malentesos.

### 4.2 Barreja entre criteris i solucions tancades

- En molts informes hi ha:
  - Criteris de fons molt bons (salut interior, durabilitat, manteniment, coherència històrica).
  - Barrejats amb **solucions i marques concretes** (Bulthaup, Santos, Neff, Laser TV concret, RALs molt específics, etc.).
- Sovint no es distingeix clarament:
  - Què és **no negociable** (p.ex. “no PVC a façana VNG”, “cal VMC”, “domòtica local-first, no núvol”).
  - Què és simplement **preferència forta o exemple** (p.ex. opcions de marques, models d’electrodomèstics).
- Risc: l’arquitecte pot percebre que rep “un projecte fet” en lloc d’un **brief de criteris obert**, i això pot dificultar la col·laboració creativa.

### 4.3 Traçabilitat parcial per espai

- Les simulacions visuals donen una lectura excel·lent **per estança**, però la documentació escrita està més organitzada **per temes** (energia, paviments, banys, cuina…) que no pas per espais.
- Això fa que, si algú vol revisar només “Sala P1” o “Suite P2”:
  - Hagi de saltar entre diversos informes (interiorisme, il·luminació, paviments, domòtica, etc.) per reconstruir el paquet complet de decisions.
- Risc: en fase de PE i, sobretot, en obra, aquesta dispersió pot generar omissions o incoherències puntuals en espais concrets.

### 4.4 Sistema d’auditoria molt focalitzat en PB i poc preparat per PE/obra

- Ara mateix, el motor d’auditoria:
  - Està clarament orientat al **Projecte Bàsic** i a la seva coherència documental.
  - No hi ha (encara) un equivalent específic per **PE** ni una versió resumida per **control d’obra**.
- Risc:
  - Part dels riscos que ara controles bé en PB (EnerPHit, VMC, urbanisme, accessibilitat, ajuts) podrien tornar a aparèixer en forma de desviacions al PE o a l’obra si no hi ha un check final similar.

---

## 5. Propostes de millora estructurals

### 5.1 Crear un “Brief Executiu PE” molt sintètic

**Objectiu:** donar a l’arquitecte i a qualsevol tercer una entrada ràpida i amable al projecte.

**Format suggerit:** document nou en `.md` (per ex. `BRIEF_EXECUTIU_PE_RSM.md`) amb 4 blocs:

1. **Visió general (1 pàgina)**
   - ADN tècnic (aprox. EnerPHit, salut, confort acústic).
   - ADN històric (elements de 1986 que es volen reinterpretar).
   - ADN artístic (paleta de color, concepte “Sala Viva”, Laser TV).

2. **Resum tècnic (1 pàgina)**
   - Estratègia de clima i VMC triada (opció Aire-Aire + aerotermo ACS, ubicació d’equips, ruta de conductes).
   - Estratègia fotovoltaica i VE (planta, inversor, integració domòtica).
   - Accessibilitat i ascensor (itinerari, reserva, model desitjat).

3. **Resum d’interiorisme i materials (1 pàgina)**
   - Paleta global (parets/sostres, paviments per planta, fusteries).
   - Filosofia d’il·luminació (indirecta, carrils, escenes).
   - Dues o tres imatges clau (façana, sala, suite) amb notes breus.

4. **Prioritats i límits (1 pàgina)**
   - No negociables.
   - Rang de qualitat (nivell 2 per cuina, paviments, banys…).
   - Franges de pressupost orientatiu per grans capítols (on sigui possible).

Aquest brief es pot enllaçar des de la targeta PE del dashboard com a **punt d’entrada oficial** per a qualsevol col·laborador.

### 5.2 Distingir explícitament entre “No negociable / Recomanat / Obert”

Afegir al final de cada informe temàtic (cuina, revestiments, clima, banys, etc.) una **taula de síntesi de prioritat**, per exemple:

- **No negociable**
  - Ex.: VMC amb recuperador, Ausència de PVC en fusteria exterior, SATE transpirable, domòtica amb control local, etc.
- **Molt recomanat**
  - Ex.: sòcols enrasats, campana recirculació específica Passivhaus, determinat nivell de marques (nivell 2), determinats colors RAL.
- **Obert / Exemple**
  - Ex.: marques concretes, sèries exactes de producte, models específics de Laser TV o electrodomèstics.

Això facilita la feina a l’arquitecte: pot mantenir intactes els punts durs i, alhora, proposar alternatives on hi ha marge.

### 5.3 Fitxes per espais que creuin interiorisme, normativa i tècnica

Crear un document nou (per ex. `FITXES_ESPAIS_CASA_RSM.md`) amb una fitxa per a cada espai clau:

- Vestíbul PB  
- Estudi PB / futur dormitori accessible  
- Pati bioclimàtic  
- Cuina-menjador P1  
- Sala P1  
- Distribuidor-biblioteca P2  
- Dormitori principal P2  
- Dormitori 1 P2  
- Banys (P1/P2)  
- Sotacoberta / refugi

**Per cada fitxa:**

- **Ús i sensació desitjada** (3-4 línies).
- **Materials i acabats clau** (parets, paviment, fusteries vistes).
- **Llum i escena domòtica principal**.
- **Requisits normatius/funcionals específics** (alçades, VMC, accessibilitat, ventilació, etc.).
- **Punts no negociables** per aquell espai.

Aquestes fitxes es poden:

- Enllaçar des del portal de simulacions (botó “Fitxa tècnica de l’espai”).
- Utilitzar en reunions de PE i d’obra com a guia ràpida per no perdre cap detall important.

### 5.4 Fer més explícit el significat dels KPIs al dashboard

Al bloc PB de `index.html`, afegir:

- Una breu **llegenda** sota els KPIs:
  - “100% = cap alerta a les regles auditades (EnerPHit/Normativa)”.
  - Explicitar que **no és un càlcul PHPP** ni una certificació, sinó una mesura de completitud i claredat documental.
- Una línia amb **“Darrera auditoria PB: versió i data”** (ex.: “PB_RSM_V1 – 16/02/2026”), que es pot fer sortir directament des d’`orchestrator.py` en actualitzar el dashboard.

Això et permet usar aquests percentatges amb confiança com a eina de diàleg, sense malentesos.

### 5.5 Estendre l’auditoria a PE i preparar un checklist d’obra

1. **Auditoria PE**
   - Crear una variació de `orchestrator.py` o un nou script (per exemple `orchestrator_pe.py`) que:
     - No només miri PB, sinó també el **PE lliurat per l’arquitecte** (PDF + amidaments).
     - Verifiqui que els grans criteris del `Dossier_Plantejament_PE_Promotor.md` queden recollits a:
       - Memòria i plecs.
       - Plànols de detalls i instal·lacions.
       - Amidaments (paviments, fusteries, VMC, etc.).

2. **Checklist d’obra**
   - Crear un `.md` del tipus `CHECKLIST_OBRA_RSM.md`, amb ítems agrupats per capítol:
     - Envolupant i SATE.
     - Fusteries exteriors i proteccions solars.
     - Sistemes de clima, VMC i fotovoltaica.
     - Paviments per planta i escales.
     - Banys i cuina.
     - Domòtica i preinstal·lacions (VE, dades, sensors).
   - Pensat perquè es pugui imprimir o consultar al mòbil durant obra i anar marcant complerts/no complerts.

### 5.6 Separar la “biblioteca de referències” del nucli del briefing

Per rebaixar soroll en els documents troncals:

- Crear una carpeta o document `BIBLIOTECA_REFERENCIES_RSM.md` on agrupar:
  - Taules de marques, gammes i models (cuina, electrodomèstics, Laser TV, mobiliari, pintures).
  - Llistes detallades de botigues i recursos online.
  - Detalls avançats de domòtica DIY (integracions específiques d’HA, protocols, etc.).
- Als informes operatius (cuina, interiorisme, clima) deixar només:
  - Conclusions.
  - Rang de nivell/qualitat recomanat.
  - Un parell de referències a tall d’exemple (amb enllaç a la biblioteca per qui ho vulgui aprofundir).

---

## 6. Recomanacions de següent pas

1. **Redactar el “Brief Executiu PE”** i col·locar-lo com a peça central de la vista PE del dashboard.
2. **Crear les fitxes per espais** amb la lògica descrita i enllaçar-les des del portal de simulacions.
3. **Afegir la llegenda i la data d’auditoria als KPIs de PB** per fer-los autoexplicatius.
4. **Planificar una extensió de l’auditoria cap al PE** (encara que inicialment sigui manual) i començar a esbossar el `CHECKLIST_OBRA_RSM.md`.
5. **Reorganitzar els continguts més “frikis” de marques i tecnologia** en una biblioteca de referències separada, deixant els informes troncals més nets i fàcils de digerir.

Amb aquestes millores, el que ja és un sistema molt potent es converteix en una eina encara més clara i col·laborativa, preparada perquè qualsevol tècnic que s’hi incorpori entengui ràpidament la Casa RSM i pugui sumar-hi valor sense perdre’s en la quantitat d’informació disponible.

