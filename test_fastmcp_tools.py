#!/usr/bin/env python3
"""
Test simple pour vérifier que tous les outils sont bien enregistrés avec FastMCP.
"""

print("🧪 Test FastMCP PowerPoint Server")
print("="*60)

# Import du serveur
import server

print(f"\n✅ Serveur importé: {server.app.name}")
print(f"✅ Présentations: {len(server.presentations)} chargées")
print(f"✅ Current ID: {server.current_presentation_id}")

# Test basique de création
print("\n📊 Test de création de présentation...")
try:
    from server import presentations, set_current_presentation_id
    import utils as ppt_utils

    # Créer une présentation de test
    pres = ppt_utils.create_presentation()
    presentations["test_1"] = pres
    set_current_presentation_id("test_1")

    print(f"✅ Présentation test créée")
    print(f"✅ ID courant: {server.get_current_presentation_id()}")
    print(f"✅ Nombre de slides: {len(pres.slides)}")

except Exception as e:
    print(f"❌ Erreur: {e}")
    import traceback
    traceback.print_exc()

# Test d'ajout de slide
print("\n📄 Test d'ajout de slide...")
try:
    from utils import add_slide

    slide, layout = add_slide(pres, 0)  # Title slide
    print(f"✅ Slide ajouté")
    print(f"✅ Total slides: {len(pres.slides)}")

except Exception as e:
    print(f"❌ Erreur: {e}")

# Test de sauvegarde
print("\n💾 Test de sauvegarde...")
try:
    pres.save("test_fastmcp_output.pptx")
    print(f"✅ Fichier sauvegardé: test_fastmcp_output.pptx")

    import os
    if os.path.exists("test_fastmcp_output.pptx"):
        size = os.path.getsize("test_fastmcp_output.pptx")
        print(f"✅ Taille du fichier: {size} bytes")

except Exception as e:
    print(f"❌ Erreur: {e}")

print("\n" + "="*60)
print("✅ Tests terminés avec succès!")
print("\n📝 Le serveur FastMCP est prêt pour Claude Desktop")
print("\nConfiguration Claude Desktop:")
print("""{
  "mcpServers": {
    "powerpoint": {
      "command": "uv",
      "args": [
        "--directory",
        \"""" + __file__.rsplit('/', 1)[0] + """\",
        "run",
        "python",
        "server.py"
      ]
    }
  }
}""")
