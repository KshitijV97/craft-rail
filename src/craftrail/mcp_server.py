"""Optional stdio MCP adapter for CraftRail knowledge retrieval."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

from craftrail.knowledge import ProjectKnowledge


def build_server(project_root: Path) -> Any:
    """Create a server whose complete read scope is the configured project root."""
    try:
        from mcp.server import MCPServer
    except ImportError as exc:  # pragma: no cover - depends on the optional MCP extra
        raise RuntimeError(
            "The optional MCP dependency is missing. Install CraftRail with its 'mcp' extra "
            "under Python 3.11 or newer."
        ) from exc

    knowledge = ProjectKnowledge(project_root)
    server = MCPServer("CraftRail Knowledge")

    @server.tool()
    def search_knowledge(
        query: str,
        artifact_type: str | None = None,
        status: str | None = None,
        limit: int = 10,
    ) -> list[dict[str, Any]]:
        """Search canonical CraftRail documents and return source-backed excerpts."""
        return knowledge.search(query, artifact_type=artifact_type, status=status, limit=limit)

    @server.tool()
    def get_requirement(identifier: str) -> dict[str, object]:
        """Retrieve a declared BR, FR, NFR, or CON requirement."""
        return knowledge.get_requirement(identifier)

    @server.tool()
    def get_adr(identifier: str) -> dict[str, object]:
        """Retrieve a declared architecture decision record."""
        return knowledge.get_adr(identifier)

    @server.tool()
    def get_feature_context(feature_id: str) -> dict[str, object]:
        """Assemble the files and declared requirements for a numbered feature."""
        return knowledge.get_feature_context(feature_id)

    @server.tool()
    def validate_artifacts() -> dict[str, object]:
        """Check source discovery and duplicate declared IDs; this is not semantic validation."""
        return knowledge.validate_artifacts()

    return server


def main(argv: list[str] | None = None) -> int:
    if sys.version_info < (3, 11):
        print("craftrail-mcp requires Python 3.11 or newer", file=sys.stderr)
        return 2
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--project-root",
        type=Path,
        default=Path.cwd(),
        help="repository to read (defaults to the process working directory)",
    )
    args = parser.parse_args(argv)
    try:
        server = build_server(args.project_root)
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"craftrail-mcp: {exc}", file=sys.stderr)
        return 2
    server.run()
    return 0


if __name__ == "__main__":  # pragma: no cover - exercised by an MCP host
    raise SystemExit(main())
