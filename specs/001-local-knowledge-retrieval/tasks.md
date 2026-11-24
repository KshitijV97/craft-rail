# Tasks: 001 Local read-only knowledge retrieval

| ID | Task / expected output | Requirement / AC | Depends on | Verification | Status |
|---|---|---|---|---|---|
| TASK-001 | Implement provider-independent artifact discovery, metadata extraction, search, requirement/ADR lookup, and feature-context assembly. | FR-001, FR-002, FR-003; AC-001–AC-004 | — | Core reader checks for IDs, status, ambiguity, empty results, and optional dependency isolation | implemented |
| TASK-002 | Add the optional stdio MCP server exposing the read-only Core operations. | FR-001–FR-003; AC-001–AC-004 | TASK-001 | MCP SDK client calls and path-boundary cases | implemented |
| TASK-003 | Add a minimal Claude Code plugin adapter and local setup guide. | NFR-001; AC-004, AC-005 | TASK-002 | Validate plugin structure and test host discovery when available | implemented; host verification pending |
| TASK-004 | Update CraftRail implementation/adoption documentation and website navigation to describe installation, scope, compatibility evidence, and limitations. | FR-003, NFR-001; AC-001, AC-004 | TASK-001–003 | Strict docs/site build when available; review links and claims | implemented; site build pending |
