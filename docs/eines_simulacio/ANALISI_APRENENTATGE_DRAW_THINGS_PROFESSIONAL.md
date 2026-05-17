# Anàlisi d'aprenentatge: generació professional amb Draw Things

Aquest document recull la recerca avançada sobre com passar de proves de concepte a renders arquitectònics de precisió constructiva per a la Casa RSM.

## El problema de la literalitat i com resoldre'l
Fins ara, la IA s'ha limitat a pintar a sobre de la foto original o del plànol. El resultat sembla un dibuix perquè el pes del ControlNet és massa alt o només en fem servir un.

### La solució: Multi-ControlNet (stacking)
Draw Things permet apilar guies. Per a la Casa RSM, el workflow professional és:
- Guia 1 (Canny): plànol 2D de l'arquitecte (pes 0.3). Defineix on van els mobles.
- Guia 2 (Depth): foto de l'estat actual (pes 0.6). Defineix la perspectiva i el volum.
- Guia 3 (IP-Adapter): una foto d'una revista que t'agradi (pes 0.4). Defineix l'estil de la llum i els materials.

## Models i extensions crítiques
El model Juggernaut XL és bo, però per a arquitectura necessitem LoRAs (Low-Rank Adaptation). 
- Què és un LoRA? És un fitxer que especialitza la IA.
- LoRAs recomanats: 
    - Modern interior design SDXL
    - Architectural realism / photography
    - Natural lighting / sun shadows

## Tècniques de post-processat (upscaling)
Un render professional no surt directe a la primera. Cal un procés de tiled diffusion o ultimate SD upscale:
1. Generar la base a 1024x1024.
2. Passar-la per un upscaler que afegeixi detalls de textures (porus de la fusta, juntes de les rajoles) en petits trossos per no perdre la geometria.

## Fonts de consulta profunda
Per aprendre de manera autònoma, et recomano seguir aquestes fonts específiques:
1. Draw Things Wiki (Official): drawthings.ai - Secció de Advanced ControlNet.
2. Greg Gant Tutorials: el referent més clar per a usuaris de Mac.
3. Civitai (Architecture Section): per descarregar els LoRAs de materials de construcció reals.

## Propers passos per a la Casa RSM
- Instal·lar el model de ControlNet Depth i IP-Adapter.
- Descarregar un LoRA d'interiors moderns des de Civitai i importar-lo a Draw Things.
- Realitzar una prova de tripla guia (plànol + foto + referència).

---
*Aquest document és el full de ruta per elevar la qualitat visual del Projecte Executiu.*
