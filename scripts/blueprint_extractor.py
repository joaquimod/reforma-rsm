import fitz
import os

def analyze_blueprint_text(pdf_path):
    print(f"Analitzant text de plànols: {pdf_path}")
    findings = []
    try:
        doc = fitz.open(pdf_path)
        for i, page in enumerate(doc):
            text = page.get_text()
            # Busquem paraules clau en els plànols
            keywords = ['sate', 'aïllament', 'llana', 'eps', 'xps', 'cm', 'mm']
            
            # Simple check if any keyword is in text (insensitive)
            # Però volem context.
            lines = text.split('\n')
            for line in lines:
                if any(k in line.lower() for k in keywords):
                    # Ignorem cotes soles tipus "150 cm" si no tenen més context, però "SATE 16 cm" sí que ens interessa.
                    if len(line.strip()) > 3: 
                         findings.append(f"Pàgina {i+1}: {line.strip()}")
        
        return findings
    except Exception as e:
        print(f"Error llegint PDF gràfic: {e}")
        return []

if __name__ == "__main__":
    base_path = "docs/PB/V1"
    pdf_files = [f for f in os.listdir(base_path) if f.startswith('03') and f.endswith('.pdf')]
    
    if pdf_files:
        pdf_path = os.path.join(base_path, pdf_files[0])
        results = analyze_blueprint_text(pdf_path)
        
        print("\n--- TEXT TROBAT ALS PLÀNOLS (DOC 03) ---\n")
        for res in results:
            print(res)
    else:
        print("No s'ha trobat el fitxer gràfic a docs/PB/V1")
