"""MCP server for anatomyfyi."""

from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from anatomyfyi.api import AnatomyFYI

mcp = FastMCP("anatomyfyi")


@mcp.tool()
def search_anatomyfyi(query: str) -> dict[str, Any]:
    """Search anatomyfyi.com for content matching the query."""
    with AnatomyFYI() as api:
        return api.search(query)
