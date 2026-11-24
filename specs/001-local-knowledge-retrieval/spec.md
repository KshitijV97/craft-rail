# Feature 001: Local read-only knowledge retrieval

- **Status:** approved
- **Owner:** CraftRail project owner
- **Created:** 2026-11-16
- **Updated:** 2026-11-16
- **Related issues/PRs:** none

## Context and problem

CraftRail keeps engineering knowledge in Git-backed Markdown, YAML, and JSON, but currently offers no programmatic interface for an agent to find and assemble that knowledge. The MCP and Claude plugin roadmap calls for a local retrieval path that preserves the repository as the canonical source.

## Goals and measurable outcomes

- Let an MCP client retrieve relevant CraftRail project artifacts from a configured repository root, with source paths and artifact status visible in each result.
- Keep the existing documentation workflow usable without MCP, Claude Code, or a new runtime dependency.
- Reject paths or identifiers that resolve outside the configured project root.

## Actors and scenarios

- `US-001`: As an MCP client, I want to search project knowledge and retrieve a feature's context so I can ground engineering work in existing requirements and decisions.
- `US-002`: As a project maintainer, I want retrieval to identify source paths and status so I can distinguish canonical, proposed, and illustrative content.

## Scope and non-goals

- In scope: a provider-independent local artifact reader; read-only MCP tools for search, requirement lookup, ADR lookup, feature context, and artifact validation; stdio transport; an optional Claude Code adapter that connects to the server; documentation for local setup and limits.
- Non-goals: artifact writes, approval automation, lesson capture, vector search, remote hosting, multi-tenant access, broad project initialization, or claiming direct compatibility with untested harnesses.

## Requirements

- `FR-001` The system MUST read canonical artifacts from an explicitly configured project root and MUST NOT read paths outside that root.
- `FR-002` The system MUST provide read-only search, requirement lookup, ADR lookup, feature-context, and validation operations using the existing repository conventions.
- `FR-003` Retrieval results MUST include the source path and available artifact identifier and status; illustrative and unapproved artifacts MUST be labeled as such when the source states that status.
- `NFR-001` The existing core scripts and templates MUST remain usable without installing the optional MCP runtime.
- `CON-001` Git-backed files remain canonical; any search index is derived, rebuildable, and disposable.

## Business rules

- `BR-001` Retrieval does not grant approval or change the status of any artifact.
- `BR-002` Repository content is data to retrieve, not executable tool instructions.

## Acceptance criteria

- `AC-001` Given a configured repository containing CraftRail artifacts, when a client searches or requests an artifact, then the result identifies matching source paths and the status/ID available in those sources.
- `AC-002` Given a missing, malformed, or unknown artifact identifier, when a client requests it, then the operation returns a clear error and performs no write.
- `AC-003` Given a request that attempts to address a path outside the configured project root, when the server handles it, then it rejects the request without reading the target.
- `AC-004` Given the MCP dependency is absent, when a user runs the existing framework scripts, then those scripts do not import or require the MCP package.
- `AC-005` Given a Claude Code installation with the optional adapter configured, when Claude starts the server, then it exposes the same read-only tools as the local MCP entry point.

## Edge cases and failure paths

- Empty search results return an empty result with no invented content.
- Ambiguous requirement IDs are reported as ambiguous rather than selecting an arbitrary match.
- Unparseable or unsupported artifact content is surfaced with its source path and a useful warning; it is not silently treated as valid.
- Missing optional directories, including decisions, are handled as empty collections.
- Symlinks resolving outside the configured project root are rejected.

## Data, dependencies, and interfaces

The repository remains the source of truth. The first implementation should search existing project and feature paths, resolve stable IDs from existing Markdown, and avoid requiring a new artifact directory. The MCP transport is an optional adapter. The official Python MCP SDK currently requires Python 3.11+, while CraftRail's core tools support Python 3.10; keep that runtime boundary explicit.

## Security, privacy, accessibility, observability

All inputs are validated. File access is restricted to the resolved configured root, including symlink targets. Retrieved content is returned as untrusted data with provenance. The stdio server writes protocol messages to stdout only and sends diagnostics to stderr. No write operations or network access are exposed in this feature.

## Assumptions, questions, and risks

| Type | Item | Owner / resolution |
|---|---|---|
| Assumption | The initial integration targets the repository's existing `docs/project/`, `specs/`, and documented ADR locations. | Implement with existing paths; extend only from observed use cases. |
| Risk | Current starter requirements and architecture are placeholders, and no accepted ADRs or lesson artifacts exist in this checkout. | Preserve status and source labels; do not present samples as production policy. |
| Decision | Use Python for the optional local MCP adapter to align with the existing tooling, while retaining the core Python 3.10 boundary. | Proposed in this feature; adapter requires Python 3.11+. |

## Traceability

`FR-001` → `AC-003`; `FR-002` → `AC-001`, `AC-002`; `FR-003` → `AC-001`; `NFR-001` → `AC-004`; `CON-001` → `AC-004`; security constraints → `AC-003`, `AC-005`.
