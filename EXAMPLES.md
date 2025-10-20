# Exemples d'Utilisation - PowerPoint MCP Server

Ce document contient des exemples concrets d'utilisation du PowerPoint MCP Server avec Claude Desktop.

## Exemples de Base

### 1. Créer une Présentation Simple

**Demande à Claude:**
```
Crée une nouvelle présentation PowerPoint avec :
1. Un slide de titre "Marketing Strategy 2024"
2. Un slide agenda avec 3 points
3. Sauvegarde-la sous "strategy.pptx"
```

**Ce que Claude va faire:**
1. Appeler `create_presentation()`
2. Appeler `create_slide_from_template()` avec template "title_slide"
3. Appeler `create_slide_from_template()` avec template "agenda_slide"
4. Appeler `save_presentation()` avec le nom de fichier

### 2. Utiliser des Templates Prédéfinis

**Demande à Claude:**
```
Crée une présentation business complète sur "Quarterly Results Q4 2024" avec :
- Slide de titre
- Agenda
- 3 slides de métriques clés
- 2 slides avec graphiques
- Slide de conclusion
Utilise le schéma de couleurs modern_blue
```

**Ce que Claude va faire:**
1. `create_presentation()`
2. Plusieurs appels à `create_slide_from_template()` avec différents templates
3. `apply_professional_design()` avec color_scheme="modern_blue"
4. `save_presentation()`

## Exemples Avancés

### 3. Présentation avec Tableaux et Graphiques

**Demande à Claude:**
```
Crée une présentation d'analyse financière avec :
1. Slide de titre
2. Un tableau comparant les revenus 2023 vs 2024 par trimestre
3. Un graphique en barres montrant l'évolution
4. Une slide de conclusions avec 5 bullet points
```

**Ce que Claude va faire:**
```python
# 1. Créer la présentation
create_presentation(id="financial_analysis")

# 2. Slide de titre
create_slide_from_template(
    template_name="title_slide",
    content={
        "title": "Financial Analysis 2023-2024",
        "subtitle": "Quarterly Revenue Comparison"
    }
)

# 3. Slide avec tableau
add_slide(layout_index=5)
add_table(
    slide_index=1,
    rows=5,
    cols=3,
    left=1.5,
    top=2.0,
    width=7.0,
    height=3.0,
    data=[
        ["Quarter", "2023", "2024"],
        ["Q1", "$1.2M", "$1.5M"],
        ["Q2", "$1.4M", "$1.7M"],
        ["Q3", "$1.6M", "$1.9M"],
        ["Q4", "$1.8M", "$2.2M"]
    ]
)

# 4. Slide avec graphique
add_slide(layout_index=5)
add_chart(
    slide_index=2,
    chart_type="column",
    left=1.5,
    top=2.0,
    width=7.0,
    height=4.0,
    categories=["Q1", "Q2", "Q3", "Q4"],
    series=[
        {"name": "2023", "values": [1.2, 1.4, 1.6, 1.8]},
        {"name": "2024", "values": [1.5, 1.7, 1.9, 2.2]}
    ]
)

# 5. Slide de conclusions
create_slide_from_template(
    template_name="bullet_points",
    content={
        "title": "Key Takeaways",
        "bullets": [
            "22% revenue growth year-over-year",
            "Consistent growth across all quarters",
            "Q4 showed strongest performance",
            "Exceeded targets by 15%",
            "Momentum continues into 2025"
        ]
    }
)

# 6. Sauvegarder
save_presentation(file_path="financial_analysis.pptx")
```

### 4. Présentation avec Images et Design Personnalisé

**Demande à Claude:**
```
Crée une présentation produit avec :
- Design élégant avec le schéma elegant_green
- Slide de titre avec logo
- 3 slides produit avec image et texte côte à côte
- Slide de témoignage client
- Slide de contact
```

