#!/bin/zsh

# 1. Regenerar dades (Markdown to JSON)
echo "Recollint dades de l'Obsidian..."
python3 -c "
import os, json, yaml, shutil
src_dir = 'docs/espais'
web_public = 'web/public'
os.makedirs(web_public, exist_ok=True)
data = []
for filename in os.listdir(src_dir):
    if filename.endswith('.md') and filename != 'DOC_ESPAIS_MASTER.md':
        with open(os.path.join(src_dir, filename), 'r', encoding='utf-8') as f:
            content = f.read()
            if content.startswith('---'):
                try:
                    parts = content.split('---')
                    meta = yaml.safe_load(parts[1])
                    meta['name'] = filename.replace('.md', '').replace('_', ' ')
                    meta['body'] = parts[2]
                    data.append(meta)
                except: continue
with open(os.path.join(web_public, 'data.json'), 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)
for f in os.listdir(src_dir):
    if f.lower().endswith('.png'):
        shutil.copy(os.path.join(src_dir, f), os.path.join(web_public, f))
"

# 2. Compilar web
echo "Compilant aplicació web..."
cd web && npm run build && cd ..

# 3. Pujar a Surge
echo "Pujant a la xarxa (casa-rsm-explorer.surge.sh)..."
npx -y surge web/dist --domain casa-rsm-explorer.surge.sh

echo "Actualització completada amb èxit!"
