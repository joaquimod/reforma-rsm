import json
import os

bundle_path = "/Users/joaquimolive/Programació/projecte_rsm/docs_bundle.js"
docs_to_inject = [
    "/Users/joaquimolive/Programació/projecte_rsm/docs/PE/20260515_SEGUIMENT_ELABORACIO_PE.md",
    "/Users/joaquimolive/Programació/projecte_rsm/docs/PE/20260515_GUIA_PAVIMENT_CERAMIC_RSM.md",
    "/Users/joaquimolive/Programació/projecte_rsm/docs/PE/20260515_CORREU_ARQUITECTA_DOMOTICA_ARMARIS.md",
    "/Users/joaquimolive/Programació/projecte_rsm/docs/PE/COMUNICACIONS_I_DOMOTICA_PE_MASTER.md",
    "/Users/joaquimolive/Programació/projecte_rsm/docs/PE/Documents_Treball/Informe_Paviments.md"
]

# Llegir el bundle actual
with open(bundle_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Preparar el nou contingut de l'objecte
new_bundle_dict = {}

# Extreure dades existents (molt simplificat)
# Nota: Això és per mantenir el que ja hi ha i només sobreescriure/afegir els nous
for doc_path in docs_to_inject:
    rel_path = doc_path.replace("/Users/joaquimolive/Programació/projecte_rsm/", "")
    if os.path.exists(doc_path):
        with open(doc_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Eliminar linies velles d'aquest fitxer si existeixen
        lines = [l for l in lines if f'"{rel_path}"' not in l]
        
        # Crear la nova entrada
        new_entry = f'  "{rel_path}": {json.dumps(content, ensure_ascii=False)},\n'
        
        # Inserir després de l'obertura de l'objecte
        for i, line in enumerate(lines):
            if "window.DOCS_BUNDLE = {" in line:
                lines.insert(i + 1, new_entry)
                break

# Guardar el bundle actualitzat
with open(bundle_path, "w", encoding="utf-8") as f:
    f.writelines(lines)

print("Dashboard sincronitzat amb els nous documents del PE.")
