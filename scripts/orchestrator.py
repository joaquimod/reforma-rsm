import os
import argparse
import yaml
import asyncio
import pdfplumber
import pandas as pd
import re
import sys
# Afegim el directori arrel al path per si s'executa des de subcarpetes
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.sync_manager import SyncManager

def load_config():
    config_path = "config/audit_rules.yaml"
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    return {}

def extract_project_data(version):
    base_path = f"docs/PB/{version}"
    if not os.path.exists(base_path):
        print(f"Error: La carpeta {base_path} no existeix.")
        return {"text": "", "measurements": None}
        
    data = {
        "text": "",
        "measurements": None
    }
    
    # PDF Extraction
    pdf_files = [f for f in os.listdir(base_path) if f.lower().endswith('.pdf')]
    pdf_files.sort() # Ensure consistent order
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(base_path, pdf_file)
        print(f"Llegint PDF: {pdf_path}")
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        data["text"] += text + "\n"
        except Exception as e:
            print(f"Error llegint PDF {pdf_file}: {e}")
    
    # Excel Extraction
    excel_files = [f for f in os.listdir(base_path) if f.endswith('.xlsx') or f.endswith('.xls')]
    if excel_files:
        excel_path = os.path.join(base_path, excel_files[0])
        print(f"Llegint Excel: {excel_path}")
        data["measurements"] = pd.read_excel(excel_path)
    
    return data

def load_normativa_vilanova():
    path = "docs/normativa/Regles_aplicables_a_Vilanova_i_la_Geltru.txt"
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

def generate_local_llm_prompt(data, context_type="thermal"):
    """Genera un fitxer per ser processat per gpt-oss-safeguard-20b-mlx a LM Studio."""
    prompt = f"### SYSTEM: Ets un expert en auditoria forense d'edificació i Passivhaus.\n"
    prompt += f"### CONTEXT: {context_type}\n"
    
    if context_type == "thermal":
        prompt += "Analitza la següent llista de materials i calcula si la transmitància (U) estimada és coherent amb l'objectiu EnerPHit (U < 0.15 W/m2K).\n"
        if data["measurements"] is not None:
             # Agafem només files relacionades amb aïllament per no saturar el model
             df = data["measurements"]
             relevant = df[df.astype(str).apply(lambda x: x.str.contains('aïllament|xps|eps|sate|lan', case=False)).any(axis=1)]
             prompt += relevant.to_string()
    
    output_path = f"PROMPT_LM_STUDIO_{context_type}.txt"
    with open(output_path, "w") as f:
        f.write(prompt)
    return output_path

