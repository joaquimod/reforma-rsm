# Informe d'Anàlisi Tècnica - Projecte RSM (V2)

## 1. Configuració d'IA
- **Orquestrador:** Antigravity (Local Python Tools)
- **Model Local Confidencial:** gpt-oss-safeguard-20b-mlx (LM Studio)
- **Base de Coneixement:** NotebookLM (Export Normativa Vilanova)

## 2. Punts de Control i Troballes

### [ALTA] ENERPHIT: No s'han detectat especificacions clares de gruix d'aïllament al text.
- **Referència:** Anàlisi Text PDF
- **Recomanació:** Assegurar que la Memòria Constructiva defineixi els gruixos d'aïllament (SATE, Trasdossats).

### [ALTA] HABITABILITAT: Possible incompliment d'alçada mínima (2.5m) detectat al text.
- **Referència:** Anàlisi de text del PDF
- **Recomanació:** Verificar en seccions que l'alçada lliure general sigui de 2.5m.

### [MITJANA] ACCESSIBILITAT: No es detecta menció explícita al cercle de gir de 1.2m.
- **Referència:** Anàlisi de text del PDF
- **Recomanació:** Assegurar que davant de portes i dins de cuina/bany practicable es pot inscriure un cercle d'1.20m.

### [ALTA] FINANCES: No es detecta menció al Certificat Energètic d'Abans de l'obra.
- **Referència:** Anàlisi de text del PB
- **Recomanació:** És obligatori registrar el CEE original a l'ICAEN per accedir a deduccions d'IRPF (fins a 60%) i Next Gen.

### [MITJANA] FINANCES: El projecte no quantifica l'estalvi d'energia primària per a subvencions.
- **Referència:** Anàlisi de text del PB
- **Recomanació:** L'arquitecte ha de preveure un estalvi >30% per assegurar el finançament extern.

## 3. Pendents per a LM Studio (Dades Sensibles)
S'ha generat un fitxer a `PROMPT_LM_STUDIO_thermal.txt`. 
Si us plau, processa'l amb el teu model `gpt-oss-safeguard-20b-mlx` per validar la física de l'edifici.
