# Verification: 001 Local read-only knowledge retrieval

Statuses: `planned`, `implemented`, `verified`, `blocked`, `waived`, `deprecated`.

| Requirement | Acceptance criterion | Verification ID / method | Evidence or location | Status |
|---|---|---|---|---|
| FR-001, FR-003 | AC-001 | TEST-001: retrieve existing requirement and feature records; inspect source/status metadata | Planned | planned |
| FR-002 | AC-002, AC-005 | TEST-002: call operations with unknown/malformed IDs; TEST-005: initialize plugin and inspect tools | MCP client and Claude Code host | planned |
| FR-001 | AC-003 | TEST-003: request traversal and symlink escape cases; confirm no outside read | Planned | planned |
| NFR-001, CON-001 | AC-004 | TEST-004: import/run core without MCP dependencies and confirm no writes | Planned | planned |
