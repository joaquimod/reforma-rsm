# Guió de reunió amb l'arquitecte

**Projecte:** Casa RSM (Reforma)  
**Data de la reunió:** Dijous, 14 de maig de 2026  
**Objectiu:** Validar la integració de la infraestructura tecnològica al projecte executiu (PE).

---

## 1. Les línies vermelles
Aquests punts han d'aparèixer sí o sí als amidaments i plànols elèctrics:
- [ ] **Fil neutre a TOTS els mecanismes:** Obligatori per a interruptors, commutadors i endolls a totes les plantes.
- [ ] **Caixes de mecanismes de 60mm de fons:** Tota l'obra ha de portar caixes de gran profunditat per encastar els micromòduls Zigbee.
- [ ] **Ubicació del rack:** Confirmar espai lliure de 60x60x60 cm a la sala d'instal·lacions (PB) amb ventilació i 6 preses de corrent.

## 2. Escomeses i connectivitat vertical
- [ ] **Traçat de fibra (PES):** Validar tub de Ø40mm: Porxo -> Garatge -> Distribuidor -> Sala instal·lacions (PB).
- [ ] **Dorsal tècnica:** Tub de Ø40mm que comuniqui verticalment totes les plantes (de la PB a la coberta).
- [ ] **Backup 5G i TV:** Tubs de Ø25mm des de la planta coberta (PC) fins al rack central.
- [ ] **Punts WiFi i pantalles:** Validar punts a sostre (WiFi) i a 1,45m (dashboards PoE) amb tubs directes al rack.

## 3. Seguretat i accessibilitat
- [ ] **Sensors de fusteria:** Confirmar que les portes i finestres es demanen amb preparació per a sensors magnètics encastats i que arriba un tub de Ø16/20mm a cada marc.
- [ ] **CCTV PoE:** Punts de càmera a les façanes de cada planta connectats al rack.
- [ ] **Ascensor:** Presa RJ45 i tub de dades a la sala de màquines (seguretat IP).
- [ ] **Control d'accés:** Tub des del rack fins al marc de la porta principal.

## 4. Eficiència energètica i clima
- [ ] **V2H (bidireccional):** Tub de Ø40mm i presa RJ45 al punt de càrrega del garatge. Cable de 10mm².
- [ ] **Monitorització de màquines:** Preses RJ45 a l'aerotèrmia i a la VMC per a control de dades.
- [ ] **Espai al quadre elèctric:** Reserva del 20% en rail DIN per a mesuradors de consum (smart meters).

## 5. Exteriors i gestió de recursos
- [ ] **Aljub de pluvials:** Tub de dades fins al dipòsit per al sensor de nivell DIY.
- [ ] **Reg automatitzat:** Tub de dades/elèctric fins a l'arqueta de reg del pati mediterrani.
- [ ] **Estació meteorològica:** Ubicació i tub a la terrassa de la P2.

---

### Documents per entregar a l'arquitecte:
1.  **Instruccions executives PE** (Resum de tubs i requeriments).
2.  **Instruccions V2H garatge** (Especificacions elèctriques).
