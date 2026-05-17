import json
import os

bundle_path = "/Users/joaquimolive/Programació/projecte_rsm/docs_bundle.js"
report_path = "/Users/joaquimolive/Programació/projecte_rsm/docs/PE/20260513_INFORME_SIMULACIO_ESCALA_RSM.md"

# Llegir l'informe corregit
with open(report_path, "r", encoding="utf-8") as f:
    report_content = f.read()

# Llegir el bundle actual
with open(bundle_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Filtrar totes les línies que continguin la clau del document per netejar duplicitats
key_to_remove = "docs/PE/20260513_INFORME_SIMULACIO_ESCALA_RSM.md"
filtered_lines = [line for line in lines if key_to_remove not in line]

# Reconstruir el fitxer injectant la versió bona al principi de l'objecte
new_entry = f'  "{key_to_remove}": {json.dumps(report_content, ensure_ascii=False)},\n'

# Busquem la línia de "window.DOCS_BUNDLE = {"
for i, line in enumerate(filtered_lines):
    if "window.DOCS_BUNDLE = {" in line:
        filtered_lines.insert(i + 1, new_entry)
        break

# Guardar el bundle net
with open(bundle_path, "w", encoding="utf-8") as f:
    f.writelines(filtered_lines)

print(f"Netejat i injectat correctament: {key_to_remove}")
