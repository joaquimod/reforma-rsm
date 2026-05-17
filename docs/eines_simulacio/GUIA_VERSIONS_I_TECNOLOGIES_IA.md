# Guia de versions i tecnologies d'intel·ligència artificial generativa

Aquesta guia explica les diferències tècniques i els criteris de selecció entre les principals arquitectures de models disponibles per a l'aplicació Draw Things en el context de l'arquitectura.

## Stable Diffusion 1.5 (SD 1.5)
És l'arquitectura més antiga encara en ús massiu, però segueix sent molt rellevant per la seva especialització.

- Resolució nativa: 512x512 píxels.
- Avantatges: és molt ràpida i té la biblioteca més gran de models especialitzats en arquitectura (com el que hem fet servir avui).
- Inconvenients: li costa entendre frases llargues i deforma la imatge si pugem massa la resolució.
- Ús ideal: simulacions ràpides i detalls concrets on necessitem un model molt específic.

## Stable Diffusion XL (SDXL)
És l'estàndard professional actual per a la generació local d'alta qualitat.

- Resolució nativa: 1024x1024 píxels.
- Avantatges: entén molt millor el llenguatge natural i el fotorealisme és superior de forma nativa. És molt més difícil que faci coses estranyes com "portes al sostre".
- Inconvenients: requereix més memòria ram i targeta gràfica que SD 1.5.
- Ús ideal: renders de gran format i imatges que requereixin un realisme fotogràfic total sense gaires retocs.

## Flux (L'estat de l'art)
És el model més potent llançat recentment (per l'equip original de Stable Diffusion).

- Resolució nativa: variable, però excel·lent a qualsevol mida.
- Avantatges: comprensió gairebé perfecta del prompt. Si li demanes tres objectes en un ordre concret, els posarà exactament allà. El realisme de les textures i la il·luminació és imbatible.
- Inconvenients: és molt pesat. En un mac, pot trigar diversos minuts per imatge segons la configuració.
- Ús ideal: quan el prompt és molt complex i necessitem que la ia no s'inventi res fora del que hem escrit.

## Què és un LoRA i com millora la generació
LoRA (Low-Rank Adaptation) és una tecnologia que permet afegir coneixement específic a un model gran sense haver de tornar a entrenar-lo sencer.

- Funció: actua com un filtre d'estil o de contingut. Si el model base sap fer un passadís, el lora l'especialitza en un estil concret (minimalisme japonès, fusta de roure específica, il·luminació nocturna).
- Aplicació en arquitectura: és la millor manera d'injectar materials reals. Podem carregar un lora de porcellànic i un altre de fusta per assegurar-nos que les textures de la casa rsm siguin constants en totes les simulacions.

## Criteris de selecció
Per triar el model adequat en cada moment del projecte rsm, segueix aquests criteris:

1. Per a idees ràpides i proves de materials: SD 1.5 amb models d'interiors (com architectureInterior).
2. Per a renders finals de presentació: SDXL (com Juggernaut XL) per la seva nitidesa i realisme.
3. Per a dissenys molt complexos amb molts elements específics: Flux (si el hardware ho permet).
4. Per a una precisió total de materials: qualsevol dels anteriors combinat amb un lora de materials de construcció.
