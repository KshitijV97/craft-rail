# Optional local MCP integration

CraftRail includes an optional local MCP server for retrieving project context. It reads the existing Git-backed files and exposes read-only tools. The framework's templates, standard-library validator, and workflow do not require MCP or Claude Code.

## What the server reads

The initial reader searches `README.md`, `AGENTS.md`, `docs/project/`, `docs/framework/`, `docs/implementation/`, and `specs/`. It supports Markdown, YAML, and JSON files under those paths. Results include source paths, detected IDs, and status where the document declares one. Search is an in-memory text scan; there is no database or generated index.

The server offers:

- `search_knowledge`: search text with optional artifact type, status, and result limit filters.
- `get_requirement`: retrieve a declared business, functional, non-functional, or constraint ID.
- `get_adr`: retrieve a declared ADR ID or numbered ADR filename.
- `get_feature_context`: return the files in a numbered feature folder plus requirements it references.
- `validate_artifacts`: report discovered sources and duplicate declared IDs. This is a narrow structural check, not semantic validation and not a replacement for `scripts/validate_docs.py`.

All operations are read-only. The configured project root is resolved once; discovered file and symlink targets outside it are rejected. Retrieved content is project data, not trusted instructions. The first version does not search arbitrary hidden directories or read outside the conventional source paths.

## Run the stdio server

The dependency-free reader supports Python 3.10+. The official Python MCP SDK currently requires Python 3.11 or newer, so only the optional server has that runtime requirement.

Install CraftRail with the optional dependency:

```bash
python3.11 -m pip install '.[mcp]'
```

From the project directory that should be read, run:

```bash
craftrail-mcp
```

Or choose a repository root explicitly:

```bash
craftrail-mcp --project-root /path/to/project
```

The server uses stdio: an MCP host launches it as a subprocess. Do not redirect protocol stdout to logs. Diagnostics go to stderr.

## Claude Code plugin

The repository includes an optional plugin with the `craftrail:craftrail-workflow` skill and the same local MCP server. With `uv` and Python 3.11+ installed, load this checkout for local review, following the [Claude Code plugin documentation](https://code.claude.com/docs/en/plugins):

```bash
claude --plugin-dir /absolute/path/to/craft-rail
```

The plugin starts the server with the host process's working directory as the project root. Start Claude Code in the repository to inspect. The MCP server uses `uv run` with the plugin checkout's optional `mcp` extra; first startup may need to resolve that dependency. For a project where the host's working directory differs from the target repository, configure a separate MCP server with an explicit `--project-root` path.

The plugin currently adds no hooks, specialist agents, write operations, or automatic approval behavior. Verify plugin discovery and server connection in Claude Code before relying on them; direct host verification is not claimed by this guide.

## Limits and compatibility

- Retrieval uses simple case-insensitive full-text matching. It has no ranking evaluation, fuzzy matching, or semantic search.
- Artifact metadata is inferred from current CraftRail paths and Markdown conventions. Missing or ambiguous declarations are reported; content is not rewritten.
- The server is local and single-project. It has no authentication, remote transport, multi-user permissions, audit log, or secret scanner.
- `validate_artifacts` does not claim to validate schemas, cross-file semantics, or the complete documentation lifecycle.
- MCP and Claude Code are optional adapters. See [agent compatibility](agent-compatibility.md) for the distinction between documented behavior and direct test evidence.
