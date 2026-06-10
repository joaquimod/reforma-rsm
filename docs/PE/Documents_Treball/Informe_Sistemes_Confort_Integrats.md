# Informe integrat de climatització, ventilació i domòtica per a la Casa RSM

Aquest document tècnic descriu la sinergia, els mètodes d'integració física i lògica, i els requeriments del Projecte Executiu (PE) per als sistemes de climatització, ventilació mecànica controlada (VMC) de doble flux i domòtica de la Casa RSM a Vilanova i la Geltrú. L'objectiu és aconseguir una gestió local, robusta, eficient i totalment autònoma de la qualitat de l'aire interior i del benestar higrotèrmic.

![Sistemes de confort de la Casa RSM](assets/infografia_sistemes_rsm.png)

---

## 1. Sinergia del sistema VMC amb la climatització

Per dissenyar correctament les instal·lacions, cal definir amb claredat el propòsit de cada sistema, evitant interferències i aprofitant-ne el funcionament combinat:

*   **Sistema de climatització:** Té com a funció principal el control de la temperatura interior sensible i latent (calor i fred) per mantenir les estances en el rang de confort (normalment entre 21 °C a l'hivern i 24 °C a l'estiu). Treballa en circuit tancat mitjançant la recirculació d'aire interior de cada zona.
*   **Sistema VMC:** Té com a única funció garantir la qualitat de l'aire interior mitjançant la renovació continuada, extreient l'aire viciat (amb alts nivells de CO2, humitat, COVs i olors) dels banys i la cuina, i impulsant aire fresc i filtrat de l'exterior cap als dormitoris i la sala d'estar. Treballa en circuit obert de doble flux.

L'acoblament tècnic entre ambdós es produeix a l'intercanviador de calor de la unitat VMC, on el corrent d'extracció i el d'impulsió intercanvien energia tèrmica sense barrejar els fluxos físics d'aire.

---

## 2. Càlculs i rendiment del recuperador de calor

El cor del sistema VMC és el recuperador de plaques a contraflux. Per a la Casa RSM, amb un volum d'aire de disseny aproximat de 450 m³ i un cabal de ventilació nominal de 150 m³/h (equivalent a unes 0,33 renovacions de l'aire per hora, d'acord amb el CTE DB-HS3 i els criteris EnerPHit), el rendiment tèrmic del sistema s'avalua mitjançant les següents relacions:

### 2.1 Càlcul de la potència tèrmica recuperada

La potència tèrmica sensible recuperada (Qr) expressada en watts es calcula com:

`Qr = m * Cp * (Tint - Text) * η`

On:
*   `Qr` és la potència sensible recuperada en watts (W).
*   `m` és el cabal massic d'aire (per a 150 m³/h, m ≈ 0,05 kg/s).
*   `Cp` és la calor específica de l'aire (Cp ≈ 1005 J/kg·K).
*   `Tint` i `Text` són les temperatures interiors i exteriors de l'aire.
*   `η` és l'eficiència tèrmica del recuperador de calor (per a equips com Zehnder ComfoAir Q, η ≥ 90% o 0,90).

### 2.2 Exemple de funcionament en condicions extremes a Vilanova i la Geltrú

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

## 3. Comportament estacional i el bypass d'estiu (free-cooling)

El sistema VMC disposa d'un sistema de regulació automatitzat que ajusta el seu comportament segons les diferències de temperatura interior i exterior:

### 3.1 Hivern i temporades fredes
El bypass roman tancat per assegurar que el 100% de l'aire d'extracció cedeixi la seva calor a l'aire fred d'admissió. Això manté la inèrcia tèrmica dels paraments i redueix el consum elèctric de la bomba de calor de climatització.

### 3.2 Estiu i períodes de calor
Durant el dia, el bypass es manté tancat per conservar l'aire fred generat per l'aire condicionat (l'aire exterior calent es refreda abans d'entrar). Durant la nit, s'activa l'estratègia de free-cooling:
*   Si la temperatura exterior cau per sota de la interior (per exemple, 20 °C a l'exterior i 25 °C a l'interior) i la temperatura exterior és superior a 15 °C (per evitar refredar en excés), el bypass s'obre automàticament.
*   L'aire fresc de la nit s'impulsa a l'interior de la casa sense intercanviar calor amb l'aire extret, utilitzant el mateix sistema de ventilació per refrigerar passivament l'estructura de la casa sense engegar les màquines de clima.

---

## 4. Control de la humitat i benestar higrotèrmic

El confort tèrmic depèn tant de la temperatura seca de l'aire com de la humitat relativa. Un nivell d'humitat relativa (HR) d'entre el 40% i el 60% és ideal per evitar problemes respiratoris i minimitzar la sensació tèrmica de xafogor.

