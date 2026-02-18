---
description: Flux de treball per a l'auditoria del Projecte Bàsic (PB) i posteriors.
---

Aquest workflow automatitza l'extracció de dades dels documents del projecte i la seva comparació amb els criteris de normativa i Passivhaus.

### 1. Preparació de l'entorn (Només la primera vegada)
Crea l'estructura de carpetes per gestionar versions i normativa.
// turbo
```bash
mkdir -p docs/normativa docs/PB/V1 output scripts config
mv pb_llanes.pdf docs/PB/V1/
mv Amidaments_pb_llanes_VALIDAT.xlsx docs/PB/V1/
mv *.py scripts/
```

### 2. Ingestió de Normativa (NotebookLM)
Per no haver de copiar-ho tot cada vegada, exporta els "Summaries" o "Notes" de NotebookLM a fitxers `.md` o `.txt` i guarda'ls a `docs/normativa/`. L'agent els farà servir com a base de coneixement.

### 3. Execució de l'Auditoria
L'agent analitza els documents de la versió especificada i genera un informe preliminar.
// turbo
```bash
python3 scripts/orchestrator.py --version V1
```

### 4. Revisió Confidencial (Opcional - LM Studio)
Si hi ha dades sensibles, l'agent generarà un fitxer `output/PB_V1_sensible.json`. Pots portar aquest fitxer al teu LM Studio local per a una anàlisi privada.

### 5. Generació de l'Informe de Negociació
L'agent consolida totes les troballes en un document final per parlar amb l'arquitecte.
