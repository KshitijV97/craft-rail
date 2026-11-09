# ADR-001: Machine-readable conventions and an optional, Git-native Studio view

- **Status:** proposed
- **Date:** 2026-11-09
- **Decision owner:** CraftRail maintainer
- **Related:** feature `specs/001-machine-readable-conventions-and-graph-export/`, feature `specs/002-craftrail-studio/`, contracts in `specs/001-machine-readable-conventions-and-graph-export/contracts/`; guides [concepts](../framework/concepts.md), [traceability and verification](../framework/traceability-and-verification.md), [agent compatibility](../framework/agent-compatibility.md), [ecosystem comparison](../framework/ecosystem-comparison.md)

## Context and forces

CraftRail records intent, decisions, work and evidence as Markdown in Git. People want what tools like Jira and Trello offer: boards, filters, item detail, history, burn-up, cycle time and WIP. They also want what those tools can't do: requirement → acceptance → task → test → evidence traceability. The relevant forces:

1. **Single source of truth.** Generated views must never become a second source of policy ([concepts](../framework/concepts.md), "Canonical versus generated information"). A tracker with its own database would drift away from `spec.md`, `tasks.md` and `verification.md`.
2. **Agent neutrality.** The core must not depend on any AI provider, and adapters stay optional (`AGENTS.md`).
3. **Dependency-free core.** CraftRail's Python tools use only the standard library.
4. **Cost.** Hosting should be free or nearly free, and token spend should be zero unless a person explicitly runs an AI action.
5. **Honest metrics.** A dashboard percentage can create false confidence ([traceability and verification](../framework/traceability-and-verification.md)). Metrics must say what they measure.
6. **Parseability.** The current conventions mix bullet metadata (`- **Status:** draft`), Markdown tables and prose. Parsing is fragile, and the same IDs (for example `TASK-001`) appear in many feature folders.
7. **Ecosystem fit.** CraftRail says it "does not attempt to replace Spec Kit or OpenSpec's command-driven feature orchestration" ([ecosystem comparison](../framework/ecosystem-comparison.md)). Any new tooling must keep that promise.

## Decision

The work is split into two features. They are approved, built and released in order.

**Feature 001: machine-readable conventions and graph export (CraftRail core).**

1. **Front-matter profile.** A restricted YAML front-matter profile carries per-file metadata. Per-item data stays in Markdown tables and declaration bullets with **canonical column headers**. Both are documented as contracts and checked by the standard-library validator. Files without front-matter still parse through the legacy bullet metadata, and a migration command converts them.
2. **Identity model.** Project-wide kinds (`BR`, `FR`, `NFR`, `CON`, `US`, `ADR`) are unique across the repository. Feature-local kinds (`AC`, `TASK`, `TEST`) are qualified by feature number, giving keys like `003:TASK-002`. This formalises what [concepts](../framework/concepts.md) already permits.
3. **Exporter.** `scripts/export_graph.py` uses only the standard library. It reads repository artifacts through **source readers** and Git history through the `git` CLI, and writes one versioned JSON document, `craftrail.json`. The document holds items, typed links, status-change events, computed metrics and diagnostics. v1 ships a CraftRail reader. The reader interface is public so that other spec systems, such as OpenSpec's `specs/` and `changes/` folders, can be read later without changing the graph contract. The exporter uses no AI.
4. **Context packs.** `scripts/context_pack.py` builds small, linked, deterministic context bundles for any agent.

**Feature 002: CraftRail Studio (optional).**

5. **Static app.** A static single-page app in `studio/` reads `craftrail.json` and renders an overview, boards, a traceability graph and matrix, item detail, history, metrics and decisions. It has no server and no database, and can be hosted on any static host.
6. **Editing through Git only.** Every edit is a typed patch that a single TypeScript patch engine turns into a minimal text diff. Edits are saved through a pluggable Git backend:
   - `local`: a standard-library HTTP server bound to `127.0.0.1`;
   - `github`: one commit on a branch plus a pull request; approval changes always go through a pull request.
7. **No model calls.** Studio only offers copyable prompts built from context packs and CraftRail's neutral workflow prompts.

## Relationship to OpenSpec and GitHub Spec Kit

