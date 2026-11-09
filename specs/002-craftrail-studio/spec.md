# Feature 002: CraftRail Studio

- **Status:** proposed
- **Owner:** CraftRail maintainer
- **Created:** 2026-11-09
- **Updated:** 2026-11-09
- **Related issues/PRs:** proposal pull request `proposal/craftrail-studio`
- **Decision:** [ADR-001](../../docs/decisions/ADR-001-craftrail-studio-git-native-static-studio.md)
- **Depends on:** [Feature 001: Machine-readable conventions and graph export](../001-machine-readable-conventions-and-graph-export/spec.md). Approval of this feature requires feature 001 to be at least `approved`; implementation starts after feature 001 is `verified`.

## Context and problem

Feature 001 makes CraftRail project state available as `craftrail.json`. People still need to *see* and *change* that state without reading every file: what is in progress, what is blocked, which requirements lack evidence, how long work takes, and what changed this week. Without such a view, teams reach for Jira or Trello and create a second source of truth.

Studio is an optional, static web view and editor over the repository. It does not author or orchestrate changes. That is the job of OpenSpec, Spec Kit or a person with an agent ([ADR-001](../../docs/decisions/ADR-001-craftrail-studio-git-native-static-studio.md), "Relationship to OpenSpec and GitHub Spec Kit").

## Goals and measurable outcomes

- One page shows project state: boards, gaps, metrics and history. Signal: every view renders the fixture repository correctly in the e2e suite.
- Form edits produce minimal Git diffs. Signal: round-trip fixtures show only intended lines change.
- Studio costs $0 to run: static hosting, offline local mode, no AI calls. Signal: the build contains no server code, and a network-blocked e2e run passes.
- Traceability gaps are visible. Signal: every gap category in `FR-019` is highlighted on fixtures.

## Actors and scenarios

- **Maintainer / tech lead:** reviews the board weekly, spots blocked tasks and uncovered requirements, and approves a spec through a pull request opened from Studio.
- **Contributor:** drags a task to `in-progress`, fills in verification evidence after running tests, and saves. Studio writes the files, and the contributor commits.
- **Coding agent user:** copies a scoped prompt from an item into any agent.
- **Stakeholder:** opens the hosted read-only Studio to check progress.

## Scope and non-goals

