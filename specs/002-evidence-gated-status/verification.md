# Verification: 002 Evidence-gated status

Statuses: `planned`, `implemented`, `verified`, `blocked`, `waived`, `deprecated`.

Once `craftrail status` exists, this feature's status is computed by it (CON-001) and this table becomes a planning view. Until then every row is `planned`.

| Requirement | Acceptance criterion | Verification ID / method | Evidence or location | Status |
|---|---|---|---|---|
| FR-001, FR-002, FR-004 | AC-001 | unit | — | planned |
| FR-004, BR-002 | AC-002 | unit | — | planned |
| FR-003, BR-002 | AC-003 | integration (real git repository) | — | planned |
| FR-004, BR-003, BR-004 | AC-004 | unit | — | planned |
| FR-002, BR-005 | AC-005 | unit | — | planned |
| FR-002, FR-004 | AC-006 | unit | — | planned |
| FR-005, FR-007 | AC-007 | integration (real git repository) | — | planned |
| FR-006, FR-007, CON-001 | AC-008 | acceptance (CraftRail CI) | — | planned |
| FR-006, NFR-002 | AC-009 | unit | — | planned |
| FR-001, FR-007, NFR-003 | AC-010 | integration | — | planned |
| NFR-001, CON-002 | AC-011 | unit | — | planned |
| FR-008 | — | not yet defined | — | planned |

Waivers require an accountable owner, rationale, and accepted risk. Code generation alone is not evidence.