def run_audit(data, rules, normativa_text):
    findings = []
    
    # 1. Comprovació d'aïllament (EnerPHit)
    # 1.a) Via Excel (Prioritari)
    if data["measurements"] is not None:
        df = data["measurements"]
        desc_cols = [c for c in df.columns if any(x in str(c).lower() for x in ['desc', 'partida', 'concepte', 'col_2', 'col_1'])]
        if not desc_cols: desc_cols = list(df.columns)
        
        ph_min = rules.get('enerphit', {}).get('u_max_facana', 0.15)
        
        for col in desc_cols:
            aill_rows = df[df[col].astype(str).str.contains('aïllament|aillament|xps|eps|mineral|roca', case=False, na=False)]
            for idx, row in aill_rows.iterrows():
                desc = str(row[col])
                match = re.search(r'(\d+)\s*(cm|mm)', desc.lower())
                if match:
                    val = int(match.group(1))
                    unit = match.group(2)
                    thick_m = val / 100 if unit == 'cm' else val / 1000
                    # Lògica simple: si < 15cm, probablement no compleix EnerPHit (U < 0.15)
                    if thick_m < 0.15:
                        findings.append({
                            "type": "ENERPHIT",
                            "severity": "ALTA",
                            "issue": f"Gruix d'aïllament ({val}{unit}) possiblement insuficient per EnerPHit.",
                            "ref": desc,
                            "recommendation": "Verificar càlcul U-value amb el model local (LM Studio)."
                        })
    # 1.b) Via Text PDF (Fallback si no hi ha Excel)
    else:
        # Busquem patrons de gruix d'aïllament en el text
        # Ex: "panell de llana mineral de 8 cm" -> (\d+)\s*(cm|mm)
        # Context: aïllament, sate, xps, eps, llana
        
        # Capturem frases del tipus: "aïllament ... XX cm"
        matches = re.finditer(r'(aïllament|sate|xps|eps|llana)[^.\n]*?(\d+)\s*(cm|mm)', data["text"], re.IGNORECASE)
        found_isolation = False
        for match in matches:
            found_isolation = True
            mat_type = match.group(1)
            val = int(match.group(2))
            unit = match.group(3)
            thick_m = val / 100 if unit == 'cm' else val / 1000
            
            if thick_m < 0.15:
                 findings.append({
                    "type": "ENERPHIT",
                    "severity": "ALTA",
                    "issue": f"Menció a aïllament ({mat_type} {val}{unit}) insuficient per objectius EnerPHit (>15cm).",
                    "ref": f"Text PDF: ...{match.group(0)}...",
                    "recommendation": "Revisar la Memòria/Plànols per confirmar gruixos. EnerPHit sol requerir 15-20cm en façana."
                })

        if not found_isolation:
             findings.append({
                "type": "ENERPHIT",
                "severity": "ALTA",
                "issue": "No s'han detectat especificacions clares de gruix d'aïllament al text.",
                "ref": "Anàlisi Text PDF",
                "recommendation": "Assegurar que la Memòria Constructiva defineixi els gruixos d'aïllament (SATE, Trasdossats)."
            })

    # 2. Comprovació d'Habitabilitat (Catalunya)
    hab_rules = rules.get('habitabilitat_cat', {})
    
    # 2.1 Alçada lliure mínima
    h_min = hab_rules.get('alcada_minima', 2.5)
    if re.search(rf'h\s*<\s*{h_min}|alçada\s*<\s*{h_min}|2\.4[0-9]', data["text"].lower()):
         findings.append({
            "type": "HABITABILITAT",
            "severity": "ALTA",
            "issue": f"Possible incompliment d'alçada mínima ({h_min}m) detectat al text.",
            "ref": "Anàlisi de text del PDF",
            "recommendation": f"Verificar en seccions que l'alçada lliure general sigui de {h_min}m."
        })

    # 2.2 Superfícies mínimes d'habitacions (a l'Excel)
    if data["measurements"] is not None:
        df = data["measurements"]
        # Busquem files que parlin d'habitacions o dormitoris i tinguin m2
        hab_rows = df[df.astype(str).apply(lambda x: x.str.contains('habitació|dormitori|peça|sala', case=False)).any(axis=1)]
        s_min_hab = hab_rules.get('superficie_minima_habitacio', 6)
        
        for idx, row in hab_rows.iterrows():
            # Intentem trobar un número que sembli m2 (sovint en una columna numèrica)
            for col in df.columns:
                val = row[col]
                if isinstance(val, (int, float)) and 0 < val < s_min_hab:
                    findings.append({
                        "type": "HABITABILITAT",
                        "severity": "ALTA",
                        "issue": f"Superfície de peça ({val} m2) inferior al mínim legal de {s_min_hab} m2.",
                        "ref": f"Excel: {row.get('concepte', 'N/A')}",
                        "recommendation": "Revisar dimensions de la peça per complir Decret 141/2012."
                    })

    # 3. Comprovació de Normativa Vilanova (Accessibilitat/Ascensor)
    access_rules = rules.get('accessibilitat_vng', {})
    
    # Check Ascensor Reserve
    reserva_min = access_rules.get('reserva_ascensor', 1.60)
    if "ascensor" in normativa_text.lower():
        if "ascensor" not in data["text"].lower() and "elevador" not in data["text"].lower() and "reserva" not in data["text"].lower():
            findings.append({
                "type": "ACCESSIBILITAT",
                "severity": "CRÍTICA",
                "issue": "No es detecta menció a l'ascensor o espai de reserva.",
                "ref": "Anàlisi de text del PDF",
                "recommendation": f"La normativa de Vilanova requereix reserva d'espai per a ascensor ({reserva_min}x{reserva_min}m) en plurifamiliars."
            })
    
    # Check Door Widths (0.80m for accessible rooms)
    porta_min = access_rules.get('amplada_porta_llum', 0.80)
    # Busquem portes de 70 o 72 que podrien ser incorrectes per a estances practicables
    match_portes = re.search(r'(porta|fulla|pas)\s+(de\s+)?(70|72)\s*(cm)?', data["text"].lower())
    if match_portes:
         findings.append({
            "type": "ACCESSIBILITAT",
            "severity": "ALTA",
            "issue": f"Detectada possible porta de pas estret ({match_portes.group(0)}).",
            "ref": "Anàlisi de text del PDF",
            "recommendation": f"Les portes d'accés a l'habitatge i estances practicables (sala, cuina, bany, 1 hab) han de fer {porta_min}m de pas lliure."
        })

    # Check Corridor Widths (1.00m for accessible route)
    pas_min = access_rules.get('amplada_pas_habitables', 1.00)
    match_pas = re.search(r'(passadís|corredor|pas)\s+(de\s+)?(90|0\.90)\s*(cm|m)?', data["text"].lower())
    if match_pas:
         findings.append({
            "type": "ACCESSIBILITAT",
            "severity": "ALTA",
            "issue": f"Detectat passadís de {match_pas.group(3)}. La normativa marca {pas_min}m en recorregut accessible.",
            "ref": "Anàlisi de text del PDF",
            "recommendation": "Verificar que el recorregut d'accés fins a les estances principals compleix l'amplada d'1.00m (0.90m només a la resta)."
        })

    # Check Turning Circle (1.20m in bathroom/kitchen)
    cercle_min = access_rules.get('diametre_gir_bany', 1.20)
    if not re.search(r'cercle\s+de\s+gir|diàmetre\s+1\.20|diametre\s+1\.20', data["text"].lower()):
        findings.append({
            "type": "ACCESSIBILITAT",
            "severity": "MITJANA",
            "issue": f"No es detecta menció explícita al cercle de gir de {cercle_min}m.",
            "ref": "Anàlisi de text del PDF",
            "recommendation": "Assegurar que davant de portes i dins de cuina/bany practicable es pot inscriure un cercle d'1.20m."
        })

    # 4. Comprovació d'Incentius i Ajuts (Econòmics)
    # Requisit: Menció al CEE d'abans i objectiu d'estalvi > 30%
    if not re.search(r'certificat énergétique|cee\s+abans|cee\s+original', data["text"].lower()):
        findings.append({
            "type": "FINANCES",
            "severity": "ALTA",
            "issue": "No es detecta menció al Certificat Energètic d'Abans de l'obra.",
            "ref": "Anàlisi de text del PB",
            "recommendation": "És obligatori registrar el CEE original a l'ICAEN per accedir a deduccions d'IRPF (fins a 60%) i Next Gen."
        })
    
    if not re.search(r'30%|60%|estalvi\s+energia\s+primària', data["text"].lower()):
         findings.append({
            "type": "FINANCES",
            "severity": "MITJANA",
            "issue": "El projecte no quantifica l'estalvi d'energia primària per a subvencions.",
            "ref": "Anàlisi de text del PB",
            "recommendation": "L'arquitecte ha de preveure un estalvi >30% per assegurar el finançament extern."
        })

    # 5. Comprovació d'Urbanisme VNG (Nucli Antic)
    vng_rules = rules.get('urbanisme_vng', {})
    
    # 5.1 Fusteries de PVC i materials prohibits
    prohibited = vng_rules.get('materials_prohibits', ['pvc'])
    for mat in prohibited:
        if re.search(rf'fusteria\s+{mat}|finestra\s+{mat}|perfils\s+{mat}', data["text"].lower()):
            findings.append({
                "type": "URBANISME",
                "severity": "CRÍTICA",
                "issue": f"Ús de {mat.upper()} detectat. Estrictament prohibit al Nucli Antic de VNG.",
                "ref": "Anàlisi de text del PB",
                "recommendation": "Canviar a Fusta o Alumini lacat de color fosc (gris antracita o negre mat)."
            })

    # 5.2 Acabat SATE (no acrílic) i colors
    if re.search(r'acabat\s+acrílic|morter\s+acrílic|acabat\s+plàstic', data["text"].lower()):
        findings.append({
            "type": "URBANISME",
            "severity": "ALTA",
            "issue": "Acabat acrílic/plàstic detectat en façana. Prohibit a VNG.",
            "ref": "Anàlisi de text del PB",
            "recommendation": "Especificar 'Morter de Calç' o 'Estuc de calç tradicional' per garantir la transpirabilitat i compatibilitat històrica."
        })
    
    allowed_colors = vng_rules.get('colors_permesos', [])
    # Busquem colors que NO estiguin a la llista (comprova si hi ha colors prohibits o cridaners)
    if re.search(r'color\s+(vermell|blau|verd\s+clar|groc\s+llampant)', data["text"].lower()):
        findings.append({
            "type": "URBANISME",
            "severity": "ALTA",
            "issue": "Color de façana no compatible amb la paleta cromàtica de VNG.",
            "ref": "Anàlisi de text del PB",
            "recommendation": f"Utilitzar tons de la gamma: {', '.join(allowed_colors)}."
        })

    # 5.3 Unitats d'aire condicionat en façana
    if re.search(r'unitat\s+exterior\s+façana|split\s+façana|aerotèrmia\s+balcó', data["text"].lower()):
        findings.append({
            "type": "URBANISME",
            "severity": "ALTA",
            "issue": "Unitats d'instal·lacions visibles en façana o balcons.",
            "ref": "Anàlisi de text del PB",
            "recommendation": "L'ordenança prohibeix unitats visibles. Cal integrar-les en coberta, patis interiors o rere reixes ventilades integrades."
        })

    # 5.4 Volades i Projeccions
    volada_max = vng_rules.get('limitacions_balcons', {}).get('volada_maxima', 0.45)
    # Busquem mencions a balcons amb més de la volada permesa
    match_volada = re.search(r'balcó\s+de\s+(\d+[\.,]\d+|\d+)\s*m', data["text"].lower())
    if match_volada:
        val_v = float(match_volada.group(1).replace(',', '.'))
        if val_v > volada_max:
            findings.append({
                "type": "URBANISME",
                "severity": "MITJANA",
                "issue": f"Volada de balcó ({val_v}m) superior al límit de {volada_max}m.",
                "ref": "Anàlisi de text del PB",
                "recommendation": "Reduir la volada o justificar singularitat segons l'amplada del carrer."
            })
    
    # 5.5 Proteccions solars (calaixos exteriors)
    if re.search(r'calaix\s+exterior|persiana\s+aluterm', data["text"].lower()):
        findings.append({
            "type": "URBANISME",
            "severity": "MITJANA",
            "issue": "Calaixos de persiana exteriors detectats.",
            "ref": "Anàlisi de text del PB",
            "recommendation": "L'ordenança de VNG prefereix persianes de llibret o calaixos interiors per no rompre el pla de façana."
        })

    # 6. Ventilació Mecànica Controlada (VMC) - Crucial per Passivhaus i Salut
    if vng_rules.get('vmc_obligatori') and 'vmc' not in data["text"].lower() and 'ventilació mecànica' not in data["text"].lower():
        findings.append({
            "type": "ENERPHIT",
            "severity": "CRÍTICA",
            "issue": "No es detecta sistema de Ventilació Mecànica Controlada (VMC).",
            "ref": "Anàlisi global de les instal·lacions",
            "recommendation": "En una reforma amb alt aïllament i hermeticitat, la VMC amb recuperació de calor és indispensable per evitar condensacions i garantir la salut."
        })

    # 7. Flexibilitat Accessibilitat (Reforma)
    if 'reforma' in data["text"].lower() or 'contingut' in data["text"].lower():
        # En reformes, el passadís pot ser de 0.90m en lloc de 1.10m en certs punts
        if re.search(r'passadís\s+<\s*0\.90|corredor\s+<\s*0\.90', data["text"].lower()):
             findings.append({
                "type": "ACCESSIBILITAT",
                "severity": "ALTA",
                "issue": "Amplada de passadís inferior al mínim de flexibilitat (0.90m).",
                "ref": "Anàlisi de text del PB",
                "recommendation": "Cal garantir almenys 0.90m lliures segons criteris de flexibilitat del CTE per a edificis existents."
            })

    return findings