**Commandes Claude utilisera:**
```python
# Créer et appliquer le design
create_presentation(id="product_showcase")
apply_professional_design(
    operation="apply_color_scheme",
    color_scheme="elegant_green"
)

# Slide de titre avec image
create_slide_from_template(template_name="title_slide")
manage_image(
    operation="add",
    slide_index=0,
    image_path="logo.png",
    left=8.0,
    top=0.5,
    width=1.5,
    height=1.0
)

# Slides produit
for i in range(3):
    create_slide_from_template(
        template_name="text_with_image",
        content={
            "title": f"Product Feature {i+1}",
            "text": "Description du produit...",
            "image_path": f"product_{i+1}.png"
        }
    )

# Slide de témoignage
create_slide_from_template(
    template_name="quote_testimonial",
    content={
        "quote": "Ce produit a transformé notre business!",
        "author": "John Doe, CEO"
    }
)

# Slide de contact
create_slide_from_template(template_name="thank_you_slide")
```

### 5. Auto-Génération Complète

**Demande à Claude:**
```
Génère automatiquement une présentation de 10 slides sur "Machine Learning Applications in Healthcare" de type academic avec des graphiques
```

**Commande directe:**
```python
auto_generate_presentation(
    topic="Machine Learning Applications in Healthcare",
    presentation_type="academic",
    num_slides=10,
    include_charts=True,
    include_images=True,
    color_scheme="corporate_gray",
    typography_style="elegant_serif"
)
save_presentation(file_path="ml_healthcare.pptx")
```

## Exemples de Templates

### Template: Title Slide

```python
create_slide_from_template(
    template_name="title_slide",
    content={
        "title": "Votre Titre Principal",
        "subtitle": "Sous-titre ou date"
    },
    color_scheme="modern_blue"
)
```

### Template: Agenda Slide

```python
create_slide_from_template(
    template_name="agenda_slide",
    content={
        "title": "Agenda",
        "items": [
            "Introduction",
            "Current Situation",
            "Proposed Solution",
            "Implementation Plan",
            "Q&A"
        ]
    }
)
```

### Template: Two Column Text

```python
create_slide_from_template(
    template_name="two_column_text",
    content={
        "title": "Comparison",
        "left_column": {
            "title": "Before",
            "text": "Points about before..."
        },
        "right_column": {
            "title": "After",
            "text": "Points about after..."
        }
    }
)
```

### Template: Key Metrics Dashboard

```python
create_slide_from_template(
    template_name="key_metrics_dashboard",
    content={
        "title": "Q4 Performance",
        "metrics": [
            {"label": "Revenue", "value": "$2.5M", "change": "+22%"},
            {"label": "Users", "value": "150K", "change": "+35%"},
            {"label": "NPS", "value": "72", "change": "+8"},
            {"label": "Churn", "value": "2.1%", "change": "-0.5%"}
        ]
    }
)
```

## Exemples de Formatage Avancé

### Texte avec Styles Multiples

**Demande à Claude:**
```
Sur le slide 2, ajoute un titre en gras bleu de 32pt, puis un paragraphe normal de 18pt en noir
```

**Commandes:**
```python
manage_text(
    operation="add",
    slide_index=2,
    text="Important Title",
    left=1.0,
    top=1.0,
    width=8.0,
    height=1.0,
    font_name="Arial",
    font_size=32,
    bold=True,
    color_rgb=[0, 120, 215]
)

manage_text(
    operation="add",
    slide_index=2,
    text="This is the main paragraph content...",
    left=1.0,
    top=2.5,
    width=8.0,
    height=3.0,
    font_size=18,
    color_rgb=[0, 0, 0]
)
```

### Images avec Effets

**Demande à Claude:**
```
Ajoute une image avec un effet de contraste élevé et luminosité augmentée
```

**Commande:**
```python
manage_image(
    operation="add_enhanced",
    slide_index=1,
    image_path="photo.jpg",
    left=2.0,
    top=2.0,
    width=6.0,
    height=4.0,
    brightness=1.2,
    contrast=1.5,
    saturation=1.1
)
```

## Workflow Complet : Présentation de Startup Pitch

