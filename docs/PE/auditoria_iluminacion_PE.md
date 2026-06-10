# Auditoria automatitzada de la proposta de plànols elèctrics del PE

He realitzat una revisió automatitzada comparant els requisits tècnics i de confort definits en les instruccions del projecte amb la distribució de punts real que hem extret dels plànols. A continuació detallo els punts crítics detectats, ordenats per plantes, que hauries de revisar amb l'arquitecte abans de tancar el projecte.

## 1. Punts crítics detectats (Alertes de disseny)

### Planta Baixa (PB)

#### Porxo (Po) i Vestíbul d'accés (A)
*   **Alerta (Manca de timbre i intèrfon exterior):** S'ha confirmat que als plànols de Planta Baixa (tant d'electricitat com de seguretat) no s'indica cap element de trucada (timbre o videoporter IP exterior) al porxo d'accés exterior, ni tampoc cap presa de força `S1` a cota baixa al porxo. Cal demanar la previsió de la canalització i presa RJ-45 amb PoE per al videoporter de carrer.
*   **Seguretat (Càmeres i sensors):** Es confirma la correcta col·locació de la càmera de seguretat `CV 01` a l'interior del vestíbol d'accés i el contacte magnètic `DP 01` a la porta d'accés `P-90`, d'acord amb el plànol de seguretat `I3.08.01`.

#### Sala Polivalent (Sp)
*   **Disseny de doble funció (Estudi / Dormitori):** Aquest espai funcionarà inicialment com a estudi de treball i en el futur com a dormitori. La distribució de les preses elèctriques i de dades s'ha de dissenyar de manera compatible per a ambdues funcions, evitant haver de modificar la instal·lació en el canvi d'ús:
    *   **Dades/RJ-45 (redistribució):** S'ha confirmat la reducció a 4 preses de dades RJ-45. Per garantir la màxima flexibilitat com a oficina i futur dormitori, els 4 drops es repartiran col·locant-ne 2 a la paret superior i els altres 2 a la paret inferior.
    *   **Força (Ubicació de preses de llit/estudi):** Els dos endolls de corrent de la paret inferior s'han de col·locar separats físicament, de manera que quedin situats un a cada costat del futur llit (actuant com a preses per a les tauletes de nit) i que alhora siguin funcionals per a la distribució d'escriptoris de l'estudi.



#### Garatge (G)
*   **Carregador cotxe elèctric:** Validat correctament. S'inclou la presa de 25A de força i s'ha previst la preinstal·lació del carregador amb 2 preses RJ-45 (drops 3 i 4) directes al rack per a la gestió intel·ligent de càrrega elèctrica.
*   **Seguretat:** Es confirma la ubicació de la càmera `CV 02` enfocat al vehicle/carregador i el sensor de porta de garatge `DP 02`.

