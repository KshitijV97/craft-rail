# Feature 001: Machine-readable conventions and graph export

- **Status:** proposed
- **Owner:** CraftRail maintainer
- **Created:** 2026-11-09
- **Updated:** 2026-11-09
- **Related issues/PRs:** proposal pull request `proposal/craftrail-studio`
- **Decision:** [ADR-001](../../docs/decisions/ADR-001-craftrail-studio-git-native-static-studio.md)
- **Followed by:** [Feature 002: CraftRail Studio](../002-craftrail-studio/spec.md)

## Context and problem

CraftRail keeps requirements, decisions, tasks and verification evidence as Markdown in Git. Tools, agents and CI cannot reliably read project state from these files today:

- Feature metadata is a bullet block (`- **Status:** draft`) parsed by `scripts/validate_docs.py`. Registers, tasks and verification are Markdown tables with mostly consistent headers.
- `scripts/new_feature.py` copies `templates/feature/`. Every feature therefore contains `TASK-001` and `TEST-001`, which are unique only within one feature, as [concepts](../../docs/framework/concepts.md) allows. The script also puts the feature number into requirement placeholders, so feature `001` declares `FR-001`, which can collide with the project register.
- The validator detects duplicate IDs only within one file.
- [Traceability and verification](../../docs/framework/traceability-and-verification.md) warns that dashboard percentages can create false confidence.

This feature makes the conventions machine-readable and exports one deterministic graph document. Agents, CI gates and the optional [Studio](../002-craftrail-studio/spec.md) can all consume it. It changes CraftRail core, so it lands and is released before Studio.

## Goals and measurable outcomes

- Any tool can read project state from one JSON file without parsing Markdown. Signal: `craftrail.json` validates against the graph schema for the CraftRail repository and the fixture repositories.
- Project-wide ID collisions are detectable. Signal: `validate_docs.py --graph` fails on every duplicate fixture.
- Agents get small, linked context. Signal: `context_pack.py` output stays within budget and matches golden files.
- Existing adopters are not broken. Signal: the existing 26 tests and validator runs on unmigrated repositories still pass. Graph mode is opt-in in this release.

## Actors and scenarios

- **Maintainer:** runs `validate_docs.py --graph` in CI to catch collisions and unknown statuses.
- **Coding agent (any provider):** runs `python3 scripts/context_pack.py 003:TASK-002` before implementing a task.
- **CI or external dashboard:** consumes `craftrail.json` for gates or reporting.
- **Adopter with an existing repository:** runs `migrate_frontmatter.py --check`, then migrates when ready.

## Scope and non-goals

- In scope: the front-matter profile, canonical table conventions, the identity model, validator graph mode, the migration tool, `new_feature.py` changes, the exporter (items, links, Git-history events, metrics, diagnostics), the source-reader interface with a CraftRail reader, the context-pack CLI, `.craftrail/studio.json` configuration loading, and docs updates.
- Non-goals: the Studio web app and editing (feature 002); readers for other systems (OpenSpec, Spec Kit), which are named follow-ups; workflow orchestration of any kind (`CON-003`); AI model calls.

## Requirements

### Conventions and identity

