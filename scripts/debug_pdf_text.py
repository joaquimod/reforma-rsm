import fitz  # PyMuPDF
import os

def dump_pdf_text_raw(pdf_path):
    print(f"--- DUMP DE TEXT DEL PDF: {os.path.basename(pdf_path)} ---")
    try:
        doc = fitz.open(pdf_path)
        total_text_length = 0
        
        for i, page in enumerate(doc):
            text = page.get_text("text") # Extracció crua
            clean_text = text.strip()
            
            if clean_text:
                print(f"\n[PÀGINA {i+1}]")
                # Imprimim les primeres 500 lletres per no saturar, o tot si és curt
                print(f"Longitud: {len(clean_text)} caràcters")
                print("-" * 20)
                print(clean_text[:1000]) # Mostrem força context
                print("-" * 20)
                total_text_length += len(clean_text)
            else:
                print(f"\n[PÀGINA {i+1}] - (Sense text detectat)")
                
        print(f"\nRESULTAT FINAL: S'han llegit {total_text_length} caràcters en total.")
        return total_text_length
        
    except Exception as e:
        print(f"Error fatal llegint PDF: {e}")
        return 0

if __name__ == "__main__":
    base_path = "docs/PB/V1"
    pdf_files = [f for f in os.listdir(base_path) if f.startswith('03') and f.endswith('.pdf')]
    
    if pdf_files:
        dump_pdf_text_raw(os.path.join(base_path, pdf_files[0]))
    else:
        print("No s'ha trobat el fitxer 03 docs/PB/V1")
