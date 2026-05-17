import os
import json

def generate_bundle():
    docs_dir = "."
    bundle_file = "docs_bundle.js"
    
    docs_data = {}
    
    # Files to include (recursive search for .md and .txt)
    extensions = ('.md', '.txt')
    
    for root, dirs, files in os.walk(docs_dir):
        # Skip some directories
        if any(skip in root for skip in ['node_modules', '.git', '.gemini', '.agent', 'patrimoni_personal']):
            continue
            
        for file in files:
            if file.endswith(extensions):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, docs_dir)
                
                try:
                    with open(full_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        docs_data[rel_path] = content
                        # Also map by filename only for easier access
                        docs_data[file] = content
                except Exception as e:
                    print(f"Error reading {full_path}: {e}")

    # Generate the JS file in multiple locations
    paths = ["docs_bundle.js", "web/public/docs_bundle.js"]
    for p in paths:
        try:
            with open(p, 'w', encoding='utf-8') as f:
                f.write("// AUTO-GENERATED DOCS BUNDLE - DO NOT EDIT MANUALLY\n")
                f.write("window.DOCS_BUNDLE = ")
                json.dump(docs_data, f, indent=2)
                f.write(";")
        except Exception as e:
            print(f"Error writing to {p}: {e}")
    
    print(f"Bundle generated: {len(docs_data)} files included.")

if __name__ == "__main__":
    generate_bundle()