- `FR-001`: The system MUST define and validate a **front-matter profile**: a restricted YAML subset between `---` lines at the top of a Markdown file. The profile allows these keys:
  - `craftrail` (profile version, integer, required when front-matter is present);
  - `type`;
  - `id`;
  - `feature` (owning feature number in plan, tasks and verification files);
  - `title`;
  - `status`;
  - `owner`;
  - `created`;
  - `updated`;
  - `approved_by`;
  - `approved_on`;
  - `related`;
  - `tags`;
  - `supersedes` and `superseded_by` (ADRs);
  - extension keys prefixed `x_`.

  The grammar is defined in [Front-matter profile](#front-matter-profile). The contract is [craftrail-frontmatter.schema.json](contracts/craftrail-frontmatter.schema.json).
- `FR-002`: The parser MUST also read the legacy bullet metadata block (`- **Key:** value` lines directly under the H1). It MUST emit a `deprecated-metadata` warning for files using only the legacy form. When both forms are present, front-matter wins, and conflicting values produce an error.
- `FR-003`: The system MUST provide `python3 scripts/migrate_frontmatter.py [--check] [paths…]`. The command converts legacy metadata to front-matter, idempotently and without changing any other line. `--check` changes nothing and exits non-zero if a migration is needed.
- `FR-004`: The parser MUST recognise item tables by **canonical headers**, matched case-insensitively after trimming and collapsing whitespace, as listed in [Canonical tables](#canonical-tables). It MUST ignore other tables.
- `FR-005`: The system MUST assign every item a **canonical key**:
  - Features use `F<number>` (`F003`).
  - Project-wide kinds (`BR`, `FR`, `NFR`, `CON`, `US`, `ADR`) use the bare ID (`FR-012`).
  - Feature-local kinds (`AC`, `TASK`, `TEST`) use `<feature-number>:<ID>` (`003:TASK-002`).

  In graph mode (`validate_docs.py --graph`), duplicate declarations of a project-wide ID outside exempt paths MUST be an error.
- `FR-006`: The validator MUST check item statuses against per-type vocabularies ([Status vocabularies](#status-vocabularies)). Unknown statuses are errors in graph mode. A trailing parenthetical note, such as `verified (illustrative)`, MUST be read as the base status plus a note.
- `FR-007`: `scripts/new_feature.py` MUST write front-matter into new feature files. It MUST replace requirement placeholders (`FR-NNN`, `NFR-NNN`, `BR-NNN`, `CON-NNN`) with the next free project-wide number per kind instead of the feature number. It MUST keep `AC`, `TASK` and `TEST` numbering local, starting at `001`. The previous behaviour MUST remain available behind `--local-requirement-ids` for one minor release.

### Exporter

- `FR-008`: `python3 scripts/export_graph.py [--out PATH] [--no-history] [--since REF] [--strict]` MUST write a JSON document conforming to [craftrail-graph.schema.json](contracts/craftrail-graph.schema.json). The default output is `craftrail.json` at the repository root, which is ignored by Git.
- `FR-009`: The exporter MUST extract typed links using [Link extraction](#link-extraction). Each link records its source location.
- `FR-010`: Unless `--no-history` is given, the exporter MUST mine Git history through the `git` CLI into `events` (`item_created`, `status_changed`, `owner_changed`, `item_removed`). Each event records the commit SHA, ISO-8601 timestamp and author **name** (never email). Renames MUST be followed.
- `FR-011`: The exporter MUST keep an incremental cache in `.craftrail/cache/` keyed by the last processed commit. It MUST rebuild fully when that commit is no longer an ancestor of `HEAD`.
- `FR-012`: The exporter MUST compute the metrics in [Metrics](#metrics) and include each metric's definition text. If history is shallow or missing, history-based metrics MUST be marked `partial: true` with a reason.
- `FR-013`: The exporter MUST report problems as structured diagnostics (`severity`, `code`, `message`, `file`, `line`). It MUST exit non-zero only for errors, and only when `--strict` is given. A problem in one file MUST NOT stop the export of other files.
- `FR-014`: For the same commit and a clean working tree, output MUST be byte-identical across runs. Keys are sorted, collections are ordered by canonical key, and `generated_at` is the `HEAD` commit time. A dirty working tree MUST set `repo.dirty: true`.
- `FR-015`: `python3 scripts/context_pack.py <key> [--budget CHARS] [--prompt NAME]` MUST output a Markdown context pack using the [Context pack algorithm](#context-pack-algorithm), optionally followed by a prompt from [workflow prompts](../../docs/framework/workflow-prompts.md).
- `FR-016`: Tools MUST read optional configuration from `.craftrail/studio.json`, validated against the `config` definition of the graph schema. The configuration covers artifact and exempt globs, board column mappings (consumed by feature 002), the blocked-age threshold, the stale-ADR threshold, the context budget and the forge URL template. Missing keys take documented defaults, and an invalid file produces a diagnostic and falls back to defaults.
- `FR-017`: The exporter MUST obtain items and links through a **source-reader interface** ([Source readers](#source-readers)). v1 MUST ship exactly one reader, `craftrail`. Every item MUST record its `source`, and `repo.readers` MUST list the readers used. Adding a reader MUST NOT require changes to the graph contract.

## Non-functional requirements

- `NFR-001`: The validator, exporter, migration tool and context-pack CLI MUST use only the Python standard library and support every Python version the core supports.
- `NFR-002`: On GitHub's `ubuntu-latest` runner, export of the reference fixture (2,000 items, 1,500 commits) MUST finish in under 15 s cold and under 2 s incremental with one new commit.
- `NFR-003`: The new Python modules MUST have at least 90% line+branch coverage. The front-matter parser, table tokenizer and status parser MUST have 100% branch coverage.

## Business rules

- `BR-001`: Every coverage metric's definition MUST label it "linked coverage, not proof" ([traceability and verification](../../docs/framework/traceability-and-verification.md)).
- `BR-002`: Generated outputs (`craftrail.json`, `.craftrail/cache/`) MUST NOT be committed. `.gitignore` MUST list them.
- `BR-003`: Tools MUST NOT invent approval records. A feature or ADR in an approved or accepted state without `approved_by`/`approved_on` MUST produce an `approval-unrecorded` error in graph mode. The migration tool MUST NOT fill those fields.

## Constraints

- `CON-001`: No AI-provider or forge SDK may be a dependency of core tools.
- `CON-002`: Canonical artifacts MUST stay readable and reviewable as plain Markdown. No convention may require a tool to understand a file.
- `CON-003`: This feature MUST NOT add workflow commands, change lifecycles or agent execution ([ADR-001](../../docs/decisions/ADR-001-craftrail-studio-git-native-static-studio.md), "Relationship to OpenSpec and GitHub Spec Kit").

## Acceptance criteria

- `AC-001`: Given a file with valid front-matter, when the validator runs, then it reports no front-matter errors. Given each invalid case in the fixture corpus (bad key, nested map, multi-line string, wrong type, missing `craftrail`), then it reports one error with file and line. (`FR-001`)
- `AC-002`: Given a spec with only legacy bullet metadata, when exported, then its status is read correctly and a `deprecated-metadata` warning is emitted. Given conflicting front-matter and bullets, then an error is emitted. (`FR-002`)
- `AC-003`: Given this repository, when `migrate_frontmatter.py` runs twice, then the second run changes nothing, and the first run's diff touches only metadata lines. `--check` exits 1 before migration and 0 after. (`FR-003`)
- `AC-004`: Given tables whose headers differ only in case or spacing from the canonical ones, when exported, then their rows become items. Given an unrelated table, then no items are created from it. (`FR-004`)
- `AC-005`: Given two features that each declare `TASK-001`, when exported, then keys `001:TASK-001` and `002:TASK-001` both exist. Given `FR-004` declared in two files, when `validate_docs.py --graph` runs, then it exits non-zero naming both locations. (`FR-005`)
- `AC-006`: Given `verified (illustrative)` in a verification row, when exported, then status is `verified` and note is `illustrative`. Given `donee`, then graph mode reports an unknown-status error. (`FR-006`)
- `AC-007`: Given registers that already declare `FR-001` to `FR-007`, when `new_feature.py "X"` runs, then the new spec declares `FR-008`, its tasks start at `TASK-001`, and the files contain valid front-matter. With `--local-requirement-ids`, the old numbering is produced. (`FR-007`)
- `AC-008`: Given the fixture repository, when exported, then the output validates against the graph schema and matches the committed golden file. (`FR-008`, `FR-014`)
- `AC-009`: Given a tasks row `| TASK-002 | … | FR-003, AC-002 | TASK-001 | TEST-002 … | planned |` in feature `004`, when exported, then the links include `004:TASK-002 implements FR-003`, `004:TASK-002 implements 004:AC-002`, `004:TASK-002 depends_on 004:TASK-001` and `004:TASK-002 verified_by 004:TEST-002`. (`FR-009`)
- `AC-010`: Given a fixture history where `003:TASK-001` moves `planned → in-progress → done` across three commits and its file is renamed in between, when exported, then three events exist with correct timestamps and author names, and no email appears in the output. (`FR-010`)
- `AC-011`: Given an exported repository, when one commit is added and export runs again, then only that commit is parsed (verified by a parse-count hook in tests). Given a rebase that removes the cached commit, then a full rebuild happens and the output equals a cold export. (`FR-011`)
- `AC-012`: Given the metrics fixture with known timestamps, when exported, then every metric equals the hand-calculated value in `expected-metrics.json`, and coverage definitions contain "linked coverage, not proof". Given a shallow clone, then history metrics have `partial: true` with reason `shallow-clone`. (`FR-012`, `BR-001`)
- `AC-013`: Given one malformed file among valid ones, when exported, then valid files' items are present, one error diagnostic points at the malformed file, and the exit code is 0 without `--strict` and 1 with it. (`FR-013`)
- `AC-014`: Given a clean checkout, when exported twice, then the outputs are byte-identical. Given an uncommitted change, then `repo.dirty` is `true`. (`FR-014`)
- `AC-015`: Given `003:TASK-002` in the fixture, when `context_pack.py 003:TASK-002 --budget 4000` runs, then the output is at most 4,000 characters, contains the task, its linked requirement and ACs with file paths, and matches the golden file. (`FR-015`)
- `AC-016`: Given a valid `.craftrail/studio.json` changing `blocked_threshold_days`, when exported, then `config` reflects it and the blocked-age metric uses it. Given an invalid file, then a diagnostic is emitted and defaults are used. (`FR-016`)
- `AC-017`: Given the fixture, when exported, then every item has `source: "craftrail"` and `repo.readers` lists `craftrail`. Given a test-only reader registered in the test suite, then its items appear with its source name, and the output still validates against the unchanged schema. (`FR-017`)
- `AC-018`: Given a migrated approved feature without `approved_by`, when `validate_docs.py --graph` runs, then it reports `approval-unrecorded`, and the migration tool left the field absent. (`BR-003`)
- `AC-019`: Given CI, when the quality jobs run, then:
  - core tests pass on every supported Python version with only the standard library;
  - coverage meets `NFR-003`;
  - the export benchmark meets `NFR-002`;
  - `git check-ignore` confirms `craftrail.json` and `.craftrail/cache/` are ignored.

  (`NFR-001`–`NFR-003`, `BR-002`)

## Edge cases and failure paths

- A table cell with an escaped pipe (`\|`) or inline code containing pipes MUST parse correctly.
- An item ID that appears only in prose becomes a `mentions` link, not an item.
- A folder under `specs/` without a number is ignored, with an info diagnostic.
- Two features with the same number produce an error.
- Files over 1 MB are skipped with a warning. Non-UTF-8 files are skipped with an error.
- Merge-conflict markers in a file produce an error, and that file's items are marked `frozen`.
- An item deleted and later re-added with the same ID emits `item_removed` then `item_created`. Metrics treat it as reopened.
- Running outside a Git repository: export still works, `repo.has_git` is `false`, and history metrics are partial with reason `no-git`.

## Data, dependencies, and interfaces

### Front-matter profile

```text
frontmatter := "---" NEWLINE { line } "---" NEWLINE
line        := key ":" SP value [SP "#" comment] NEWLINE
             | key ":" NEWLINE { "  - " scalar NEWLINE }      ; block list of scalars
             | "#" comment NEWLINE | NEWLINE
key         := [a-z][a-z0-9_]*
value       := scalar | "[" [ scalar { "," SP scalar } ] "]"   ; inline list
scalar      := integer | "true" | "false" | date | quoted | plain
date        := YYYY-MM-DD
quoted      := '"' { char | '\"' } '"'
plain       := text without leading [ "[", "{", "&", "*", "!", "|", ">", "'", '"', "%", "@", "`" ] and without ": " or " #"
```

No anchors, aliases, tags, nested mappings, flow mappings or multi-line scalars. Keys and types per `type` are defined in [craftrail-frontmatter.schema.json](contracts/craftrail-frontmatter.schema.json).

Example (feature spec):

```yaml
---
craftrail: 1
type: feature
id: "003"
title: Account recovery
status: approved
owner: Identity lead
created: 2026-11-09
updated: 2026-11-12
approved_by: Identity lead
approved_on: 2026-11-12
related: [FR-012, ADR-004]
tags: [auth, security]
---
```

### Canonical tables

| Table (file) | Required headers | Item key from | Optional headers |
|---|---|---|---|
| Requirement register (`docs/project/requirements/*.md`) | `ID` first, any title header second, `Status` | `ID` cell (project-wide kind) | `Owner`, `Rationale/source`, `Acceptance / verification`, `Scope`, `Type (BR or CON)`, `Measure or evaluation method` |
| Tasks (`specs/NNN-*/tasks.md`) | `ID`, `Task / expected output` (alias `Expected output`), `Requirement / AC`, `Depends on`, `Verification`, `Status` | `ID` cell (feature-local) | `Owner`, `Estimate`, `Notes` |
| Verification (`specs/NNN-*/verification.md`) | `Requirement`, `Acceptance criterion`, `Verification ID / method` (alias `Verification`), `Evidence or location` (alias `Evidence / location`), `Status` | first `TEST-` ID in the verification cell (feature-local) | `Owner`, `Date`, `Environment` |
| ADR index (`docs/**/decisions/README.md`) | `ADR`, `Decision`, `Status` | not items (ADR files are canonical); used for consistency diagnostics only | — |

Declaration bullets in `spec.md`: `` - `FR-001`: text `` (colon optional for legacy). A bullet declares an item. Its status is `proposed` unless a register row or the item's front-matter says otherwise.

### Status vocabularies

| Item type | Statuses (board column order) |
|---|---|
| feature | `draft`, `proposed`, `approved`, `in-progress`, `verified`, `deferred`, `deprecated` |
| requirement (`BR`/`FR`/`NFR`/`CON`/`US`) | `proposed`, `approved`, `implemented`, `verified`, `deferred`, `deprecated`, `superseded` |
| acceptance criterion | derived: `uncovered`, `planned`, `implemented`, `verified`, `blocked`, `waived` (from linked verification rows; worst state wins) |
| task | `planned`, `in-progress`, `blocked`, `in-review`, `done`, `dropped` |
| verification (`TEST`) | `planned`, `implemented`, `verified`, `blocked`, `waived`, `deprecated` |
| ADR | `proposed`, `accepted`, `rejected`, `deprecated`, `superseded` |

Done states for metrics: task `done`; feature, verification and requirement `verified`. Started states: task and feature `in-progress`.

### Link extraction

| Source | Rule | Link type |
|---|---|---|
| Tasks `Requirement / AC` cell | each ID | `implements` |
| Tasks `Depends on` cell | each `TASK-` ID | `depends_on` |
| Tasks `Verification` cell | each `TEST-` ID | `verified_by` |
| Verification row `Requirement` cell | each ID | `verifies` (TEST → requirement) |
| Verification row `Acceptance criterion` cell | each ID | `verifies` (TEST → AC) |
| Verification row `Evidence` cell | non-empty and not a placeholder | sets the `evidence` attribute |
| Spec AC bullet | requirement IDs in its text | `refines` (AC → requirement) |
| Spec | every declared item | `belongs_to` (item → feature) |
| Front-matter `related` | each ID | `related` |
| ADR "Supersedes / superseded by" section or front-matter | ADR IDs | `supersedes` |
| Any other ID mention in prose | — | `mentions` (weak; not used for coverage) |

Feature-local IDs in a feature's own files resolve to that feature. Cross-feature references use `NNN:ID`. Unresolvable references produce `dangling-reference` diagnostics.

### Metrics

All time metrics use event timestamps (commit author time, UTC). Weeks are ISO weeks. Values cover tasks unless stated otherwise.

| Metric | Definition |
|---|---|
| Linked coverage (requirements) | approved-or-later requirements with at least one `verifies` link from a `verified` TEST ÷ approved-or-later requirements. Label: "linked coverage, not proof". |
| Linked coverage (ACs) | ACs whose derived status is `verified` or `waived` ÷ all ACs in approved-or-later features. Same label. |
| Cycle time | first transition into a started state → first subsequent transition into a done state. Reported as median, 85th percentile and per item. |
| Lead time | `item_created` → first done transition |
| Throughput | items entering a done state per ISO week |
| WIP | items in a started state at the end of each day |
| Cumulative flow | per day, items per status |
| Burn-up | per day, cumulative done count and total scope (created minus removed or dropped) |
| Ageing | for items currently started: HEAD time − latest start |
| Blocked age | for items currently `blocked`: HEAD time − entry into `blocked`. Items over the threshold (default 5 days) are flagged. |
| ADR staleness | `proposed` ADRs older than the threshold (default 14 days) since `item_created` |

If a tasks table has a numeric `Estimate` column, burn-up and throughput are also computed by estimate sum. No velocity is computed without estimates.

### Context pack algorithm

1. Start from the root item. Collect neighbours by link type in priority order:
   1. `implements` / `refines` targets;
   2. `verified_by` / `verifies`;
   3. `depends_on`;
   4. `belongs_to` feature;
   5. `related` ADRs.

   Use depth 1. For a feature root, use depth 2.
2. For each item, emit `### <key> — <title> (<status>)`, `Source: <path>:<line>`, then its excerpt (at most 600 characters, whole sentences).
3. If over budget (default 8,000 characters), drop excerpts in reverse priority order, then whole items, but never the root or its direct requirements.
4. Append `Read the source files listed above before acting.`, then the selected workflow prompt with `[spec path]`/`[IDs]` filled in.
5. Output is deterministic. Feature 002 reimplements this in TypeScript and MUST match this output on shared fixtures.

### Source readers

```python
class SourceReader(Protocol):
    name: str  # e.g. "craftrail"; recorded as item.source
    version: str

    def discover(self, root: Path, config: Config) -> list[Path]: ...
    def read(self, path: Path, text: str) -> ReadResult: ...  # items, links, diagnostics
    def keys_for_history(
        self, path: Path, text: str
    ) -> dict[str, ItemState]: ...  # key -> status/owner for event mining
```

Readers are registered in `craftrail_core/readers/__init__.py`. v1 registers only `craftrail`. Future readers (OpenSpec, Spec Kit) map their artifacts onto the same item types and links. They do not change canonical files and add no workflow behaviour (`CON-003`).

### Interfaces

- Graph JSON: [craftrail-graph.schema.json](contracts/craftrail-graph.schema.json) (`schema_version` `1.0`; additive changes bump the minor version, breaking changes the major).
- Front-matter: [craftrail-frontmatter.schema.json](contracts/craftrail-frontmatter.schema.json).

## Security, privacy, accessibility, observability

- **Security:** the exporter only reads files and runs read-only `git` commands (`log`, `show`, `rev-parse`, `merge-base`). Paths in output are repository-relative, and absolute paths are never exported.
- **Privacy:** author names only; email addresses are never read into output. No telemetry.
- **Accessibility:** not applicable (CLI tools; output is text and JSON).
- **Observability:** `--verbose` prints timings per phase.

## Assumptions, questions, and risks

| Type | Item | Owner / resolution |
|---|---|---|
| Question | Final location of the contracts: keep in this feature folder, move to `contracts/`, or move to `docs/framework/contracts/`? | Maintainer, TASK-001 |
| Question | Is `docs/decisions/` the right home for CraftRail's own ADRs (proposed in this PR)? | Maintainer, TASK-001 |
| Assumption | The core minimum Python version is unchanged by this feature. | Maintainer |
| Risk | Changing `new_feature.py` ID allocation affects adopters. Mitigation: CHANGELOG entry and `--local-requirement-ids`. | Maintainer |
| Risk | Teams may treat metrics as performance targets. Mitigation: definitions everywhere and guidance in docs. | Maintainer |

## Traceability

- Decision: [ADR-001](../../docs/decisions/ADR-001-craftrail-studio-git-native-static-studio.md)
- Plan: [plan.md](plan.md) · Tasks: [tasks.md](tasks.md) · Verification: [verification.md](verification.md)
- Consumer: [Feature 002](../002-craftrail-studio/spec.md)
