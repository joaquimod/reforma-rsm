# Instruccions tècniques per al Projecte Executiu (PE) - Sistema V2H (Bidireccional)

**Projecte:** Reforma Casa RSM  
**Ubicació:** Garatge (G) - Planta Baixa  
**Objectiu:** Previsió de la infraestructura per a un sistema de càrrega bidireccional Vehicle-to-Home (V2H).

---

## 1. Descripció del sistema
El sistema V2H permetrà utilitzar la bateria del vehicle elèctric com a font d'energia per a la vivenda en moments de baixa producció solar o durant les hores punta de preu elèctric. Aquesta instal·lació ha de ser bidireccional (càrrega i descàrrega).

## 2. Requeriments elèctrics
- **Escomesa dedicada:** Canalització de Ø40 mm des del Quadre General de Comandament i Protecció (QGCP) fins a la paret lateral del Garatge (G).
- **Cablejat:** Mínim 3x10 mm² + terra (per a instal·lació monofàsica de 7.4 kW) o 5x6 mm² (si es preveu futur trifàsic).
- **Proteccions:**
    - Espai reservat al quadre per a un protector de sobretensions permanents i transitòries.
    - Diferencial **Tipus B** (específic per a fuites de CC en carregadors elèctrics).
    - Magnetotèrmic d'acord amb la potència del carregador.

## 3. Comunicacions i Gestió Intel·ligent
El V2H no pot funcionar sense dades en temps real.
- **Punt de dades:** Instal·lació d'una presa **RJ45 (Cat6a)** al costat de la base de càrrega, connectada directament al Rack Central de la PB.
- **Smart Meter:** L'arquitecte ha de preveure l'espai i el cablejat de dades (Modbus o Ethernet) entre el comptador de l'escomesa general i el carregador per a la gestió de la modulació de càrrega i la descàrrega cap a l'habitatge.

## 4. Ubicació física
- El carregador s'instal·larà a una alçada de 1,20 m en la paret lateral del garatge, preferiblement a prop del quadre elèctric si la distribució ho permet, per minimitzar pèrdues.
- Cal deixar un espai lliure de 50x50 cm al voltant del carregador per a ventilació.

## 5. Integració Fotovoltaica
- El sistema V2H ha d'estar coordinat amb l'inversor fotovoltaic de la planta coberta (PSC). Cal garantir que el tub de dades entre l'inversor i el Rack Central estigui operatiu per permetre la càrrega del vehicle exclusivament amb excedents solars.

---
*Aquesta previsió és crítica per a l'estratègia d'eficiència energètica de la Casa RSM.*
