# Informe tècnic: estratègia integral de climatització i energia

**Data:** 16 de febrer de 2026
**Fase:** Projecte Executiu
**Objectiu:** Definir el sistema de climatització i aigua calenta sanitària (ACS) més eficient per a una rehabilitació Passivhaus, evitant el sobredimensionament i maximitzant l'autoconsum fotovoltaic.

---

## 1. El repte Passivhaus: menys és més

En una casa Passivhaus (demanda < 15 kWh/m²a), les regles del joc canvien respecte a l'obra convencional:
*   **Problema de sobredimensionament:** Si instal·lem màquines potents estàndard, faran cicles curts d'encesa/apagada (*cycling*), reduint la vida útil del compressor i provocant disconfort (pics de fred/calor).
*   **Control d'Humitat:** A l'estiu, amb tanta hermeticitat, el sistema ha de ser capaç de deshumidificar suaument sense congelar els ocupants.
*   **La clau:** Equips amb tecnologia *Inverter* de **molt baixa potència mínima** i modulació fina.

---

## 2. Comparativa de sistemes de climatització

### Opció A: Expansió directa
*   **Configuració:**
    *   **Clima:** Unitat exterior Multi-Split (o VRV Mini) + 2 Unitats interiors de conductes (P1, P2) + 1 Split mural/casset (PB).
    *   **ACS:** Aerotermo independent (Bomba de calor dedicada només per a aigua calenta) de 200-300L.
*   **Avantatges:**
    *   **Zonificació total:** Pots encendre la P1 i tenir la P2 apagada. Resposta molt ràpida (aire).
    *   **Redundància:** Si s'espatlla l'aire condicionat, segueixes tenint aigua calenta (són màquines independents).
    *   **Cost:** Sol ser la opció més econòmica d'instal·lació.
*   **Desavantatges:**
    *   **Ocupació:** Necessites lloc per a **dues unitats exteriors** (o una molt gran) i un termo interior voluminós.
    *   **Confort:** L'aire per conductes pot ressecar l'ambient si no es controla bé.

### Opció B: Aerotèrmia Aire-Aigua (Hidrònica)
*   **Configuració:**
    *   Una sola unitat exterior potent ("Bibloc").
    *   Unitat interior "Nevera" (Hydrokit) que produeix aigua freda/calenta per a tot.
    *   **Clima:** Fancoils de conductes (alimentats per aigua) o Sòl Radiant/Refrescant.
    *   **ACS:** Dipòsit integrat a la unitat interior.
*   **Avantatges:**
    *   **Eficiència:** Aprofita millor la inèrcia tèrmica. COP (rendiment) molt alt.
    *   **Confort:** Si es fa amb Sòl Radiant, és el màxim confort (silenciosíssim). Amb fancoils és similar a l'opció A.
    *   **Estètica:** Només una màquina a coberta.
*   **Desavantatges:**
    *   **Preu:** Més car d'instal·lar (lampisteria de coure/multicapa a tot arreu).
    *   **Averia:** Si falla l'exterior, et quedes sense clima i sense dutxa calenta.
    *   **Inèrcia:** Si és terra radiant, tarda hores a escalfar/refredar (poc àgil per a segona residència o ús discontinu).

**Recomanació:** Donat l'ús i el tipus de reforma, l'**Opció A (Aire-Aire Conductes + ACS Independent)** sembla la més racional per cost/benefici i rapidesa de resposta, *sempre que es dimensionin els equips a la baixa*.

---

## 3. Estratègia d'ubicació d'equips

1.  **Unitat Exterior (El soroll i la vibració):**
    *   **Proposta:** Coberta (Teulada).
    *   **Requisit Crític:** Cal preveure **silent-blocks** d'alta qualitat i, si està sobre un dormitori, una bancada flotant de formigó per evitar que la vibració es transmeti a l'estructura de fusta.
    *   **Pas d'Instal·lacions:** Els tubs frigorífics han de baixar per un celobert o patí tècnic fins als banys de P1/P2 i PB. Aquest patí ha d'estar aïllat acústicament.

2.  **Unitats Interiors (Fals sostre banys):**
    *   Ideal per manteniment (registre accessible).
    *   **Alerta VMC:** El recuperador de calor (ventilació) també sol anar al sostre del bany o safareig. Cal coordinar plànols per no baixar el sostre a 2,10m per culpa de l'encreuament de conductes.

---

## 4. Fotovoltaica i gestió energètica

L'objectiu és "Cost Zero" en factura elèctrica anual.

1.  **Dimensionament Solar:**
    *   No dimensionar només per al consum instantani. Cal **sobredimensionar** el camp solar (omplir la coberta al màxim possible, ex: 3-5 kWp).
    *   **Motiu (Canvi Climàtic):** Els estius seran més tòrrids. Necessitarem més aire condicionat al migdia (quan hi ha sol = gratis).
