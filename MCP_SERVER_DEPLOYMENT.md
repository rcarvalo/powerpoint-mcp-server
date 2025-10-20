# PowerPoint MCP Server - Deployment Guide

## 🚀 Deployment Status

### Cloud Deployment (Fly.io)
- **Status**: ✅ Live
- **URL**: https://powerpoint-mcp-server-delicate-surf-2694.fly.dev/
- **App Name**: powerpoint-mcp-server-delicate-surf-2694
- **Region**: CDG (Paris)
- **Configuration**: Auto-scaling (0-N machines), HTTPS enforced

### Local Deployment (Docker)
- **Status**: ✅ Running
- **Port**: 8000 (local)
- **Command**: `docker compose up -d`

---

## 📋 MCP Server Configuration

### For Cursor/Claude
Add this to your `~/.cursor/mcp.json`:

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

---

## 🛠️ Available Tools

### Presentation Management (7 tools)
- `create_presentation` - Create new presentation
- `open_presentation` - Open existing presentation
- `save_presentation` - Save presentation to file
- `get_presentation_info` - Get presentation metadata
- `list_presentations` - List all loaded presentations
- `switch_presentation` - Switch between presentations

### Content Management (6 tools)
- `manage_text` - Add and format text
- `populate_placeholder` - Fill placeholder text
- `add_bullet_points` - Add bulleted lists
- `manage_image` - Add and enhance images
- `add_table` - Create tables with formatting
- `add_chart` - Create charts with data

### Template Operations (7 tools)
- `create_presentation_from_template` - Create from template file
- `create_slide_from_template` - Create slide from template
- `apply_slide_template` - Apply template to existing slide
- `list_slide_templates` - List available templates
- `get_template_info` - Get template information
- `create_presentation_from_templates` - Create presentation from sequence
- `auto_generate_presentation` - Auto-generate presentation

### Structural Elements (4 tools)
- `add_slide` - Add new slide
- `add_shape` - Add shapes (rectangle, circle, etc.)
- `add_connector` - Add connector lines/arrows
- `manage_slide_masters` - Manage slide masters

### Professional Design (3 tools)
- `apply_professional_design` - Apply professional styling
- `apply_picture_effects` - Apply image effects
- `optimize_slide_text` - Optimize text layout

### Specialized Features (5 tools)
- `manage_hyperlinks` - Manage hyperlinks
- `update_chart_data` - Update chart data
- `manage_fonts` - Font management
- `manage_slide_transitions` - Slide transitions
- `set_core_properties` - Set document metadata

---

## 📝 Using the Template

The server uses the Sia_Template_Master.pptx template located at:
```
/Users/remicarvalot/project_pro/powerpoint-mcp-server/templates/Sia_Template_Master.pptx
```

### To use the template:
```python
# Create presentation from template
result = create_presentation_from_template(
    template_id="title_slide",
    color_scheme="modern_blue",
    content_mapping={
        "title": "My Presentation",
        "subtitle": "Subtitle here"
    }
)
```

---

## 🐳 Docker Management

### Start local server:
```bash
cd /Users/remicarvalot/project_pro/powerpoint-mcp-server
docker compose up -d
```

### View logs:
```bash
docker compose logs -f
```

### Stop server:
```bash
docker compose down
```

### Rebuild without cache:
```bash
docker compose build --no-cache
docker compose up -d
```

---

## 🚀 Fly.io Management

### Deploy updates:
```bash
fly deploy
```

### View deployment status:
```bash
fly status
```

### View logs:
```bash
fly logs
```

### Monitor app:
https://fly.io/apps/powerpoint-mcp-server-delicate-surf-2694/monitoring

---

## 🔧 Environment Variables

- `PPT_TEMPLATE_PATH`: Path to template directory
  - Local: `/Users/remicarvalot/project_pro/powerpoint-mcp-server/templates`
  - Docker: `/app/templates`

---

## 📦 Dependencies

- `chuk-mcp-server>=0.4.4` - MCP server framework
- `python-pptx>=0.6.21` - PowerPoint manipulation
- `Pillow>=8.0.0` - Image processing
- `fonttools>=4.0.0` - Font handling
- `mcp>=1.3.0` - MCP protocol

---

## 🔄 Architecture

```
┌─────────────────────────┐
│   Cursor / Claude       │
└────────────┬────────────┘
             │
             │ MCP Protocol (stdio)
             │
┌────────────▼────────────┐
│  PowerPoint MCP Server  │
│  - Content Tools        │
│  - Template Tools       │
│  - Professional Design  │
│  - Specialized Features │
└────────────┬────────────┘
             │
             ├─► python-pptx (PowerPoint generation)
             ├─► Pillow (Image processing)
             └─► fonttools (Font handling)
```

---

## ✅ Quick Start Checklist

- [x] Template configured (Sia_Template_Master.pptx)
- [x] MCP server registered in mcp.json
- [x] Local Docker running
- [x] Cloud deployment on Fly.io
- [x] All 32 tools available
- [x] Environment variables set correctly

---

## 📞 Support

For issues or questions, refer to:
- Local server logs: `docker compose logs -f`
- Fly.io monitoring: https://fly.io/apps/powerpoint-mcp-server-delicate-surf-2694/monitoring
- Server info: Call `get_server_info()` tool
