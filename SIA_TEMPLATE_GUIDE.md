# Guide d'Utilisation du Template SIA

## 📍 Localisation du Template

Le template SIA est maintenant disponible à deux endroits :

1. **Emplacement original** : `/Users/remicarvalot/project_pro/Office-PowerPoint-MCP-Server/templates/Sia_Template_Master.pptx`
2. **Copie locale** : `/Users/remicarvalot/project_pro/powerpoint-mcp-server/templates/Sia_Template_Master.pptx`

## ⚙️ Configuration

La configuration dans `/Users/remicarvalot/.cursor/mcp.json` est maintenant :

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
      ],
      "env": {
        "PPT_TEMPLATE_PATH": "/Users/remicarvalot/project_pro/Office-PowerPoint-MCP-Server/templates"
      }
    }
  }
}
```

**Note** : La variable `PPT_TEMPLATE_PATH` permet au serveur de chercher automatiquement les templates dans ce dossier.

## 🚀 Comment Utiliser le Template SIA

### Option 1: Créer une Présentation depuis le Template SIA

**Commande à donner à Claude** :
```
Crée une nouvelle présentation à partir du template "Sia_Template_Master.pptx"
```

**Ou plus précisément** :
```
Utilise create_presentation_from_template avec le chemin "Sia_Template_Master.pptx"
```

**L'outil utilisera** :
```python
create_presentation_from_template(
    template_path="Sia_Template_Master.pptx",
    id="ma_presentation_sia"
)
```

### Option 2: Utiliser un Chemin Absolu

**Commande** :
```
Crée une présentation depuis le template situé à "/Users/remicarvalot/project_pro/powerpoint-mcp-server/templates/Sia_Template_Master.pptx"
```

### Option 3: Copier et Modifier

**Workflow complet** :
```
1. Ouvre le template SIA (Sia_Template_Master.pptx)
2. Modifie le slide 1 avec le titre "Mon Projet"
3. Ajoute 3 nouveaux slides
4. Sauvegarde sous "projet_sia_2024.pptx"
```

## 📝 Exemples d'Utilisation avec Claude

### Exemple 1: Présentation d'Appel d'Offre

```
Crée une présentation à partir du template SIA pour répondre à un appel d'offre.
Utilise le template "Sia_Template_Master.pptx" et crée :
1. Slide de titre avec "Réponse AO - SNCF Digital"
2. Slide agenda
3. Slide avec nos références similaires (tableau)
4. Slide équipe proposée
5. Slide conclusion

Applique les couleurs et la charte graphique SIA
```

### Exemple 2: Présentation Business

```
Utilise le template Sia_Template_Master.pptx pour créer une présentation de 8 slides :
- Titre : "Bilan Q4 2024"
- Résumé exécutif
- Métriques clés (tableau)
- Évolution des ventes (graphique)
- Analyse marché
- Recommandations
- Plan d'action
- Conclusion
```

### Exemple 3: Modification d'un Template Existant

```
Ouvre Sia_Template_Master.pptx, récupère le slide master et applique-le à ma présentation actuelle
```

## 🔧 Outils MCP Disponibles pour le Template SIA

### 1. `create_presentation_from_template`
Crée une nouvelle présentation basée sur le template SIA.

**Paramètres** :
- `template_path`: "Sia_Template_Master.pptx" (le serveur cherchera automatiquement dans `/templates/`)
- `id`: Identifiant optionnel pour la présentation

**Exemple** :
```
create_presentation_from_template("Sia_Template_Master.pptx", "presentation_ao")
```

### 2. `get_template_file_info`
Obtient les informations sur le template SIA (layouts disponibles, etc.)

**Exemple** :
```
get_template_file_info("Sia_Template_Master.pptx")
```

### 3. `open_presentation`
Ouvre le template SIA comme présentation

**Exemple** :
```
open_presentation("/Users/remicarvalot/project_pro/powerpoint-mcp-server/templates/Sia_Template_Master.pptx")
```

## 📊 Structure du Template SIA

Le template `Sia_Template_Master.pptx` (12 MB) contient probablement :
- ✅ Charte graphique SIA
- ✅ Couleurs d'entreprise
- ✅ Polices corporate
- ✅ Layouts de slides prédéfinis
- ✅ Logos et éléments de marque
- ✅ Slide masters personnalisés

## 💡 Conseils d'Utilisation

### 1. Préserver la Charte Graphique
Lorsque vous créez depuis le template SIA, tous les slides héritent automatiquement de la charte graphique.

### 2. Réutiliser les Layouts
Le template contient des layouts prédéfinis. Listez-les avec :
```
get_template_file_info("Sia_Template_Master.pptx")
```

### 3. Créer des Variantes
```
1. Crée depuis le template SIA
2. Modifie le contenu
3. Sauvegarde sous un nouveau nom
4. Le template original reste intact
```

## 🎯 Workflow Recommandé pour Appels d'Offre

```python
# 1. Créer depuis le template SIA
create_presentation_from_template(
    template_path="Sia_Template_Master.pptx",
    id="reponse_ao_client_2024"
)

# 2. Modifier le contenu
# Les slides gardent automatiquement la charte SIA

# 3. Ajouter du contenu personnalisé
add_slide(layout_index=1)  # Utilise un layout du template
manage_text(...)
add_table(...)

# 4. Sauvegarder
save_presentation("Reponse_AO_Client_2024.pptx")
```

## 🔍 Dépannage

### Le template n'est pas trouvé
**Vérifiez** :
```bash
ls -lh /Users/remicarvalot/project_pro/powerpoint-mcp-server/templates/
```

**Devrait afficher** :
```
Sia_Template_Master.pptx (12M)
```

### Utiliser le chemin complet
Si le template n'est pas trouvé automatiquement :
```python
create_presentation_from_template(
    template_path="/Users/remicarvalot/project_pro/powerpoint-mcp-server/templates/Sia_Template_Master.pptx"
)
```

### Vérifier la variable d'environnement
Le serveur cherche dans `PPT_TEMPLATE_PATH` qui est configuré dans `mcp.json`.

## 📁 Organisation des Templates

```
powerpoint-mcp-server/
├── templates/
│   └── Sia_Template_Master.pptx  ← Template SIA (12 MB)
├── presentations/                 ← Présentations générées (vide au départ)
└── server.py
```

## 🚀 Commandes Rapides

### Créer depuis SIA
```
Crée une présentation depuis Sia_Template_Master.pptx
```

### Lister les layouts du template
```
Montre-moi les layouts disponibles dans Sia_Template_Master.pptx
```

### Créer et personnaliser
```
Crée une présentation depuis le template SIA, ajoute 5 slides personnalisés,
et sauvegarde sous "ma_presentation.pptx"
```

---

**Template Location**: `/Users/remicarvalot/project_pro/powerpoint-mcp-server/templates/Sia_Template_Master.pptx`
**Size**: 12 MB
**Status**: ✅ Prêt à l'emploi
