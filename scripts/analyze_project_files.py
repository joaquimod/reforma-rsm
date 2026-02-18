import pandas as pd
import os

pdf_path = "pb_llanes.pdf"
excel_path = "Amidaments_pb_llanes_VALIDAT.xlsx"
output_excel_summary = "project_excel_dump.txt"

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
            f.write("\n\n--- MATERIAL CHECK (searching for thermal keywords) ---\n")
            
            keywords = ['aïllament', 'aillament', 'lan', 'roca', 'mineral', 'xps', 'eps', 'sate', 'vidre', 'fusteria', 'ventil', 'recuperador', 'aerotermia']
            
            # Try to find columns with material descriptions
            possible_cols = [c for c in df.columns if isinstance(c, str) and any(x in c.lower() for x in ['desc', 'concepte', 'mat', 'partida', 'resum'])]
            
            if possible_cols:
                for col in possible_cols:
                    f.write(f"\nScanning column: {col}\n")
                    # Filter rows containing keywords
                    for keyword in keywords:
                        matches = df[df[col].astype(str).str.contains(keyword, case=False, na=False)]
                        if not matches.empty:
                            f.write(f"\n  [KEYWORD: {keyword}]\n")
                            for idx, row in matches.head(10).iterrows():
                                f.write(f"    - {row[col]} (Quant: {row.get('Amidament', 'N/A')})\n")
            else:
                f.write("No typical description columns found. Dumping all string columns for first 5 rows:\n")
                f.write(df.select_dtypes(include=['object']).head().to_string())
            
        print(f"Excel analysis complete. Saved to {output_excel_summary}")

    except Exception as e:
        print(f"Error analyzing Excel: {e}")

if __name__ == "__main__":
    analyze_excel()
