from fastmcp import FastMCP
from dotenv import load_dotenv
from starlette.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware

# Load Environment variables
load_dotenv()

# Create new MCP App
mcp = FastMCP(name="Invoice MCP Server")

@mcp.tool
def greet(name: str) -> str:
    """Greet a person by name."""
    return f"Hello, {name}!"

@mcp.tool
def get_my_notes() -> str:
    """Get all notes for a user"""
    return "No notes"

@mcp.tool
def add_note(content:str) -> str:
    """Add a note for a user"""
    return f"added note: {content}"

@mcp.custom_route("/health", methods=["GET"])
async def health_check(_request):
    """
    Health check endpoint for service availability.

    This endpoint is used by Azure Container Apps to verify that the service is running and healthy.
    It returns a simple JSON response indicating the status of the service:

    {
        "status": "healthy",
        "service": "invoice-mcp-server"
    }
    """
    return JSONResponse({"status": "healthy", "service": "invoice-mcp-server"}) 


if __name__ == "__main__":
    mcp.run(
        transport="http", 
        host="127.0.0.1", 
        port=8000,
        middleware=[
            Middleware(
                CORSMiddleware,
                allow_origins=["*"],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )
        ]
    )