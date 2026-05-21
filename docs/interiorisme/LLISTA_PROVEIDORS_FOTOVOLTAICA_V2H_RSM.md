# Proveïdors de fotovoltaica, bateries i V2H - Casa RSM

Aquesta llista recull els millors fabricants d'equips i empreses instal·ladores especialitzades en energia solar fotovoltaica, sistemes d'emmagatzematge de darrera generació i tecnologia de càrrega bidireccional (V2H).

## 1. Plaques i inversors de rendiment extrem
Marques amb les garanties més extenses (25-40 anys) i la major eficiència per m2 (ideal per a la teulada de Casa RSM).

*   **SunPower (Maxeon)**: [maxeon.com](https://maxeon.com)
    *   Especialitat: Les plaques més eficients del mercat amb garantia de 40 anys. Tecnologia de cèl·lules de contacte posterior.
*   **SolarEdge / Enphase**: [solaredge.com](https://www.solaredge.com) / [enphase.com](https://enphase.com)
    *   Especialitat: Ús d'optimitzadors o microinversors que maximitzen la producció de cada placa individualment (clau si hi ha ombres d'altres edificis o xemeneies).
*   **Victron Energy**: [victronenergy.es](https://www.victronenergy.es)
    *   Especialitat: Inversors d'alta fiabilitat per a sistemes híbrids complexos amb gestió avançada de bateries.

## 2. Acumuladors d'energia (bateries estacionàries)
Acumulació d'energia per utilitzar-la durant la nit o en pics de consum.

*   **Tesla Powerwall**: [tesla.com/powerwall](https://www.tesla.com/powerwall)
    *   Especialitat: Disseny integrat, fàcil instal·lació i una aplicació de gestió molt intuïtiva.
*   **Sonnen**: [sonnen.es](https://sonnen.es)
    *   Especialitat: Bateries intel·ligents alemanyes dissenyades per a la màxima vida útil i gestió comunitària de l'energia.
*   **BYD / Huawei (Luna2000)**: [byd.com](https://www.byd.com) / [huawei.com](https://solar.huawei.com)
    *   Especialitat: Sistemes modulars d'alta tensió amb excel·lent relació qualitat-preu i escalabilitat.

## 3. Càrrega bidireccional i V2H (Vehicle-to-Home)
Sistemes que permeten utilitzar la bateria del cotxe elèctric per alimentar la llar (bidireccionalitat).

*   **Wallbox (Barcelona)**: [wallbox.com](https://wallbox.com)
    *   Seu: Carrer del Foc, 68, Barcelona (Headquarters/Showroom).
    *   Equip Clau: **Wallbox Quasar 2**. Dissenyat a Barcelona, és un dels pocs carregadors bidireccionals domèstics (CCS Combo 2) que permeten el V2H, convertint el cotxe en una mega-bateria per a la casa.
*   **Circutor (BCN - Vallès)**: [circutor.com](https://circutor.com)
    *   Especialitat: Experts en gestió d'energia i sistemes de recàrrega intel·ligents per a infraestructures de doble sentit.

## 4. Requeriments per al funcionament del V2H
Per a poder utilitzar la bateria del vehicle elèctric com a acumulador de la llar de manera segura i eficient, es requereixen una sèrie de condicions tècniques:

### Requeriments del vehicle
1.  **Tecnologia bidireccional nativa (V2H/V2G):** El cotxe ha de disposar del programari i del maquinari de càrrega bidireccional (no n'hi ha prou amb V2L o *Vehicle-to-Load*, que només proporciona corrent altern a un endoll individual per a dispositius externs).
2.  **Protocol ISO 15118-20:** És l'estàndard internacional de comunicació vehicle-infraestructura que permet la bidireccionalitat mitjançant connectors CSS Combo 2 (estàndard europeu) tant en corrent altern (AC) com continu (DC).
3.  **Connector compatible:** Connector CCS Combo 2 (AC/DC combinat) o bé l'històric connector japonès CHAdeMO (pioner en bidireccionalitat però en desús a Europa).

### Requeriments de la llar
1.  **Carregador bidireccional compatible:** Wallbox de corrent altern bidireccional (com el *Mobilize Powerbox Verso*) o de corrent continu bidireccional (com el *Wallbox Quasar 2*).
2.  **Gestor energètic (HEMS):** Un dispositiu al quadre elèctric principal que reguli en quin moment s'utilitza l'energia de la bateria del cotxe per a la casa, evitant sobrepassar el consum contractat.
3.  **Sistema d'aïllament de la xarxa (Anti-islanding):** Un interruptor de tall automàtic homologat que aïlli la casa de la xarxa elèctrica externa en cas de fallada o tall de llum general. Això garanteix que l'energia del vehicle elèctric no flueixi cap a la xarxa de distribució pública, protegint els operaris de la companyia.

### Com funciona
1.  **Fase de càrrega:** El cotxe elèctric es connecta al carregador domèstic i emmagatzema l'energia durant les hores de màxima producció solar (excedents) o en hores vall de tarifa reduïda.
2.  **Fase de descàrrega (alimentació):** En hores de consum punta o a la nit, quan les plaques no generen energia, la instal·lació inverteix el sentit de la càrrega i el vehicle passa a injectar energia cap a la llar a través de la línia de distribució interior, reduint el consum de la xarxa al mínim.

### Avantatges i desavantatges
*   **Avantatges:**
    *   *Estalvi energètic elevat:* Permet minimitzar les compres de llum de la xarxa, reduint la factura mensual un 60-80% si es combina amb plaques solars.
    *   *Energia de reserva (Backup):* Ofereix autonomia elèctrica completa a la llar durant diversos dies en cas de tall del subministrament públic (especialment crític en cases d'alta dependència elèctrica).
    *   *Megabateria de baix cost:* Una bateria de llar típica té 10-15 kWh i costa uns 8.000-10.000 €. La bateria d'un cotxe elèctric mitjà té de 50 a 80 kWh (entre 4 i 6 vegades més capacitat) pel mateix cost que ja hem assumit en comprar el cotxe.
*   **Desavantatges:**
    *   *Inversió inicial en equips:* Els carregadors bidireccionals tenen un cost elevat (~3.000 - 5.000 € segons si són AC o DC) i la instal·lació en el quadre elèctric requereix mà d'obra especialitzada.
    *   *Degradació tèrmica lleugera:* L'ús periòdic per a la llar augmenta el nombre de cicles de càrrega/descàrrega de la bateria del cotxe, tot i que els fabricants imposen límits (ex. aturar el V2H quan la bateria baixa del 20%) per minimitzar l'impacte.
    *   *Dependència del vehicle:* Si el vehicle no es troba estacionat al garatge de la llar, la casa perd la font d'emmagatzematge d'energia.

## 5. Cotxes de gamma mitjana compatibles (subvencionables MOVES III)
Per poder rebre les ajudes del Pla MOVES III a Espanya, el vehicle elèctric ha de tenir un preu de venda al públic inferior a 45.000 € (abans d'IVA). Els models compatibles o preparats per a V2H actualment són:

1.  **Renault 5 E-Tech (bateria de 52 kWh):**
    *   *Preu:* Des de 32.900 € (abans de subvencions). Acollible al MOVES III.
    *   *Tecnologia:* Integra un carregador AC bidireccional d'11 kW de sèrie (la versió de 40 kWh no el porta). Funciona associat al carregador de paret *Mobilize Powerbox Verso* (opció més econòmica perquè la inversió es realitza dins de l'inversor del vehicle).
2.  **Kia EV3 (versions Air i Earth / GT-Line):**
    *   *Preu:* Des de 36.000 € (abans de subvencions). Acollible al MOVES III.
    *   *Tecnologia:* Plataforma E-GMP adaptada amb suport V2H de sèrie per programari (activació gradual en funció del carregador domèstic homologat).
3.  **Volvo EX30:**
    *   *Preu:* Des de 36.000 € (abans de subvencions). Acollible al MOVES III.
    *   *Tecnologia:* Dissenyat des de l'inici per ser "future-ready" per a bidireccionalitat. Disposa de **V2L** a través d'un adaptador físic a la presa Type 2, i el maquinari és compatible amb V2H/V2G en corrent altern (AC) de fins a 11 kW, pendent de futures actualitzacions de programari i de la disponibilitat de carregadors de paret bidireccionals homologats a Espanya. *(Nota: El Volvo EX90 inclou bidireccionalitat completa de sèrie, però queda exclòs del MOVES III en superar els 80.000 €).*
4.  **Hyundai Ioniq 5 / Ioniq 6 (versions d'accés de 58 kWh i 77 kWh):**
    *   *Preu:* Des de 39.000 - 44.000 € (amb descomptes del concessionari, abans de MOVES III). Acollibles.
    *   *Tecnologia:* Suport V2L (Vehicle-to-Load) de 3,6 kW integrat i llest per a V2H DC mitjançant protocol ISO 15118-20 d'alt rendiment.
5.  **Volkswagen ID.3 / Cupra Born (bateria de 77 kWh):**
    *   *Preu:* Al voltant de 40.000 - 43.000 € (versions Pro S / e-Boost 77 kWh). Acollibles.
    *   *Tecnologia:* El maquinari permet la bidireccionalitat DC sota protocol ISO 15118-20 (requereix programari de cotxe v3.5 o superior i instal·lació de carregador domèstic DC compatible de tercers com Hager).
6.  **BYD (Dolphin, Atto 3, Seal):**
    *   *Preu:* Des de 24.000 € (Dolphin) fins a 40.000 € (Seal/Atto 3). Acollibles al MOVES III.
    *   *Tecnologia:* Actualment a Espanya **només admeten V2L (Vehicle-to-Load)** fins a 3,3 kW per subministrar energia a petits aparells mitjançant un adaptador a la presa de càrrega. Les capacitats de V2H/V2G estan en fase de proves de pilot en mercats com el Regne Unit (en col·laboració amb Octopus Energy i Zaptec) i s'espera la seva homologació europea a curt termini, però no estan comercialitzades com a servei domèstic obert a Espanya encara.
7.  **Nissan Leaf (model de liquidació o segona mà):**
    *   *Preu:* Des de 25.000 € (nou) o inferior a 15.000 € (segona mà).
    *   *Tecnologia:* Model històric precursor en V2H. Funciona amb protocol CHAdeMO (requereix carregador DC específic com el Wallbox Quasar 1/2). El connector CHAdeMO està en risc d'obsolescència a Europa en favor del CCS.

## 6. Instal·ladors especialitzats (Barcelona i Garraf)
Empreses amb experiència acreditada en el disseny i muntatge de projectes d'autoconsum avançat i punts de recàrrega.

*   **SolarProfit**: [solarprofit.es](https://www.solarprofit.es) (Llinars del Vallès). Empresa referent amb gran infraestructura de muntatge a tota Catalunya.
*   **Becquel**: [becquel.com](https://becquel.com). Especialistes en el disseny personalitzat de plantes d'autoconsum residencial.
*   **Empreses locals al Garraf**:
    *   **Solman Fotovoltaica (VNG)**: [solman.es](https://solman.es)
    *   **Aura Solar**: [aurasolar.es](https://aurasolar.es)
    *   **Voltaica Garraf**: [voltaicagarraf.com](https://voltaicagarraf.com)

---
*Darrera actualització: 19 de maig de 2026*
