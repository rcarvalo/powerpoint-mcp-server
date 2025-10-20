# 🚀 Guide de déploiement rapide

## Déployer les changements sur Render

### Option 1 : Redéploiement automatique via Git (Recommandé)

```bash
cd /Users/remicarvalot/project_pro/powerpoint-mcp-server

# Ajouter les nouveaux fichiers
git add openapi.json OPENAI_INTEGRATION.md DEPLOY.md requirements.txt render.yaml run_server.py

# Commit
git commit -m "Add OpenAI Agent Builder support with OpenAPI spec"

# Push vers votre repo
git push origin main
```

Render redéploiera automatiquement (si auto-deploy est activé).

---

### Option 2 : Déploiement manuel via Render Dashboard

1. Allez sur [dashboard.render.com](https://dashboard.render.com)
2. Sélectionnez votre service **powerpoint-mcp-server**
3. Cliquez sur **"Manual Deploy"** → **"Deploy latest commit"**
4. Attendez 2-3 minutes

---

### Option 3 : Redéploiement via Render CLI

```bash
# Installer Render CLI
npm install -g @render/cli

# Se connecter
render login

# Déployer
render deploy
```

---

## Vérification après déploiement

```bash
# 1. Health check
curl https://powerpoint-mcp-server.onrender.com/health

# 2. Vérifier OpenAPI spec
curl https://powerpoint-mcp-server.onrender.com/openapi.json

# 3. Tester un outil
curl -X POST https://powerpoint-mcp-server.onrender.com/mcp/call \
  -H "Content-Type: application/json" \
  -d '{"tool_name": "create_presentation", "arguments": {}}'
```

---

## Utilisation dans OpenAI Agent Builder

Une fois déployé, suivez le guide [OPENAI_INTEGRATION.md](OPENAI_INTEGRATION.md) :

1. Créer un nouveau GPT
2. Ajouter une Action
3. Importer depuis URL : `https://powerpoint-mcp-server.onrender.com/openapi.json`
4. Tester !

---

## Troubleshooting

### Le serveur ne démarre pas

**Vérifier les logs Render :**
```
Dashboard → Votre service → Logs
```

### L'OpenAPI spec n'est pas accessible

**Vérifier que le fichier existe :**
```bash
ls -la openapi.json
```

**Redéployer manuellement si nécessaire.**

### Cold start lent (Free tier)

C'est normal ! Render Free tier s'endort après 15min.
- Premier appel : 30-60s
- Solution : Plan Starter ($7/mois)

---

## URL importantes

- **Production** : https://powerpoint-mcp-server.onrender.com
- **OpenAPI Spec** : https://powerpoint-mcp-server.onrender.com/openapi.json
- **Health** : https://powerpoint-mcp-server.onrender.com/health
- **Dashboard Render** : https://dashboard.render.com
