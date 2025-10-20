#!/usr/bin/env python
"""
HTTP Server wrapper for PowerPoint MCP Server
Provides HTTP REST API for PowerPoint manipulation with full MCP tools exposure
"""
import os
import sys
import json
import logging
from typing import Dict, Any, List, Optional
from fastapi import FastAPI, HTTPException, Body
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn
import inspect

# Add the project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import the MCP app and global state
from server import app as mcp_app, presentations, get_current_presentation_id, set_current_presentation_id

# Create FastAPI app for HTTP wrapper
http_app = FastAPI(
    title="PowerPoint MCP Server",
    description="HTTP API for PowerPoint manipulation using MCP protocol",
    version="2.2.0"
)

# Override FastAPI's openapi() method to serve our custom spec
def custom_openapi():
    optimized_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "openapi_optimized.json")
    try:
        with open(optimized_path, 'r', encoding='utf-8') as f:
            logger.info("Loading custom optimized OpenAPI spec for OpenAI Agent Builder")
            return json.load(f)
    except Exception as e:
        logger.error(f"Error loading custom OpenAPI: {e}")
        # Fallback to FastAPI's default
        from fastapi.openapi.utils import get_openapi
        return get_openapi(
            title=http_app.title,
            version=http_app.version,
            description=http_app.description,
            routes=http_app.routes,
        )

http_app.openapi = custom_openapi

# Pydantic models
class ToolCall(BaseModel):
    tool_name: str
    arguments: Dict[str, Any] = {}

class ToolResponse(BaseModel):
    status: str
    result: Any = None
    error: Optional[str] = None

# ============= HEALTH & INFO ENDPOINTS =============

@http_app.get("/health")
async def health_check() -> Dict[str, Any]:
    """Health check endpoint for Fly.io monitoring"""
    return {
        "status": "healthy",
        "service": "ppt-mcp-server",
        "version": "2.2.0",
        "total_presentations": len(presentations),
        "current_presentation": get_current_presentation_id()
    }

@http_app.get("/")
async def root() -> Dict[str, Any]:
    """Root endpoint with server information"""
    return {
        "name": "PowerPoint MCP Server",
        "version": "2.2.0",
        "status": "running",
        "description": "HTTP API for PowerPoint manipulation",
        "endpoints": {
            "health": "/health",
            "info": "/",
            "mcp_api": "/mcp",
            "tools": "/mcp/tools",
            "call_tool": "/mcp/call",
            "presentations": "/mcp/presentations"
        }
    }

# ============= MCP API ROOT ENDPOINT =============

@http_app.get("/mcp")
async def mcp_root() -> Dict[str, Any]:
    """MCP API root endpoint - shows available MCP endpoints"""
    return {
        "status": "success",
        "service": "PowerPoint MCP Server",
        "version": "2.2.0",
        "description": "Model Context Protocol - HTTP API for PowerPoint manipulation",
        "mcp_endpoints": {
            "tools": {
                "path": "/mcp/tools",
                "method": "GET",
                "description": "List all 32 available PowerPoint tools"
            },
            "call": {
                "path": "/mcp/call",
                "method": "POST",
                "description": "Call a specific tool with arguments",
                "example": {
                    "tool_name": "create_presentation",
                    "arguments": {}
                }
            },
            "presentations": {
                "path": "/mcp/presentations",
                "method": "GET",
                "description": "List all open presentations"
            },
            "select_presentation": {
                "path": "/mcp/presentations/select/{id}",
                "method": "POST",
                "description": "Select a presentation to work with"
            },
            "presentation_info": {
                "path": "/mcp/presentations/{id}/info",
                "method": "GET",
                "description": "Get information about a specific presentation"
            },
            "server_info": {
                "path": "/mcp/server-info",
                "method": "GET",
                "description": "Get detailed server information"
            }
        },
        "quick_start": {
            "1_list_tools": "curl https://powerpoint-mcp-server-delicate-surf-2694.fly.dev/mcp/tools",
            "2_create_presentation": "curl -X POST https://powerpoint-mcp-server-delicate-surf-2694.fly.dev/mcp/call -H 'Content-Type: application/json' -d '{\"tool_name\": \"create_presentation\", \"arguments\": {}}'",
            "3_add_slide": "curl -X POST https://powerpoint-mcp-server-delicate-surf-2694.fly.dev/mcp/call -H 'Content-Type: application/json' -d '{\"tool_name\": \"add_slide\", \"arguments\": {\"presentation_id\": \"pres_1\", \"layout_index\": 0, \"title\": \"My Slide\"}}'"
        }
    }

# ============= MCP TOOLS ENDPOINTS =============

@http_app.get("/mcp/tools")
async def list_tools() -> Dict[str, Any]:
    """List all available MCP tools"""
    try:
        # FastMCP's list_tools() is async, so we need to await it
        tools_result = mcp_app.list_tools()
        
        # If it's a coroutine, await it
        import inspect
        if inspect.iscoroutine(tools_result):
            tools_list = await tools_result
        else:
            tools_list = tools_result
        
        tools_info = []
        if tools_list:
            for tool in tools_list:
                # Tool might be an object or dict, handle both
                if hasattr(tool, '__dict__'):
                    tool_dict = tool.__dict__ if hasattr(tool, '__dict__') else {}
                    tool_info = {
                        "name": getattr(tool, 'name', tool_dict.get('name', 'Unknown')),
                        "description": getattr(tool, 'description', tool_dict.get('description', 'No description')),
                        "inputSchema": getattr(tool, 'inputSchema', tool_dict.get('inputSchema', {}))
                    }
                else:
                    tool_info = {
                        "name": tool.get("name", "Unknown"),
                        "description": tool.get("description", "No description"),
                        "inputSchema": tool.get("inputSchema", {})
                    }
                tools_info.append(tool_info)
        
        return {
            "status": "success",
            "total_tools": len(tools_info),
            "tools": tools_info,
            "usage": "POST /mcp/call with { 'tool_name': 'name', 'arguments': {...} }"
        }
    except Exception as e:
        logger.error(f"Error listing tools: {e}", exc_info=True)
        return {
            "status": "error",
            "error": str(e),
            "debug_info": f"Error type: {type(e).__name__}"
        }

