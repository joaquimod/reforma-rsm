# Procés de simulació del vestíbol: metodologia d'èxit

Aquest document descriu el flux de treball tècnic utilitzat per obtenir la visualització final validada del vestíbol de la Casa RSM mitjançant l'aplicació Draw Things.

## Configuració tècnica del model
Per a la simulació final, s'ha optat per un model especialitzat en arquitectura que ofereix un millor control de les línies rectes i els materials d'interior.

- Model base: architectureInterior_v70.safetensors (SD 1.5).
- Resolució: 512x768 píxels. Aquesta mida és crítica per evitar duplicacions d'elements o errors de perspectiva en models SD 1.5.
- Mostrejador (sampler): DPM++ 2M Karras (o similar d'alta precisió).
- Escala de guia (cfg scale): 7.0 a 8.0.

## Flux de treball pas a pas

### 1. Generació des de zero (text to image)
S'ha abandonat l'ús de la fotografia antiga com a base directa per evitar que la ia heretés les escales i el mosaic antic. Es va generar una imatge completament nova basada en el programa de necessitats: armari de roure, terra de porcellànic gris i parets blanques.

### 2. Estructura dels prompts
L'ordre de les paraules ha estat clau per donar prioritat als materials constructius.

- Prompt positiu: large format light grey technical porcelain tiles floor, minimalist entrance hall, light oak cabinetry on the left, seamless doors, plain white wall on the right, no windows, high-end architectural photography.
- Prompt negatiu: window, window frame, view to the outside, glass pane, stairs, staircase, steps, old furniture, wooden floor, parquet, distorted perspective, extra doors.

### 3. Ajust de simetria (flip)
Degut a la tendència de la ia a invertir els costats, la imatge resultant es va girar horitzontalment mitjançant un editor extern per situar l'armari a l'esquerra, segons el plànol executiu.

### 4. Correcció arquitectònica (inpainting)
Per eliminar curvatures en les parets i assegurar la verticalitat de les arestes:
- Mode: inpainting.
- Màscara: s'han pintat exclusivament les línies de les cantonades i les arestes de les parets.
- Força (denoising strength): 0.4 a 0.5. Aquest valor és el que permet corregir la línia sense canviar el disseny de la paret.
- Prompt de reparació: straight architectural line, perfectly vertical wall edge, sharp detail.

## Conclusions i aprenentatges
- La resolució ha de ser coherent amb la versió del model (SD 1.5 o SDXL) per evitar "al·lucinacions" geomètriques.
- El prompt negatiu és tan important com el positiu per evitar elements existents (com les escales) que la ia tendeix a reproduir per defecte en passadissos.
- L'ús de loras no ha estat necessari en la versió final gràcies a la qualitat del model especialitzat en arquitectura.
