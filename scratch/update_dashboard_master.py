import json
import os

bundle_path = "/Users/joaquimolive/Programació/projecte_rsm/docs_bundle.js"
master_doc_path = "/Users/joaquimolive/Programació/projecte_rsm/docs/PE/COMUNICACIONS_I_DOMOTICA_PE_MASTER.md"

# Llegir el document mestre
with open(master_doc_path, "r", encoding="utf-8") as f:
    master_content = f.read()

# Llegir el bundle actual
with open(bundle_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Llista de claus a eliminar (documents obsolets o duplicats)
keys_to_remove = [
    "docs/PE/INSTRUCCIONS_COMUNICACIONS_DOMOTICA_PE.md",
    "docs/tecnologia/ESTRATEGIA_COMUNICACIONS_DOMOTICA_RSM.md",
    "docs/PE/Documents_Treball/Informe_Domotica.md",
    "docs/PE/COMUNICACIONS_I_DOMOTICA_PE_MASTER.md" # Per si ja hi era, per evitar duplicats
]

# Filtrar línies
filtered_lines = [line for line in lines if not any(key in line for key in keys_to_remove)]

# Inserir la nova entrada al principi
new_key = "docs/PE/COMUNICACIONS_I_DOMOTICA_PE_MASTER.md"
new_entry = f'  "{new_key}": {json.dumps(master_content, ensure_ascii=False)},\n'

for i, line in enumerate(filtered_lines):
    if "window.DOCS_BUNDLE = {" in line:
        filtered_lines.insert(i + 1, new_entry)
        break

# Guardar el bundle
with open(bundle_path, "w", encoding="utf-8") as f:
    f.writelines(filtered_lines)

print(f"Dashboard actualitzat amb el document mestre: {new_key}")
print("Documents obsolets eliminats del bundle.")