def generate_report(version, findings):
    # Nomenclatura específica: PB_RSM_v1
    file_version = version if "RSM" in version else f"RSM_{version}"
    report_path = f"Informe_Analisi_PB_{file_version}.md"
    with open(report_path, "w") as f:
        f.write(f"# Informe d'Anàlisi Tècnica - Projecte RSM ({version})\n\n")
        f.write("## 1. Configuració d'IA\n")
        f.write("- **Orquestrador:** Antigravity (Local Python Tools)\n")
        f.write("- **Model Local Confidencial:** gpt-oss-safeguard-20b-mlx (LM Studio)\n")
        f.write("- **Base de Coneixement:** NotebookLM (Export Normativa Vilanova)\n\n")
        
        f.write("## 2. Punts de Control i Troballes\n\n")
        for fnd in findings:
            f.write(f"### [{fnd['severity']}] {fnd['type']}: {fnd['issue']}\n")
            f.write(f"- **Referència:** {fnd['ref']}\n")
            f.write(f"- **Recomanació:** {fnd['recommendation']}\n\n")
            
        f.write("## 3. Pendents per a LM Studio (Dades Sensibles)\n")
        f.write("S'ha generat un fitxer a `PROMPT_LM_STUDIO_thermal.txt`. \n")
        f.write("Si us plau, processa'l amb el teu model `gpt-oss-safeguard-20b-mlx` per validar la física de l'edifici.\n")

