# Seguretat Integrada i Protocal DIY | Casa RSM

## 1. Visió General
La seguretat de la Casa RSM no es concep com un sistema aïllat i opac, sinó com una capa invisible d'intel·ligència integrada en l'ecosistema domòtic DIY. L'objectiu és protegir tant el patrimoni físic com la integritat dels habitants a través de la prevenció i la detecció anticipada.

## 2. Prevenció d'Accessos i Antiroboratori
S'estableixen diversos perímetres de seguretat actius:
- **Control d'accés intel·ligent:** Pany electrònic amb protocols xifrats integrat a la xarxa local, permetent gestió de permisos remota i registres d'entrada.
- **Detecció perimetral:** Sensors d'obertura a totes les fusteries exteriors (finestres i portes) connectats via Zigbee/Thread per a una latència mínima.
- **Càmeres de visió computacional:** Integració de càmeres privades (Local-only) que utilitzen IA per diferenciar entre moviment de mascotes, ombres o presència humana real.

## 3. Protecció Contra Incendis
La detecció de foc i fum és una prioritat crítica. En cas de detecció per part dels sensors fotoelèctrics:
- **Persianes i Accessos:** Totes les persianes motoritzades es pugen automàticament al 100% per evitar bloquejos en les vies d'evacuació i permetre l'entrada visual/accés als equips d'emergència des de l'exterior.
- **Enllumenat d'Evacuació:** Tota la il·luminació interior s'encén en blanc neutre al 100% per garantir visibilitat màxima a través del fum.
- **Senyalització Exterior:** Les llums de façana i pati realitzen un parpelleig ràpid per senyalitzar visualment l'habitatge en emergència des del carrer.
- **Climatització:** Aturada immediata de la ventilació mecànica per evitar la propagació de fum entre estances.

## 4. Protocols d'Intrusió i Dissuasió
Integració de lògiques de "Casa Viva" i resposta activa:
- **Simulació de Presència:** Algorisme DIY que apaga i encén llums de forma natural i mou persianes a hores aleatòries durant períodes d'absència.
- **Resposta davant Intrusió Detectada:**
  - **Enllumenat Dissuasiu:** Totes les llums exteriors i de zones comunes s'encenen de forma instantània.
  - **Bloqueig:** Tancament automàtic de panys intel·ligents si el sistema detecta intents d'accés no autoritzats.
  - **Notificació Crítica:** Enviament d'imatges del moment de la intrusió als dispositius mòbils definits.

## 5. Integració Domòtica DIY (Ecosistema)
L'arquitectura es basa en la privadesa i l'autonomia:
- **Hub Local:** Home Assistant instal·lat en hardware dedicat a la casa.
- **Independència del Núvol:** Els protocols funcionen encara que es talli la connexió a Internet (fonamental per a la seguretat).
- **Control d'Energia:** Monitorització en temps real per detectar consums anòmals que podrien indicar avaries o incendis elèctrics.

