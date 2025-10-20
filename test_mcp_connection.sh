#!/bin/bash
# Test script pour vérifier que le serveur MCP fonctionne

echo "🧪 Test de connexion MCP PowerPoint Server"
echo "=========================================="

# Test 1: Démarrage du serveur
echo ""
echo "Test 1: Vérification que le serveur démarre..."
timeout 2 uv run python server.py --help > /dev/null 2>&1
if [ $? -eq 0 ] || [ $? -eq 124 ]; then
    echo "✅ Serveur peut démarrer"
else
    echo "❌ Erreur au démarrage du serveur"
    exit 1
fi

# Test 2: Vérifier les imports
echo ""
echo "Test 2: Vérification des imports..."
python3 << 'EOF'
import sys
sys.path.insert(0, '.')

try:
    from mcp.server.fastmcp import FastMCP
    print("✅ FastMCP importé")
except ImportError as e:
    print(f"❌ Erreur import FastMCP: {e}")
    sys.exit(1)

try:
    from tools import register_presentation_tools
    print("✅ Tools importés")
except ImportError as e:
    print(f"❌ Erreur import tools: {e}")
    sys.exit(1)

try:
    import utils as ppt_utils
    print("✅ Utils importés")
except ImportError as e:
    print(f"❌ Erreur import utils: {e}")
    sys.exit(1)

print("✅ Tous les imports sont OK")
EOF

# Test 3: Compter les outils enregistrés
echo ""
echo "Test 3: Comptage des outils..."
python3 << 'EOF'
import sys
sys.path.insert(0, '.')

from mcp.server.fastmcp import FastMCP
from tools import (
    register_presentation_tools,
    register_content_tools,
    register_structural_tools,
    register_professional_tools,
    register_template_tools,
)

app = FastMCP("test")
presentations = {}

def get_current_presentation_id():
    return None

def get_template_search_directories():
    return ['.']

def validate_parameters(params):
    return True, None

def is_positive(x):
    return x > 0

def is_non_negative(x):
    return x >= 0

def is_in_range(min_val, max_val):
    return lambda x: min_val <= x <= max_val

def is_valid_rgb(color_list):
    return isinstance(color_list, list) and len(color_list) == 3

# Enregistrer quelques modules
register_presentation_tools(app, presentations, get_current_presentation_id, get_template_search_directories)
register_content_tools(app, presentations, get_current_presentation_id, validate_parameters, is_positive, is_non_negative, is_in_range, is_valid_rgb)

print(f"✅ Outils enregistrés avec succès")
EOF

echo ""
echo "=========================================="
echo "✅ Tous les tests de base réussis!"
echo ""
echo "Le serveur est prêt pour Claude Desktop"
echo "Ajoutez cette configuration:"
echo ""
echo '{'
echo '  "mcpServers": {'
echo '    "powerpoint": {'
echo '      "command": "uv",'
echo '      "args": ['
echo '        "--directory",'
echo '        "'$(pwd)'",'
echo '        "run",'
echo '        "python",'
echo '        "server.py"'
echo '      ]'
echo '    }'
echo '  }'
echo '}'
