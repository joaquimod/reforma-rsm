import json
import os

bundle_path = "/Users/joaquimolive/Programació/projecte_rsm/docs_bundle.js"
report_path = "/Users/joaquimolive/Programació/projecte_rsm/docs/PE/20260513_INFORME_SIMULACIO_ESCALA_RSM.md"

# Llegir l'informe
with open(report_path, "r", encoding="utf-8") as f:
    report_content = f.read()

# Llegir el bundle actual
with open(bundle_path, "r", encoding="utf-8") as f:
    content = f.read()

# Preparar la nova entrada
key = "docs/PE/20260513_INFORME_SIMULACIO_ESCALA_RSM.md"
value = json.dumps(report_content, ensure_ascii=False)

# Inserir la nova entrada al principi de l'objecte window.DOCS_BUNDLE
new_entry = f'\n  "{key}": {value},'
updated_content = content.replace("window.DOCS_BUNDLE = {", "window.DOCS_BUNDLE = {" + new_entry)

# Guardar el bundle actualitzat
with open(bundle_path, "w", encoding="utf-8") as f:
    f.write(updated_content)

print(f"Injectat: {key}")
