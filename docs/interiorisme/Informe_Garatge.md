# Disseny i organització: garatge (PB)

**Superfície:** 16,80 m²  
**Ubicació:** Planta Baixa (PB)

## 1. Objectius i funcions
L'objectiu principal és optimitzar el garatge no només com a espai d'aparcament del vehicle, sinó com a node de seguretat de l'envolupant, punt de recàrrega de mobilitat elèctrica (V2H) i emmagatzematge de llarga durada mitjançant l'aprofitament del sota escala.

1. **Aparcament i recàrrega:** Estacionament del vehicle i punt de recàrrega elèctrica intel·ligent bidireccional.
2. **Seguretat i aïllament:** Zona de transició segura cap a l'habitatge amb tancaments tallafocs i sensors de seguretat.
3. **Emmagatzematge domèstic:** Integració d'un armari de magatzem de llarga durada en el buit sota l'escala.
4. **Espai de reciclatge:** Zona intermèdia de galledes de reciclatge abans de ser extretes a la façana.

## 2. Estratègia d'ordenació (zonificació i sota escala)
L'espai lliure al voltant del vehicle s'ha d'aprofitar sense comprometre l'obertura de les portes del cotxe:

*   **Zona del sota escala (Emmagatzematge i armari):**
    *   Al final del garatge, el buit generat per la inclinació de l'escala que puja a la planta primera és idoni per encastar-hi un armari a mida amb frontals de roure clar (RSM standard).
    *   Aquest volum es destinarà exclusivament a magatzem tancat per a objectes voluminosos de poc ús (maletes, material esportiu o eines). El descalcificador general de l'aigua i els col·lectors de derivació es col·locaran a la sala d'instal·lacions de la PB.
*   **Zona de recàrrega elèctrica (Paret lateral):**
    *   Punt de recàrrega bidireccional amb l'equip Wallbox Quasar 2 (proposta alta) fixat a una alçada d'1,20 metres a la paret lateral, garantint que el cable quedi recollit sense destorbar el pas cap al vestíbol.
*   **Zona de residus:**
    *   Espai pavimentat proper a la façana per ordenar les galledes de reciclatge selectiu (orgànic, envasos, paper i vidre), permetent-ne el trasllat directe al carrer el dia de recollida.

## 3. Seguretat i contraincendis
Com a zona d'emmagatzematge de vehicles i bateries, s'han de preveure les mesures de protecció obligatòries pel codi tècnic (CTE-DB-SI):
*   **Porta de seguretat interior:** L'accés directe al vestíbol de la casa es farà mitjançant una porta tallafocs homologada tipus EI2 60-C5, dotada de tanca-portes automàtic i juntes intumescents per a un segellat hermètic de fums i gasos.
*   **Extinció:** Un extintor de pols polivalent tipus ABC de 6 kg es col·locarà penjat a la paret al costat de la porta de pas de servei del vestíbol, completament visible i lliure d'obstacles.
*   **Detecció domòtica:** Un detector de fums i monòxid de carboni (CO) integrat en el sistema Zigbee/Home Assistant per a avisos i automatització de ventilació d'emergència en cas de concentració nociva.

## 4. Il·luminació (Lux Light)
Per aconseguir un ambient tècnic, net i minimalista, s'evitaran els tubs fluorescents industrials de caràcter industrial en favor del catàleg de Lux Light:
*   **Tires LED lineals:** Es disposaran tires de perfils lineals encastats a sostre de Lux Light (3000K, CRI > 90) al llarg dels dos costats del vehicle, evitant que el mateix sostre del cotxe tapi la llum en obrir les portes.
*   **Protecció IP:** Els perfils lineals i els seus difusors de plàstic han de tenir un índex de protecció mínim de **IP44** per protegir la instal·lació de partícules de pols de pneumàtics o humitat esporàdica.
*   **Sensòrica:** L'encesa de les tires LED s'automatitzarà amb Home Assistant mitjançant l'obertura de la porta basculant del carrer o en detectar pas per la porta de seguretat del vestíbol.

## 5. Requisits d'instal·lacions (PE)
S'ha de traslladar a l'arquitecte per plànols de PE:
1. **Ventilació natural permanent:** Reixetes de ventilació en posició alta i baixa en façana o patis de servei per complir amb les condicions d'extracció i salubritat del CTE.
2. **Presa d'aigua i desguàs (Opció en avaluació):** Es planteja com a opcional la instal·lació d'una aixeta de servei a la paret i un desguàs de reixeta sifònica a terra (sumidero). La decisió final es prendrà valorant els següents aspectes:
    *   *Avantatges:*
        *   Facilitat per netejar el paviment de pols, fang o restes de greix de forma directa cap al desguàs.
        *   Punt d'aigua accessible per a petits manteniments, rentat de mans o eines prèvi a entrar a l'habitatge.
        *   Recollida de l'aigua de pluja que degota de la carrosseria del vehicle en dies plujosos.
    *   *Desavantatges:*
        *   Increment del risc d'humitats en un espai interior que allotja el punt de recàrrega elèctrica de potència (V2H).
        *   Complexitat addicional de fontaneria i sanejament per portar aigua i evacuar-la des d'aquesta zona de la Planta Baixa (PB).
        *   Risc d'olors si el tancament sifònic del sumidero s'asseca per falta d'ús prolongat.
