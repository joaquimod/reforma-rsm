# Espais de la Casa RSM 2026

Les següents taules resumeixen les característiques dels espais i els equipaments per a la definició del Projecte Executiu i el futur manteniment de l'habitatge, organitzat per cotes arquitectòniques.

---

## 1. Planta Baixa (PB)
**[[P 0 RSM.png|Plànol Planta Baixa]]**

```dataview
TABLE 
    superficie_m2 as "m2",
    paviment as "Paviment",
    funcio as "Funció principal", 
    mobiliari_equipament as "Mobiliari / Equipament",
    il_luminacio as "Il·luminació",
    clima as "Clima / VMC",
    proposta_mitjana as "Gama Mitjana",
    proposta_alta as "Gama Alta"
FROM ""
WHERE (planta = "PB" OR planta = "0") AND file.name != this.file.name
SORT file.name ASC
```

---

## 2. Planta Primera (P1)
**[[P 1 RSM.png|Plànol Planta Primera]]**

```dataview
TABLE 
    superficie_m2 as "m2",
    paviment as "Paviment",
    funcio as "Funció principal", 
    mobiliari_equipament as "Mobiliari / Equipament",
    clima as "Clima / VMC",
    proposta_mitjana as "Gama Mitjana",
    proposta_alta as "Gama Alta"
FROM ""
WHERE planta = "P1" AND file.name != this.file.name
SORT file.name ASC
```

---

## 3. Planta Segona (P2)
**[[P 2 RSM.png|Plànol Planta Segona]]**

```dataview
TABLE 
    superficie_m2 as "m2",
    paviment as "Paviment",
    funcio as "Funció principal", 
    mobiliari_equipament as "Mobiliari / Equipament",
    clima as "Clima / VMC",
    proposta_mitjana as "Gama Mitjana",
    proposta_alta as "Gama Alta"
FROM ""
WHERE planta = "P2" AND file.name != this.file.name
SORT file.name ASC
```

---

## 4. Sotacoberta i Coberta (PSC/PC)
**[[P Sotacoberta RSM.png|Plànol Planta Sotacoberta]]**  
**[[P Coberta RSM.png|Plànol Planta Coberta]]**

```dataview
TABLE 
    planta as "Planta",
    superficie_m2 as "m2",
    paviment as "Paviment",
    funcio as "Funció técnica", 
    mobiliari_equipament as "Instal·lacions",
    proposta_mitjana as "Gama Mitjana",
    proposta_alta as "Gama Alta"
FROM ""
WHERE (planta = "PSC" OR planta = "PC" OR planta = "C") AND file.name != this.file.name
SORT planta DESC, file.name ASC
```

---
## Resum de partides tècniques (Estst de materials)
Aquestes taules agrupen els espais segons els acabats i sistemes per a facilitar la gestió de pressupostos i obra.

### A. Quadre de paviments
```dataview
TABLE map(rows, (r) => "**" + r.file.link + "**<br>▫️ *Mitjana:* " + choice(r.proposta_mitjana, r.proposta_mitjana, "Per definir") + "<br>▫️ *Alta:* " + choice(r.proposta_alta, r.proposta_alta, "Per definir")) as "Detall de l'Espai i Equipament"
FROM ""
WHERE paviment != null AND file.name != this.file.name
GROUP BY paviment
```

### B. Quadre d'acabats de paret
```dataview
TABLE map(rows, (r) => "**" + r.file.link + "**<br>▫️ *Mitjana:* " + choice(r.proposta_mitjana, r.proposta_mitjana, "Per definir") + "<br>▫️ *Alta:* " + choice(r.proposta_alta, r.proposta_alta, "Per definir")) as "Detall de l'Espai i Equipament"
FROM ""
WHERE color_paret != null AND file.name != this.file.name
GROUP BY color_paret
```

### C. Quadre de climatització i VMC
```dataview
TABLE map(rows, (r) => "**" + r.file.link + "**<br>▫️ *Mitjana:* " + choice(r.proposta_mitjana, r.proposta_mitjana, "Per definir") + "<br>▫️ *Alta:* " + choice(r.proposta_alta, r.proposta_alta, "Per definir")) as "Detall de l'Espai i Equipament"
FROM ""
WHERE clima != null AND file.name != this.file.name
GROUP BY clima
```

### D. Quadre de portes interiors
```dataview
TABLE map(rows, (r) => "**" + r.file.link + "**<br>▫️ *Mitjana:* " + choice(r.proposta_mitjana, r.proposta_mitjana, "Per definir") + "<br>▫️ *Alta:* " + choice(r.proposta_alta, r.proposta_alta, "Per definir")) as "Detall de l'Espai i Equipament"
FROM ""
WHERE portes_interiors != null AND file.name != this.file.name
GROUP BY portes_interiors
```

### E. Quadre d'il·luminació
```dataview
TABLE map(rows, (r) => "**" + r.file.link + "**<br>▫️ *Mitjana:* " + choice(r.proposta_mitjana, r.proposta_mitjana, "Per definir") + "<br>▫️ *Alta:* " + choice(r.proposta_alta, r.proposta_alta, "Per definir")) as "Detall de l'Espai i Equipament"
FROM ""
WHERE il_luminacio != null AND file.name != this.file.name
GROUP BY il_luminacio
```

### F. Quadre de portes exteriors
```dataview
TABLE map(rows, (r) => "**" + r.file.link + "**<br>▫️ *Mitjana:* " + choice(r.proposta_mitjana, r.proposta_mitjana, "Per definir") + "<br>▫️ *Alta:* " + choice(r.proposta_alta, r.proposta_alta, "Per definir")) as "Detall de l'Espai i Equipament"
FROM ""
WHERE portes_exteriors != null AND file.name != this.file.name
GROUP BY portes_exteriors
```

### G. Quadre de finestres
```dataview
TABLE map(rows, (r) => "**" + r.file.link + "**<br>▫️ *Mitjana:* " + choice(r.proposta_mitjana, r.proposta_mitjana, "Per definir") + "<br>▫️ *Alta:* " + choice(r.proposta_alta, r.proposta_alta, "Per definir")) as "Detall de l'Espai i Equipament"
FROM ""
WHERE finestres != null AND file.name != this.file.name
GROUP BY finestres
```

---

---
## Instruccions de manteniment del document
*   Les taules s'actualitzen cada vegada que s'obra el document o es fan canvis a les fitxes individuals.
*   Es pot fer clic sobre el nom de cada espai per anar a la seva fitxa detallada.
