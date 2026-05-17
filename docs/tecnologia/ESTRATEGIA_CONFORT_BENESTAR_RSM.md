# Estratègia de Confort i Benestar - Casa RSM

Aquest document detalla les lògiques d'automatització avançada per millorar la qualitat de vida, la salut i l'eficiència energètica de la vivenda. Aquesta fase s'implementarà íntegrament via Home Assistant (DIY).

---

## 1. Gestió de la Qualitat de l'Aire (VMC + CO2)
En una vivenda Passivhaus l'estanquitat és total; per tant, la gestió de la ventilació és crítica per al descans i la concentració.

### Lògica de control:
- **Sensors:** Instal·lació de sensors Zigbee de CO2 i VOC (Compostos Orgànics Volàtils) als dormitoris (P2), Sala Polivalent (PB) i Sala d'Estar (P1).
- **Automatització:**
    - **Mode Normal (< 600 ppm):** VMC al 20-30% de cabal (mínim consum).
    - **Mode Confort (600-900 ppm):** Increment progressiu del cabal fins al 50%.
    - **Mode Shock (> 1000 ppm):** VMC al 100% fins que el nivell baixi de 700 ppm.
- **Benefici:** Millora dràstica de la qualitat del son i eliminació de la sensació d'"aire carregat".

## 2. Protecció Solar Passiva i Activa
Gestió de les persianes i estors basada en la radiació solar real per optimitzar la temperatura sense consumir energia.

### Lògica de control:
- **Inputs:** Dades de l'Estació Meteorològica (Lux i W/m²) + Temperatura Interior + Previsió del temps.
- **Automatització d'Estiu:** Si la radiació solar incideix directament en una façana i la temp. interior és > 23°C, les persianes es tanquen automàticament fins a la posició de "ombra total" però permetent la ventilació.
- **Automatització d'Hivern:** Les persianes s'obren al 100% quan hi ha sol directe per escalfar la casa de forma gratuïta, i es tanquen al pondre's el sol per augmentar l'aïllament tèrmic (efecte persiana com a capa extra).

## 3. Il·luminació Circadiària (Human Centric Lighting)
Sincronització de la llum artificial amb el cicle natural del sol per regular el ritme circadiari.

### Lògica de control:
- **Hardware:** Bombetes i tires LED CCT (Canvi de temperatura de color) o RGBW.
- **Dinàmica temporal:**
    - **Matí (08:00 - 12:00):** Blanc fred (5000K-6000K) i alta intensitat per inhibir la melatonina i augmentar l'alerta.
    - **Tarda (12:00 - 18:00):** Blanc neutre (4000K).
    - **Vespre (19:00 - 22:00):** Blanc molt càlid (2200K-2700K) amb intensitat reduïda per preparar el cos per al son.
    - **Nit:** Mode "Llum de lluna" (0.5% d'intensitat en tons vermellosos) per als passos nocturns al bany sense activar el sistema nerviós.

## 4. Presència Real (mmWave Radar)
Superació de les limitacions dels sensors PIR convencionals per evitar que les llums s'apaguin quan estem quiets.

### Lògica de control:
- **Hardware:** Sensors Zigbee de tecnologia de radar d'ona mil·limètrica (mmWave).
- **Ubicacions clau:**
    - **Sofà (Sala d'Estar):** Perquè les llums no s'apaguin mentre mires una pel·lícula.
    - **Escriptori (Estudi/Distribuidor P2):** Perquè la llum es mantingui mentre llegeixes o treballes.
    - **Llit (Dormitori):** Per detectar si algú està dormint i evitar que s'activin certes automatitzacions de soroll o llum.
- **Benefici:** Eliminació de les falses pèrdues de presència i automatització invisible (no has de fer res, la casa "sap" que hi ets).
- **Control d'Accés:** Reconeixement per Bluetooth (mòbil) per desbloquejar el pany intel·ligent automàticament quan t'apropis a la porta amb la compra.

## 5. Seguretat Activa i Tècnica (Protocol d'Emergència)
La seguretat s'integra amb la resta d'instal·lacions per protegir els habitants i l'edifici.

### 5.1 Protocol d'Incendi (VMC + Persianes + Llums)
En cas de detecció de fum per qualsevol sensor de la casa:
- **Aturada de VMC:** Tall immediat de la ventilació per no injectar oxigen al focus del foc ni escampar el fum per altres plantes.
- **Obertura de Persianes:** Totes les persianes motoritzades s'obren al 100% per permetre l'evacuació i l'entrada de serveis d'emergència.
- **Il·luminació de Pànic:** S'encenen tots els llums de la casa al 100% per facilitar la visibilitat en entorns amb fum.

### 5.2 Alarma d'Intrusió DIY
- **Perímetre:** Ús dels sensors de fusteria cablejats per detectar obertures no autoritzades en mode "Alarma Activada".
- **Notificació:** Avís immediat al mòbil amb captures de pantalla de les càmeres CCTV de la planta on s'ha detectat la intrusió.
- **Dissuasió:** Activació de la sirena interna i pampallugues dels llums exteriors.

---
*Aquest document és una guia de configuració per a la fase d'implementació en Home Assistant.*
