"""Command-line interface for anatomyfyi."""

from __future__ import annotations

import json

import typer

from anatomyfyi.api import AnatomyFYI

app = typer.Typer(help="AnatomyFYI — Human anatomy and body systems API client.")


@app.command()
def search(query: str) -> None:
    """Search anatomyfyi.com."""
    with AnatomyFYI() as api:
        result = api.search(query)
        typer.echo(json.dumps(result, indent=2))
