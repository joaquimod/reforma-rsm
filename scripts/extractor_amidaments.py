import pdfplumber
import pandas as pd
import os

# CONFIGURACIÓ
pdf_path = "pb_llanes.pdf"
excel_output = "Amidaments_pb_llanes_VALIDAT.xlsx"

def extreure_taules_amidaments(path):
    all_tables_data = [] # Llista buida inicialitzada rectament
    
    if not os.path.exists(path):
        print(f"❌ Error: No s'ha trobat el fitxer '{path}'")
        return

    with pdfplumber.open(path) as pdf:
        print(f"🔍 Processant {len(pdf.pages)} pàgines del Projecte Bàsic RSM...")
        
        for i, page in enumerate(pdf.pages):
            table = page.extract_table(table_settings={
                "vertical_strategy": "lines",
                "horizontal_strategy": "lines",
                "snap_tolerance": 3,
            })
            
            if table:
                # Convertim a DataFrame
                df = pd.DataFrame(table)
                
                # NETEJA CRÍTICA PER EVITAR L'ERROR DE CONCATENACIÓ:
                # Eliminem noms de columnes i indexs que puguin causar conflictes
                df.columns = [f"Col_{n}" for n in range(len(df.columns))]
                df = df.reset_index(drop=True)
                
                if not df.empty:
                    df['Pagina_Origen'] = i + 1
                    all_tables_data.append(df)
                    print(f"✅ Taula normalitzada a la pàgina {i+1}")

    if all_tables_data:
        # Utilitzem sort=False per permetre que s'ajuntin taules amb diferent nombre de columnes
        final_df = pd.concat(all_tables_data, axis=0, ignore_index=True, sort=False)
        
        # Guardem a Excel
        final_df.to_excel(excel_output, index=False)
        print(f"\n🚀 ÈXIT! Fitxer generat: {excel_output}")
    else:
        print("\n⚠️ No s'ha pogut extreure cap dada.")

if __name__ == "__main__":
    extreure_taules_amidaments(pdf_path)