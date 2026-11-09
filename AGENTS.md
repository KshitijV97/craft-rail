# CraftRail repository instructions

CraftRail is an agent-neutral engineering framework. The framework owns the engineering process; the coding agent is replaceable. This file is the canonical shared instruction source for every agent and contributor. Provider adapters may point here but must not duplicate or override project policy.

## Navigate with intent

- Start with `README.md` and `docs/framework/overview.md` for the project model.
- Before substantial work, read the relevant `docs/project/` requirements and accepted ADRs.
- For a feature, identify its `specs/NNN-name/spec.md` and check its status. Draft or proposed specifications are not implementation approval.
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

## Verification and reporting

- Run relevant checks and report exact commands and outcomes. Do not claim unrun checks passed.
- Code generation alone does not verify a requirement. Link verification evidence to acceptance criteria.
- Report deviations, limitations, and unresolved questions clearly.

## Shared workflow

Use `docs/framework/workflow.md` and copyable prompts in `docs/framework/workflow-prompts.md`. Prompts are ordinary instructions, not proprietary slash commands, skills, hooks, or required services.
