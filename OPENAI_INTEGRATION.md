# 🤖 Intégration avec OpenAI Agent Builder

Guide complet pour utiliser votre serveur PowerPoint MCP avec OpenAI Agent Builder via Actions.

## 📋 Prérequis

- Compte OpenAI avec accès à GPT-4 et Agent Builder
- Votre serveur déployé sur Render : `https://powerpoint-mcp-server.onrender.com`
- Le fichier OpenAPI spec disponible à : `https://powerpoint-mcp-server.onrender.com/openapi.json`

---

## 🚀 Étapes d'intégration

### 1. Accéder à OpenAI Agent Builder

1. Allez sur [platform.openai.com](https://platform.openai.com)
2. Naviguez vers **"Assistants"** ou **"GPTs"**
3. Cliquez sur **"Create"** pour créer un nouveau GPT/Assistant

### 2. Configurer votre GPT

**Nom suggéré :** PowerPoint Creator Assistant

**Description :**
```
Je suis un assistant spécialisé dans la création de présentations PowerPoint professionnelles.
Je peux créer des présentations complètes, ajouter des slides, appliquer des templates,
ajouter du contenu (texte, images, graphiques, tableaux), et bien plus encore.
```

**Instructions :**
```
Tu es un assistant expert en création de présentations PowerPoint. Tu utilises l'API PowerPoint
pour créer des présentations professionnelles.

WORKFLOW STANDARD :
1. Toujours commencer par créer une présentation avec create_presentation
2. Récupérer le presentation_id retourné
3. Ajouter des slides avec add_slide en utilisant ce presentation_id
4. Ajouter du contenu (texte, images, graphiques)
5. Sauvegarder avec save_presentation

OUTILS DISPONIBLES :
- create_presentation : Créer une nouvelle présentation
- add_slide : Ajouter un slide
- manage_text : Ajouter/modifier du texte
- manage_image : Ajouter des images
- add_chart : Ajouter des graphiques
- add_table : Ajouter des tableaux
- apply_slide_template : Appliquer des templates prédéfinis
- save_presentation : Sauvegarder (retourne le fichier .pptx)

Et 25+ autres outils disponibles via listTools.

IMPORTANT :
- Toujours utiliser listTools en premier pour découvrir tous les outils
- Conserver les presentation_id entre les appels
- Proposer des designs professionnels et visuellement attrayants
- Demander confirmation avant de sauvegarder
```

### 3. Ajouter l'Action API

1. Allez dans l'onglet **"Actions"**
2. Cliquez sur **"Create new action"**
3. Sélectionnez **"Import from URL"**

#### Option A : Importer depuis URL (Recommandé)

Collez cette URL :
```
https://powerpoint-mcp-server.onrender.com/openapi.json
```

#### Option B : Coller le schema manuellement

Si l'import URL ne fonctionne pas, copiez-collez le contenu du fichier `openapi.json` dans le champ schema.

### 4. Configuration de l'authentification

**Type d'authentification :** `None` (API publique)

Si vous souhaitez sécuriser votre API plus tard, vous pouvez ajouter :
- API Key authentication
- OAuth 2.0

### 5. Tester l'intégration

Dans le playground de votre GPT, testez avec :

```
Crée-moi une présentation PowerPoint sur l'intelligence artificielle avec 5 slides :
1. Page de titre
2. Qu'est-ce que l'IA ?
3. Applications de l'IA
4. Avantages et défis
5. Conclusion
```

---

## 🔧 Exemples d'utilisation

### Exemple 1 : Présentation simple

**Prompt utilisateur :**
```
Crée une présentation de 3 slides sur le marketing digital
```

**Actions exécutées par le GPT :**
```json
// 1. Créer la présentation
POST /mcp/call
{
  "tool_name": "create_presentation",
  "arguments": {}
}
// Résultat: {"presentation_id": "pres_1"}

// 2. Ajouter slide de titre
POST /mcp/call
{
  "tool_name": "add_slide",
  "arguments": {
    "presentation_id": "pres_1",
    "layout_index": 0,
    "title": "Marketing Digital 2024"
  }
}

// 3. Ajouter slide de contenu
POST /mcp/call
{
  "tool_name": "add_slide",
  "arguments": {
    "presentation_id": "pres_1",
    "layout_index": 1,
    "title": "Stratégies principales"
  }
}

// 4. Sauvegarder
POST /mcp/call
{
  "tool_name": "save_presentation",
  "arguments": {
    "presentation_id": "pres_1",
    "filename": "marketing_digital.pptx"
  }
}
```

### Exemple 2 : Présentation avec templates

**Prompt utilisateur :**
```
Utilise le template moderne bleu et crée une présentation de 4 slides
```

**Actions :**
```json
// 1. Lister les templates disponibles
POST /mcp/call
{
  "tool_name": "list_slide_templates",
  "arguments": {}
}

// 2. Créer avec le template choisi
POST /mcp/call
{
  "tool_name": "create_slide_from_template",
  "arguments": {
    "template_name": "modern_blue_title",
    "presentation_id": "pres_1"
  }
}
```

---

## 📊 Outils disponibles (32 au total)

Utilisez **listTools** dans votre GPT pour voir la liste complète :

```json
POST /mcp/call
{
  "tool_name": "listTools",
  "arguments": {}
}
```

### Catégories principales :

1. **Gestion des présentations (7 outils)**
   - `create_presentation` - Créer nouvelle présentation
   - `save_presentation` - Sauvegarder
   - `open_presentation` - Ouvrir existante
   - `get_presentation_info` - Info

2. **Gestion du contenu (6 outils)**
   - `add_slide` - Ajouter slide
   - `manage_text` - Gérer texte
   - `manage_image` - Gérer images
   - `add_bullet_points` - Ajouter puces

3. **Templates (7 outils)**
   - `list_slide_templates` - Lister templates
   - `apply_slide_template` - Appliquer template
   - `auto_generate_presentation` - Génération auto

4. **Éléments structurels (4 outils)**
   - `add_table` - Ajouter tableau
   - `add_shape` - Ajouter forme
   - `add_chart` - Ajouter graphique

5. **Design professionnel (3 outils)**
   - `apply_professional_design` - Appliquer thème
   - `format_text_advanced` - Formatage avancé

6. **Fonctionnalités spécialisées (5 outils)**
   - `manage_hyperlinks` - Liens
   - `add_connector` - Connecteurs
   - `manage_slide_transitions` - Transitions

---

## 🎨 Templates et thèmes disponibles

### 31+ templates de slides

- `title_slide` - Page de titre
- `agenda_slide` - Agenda
- `text_with_image` - Texte + image
- `two_column_text` - Deux colonnes
- `key_metrics_dashboard` - Dashboard métriques
- `chart_comparison` - Comparaison graphiques
- `thank_you_slide` - Merci
- Et 24 autres...

### 8 schémas de couleurs

1. `modern_blue` - Bleu moderne
2. `corporate_gray` - Gris corporate
3. `elegant_green` - Vert élégant
4. `warm_red` - Rouge chaleureux
5. `pastel_dream` - Pastel
6. `nature_earth` - Terre naturelle
7. `neon_vibrant` - Néon vibrant
8. `minimalist_mono` - Mono minimaliste

### 5 styles typographiques

1. `modern_sans` - Sans-serif moderne
2. `elegant_serif` - Serif élégant
3. `tech_modern` - Tech moderne
4. `organic_flow` - Organique fluide
5. `brutalist_bold` - Brutalist audacieux

---

## 🐛 Troubleshooting

### Problème : "Error calling API"

**Solution :**
- Vérifiez que votre serveur Render est bien démarré
- Testez l'endpoint manuellement : `curl https://powerpoint-mcp-server.onrender.com/health`
- Vérifiez les logs Render

### Problème : "presentation_id not found"

**Solution :**
- Le serveur Render redémarre et perd la mémoire (plan Free)
- Recréez une présentation au début de chaque session
- Considérez un plan payant Render pour persistance

### Problème : "Timeout"

**Solution :**
- Le plan Free Render s'endort après 15min d'inactivité
- Premier appel peut prendre 30-60s (cold start)
- Utilisez le plan Starter ($7/mois) pour éviter le sleep

### Problème : "Tool not found"

**Solution :**
- Appelez `listTools` d'abord pour voir les outils disponibles
- Vérifiez l'orthographe exacte du tool_name
- Les noms sont sensibles à la casse

---

## 🔒 Sécurisation (Optionnelle)

Pour sécuriser votre API :

### Option 1 : Ajouter une API Key

1. Modifiez `run_server.py` pour vérifier une API key dans les headers
2. Ajoutez la key dans les secrets OpenAI
3. Configurez l'authentification dans OpenAI Actions

### Option 2 : Limiter les IPs

Dans Render, configurez les restrictions IP pour n'autoriser que les IPs OpenAI.

---

## 💰 Coûts

### Render (Hébergement)

- **Free Tier** : 750h/mois, sleep après 15min
- **Starter** : $7/mois, pas de sleep, SSL
- **Pro** : $25/mois, auto-scaling

### OpenAI

- **ChatGPT Plus** : $20/mois (accès GPTs)
- **API Usage** : Selon consommation GPT-4

---

## 📚 Ressources

- **Documentation OpenAPI** : `https://powerpoint-mcp-server.onrender.com/openapi.json`
- **Health check** : `https://powerpoint-mcp-server.onrender.com/health`
- **Liste des outils** : `https://powerpoint-mcp-server.onrender.com/mcp/tools`
- **Serveur info** : `https://powerpoint-mcp-server.onrender.com/mcp/server-info`

---

## ✅ Checklist de déploiement

- [ ] Serveur déployé sur Render
- [ ] Endpoint `/openapi.json` accessible
- [ ] Health check fonctionne
- [ ] GPT créé dans OpenAI
- [ ] Action API importée
- [ ] Test simple réussi
- [ ] Instructions GPT configurées
- [ ] Documentation partagée avec l'équipe

---

## 🎯 Prochaines étapes

1. **Tester** votre GPT avec différents prompts
2. **Personnaliser** les instructions selon vos besoins
3. **Partager** votre GPT avec votre équipe (si plan Team)
4. **Monitorer** l'usage dans Render Dashboard
5. **Améliorer** en ajoutant plus d'outils si nécessaire

---

**Besoin d'aide ?**
- GitHub Issues : [Votre repo]
- Documentation MCP : https://modelcontextprotocol.io
- OpenAI Docs : https://platform.openai.com/docs
