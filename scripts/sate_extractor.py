import pdfplumber
import pandas as pd
import re
import os

def extract_sate_mentions(pdf_path):
    print(f"Analitzant: {pdf_path}")
    mentions = []
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if not text:
                    continue
                
                # Llista de paraules clau ampliada (tècnica i materials)
                keywords = [
                    'sate', 'aïllament', 'llana', 'mineral', 'roca', 'eps', 'xps', 
                    'poliestirè', 'façana', 'envolupant', 'trasdossat', 'transmitància', 
                    'he 1', 'he1', 'enerphit', 'passivhaus'
                ]
                
                # Creem una regex combinada: (paraula1|paraula2|...)
                pattern = r'(.{0,100})(' + '|'.join(keywords) + r')(.{0,100})'
                
                matches = re.finditer(pattern, text, re.IGNORECASE | re.DOTALL)
                
                for match in matches:
                    found_term = match.group(2).upper()
                    # Neteja de context
                    context = f"...{match.group(1)}**{match.group(2)}**{match.group(3)}..."
                    context = context.replace('\n', ' ').replace('\r', '')
                    
                    # Evitem duplicats de context molt propers en la mateixa pàgina
                    # (simple filtre per no tenir la mateixa frase 3 cops si té 3 paraules clau)
                    is_duplicate = any(m['Pàgina'] == i+1 and abs(len(m['Context (Fragment)']) - len(context)) < 20 and m['Terme'] == found_term for m in mentions)
                    
                    if not is_duplicate:
                        mentions.append({
                            "Pàgina": i + 1,
                            "Terme": found_term,
                            "Context (Fragment)": context[:200] + "..." # Limitem llargada
                        })
                    
        return mentions
    except Exception as e:
        print(f"Error llegint PDF: {e}")
        return []

if __name__ == "__main__":
    base_path = "docs/PB/V1"
    # Busquem el fitxer de memòria
    pdf_files = [f for f in os.listdir(base_path) if f.startswith('01') and f.endswith('.pdf')]
    
    if pdf_files:
        pdf_path = os.path.join(base_path, pdf_files[0])
        results = extract_sate_mentions(pdf_path)
        
        if results:
            df = pd.DataFrame(results)
            print("\nRESULTATS DE CERCADOR DE 'SATE':\n")
            print(df.to_markdown(index=False))
        else:
            print("No s'han trobat mencions a 'SATE' a la memòria.")
    else:
        print("No s'ha trobat el fitxer de memòria a docs/PB/V1")