*   **Evacuació passiva d'humitat:** La VMC extreu de manera continuada l'aire de les cambres on es genera humitat (banys, cuina i bugaderia). Això evita la condensació superficial en elements estructurals i redueix la xafogor acumulada.
*   **Opcions d'intercanviador entàlpic:** Per a la Casa RSM, en trobar-se en una zona costanera (Vilanova i la Geltrú) amb humitats exteriors estivals molt elevades, es recomana valorar la instal·lació d'un intercanviador entàlpic en lloc del sensible estàndard. L'intercanviador entàlpic és capaç de recuperar tant la calor sensible (temperatura) com la calor latent (humitat), evitant que l'alta humitat exterior de l'estiu saturi l'ambient de la casa, ajudant a mantenir una atmosfera interior molt més seca i confortable.

---

## 5. Integració física i lògica dels sistemes a la domòtica (Home Assistant)

La integració es dissenya sota el criteri de prioritzar connexions locals directes (Local-First) per garantir el control independent d'internet.

### 5.1 Integració del sistema de climatització Panasonic

Les unitats previstes (CS-Z35UD3EAW per a conductes i CS-Z35ZKEW per a split de paret) disposen de diferents passarel·les per comunicar-se amb Home Assistant:

*   **Interfície local directa CN-CNT (recomanada):** Connexió d'un microcontrolador ESP32 amb convertidor de nivell (5V a 3.3V) directament al port sèrie CN-CNT de la placa mare de les unitats interiors. Es programa amb ESPHome utilitzant el component `panasonic_ac`. Permet un control en temps real sense dependència del núvol.
*   **Integració oficial Panasonic Comfort Cloud:** Mètode basat en el Wi-Fi integrat connectant-se als servidors de Panasonic a internet. Requereix connexió constant a la xarxa externa i està subjecte a la disponibilitat de l'API oficial.
*   **Maquinari professional local Modbus (IntesisBox):** Connexió industrial mitjançant pasarel·la de Modbus TCP. Molt estable per xarxa de cable, però amb un cost elevat per unitat interior.

### 5.2 Integració del recuperador de calor Zehnder ComfoAir Q

*   **Passarel·la de xarxa oficial ComfoConnect LAN C (recomanada):** Mòdul de carril DIN connectat a la VMC per bus físic (ComfoBus) i al switch PoE de xarxa per cable Ethernet. Permet integració total local de lectura de pressions, cabals i temperatures, així com control de velocitats i bypass.
*   **Interfície sèrie DIY per ESP32:** Ús d'un ESP32 amb transceptor RS-485 connectat al port de servei de la VMC, comunicat per ESPHome a través de xarxa local Wi-Fi.
*   **Control analògic-digital Option Box:** Modificació de velocitats mitjançant contactes secs i entrades 0-10V des de relés externs, independent de la xarxa de dades informàtica.

---

## 6. Automatitzacions avançades de confort i estalvi energètic

L'enllaç lògic a través de Home Assistant permet desenvolupar funcionalitats que van més enllà dels termòstats i sensors individuals de cada fabricant:

### 6.1 Gestió dinàmica d'humitat als banys (anticondensacions)
Ús de sensors de resposta ràpida col·locats a la zona de dutxa de cada bany. Si es detecta un augment de la humitat superior al 10% en menys de 2 minuts, s'activa automàticament el mode Boost al 100% de la VMC. Es retorna al cabal nominal quan la humitat cau per sota del 60%.

### 6.2 Renovació de l'aire per CO2 i qualitat ambient
Durant les hores de son nocturn, sensors de CO2 ubicats als capçals dels llits dels dormitoris avaluen la concentració. Si se superen les 800 ppm, el cabal de la VMC s'incrementa automàticament a velocitat 2. Si se superen les 1.100 ppm, s'estableix la velocitat 3. En baixar de 700 ppm, es restableix la velocitat 1 (silenciosa).

### 6.3 Climatització per excedents solars (solar dump)
Coordinació de la producció solar obtinguda per l'inversor i la mesura del comptador Smart Meter. Si es generen excedents superiors a 1.5 kW de manera sostinguda durant el dia, Home Assistant encén les bombes de calor per pre-refredar o pre-escalfar les diferents plantes utilitzant la inèrcia tèrmica dels paraments en les hores de producció gratuïta.

### 6.4 Seguretat d'obertura de fusteries i aturada de màquines
Si algun sensor magnètic de finestra detecta l'obertura continuada durant més de 3 minuts, la climatització d'aquella planta s'apaga de manera automàtica. No es permet tornar-la a engegar fins que tots els tancaments exteriors de la zona estiguin tancats. Així mateix, en cas d'incendi detectat per fum, el sistema atura immediatament la ventilació VMC i obre al màxim les persianes.

