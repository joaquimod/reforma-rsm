#!/usr/bin/env bash
set -euo pipefail

OLLAMA_URL="${OLLAMA_URL:-http://127.0.0.1:11434}"

echo "== Cursor + Ollama setup check =="
echo "Endpoint: ${OLLAMA_URL}"

if ! command -v curl >/dev/null 2>&1; then
  echo "Error: curl no esta instal lat."
  exit 1
fi

if ! curl -fsS "${OLLAMA_URL}/api/tags" >/tmp/ollama-tags.json; then
  echo "Error: No puc connectar amb Ollama a ${OLLAMA_URL}."
  echo "Assegura't que Ollama esta en marxa."
  exit 1
fi

echo "Ollama respon correctament."
echo
echo "Models detectats:"
python3 - <<'PY'
import json
from pathlib import Path

data = json.loads(Path("/tmp/ollama-tags.json").read_text())
models = [m.get("name", "") for m in data.get("models", [])]
if not models:
    print("- (cap model)")
else:
    for m in models:
        print(f"- {m}")
PY

echo
echo "Configura Cursor aixi (Settings -> Models -> Add custom model):"
echo "  - Base URL: ${OLLAMA_URL}/v1"
echo "  - API key: ollama (qualsevol valor no buit)"
echo "  - Model name: tria un dels models de la llista"
echo
echo "Prova recomanada:"
echo "  1) Selecciona nomes aquest model al xat."
echo "  2) Fes una pregunta curta per verificar resposta."
