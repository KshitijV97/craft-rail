# Tasks: 002 CraftRail Studio

Dependency-ordered slices; each task is one reviewable pull request. Start only after feature 001 is `verified` and this spec is `approved`.

| ID | Task / expected output | Requirement / AC | Depends on | Verification | Status |
|---|---|---|---|---|---|
| TASK-001 | Scaffold `studio/` (Vite, React, TS strict, Biome, Vitest, Playwright, pnpm lock); generated types with staleness check; `studio` CI job | CON-005, NFR-008 | — | TEST-016 | planned |
| TASK-002 | `studio_server.py` read endpoints (`/`, `/api/health`, `/api/graph`, `GET /api/file`) with token and Host/Origin checks | FR-026, AC-008 | — | TEST-008 | planned |
| TASK-003 | App shell: graph loading (static file or API), freshness banner, diagnostics panel, hash routing, URL state, search | FR-024, AC-003 | TASK-001, TASK-002 | TEST-003 | planned |
| TASK-004 | Overview view | FR-018, AC-001 | TASK-003 | TEST-001 | planned |
| TASK-005 | Boards: column mapping, filters, swimlanes, keyboard "Move to…" (read-only until TASK-012) | FR-020, AC-003 | TASK-003 | TEST-003 | planned |
| TASK-006 | Traceability graph (React Flow + dagre, clustering) and matrix with gap highlighting | FR-019, AC-002 | TASK-003 | TEST-002 | planned |
| TASK-007 | Item detail: metadata, sanitised excerpt, links, source link, timeline; source badge and read-only for non-craftrail items | FR-021, FR-033, AC-004, AC-015 | TASK-003 | TEST-004, TEST-015 | planned |
| TASK-008 | Metrics view (uPlot) with definitions, partial notices, data tables, linked-coverage labels | FR-022, BR-006, AC-005 | TASK-003 | TEST-005 | planned |
| TASK-009 | Decisions view with supersession chains | FR-023, AC-006 | TASK-003 | TEST-006 | planned |
| TASK-010 | TS patch engine for all operations; 100% branch coverage; cross-language contract tests | FR-025, AC-007 | TASK-001 | TEST-007 | planned |
| TASK-011 | Client validation (Ajv + graph rules) and change queue with diff preview | FR-028, FR-030, AC-011 | TASK-010 | TEST-011 | planned |
| TASK-012 | Server `PUT /api/file` (atomic, newline-preserving, globs, symlinks, size); local backend; conflict view; enable editing in views | FR-025, FR-026, FR-029, BR-005, AC-007, AC-008, AC-010 | TASK-011, TASK-002 | TEST-007, TEST-008, TEST-010 | planned |
| TASK-013 | Approval guard (typed confirmation, recorded approver, no bulk approve, PR-only on GitHub) | BR-004, AC-012 | TASK-012 | TEST-012 | planned |
| TASK-014 | GitHub backend (PAT entry, single-commit Git Data API flow, branch naming, PR body, errors) with MSW tests | FR-027, FR-029, AC-009, AC-010 | TASK-011, TASK-013 | TEST-009, TEST-010 | planned |
| TASK-015 | TS context pack parity and Copy prompt menu; network assertion | FR-031, NFR-006, AC-013 | TASK-007 | TEST-013 | planned |
| TASK-016 | Accessibility pass and cross-browser Playwright projects | NFR-005, NFR-009, AC-016 | TASK-004, TASK-005, TASK-006, TASK-007, TASK-008, TASK-009 | TEST-016 | planned |
| TASK-017 | `studio.yml`, base-path build, CSP meta, bundle budget; scratch-repo run | FR-032, NFR-004, NFR-007, CON-004, AC-014, AC-016 | TASK-014 | TEST-014, TEST-016 | planned |
| TASK-018 | Docs (`docs/framework/studio.md`, nav, CHANGELOG) and release asset packaging | FR-032, CON-006 | TASK-017 | TEST-016 review | planned |
| TASK-019 | Converge: evidence, deviations, status per owner decision | — | TASK-018 | TEST-016 | planned |
