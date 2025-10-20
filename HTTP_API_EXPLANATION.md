# PowerPoint MCP Server - Usage Guide

## 🎯 Overview

Le serveur PowerPoint MCP fournit 32 outils pour manipuler les présentations PowerPoint. Il fonctionne selon deux modes :

### 1. **Mode Cursor/Claude (Recommandé)**
Le serveur fonctionne en mode **stdio** et communique directement avec Cursor/Claude via le protocole MCP.

**Configuration dans `~/.cursor/mcp.json` :**
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
        "PPT_TEMPLATE_PATH": "/Users/remicarvalot/project_pro/powerpoint-mcp-server/templates"
      }
    }
  }
}
```

**Utilisation :**
- Les 32 outils sont disponibles automatiquement dans Cursor
- Pas d'endpoints HTTP REST à appeler
- Communication directe via MCP protocol

### 2. **Mode HTTP/Cloud (Fly.io)**
Le serveur expose des endpoints HTTP pour:
- Health checks (`/health`)
- Information serveur (`/`, `/mcp`, `/mcp/server-info`)
- Documentation API (`/docs`)

**Endpoints disponibles :**
```
GET  /health                        - Health check
GET  /                              - Server info
GET  /mcp                           - MCP API root with documentation
GET  /mcp/tools                     - List available tools (endpoint disponible localement)
POST /mcp/call                      - Call a tool (endpoint disponible localement)
GET  /mcp/presentations             - List presentations
POST /mcp/presentations/select/{id} - Select presentation
GET  /mcp/presentations/{id}/info   - Get presentation info
GET  /mcp/server-info               - Detailed server info
```

**URL en production :**
```
https://powerpoint-mcp-server-delicate-surf-2694.fly.dev/
```

---

## 📋 Les 32 Outils Disponibles

### Presentation Management (7 tools)
- `create_presentation` - Create new presentation
- `open_presentation` - Open existing presentation file
- `save_presentation` - Save presentation to file
- `get_presentation_info` - Get presentation metadata
- `list_presentations` - List all loaded presentations
- `switch_presentation` - Switch between presentations
- `get_server_info` - Get detailed server information

### Content Management (6 tools)
- `manage_text` - Add, edit, and format text
- `populate_placeholder` - Fill placeholder elements with text
- `add_bullet_points` - Add bulleted list content
- `manage_image` - Add and enhance images with effects
- `add_table` - Create formatted tables
- `add_chart` - Create charts with data

### Template Operations (7 tools)
- `create_presentation_from_template` - Create from template file
- `create_slide_from_template` - Create slide from template
- `apply_slide_template` - Apply template to existing slide
- `list_slide_templates` - List available templates
- `get_template_info` - Get template metadata
- `create_presentation_from_templates` - Create from template sequence
- `auto_generate_presentation` - Auto-generate presentation

### Structural Elements (4 tools)
- `add_slide` - Add new slide
- `add_shape` - Add shapes (rectangle, circle, etc.)
- `add_connector` - Add connector lines/arrows
- `manage_slide_masters` - Access slide masters

### Professional Design (3 tools)
- `apply_professional_design` - Apply professional styling
- `apply_picture_effects` - Apply image effects
- `optimize_slide_text` - Optimize text layout

### Specialized Features (5 tools)
- `manage_hyperlinks` - Add/remove hyperlinks
- `update_chart_data` - Update chart data
- `manage_fonts` - Font management
- `manage_slide_transitions` - Slide transitions
- `set_core_properties` - Document metadata

---

## 🚀 Usage Examples

### Example 1: Using via Cursor (Recommended)
```
User: Create a PowerPoint presentation with title "My Presentation" and add a slide with text "Hello World"

Claude can now call:
1. create_presentation() 
2. add_slide(presentation_id, layout_index=0, title="My Presentation")
3. populate_placeholder(slide_index=0, placeholder_idx=1, text="Hello World")
4. save_presentation(presentation_id, "output.pptx")
```

### Example 2: Using Local Docker
```bash
cd /Users/remicarvalot/project_pro/powerpoint-mcp-server
docker compose up -d

# Then use the endpoints locally
curl http://localhost:8000/health
curl http://localhost:8000/mcp/server-info
```

### Example 3: Using Cloud Endpoint
```bash
# Health check
curl https://powerpoint-mcp-server-delicate-surf-2694.fly.dev/health

# Get server info
curl https://powerpoint-mcp-server-delicate-surf-2694.fly.dev/mcp/server-info

# List available endpoints
curl https://powerpoint-mcp-server-delicate-surf-2694.fly.dev/mcp
```

---

## 🔧 Configuration

### Template Path
- **Local:** `/Users/remicarvalot/project_pro/powerpoint-mcp-server/templates/Sia_Template_Master.pptx`
- **Docker:** `/app/templates/Sia_Template_Master.pptx`

### Environment Variables
- `PPT_TEMPLATE_PATH` - Path to template directory (for Cursor)
- `HOST` - Server host (default: 0.0.0.0)
- `PORT` - Server port (default: 8000)

---

## 📊 Deployment

### Local Docker
```bash
docker compose up -d
```

### Cloud (Fly.io)
```bash
fly deploy
```

### View Logs
```bash
# Local
docker compose logs -f

# Cloud
fly logs -a powerpoint-mcp-server-delicate-surf-2694
```

---

## ⚠️ Important Notes

1. **Cursor Usage (Recommended)**
   - Outils disponibles directement dans Cursor
   - Pas d'authentification requise
   - Communication sécurisée via stdio

2. **HTTP API (Cloud)**
   - Endpoints pour monitoring et health checks
   - Outils disponibles via Cursor/Claude (pas via HTTP REST)
   - Useful for Fly.io integration

3. **Template Handling**
   - Le template `Sia_Template_Master.pptx` est automatiquement utilisé
   - Placé dans le dossier `/templates`
   - Accessible via les outils template

---

## 🆘 Troubleshooting

### "No tools available"
- Assurez-vous que vous utilisez Cursor/Claude (mode stdio)
- Ou utilisez l'endpoint `/mcp/server-info` pour vérifier l'état du serveur

### Health check fails
```bash
# Vérifier que le serveur écoute sur 0.0.0.0:8000
curl http://localhost:8000/health
```

### Template not found
- Vérifiez que `PPT_TEMPLATE_PATH` pointe vers le bon dossier
- Confirmez que `Sia_Template_Master.pptx` existe dans ce dossier

---

## 📞 API Documentation

### Auto-generated Swagger UI
```
http://localhost:8000/docs
```
or
```
https://powerpoint-mcp-server-delicate-surf-2694.fly.dev/docs
```

---

## 🔗 Quick Links

- **Fly.io App:** https://fly.io/apps/powerpoint-mcp-server-delicate-surf-2694
- **Cloud Server:** https://powerpoint-mcp-server-delicate-surf-2694.fly.dev/
- **GitHub (if applicable):** [Your GitHub URL]
- **Documentation:** This file
