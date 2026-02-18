import pdfplumber
import re
import os

def check_habitability_decree(pdf_path):
    print(f"Buscant 'Decret 141/2012' a: {os.path.basename(pdf_path)}")
    keywords = ['141/2012', 'annex 2', 'annex II', 'flexibilitat', 'habitatges existents', 'preexistència']
    
    findings = []
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if not text: continue
                
                # Busquem paraules clau en context
                for kw in keywords:
                    if kw in text.lower():
                        # Extraiem la frase on surt (context ampli)
                        match = re.search(r'(.{0,100}' + re.escape(kw) + r'.{0,100})', text, re.IGNORECASE)
                        if match:
                            clean_sentence = match.group(0).replace('\n', ' ').strip()
                            findings.append(f"Pàg {i+1}: ...{clean_sentence}...")

        return findings

    except Exception as e:
        return [f"Error: {e}"]

if __name__ == "__main__":
    base_path = "docs/PB/V1"
    pdf_files = [f for f in os.listdir(base_path) if f.startswith('01') and f.endswith('.pdf')]
    
    if pdf_files:
        res = check_habitability_decree(os.path.join(base_path, pdf_files[0]))
        print("\n--- RESULTATS DECRET ---")
        if not res:
            print("No s'ha trobat cap referència al Decret 141/2012 ni a l'Annex 2.")
        for r in res:
            print(r)
    else:
        print("No trobat PDF Memòria")
