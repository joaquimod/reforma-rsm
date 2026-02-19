
import json
import os

def format_stitch_output(stitch_result):
    """Auxiliary to format Stitch MCP output for better readability in Antigravity."""
    try:
        content = stitch_result.get("content", [])
        if not content:
            return "No content found in Stitch result."
        
        output = []
        for item in content:
            if item.get("type") == "text":
                # Try to pretty print if it's JSON string
                try:
                    js = json.loads(item.get("text"))
                    output.append(json.dumps(js, indent=2))
                except:
                    output.append(item.get("text"))
        return "\n---\n".join(output)
    except Exception as e:
        return f"Error formatting: {str(e)}"