#### Pati (Pa)
*   **Alerta (Instal·lació per a recollida d'aigua, reg i font):** S'ha comprovat que als plànols elèctrics no es preveu cap mena de presa de corrent estanca ni canalització per a la bomba del dipòsit soterrat d'aigua de pluja, la bomba de la font contínua ni per al cablejat del sensor de nivell (que ha de ser cablejat). Cal demanar la seva incorporació per a la viabilitat del pati bioclimàtic.
*   **Seguretat:** Es confirma la ubicació de la càmera perimetral exterior `CV 03` enfocant el pati i el sensor magnètic de la porta exterior `DP 03`.


#### Distribuidor PB (D)
*   **Disseny:** Aquest espai només conté tires LED de sostre. La rentadora està situada físicament dins la Sala Polivalent (Sp).

### Planta Primera (P1)

#### Cuina - Menjador (C-M)
*   **Alerta (Ubicació de preses de telecomunicacions i força):** S'han localitzat 2 preses RJ-45 (O2) i 2 endolls a l'extrem esquerre de la paret de la façana. Es proposa desplaçar aquest conjunt de 2 endolls + 2 RJ-45 al centre de la paret (cap a la dreta) i afegir un nou endoll individual de corrent a la cantonada esquerra (on estan situades les preses actualment).
*   **Força:** S'ha comprovat correctament que hi ha preses per a nevera, congelador, forn, microones i inducció elèctrica (circuit especial S2 de 25A).

#### Sala d'Estar (S)
*   **Dades/Multimèdia:** Es confirma la correcta col·locació de les 4 preses de dades RJ-45 a la paret de la Laser TV, complint exactament amb la necessitat de dades d'alta velocitat per al hub de la sala d'estar.
*   **Il·luminació:** Es detecta correctament la fussa LED perimetral de 5,20 metres (L1-05,20m) i 4 punts de llum de paret de suport, idonis per a l'escena de llum circadiària (Dual White / CCT).

### Planta Segona (P2)
*   **Disseny:** No s'han detectat desviacions respecte als requeriments en aquesta planta. Les preses del Dormitori 1 i del Distribuïdor/estudi estan correctes.

---

## 2. Mancances i modificacions sol·licitades

Llista senzilla de canvis a demanar a l'arquitecte abans de tancar els plànols definitius:

1.  **Manca de timbre/videoporter al porxo (PB):** Als plànols no s'hi veu cap timbre o videoporter amb accés a internet a la zona del porxo d'entrada.
2.  **Moure i afegir endolls a la Cuina-Menjador (P1):** El grup de 2 endolls i 2 preses de dades d'Internet està massa a la cantonada esquerra de la paret de façana. S'ha de desplaçar aquest bloc cap a la dreta (al centre de la paret) i, a més, s'ha d'afegir un nou endoll a l'esquerra (el lloc original).
3.  **Motors de les persianes elèctriques:** Cal assegurar-se que els motors de les persianes siguin estàndard (amb cables tradicionals de 4 fils) i no motors sense fils (de marca tipus Somfy o similars) per poder-los controlar i programar directament amb el sistema domòtic de la casa.
4.  **Alimentació de la climatització per zones (DIY/sense fils):** Els sensors de temperatura i humitat relativa (HR), així com els motors de les reixetes, seran sense fils (inhalàmbrics) i gestionats de forma autònoma (DIY), per la qual cosa no cal preveure canalitzacions físiques de control per als termòstats. No obstant això, cal assegurar-se que hi ha una font d'alimentació elèctrica o previsió de corrent a prop de les caixes de distribució o conductes per alimentar els motors de les reixetes i la unitat de control DIY.

5.  **Endolls exteriors a les Terrasses 1 i 3:** Cal afegir la previsió d'un endoll blindat per a intempèrie (estanc de seguretat per a exteriors) a la Terrassa 1 i a la Terrassa 3.
6.  **Endolls a la Planta Sotacoberta:** Cal afegir dos endolls a la planta sotacoberta: un a la paret superior i l'altre a la paret inferior.
7.  **Instal·lació elèctrica per al pati bioclimàtic (bomba de reg, font i dipòsit):** Com que s'utilitzarà l'aigua del dipòsit de pluja soterrat per a regar i alimentar la font ambiental, cal demanar a l'arquitecte que afegeixi al pati:
    *   Una escomesa elèctrica o preses de corrent estanques (IP66/IP68) per a la bomba d'aigua del dipòsit i la bomba de recirculació de la font.
    *   Previsió de tubs/canalitzacions físiques per al sensor de nivell d'aigua del dipòsit (boia o sensor de nivell), el qual és altament recomanable que sigui cablejat per seguretat (per evitar apantallaments radiofònics sota terra i per no dependre de bateries en un entorn humit), a més de les canalitzacions per a les electrovàlvules de reg.
8.  **Doble funció i distribució de la Sala Polivalent (PB):** Aquest espai tindrà un ús inicial d'Estudi i un ús futur de Dormitori. Per a fer la instal·lació compatible amb ambdós usos sense futures reformes, cal distribuir els elements així:
    *   **Dades:** Repartir les 4 preses RJ-45 col·locant-ne 2 a la paret superior i 2 a la paret inferior per a màxima flexibilitat.
    *   **Endolls:** Separar els dos endolls de la paret inferior perquè quedin a banda i banda del futur llit (a l'alçada de les tauletes de nit), servint també com a preses d'escriptori en la fase d'estudi.






