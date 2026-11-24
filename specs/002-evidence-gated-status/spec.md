# Feature 002: Evidence-gated status (`craftrail status`)

- **Status:** proposed
- **Owner:** CraftRail project owner
- **Created:** 2026-11-24
- **Updated:** 2026-11-24
- **Related issues/PRs:** [#5](https://github.com/KshitijV97/craft-rail/pull/5) (product direction and ADR-002 to ADR-014)

This is the product requirements document for CraftRail's first version. The product-level direction is in [`docs/direction/vision.md`](../../docs/direction/vision.md); the decisions it rests on are ADR-002 to ADR-014 in [`docs/adr/`](../../docs/adr/README.md). Feature number 001 belongs to local knowledge retrieval ([#6](https://github.com/KshitijV97/craft-rail/pull/6)).

## Context and problem

Coding agents in a software factory report their own work as done. CI reports whether the suite passed, not which acceptance criteria have fresh evidence from a check of the right level. Today CraftRail's `verification.md` files carry a hand-typed status column, so any party, including the agent being judged, can mark a criterion verified. Feature 001's criteria are all still `planned` while its code exists, and nothing in CI notices.

## Goals and measurable outcomes

- An agent or CI job can learn, with one command, which acceptance criteria are not satisfied at the current commit and why.
- Status is computed from accepted links, fresh evidence, and waivers, never typed in (ADR-003).
- Dogfooding on CraftRail's own repository, measured against the current state (Compound Engineering, test-driven development, and CI without CraftRail), counts:
  - criteria found with no evidence;
  - criteria whose only evidence was a check below the required level;
  - false "done" claims caught (a `verification.md` row marked `verified` or `implemented` whose computed status is not `verified`).

## Actors and scenarios

- `US-001`: As a coding agent in a verification loop, I want each unsatisfied criterion with a reason code so I can fix the code, write the missing check, or propose a link.
- `US-002`: As a CI job, I want an exit code so I can gate a merge on every criterion being verified or waived.
- `US-003`: As a reviewer, I want pull requests that change links or waivers flagged so I review only the changes that alter what counts as evidence.
- `US-004`: As a project maintainer, I want the same inputs to produce the same status on any machine.

## Scope and non-goals

- In scope: reading criteria, links, and waivers from spec files; reading JUnit XML; computing status; text and JSON output; exit codes; detecting acceptance changes against a base ref; one agent-neutral skill that runs the command and acts on its output; dogfooding on this repository's CI.
- Non-goals: change-impact analysis or selective re-verification; running checks; architecture or contract rules of its own; result formats other than JUnit XML; manual check records; any planning, test-driven development, or review workflow; a dashboard; writing to the repository; blocking merges itself.

## Requirements

- `FR-001` The CLI MUST read acceptance criteria, each with its required verification level, from spec files under `specs/NNN-name/`.
- `FR-002` The CLI MUST read verification links and waivers from those spec files. A link names one criterion, one check by the identifier the runner reports (JUnit `classname` and `name`), and the check's verification level. A waiver names one criterion, an approver, a reason, and a scope.
- `FR-003` The CLI MUST read one or more JUnit XML reports and stamp every result with the commit observed from git at run time and the environment it was given. It MUST NOT take the commit from the report.
- `FR-004` The CLI MUST compute one status per criterion (`unlinked`, `pending`, `failing`, `verified`, `waived`) using the rules in ADR-004 and ADR-009, with exactly one reason code from `no-link`, `no-evidence`, `stale`, `skipped`, `failed`, `below-level`, `check-not-found`.
- `FR-005` Given a base ref, the CLI MUST count as accepted only links and waivers present at the merge base, treat branch-only ones as proposed, and report any added, changed, or removed link or waiver as acceptance changes present (ADR-014).
- `FR-006` The CLI MUST print a human-readable report by default and the versioned JSON contract with `--format json` (ADR-013).
- `FR-007` The CLI MUST exit `2` for invalid input or configuration, otherwise `1` if any criterion is not verified or waived, otherwise `3` if acceptance changes are present, otherwise `0`.
- `FR-008` CraftRail MUST ship one agent-neutral skill that runs `craftrail status`, reads the reasons, writes criteria into spec files, and proposes links, without accepting links or granting waivers.
- `NFR-001` The core MUST use only the Python standard library and support Python 3.10 and later.
- `NFR-002` Given identical repository contents, reports, base ref, and environment, the JSON output MUST be byte-identical.
- `NFR-003` The CLI MUST NOT write to the repository or the network.
- `CON-001` Verification status is never stored in a file; any hand-typed status column is ignored by the computation.
- `CON-002` Nothing in the core depends on a specific coding agent, agent workflow, or code host.

## Business rules

- `BR-001` Only a human, through a merge to the protected branch, accepts a link or grants a waiver (ADR-003, ADR-006).
- `BR-002` A skipped result, a stale result, and a missing result are not evidence (ADR-004).
- `BR-003` A check that fails on any run at the commit is failing, even if a retry passes (ADR-004).
- `BR-004` Failing outranks waived (ADR-009).
- `BR-005` On the chain `unit` < `component` < `integration` < `acceptance`, a check at or above the required level counts; `contract`, `architecture`, and `non-functional` count only for a criterion requiring exactly that kind (ADR-009).

## Acceptance criteria

Each criterion declares the verification level required to verify it (ADR-007).

- `AC-001` (required level: `unit`) Given a criterion with no accepted link and no waiver, when status is computed, then it is `unlinked` with reason `no-link`.
- `AC-002` (required level: `unit`) Given an accepted link whose check has no result in the reports, or only a skipped result, when status is computed, then the criterion is `pending` with reason `no-evidence` or `skipped`.
- `AC-003` (required level: `integration`) Given a report produced at an earlier commit than `HEAD`, when status is computed in a real git repository, then the criterion is `pending` with reason `stale`, whatever commit the report claims.
- `AC-004` (required level: `unit`) Given an accepted link whose check failed on any run at the current commit, when status is computed, then the criterion is `failing` with reason `failed`, even if it is also waived or a retry passed.
- `AC-005` (required level: `unit`) Given a criterion requiring `integration` whose only accepted link is to a `unit` check, when status is computed, then that link does not count and the reason is `below-level`.
- `AC-006` (required level: `unit`) Given an accepted link to a check identifier that appears in no report, when status is computed, then the reason is `check-not-found`.
- `AC-007` (required level: `integration`) Given a branch that adds a link which is not on the base ref, when status is computed against that base, then the new link does not count and, if every criterion is otherwise verified or waived, the exit code is `3`.
- `AC-008` (required level: `acceptance`) Given CraftRail's own repository, when CI runs its tests with JUnit output and then `craftrail status --format json`, then the job's result follows the exit-code rules and the JSON lists every criterion of features 001 and 002.
- `AC-009` (required level: `unit`) Given the same inputs twice, when `--format json` runs, then the outputs are byte-identical.
- `AC-010` (required level: `integration`) Given a malformed spec file or unreadable report, when the CLI runs, then it exits `2` with a message naming the file, and writes nothing.
- `AC-011` (required level: `unit`) Given the core package imported in an environment with only the standard library, when `craftrail status` runs, then it needs no third-party package.

## Edge cases and failure paths

- A criterion ID defined twice is an input error (`2`), not a silent pick.
- A link to an unknown criterion ID is an input error.
- A waiver without an approver or reason is an input error.
- The same check reported in several files at one commit: any failure makes it failing.
- No reports given: every linked criterion is `pending` with `no-evidence`.
- No spec files with criteria: exit `0` with an empty report, and say so.
- Not a git repository, or a detached or shallow checkout where the merge base cannot be found: input error naming the cause.

## Data, dependencies, and interfaces

Inputs are spec files, JUnit XML reports, git, and command-line options. Output is text or JSON on stdout and an exit code. The syntax for criteria, links, and waivers inside spec files is decided in the technical plan; it must keep `spec.md` readable as prose, parse with the standard library, and let CODEOWNERS cover the files that hold links and waivers.

## Security, privacy, accessibility, observability

Reports and spec files are untrusted input: parse XML without resolving external entities, cap input sizes, and never execute content. The CLI runs read-only and offline. Diagnostics go to stderr so stdout stays parseable.

## Assumptions, questions, and risks

| Type | Item | Owner / resolution |
|---|---|---|
| Open question | Syntax for criteria, required levels, links, and waivers in spec files, and how it relates to the existing `verification.md` table. | Decide in `plan.md` before implementation. |
| Open question | Whether the hand-typed status column in `verification.md` is removed or kept as a planning note that the computation ignores. | Decide in `plan.md`. |
| Decision (ADR-014) | Exit code `1` outranks `3`, so an agent keeps working before a human is asked to review acceptance changes. | Accepted; revisit after dogfooding. |
| Risk | The standard-library XML parser is not hardened against every malicious input. | Reject DTDs and entity declarations; reports come from the project's own CI. |
| Risk | Renaming a test breaks its link. | `check-not-found` surfaces it on the next run. |
| Assumption | Dogfooding on this repository is enough to judge the first version; an external project comes later. | Owner decision, 2026-11-24. |

## Traceability

`FR-001` → `AC-001`, `AC-010`; `FR-002` → `AC-001`, `AC-005`, `AC-006`, `AC-010`; `FR-003` → `AC-003`; `FR-004` → `AC-001` to `AC-006`; `FR-005` → `AC-007`; `FR-006` → `AC-008`, `AC-009`; `FR-007` → `AC-007`, `AC-008`, `AC-010`; `FR-008` → no criterion yet (added with the skill's design in `plan.md`); `NFR-001` → `AC-011`; `NFR-002` → `AC-009`; `NFR-003` → `AC-010`; `CON-001` → `AC-008`; `CON-002` → `AC-011`.
