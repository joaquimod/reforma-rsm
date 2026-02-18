# Gestió Integral i Circular de l'Aigua | Casa RSM 2026

Estratègia per a l'optimització del recurs hídric, control de qualitat i aprofitament pluvial.

## 1. Gestió de l'Aigua de Subministrament (Xarxa Municipal)
L'aigua de Vilanova i la Geltrú es caracteritza per una duresa elevada (presència de calç). Cal implementar mesures per protegir les instal·lacions i millorar l'experiència d'ús.

### Qualitat i Tractament:
- **Descalcificació Centralitzada:** Instal·lació d'un descalcificador d'ions a l'entrada principal. És vital per a:
    - **Benestar:** Protecció de la pell i el cabell a les dutxes (evita la sequedat extrema).
    - **Manteniment:** Elimina les taques de calç en mampares de vidre i superfícies de bany.
    - **Protecció:** Allarga la vida d'electrodomèstics (rentadora, rentaplats) i aixeteria termostàtica.
- **Filtració per a Consum (Osmosi):** Sistema d'osmosi inversa sota la pica de la cuina per eliminar el gust de clor i residus, evitant la compra de plàstic (ampolles).
- **Control de Puresa:** Monitorització via Home Assistant de la conductivitat (TDS) per preveure el canvi de filtres.

### Estalvi Tàctic (Sense Doble Circuit):
- **Aixeteria d'Alta Eficiència:** Instal·lació d'airejadors i vàlvules de reducció de cabal a tots els punts de consum.
- **Dutxa Intel·ligent:** Capçals de dutxa amb sistema de limitació de l'aigua fins que s'arriba a la temperatura desitjada.
- **Electrodomèstics Eficients:** Selecció de rentadora i rentaplats amb certificació mínima A+++ i sensors de càrrega.

## 2. Aprofitament de Recursos Pluvials
La pluja es considera un recurs de "Qualitat Tècnica" per a usos que no requereixen portabilitat.

- **Captació i Emmagatzematge:** Ús dels 55 m² de coberta i la cisterna històrica de 10 m³.
- **Usos:** Reg exclusiu del pati bioclimàtic (assecat segur per a plantes, sense taques de calç a la font) i neteja de paviments exteriors.
- **Manteniment de Qualitat:** 
    - **Filtre de fulles:** Mecànic a l'entrada.
    - **Sifó de sobreeixidor:** Per evitar el retorn d'olors i l'entrada de petits animals.
    - **Decantador de primeres aigües:** Desvia els primers litres de pluja (més bruts) abans d'omplir la cisterna.

## 3. Monitorització i Seguretat (Home Assistant)
- **Detecció de Fugues:** Comptador d'impulsos digital a l'entrada que avisa al mòbil si hi ha un consum anòmal (possibles fuites invisibles).
- **Vàlvula de Tall Remota:** Possibilitat de tancar l'entrada general d'aigua des del Dashboard en cas de marxa prolongada o emergència.
- **Previsió Metereològica:** Coordinació del reg segons el servei Meteorològic de Catalunya (Meteocat) per maximitzar l'estalvi.

---
*Document generat per Antigravity per al Projecte Executiu Casa RSM - Gener 2026*
