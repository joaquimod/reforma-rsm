import pdfplumber
import os

def validate_pdf_quality(pdf_path):
    print(f"Analitzant qualitat del PDF: {pdf_path}\n")
    if not os.path.exists(pdf_path):
        print("Error: El fitxer no existeix.")
        return

    report = {
        "total_pages": 0,
        "text_pages": 0,
        "image_only_pages": 0,
        "is_vectorial": False,
        "sample_text": ""
    }

    try:
        with pdfplumber.open(pdf_path) as pdf:
            report["total_pages"] = len(pdf.pages)
            
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text and len(text.strip()) > 50: # Mínim de caràcters per considerar-ho text útil
                    report["text_pages"] += 1
                    if not report["sample_text"]:
                        report["sample_text"] = text[:200].replace('\n', ' ')
                else:
                    report["image_only_pages"] += 1
                    
        # Conclusió
        if report["text_pages"] == report["total_pages"]:
            report["is_vectorial"] = True
            resultat = "✅ PDF VECTORIAL (EXCEL·LENT): Tot el text és llegible per IA."
        elif report["text_pages"] > 0:
            resultat = "⚠️ PDF MIXT: Algunes pàgines podrien ser imatges o plànols sense text."
        else:
            resultat = "❌ PDF ESCANEJAT (MALT): El contingut són només imatges. L'auditoria fallarà."

        print(f"--- RESULTAT DE L'ANÀLISI ---")
        print(f"Pàgines totals: {report['total_pages']}")
        print(f"Pàgines amb text: {report['text_pages']}")
        print(f"Pàgines només imatge: {report['image_only_pages']}")
        print(f"\nESTAT: {resultat}")
        
        if report["sample_text"]:
            print(f"\nMostra de text detectat: \"{report['sample_text']}...\"")
        
        print("\nCONSELL PER A L'ARQUITECTE:")
        if not report["is_vectorial"]:
            print("Demanar que exportin el PB directament des d'AutoCAD/ArchiCAD/Revit com a 'PDF amb text', no imprimir i escanejar.")
        else:
            print("Aquests fitxers són perfectes per a l'auditoria forense digital.")

    except Exception as e:
        print(f"Error analitzant el PDF: {e}")

if __name__ == "__main__":
    import sys
    # Fem servir el fitxer de proves per defecte si no es passa un argument
    path = sys.argv[1] if len(sys.argv) > 1 else "docs/PB/proves_Llanes/pb_llanes.pdf"
    validate_pdf_quality(path)
