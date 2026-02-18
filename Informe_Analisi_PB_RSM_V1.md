# Informe d'Anàlisi Tècnica - Projecte RSM (V1)

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

## 5. Conclusions i Estratègia del Promotor (16/02/2026)

Després de la revisió automàtica i manual, i la reunió del 14/02, es valida el Projecte Bàsic amb la següent estratègia:

1.  **Definició Gràfica Confirmada:** Tot i l'alerta de text sobre "Aïllaments no especificats", s'ha verificat visualment que estan dibuixats als plànols. S'assumeix com a correcte per a Llicència, però es demana (per correu) que es defineixin per escrit de cara al Pressupost.
2.  **Accessibilitat:** S'identifica que, tot i complir CTE-SUA, falta relat per a ajuts específics. S'ha demanat reforçar-ho a la Memòria incloent l'itinerari practicable i l'ascensor.
3.  **Flexibilitat Normativa:** Per evitar requeriments per alçades/amplades existents, s'ha demanat citar explícitament els criteris de flexibilitat del Decret d'Habitabilitat (Annex 2).

**Decisió:** Enviar correu de validació a l'Arquitecte amb suggeriments de millora, però sense bloquejar l'entrada a l'Ajuntament.
