from fastmcp import FastMCP
from starlette.responses import JSONResponse

mcp = FastMCP(name="Invoice MCP Server")

@mcp.tool
def greet(name: str) -> str:
    """Greet a person by name."""
    return f"Hello, {name}!"

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
    mcp.run(transport="http", host="127.0.0.1", port=8000)