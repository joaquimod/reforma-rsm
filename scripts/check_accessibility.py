import pdfplumber
import re
import os

def check_accessibility_focus(pdf_path):
    print(f"Buscant temes d'Accessibilitat a: {os.path.basename(pdf_path)}")
    keywords = [
        'accessibilitat', 'barreres arquitectòniques', 'itinerari practicable', 
        'ascensor', 'rampa', 'graó', 'desnivell', 'amplada pas', 'cercle de gir',
        'adaptat', 'practicable'
    ]
    
    findings = []
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if not text: continue
                
                # Busquem si hi ha un títol de secció
                if re.search(r'^\s*(DB-SUA|Accessibilitat|Barreres)', text, re.IGNORECASE | re.MULTILINE):
                    findings.append(f"Possible TÍTOL a Pàgina {i+1}: {text.splitlines()[0][:50]}...")
                
                # Busquem paraules clau en context
                for kw in keywords:
                    if kw in text.lower():
                        # Extraiem la frase on surt
                        match = re.search(r'([^.]*?' + kw + r'[^.]*\.)', text, re.IGNORECASE)
                        if match:
                            clean_sentence = match.group(1).replace('\n', ' ').strip()
                            findings.append(f"Pàg {i+1} ({kw}): ...{clean_sentence[:100]}...")

        return findings

    except Exception as e:
        return [f"Error: {e}"]

if __name__ == "__main__":
    base_path = "docs/PB/V1"
    pdf_files = [f for f in os.listdir(base_path) if f.startswith('01') and f.endswith('.pdf')]
    
    if pdf_files:
        res = check_accessibility_focus(os.path.join(base_path, pdf_files[0]))
        print("\n--- RESULTATS ACCESSIBILITAT ---")
        for r in res:
            print(r)
    else:
        print("No trobat PDF Memòria")
