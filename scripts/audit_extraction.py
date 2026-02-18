import pdfplumber
import pandas as pd
import os
import re

pdf_path = "pb_llanes.pdf"
excel_path = "Amidaments_pb_llanes_VALIDAT.xlsx"
output_text_file = "project_text_dump.txt"
output_excel_summary = "project_excel_dump.txt"

def extract_text_from_pdf():
    print(f"Extracting text from {pdf_path}...")
    full_text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    full_text += f"\n--- PAGE {i+1} ---\n{text}\n"
        
        with open(output_text_file, "w") as f:
            f.write(full_text)
        print(f"Text extraction complete. Saved to {output_text_file}")
    except Exception as e:
        print(f"Error extracting PDF text: {e}")

def analyze_excel():
    print(f"Analyzing Excel {excel_path}...")
    try:
        if not os.path.exists(excel_path):
            print("Excel file not found.")
            return

        df = pd.read_excel(excel_path)
        
        # Save a summary of the dataframe to text
        with open(output_excel_summary, "w") as f:
            f.write("--- EXCEL COLUMNS ---\n")
            f.write(str(df.columns.tolist()) + "\n\n")
            f.write("--- FIRST 50 ROWS ---\n")
            f.write(df.head(50).to_string())
            f.write("\n\n--- MATERIAL CHECK (searching for thermal/compliance keywords) ---\n")
            
            keywords = [
                'aïllament', 'aillament', 'lan', 'roca', 'mineral', 'xps', 'eps', 'sate', 'vidre', 'fusteria', 
                'ventil', 'recuperador', 'aerotermia', 'solar', 'ombra', 'persiana', 'façana', 'coberta'
            ]
            
            # Try to find columns with material descriptions
            possible_cols = [c for c in df.columns if isinstance(c, str) and any(x in c.lower() for x in ['desc', 'concepte', 'mat', 'partida', 'resum'])]
            
            if possible_cols:
                for col in possible_cols:
                    f.write(f"\nScanning column: {col}\n")
                    # Filter rows containing keywords
                    for keyword in keywords:
                        try:
                             matches = df[df[col].astype(str).str.contains(keyword, case=False, na=False)]
                             if not matches.empty:
                                f.write(f"\n  [KEYWORD: {keyword}]\n")
                                for idx, row in matches.head(10).iterrows():
                                    # Try to find quantity and unit
                                    amid = row.get('Amidament', list(row)[-1] if len(row)>1 else 'N/A')
                                    f.write(f"    - {row[col]} (Quant: {amid})\n")
                        except Exception as e:
                            f.write(f"Error filtering for {keyword}: {e}\n")
            else:
                f.write("No typical description columns found. Dumping all string columns for first 5 rows:\n")
                f.write(df.select_dtypes(include=['object']).head().to_string())
            
        print(f"Excel analysis complete. Saved to {output_excel_summary}")

    except Exception as e:
        print(f"Error analyzing Excel: {e}")

if __name__ == "__main__":
    extract_text_from_pdf()
    analyze_excel()
