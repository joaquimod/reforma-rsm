import re
import os

def check_file(path, current_dir):
    full_path = os.path.join(current_dir, path)
    if not os.path.exists(full_path):
        return False
    return True

html_files = ['index.html', 'PORTAL_SIMULACIONS_RSM.html', 'PROPOSTA_INTERIORISME_RSM.html', 'SIMULACIO_DORMITORI_1.html', 'SIMULACIO_DORMITORI_2.html', 'SIMULACIO_SOTACOBERTA.html']
broken_links = []

for html_file in html_files:
    if not os.path.exists(html_file):
        continue
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    links = re.findall(r'href="([^"]+)"', content)
    for link in links:
        if link.startswith('http') or link.startswith('#') or link.startswith('/'):
            continue
        # Extract file path
        if link.startswith('view.html?file='):
            file_path = link.split('file=')[1].split('&')[0]
            if not check_file(file_path, '.'):
                broken_links.append(f"{html_file}: {file_path} (via view.html)")
        else:
            file_path = link.split('#')[0]
            if file_path and not check_file(file_path, '.'):
                broken_links.append(f"{html_file}: {file_path}")

for b in broken_links:
    print("BROKEN:", b)
if not broken_links:
    print("All links OK")
