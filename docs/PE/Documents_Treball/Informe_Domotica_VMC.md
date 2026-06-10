# Integració de la VMC a la domòtica (Home Assistant)

Aquest informe tècnic descriu els requeriments de connexió, integració i automatització del sistema de ventilació mecànica controlada (VMC) de doble flux amb el sistema de domòtica basat en Home Assistant previst per a la Casa RSM. L'objectiu és aconseguir una gestió local, robusta, eficient i totalment autònoma de la qualitat de l'aire interior.

---

## 1. Mètodes d'integració física i lògica

Per connectar el recuperador de calor (Zehnder ComfoAir Q) amb el servidor central de domòtica, es valoren tres mètodes segons la seva complexitat tècnica, cost i grau de llibertat de control:

### 1.1. Passarel·la de xarxa oficial: Zehnder ComfoConnect LAN C

És el mètode més recomanat per a la fase de Projecte Executiu per la seva fiabilitat de muntatge i certificació.

*   **Connexió física:** Es tracta d'un mòdul DIN que es col·loca al costat de la VMC o al subquadre, connectat a la placa de control per un cable de bus (ComfoBus, 4 fils) i al switch PoE de xarxa per cable Ethernet RJ45.
*   **Integració lògica:** Home Assistant disposa de la integració nativa local **Zehnder ComfoConnect**. Aquesta integració es comunica directament per xarxa local amb el mòdul LAN C (sense passar per cap servidor al núvol).
*   **Lectura i control de variables:**
    *   **Lectura:** Temperatura exterior de disseny, temperatura d'impulsió, cabal d'admissió/extracció (m³/h), percentatge de bypass obert, nivell d'obstrucció dels filtres (pressió i hores acumulades).
    *   **Escriptura:** Canvi de velocitats de ventilació (Absència, Velocitat 1, Velocitat 2, Velocitat 3), activació del mode bypass (free-cooling forçat) o de la ventilació temporal forçada (Boost).

### 1.2. Interfície sèrie DIY: ESP32 amb RS-485/CAN Bus

Aquesta opció, completament de maquinari lliure (Open Source), substitueix la costosa electrònica oficial per un microcontrolador ESP32 de baix cost (mínim 15 €).

*   **Connexió física:** Connexió d'una placa ESP32 amb un transceptor RS-485 o un controlador CAN Bus directament al port RJ12 o RJ45 de servei de la unitat principal.
*   **Integració lògica:** S'instal·la el firmware **ESPHome** o el projecte **ComfoAir-ESP** a l'ESP32. Aquest firmware llegeix directament el protocol sèrie de Zehnder, transmetent les variables a través del protocol natiu d'ESPHome o de missatges MQTT cap al servidor de Home Assistant per xarxa sense fils (Wi-Fi).
*   **Avantatges:** Cost extremadament reduït i llibertat total en el maneig dels paràmetres de baix nivell de la màquina.

### 1.3. Control analògic/digital bàsic: Option Box i Relés

Si es desitja un control independent de la xarxa informàtica, es pot optar per la commutació física de velocitats.

*   **Connexió física:** Ús del mòdul de connexions auxiliars *Zehnder Option Box*, que disposa d'entrades de contactes secs de velocitat i entrades analògiques 0-10V. S'hi connecta un relè múltiple connectat localment (com ara un mòdul Shelly Plus 2PM en mode intermitent o una placa amb ESPHome).
*   **Integració lògica:** Home Assistant actua sobre els relés digitals per tancar els contactes de la màquina, forçant físicament les diferents velocitats de disseny.

---

## 2. Automatitzacions de control higrotèrmic i qualitat de l'aire

La gran virtut d'integrar la VMC a la domòtica és la capacitat de reaccionar a sensors distribuïts per l'habitatge que no formen part de la instal·lació nativa de la màquina.

### 2.1. Gestió dinàmica d'humitat als banys (Anticondensacions)

A diferència dels sensors d'humitat interns de la màquina, que mesuren la humitat global de l'aire al conducte de retorn del plenum, s'utilitzen sensors d'humitat d'alta velocitat Zigbee col·locats a la zona de dutxa de cada bany.

*   **Lògica de control:**
    *   Si la humitat relativa (HR) d'un bany supera el 75% o s'incrementa un 10% en menys de 2 minuts, Home Assistant activa el **mode Boost al 100% de potència** de la VMC.
    *   Quan la humitat es redueix per sota del 60% o el nivell base habitual, la VMC torna al seu mode de funcionament ordinari, eliminant la necessitat de polsadors de bany físics.

### 2.2. Renovació segons la qualitat de l'aire per CO2 i VOCs

En un habitatge altament estanc (criteris Passivhaus / EnerPHit), la taxa de CO2 a les habitacions de nit s'eleva ràpidament si no es ventila bé, provocant pèrdua de confort i mals de cap.

*   **Lògica de control:**
    *   Durant el dia, el cabal de la VMC es manté en velocitat mínima (Absència o Velocitat 1) si no hi ha ocupació.
    *   Durant la nit, sensors de CO2 ubicats al capçal dels llits dels dormitoris avaluen la concentració. Si es superen les **800 ppm** de CO2, s'incrementa la ventilació a Velocitat 2 (nominal); si es superen les **1.100 ppm**, s'incrementa a Velocitat 3. Una vegada que cau per sota de **700 ppm**, s'estableix la Velocitat 1 (silenciosa) per garantir el màxim silenci acústic per al descans.

### 2.3. Optimització estival del free-cooling (Refredament nocturn passiu)

*   **Lògica de control:**
    *   Mitjançant la comparativa de la temperatura interior mitjana de la casa i la temperatura real mesurada pel sensor de façana nord, Home Assistant decideix quan forçar l'obertura del bypass.
    *   Quan es detecta una nit d'estiu fresca (temperatura exterior inferior a la interior per almenys 3 °C) i la temperatura de confort s'ha superat a dins durant el dia, el sistema força l'obertura del bypass i augmenta la ventilació fins al 60% durant les hores fresques de la matinada per refredar l'estructura interior sense consum de climatització actiu.

---

## 3. Requisits per al Projecte Executiu (PE)

Per permetre la integració d'aquestes funcions domòtiques en la fase d'obra, el PE ha de preveure les següents especificacions:

1.  **Presa de dades RJ45 prop de la VMC:** Cal una connexió física RJ45 de Categoria 6a al costat de la ubicació de la màquina VMC (Sala d'Instal·lacions de la Planta Baixa) que connecti directament amb l'armari rack principal.
2.  **Alimentació independent per a la passarel·la:** Reservar espai per a un mòdul de carril DIN al subquadre elèctric de la Planta Baixa per a l'alimentació a 230V de la passarel·la de comunicacions LAN C o l'accessori Option Box.
3.  **Traçat de sensors de fusteria:** Cablejat de sensors d'obertura magnètics a les finestres de planta coberta (PSC) per evitar que la ventilació mecànica forci la renovació d'aire si les finestres del sostre s'obren de forma manual.
4.  **Caixes de mecanismes de gran capacitat:** Garantir que les zones on es preveuen controladors o pantalles d'usuari de la VMC disposin de caixes de 60 mm de fons per allotjar cablejats de dades extres i connexions PoE de paret.

---
*Document de treball per a la integració domòtica de la VMC en Home Assistant.*