@http_app.post("/mcp/call", response_model=ToolResponse)
async def call_tool(call: ToolCall) -> ToolResponse:
    """Call a specific MCP tool"""
    try:
        logger.info(f"Calling tool: {call.tool_name} with args: {call.arguments}")
        
        # FastMCP's call_tool() might be async, so we need to handle it
        import inspect
        call_result = mcp_app.call_tool(call.tool_name, call.arguments)
        
        if inspect.iscoroutine(call_result):
            result = await call_result
        else:
            result = call_result
        
        return ToolResponse(
            status="success",
            result=result
        )
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Tool '{call.tool_name}' not found")
    except Exception as e:
        logger.error(f"Error calling tool {call.tool_name}: {e}", exc_info=True)
        return ToolResponse(
            status="error",
            error=str(e)
        )

# ============= PRESENTATION MANAGEMENT ENDPOINTS =============

@http_app.get("/mcp/presentations")
async def list_presentations() -> Dict[str, Any]:
    """List all open presentations"""
    return {
        "status": "success",
        "total_presentations": len(presentations),
        "presentation_ids": list(presentations.keys()),
        "current_presentation_id": get_current_presentation_id()
    }

@http_app.post("/mcp/presentations/select/{presentation_id}")
async def select_presentation(presentation_id: str) -> Dict[str, Any]:
    """Select the current presentation"""
    if presentation_id not in presentations:
        raise HTTPException(status_code=404, detail=f"Presentation '{presentation_id}' not found")
    
    old_id = get_current_presentation_id()
    set_current_presentation_id(presentation_id)
    
    return {
        "status": "success",
        "message": f"Switched to presentation '{presentation_id}'",
        "previous_id": old_id,
        "current_id": presentation_id
    }

@http_app.get("/mcp/presentations/{presentation_id}/info")
async def get_presentation_info(presentation_id: str) -> Dict[str, Any]:
    """Get information about a specific presentation"""
    if presentation_id not in presentations:
        raise HTTPException(status_code=404, detail=f"Presentation '{presentation_id}' not found")
    
    pres = presentations[presentation_id]
    return {
        "status": "success",
        "presentation_id": presentation_id,
        "slides_count": len(pres.slides),
        "is_current": presentation_id == get_current_presentation_id()
    }

# ============= UTILITY ENDPOINTS =============

@http_app.get("/mcp/server-info")
async def get_server_info() -> Dict[str, Any]:
    """Get detailed server information"""
    return {
        "name": "PowerPoint MCP Server - ChukMCP Edition",
        "version": "2.2.0",
        "total_tools": 32,
        "loaded_presentations": len(presentations),
        "current_presentation": get_current_presentation_id(),
        "features": [
            "Presentation Management (7 tools)",
            "Content Management (6 tools)",
            "Template Operations (7 tools)",
            "Structural Elements (4 tools)",
            "Professional Design (3 tools)",
            "Specialized Features (5 tools)"
        ],
        "endpoints": {
            "health": "/health - Health check",
            "info": "/ - Server info",
            "tools": "/mcp/tools - List all tools",
            "call": "/mcp/call - Call a tool (POST)",
            "presentations": "/mcp/presentations - List presentations",
            "select": "/mcp/presentations/select/{id} - Select presentation",
            "presentation_info": "/mcp/presentations/{id}/info - Get presentation info",
            "server_info": "/mcp/server-info - Full server info",
            "openapi": "/openapi.json - OpenAPI spec for OpenAI"
        }
    }

@http_app.get("/openapi.json")
async def get_openapi_spec() -> Dict[str, Any]:
    """Get OpenAPI specification for OpenAI Agent Builder"""
    # Try optimized version first, fallback to basic version
    optimized_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "openapi_optimized.json")
    basic_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "openapi.json")

    try:
        with open(optimized_path, 'r', encoding='utf-8') as f:
            logger.info("Serving optimized OpenAPI spec for OpenAI Agent Builder")
            return json.load(f)
    except FileNotFoundError:
        try:
            with open(basic_path, 'r', encoding='utf-8') as f:
                logger.info("Serving basic OpenAPI spec")
                return json.load(f)
        except FileNotFoundError:
            raise HTTPException(status_code=404, detail="OpenAPI spec not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Invalid OpenAPI spec")

def main():
    """Start the HTTP server"""
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    
    logger.info(f"Starting PowerPoint MCP Server on {host}:{port}")
    logger.info("Available endpoints:")
    logger.info("  GET  / - Server info")
    logger.info("  GET  /health - Health check")
    logger.info("  GET  /mcp - MCP API root")
    logger.info("  GET  /mcp/tools - List all 32 tools")
    logger.info("  POST /mcp/call - Call a tool")
    logger.info("  GET  /mcp/presentations - List presentations")
    logger.info("  GET  /mcp/server-info - Full server info")
    
    uvicorn.run(
        http_app,
        host=host,
        port=port,
        log_level="info"
    )

if __name__ == "__main__":
    main()
