# Migració del sistema de seguretat: De Verisure a DIY Casa RSM

Aquest document detalla el procés, el maquinari i la lògica per substituir el sistema de seguretat propietari actual (Verisure) per un sistema d'alt rendiment basat en Home Assistant, garantint la protecció contra robatori i ocupació.

---

## 1. Per què la migració? (DIY vs Verisure)

| Característica | Sistema Verisure (Actual) | Sistema DIY RSM (Nou) |
| :--- | :--- | :--- |
| **Connexió** | Sense fils (Vulnerable a inhibidors) | **Cablejada (Immune a inhibidors)** |
| **Privacitat** | Vídeo al núvol de l'empresa | **Vídeo 100% local (NVR al Rack)** |
| **Cost** | Quota mensual elevada | **Cost mensual 0 €** |
| **Integració** | Sistema tancat i aïllat | **Integrat amb llums, persianes i clima** |
| **Anti-ocupació** | Reactiva (avís a policia) | **Preventiva (simulació real de presència)** |

---

## 2. Maquinari necessari (La substitució)

Per substituir els elements actuals, instal·larem els següents components integrats al projecte executiu:

### 2.1 Central i Control
- **En lloc del Panel Verisure:** Farem servir la **Raspberry Pi 4** amb un **Dongle Zigbee 3.0** i el programari **Alarmo** (integració de Home Assistant).
- **Teclat:** Farem servir les **Pantalles de Control (PoE)** situades a cada planta i el telèfon mòbil (via VPN segura).

### 2.2 Sensors i Detecció
- **En lloc de sensors de moviment PIR Wi-Fi:**
    - **Sensors de fusteria (Reed):** Cablejats directament al Rack (previstos al PE). Detecten l'obertura abans que l'intrús entri.
    - **Sensors mmWave (Radar):** Per a detecció de presència real sense "punts cecs".
- **En lloc de càmeres Cloud:**
    - **Càmeres PoE (Cat6a):** Alimentades per cable. Gravació 24/7 mitjançant **Frigate (AI)** que distingeix entre persones, animals i vehicles localment.

---

## 3. Estratègia anti-ocupació i robatori

La millor seguretat és la que evita que l'intrús esculli la teva casa.

### 3.1 Simulació de presència activa
- **Il·luminació dinàmica:** Home Assistant reproduirà els teus hàbits reals de llum (estades, horaris) quan la casa estigui en mode "Vacances".
- **Persianes intel·ligents:** Moviment natural de persianes segons la llum solar, simulant activitat diària.
- **So dissuasiu:** Possibilitat de reproduir sons (gos, veus, TV) a través dels altaveus si es detecta presència al perímetre exterior.

### 3.2 Protocol d'intrusió
En cas de detecció confirmada per sensors o IA de les càmeres:
1.  **Notificació Crítica:** Avís al mòbil que se salta el mode "Silenci" amb imatge de l'intrús.
2.  **Dissuasió Acústica:** Activació de la sirena exterior de 110dB.
3.  **Dissuasió Visual:** Pampallugues de tots els llums de la façana i interiors.
4.  **Cierre de Seguretat:** Bloqueig del pany intel·ligent (si estava obert) i tancament de totes les persianes.

---

## 4. Requeriments crítics per al PE

Perquè aquesta migració sigui possible, el Projecte Executiu ha de garantir:
- **Tubs i cables RJ45:** Als punts de càmeres (Vestíbol, Garatge, Sala d'Estar i Façanes).
- **Tubs de fusteria:** Des de cada finestra fins al Rack Central.
- **Reserva de bateria (SAI):** El sistema de seguretat ha de funcionar encara que tallin el corrent elèctric des de l'exterior.
- **Backup 4G/5G:** Per mantenir les notificacions al mòbil si tallen el cable de fibra òptica del carrer.

---
*Aquest sistema ofereix un nivell de protecció superior al grau 2 de les alarmes comercials gràcies a la infraestructura cablejada i la intel·ligència local.*