These tools sit at different layers and are meant to coexist.

| | OpenSpec / Spec Kit | CraftRail conventions + Studio |
|---|---|---|
| Job | Author and drive spec-driven changes through a CLI and agent commands (for example explore → propose → apply → archive) | Keep intent, decisions and evidence canonical in Git, and make the state of the project visible |
| Main question | "What should this change be, and how does the agent carry it out?" | "Where do we stand, what is blocked, which requirements lack evidence, how long does work take?" |
| Interface | CLI + agent integrations | Validator/exporter + static web view with Git-diff editing |
| AI | Built around driving coding agents | None; only copyable prompts |

Commitments that follow from this decision:

- **Studio is a view and tracking layer, not a spec-authoring or change-orchestration tool.** It will not add workflow commands, a change lifecycle (propose/apply/archive), agent execution, or "run" buttons. Those requests belong to OpenSpec, Spec Kit, or a future optional adapter, not to Studio.
- **Format changes are limited to what parsing needs:** front-matter keys, canonical table headers and the identity model. They stay readable plain Markdown, and teams using OpenSpec or Spec Kit keep those tools' files canonical for change proposals, as the ecosystem comparison already recommends.
- **Source readers make Studio useful to OpenSpec and Spec Kit users too.** An OpenSpec reader is the first named follow-up after v1. A team could drive changes with OpenSpec and use Studio to see the whole project.
- The [ecosystem comparison](../framework/ecosystem-comparison.md) will be updated to describe this positioning when feature 001 ships.

## Alternatives considered

| Alternative | Why not chosen |
|---|---|
| Jira, Linear or another SaaS tracker | Paid, proprietary, and a second source of truth that drifts from specs |
| GitHub Projects or Issues as the tracker | Free, but duplicates status and is tied to one forge. Acceptable later as a one-way mirror adapter only. |
| Git-based CMS (Decap, TinaCMS, Keystatic) | Good for editing prose, but no traceability, boards, metrics or ID model |
| Obsidian with plugins | Not open source and not shareable as a hosted view |
| Server app with a database | Hosting cost, sync problems, backups, a second source of truth |
| Adopt OpenSpec's artifact format as CraftRail's | OpenSpec is a change-orchestration workflow with its own lifecycle. CraftRail spans project-level intent (registers, ADRs, verification evidence) that OpenSpec does not model. Reading OpenSpec files through a source reader gives interoperability without either project changing its model. |
| One file per requirement or task | Machine-friendly, but too much churn for people |
| TOML front-matter with `tomllib` | GitHub and Zensical render YAML front-matter natively, not TOML. `tomllib` also forces Python 3.11+ on the core. |
| Patch engine in both Python and TypeScript | Two writers to keep in sync. Only reads are duplicated, and shared fixtures check them against each other. |
| AI calls inside Studio | Provider coupling, keys and cost. Copyable prompts give most of the value for free. |
| One combined feature | Mixes framework changes affecting every adopter with an optional app. Splitting lets the core land, be reviewed and be released on its own, and keeps the app from driving framework design. |

## Consequences

- **Positive:**
  - Git stays the only source of truth, and the forge provides history, review, permissions and audit.
  - Hosting costs $0, and local mode works offline.
  - `craftrail.json` is useful to agents, CI gates and external dashboards even without Studio.
  - Source readers open a path to interoperate with OpenSpec and Spec Kit rather than compete with them.
- **Negative / risks:**
  - Table parsing is less robust than a database. Mitigation: canonical headers, diagnostics, fixture round-trip tests.
  - Concurrent edits can collide. Mitigation: optimistic concurrency and a conflict view.
  - History mining needs full Git history. Mitigation: an incremental cache, and metrics marked `partial` on shallow clones.
  - A Node toolchain appears, isolated in `studio/`.
  - Metrics can be misread. Mitigation: every metric shows its definition, and coverage is labelled "linked coverage, not proof".
  - Scope pressure toward orchestration features. Mitigation: the explicit non-goal above.
- **Follow-ups (not in v1):** an OpenSpec source reader, a Spec Kit source reader, a GitHub Projects one-way mirror, GitLab/Gitea backends, and live collaboration.

## Supersedes / superseded by

None.
