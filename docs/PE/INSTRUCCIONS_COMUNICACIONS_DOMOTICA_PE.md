# Instruccions tècniques per al Projecte Executiu (PE) - Comunicacions i Domòtica

**Projecte:** Reforma Casa RSM  
**Data:** 12 de maig de 2026  
**Objectiu:** Definició de la infraestructura passiva per a xarxes i domòtica DIY.

---

## 1. Ubicació del Rack Central
Tota la xarxa i el control domòtic es centralitzaran a la **Sala d'Instal·lacions (PB)**.
- **Espai reservat:** Armari Rack de 19" (60x60x60 cm).
- **Alimentació:** 6 preses de corrent en circuit independent protegit.
- **Ventilació:** Preveure circulació d'aire per evitar sobreescalfament.

## 2. Escomesa de serveis i vertical tècnica
- **Escomesa Fibra:** Tub de Ø40mm des de la façana (Porxo) travessant el Garatge i el Distribuidor fins al Rack Central a la Sala d'Instal·lacions (PB).
- **Dorsal Vertical:** Tub de Ø40mm que comuniqui el Rack Central (PB) amb totes les plantes (P1, P2 i PSC).
- **Escomesa TV/Sat:** Tub de Ø25mm des de la planta coberta (PSC) fins al Rack per a futura instal·lació d'antena TDT/Satèl·lit.
- **Redundància (Backup):** Tub de Ø25mm des de la planta coberta (PSC) fins al Rack per a futura antena 4G/5G/Starlink.

## 3. Requeriments elèctrics per a la domòtica
Per permetre la instal·lació posterior de mòduls Zigbee/Wi-Fi, s'exigeix:
- **Fil Neutre:** Portar obligatòriament el fil neutre (blau) a TOTS els punts d'encès (interruptors, commutadors, polsadors) i a totes les preses de corrent.
- **Caixes de mecanismes:** Totes les caixes de tota l'obra han de ser de **60mm de profunditat mínima** (per allotjar micromòduls domòtics).
- **Endolls de servei:** Instal·lació de preses de corrent a les zones previstes per a mobiliari integrat (llibreries, estanteries, capçals de llit) per a il·luminació LED ambiental posterior.
- **Quadres elèctrics:** Preveure tub de dades (RJ45) a cada quadre i un 20% d'espai lliure en rail DIN per a medidors de consum.

## 4. Xarxa de dades i Televisió
- **Punts de xarxa RJ45 (Cat6a):**
    - Sala d'estar (4), Cuina (2), Dormitoris (2 per hab).
    - **Distribuidor P2 (Zona Treball):** 2 preses dobles a sobre l'escriptori.
    - **Sala Polivalent / Estudi (PB):** 4 preses RJ45.
    - Punts de càrrega de vehicle elèctric i inversor solar.
- **Distribució TV Coaxial:**
    - Cal preveure una presa de TV coaxial a la **Sala d'Estar** i una altra a la **Cuina-Menjador**, amb tub directe al Rack Central.
    - **No cal** cablejat coaxial als dormitoris (la televisió es distribuirà via IP/RJ45).
- **Telefonia:** Es prescindeix totalment de la telefonia fixa. **No instal·lar cap presa RJ11.**
- **Wi-Fi (APs a sostre):** Preveure caixa de mecanisme a sostre amb tub de Ø25mm al Rack a:
    - Distribuïdor P1.
    - Passadís P2.
    - Terrassa exterior.
- **Pantalles de Control (Dashboards):** Preveure una caixa de mecanisme a 1,45m d'alçada en un punt central de cada planta (PB, P1, P2) amb un tub de Ø25mm directe al Rack Central per a la instal·lació de pantalles tàctils (PoE).
- **Control d'Accés Porta Principal:** Tub de Ø20mm des del Rack fins al marc de la porta principal per a futur pany motoritzat o teclat/lector NFC.

## 5. Seguretat i Sensors de fusteria
- **CCTV Interior (Substitució Alarma actual):** Preveure tub de Ø25mm i presa RJ45 Cat6a per a càmeres PoE a:
    - Vestíbol d'entrada (PB).
    - Garatge (PB).
    - Sala d'estar (P1).
- **CCTV Exterior:** Tub de Ø25mm des del Rack fins a cada punt de càmera exterior previst a totes les plantes.
- **Sensors de fusteria:** Tub de Ø16/20mm des del marc de cada porta i finestra exterior fins a la caixa de registre més propera. S'instal·laran contactes magnètics encastats (reed switches) cablejats.
- **Detecció d'Incendis:** El sistema de seguretat inclourà detectors de fum a cada planta. Cal garantir que Home Assistant tingui el control d'aturada de la VMC i obertura de persianes motoritzades en cas d'emergència.

## 6. Instal·lacions especials
- **Monitorització Aljub:** Tub de Ø25mm des del Rack fins al dipòsit d'aigües pluvials.
- **Reg Automatitzat (Pati):** Tub de Ø25mm des del Rack Central fins a una arqueta de reg al pati per al control d'electrovàlvules.
- **Climatització (Aerotèrmia i VMC):** Tub de Ø25mm i presa RJ45 Cat6a a cada unitat (Bomba de calor i recuperador de calor) per a monitorització de rendiment (COP) i control de dades.
- **Ascensor:** Presa RJ45 Cat6a a la sala de màquines/quadre de control per a telèfon d'emergència IP i monitorització d'estat a Home Assistant.
- **Sirena Exterior:** Tub de Ø20mm des del Rack fins a un punt elevat de la façana per a instal·lació de sirena d'alarma.
- **Motor Porta Garatge:** Tub de Ø25mm des del Rack fins al motor de la porta del garatge per al control d'obertura remot.
- **Comptador d'Aigua General:** Tub de Ø25mm des del Rack fins a l'arqueta de l'escomesa d'aigua per a futura monitorització de consum general.
- **Estació Meteorològica:** Tub de Ø25mm des del Rack fins a la terrassa de la P2.

---
*Aquestes instruccions han de ser integrades en els plànols d'instal·lacions i el pressupost d'amidaments del Projecte Executiu.*
