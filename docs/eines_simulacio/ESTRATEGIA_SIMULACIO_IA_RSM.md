# Estratègia de Simulació IA de Precisió (Casa RSM)

Basat en el document "Architectural AI Precision", aquest document defineix el sistema a implementar per generar renders realistes i geomètricament exactes de la reforma.

## 1. Objectiu Tècnic
Passar d'imatges conceptuals a **Renders de Validació**. La imatge ha de respectar les mides del Projecte Executiu (PE) per poder prendre decisions reals sobre mobiliari i materials.

## 2. El "Stack" Tecnològic Proposat

| Component | Eina Recomanada | Funció |
| :--- | :--- | :--- |
| **Captura** | Luma AI / Polycam | Escaneig 3D de l'estat actual per a referència de volums. |
| **Geometria** | ControlNet (Canny/MLSD) | Extreure les línies mestres dels plànols PDF de l'arquitecte. |
| **Motor IA** | Stable Diffusion XL | Generació de textures i il·luminació fotorealista. |
| **Interfície** | RoomVision / Krea.ai | Plataforma per orquestrar la generació sense complicacions tècniques. |

## 3. Flux de Treball (Workflow)

1. **Extracció de la Bestida:** Convertim el plànol de la planta (PDF) en un mapa de línies negres sobre fons blanc (Mapa Canny).
2. **Definició de l'Estil (Prompting):** Utilitzarem la llista de materials que estem elaborant (Roure clar, calç, porcellànic gris).
3. **Renderitzat Guiat:** La IA omplirà la "bestida" amb els materials, respectant la posició exacta de parets, portes i finestres.
4. **Inpainting:** Per a zones crítiques (com l'armari del vestíbol), utilitzarem el pinzell d'IA per provar diferents acabats sense canviar la resta de la sala.

## 4. Propers Passos
- [ ] Escollir entre instal·lació local (Mac) o ús de plataforma Cloud especialitzada.
- [ ] Exportar una vista neta en PDF d'un espai (ex. Vestíbol) per fer la primera prova de ControlNet.
- [ ] Crear la biblioteca de "Prompts de Materials" (Roure RSM, Gris Mineral RSM).

---
*Document de treball per a la implementació del sistema de simulació 3D.*
