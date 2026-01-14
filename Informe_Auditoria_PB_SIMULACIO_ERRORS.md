# Informe d'Auditoria Forense - Casa RSM (SIMULACIO_ERRORS)

## 1. Configuració d'IA
- **Orquestrador:** Antigravity (Local Python Tools)
- **Model Local Confidencial:** gpt-oss-safeguard-20b-mlx (LM Studio)
- **Base de Coneixement:** NotebookLM (Export Normativa Vilanova)

## 2. Punts de Control i Troballes

### [ALTA] ENERPHIT: Gruix d'aïllament (8cm) possiblement insuficient per EnerPHit.
- **Referència:** SATE aïllament exterior poliestirè 8cm gruix
- **Recomanació:** Verificar càlcul U-value amb el model local (LM Studio).

### [ALTA] ENERPHIT: Gruix d'aïllament (10cm) possiblement insuficient per EnerPHit.
- **Referència:** Aïllament de coberta amb llana de roca 10cm
- **Recomanació:** Verificar càlcul U-value amb el model local (LM Studio).

### [ALTA] HABITABILITAT: Superfície de peça (2.1 m2) inferior al mínim legal de 6 m2.
- **Referència:** Excel: N/A
- **Recomanació:** Revisar dimensions de la peça per complir Decret 141/2012.

### [ALTA] HABITABILITAT: Superfície de peça (1 m2) inferior al mínim legal de 6 m2.
- **Referència:** Excel: N/A
- **Recomanació:** Revisar dimensions de la peça per complir Decret 141/2012.

### [CRÍTICA] ACCESSIBILITAT: No es detecta menció a l'ascensor o espai de reserva.
- **Referència:** Anàlisi de text del PDF
- **Recomanació:** La normativa de Vilanova/Habitabilitat requereix itinerari accessible o reserva d'espai (1.60x1.60m).

### [ALTA] FINANCES: No es detecta menció al Certificat Energètic d'Abans de l'obra.
- **Referència:** Anàlisi de text del PB
- **Recomanació:** És obligatori registrar el CEE original a l'ICAEN per accedir a deduccions d'IRPF (fins a 60%) i Next Gen.

### [MITJANA] FINANCES: El projecte no quantifica l'estalvi d'energia primària per a subvencions.
- **Referència:** Anàlisi de text del PB
- **Recomanació:** L'arquitecte ha de preveure un estalvi >30% per assegurar el finançament extern.

## 3. Pendents per a LM Studio (Dades Sensibles)
S'ha generat un fitxer a `output/PROMPT_LM_STUDIO_thermal.txt`. 
Si us plau, processa'l amb el teu model `gpt-oss-safeguard-20b-mlx` per validar la física de l'edifici.
