# Concepts

## Requirements and related records

- **Business requirement (`BR-`)**: desired business outcome or policy.
- **Functional requirement (`FR-`)**: observable system behavior.
- **Non-functional requirement (`NFR-`)**: quality attribute or operating constraint such as reliability, privacy, or accessibility.
- **Constraint (`CON-`)**: a boundary the solution must respect.
- **Assumption**: treated as true pending confirmation; give it an owner and revisit date when possible.
- **Acceptance criterion (`AC-`)**: an evaluable condition for deciding whether a requirement or feature is satisfied.
- **User story (`US-`)**: a concise user-centered expression of need.
- **Decision (`ADR-`)**: durable reasoning for an important technical choice.
- **Task (`TASK-`)** and **verification (`TEST-`)**: work and evidence references.

Use normative language consistently: MUST is mandatory, SHOULD is recommended with documented exceptions, MAY is optional. IDs identify items that need stable reference; do not ID every sentence. Do not casually recycle retired IDs.

## Statuses

Feature statuses: `draft`, `proposed`, `approved`, `in-progress`, `verified`, `deferred`, `deprecated`. Verification statuses: `planned`, `implemented`, `verified`, `blocked`, `waived`, `deprecated`. ADR statuses: `proposed`, `accepted`, `rejected`, `deprecated`, `superseded`. A status is a recorded state, not approval by itself: the responsible humans define who may approve.

## Canonical artifacts

Approved Markdown, Mermaid source, YAML contracts, and JSON schemas committed to the project are canonical. Rendered diagrams and agent-specific command files are derived or optional adapters. Choose one owner for each requirement and contract; links are safer than copied versions.
