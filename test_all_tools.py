#!/usr/bin/env python3
"""
Script de test complet pour tous les 32 outils PowerPoint MCP Server.
Ce script teste chaque outil de manière séquentielle et génère une présentation de démonstration.
"""

import json
import sys
from pathlib import Path

# Ajouter le répertoire parent au PYTHONPATH pour importer le serveur
sys.path.insert(0, str(Path(__file__).parent))

# Importer le serveur et ses dépendances
from server import (
    presentations,
    get_current_presentation_id,
    set_current_presentation_id,
)

# Importer tous les modules de tools
from tools.presentation_tools import register_presentation_tools
from tools.content_tools import register_content_tools
from tools.template_tools import register_template_tools
from tools.structural_tools import register_structural_tools
from tools.professional_tools import register_professional_tools
from tools.chart_tools import register_chart_tools
from tools.hyperlink_tools import register_hyperlink_tools
from tools.connector_tools import register_connector_tools
from tools.master_tools import register_master_tools
from tools.transition_tools import register_transition_tools


class ToolTester:
    """Classe pour tester tous les outils du serveur."""

    def __init__(self):
        self.results = {
            "total_tests": 0,
            "passed": 0,
            "failed": 0,
            "errors": []
        }
        self.tools = {}
        self._register_all_tools()

    def _register_all_tools(self):
        """Enregistre tous les outils dans un dictionnaire accessible."""
        print("📋 Enregistrement des outils...")

        # Mock app pour collecter les outils
        class MockApp:
            def __init__(self, tester):
                self.tester = tester
                self.tool_counter = 0

            def tool(self):
                def decorator(func):
                    tool_name = func.__name__
                    self.tester.tools[tool_name] = func
                    self.tool_counter += 1
                    return func
                return decorator

        mock_app = MockApp(self)

        # Import des fonctions helper du serveur
        from server import (
            get_template_search_directories,
            validate_parameters,
            is_positive,
            is_non_negative,
            is_in_range,
            is_valid_rgb,
            add_shape_direct
        )

        # Enregistrer tous les modules
        register_presentation_tools(
            mock_app, presentations, get_current_presentation_id,
            get_template_search_directories
        )
        register_content_tools(
            mock_app, presentations, get_current_presentation_id,
            validate_parameters, is_positive, is_non_negative,
            is_in_range, is_valid_rgb
        )
        register_structural_tools(
            mock_app, presentations, get_current_presentation_id,
            validate_parameters, is_positive, is_non_negative,
            is_in_range, is_valid_rgb, add_shape_direct
        )
        register_professional_tools(
            mock_app, presentations, get_current_presentation_id
        )
        register_template_tools(
            mock_app, presentations, get_current_presentation_id
        )
        register_chart_tools(
            mock_app, presentations, get_current_presentation_id,
            validate_parameters, is_positive, is_non_negative,
            is_in_range, is_valid_rgb
        )
        register_hyperlink_tools(
            mock_app, presentations, get_current_presentation_id,
            validate_parameters, is_positive, is_non_negative,
            is_in_range, is_valid_rgb
        )
        register_connector_tools(
            mock_app, presentations, get_current_presentation_id,
            validate_parameters, is_positive, is_non_negative,
            is_in_range, is_valid_rgb
        )
        register_master_tools(
            mock_app, presentations, get_current_presentation_id,
            validate_parameters, is_positive, is_non_negative,
            is_in_range, is_valid_rgb
        )
        register_transition_tools(
            mock_app, presentations, get_current_presentation_id,
            validate_parameters, is_positive, is_non_negative,
            is_in_range, is_valid_rgb
        )

        print(f"✅ {mock_app.tool_counter} outils enregistrés\n")

    def run_test(self, category, tool_name, func, *args, **kwargs):
        """Exécute un test pour un outil spécifique."""
        self.results["total_tests"] += 1
        print(f"  🧪 Test: {tool_name}")

        try:
            result = func(*args, **kwargs)

            # Vérifier si le résultat contient une erreur
            if isinstance(result, dict) and "error" in result:
                print(f"    ❌ Erreur: {result['error']}")
                self.results["failed"] += 1
                self.results["errors"].append({
                    "category": category,
                    "tool": tool_name,
                    "error": result["error"]
                })
            else:
                print(f"    ✅ Succès")
                self.results["passed"] += 1
                return result

        except Exception as e:
            print(f"    ❌ Exception: {str(e)}")
            self.results["failed"] += 1
            self.results["errors"].append({
                "category": category,
                "tool": tool_name,
                "error": str(e)
            })
            return None

    def test_presentation_management(self):
        """Test des 7 outils de gestion de présentation."""
        print("\n" + "="*60)
        print("📊 CATÉGORIE 1: GESTION DE PRÉSENTATION (7 outils)")
        print("="*60)

        # 1. create_presentation
        result = self.run_test(
            "Presentation Management",
            "create_presentation",
            self.tools["create_presentation"],
            id="test_presentation"
        )

        # 2. get_presentation_info
        if result:
            self.run_test(
                "Presentation Management",
                "get_presentation_info",
                self.tools["get_presentation_info"]
            )

        # 3. set_core_properties
        self.run_test(
            "Presentation Management",
            "set_core_properties",
            self.tools["set_core_properties"],
            title="Test Presentation PowerPoint MCP",
            author="PowerPoint MCP Server",
            subject="Tests Complets",
            keywords="test, powerpoint, mcp"
        )

        # 4. save_presentation
        self.run_test(
            "Presentation Management",
            "save_presentation",
            self.tools["save_presentation"],
            file_path="test_output.pptx"
        )

        print(f"\n✅ Gestion de présentation: {self.results['passed']}/{self.results['total_tests']} tests réussis")

    def test_content_management(self):
        """Test des 6+ outils de gestion de contenu."""
        print("\n" + "="*60)
        print("📝 CATÉGORIE 2: GESTION DE CONTENU (6+ outils)")
        print("="*60)

        # 1. add_slide
        self.run_test(
            "Content Management",
            "add_slide",
            self.tools["add_slide"],
            layout_index=6,
            background_color=[240, 240, 255]
        )

        # 2. get_slide_info
        self.run_test(
            "Content Management",
            "get_slide_info",
            self.tools["get_slide_info"],
            slide_index=0
        )

        # 3. manage_text (add operation)
        self.run_test(
            "Content Management",
            "manage_text",
            self.tools["manage_text"],
            operation="add",
            slide_index=0,
            text="Bienvenue au Test Complet PowerPoint MCP",
            left=1.0,
            top=2.0,
            width=8.0,
            height=1.5,
            font_size=36,
            bold=True,
            color_rgb=[0, 120, 215]
        )

        # 4. add_bullet_points
        self.run_test(
            "Content Management",
            "add_bullet_points",
            self.tools["add_bullet_points"],
            slide_index=0,
            left=1.5,
            top=4.0,
            width=7.0,
            height=2.0,
            bullet_points=[
                "Test de tous les 32 outils",
                "Génération automatique de présentation",
                "Vérification des fonctionnalités"
            ]
        )

        # 5. extract_slide_text
        self.run_test(
            "Content Management",
            "extract_slide_text",
            self.tools["extract_slide_text"],
            slide_index=0
        )

        # 6. extract_presentation_text
        self.run_test(
            "Content Management",
            "extract_presentation_text",
            self.tools["extract_presentation_text"]
        )

        print(f"\n✅ Gestion de contenu: Tests complétés")

    def test_template_operations(self):
        """Test des 7 outils de templates."""
        print("\n" + "="*60)
        print("🎨 CATÉGORIE 3: OPÉRATIONS DE TEMPLATES (7 outils)")
        print("="*60)

        # 1. list_slide_templates
        templates_result = self.run_test(
            "Template Operations",
            "list_slide_templates",
            self.tools["list_slide_templates"]
        )

        # 2. get_template_info
        if templates_result and "templates" in templates_result:
            first_template = templates_result["templates"][0]["name"]
            self.run_test(
                "Template Operations",
                "get_template_info",
                self.tools["get_template_info"],
                template_name=first_template
            )

        # 3. create_slide_from_template
        self.run_test(
            "Template Operations",
            "create_slide_from_template",
            self.tools["create_slide_from_template"],
            template_name="title_slide",
            content={
                "title": "Slide de Template",
                "subtitle": "Généré automatiquement"
            },
            color_scheme="modern_blue"
        )

        # 4. apply_slide_template
        self.run_test(
            "Template Operations",
            "apply_slide_template",
            self.tools["apply_slide_template"],
            slide_index=1,
            template_name="two_column_text",
            content={
                "title": "Comparaison",
                "left_text": "Avant",
                "right_text": "Après"
            }
        )

        # 5. optimize_slide_text
        self.run_test(
            "Template Operations",
            "optimize_slide_text",
            self.tools["optimize_slide_text"],
            slide_index=0,
            min_font_size=12,
            max_font_size=32
        )

        print(f"\n✅ Opérations de templates: Tests complétés")

    def test_structural_elements(self):
        """Test des 4 outils d'éléments structurels."""
        print("\n" + "="*60)
        print("🔲 CATÉGORIE 4: ÉLÉMENTS STRUCTURELS (4 outils)")
        print("="*60)

        # Ajouter un slide pour les tests
        self.tools["add_slide"](layout_index=6)
        current_slide = len(presentations[get_current_presentation_id()].slides) - 1

        # 1. add_table
        self.run_test(
            "Structural Elements",
            "add_table",
            self.tools["add_table"],
            slide_index=current_slide,
            rows=4,
            cols=3,
            left=1.0,
            top=1.5,
            width=8.0,
            height=3.0,
            data=[
                ["Produit", "Prix", "Stock"],
                ["Produit A", "100€", "50"],
                ["Produit B", "150€", "30"],
                ["Produit C", "200€", "20"]
            ]
        )

        # 2. add_shape
        self.run_test(
            "Structural Elements",
            "add_shape",
            self.tools["add_shape"],
            slide_index=current_slide,
            shape_type="rectangle",
            left=1.0,
            top=5.0,
            width=2.0,
            height=1.0,
            fill_color=[100, 150, 200]
        )

        # 3. add_line
        self.run_test(
            "Structural Elements",
            "add_line",
            self.tools["add_line"],
            slide_index=current_slide,
            start_x=4.0,
            start_y=5.5,
            end_x=7.0,
            end_y=5.5,
            line_color=[255, 0, 0],
            line_width=3
        )

        # 4. add_textbox
        self.run_test(
            "Structural Elements",
            "add_textbox",
            self.tools["add_textbox"],
            slide_index=current_slide,
            text="Zone de texte de test",
            left=4.5,
            top=5.0,
            width=2.5,
            height=1.0,
            font_size=14
        )

        print(f"\n✅ Éléments structurels: Tests complétés")

    def test_professional_design(self):
        """Test des 3 outils de design professionnel."""
        print("\n" + "="*60)
        print("✨ CATÉGORIE 5: DESIGN PROFESSIONNEL (3 outils)")
        print("="*60)

        # Ajouter un slide pour les tests
        self.tools["add_slide"](layout_index=6)
        current_slide = len(presentations[get_current_presentation_id()].slides) - 1

        # 1. apply_professional_design
        self.run_test(
            "Professional Design",
            "apply_professional_design",
            self.tools["apply_professional_design"],
            operation="apply_color_scheme",
            color_scheme="corporate_gray"
        )

        # 2. add_chart
        self.run_test(
            "Professional Design",
            "add_chart",
            self.tools["add_chart"],
            slide_index=current_slide,
            chart_type="column",
            left=1.5,
            top=1.5,
            width=7.0,
            height=4.0,
            title="Ventes Trimestrielles",
            categories=["Q1", "Q2", "Q3", "Q4"],
            series=[
                {"name": "2023", "values": [100, 120, 140, 160]},
                {"name": "2024", "values": [130, 150, 170, 190]}
            ]
        )

        # 3. format_text_advanced (si disponible)
        if "format_text_advanced" in self.tools:
            self.run_test(
                "Professional Design",
                "format_text_advanced",
                self.tools["format_text_advanced"],
                slide_index=0,
                shape_index=0,
                font_name="Arial",
                font_size=24,
                bold=True
            )

        print(f"\n✅ Design professionnel: Tests complétés")

    def test_specialized_features(self):
        """Test des 5 outils spécialisés."""
        print("\n" + "="*60)
        print("🔧 CATÉGORIE 6: FONCTIONNALITÉS SPÉCIALISÉES (5 outils)")
        print("="*60)

        # Ajouter un slide pour les tests
        self.tools["add_slide"](layout_index=6)
        current_slide = len(presentations[get_current_presentation_id()].slides) - 1

        # Ajouter du texte pour tester les hyperlinks
        self.tools["manage_text"](
            operation="add",
            slide_index=current_slide,
            text="Visitez notre site web",
            left=1.0,
            top=1.0,
            width=5.0,
            height=1.0
        )

        # 1. manage_hyperlinks
        self.run_test(
            "Specialized Features",
            "manage_hyperlinks",
            self.tools["manage_hyperlinks"],
            operation="list",
            slide_index=current_slide
        )

        # 2. update_chart_data (sur le chart créé précédemment)
        chart_slide = current_slide - 1  # Slide précédent avec le chart
        self.run_test(
            "Specialized Features",
            "update_chart_data",
            self.tools["update_chart_data"],
            slide_index=chart_slide,
            chart_index=0,
            categories=["Q1", "Q2", "Q3", "Q4"],
            series=[
                {"name": "2023", "values": [110, 130, 150, 170]},
                {"name": "2024", "values": [140, 160, 180, 200]}
            ]
        )

        # 3. add_connector
        self.run_test(
            "Specialized Features",
            "add_connector",
            self.tools["add_connector"],
            slide_index=current_slide,
            connector_type="straight",
            start_x=2.0,
            start_y=3.0,
            end_x=6.0,
            end_y=3.0,
            line_color=[0, 0, 255],
            line_width=2
        )

        # 4. manage_slide_masters
        self.run_test(
            "Specialized Features",
            "manage_slide_masters",
            self.tools["manage_slide_masters"],
            operation="list"
        )

        # 5. manage_slide_transitions
        self.run_test(
            "Specialized Features",
            "manage_slide_transitions",
            self.tools["manage_slide_transitions"],
            operation="list"
        )

        print(f"\n✅ Fonctionnalités spécialisées: Tests complétés")

    def run_all_tests(self):
        """Exécute tous les tests."""
        print("\n" + "="*60)
        print("🚀 DÉMARRAGE DES TESTS - PowerPoint MCP Server")
        print("="*60)
        print(f"Total d'outils à tester: {len(self.tools)}")

        # Exécuter tous les tests par catégorie
        self.test_presentation_management()
        self.test_content_management()
        self.test_template_operations()
        self.test_structural_elements()
        self.test_professional_design()
        self.test_specialized_features()

        # Sauvegarder la présentation finale
        print("\n" + "="*60)
        print("💾 SAUVEGARDE DE LA PRÉSENTATION DE TEST")
        print("="*60)
        self.run_test(
            "Final",
            "save_presentation",
            self.tools["save_presentation"],
            file_path="test_complete_output.pptx"
        )

        # Afficher le résumé
        self.print_summary()

    def print_summary(self):
        """Affiche le résumé des tests."""
        print("\n" + "="*60)
        print("📊 RÉSUMÉ DES TESTS")
        print("="*60)
        print(f"Total de tests: {self.results['total_tests']}")
        print(f"✅ Réussis: {self.results['passed']}")
        print(f"❌ Échoués: {self.results['failed']}")

        success_rate = (self.results['passed'] / self.results['total_tests'] * 100) if self.results['total_tests'] > 0 else 0
        print(f"📈 Taux de réussite: {success_rate:.1f}%")

        if self.results['errors']:
            print("\n❌ ERREURS DÉTECTÉES:")
            for i, error in enumerate(self.results['errors'], 1):
                print(f"\n  {i}. {error['category']} - {error['tool']}")
                print(f"     Erreur: {error['error']}")

        # Vérifier si le fichier a été créé
        output_file = Path("test_complete_output.pptx")
        if output_file.exists():
            file_size = output_file.stat().st_size
            print(f"\n✅ Fichier PowerPoint généré: test_complete_output.pptx ({file_size} bytes)")
        else:
            print("\n⚠️  Le fichier PowerPoint n'a pas été créé")

        print("\n" + "="*60)
        print("🎉 TESTS TERMINÉS")
        print("="*60)


if __name__ == "__main__":
    tester = ToolTester()
    tester.run_all_tests()