**Demande à Claude:**
```
Crée une présentation de pitch pour une startup tech avec :
1. Slide de couverture impactante
2. Le problème (avec stats)
3. Notre solution
4. Marché adressable (avec graphique)
5. Business model
6. Équipe
7. Traction (métriques)
8. Ask
Utilise modern_blue et typographie tech_modern
```

**Claude exécutera:**

```python
# Setup
create_presentation(id="startup_pitch")
apply_professional_design(
    operation="apply_color_scheme",
    color_scheme="modern_blue",
    typography_style="tech_modern"
)

# 1. Couverture
create_slide_from_template(
    template_name="title_slide",
    content={
        "title": "TechCorp",
        "subtitle": "Revolutionizing Industry X"
    }
)

# 2. Problème
create_slide_from_template(
    template_name="text_with_image",
    content={
        "title": "The Problem",
        "text": "85% of companies struggle with X\n$50B lost annually\nNo effective solution exists"
    }
)

# 3. Solution
create_slide_from_template(
    template_name="two_column_text",
    content={
        "title": "Our Solution",
        "left_column": {
            "title": "Traditional Approach",
            "text": "Slow, expensive, ineffective"
        },
        "right_column": {
            "title": "TechCorp",
            "text": "Fast, affordable, proven results"
        }
    }
)

# 4. Marché avec graphique
add_slide(layout_index=5)
manage_text(
    operation="add",
    slide_index=3,
    text="Total Addressable Market",
    left=1.0,
    top=0.5,
    width=8.0,
    height=0.8,
    font_size=32,
    bold=True
)
add_chart(
    slide_index=3,
    chart_type="pie",
    left=2.0,
    top=2.0,
    width=6.0,
    height=4.0,
    categories=["TAM", "SAM", "SOM"],
    series=[{"name": "Market Size ($B)", "values": [50, 20, 5]}]
)

# 5. Business Model
create_slide_from_template(
    template_name="three_column_layout",
    content={
        "title": "Business Model",
        "columns": [
            {"title": "Freemium", "text": "Free tier to attract"},
            {"title": "Pro", "text": "$99/mo for teams"},
            {"title": "Enterprise", "text": "Custom pricing"}
        ]
    }
)

# 6. Équipe
create_slide_from_template(
    template_name="text_with_image",
    content={
        "title": "World-Class Team",
        "text": "CEO: Ex-Google, 15 years\nCTO: MIT PhD, AI expert\nCOO: Built 2 successful startups"
    }
)

# 7. Traction
create_slide_from_template(
    template_name="key_metrics_dashboard",
    content={
        "title": "Traction",
        "metrics": [
            {"label": "Users", "value": "50K", "change": "+200%"},
            {"label": "MRR", "value": "$100K", "change": "+150%"},
            {"label": "NPS", "value": "75", "change": "+10"},
            {"label": "Retention", "value": "94%", "change": "+5%"}
        ]
    }
)

# 8. Ask
create_slide_from_template(
    template_name="title_slide",
    content={
        "title": "Raising $5M Series A",
        "subtitle": "Let's build the future together"
    }
)

# Sauvegarder
save_presentation(file_path="techcorp_pitch.pptx")
```

## Conseils d'Utilisation

1. **Commencez Simple**: Créez d'abord une structure basique, puis ajoutez des détails
2. **Utilisez les Templates**: Ils garantissent un design cohérent
3. **Testez les Schémas de Couleurs**: Essayez différents schémas pour trouver le bon
4. **Optimisez le Texte**: Utilisez `optimize_slide_text()` si le texte déborde
5. **Sauvegardez Régulièrement**: Appelez `save_presentation()` après des modifications importantes

## Ressources Utiles

- **Liste des Templates**: Utilisez `list_slide_templates()` pour voir tous les templates
- **Info Serveur**: Utilisez `get_server_info()` pour voir toutes les capacités
- **Info Présentation**: Utilisez `get_presentation_info()` pour vérifier l'état actuel

Bon travail avec PowerPoint MCP Server! 🚀