2.  **Tecnologia de l'Inversor (Clau Domòtica):**
    *   **Inversor Híbrid:** Requisit obligatori per permetre la connexió de bateries físiques en el futur sense canviar d'equip.
    *   **Protocol Obert:** Exigir que l'inversor disposi de comunicació **Modbus TCP o API local** permetre la integració total amb el sistema de control Home Assistant (DIY).
3.  **Emmagatzematge (Bateries):**
    *   Fase Inicial: Ús de **Bateria Virtual** per a la compensació d'excedents.
    *   Previsió Física: Deixar espai lliure a la sala de màquines (aprox. 60x80cm) i canalització preparada per a la instal·lació d'un banc de bateries de liti en segona fase.
4.  **Gestió Intel·ligent:**
    *   L'aerotèrmia d'ACS ha de ser "Smart Grid Ready" per poder forçar l'escalfament de l'aigua durant els pics de producció solar.

---

## 5. Pre-instal·lació per a Vehicle Elèctric (VE)

Previsió per a la càrrega de vehicle elèctric o híbrid endollable al garatge, amb capacitat de gestió intel·ligent de càrrega.

1.  **Infraestructura Elèctrica:**
    *   **Circuit Dedicat:** Tub corrugat de Ø40mm des del quadre principal fins al punt de càrrega al garatge.
    *   **Cablejat:** Secció de **10mm²** per permetre càrregues de fins a 7,4 kW (32A) amb total seguretat.
    *   **Proteccions:** Espai reservat al quadre elèctric per a diferencial de Tipus B (específic per a VE) i proteccions de sobretensions.
2.  **Integració Domòtica (Control d'Excedents):**
    *   **Dades:** Instal·lació de presa **Ethernet (Cat6)** al costat del punt de càrrega.
    *   **Intel·ligència:** El carregador seleccionat en fase d'obra (ex: Wallbox, Tesla Wall Connector, Zappi) ha de ser compatible amb el protocol **OCPP** o disposar d'integració local per a **Home Assistant**.
    *   **Objectiu:** Permetre la "Càrrega Solar" (carregar el cotxe només amb l'energia sobrant de les plaques fotovoltaiques).

---

## 6. Resum de requeriments executius

1.  **Càlcul PHPP:** Exigir càlcul de càrregues tèrmiques específic Passivhaus per no comprar màquines massa grans.
2.  **Sistema:** Validar l'aposta per **Aire-Aire (Conductes) + Aerotermo ACS** per flexibilitat i resposta ràpida.
3.  **VMC:** Confirmar ubicació de la màquina de ventilació (independent del clima) i els seus conductes (diàmetre 160/125mm).
4.  **Fotovoltaica:** Maximitzar la superfície de captació a coberta.
5.  **Aïllament acústic:** Bancada anti-vibratòria a la coberta per a la unitat exterior.
6.  **Vehicle Elèctric:** Infraestructura de 10mm² + Dades Cat6 al garatge.

## 7. Anàlisi econòmica i de manteniment (Estimació 2026)

| Concepte | **Opció A (Aire-Aire + ACS)** | **Opció B (Aire-Aigua + Fancoils)** | **Opció C (Aire-Aigua + Terra Radiant)** |
| :--- | :---: | :---: | :---: |
| **Inversió Inicial (CAPEX)** | **Baixa** (Referència 100%) | **Mitjana** (+40%) | **Alta** (+70%) |
| **Instal·lació** | Ràpida. Tubs frigorífics senzills. | Complexa. Hidràulica, aïllaments, desguassos. | Molt complexa. Obra de paleta (morter) a tot el terra. |
| **Consum (OPEX)** | Molt Baix (Passivhaus) | Molt Baix (COP lleugerament millor) | **Mínim Possible** (Aerotèrmia a baixa temperatura) |
| **Manteniment** | Neteja filtres aire anual. Revisió gas. (2 màquines ext). | Purga aire circuit, neteja filtres aigua. (1 màquina ext). | Neteja circuits cada 5-10 anys (llots). |
| **Vida Útil** | 15-18 anys | 15-20 anys | > 30 anys (tubs terra) / 15 maq. |

### Conclusió Econòmica
1.  **Cost:** L'Opció A és imbatible en preu d'instal·lació. Per a una casa amb demanda tan baixa (Passivhaus), el petit estalvi de consum de l'Opció C (Terra Radiant) **trigaria 50 anys a amortitzar** el sobrecost de la instal·lació.
2.  **Racionalitat:** L'**Opció A** és la més equilibrada financerament per a aquesta reforma. Inverteixes els diners en aïllament (passiu) en lloc de màquines cares (actiu).
