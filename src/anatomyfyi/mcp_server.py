"""MCP server for anatomyfyi — AI assistant tools for anatomyfyi.com.

Run: uvx --from "anatomyfyi[mcp]" python -m anatomyfyi.mcp_server
"""
from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("AnatomyFYI")


@mcp.tool()
def list_entities(limit: int = 20, offset: int = 0) -> str:
    """List entities from anatomyfyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from anatomyfyi.api import AnatomyFYI

    with AnatomyFYI() as api:
        data = api.list_entities(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No entities found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def get_entity(slug: str) -> str:
    """Get detailed information about a specific entity.

    Args:
        slug: URL slug identifier for the entity.
    """
    from anatomyfyi.api import AnatomyFYI

    with AnatomyFYI() as api:
        data = api.get_entity(slug)
        return str(data)


@mcp.tool()
def list_regions(limit: int = 20, offset: int = 0) -> str:
    """List regions from anatomyfyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from anatomyfyi.api import AnatomyFYI

    with AnatomyFYI() as api:
        data = api.list_regions(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No regions found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def search_anatomy(query: str) -> str:
    """Search anatomyfyi.com for anatomical structures, body systems, and organs.

    Args:
        query: Search query string.
    """
    from anatomyfyi.api import AnatomyFYI

    with AnatomyFYI() as api:
        data = api.search(query)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return f"No results found for \"{query}\"."
        items = results[:10] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


def main() -> None:
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
