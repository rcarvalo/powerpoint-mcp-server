# Changelog - PowerPoint MCP Server

## [2.3.0] - 2024-10-19

### 🔧 Fixed
- **CRITICAL FIX**: Replaced ChukMCP with pure FastMCP to resolve "Invalid tool schema" errors
- Fixed `add_bullet_points` and all other tools that were failing with schema validation
- Removed incompatible ChukMCP/FastMCP hybrid architecture

### ✨ Changed
- Migrated from ChukMCPServer to pure FastMCP implementation
- Simplified server architecture - now uses FastMCP directly
- Updated all `@tool` decorators to `@app.tool()` for FastMCP compatibility
- Streamlined command-line arguments (removed unused HTTP options)

### 📝 Technical Details
**Problem**: ChukMCP and FastMCP use different tool registration systems. The previous version tried to bridge them with a `MockServer` class, which caused JSON Schema generation failures.

**Solution**: Removed all ChukMCP dependencies and use FastMCP natively. All 32 tools now register directly with FastMCP's `@app.tool()` decorator.

**Impact**: All tools now have valid JSON schemas that Claude can understand and use.

### 🧪 Tested
- ✅ Server startup
- ✅ Tool registration (32 tools)
- ✅ Presentation creation
- ✅ Slide addition
- ✅ File generation (test_fastmcp_output.pptx)
- ✅ All imports working

---

## [2.2.0] - 2024-10-19

### ✨ Added
- Initial ChukMCP Edition release
- 32 PowerPoint tools across 11 modules
- Comprehensive documentation
- Docker support

### ⚠️ Known Issues
- Tool schema validation errors with ChukMCP (fixed in 2.3.0)

---

## Version History

- **2.3.0** (Current) - FastMCP Edition - Fixed all tool schema issues
- **2.2.0** - ChukMCP Edition - Had schema validation issues
- **2.1.0** - Office-PowerPoint-MCP-Server original
- **1.0.0** - Initial release
