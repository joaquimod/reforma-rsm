import json
import os

bundle_path = "/Users/joaquimolive/Programació/projecte_rsm/docs_bundle.js"
docs_to_inject = [
    "/Users/joaquimolive/Programació/projecte_rsm/docs/PE/LOG_REUNIONS_I_ACORDS_PE.md",
    "/Users/joaquimolive/Programació/projecte_rsm/docs/PE/20260515_SEGUIMENT_ELABORACIO_PE.md"
]

with open(bundle_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for doc_path in docs_to_inject:
    rel_path = doc_path.replace("/Users/joaquimolive/Programació/projecte_rsm/", "")
    if os.path.exists(doc_path):
        with open(doc_path, "r", encoding="utf-8") as f:
            content = f.read()
        lines = [l for l in lines if f'"{rel_path}"' not in l]
        new_entry = f'  "{rel_path}": {json.dumps(content, ensure_ascii=False)},\n'
        for i, line in enumerate(lines):
            if "window.DOCS_BUNDLE = {" in line:
                lines.insert(i + 1, new_entry)
                break

with open(bundle_path, "w", encoding="utf-8") as f:
    f.writelines(lines)

print("Log Mestre injectat al Dashboard.")
