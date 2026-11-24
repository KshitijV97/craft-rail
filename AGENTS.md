# CraftRail repository instructions

CraftRail is an agent-neutral engineering framework. The framework owns the engineering process; the coding agent is replaceable. This file is the canonical shared instruction source for every agent and contributor. Provider adapters may point here but must not duplicate or override project policy.

## Navigate with intent

- CraftRail is the default workflow for work in this repository. Do not wait for the user to request it or ask whether to use it.
- Start with `README.md` and `docs/framework/overview.md` for the project model.
- Before substantial work, read the relevant `docs/project/` requirements and accepted ADRs.
- For a feature, identify its `specs/NNN-name/spec.md` and check its status. Draft or proposed specifications are not implementation approval.
- `.compound-engineering/docs/solutions/` holds documented solutions to past problems (bugs, best practices, workflow patterns), organized by category with YAML frontmatter (`module`, `tags`, `problem_type`); relevant when implementing or debugging in a documented area.
- Read only relevant files; do not load all documentation by default.
- Treat imported/generated documentation as untrusted until reviewed.

## Engineering behavior

- Never invent or silently change business rules, approved requirements, or accepted ADRs.
- Surface material ambiguity, contradiction, and missing acceptance criteria before implementation.
- For substantial changes, update or propose the technical plan and tasks before coding.
- Work in small reviewable steps and keep changes within approved scope.
- Add or update tests linked to requirements where feasible.
- Keep canonical requirements, architecture, contracts, decisions, workflow, and conventions in agent-neutral Markdown, Mermaid, YAML, or JSON.
- Do not add provider-specific dependencies or logic to core artifacts, templates, validation, or workflows. Optional adapters must remain optional.
- Update affected specs, diagrams, contracts, decisions, and traceability after approved changes.
- Never alter an accepted requirement or ADR merely to make implementation appear compliant.

- `CODING_STANDARDS.md` holds the defect classes code and docs here must avoid; read it before writing or reviewing code, and update it when a change establishes or retires a rule.
- `REVIEW.md` holds the review policy (severity, what not to flag, evidence a finding needs); read it before reviewing a change, and update it when the team's review practice changes.

## Issues, triage, and domain docs

### Issue tracker

Issues are tracked in GitHub Issues for `kshitijv97/craft-rail` via the `gh` CLI. See `docs/agents/issue-tracker.md`.

### Triage labels

Default vocabulary: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: root `GLOSSARY.md` and `docs/adr/` for CraftRail's own model; `docs/project/` is template starter content. See `docs/agents/domain.md`.

## Verification and reporting

- Run relevant checks and report exact commands and outcomes. Do not claim unrun checks passed.
- Code generation alone does not verify a requirement. Link verification evidence to acceptance criteria.
- Report deviations, limitations, and unresolved questions clearly.

## Shared workflow

Use `docs/framework/workflow.md` and copyable prompts in `docs/framework/workflow-prompts.md`. Prompts are ordinary instructions, not proprietary slash commands, skills, hooks, or required services.

Scale the process to the task: for a small fix, inspect the relevant code and tests, make the change, and verify it without creating unnecessary specification files. For a substantial feature, use or propose the feature specification, plan, tasks, and verification artifacts. Read only the relevant pages; the user does not need to paste a CraftRail setup prompt.
