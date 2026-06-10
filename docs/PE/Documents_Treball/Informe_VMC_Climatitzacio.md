# Sinergia del sistema VMC amb la climatització

Aquest informe analitza la interacció i integració del sistema de ventilació mecànica controlada (VMC) de doble flux amb recuperació de calor amb els sistemes de climatització (aire condicionat i bomba de calor) previstos per a la Casa RSM. L'objectiu és establir les bases tècniques per al Projecte Executiu (PE) que garanteixin el màxim confort i la màxima eficiència energètica.

---

## 1. Diferenciació de rols i acoblament tècnic

Per dissenyar correctament les instal·lacions, cal definir amb claredat el propòsit de cada sistema, evitant interferències i aprofitant-ne el funcionament combinat:

*   **Sistema de climatització:** Té com a funció principal el control de la temperatura interior sensible i latent (calor i fred) per mantenir les estances en el rang de confort (normalment entre 21 °C a l'hivern i 24 °C a l'estiu). Treballa en circuit tancat (recirculació d'aire interior de cada zona).
*   **Sistema VMC:** Té com a única funció garantir la qualitat de l'aire interior mitjançant la renovació continuada, extreient l'aire viciat (amb alts nivells de CO2, humitat, COVs i olors) dels banys i la cuina, i impulsant aire fresc i filtrat de l'exterior cap als dormitoris i la sala d'estar. Treballa en circuit obert de doble flux.

L'acoblament tècnic entre ambdós es produeix a l'intercanviador de calor de la unitat VMC, on el corrent d'extracció i el d'impulsió intercanvien energia tèrmica sense barrejar els fluxos físics d'aire.

---

## 2. Càlculs i rendiment del recuperador de calor

El cor del sistema VMC és el recuperador de plaques a contraflux. Per a la Casa RSM, amb un volum d'aire de disseny aproximat de 450 m³ i un cabal de ventilació nominal de 150 m³/h (equivalent a unes 0,33 renovacions de l'aire per hora, d'acord amb el CTE DB-HS3 i els criteris EnerPHit), el rendiment tèrmic del sistema s'avalua mitjançant les següents relacions:

### 2.1. Càlcul de la potència tèrmica recuperada

La potència tèrmica sensible recuperada (Qr) expressada en watts es calcula com:

`Qr = m * Cp * (Tint - Text) * η`

On:
*   `Qr` és la potència sensible recuperada en watts (W).
*   `m` és el cabal massic d'aire (per a 150 m³/h, m ≈ 0,05 kg/s).
*   `Cp` és la calor específica de l'aire (Cp ≈ 1005 J/kg·K).
*   `Tint` i `Text` són les temperatures interiors i exteriors de l'aire.
*   `η` és l'eficiència tèrmica del recuperador de calor (per a equips com Zehnder ComfoAir Q, η ≥ 90% o 0,90).

### 2.2. Exemple de funcionament en condicions extremes a Vilanova i la Geltrú

#### Cas d'hivern (Temperatura exterior 5 °C, interior 21 °C):
Sense VMC, la ventilació natural introduiria aire directament a 5 °C, requerint que la bomba de calor escalfés aquest aire fins a 21 °C.
*   Amb VMC (η = 90%):
    `Timpulsió = Text + η * (Tint - Text) = 5 + 0,90 * (21 - 5) = 19,4 °C`
*   L'aire net de l'exterior s'introdueix a les habitacions a 19,4 °C, pràcticament a temperatura de confort, minimitzant el salt tèrmic que ha de cobrir la climatització.

#### Cas d'estiu (Temperatura exterior 35 °C, interior 24 °C):
Sense VMC, la ventilació natural introduiria aire a 35 °C amb una càrrega de xafogor elevada.
*   Amb VMC (η = 90%):
    `Timpulsió = Text - η * (Text - Tint) = 35 - 0,90 * (35 - 24) = 25,1 °C`
*   L'aire de ventilació s'introdueix a només 25,1 °C, evitant sobreescalfar la casa i descarregant de treball les unitats de climatització per conductes.

---

## 3. Comportament estacional i el bypass d'estiu (Free-cooling)

El sistema VMC disposa d'un sistema de regulació automatitzat que ajusta el seu comportament segons les diferències de temperatura interior i exterior:

### 3.1. Hivern i temporades fredes
El bypass roman tancat per assegurar que el 100% de l'aire d'extracció cedeixi la seva calor a l'aire fred d'admissió. Això manté la inèrcia tèrmica dels paraments i redueix el consum elèctric de la bomba de calor de climatització.

### 3.2. Estiu i períodes de xafor
Durant el dia, el bypass es manté tancat per conservar l'aire fred generat per l'aire condicionat (l'aire exterior calent es refreda abans d'entrar). Durant la nit, s'activa l'estratègia de free-cooling:
*   Si la temperatura exterior cau per sota de la interior (per exemple, 20 °C a l'exterior i 25 °C a l'interior) i la temperatura exterior és superior a 15 °C (per evitar refredar en excés), el bypass s'obre automàticament.
*   L'aire fresc de la nit s'impulsa a l'interior de la casa sense intercanviar calor amb l'aire extret, utilitzant el mateix sistema de ventilació per refrigerar passivament l'estructura de la casa sense engegar les màquines de clima.

---

## 4. Control de la humitat i benestar higrotèrmic

El confort tèrmic no depèn exclusivament de la temperatura seca de l'aire, sinó de la humitat relativa. Un nivell d'humitat relativa (HR) d'entre el 40% i el 60% és ideal per evitar problemes respiratoris i minimitzar la sensació tèrmica de xafogor.

*   **Evacuació passiva d'humitat:** La VMC extreu de manera continuada l'aire de les cambres on es genera humitat (banys, cuina i bugaderia). Això evita la condensació superficial en elements estructurals i redueix la xafogor acumulada.
*   **Opcions d'intercanviador entàlpic:** Per a la Casa RSM, en trobar-se en una zona costanera (Vilanova i la Geltrú) amb humitats exteriors estivals molt elevades, es recomana valorar la instal·lació d'un intercanviador entàlpic en lloc del sensible estàndard. L'intercanviador entàlpic és capaç de recuperar tant la calor sensible (temperatura) com la calor latent (humitat), evitant que l'alta humitat exterior de l'estiu saturi l'ambient de la casa, ajudant a mantenir una atmosfera interior molt més seca i confortable.

---

## 5. Criteris d'integració en el Projecte Executiu (PE)

Per al correcte disseny físic i coordinació en els plànols d'instal·lacions del PE, s'han de respectar els següents punts d'integració:

1.  **Independència de xarxes de conductes:** Sota cap concepte s'han d'acoblar físicament els conductes de la VMC amb els conductes de la climatització per conductes (Panasonic). Cada sistema ha de disposar del seu propi traçat de tubs, plenum i reixetes independents per mantenir l'equilibri de pressions i cabals de disseny.
2.  **Ubicació de preses i reixetes:**
    *   Les reixetes d'impulsió de la VMC s'han d'ubicar a l'extrem oposat de les portes de pas a les estances per forçar l'aire a creuar tota l'habitació.
    *   Cal preveure un pas d'aire a les portes interiors (graó de ventilació inferior de 8-10 mm o reixeta de pas acústica) per permetre el lliure retorn de l'aire cap a les reixetes d'extracció dels banys.
3.  **Aïllament dels conductes d'admissió i expulsió:** Els conductes que connecten la màquina VMC amb l'exterior (admissió d'aire net i expulsió d'aire brut) han d'anar totalment aïllats tèrmicament per evitar condensacions a l'espai interior del cel ras i pèrdues de rendiment energètic.
4.  **Manteniment dels filtres:** Un filtre de la VMC brut augmenta la pèrdua de càrrega del sistema, disminuint-ne el cabal i forçant el ventilador a consumir més electricitat. L'accés a la unitat VMC (prevista a la Sala d'Instal·lacions de la Planta Baixa) ha de ser totalment lliure de traves físiques per permetre el manteniment semestral de filtres (ISO ePM1 o F7 d'impulsió per pol·len/partícules, i G4 d'extracció per a pols).

---
*Document tècnic de sinergia entre VMC i climatització per a la Casa RSM.*
