# Guia de Configuració: Simulació IA Local (Casa RSM)

Aquest document detalla els passos per configurar el sistema de generació d'imatges de precisió al teu Mac utilitzant Draw Things.

## 1. Programari Base
- **Aplicació:** Draw Things (disponible a la Mac App Store).
- **Avantatges:** Corre 100% en local (CoreML), no requereix subscripcions i suporta ControlNet nativament.

## 2. Models recomanats per a Arquitectura
Un cop dins l'aplicació, descarrega els següents models des del gestor intern:
1. **Stable Diffusion XL (Base):** Per a la màxima qualitat de materials i textures.
2. **ControlNet Canny (SDXL):** Per a l'extracció de línies de plànols.
3. **ControlNet Depth (SDXL):** Per mantenir la percepció de profunditat i volums 3D.

## 3. Com fer un render de precisió (Workflow)

1. **Input:** Puja el plànol de l'espai com a "Image Guide".
2. **ControlNet:** Selecciona el model `Canny`. Això crearà un mapa de línies blanques sobre negre que la IA "calcarà".
3. **Prompt (Exemple):** 
   > "Modern minimalist entrance hall, light oak wood closet, light grey porcelain floor, warm indirect LED lighting, photorealistic, 8k, architectural photography style."
4. **Strength:** Posa el `ControlNet Weight` a 1.0 per a una fidelitat absoluta al plànol.

## 4. On desar els resultats?
Guardarem tots els renders de validació a la carpeta:
`docs/eines_simulacio/renders_validacio/`

---
*Aquesta guia s'actualitzarà a mesura que afinem els paràmetres per a cada espai de la casa.*
