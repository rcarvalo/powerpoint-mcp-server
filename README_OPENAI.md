# ✨ Utilisation avec OpenAI Agent Builder

## 🎯 Résumé rapide

Votre serveur PowerPoint MCP est maintenant **100% compatible avec OpenAI Agent Builder** !

### URL de votre API
```
https://powerpoint-mcp-server.onrender.com/openapi.json
```

---

## 🚀 Démarrage rapide (3 étapes)

### 1️⃣ Créer votre GPT sur OpenAI

Allez sur [platform.openai.com](https://platform.openai.com) → **"Create GPT"**

### 2️⃣ Configurer les Instructions

Copiez-collez ces instructions dans votre GPT :

```
Tu es un assistant expert en création de présentations PowerPoint professionnelles.

WORKFLOW :
1. Créer une présentation avec create_presentation
2. Récupérer le presentation_id
3. Ajouter des slides avec add_slide
4. Ajouter du contenu (texte, images, graphiques)
5. Sauvegarder avec save_presentation

Tu as accès à 32 outils PowerPoint via l'API. Utilise listTools pour les découvrir.

Sois créatif, professionnel et propose toujours des designs attrayants !
```

### 3️⃣ Ajouter l'Action API

Dans **"Actions"** → **"Import from URL"** :

```
https://powerpoint-mcp-server.onrender.com/openapi.json
```

Authentification : **None**

---

## ✅ C'est prêt !

Testez avec ce prompt :
```
Crée-moi une présentation PowerPoint de 3 slides sur l'IA
```

---

## 📚 Documentation complète

- **Guide d'intégration détaillé** : [OPENAI_INTEGRATION.md](OPENAI_INTEGRATION.md)
- **Guide de déploiement** : [DEPLOY.md](DEPLOY.md)
- **README principal** : [README.md](README.md)

---

## 🛠️ Outils disponibles (32)

Votre GPT a accès à tous ces outils :

### Création & Gestion
- `create_presentation` - Créer nouvelle présentation
- `save_presentation` - Sauvegarder en .pptx
- `add_slide` - Ajouter un slide
- `get_presentation_info` - Infos présentation

### Contenu
- `manage_text` - Gérer texte
- `manage_image` - Gérer images
- `add_bullet_points` - Ajouter puces
- `populate_placeholder` - Remplir placeholders

### Design
- `apply_slide_template` - Appliquer template
- `apply_professional_design` - Appliquer thème
- `format_text_advanced` - Formatage avancé

### Éléments
- `add_chart` - Ajouter graphique
- `add_table` - Ajouter tableau
- `add_shape` - Ajouter forme

Et 18 autres outils ! Utilisez `listTools` pour tout voir.

---

## 🎨 31+ Templates disponibles

- `title_slide` - Page de titre
- `agenda_slide` - Agenda
- `text_with_image` - Texte + image
- `two_column_text` - Deux colonnes
- `key_metrics_dashboard` - Dashboard
- `chart_comparison` - Comparaison
- Et 25 autres...

### 8 Schémas de couleurs
1. modern_blue
2. corporate_gray
3. elegant_green
4. warm_red
5. pastel_dream
6. nature_earth
7. neon_vibrant
8. minimalist_mono

---

## 🔧 Exemple complet

**Prompt utilisateur :**
```
Crée une présentation de 4 slides sur le marketing digital avec le template moderne bleu
```

**Le GPT va :**
1. Appeler `create_presentation` → obtenir `pres_1`
2. Appeler `list_slide_templates` → voir templates
3. Appeler `create_slide_from_template` avec `modern_blue_title`
4. Ajouter 3 autres slides avec contenu
5. Appeler `save_presentation` → retourner le fichier

---

## ⚠️ Important à savoir

### Cold Start (Plan Free Render)
- Premier appel peut prendre **30-60 secondes**
- Le serveur s'endort après 15min d'inactivité
- Solution : Plan Starter Render ($7/mois)

### Persistance
- Les présentations sont **en mémoire**
- Elles disparaissent si le serveur redémarre
- Toujours sauvegarder rapidement avec `save_presentation`

### Limites
- Plan Free Render : 750h/mois
- Pas de limite sur le nombre d'appels API
- Limite OpenAI : selon votre abonnement

---

## 🆘 Problèmes courants

### "Error calling API"
→ Le serveur Render est en cold start. Attendez 30-60s.

### "presentation_id not found"
→ Le serveur a redémarré. Recréez une présentation.

### "Timeout"
→ Cold start. Premier appel est lent sur Free tier.

---

## 💡 Tips & Astuces

1. **Commencez toujours par `listTools`** pour découvrir tous les outils
2. **Gardez le presentation_id** entre les appels
3. **Utilisez les templates** pour des designs pro instantanés
4. **Sauvegardez régulièrement** (le serveur peut redémarrer)
5. **Soyez spécifique** dans vos prompts pour de meilleurs résultats

---

## 📞 Support

- **Documentation MCP** : https://modelcontextprotocol.io
- **OpenAI Docs** : https://platform.openai.com/docs
- **Render Docs** : https://render.com/docs

---

## 🎉 Vous êtes prêt !

Votre serveur PowerPoint est maintenant accessible depuis OpenAI Agent Builder.

**Prochaines étapes :**
1. ✅ Créer votre GPT
2. ✅ Importer l'OpenAPI spec
3. ✅ Tester avec des prompts simples
4. ✅ Partager avec votre équipe
5. ✅ Créer des présentations automatiquement !

---

**Besoin d'aide ?** Consultez [OPENAI_INTEGRATION.md](OPENAI_INTEGRATION.md) pour le guide complet.