- In scope: the static app in `studio/` (overview, boards, traceability graph and matrix, item detail, metrics, decisions, search and URL state); editing through `local` and `github` backends; the change queue; conflict handling; the approval guard; copyable prompts; the hosting workflow template; docs.
- Non-goals (v1):
  - workflow commands, change lifecycles, agent execution or "run" buttons (`CON-006`);
  - AI model calls;
  - a database or application server;
  - live co-editing;
  - comment threads (use PR reviews);
  - time tracking and notifications;
  - GitLab/Gitea backends and a GitHub Projects mirror;
  - authentication for the hosted read-only view (use the host's access control).

## Requirements

### Views

- `FR-018`: **Overview** MUST show:
  - item counts by type and status;
  - linked-coverage figures;
  - gap counts by category;
  - items blocked longer than the configured threshold;
  - the 20 most recent events;
  - data freshness (commit, time, dirty flag).
- `FR-019`: **Traceability** MUST provide a graph view and a matrix view of requirement → acceptance criterion → task → test → evidence. Both MUST highlight these gap categories:
  - `requirement-without-ac`;
  - `ac-without-task`;
  - `ac-without-verification`;
  - `task-without-requirement`;
  - `verification-without-evidence`;
  - `verified-without-evidence`;
  - `adr-proposed-stale`;
  - `dangling-reference`.

  Above 5,000 nodes, the graph MUST cluster by feature by default.
- `FR-020`: **Boards** MUST show Kanban columns per item type (tasks by default; also features, requirements, verification and ADRs). Columns come from `config.board_columns` or the default status order. Boards MUST filter by feature, owner, tag, type, source and text, and MUST support swimlanes by feature or owner.
- `FR-021`: **Item detail** MUST show:
  - metadata;
  - a sanitised Markdown excerpt;
  - incoming and outgoing links;
  - the source location (a forge link from `forge_url_template`, or a local path);
  - a history timeline from events.
- `FR-022`: **Metrics** MUST chart burn-up, cumulative flow, cycle-time distribution, lead time, weekly throughput, WIP and ageing. Each chart MUST show the metric definition from the export, the `partial` state, and a data-table alternative.
- `FR-023`: **Decisions** MUST list ADRs with status, date and owner, and MUST draw supersession chains.
- `FR-024`: Global search MUST match keys, titles and excerpts. The view, filters and selected item MUST be encoded in the URL (hash routing) so a view can be shared by link.

### Editing

- `FR-025`: Studio MUST support these typed edit operations through one TypeScript patch engine, each producing a minimal text diff:
  - `set_status`;
  - `set_field` (owner, title, and table cells under known headers);
  - `set_frontmatter`;
  - `create_item` (next free key);
  - `create_feature` (output equivalent to `new_feature.py`);
  - `create_adr` (from `templates/adr.md`);
  - `add_link` (append an ID to the relevant cell).

  Untargeted lines MUST remain byte-identical, including line endings and the trailing newline.
- `FR-026`: The **local backend** MUST be served by `python3 scripts/studio_server.py [--port N] [--app-dir PATH] [--open]`. The server uses only the standard library, binds to `127.0.0.1`, and serves the static app plus the API in the [plan](plan.md#local-server-api). It MUST NOT run Git commands that change repository state.
- `FR-027`: The **GitHub backend** MUST authenticate with a user-supplied fine-grained personal access token. The token is held in memory by default, and in `sessionStorage` only if the user opts in. It needs `contents:write` and `pull_requests:write` on one repository. The backend MUST write all queued changes as one commit on a new branch (`studio/<YYYYMMDD>-<slug>`) through the Git Data API, then open a pull request.
- `FR-028`: Studio MUST keep a **change queue** listing pending edits with unified diff previews. The user can remove individual edits and save them together.
- `FR-029`: Saving MUST use optimistic concurrency: a content hash locally, the blob SHA on GitHub. On mismatch, Studio MUST show a conflict view and MUST never overwrite silently.
- `FR-030`: Before saving, Studio MUST validate edits against feature 001's JSON Schemas and against local graph rules (status vocabulary, existing link targets, unique keys). Errors block the save, and warnings are shown.

### Agent support and hosting

- `FR-031`: Item detail MUST offer **Copy prompt** for these prompts in [workflow prompts](../../docs/framework/workflow-prompts.md):
  - review a specification;
  - produce a technical plan;
  - decompose into tasks;
  - implement approved work;
  - verify against acceptance criteria.

  The copied text is the context pack (feature 001's algorithm, reimplemented in TypeScript) followed by the prompt. The TypeScript output MUST equal `context_pack.py` output on shared fixtures. Studio MUST NOT call any AI service.
- `FR-032`: The repository MUST include an optional workflow template, `.github/workflows/studio.yml`, that:
  1. checks out full history;
  2. runs `export_graph.py`;
  3. builds `studio/`;
  4. publishes a static artifact (app + `craftrail.json`).

  GitHub Pages deployment is the default and can be swapped for any static host. The app MUST work from any base path.
- `FR-033`: Items whose `source` is not `craftrail` (from future readers) MUST display their source and MUST be read-only unless a patch engine for that source exists.

## Non-functional requirements

- `NFR-004`: The initial JavaScript + CSS payload MUST be at most 350 KB gzip. The traceability graph MUST stay interactive with 1,000 nodes, measured as at least 30 fps while panning in a recorded manual check on a mid-range laptop.
- `NFR-005`: Studio MUST meet WCAG 2.2 AA: axe reports zero serious or critical violations on every view, every drag action has a keyboard equivalent, and colour is never the only signal.
- `NFR-006`: Studio MUST work offline in local mode. It loads no CDN assets or remote fonts and sends no telemetry.
- `NFR-007`: The hosted build MUST ship a Content-Security-Policy meta tag restricting scripts to self and network access to self plus `api.github.com`.
- `NFR-008`: `studio/src` MUST have at least 85% line+branch coverage, and the patch engine 100% branch coverage. New Python code (`studio_server.py`) MUST have at least 90%.
- `NFR-009`: Studio MUST support the latest two versions of Chrome, Firefox, Safari and Edge.

## Business rules

- `BR-004`: Setting a feature to `approved` or an ADR to `accepted` MUST require a confirmation step in which the user types the target key. The change MUST record `approved_by` and `approved_on`. In GitHub mode it MUST go through a pull request. No bulk approval is allowed.
- `BR-005`: Edits MUST only touch files matching `config.artifact_globs` and not matching `config.exempt_globs`. Templates, generated output and source code are out of reach.
- `BR-006`: Every coverage figure in the UI MUST be labelled "linked coverage" and show its definition.

## Constraints

- `CON-004`: Read-only hosting MUST need only static file serving.
- `CON-005`: `studio/` dependencies MUST use OSI-approved licences compatible with the repository licence and MUST be pinned by a lockfile. The Node toolchain stays inside `studio/`.
- `CON-006`: Studio MUST NOT add workflow commands, change lifecycles, agent execution, or AI calls ([ADR-001](../../docs/decisions/ADR-001-craftrail-studio-git-native-static-studio.md)).

## Acceptance criteria

Views (Playwright e2e against the fixture repository through the local server)

- `AC-001`: Given the fixture, when Overview opens, then counts, gap totals, blocked items and recent events equal those in the golden export. (`FR-018`)
- `AC-002`: Given a fixture with one example of every gap category, when Traceability opens in graph and matrix mode, then each gap is highlighted and listed by category. Given the 6,000-node perf fixture, then the graph opens clustered by feature. (`FR-019`)
- `AC-003`: Given the tasks board, when filtered by feature `002` and owner `qa`, then only matching cards show, and reloading the URL reproduces the same view. Given a config that remaps task columns, then the columns follow it. (`FR-020`, `FR-024`)
- `AC-004`: Given an item with links and history, when its detail opens, then links, source location and the event timeline are shown. (`FR-021`)
- `AC-005`: Given the metrics fixture, when Metrics opens, then each chart shows its definition and values equal to feature 001's `expected-metrics.json`, each has a data table, and in shallow mode a "partial data" notice appears. Every coverage figure carries the "linked coverage" label. (`FR-022`, `BR-006`)
- `AC-006`: Given ADR-003 superseded by ADR-007, when Decisions opens, then the chain is drawn and statuses are shown. (`FR-023`)

Editing

- `AC-007`: For every operation in `FR-025`, given its fixture file, when the patch is applied, then the result equals the expected file byte for byte. Feature 001's exporter on the result shows exactly the intended change. CRLF fixtures keep CRLF. (`FR-025`)
- `AC-008`: Given the local server is running, when a request comes from a non-loopback address, without the token, with a foreign `Origin`, or for a path outside the globs (including `../` traversal and symlinks), then it gets 403. A valid `PUT` writes the file, and Git shows it as unstaged. (`FR-026`, `BR-005`)
- `AC-009`: Given a mocked GitHub API (MSW), when three edits in two files are saved, then exactly one commit containing both files is created on a `studio/` branch and one pull request is opened. The token never appears in URLs, logs or `localStorage`. (`FR-027`, `FR-028`)
- `AC-010`: Given a file changed on disk (local) or on the branch (GitHub) after loading, when the user saves, then a conflict view appears and nothing is written until the user re-applies or discards. (`FR-029`)
- `AC-011`: Given an edit with an unknown status or a link to a non-existent key, when the user saves, then saving is blocked with an explanation. (`FR-030`)
- `AC-012`: Given a draft feature, when the user sets it to `approved`, then a dialog requires typing the key and records the approver and date. In GitHub mode only a pull request is possible. No multi-select approve control exists. (`BR-004`)

Agent support, hosting, quality

- `AC-013`: Given item detail, when **Copy prompt → Implement approved work** is clicked, then the clipboard holds the context pack plus the prompt, equal to `context_pack.py` output for the same item. The network log shows no request beyond the app origin. (`FR-031`, `NFR-006`)
- `AC-014`: Given the workflow template in a scratch repository, when it runs, then the artifact contains `index.html`, assets and `craftrail.json`. Served under `/repo-name/`, the app loads with no 404s, and the built `index.html` contains the CSP meta tag. (`FR-032`, `CON-004`, `NFR-007`)
- `AC-015`: Given an export containing an item from a test-only reader, when it is shown, then its source badge is visible and editing controls are disabled. (`FR-033`)
- `AC-016`: Given CI, when the Studio jobs run, then:
  - Biome and `tsc --noEmit` pass;
  - coverage meets `NFR-008`;
  - the bundle check is at most 350 KB gzip;
  - axe reports no serious or critical violations;
  - a keyboard-only journey passes;
  - Playwright passes on Chromium, Firefox and WebKit.

  (`NFR-004`, `NFR-005`, `NFR-008`, `NFR-009`)

## Edge cases and failure paths

- Items marked `frozen` by the exporter (merge conflicts, parse errors) are shown read-only with the reason.
- Duplicate feature numbers: both are shown, and editing is disabled for them.
- A GitHub token lacking scopes produces a clear permission error listing the required scopes. Nothing is retried in a loop.
- Secondary rate limit: show the retry-after time; no automatic retry loop.
- Branch name already exists: add a numeric suffix.
- A partial GitHub save (ref created, PR failed): retry reuses the branch only if its head is the commit Studio created; otherwise it creates a new suffixed branch.
- The local server started outside a Git repository still serves and edits files; history is unavailable.
- An unknown graph `schema_version` major: refuse with a message. Newer minor: load with a warning.

## Data, dependencies, and interfaces

- Input: `craftrail.json` per feature 001's [graph schema](../001-machine-readable-conventions-and-graph-export/contracts/craftrail-graph.schema.json), loaded from the static file (hosted) or `GET /api/graph` (local).
- Validation: feature 001's [front-matter schema](../001-machine-readable-conventions-and-graph-export/contracts/craftrail-frontmatter.schema.json) and graph schema through Ajv.
- Edit format rules (front-matter grammar, canonical tables, status vocabularies): feature 001 spec, "Data, dependencies, and interfaces".
- Local server API and GitHub flow: [plan](plan.md).

## Security, privacy, accessibility, observability

- **Security:**
  - The local server uses a loopback bind and a random 32-byte token. The token is passed in the URL fragment, never the query string, and sent as the `X-CraftRail-Token` header.
  - The server checks `Host` and `Origin`, uses no CORS or cookies, and enforces a 2 MB request limit, symlink rejection and the glob allow-list.
  - Markdown is rendered with `markdown-it` (`html: false`) plus DOMPurify.
  - CSP per `NFR-007`. The GitHub token is never persisted by default and never logged.
- **Privacy:** no telemetry; no external requests except the chosen forge API.
- **Accessibility:** `NFR-005`. A "Move to…" menu replaces drag, and charts have data tables.
- **Observability:** a freshness banner and a diagnostics panel.

## Assumptions, questions, and risks

| Type | Item | Owner / resolution |
|---|---|---|
| Question | Ship the prebuilt app as a release asset (`craftrail-studio-<version>.zip`) so local mode needs no Node? Proposal: yes. | Maintainer, before TASK-016 |
| Assumption | GitHub is the first forge; others follow through the backend interface. | Maintainer |
| Risk | Scope pressure toward orchestration features. Mitigation: `CON-006` and the ADR non-goal. | Maintainer |
| Risk | Concurrent edits from agents and people. Mitigation: optimistic concurrency and the conflict view. | Maintainer |

## Traceability

- Decision: [ADR-001](../../docs/decisions/ADR-001-craftrail-studio-git-native-static-studio.md)
- Depends on: [Feature 001](../001-machine-readable-conventions-and-graph-export/spec.md)
- Plan: [plan.md](plan.md) · Tasks: [tasks.md](tasks.md) · Verification: [verification.md](verification.md)
