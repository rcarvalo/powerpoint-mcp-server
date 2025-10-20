# Guide Complet des Outils MCP PowerPoint

Ce guide liste **TOUS les 32 outils** disponibles dans le PowerPoint MCP Server avec leurs signatures exactes, paramètres, et exemples d'utilisation.

## Table des Matières

1. [Gestion de Présentation (7 outils)](#1-gestion-de-présentation)
2. [Gestion de Contenu (6+ outils)](#2-gestion-de-contenu)
3. [Opérations de Templates (7 outils)](#3-opérations-de-templates)
4. [Éléments Structurels (4 outils)](#4-éléments-structurels)
5. [Design Professionnel (3 outils)](#5-design-professionnel)
6. [Fonctionnalités Spécialisées (5 outils)](#6-fonctionnalités-spécialisées)
7. [Outils Utilitaires (3 outils)](#7-outils-utilitaires)

---

## 1. Gestion de Présentation

### 1.1 `create_presentation`
Crée une nouvelle présentation PowerPoint vierge.

**Paramètres:**
- `id` (Optional[str]): ID personnalisé pour la présentation. Si non fourni, un ID automatique est généré.

**Retour:**
```json
{
  "presentation_id": "string",
  "message": "string",
  "slide_count": 0
}
```

**Exemple d'utilisation:**
```
Crée une nouvelle présentation PowerPoint
```

### 1.2 `create_presentation_from_template`
Crée une présentation à partir d'un fichier template .pptx existant.

**Paramètres:**
- `template_path` (str): Chemin vers le fichier template .pptx
- `id` (Optional[str]): ID pour la nouvelle présentation

**Exemple:**
```
Crée une présentation à partir du template "corporate_template.pptx"
```

### 1.3 `open_presentation`
Ouvre un fichier PowerPoint existant.

**Paramètres:**
- `file_path` (str): Chemin vers le fichier .pptx à ouvrir
- `id` (Optional[str]): ID pour la présentation ouverte

**Exemple:**
```
Ouvre le fichier "rapport_annuel.pptx"
```

### 1.4 `save_presentation`
Sauvegarde la présentation actuelle sur le disque.

**Paramètres:**
- `file_path` (str): Chemin où sauvegarder le fichier .pptx

**Exemple:**
```
Sauvegarde la présentation sous "ma_presentation.pptx"
```

### 1.5 `get_presentation_info`
Récupère les informations et métadonnées de la présentation actuelle.

**Paramètres:** Aucun

**Retour:**
```json
{
  "presentation_id": "string",
  "slide_count": 5,
  "slide_width": 9144000,
  "slide_height": 6858000,
  "core_properties": {
    "title": "string",
    "author": "string",
    "subject": "string"
  }
}
```

**Exemple:**
```
Donne-moi les informations de la présentation actuelle
```

### 1.6 `get_template_file_info`
Obtient des informations sur un fichier template .pptx.

**Paramètres:**
- `template_path` (str): Chemin vers le fichier template

**Exemple:**
```
Montre-moi les informations du template "business_template.pptx"
```

### 1.7 `set_core_properties`
Définit les propriétés du document (métadonnées).

**Paramètres:**
- `title` (Optional[str]): Titre du document
- `subject` (Optional[str]): Sujet
- `author` (Optional[str]): Auteur
- `keywords` (Optional[str]): Mots-clés séparés par des virgules
- `comments` (Optional[str]): Commentaires
- `category` (Optional[str]): Catégorie

**Exemple:**
```
Définis le titre "Rapport Q4 2024", l'auteur "Jean Dupont" et le sujet "Résultats financiers"
```

---

## 2. Gestion de Contenu

### 2.1 `add_slide`
Ajoute un nouveau slide à la présentation.

**Paramètres:**
- `layout_index` (int): Index du layout à utiliser (0-11 généralement)
  - 0: Title Slide
  - 1: Title and Content
  - 5: Title Only
  - 6: Blank
- `background_type` (Optional[str]): Type de fond ("solid" ou "gradient")
- `background_colors` (Optional[List]): Liste de couleurs RGB pour le fond

**Exemple:**
```
Ajoute un slide vierge (layout 6) avec un fond bleu clair
```

### 2.2 `get_slide_info`
Récupère les informations d'un slide spécifique.

**Paramètres:**
- `slide_index` (int): Index du slide (commence à 0)

**Retour:**
```json
{
  "slide_index": 0,
  "layout_name": "Title Slide",
  "shape_count": 2,
  "shapes": [...]
}
```

**Exemple:**
```
Donne-moi les informations du slide 2
```

### 2.3 `extract_slide_text`
Extrait tout le texte d'un slide.

**Paramètres:**
- `slide_index` (int): Index du slide

**Retour:**
```json
{
  "slide_index": 0,
  "text": "Texte extrait...",
  "text_runs": [...]
}
```

**Exemple:**
```
Extrais tout le texte du premier slide
```

### 2.4 `extract_presentation_text`
Extrait tout le texte de la présentation entière.

**Paramètres:** Aucun

**Retour:**
```json
{
  "total_slides": 5,
  "total_characters": 1234,
  "slides_text": [...]
}
```

**Exemple:**
```
Extrais tout le texte de la présentation
```

### 2.5 `populate_placeholder`
Remplit un placeholder d'un slide avec du texte.

**Paramètres:**
- `slide_index` (int): Index du slide
- `placeholder_index` (int): Index du placeholder (0, 1, ...)
- `text` (str): Texte à insérer

**Exemple:**
```
Sur le slide 0, remplis le placeholder 1 avec "Bienvenue"
```

### 2.6 `add_bullet_points`
Ajoute une liste à puces à un slide.

**Paramètres:**
- `slide_index` (int): Index du slide
- `bullet_points` (List[str]): Liste des points
- Paramètres de positionnement et formatage optionnels

**Exemple:**
```
Sur le slide 1, ajoute des bullet points: "Point 1", "Point 2", "Point 3"
```

### 2.7 `manage_text`
Outil unifié pour gérer le texte (ajouter, formater, valider).

**Paramètres:**
- `operation` (str): "add", "format", "validate", "format_runs"
- `slide_index` (int): Index du slide
- `text` (str): Texte à ajouter/modifier
- Position: `left`, `top`, `width`, `height` (en inches)
- Format: `font_name`, `font_size`, `bold`, `italic`, `underline`
- Couleur: `color_rgb` [R, G, B]

**Exemple:**
```
Sur le slide 0, ajoute le texte "Titre Principal" en gras, 32pt, couleur bleue à la position (1, 1) avec taille (8, 1)
```

### 2.8 `manage_image`
Outil unifié pour gérer les images.

**Paramètres:**
- `operation` (str): "add" ou "add_enhanced"
- `slide_index` (int): Index du slide
- `image_path` (str): Chemin vers l'image OU
- `image_base64` (str): Image en base64
- Position: `left`, `top`, `width`, `height`
- Effets (pour add_enhanced): `brightness`, `contrast`, `saturation`, `sharpness`, `blur`

**Exemple:**
```
Sur le slide 2, ajoute l'image "logo.png" à la position (8, 0.5) avec taille (1.5, 1)
```

---

## 3. Opérations de Templates

### 3.1 `list_slide_templates`
Liste tous les templates de slides disponibles.

**Paramètres:** Aucun

**Retour:**
```json
{
  "total_templates": 31,
  "templates": [
    {
      "name": "title_slide",
      "description": "...",
      "required_content": [...]
    }
  ]
}
```

**Exemple:**
```
Montre-moi tous les templates disponibles
```

### 3.2 `get_template_info`
Obtient des informations détaillées sur un template spécifique.

**Paramètres:**
- `template_id` (str): ID du template (ex: "title_slide")

**Exemple:**
```
Donne-moi les détails du template "title_slide"
```

### 3.3 `create_slide_from_template`
Crée un nouveau slide en utilisant un template.

**Paramètres:**
- `template_id` (str): ID du template
- `content` (dict): Contenu spécifique au template
- `color_scheme` (Optional[str]): Schéma de couleurs ("modern_blue", "corporate_gray", etc.)
- `typography_style` (Optional[str]): Style typo ("modern_sans", "elegant_serif", etc.)

**Exemple:**
```
Crée un slide avec le template "title_slide", titre "Ma Présentation", sous-titre "2024", schéma modern_blue
```

### 3.4 `apply_slide_template`
Applique un template à un slide existant.

**Paramètres:**
- `slide_index` (int): Index du slide
- `template_id` (str): ID du template
- `content` (dict): Contenu pour le template

**Exemple:**
```
Applique le template "two_column_text" au slide 2
```

### 3.5 `create_presentation_from_templates`
Crée une présentation complète à partir d'une séquence de templates.

**Paramètres:**
- `template_sequence` (List[dict]): Liste de configurations de templates
- `color_scheme` (Optional[str]): Schéma de couleurs global
- `presentation_id` (Optional[str]): ID de la présentation

**Exemple:**
```
Crée une présentation avec: slide de titre, agenda, 2 slides de contenu, slide de conclusion
```

### 3.6 `auto_generate_presentation`
Génère automatiquement une présentation basée sur un sujet.

**Paramètres:**
- `topic` (str): Sujet de la présentation
- `presentation_type` (str): "business", "academic", ou "creative"
- `num_slides` (int): Nombre de slides (3-20)
- `include_charts` (bool): Inclure des graphiques
- `include_images` (bool): Inclure des placeholders images
- `color_scheme` (Optional[str]): Schéma de couleurs
- `typography_style` (Optional[str]): Style typographique

**Exemple:**
```
Génère automatiquement une présentation de 10 slides sur "Machine Learning" de type academic avec des graphiques
```

### 3.7 `optimize_slide_text`
Optimise le texte d'un slide pour la lisibilité.

**Paramètres:**
- `slide_index` (int): Index du slide
- `min_font_size` (int): Taille minimale de police (défaut: 8)
- `max_font_size` (int): Taille maximale de police (défaut: 36)
- `adjust_line_spacing` (bool): Ajuster l'espacement des lignes

**Exemple:**
```
Optimise le texte du slide 3 avec des tailles entre 10pt et 28pt
```

---

## 4. Éléments Structurels

### 4.1 `add_table`
Ajoute un tableau à un slide.

**Paramètres:**
- `slide_index` (int): Index du slide
- `rows` (int): Nombre de lignes
- `cols` (int): Nombre de colonnes
- Position: `left`, `top`, `width`, `height` (en inches)
- `data` (Optional[List[List[str]]]): Données à insérer
- `first_row_header` (bool): Première ligne en en-tête
- Couleurs: `header_color_rgb`, `body_color_rgb`

**Exemple:**
```
Sur le slide 2, ajoute un tableau 4x3 à (1.5, 2) de taille (7, 3) avec les données: ["Nom", "Prix", "Stock"], ["Produit A", "100€", "50"]...
```

### 4.2 `add_shape`
Ajoute une forme géométrique.

**Paramètres:**
- `slide_index` (int): Index du slide
- `shape_type` (str): Type de forme
  - Basiques: "rectangle", "rounded_rectangle", "oval", "diamond", "triangle"
  - Polygones: "pentagon", "hexagon", "octagon", "star"
  - Flowchart: "flowchart_process", "flowchart_decision", "flowchart_data"
  - Spéciaux: "arrow", "cloud", "heart", "lightning_bolt", "sun", "moon"
- Position: `left`, `top`, `width`, `height`
- Couleurs: `fill_color`, `line_color` [R, G, B]
- `line_width` (float): Épaisseur du contour

**Exemple:**
```
Sur le slide 3, ajoute un rectangle bleu à (2, 2) de taille (3, 2)
```

### 4.3 `add_line`
Dessine une ligne sur un slide.

**Paramètres:**
- `slide_index` (int): Index du slide
- `start_x`, `start_y` (float): Point de départ (inches)
- `end_x`, `end_y` (float): Point d'arrivée (inches)
- `line_color` (List[int]): Couleur [R, G, B]
- `line_width` (float): Épaisseur

**Exemple:**
```
Sur le slide 4, dessine une ligne rouge de (1, 2) à (8, 2) avec épaisseur 3
```

### 4.4 `add_textbox`
Ajoute une zone de texte.

**Paramètres:**
- `slide_index` (int): Index du slide
- `text` (str): Texte
- Position: `left`, `top`, `width`, `height`
- Format: `font_name`, `font_size`, `bold`, `italic`
- Couleurs: `text_color`, `fill_color` [R, G, B]

**Exemple:**
```
Sur le slide 1, ajoute une textbox "Note importante" à (1, 5) de taille (3, 1), police 14pt
```

---

## 5. Design Professionnel

### 5.1 `apply_professional_design`
Applique un design professionnel à la présentation.

**Paramètres:**
- `operation` (str): Type d'opération
  - "apply_color_scheme": Appliquer un schéma de couleurs
  - "apply_theme": Appliquer un thème complet
  - "enhance_slide": Améliorer un slide
  - "get_available_schemes": Lister les schémas disponibles
- `color_scheme` (Optional[str]): Schéma de couleurs
  - "modern_blue", "corporate_gray", "elegant_green", "warm_red"
  - "pastel_dream", "nature_earth", "neon_vibrant", "minimalist_mono"
- `typography_style` (Optional[str]): Style typographique
  - "modern_sans", "elegant_serif", "tech_modern", "organic_flow", "brutalist_bold"
- `slide_index` (Optional[int]): Pour enhance_slide

**Exemple:**
```
Applique le schéma de couleurs "modern_blue" avec le style "modern_sans" à toute la présentation
```

### 5.2 `add_chart`
Ajoute un graphique professionnel.

**Paramètres:**
- `slide_index` (int): Index du slide
- `chart_type` (str): "column", "bar", "line", "pie"
- Position: `left`, `top`, `width`, `height`
- `title` (Optional[str]): Titre du graphique
- `categories` (List[str]): Catégories pour l'axe X
- `series` (List[dict]): Données des séries
  - Chaque série: `{"name": "...", "values": [...]}`

**Exemple:**
```
Sur le slide 3, ajoute un graphique en colonnes à (1.5, 1.5) de taille (7, 4),
titre "Ventes 2024", catégories ["Q1", "Q2", "Q3", "Q4"],
série "Revenus" avec valeurs [100, 120, 150, 180]
```

### 5.3 `format_text_advanced`
Formatage de texte avancé.

**Paramètres:**
- `slide_index` (int): Index du slide
- `shape_index` (int): Index de la forme de texte
- Formatage: `font_name`, `font_size`, `bold`, `italic`, `underline`
- Couleurs: `color_rgb` [R, G, B]
- Effets: `shadow`, `glow`

**Exemple:**
```
Sur le slide 0 forme 0, applique Arial 28pt en gras avec ombre
```

---

## 6. Fonctionnalités Spécialisées

### 6.1 `update_chart_data`
Met à jour les données d'un graphique existant.

**Paramètres:**
- `slide_index` (int): Index du slide
- `chart_index` (int): Index du graphique (défaut: 0)
- `categories` (List[str]): Nouvelles catégories
- `series` (List[dict]): Nouvelles séries de données

**Exemple:**
```
Sur le slide 3 graphique 0, met à jour avec catégories ["Jan", "Feb", "Mar"] et série "Ventes" [50, 60, 70]
```

### 6.2 `manage_hyperlinks`
Gère les hyperliens dans le texte.

**Paramètres:**
- `operation` (str): "add", "remove", "list", "update"
- `slide_index` (int): Index du slide
- `shape_index` (int): Index de la forme texte
- `url` (str): URL pour add/update
- `text_to_link` (Optional[str]): Texte à transformer en lien
- `run_index` (Optional[int]): Index du run de texte

**Exemple:**
```
Sur le slide 1 forme 0, ajoute un hyperlien "https://example.com" au texte "Cliquez ici"
```

### 6.3 `add_connector`
Ajoute une ligne de connexion/flèche.

**Paramètres:**
- `slide_index` (int): Index du slide
- `connector_type` (str): "straight", "elbow", "curved"
- `start_x`, `start_y` (float): Point de départ
- `end_x`, `end_y` (float): Point d'arrivée
- `line_color` (List[int]): Couleur [R, G, B]
- `line_width` (float): Épaisseur

**Exemple:**
```
Sur le slide 2, ajoute un connecteur droit de (2, 3) à (6, 3) en bleu, épaisseur 2
```

### 6.4 `manage_slide_masters`
Accède et gère les slide masters.

**Paramètres:**
- `operation` (str): "list", "get_layouts", "get_properties"
- `master_index` (Optional[int]): Index du master

**Exemple:**
```
Liste tous les slide masters disponibles
```

### 6.5 `manage_slide_transitions`
Gère les transitions entre slides.

**Paramètres:**
- `operation` (str): "set", "remove", "list"
- `slide_index` (Optional[int]): Index du slide
- `transition_type` (Optional[str]): Type de transition

**Exemple:**
```
Liste toutes les transitions disponibles
```

---

## 7. Outils Utilitaires

### 7.1 `list_presentations`
Liste toutes les présentations chargées en mémoire.

**Paramètres:** Aucun

**Retour:**
```json
{
  "presentations": [
    {
      "id": "presentation_1",
      "slide_count": 5,
      "is_current": true
    }
  ],
  "current_presentation_id": "presentation_1",
  "total_presentations": 1
}
```

**Exemple:**
```
Montre-moi toutes les présentations chargées
```

### 7.2 `switch_presentation`
Change de présentation active.

**Paramètres:**
- `presentation_id` (str): ID de la présentation à activer

**Exemple:**
```
Passe à la présentation "presentation_2"
```

### 7.3 `get_server_info`
Obtient des informations complètes sur le serveur.

**Paramètres:** Aucun

**Retour:**
```json
{
  "name": "PowerPoint MCP Server - ChukMCP Edition",
  "version": "2.2.0",
  "total_tools": 32,
  "features": [...],
  "improvements": [...]
}
```

**Exemple:**
```
Donne-moi les informations du serveur PowerPoint MCP
```

---

## Workflows Complets

### Workflow 1: Présentation Commerciale Simple

```
1. Crée une nouvelle présentation
2. Crée un slide avec template "title_slide", titre "Notre Produit 2024"
3. Crée un slide avec template "two_column_text" pour les avantages
4. Sur un nouveau slide vierge, ajoute un tableau 3x3 avec les prix
5. Crée un slide avec template "bullet_points" pour la conclusion
6. Applique le schéma "modern_blue"
7. Sauvegarde sous "produit_2024.pptx"
```

### Workflow 2: Rapport avec Graphiques

```
1. Crée une présentation avec id "rapport_q4"
2. Ajoute un slide de titre
3. Ajoute un slide vierge
4. Sur ce slide, ajoute un graphique en colonnes avec les ventes Q1-Q4
5. Ajoute un autre slide avec un graphique en ligne pour les tendances
6. Définis les propriétés: titre "Rapport Q4", auteur "Finance"
7. Sauvegarde sous "rapport_q4_2024.pptx"
```

### Workflow 3: Génération Automatique

```
1. Génère automatiquement une présentation sur "IA en Healthcare",
   type academic, 8 slides, avec graphiques
2. Applique le schéma "corporate_gray"
3. Optimise le texte de tous les slides
4. Sauvegarde sous "ia_healthcare.pptx"
```

---

## Schémas de Couleurs Disponibles

1. **modern_blue** - Bleu moderne RGB(0,120,215)
2. **corporate_gray** - Gris d'entreprise RGB(68,68,68)
3. **elegant_green** - Vert élégant RGB(70,136,71)
4. **warm_red** - Rouge chaleureux RGB(192,80,77)
5. **pastel_dream** - Tons pastel (violets/roses)
6. **nature_earth** - Tons terre naturels
7. **neon_vibrant** - Couleurs néon vives
8. **minimalist_mono** - Monochrome minimaliste

## Styles Typographiques Disponibles

1. **modern_sans** - Segoe UI / Arial
2. **elegant_serif** - Times New Roman / Georgia
3. **tech_modern** - Arial / Helvetica
4. **organic_flow** - Montserrat / Open Sans
5. **brutalist_bold** - Impact / Arial Black

---

## Bonnes Pratiques

1. **Toujours créer une présentation d'abord** avec `create_presentation()`
2. **Sauvegarder régulièrement** avec `save_presentation()`
3. **Utiliser les templates** pour un design cohérent
4. **Optimiser le texte** si les slides sont trop chargés
5. **Vérifier les indices** (les indices commencent à 0)
6. **Utiliser les schémas de couleurs** pour un look professionnel

## Dépannage

- **"No presentation is currently loaded"** → Créez d'abord une présentation
- **"Slide index out of range"** → Vérifiez le nombre de slides avec `get_presentation_info()`
- **"Template not found"** → Listez les templates avec `list_slide_templates()`
- **"Invalid color RGB"** → Les couleurs doivent être [R, G, B] avec valeurs 0-255

---

**Version:** 2.2.0
**Dernière mise à jour:** Octobre 2024
