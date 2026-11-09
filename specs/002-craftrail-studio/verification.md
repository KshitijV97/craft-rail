# Verification: 002 CraftRail Studio

Statuses: `planned`, `implemented`, `verified`, `blocked`, `waived`, `deprecated`.

Record command, environment (OS, Node/Python versions, browser), commit SHA, result and date when a check runs.

| Requirement | Acceptance criterion | Verification ID / method | Evidence or location | Status |
|---|---|---|---|---|
| FR-018 | AC-001 | TEST-001 e2e: `pnpm -C studio test:e2e -- overview` | not yet run | planned |
| FR-019 | AC-002 | TEST-002 e2e: gap fixtures in graph and matrix; clustering on perf fixture | not yet run | planned |
| FR-020 | AC-003 | TEST-003 e2e: filters, swimlanes, column remap | not yet run | planned |
| FR-024 | AC-003 | TEST-003 e2e: URL reload reproduces view; search | not yet run | planned |
| FR-021 | AC-004 | TEST-004 e2e: links, source, timeline | not yet run | planned |
| FR-022 | AC-005 | TEST-005 e2e: values vs `expected-metrics.json`; definitions; data tables; partial notice | not yet run | planned |
| BR-006 | AC-005 | TEST-005 e2e: "linked coverage" label on every coverage figure | not yet run | planned |
| FR-023 | AC-006 | TEST-006 e2e: supersession chain | not yet run | planned |
| FR-025 | AC-007 | TEST-007 automated: Vitest patch engine + cross-language contract suite | not yet run | planned |
| FR-026 | AC-008 | TEST-008 integration: `python -m unittest tests.test_server -v` (loopback, token, Origin, traversal, symlink, size) | not yet run | planned |
| BR-005 | AC-008 | TEST-008 integration: writes outside globs rejected | not yet run | planned |
| FR-027 | AC-009 | TEST-009 automated: Vitest + MSW; token storage assertions | not yet run | planned |
| FR-028 | AC-009 | TEST-009 automated: queue saves as one commit | not yet run | planned |
| FR-029 | AC-010 | TEST-010 e2e: local and GitHub conflict flows | not yet run | planned |
| FR-030 | AC-011 | TEST-011 automated: invalid edits blocked | not yet run | planned |
| BR-004 | AC-012 | TEST-012 e2e: typed confirmation, recorded approver, PR-only, no bulk approve | not yet run | planned |
| FR-031 | AC-013 | TEST-013 e2e + Vitest: clipboard equals `context_pack.py` output | not yet run | planned |
| NFR-006 | AC-013 | TEST-013 e2e: network blocked; only app-origin requests | not yet run | planned |
| FR-032 | AC-014 | TEST-014 manual + automated: `studio.yml` in scratch repo; sub-path load with zero 404s | not yet run | planned |
| CON-004 | AC-014 | TEST-014 review: artifact contains only static files | not yet run | planned |
| NFR-007 | AC-014 | TEST-014 review: CSP meta in built `index.html` | not yet run | planned |
| FR-033 | AC-015 | TEST-015 e2e: source badge; editing disabled | not yet run | planned |
| NFR-004 | AC-016 | TEST-016 CI bundle ≤ 350 KB gzip; manual 1,000-node fps recording | not yet run | planned |
| NFR-005 | AC-016 | TEST-016 CI axe (zero serious/critical) + keyboard-only journey | not yet run | planned |
| NFR-008 | AC-016 | TEST-016 CI coverage thresholds | not yet run | planned |
| NFR-009 | AC-016 | TEST-016 Playwright on Chromium, Firefox, WebKit; manual Edge smoke test | not yet run | planned |

Waivers require an accountable owner, rationale, and accepted risk. Code generation alone is not evidence.
