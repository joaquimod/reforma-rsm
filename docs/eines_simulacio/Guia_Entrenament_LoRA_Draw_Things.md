# Guia d'Entrenament de LoRAs Locals amb Draw Things

Aquest document és una guia de referència i llista de comprovació (checklist) per entrenar models LoRA propietaris (per a mobles específics, estils o textures de la Casa RSM) de forma local al Mac utilitzant Draw Things.

## Fase 1: Preparació del Dataset

- [ ] **Recopilació:** Reunir entre 15 i 30 fotografies de gran qualitat de l'objecte o estil desitjat. Cal assegurar diferents angles, fons i il·luminacions si és un objecte 3D (ex: cadira).
- [ ] **Retall:** Enquadrar les fotografies en format quadrat (1:1).
  - SD 1.5: 512x512 píxels.
  - SDXL: 1024x1024 píxels.
- [ ] **Emmagatzematge:** Guardar totes les imatges preparades en una única carpeta dedicada (ex: `Dataset_Cadira_RSM`).

## Fase 2: Configuració a Draw Things

- [ ] Obrir Draw Things i anar a **Manage Models** (Clica el nom del model a dalt a l'esquerra) o anar a la secció LoRA al panell dret i seleccionar **Train New LoRA...**.
- [ ] **Base Model:** Seleccionar el model base coherent amb el projecte.
  - Recomanat per a Mac estàndard (velocitat i estabilitat): `SD 1.5` (ex: architectureInterior).
  - Recomanat només per a Macs amb +32GB RAM: `SDXL`.
- [ ] **Images Directory:** Seleccionar la carpeta on s'ha guardat el Dataset.
- [ ] **Trigger Word:** Definir una paraula inventada i única (ex: `cadiraRSM`). *Anotar-la, serà imprescindible per invocar el model!*
- [ ] **Class Word:** Definir la paraula genèrica que descriu l'objecte (ex: `chair`, `bed`, `texture`, `interior architecture`).

## Fase 3: Paràmetres Tècnics Avançats

- [ ] **Repeats:** Establir entre `10` i `15` repeticions.
- [ ] **Epochs:** Ajustar aquest número perquè el càlcul automàtic d'Steps Totals quedi aproximadament entre `1000` i `1500` passos.
- [ ] **Learning Rate:** Mantenir per defecte (`1e-4` o similar) per evitar "cremar" el model.
- [ ] **Resolution:** Establir a `512` (SD 1.5) o `1024` (SDXL), d'acord amb el retall de la Fase 1.

## Fase 4: Execució i Desat

- [ ] Prémer **Start Training** i deixar el Mac treballar sense interrupcions pesades. El procés pot trigar de 10 minuts a 1 hora segons el xip (M1/M2/M3).
- [ ] Verificar que el nou LoRA apareix automàticament a la llista de LoRAs disponibles a Draw Things en finalitzar.

## Fase 5: Validació i Ús al Projecte RSM

- [ ] A la pestanya LoRA de Draw Things, afegir el model recent entrenat.
- [ ] **Pes (Weight) Inicial:** Establir a `0.7` o `0.8` (no a 1.0 per evitar saturació).
- [ ] **Prompt de prova:** Escriure un prompt descriptiu que inclogui obligatòriament la **Trigger Word** triada a la Fase 2.
- [ ] **Ajust de precisió:**
  - Si l'objecte surt deformat o es menja l'escena: baixar el pes a `0.5`.
  - Si l'objecte gairebé no s'assembla a la realitat: pujar el pes a `0.9` o `1.0`.