def update_dashboard(version, findings):
    dashboard_path = "index.html"
    if not os.path.exists(dashboard_path):
        return
        
    with open(dashboard_path, "r", encoding='utf-8') as f:
        content = f.read()
    
    # 1. Actualització del Badge de Versió i Títol
    # Etiqueta: PB_RSM_{version} -> ex: PB_RSM_v1
    display_version = f"PB_RSM_{version}"
    # Busquem el span de versió (qualsevol contingut previ)
    content = re.sub(r'<span class="text-white font-bold">[^<]+</span>', f'<span class="text-white font-bold">{display_version}</span>', content, count=1)
    
    # 2. Actualització d'Enllaços i Textos (Auditoria -> Anàlisi)
    # Nom del fitxer reportat: Informe_Analisi_PB_RSM_{version}.md
    file_version = version if "RSM" in version else f"RSM_{version}"
    new_link = f"view.html?file=Informe_Analisi_PB_{file_version}.md"
    
    # Substitució genèrica de l'enllaç antic d'auditoria/anàlisi
    content = re.sub(r'href="[^"]*Informe_(Auditoria|Analisi)[^"]*\.md"', f'href="{new_link}"', content)
    
    # Canvi de textos visuals (Auditoria -> Anàlisi)
    content = content.replace("Audit Alert", "Anàlisi Tècnica")
    content = content.replace("Veure Auditoria", "Veure Anàlisi")
    content = content.replace("Auditoria estructural", "Anàlisi estructural")
    
    # 3. Càlcul de scores
    ener_findings = [f for f in findings if f['type'] == 'ENERPHIT']
    norm_findings = [f for f in findings if f['type'] in ['URBANISME', 'HABITABILITAT', 'ACCESSIBILITAT']]
    
    ener_score = max(0, 100 - (len(ener_findings) * 15))
    norm_score = max(0, 100 - (len(norm_findings) * 10))
    
    # 304: Reemplaçament de KPIs i Progress Bars
    # EnerPHit
    # Estratègia més robusta: Reemplaçar tot el bloc del KPI
    kpi_color_ener = "text-emerald-400" if ener_score > 80 else "text-yellow-500" if ener_score > 50 else "text-red-500"
    bar_color_ener = "!bg-emerald-400" if ener_score > 80 else "!bg-yellow-500" if ener_score > 50 else "!bg-red-500"
    
    # 1. KPI Value EnerPHit
    # Utilitzem \g<N> per evitar ambigüitats amb els dígits de l'score
    content = re.sub(
        r'(EnerPHit</h4>\s*<div class="kpi-text )[^"]+(">)\d+%',
        f'\\g<1>{kpi_color_ener}\\g<2>{ener_score}%',
        content, flags=re.DOTALL
    )
    # 2. Progress Bar EnerPHit (la següent al KPI)
    content = re.sub(
        r'(EnerPHit</h4>.*?<div class="progress-bar-fill w-\[)\d+(%\] )![^"]+',
        f'\\g<1>{ener_score}\\g<2>{bar_color_ener}',
        content, flags=re.DOTALL
    )

    # Normativa
    kpi_color_norm = "text-emerald-400" if norm_score > 80 else "text-yellow-500" if norm_score > 50 else "text-red-500"
    bar_color_norm = "!bg-emerald-400" if norm_score > 80 else "!bg-yellow-500" if norm_score > 50 else "!bg-red-500"

    content = re.sub(
        r'(Normativa VNG\s*</h4>\s*<div class="kpi-text )[^"]+(">)\d+%',
        f'\\g<1>{kpi_color_norm}\\g<2>{norm_score}%',
        content, flags=re.DOTALL
    )
    content = re.sub(
        r'(Normativa VNG\s*</h4>.*?<div class="progress-bar-fill w-\[)\d+(%\] )![^"]+',
        f'\\g<1>{norm_score}\\g<2>{bar_color_norm}',
        content, flags=re.DOTALL
    )

    # 3. Actualització dels Punts d'Ajust Tècnic (No tenim llista al dashboard actual, la saltem o la creem si existeix placeholder)
    # El dashboard actual no sembla tenir una llista "finding-list". 
    # Si volem afegir-ho, hauríem de buscar on posar-ho. Per ara ho deixem estar per no trencar res.

    findings_html = ""
    for fnd in findings[:3]:
        icon = "🔴" if fnd['severity'] == "CRÍTICA" else "🟠" if fnd['severity'] == "ALTA" else "🟡"
        pill_class = fnd['severity'].lower().replace('í', 'i') # critica -> critica
        findings_html += f"""
                    <li class="finding-item">
                        <div class="finding-icon" style="background: rgba(255, 77, 77, 0.1);">{icon}</div>
                        <div class="finding-content">
                            <h3>{fnd['type']}: {fnd['issue'][:40]}... <span class="status-pill pill-{pill_class}">{fnd['severity']}</span></h3>
                            <p>{fnd['recommendation']}</p>
                        </div>
                    </li>"""
    
    # Reemplacem la llista sencera
    content = re.sub(r'<ul class="finding-list">.*?</ul>', f'<ul class="finding-list">{findings_html}\n                </ul>', content, flags=re.DOTALL)

    with open(dashboard_path, "w", encoding='utf-8') as f:
        f.write(content)
    print(f"Dashboard actualitzat: EnerPHit {ener_score}%, Normativa {norm_score}%")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", default="V1")
    parser.add_argument("--sync", action="store_true", help="Sincronitza amb NotebookLM abans de l'auditoria")
    args = parser.parse_args()
    
    if args.sync:
        print("Iniciant sincronització prèvia...")
        sync_manager = SyncManager()
        asyncio.run(sync_manager.sync_once())
    
    rules = load_config()
    normativa_text = load_normativa_vilanova()
    project_data = extract_project_data(args.version)
    
    # Generem prompt per a LM Studio
    generate_local_llm_prompt(project_data)
    
    audit_findings = run_audit(project_data, rules, normativa_text)
    generate_report(args.version, audit_findings)
    update_dashboard(args.version, audit_findings)
