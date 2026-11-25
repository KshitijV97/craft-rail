# Tasks: 001 Machine-readable conventions and graph export

Dependency-ordered slices; each task is one reviewable pull request. Implement only after the spec is `approved`.

| ID | Task / expected output | Requirement / AC | Depends on | Verification | Status |
|---|---|---|---|---|---|
| TASK-001 | Resolve open questions (contracts and ADR locations); move files if needed; add `.gitignore` entries | BR-002 | — | TEST-019 review | planned |
| TASK-002 | `frontmatter.py`: profile parser with line-accurate errors; tests for every grammar rule and invalid case | FR-001, AC-001 | TASK-001 | TEST-001 | planned |
| TASK-003 | `legacy_meta.py`; precedence and conflict rules; deprecation diagnostic | FR-002, AC-002 | TASK-002 | TEST-002 | planned |
| TASK-004 | `md_tables.py` and canonical header matching; `declarations.py` | FR-004, AC-004 | TASK-001 | TEST-004 | planned |
| TASK-005 | `items.py`, `resolve.py`, `statuses.py`: canonical keys, scoping, vocabularies with notes | FR-005, FR-006, AC-005, AC-006 | TASK-003, TASK-004 | TEST-005, TEST-006 | planned |
| TASK-006 | `validate_docs.py --graph`: global uniqueness, statuses, front-matter, dangling references, `approval-unrecorded`; existing tests unchanged and green | FR-005, FR-006, BR-003, AC-005, AC-006, AC-018 | TASK-005 | TEST-005, TEST-006, TEST-018 | planned |
| TASK-007 | `migrate_frontmatter.py` with `--check`; migrate this repository and templates; golden diffs | FR-003, BR-003, AC-003, AC-018 | TASK-003 | TEST-003, TEST-018 | planned |
| TASK-008 | `new_feature.py`: front-matter, global requirement IDs, `--local-requirement-ids` | FR-007, AC-007 | TASK-005, TASK-007 | TEST-007 | planned |
| TASK-009 | `readers/` protocol + `craftrail` reader; `links.py`; `graph.py` serializer; `export_graph.py --no-history`; golden export | FR-008, FR-009, FR-013, FR-014, FR-017, AC-008, AC-009, AC-013, AC-014, AC-017 | TASK-006 | TEST-008, TEST-009, TEST-013, TEST-014, TEST-017 | planned |
| TASK-010 | `tests/fixtures/make_fixture_repo.py`: deterministic histories (transitions, renames, deletions, re-adds, rebase, shallow clone, 2,000-item perf repo) | FR-010, FR-011 | TASK-009 | TEST-010 | planned |
| TASK-011 | `history.py`: event mining, author names only, cache, ancestry check | FR-010, FR-011, AC-010, AC-011 | TASK-010 | TEST-010, TEST-011 | planned |
| TASK-012 | `config.py`: `.craftrail/studio.json` loading, defaults, invalid-file diagnostics | FR-016, AC-016 | TASK-009 | TEST-016 | planned |
| TASK-013 | `metrics.py`: every metric in the spec, partial flags, linked-coverage labels; hand-calculated `expected-metrics.json` | FR-012, BR-001, AC-012 | TASK-011, TASK-012 | TEST-012 | planned |
| TASK-014 | `context.py` + `context_pack.py`; golden packs; shared fixtures for feature 002 parity | FR-015, AC-015 | TASK-009 | TEST-015 | planned |
| TASK-015 | CI: stdlib matrix for new tests, coverage thresholds, export benchmark job | NFR-001, NFR-002, NFR-003, AC-019 | TASK-013, TASK-014 | TEST-019 | planned |
| TASK-016 | Docs: `docs/framework/machine-readable-conventions.md`; updates to concepts, validation, feature-spec guide, ecosystem comparison; nav; CHANGELOG | CON-002, CON-003 | TASK-015 | TEST-019 review | planned |
| TASK-017 | Converge: record evidence in verification, note deviations, set status per owner decision | — | TASK-016 | TEST-019 | planned |
