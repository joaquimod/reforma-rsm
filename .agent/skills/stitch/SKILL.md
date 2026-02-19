---
name: stitch
description: Capabilitat per interactuar amb Google Stitch per a la generació de dissenys UI/UX i prototips del projecte Casa RSM.
---

# Stitch Skill

Aquesta skill permet a l'agent Antigravity utilitzar el servidor MCP de Stitch per crear, llistar i generar pantalles de disseny per al dashboard de la reforma.

## Configura d'Ús

L'agent ha de fer servir el servidor MCP configurat a `scripts/mcp/stitch_mcp.py`. 

### Comandes principals del protocol:
1. **Llistar Projectes**: `list_projects()`
2. **Crear Projecte**: `create_project(title="Nom")`
3. **Generar Pantalla**: `generate_screen_from_text(parent="project_id", prompt="descripció", deviceType="DESKTOP")`

## Estratègies de Disseny per a Casa RSM

Quan es generin nous dissenys per al dashboard:
- **Estil**: Glassmorphism, Dark Mode, Minimalista.
- **Accents**: Cyan (#00f2ff) per a enllaços, Emerald per a estats positius (EnerPHit), Orange per a la visió/ADN.
- **Context**: Sempre incloure referències a les fases del projecte (PB, PE, Visió).

## Resolució de Problemes
- Si Stitch respon "Invalid Argument", simplifica el prompt d'entrada o verifica que el `parent` (ID del projecte) sigui correcte (format `projects/数字`).
- La clau API s'ha de mantenir a la variable d'entorn `STITCH_API_KEY`.
