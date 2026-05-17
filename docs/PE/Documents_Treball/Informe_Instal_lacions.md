# Informe tècnic: estratègia integral de climatització i energia

**Data:** 16 de febrer de 2026
**Fase:** projecte executiu
**Objectiu:** definir el sistema de climatització i aigua calenta sanitària (ACS) més eficient per a una rehabilitació Passivhaus, evitant el sobredimensionament i maximitzant l'autoconsum fotovoltaic.

---

## 1. El repte Passivhaus: menys és més

En una casa Passivhaus (demanda < 15 kWh/m²a), les regles del joc canvien respecte a l'obra convencional:
*   **Problema de sobredimensionament:** si instal·lem màquines potents estàndard, faran cicles curts d'encesa/apagada, reduint la vida útil del compressor.
*   **Control d'humitat:** a l'estiu, amb tanta hermeticitat, el sistema ha de ser capaç de deshumidificar suaument.
*   **La clau:** equips amb tecnologia inverter de **molt baixa potència mínima** i modulació fina.

---

## 2. Comparativa de sistemes de climatització

### Opció A: expansió directa
*   **Configuració:**
    *   **Clima:** unitat exterior multi-split (o VRV Mini) + unitats interiors de conductes (P1, P2) + split mural (PB).
    *   **ACS:** aerotermo independent de 200-300 l.
*   **Avantatges:**
    *   **Zonificació total:** pots encendre la P1 i tenir la P2 apagada. Resposta molt ràpida.
    *   **Redundància:** si s'espatlla l'aire condicionat, segueixes tenint aigua calenta.
*   **Desavantatges:** necessites lloc per a dues unitats exteriors i un termo interior voluminós.

### Opció B: aerotèrmia aire-aigua (hidrònica)
*   **Configuració:**
    *   Una sola unitat exterior potente (bibloc).
    *   Unitat interior hydrokit que produeix aigua freda/calenta per a tot.
    *   **Clima:** fancoils de conductes o sòl radiant/refrescant.
*   **Avantatges:** aprofita millor la inèrcia tèrmica. COP molt alt. Només una màquina a coberta.
*   **Desavantatges:** més car d'instal·lar i resposta més lenta si és terra radiant.

---

## 3. Estratègia d'ubicació d'equips

1.  **Unitat exterior (soroll i vibració):**
    *   **Proposta:** coberta (teulada).
    *   **Requisit crític:** cal preveure **silent-blocks** d'alta qualitat i una bancada flotant de formigó per evitar vibracions estructurales.

2.  **Unitats interiors (fals sostre banys):**
    *   Ideal per al manteniment. Cal coordinar-ho amb el recuperador de calor de la ventilació (VMC).

---

## 4. Fotovoltaica i gestió energètica

1.  **Dimensionament solar:**
    *   **Sobredimensionar** el camp solar fins al màxim possible de la coberta (ex: 3-5 kWp).

2.  **Tecnologia de l'inversor (clau domòtica):**
    *   **Inversor híbrid:** requisit obligatori per permetre la connexió futurista de bateries.
    *   **Protocol obert:** exigir comunicació **Modbus TCP o API local** per a la integració amb Home Assistant.

3.  **Emmagatzematge (bateries):**
    *   Fase inicial: ús de **bateria virtual** per a la compensació d'excedents.
    *   **Previsió física (hibridació):** l'inversor ha de permetre bateries de liti o l'ús de la bateria del cotxe (**V2H**).

| Tipus d'emmagatzematge | Capacitat | Preu aprox. instal·lat | Vida útil |
| :--- | :--- | :--- | :--- |
| **Bateria Huawei LUNA** | 10 kWh | **~6.800 €** | 15-20 anys |
| **Tesla Powerwall 3** | 13,5 kWh | **~9.000 €** | 15-20 anys |
| **Cotxe Volvo (V2H)** | **69-82 kWh** | **~11.800 €\*** | **10-15 anys** |

---

## 5. Pre-instal·lació per a vehicle elèctric (VE)

1.  **Infraestructura elèctrica:**
    *   **Circuit dedicat:** tub de Ø40mm i cablejat de **10mm²** al garatge.
    *   **Proteccions:** espai reservat al quadre per a diferencial tipus B.

2.  **Integració domòtica:**
    *   Instal·lació de presa **Ethernet (Cat6)** al costat del punt de càrrega per a la gestió d'excedents.

---

## 6. Resum de requeriments executius

1.  **Càlcul PHPP:** exigir càlcul de càrregues tèrmiques específic Passivhaus.
2.  **Sistema:** validar l'aposta per l'Opció A (aire-aire + ACS independent).
3.  **VMC:** confirmar la ubicació independent del clima.
4.  **Aïllament acústic:** bancada antivibratòria real a la coberta.

---

## 7. Anàlisi econòmica i de manteniment (estimació 2026)

| Concepte | **Opció A (Aire-Aire + ACS)** | **Opció B (Aire-Aigua + Fancoils)** |
| :--- | :---: | :---: |
| **Inversió inicial (CAPEX)** | **Baixa** | Mitjana |
| **Consum (OPEX)** | Molt baix | Molt baix |
| **Vida útil** | 15-18 anys | 15-20 anys |

### Conclusió econòmica
L'**Opció A** és la més equilibrada financerament per a aquesta reforma. Inverteixes els diners en aïllament (passiu) en lloc de màquines complexes (actiu) que trigarien massa anys a amortitzar-se en una casa Passivhaus.

---
*Aquest document forma part de l'estratègia tècnica del Projecte executiu de la Casa RSM.*
