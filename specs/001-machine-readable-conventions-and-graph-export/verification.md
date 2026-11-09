# Verification: 001 Machine-readable conventions and graph export

Statuses: `planned`, `implemented`, `verified`, `blocked`, `waived`, `deprecated`.

Record command, environment (OS, Python version), commit SHA, result and date when a check runs.

| Requirement | Acceptance criterion | Verification ID / method | Evidence or location | Status |
|---|---|---|---|---|
| FR-001 | AC-001 | TEST-001 automated: `python -m unittest tests.test_frontmatter -v` | not yet run | planned |
| FR-002 | AC-002 | TEST-002 automated: `python -m unittest tests.test_legacy_meta -v` | not yet run | planned |
| FR-003 | AC-003 | TEST-003 automated: `python -m unittest tests.test_migrate -v` + golden diff review | not yet run | planned |
| FR-004 | AC-004 | TEST-004 automated: `python -m unittest tests.test_tables -v` | not yet run | planned |
| FR-005 | AC-005 | TEST-005 automated: `python -m unittest tests.test_identity -v`; `python3 scripts/validate_docs.py --graph` exits 1 on duplicate fixture | not yet run | planned |
| FR-006 | AC-006 | TEST-006 automated: `python -m unittest tests.test_statuses -v` | not yet run | planned |
| FR-007 | AC-007 | TEST-007 automated: `python -m unittest tests.test_new_feature_ids -v` | not yet run | planned |
| FR-008 | AC-008 | TEST-008 automated: export fixture; validate against schema; compare golden | not yet run | planned |
| FR-009 | AC-009 | TEST-009 automated: `python -m unittest tests.test_links -v` | not yet run | planned |
| FR-010 | AC-010 | TEST-010 integration: `python -m unittest tests.test_history -v` (real git, fixed dates); assert no `@` in author fields | not yet run | planned |
| FR-011 | AC-011 | TEST-011 integration: incremental parse count; rebase rebuild equals cold export | not yet run | planned |
| FR-012 | AC-012 | TEST-012 automated: `python -m unittest tests.test_metrics -v` vs `expected-metrics.json`; shallow clone | not yet run | planned |
| BR-001 | AC-012 | TEST-012 automated: coverage definitions contain "linked coverage, not proof" | not yet run | planned |
| FR-013 | AC-013 | TEST-013 automated: malformed-file fixture; exit codes with and without `--strict` | not yet run | planned |
| FR-014 | AC-014 | TEST-014 automated: byte comparison of two exports; dirty flag | not yet run | planned |
| FR-015 | AC-015 | TEST-015 automated: `python3 scripts/context_pack.py 003:TASK-002 --budget 4000` vs golden | not yet run | planned |
| FR-016 | AC-016 | TEST-016 automated: `python -m unittest tests.test_config -v` | not yet run | planned |
| FR-017 | AC-017 | TEST-017 automated: `python -m unittest tests.test_readers -v` (craftrail reader + test-only reader) | not yet run | planned |
| BR-003 | AC-018 | TEST-018 automated: `approval-unrecorded` diagnostic; migration leaves approver absent | not yet run | planned |
| NFR-001 | AC-019 | TEST-019 CI: stdlib-only matrix on all supported Python versions | not yet run | planned |
| NFR-002 | AC-019 | TEST-019 CI benchmark: cold < 15 s, incremental < 2 s on `ubuntu-latest` | not yet run | planned |
| NFR-003 | AC-019 | TEST-019 CI coverage: ≥ 90% overall; 100% branch for parsers | not yet run | planned |
| BR-002 | AC-019 | TEST-019 automated: `git check-ignore craftrail.json .craftrail/cache/` | not yet run | planned |

Waivers require an accountable owner, rationale, and accepted risk. Code generation alone is not evidence.