---

## 7. Indicadors de seguiment del confort i eficiència a la domòtica

Per al control actiu i l'avaluació contínua de les instal·lacions, es proposa la configuració dels següents indicadors clau (KPIs) en la interfície de Home Assistant:

### 7.1 Confort higrotèrmic sensible i latent
*   **Punt de rosada interior (Dew Point):** Expressat en °C. Per a una zona costanera de clima humit com Vilanova i la Geltrú, el punt de rosada és el millor indicador absolut de la presència de vapor d'aigua. El valor objectiu s'estableix entre 10 °C i 15 °C. Valors superiors a 16 °C activaran alertes o programes de deshumidificació dinàmics.
*   **Diferencial tèrmic entre plantes:** Mesura la diferència de temperatura en temps real entre la Planta Baixa (PB) i la Planta Coberta (PSC) per corregir situacions d'estratificació mitjançant el cabal de ventilació o la programació del clima.
*   **Índex de calor (Humidex):** Indicador calculat per programari que reflecteix la sensació tèrmica real de l'usuari associant la humitat relativa amb la temperatura de bulb sec.

### 7.2 Qualitat ambiental de l'aire (QAI)
*   **Taxa de diòxid de carboni (CO2):** Mesurada en parts per milió (ppm). Permet un diagnòstic de la renovació continuada d'aire als espais. El llindar de confort s'estableix a menys de 800 ppm.
*   **Índex de compostos orgànics volàtils (COVs):** Control del nivell de contaminants aerotransportats a les zones humides (cuines i banys).
*   **Concentració de partícules (PM2.5):** Indicador de la qualitat de l'aire exterior per programar cicles de recirculació interior en cas d'elevada contaminació exterior.

### 7.3 Eficiència i manteniment del sistema VMC
*   **Rendiment instantani del recuperador de calor:** Càlcul matemàtic determinat pel sensor plantilla de Home Assistant comparant les diferències tèrmiques de les sondes d'impulsió, retorn i exterior. S'espera un rendiment de disseny superior al 90%.
*   **Manteniment predictiu de filtres:** Càlcul d'hores acumulades de funcionament de la turbina i monitorització de la pèrdua de càrrega (Pa) per programar la substitució periòdica dels filtres d'aire.

### 7.4 Monitoratge energètic
*   **Rendiment solar dinàmic (Solar Dump Efficiency):** Ràtio de consum directe dels equips de climatització procedent d'excedents fotovoltaics.
*   **Energia recuperada per free-cooling:** Càlcul d'energia tèrmica estalviada a la nit mitjançant el bypass passiu de la VMC.

---

## 8. Infraestructura de xarxes i requeriments per al Projecte Executiu (PE)

Per permetre la integració d'aquestes funcions domòtiques en la fase d'obra, el PE ha de preveure les següents especificacions de cablejat i obra civil:

### 8.1 Topologia de la xarxa vertical
Atesa la configuració de 4 plantes (PB, P1, P2, PSC) i la dificultat de propagació de senyals sense fils a través de forjats de formigó, s'adopta una topologia en arbre:
*   **Rack central:** Armari de 19" ubicat a la Sala d'Instal·lacions (PB), on es centralitza l'escomesa de fibra, switch PoE de distribució, servidor de domòtica local (Home Assistant) i SAI.
*   **Columna vertebral vertical:** Canalització principal mitjançant tub corrugat de Ø40mm que comuniqui verticalment els quadres elèctrics de totes les plantes.
*   **Malla de cobertura Zigbee:** Preveure un mínim de 2 micromòduls alimentats (actuadors de persianes o enllaços elèctrics) per planta per actuar com a repetidors de senyal.

### 8.2 Partides de disseny obligatòries per al pressupost d'obra
1.  **Fil neutre:** Condició obligatòria en totes les caixes de mecanismes d'il·luminació i persianes de l'edifici.
2.  **Caixes de mecanismes de gran profunditat:** Caixes de paret encastades de 60mm de fons mínim en tots els punts d'encès d'il·luminació i persianes.
3.  **Tubs de comunicacions al subquadre:** Canalització de Ø25mm directa des del rack fins a cadascun dels subquadres elèctrics de planta per a monitoratge d'energia.
4.  **Tubs d'accés a fusteries:** Canalització de Ø16/20mm des dels marcs de totes les finestres i portes de façana fins a la caixa de registre elèctric de zona per allotjar sensors magnètics cablejats.
5.  **Preses multimèdia RJ45:** Presa doble Cat6a al darrere de cada televisor i preses simples en punts clau (inversor solar, VMC, climatització de conductes).

---
*Document tècnic unificat de sinergia entre ventilació, climatització i domòtica per al Projecte Executiu de la reforma Casa RSM.*
