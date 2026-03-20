"""HTTP API client for anatomyfyi.com REST endpoints.

Requires the ``api`` extra: ``pip install anatomyfyi[api]``

Usage::

    from anatomyfyi.api import AnatomyFYI

    with AnatomyFYI() as api:
        items = api.list_entities()
        detail = api.get_entity("example-slug")
        results = api.search("query")
"""

from __future__ import annotations

from typing import Any

import httpx


class AnatomyFYI:
    """API client for the anatomyfyi.com REST API.

    Provides typed access to all anatomyfyi.com endpoints including
    list, detail, and search operations.

    Args:
        base_url: API base URL. Defaults to ``https://anatomyfyi.com``.
        timeout: Request timeout in seconds. Defaults to ``10.0``.
    """

    def __init__(
        self,
        base_url: str = "https://anatomyfyi.com",
        timeout: float = 10.0,
    ) -> None:
        self._client = httpx.Client(base_url=base_url, timeout=timeout)

    def _get(self, path: str, **params: Any) -> dict[str, Any]:
        resp = self._client.get(
            path,
            params={k: v for k, v in params.items() if v is not None},
        )
        resp.raise_for_status()
        result: dict[str, Any] = resp.json()
        return result

    # -- Endpoints -----------------------------------------------------------

    def list_comparisons(self, **params: Any) -> dict[str, Any]:
        """List all comparisons."""
        return self._get("/api/v1/comparisons/", **params)

    def get_comparison(self, slug: str) -> dict[str, Any]:
        """Get comparison by slug."""
        return self._get(f"/api/v1/comparisons/" + slug + "/")

    def list_entities(self, **params: Any) -> dict[str, Any]:
        """List all entities."""
        return self._get("/api/v1/entities/", **params)

    def get_entity(self, slug: str) -> dict[str, Any]:
        """Get entity by slug."""
        return self._get(f"/api/v1/entities/" + slug + "/")

    def list_faqs(self, **params: Any) -> dict[str, Any]:
        """List all faqs."""
        return self._get("/api/v1/faqs/", **params)

    def get_faq(self, slug: str) -> dict[str, Any]:
        """Get faq by slug."""
        return self._get(f"/api/v1/faqs/" + slug + "/")

    def list_glossary(self, **params: Any) -> dict[str, Any]:
        """List all glossary."""
        return self._get("/api/v1/glossary/", **params)

    def get_term(self, slug: str) -> dict[str, Any]:
        """Get term by slug."""
        return self._get(f"/api/v1/glossary/" + slug + "/")

    def list_glossary_categories(self, **params: Any) -> dict[str, Any]:
        """List all glossary categories."""
        return self._get("/api/v1/glossary-categories/", **params)

    def get_glossary_category(self, slug: str) -> dict[str, Any]:
        """Get glossary category by slug."""
        return self._get(f"/api/v1/glossary-categories/" + slug + "/")

    def list_guide_series(self, **params: Any) -> dict[str, Any]:
        """List all guide series."""
        return self._get("/api/v1/guide-series/", **params)

    def get_guide_sery(self, slug: str) -> dict[str, Any]:
        """Get guide sery by slug."""
        return self._get(f"/api/v1/guide-series/" + slug + "/")

    def list_guides(self, **params: Any) -> dict[str, Any]:
        """List all guides."""
        return self._get("/api/v1/guides/", **params)

    def get_guide(self, slug: str) -> dict[str, Any]:
        """Get guide by slug."""
        return self._get(f"/api/v1/guides/" + slug + "/")

    def list_regions(self, **params: Any) -> dict[str, Any]:
        """List all regions."""
        return self._get("/api/v1/regions/", **params)

    def get_region(self, slug: str) -> dict[str, Any]:
        """Get region by slug."""
        return self._get(f"/api/v1/regions/" + slug + "/")

    def list_relations(self, **params: Any) -> dict[str, Any]:
        """List all relations."""
        return self._get("/api/v1/relations/", **params)

    def get_relation(self, slug: str) -> dict[str, Any]:
        """Get relation by slug."""
        return self._get(f"/api/v1/relations/" + slug + "/")

    def list_systems(self, **params: Any) -> dict[str, Any]:
        """List all systems."""
        return self._get("/api/v1/systems/", **params)

    def get_system(self, slug: str) -> dict[str, Any]:
        """Get system by slug."""
        return self._get(f"/api/v1/systems/" + slug + "/")

    def search(self, query: str, **params: Any) -> dict[str, Any]:
        """Search across all content."""
        return self._get(f"/api/v1/search/", q=query, **params)

    # -- Lifecycle -----------------------------------------------------------

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> AnatomyFYI:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
