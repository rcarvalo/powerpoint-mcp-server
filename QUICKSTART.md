# Quick Start Guide - PowerPoint MCP Server

## Installation Rapide

### Option 1: Utilisation Locale avec Claude Desktop

1. **Installer les dépendances**
```bash
cd /Users/remicarvalot/project_pro/powerpoint-mcp-server
uv sync
```

2. **Configurer Claude Desktop**

Éditez votre fichier de configuration Claude Desktop :
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

Ajoutez cette configuration :
```json
{
  "mcpServers": {
    "powerpoint": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/remicarvalot/project_pro/powerpoint-mcp-server",
        "run",
        "python",
        "server.py"
      ]
    }
  }
}
```

3. **Redémarrer Claude Desktop**

C'est tout! Vous avez maintenant accès à 32 outils PowerPoint.

### Option 2: Docker (Production)

1. **Lancer avec Docker Compose**
```bash
cd /Users/remicarvalot/project_pro/powerpoint-mcp-server
docker compose up -d
```

2. **Vérifier que ça fonctionne**
```bash
curl http://localhost:8000/health
```

Vous devriez voir:
```json
{"status":"healthy","server":"ChukMCPServer","timestamp":...,"uptime":...}
```

3. **Arrêter le serveur**
```bash
docker compose down
```

## Exemples d'Utilisation

Une fois connecté à Claude Desktop, vous pouvez demander :

### Créer une Présentation
```
"Crée une nouvelle présentation PowerPoint sur l'Intelligence Artificielle"
```

### Utiliser des Templates
```
"Crée une présentation avec un slide de titre, un agenda, et 3 slides de contenu en utilisant le template business"
```

### Appliquer des Styles
```
"Applique le schéma de couleurs modern_blue à la présentation"
```

### Ajouter du Contenu
```
"Ajoute un slide avec un tableau comparant 3 produits"
"Ajoute un graphique montrant les résultats du Q1 au Q4"
"Ajoute une slide avec une image et du texte à côté"
```

### Sauvegarder
```
"Sauvegarde la présentation sous le nom 'ma-presentation.pptx'"
```

## Outils Disponibles (32 Total)

### Gestion de Présentations (7 outils)
- `create_presentation` - Créer une nouvelle présentation
- `create_presentation_from_template` - Créer depuis un template
- `open_presentation` - Ouvrir un fichier .pptx
- `save_presentation` - Sauvegarder
- `get_presentation_info` - Obtenir les métadonnées
- `set_core_properties` - Définir titre, auteur, etc.

### Gestion de Contenu (6 outils)
- `add_slide` - Ajouter des slides
- `manage_text` - Gérer le texte
- `manage_image` - Ajouter/modifier des images
- `add_bullet_points` - Ajouter des listes à puces
- `extract_slide_text` - Extraire le texte

### Templates (7 outils)
- `list_slide_templates` - Lister les 31+ templates
- `apply_slide_template` - Appliquer un template
- `create_slide_from_template` - Créer depuis template
- `auto_generate_presentation` - Génération automatique
- `optimize_slide_text` - Optimiser la lisibilité

### Éléments Structurels (4 outils)
- `add_table` - Ajouter des tableaux
- `add_shape` - Ajouter 20+ types de formes
- `add_line` - Dessiner des lignes
- `add_textbox` - Ajouter des zones de texte

### Design Professionnel (3 outils)
- `apply_professional_design` - Appliquer des thèmes
- `add_chart` - Ajouter des graphiques
- `format_text_advanced` - Formatage avancé

### Fonctionnalités Spécialisées (5 outils)
- `update_chart_data` - Mettre à jour les données des graphiques
- `manage_hyperlinks` - Gérer les liens hypertexte
- `add_connector` - Ajouter des connecteurs
- `manage_slide_masters` - Gérer les masques
- `manage_slide_transitions` - Gérer les transitions

## Templates Disponibles

### Templates de Slides (31+)
- title_slide - Slide de titre
- agenda_slide - Agenda/sommaire
- text_with_image - Texte + image
- two_column_text - 2 colonnes
- key_metrics_dashboard - Tableau de bord KPI
- chart_comparison - Comparaison avec graphiques
- thank_you_slide - Slide de remerciement
- data_table_slide - Tableau de données
- full_image_slide - Image pleine page
- three_column_layout - 3 colonnes
- quote_testimonial - Citation/témoignage
- process_flow - Flux de processus
- et 19+ autres...

### Schémas de Couleurs (8)
1. **modern_blue** - Bleu moderne et professionnel
2. **corporate_gray** - Gris d'entreprise élégant
3. **elegant_green** - Vert élégant
4. **warm_red** - Rouge chaleureux
5. **pastel_dream** - Tons pastel doux
6. **nature_earth** - Tons terre naturels
7. **neon_vibrant** - Couleurs néon vives
8. **minimalist_mono** - Monochrome minimaliste

### Styles Typographiques (5)
1. **modern_sans** - Segoe UI (moderne)
2. **elegant_serif** - Times/Georgia (élégant)
3. **tech_modern** - Arial/Helvetica (tech)
4. **organic_flow** - Montserrat/Open Sans (fluide)
5. **brutalist_bold** - Impact/Arial Black (audacieux)

## Configuration Avancée

### Répertoires de Templates Personnalisés

Vous pouvez définir vos propres répertoires de templates :

```bash
# macOS/Linux
export PPT_TEMPLATE_PATH="/chemin/vers/templates:/autre/chemin"

# Windows
set PPT_TEMPLATE_PATH="C:\templates;D:\plus-templates"
```

### Mode HTTP Local

Pour tester le serveur en mode HTTP localement :

```bash
uv run python server.py --http --port 8000
```

Puis testez avec curl :
```bash
curl http://localhost:8000/health
```

## Dépannage

### Le serveur ne démarre pas dans Claude Desktop

1. Vérifiez que le chemin est correct dans la config
2. Vérifiez que `uv` est installé : `which uv`
3. Vérifiez les logs de Claude Desktop

### Docker ne fonctionne pas

```bash
# Vérifier les logs
docker compose logs

# Reconstruire l'image
docker compose down
docker compose build --no-cache
docker compose up -d
```

### Problèmes de permissions

```bash
# Donner les permissions d'exécution
chmod +x server.py
```

## Support

Pour des questions ou problèmes :
- Voir le [README.md](README.md) complet
- Vérifier les logs : `docker compose logs` ou logs de Claude Desktop
- Issues GitHub pour ChukMCPServer ou Office-PowerPoint-MCP-Server

## Prochaines Étapes

1. Essayez de créer votre première présentation
2. Explorez les différents templates disponibles
3. Testez les différents schémas de couleurs
4. Créez vos propres templates personnalisés
5. Déployez en production avec Docker si nécessaire

Bon travail avec PowerPoint MCP Server! 🎉
