import os
import sys
import requests
import json
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("Stitch")

# The API Key is read from the environment variable STITCH_API_KEY
API_KEY = os.environ.get("STITCH_API_KEY")
ENDPOINT = "https://stitch.googleapis.com/mcp"

def call_stitch_mcp(method, params=None):
    """
    Simulates an MCP JSON-RPC call over HTTP POST. 
    This is 100% transparent and uses official Google endpoints.
    """
    if not API_KEY:
        return "Error: STITCH_API_KEY not set."
    
    headers = {
        "X-Goog-Api-Key": API_KEY,
        "Content-Type": "application/json"
    }
    
    # Standard MCP JSON-RPC structure
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params or {},
        "id": "1"
    }
    
    try:
        # We send the tools/call request directly to the Stitch MCP endpoint.
        response = requests.post(ENDPOINT, json=payload, headers=headers)
        response.raise_for_status()
        
        result = response.json()
        if "error" in result:
            return f"Stitch Error: {result['error'].get('message', 'Unknown error')}"
        
        # The result from Stitch is another JSON-RPC response or a direct object
        return result.get("result")
    except Exception as e:
        return f"Connection Error: {str(e)}"

@mcp.tool()
def list_projects(filter_str: str = None):
    """List all Stitch projects accessible to the user."""
    args = {"filter": filter_str} if filter_str else {}
    return call_stitch_mcp("tools/call", {"name": "list_projects", "arguments": args})

@mcp.tool()
def create_project(title: str = None):
    """Creates a new Stitch project."""
    args = {"title": title} if title else {}
    return call_stitch_mcp("tools/call", {"name": "create_project", "arguments": args})

@mcp.tool()
def generate_screen_from_text(parent: str, prompt: str, deviceType: str = "MOBILE", modelId: str = "GEMINI_1_5_FLASH"):
    """
    Generates a new screen within a project from a text prompt.
    deviceType: MOBILE, DESKTOP, TABLET, AGNOSTIC
    modelId: GEMINI_1_5_FLASH, GEMINI_1_5_PRO
    """
    args = {
        "parent": parent,
        "prompt": prompt,
        "deviceType": deviceType,
        "modelId": modelId
    }
    return call_stitch_mcp("tools/call", {"name": "generate_screen_from_text", "arguments": args})

@mcp.tool()
def get_project(name: str):
    """Retrieves a project by ID."""
    return call_stitch_mcp("tools/call", {"name": "get_project", "arguments": {"name": name}})

@mcp.tool()
def get_screen(projectId: str, screenId: str):
    """Retrieves the details of a specific screen within a project."""
    return call_stitch_mcp("tools/call", {"name": "get_screen", "arguments": {"projectId": projectId, "screenId": screenId}})

@mcp.tool()
def list_screens(projectId: str):
    """Lists all screens within a given Stitch project."""
    return call_stitch_mcp("tools/call", {"name": "list_screens", "arguments": {"projectId": projectId}})

if __name__ == "__main__":
    mcp.run()
