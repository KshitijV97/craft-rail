# CraftRail

**Guardrails for agent-driven development.**

CraftRail is a Git-native, agent-neutral framework for keeping engineering intent, architecture, and verification aligned across human and AI-assisted development. It gives a project a shared place for requirements, decisions, contracts, feature plans, and evidence without requiring a hosted service or a particular coding agent.

> The framework owns the engineering process. The coding agent is replaceable.

## Why use it

Coding agents can work from a repository, but chat context is temporary. CraftRail keeps product intent and engineering constraints reviewable beside code, then connects requirements to acceptance criteria, tasks, and verification evidence. It is designed for individual engineers, technical leads, staff/principal engineers, and small teams.

CraftRail provides reusable project structure and templates, stable requirement IDs, architecture and ADR conventions, agent-neutral workflow prompts, and a Python standard-library validator. It does not guarantee agent correctness, replace tests or review, prescribe a language or architecture, or require a particular delivery methodology.

## Product philosophy

- Human intent before generated code.
- Specifications before implementation.
- Architecture before uncontrolled complexity.
- Verification before declaring completion.
- Documentation that evolves with the code.

## The three layers

| Layer | Owns | Canonical formats |
|---|---|---|
| Core | Requirements, architecture, decisions, contracts, traceability, validation | Markdown, Mermaid, YAML, JSON |
| Workflow | Discover, Specify, Clarify, Plan, Tasks, Analyze, Implement, Verify, Converge | Markdown guidance and prompts |
| Adapters | Agent-specific instruction discovery and optional integrations | Minimal pointers/configuration only |

`AGENTS.md` is the shared canonical instruction file and makes CraftRail the default workflow in this repository. Claude Code automatically loads the minimal root `CLAUDE.md` adapter, which imports `AGENTS.md`; OpenCode reads `AGENTS.md` directly and does not use `CLAUDE.md` as a fallback. A developer using the GitHub template can open the project in any supported agent and describe the task normally, without a setup prompt or plugin. No core artifact or tool requires an AI provider. See the [compatibility matrix](docs/framework/agent-compatibility.md).

## Workflow

```mermaid
flowchart LR
  D[Discover] --> S[Specify] --> C[Clarify] --> P[Plan] --> T[Tasks]
  T --> A[Analyze] --> I[Implement] --> V[Verify] --> K[Converge]
```

These are quality gates, not nine required meetings. Combine or skip steps for low-risk changes when intent remains clear; use the full path for high-impact work.

## Quickstart: start a project

Create a new project from the enabled [CraftRail GitHub template](https://github.com/kshitijv97/craft-rail) using **Use this template** → **Create a new repository**, or clone it locally. Replace the illustrative project files in `docs/project/`, review the engineering principles, add project requirements and architecture, and retain or adapt `AGENTS.md`. See [GitHub template usage](docs/framework/github-template-usage.md).

Create a feature and validate locally:

```bash
python3 scripts/new_feature.py "User authentication"
python3 scripts/validate_docs.py
```

See the [validation guide](docs/framework/validation.md) for what the checks cover and where their limits are.

The initializer creates the next numbered folder under `specs/` from the feature templates. Mark the specification approved through your team's review process before implementation.

## Adopt into an existing project

Copy only the conventions you need. First add the canonical `AGENTS.md`, then selectively adopt project requirements, architecture/ADR records, feature specs, templates, and validator. Keep existing authoritative documentation and link to it; do not create competing sources of truth. See [incremental adoption](docs/framework/adoption-existing-project.md).

## Repository map

```text
AGENTS.md, CLAUDE.md       Shared instructions and minimal adapter
docs/adoption/             Guides for using CraftRail in your own project
docs/implementation/       Technical implementation of CraftRail itself
docs/framework/            Detailed guides linked by both documentation parts
docs/project/              Starter brief, requirements, architecture, and contracts
specs/                     Feature-specific specs, plans, tasks, verification
templates/                 Reusable blank artifacts
scripts/                   Feature initializer and documentation validator
tests/                     Standard-library tests
```

See [the repository structure guide](docs/framework/repository-structure.md) in the adoption docs.

## Formats and integrations

Markdown is the canonical prose format because it is readable, diffable, and supported by common repository tools. Mermaid keeps diagrams editable as text. YAML is used for OpenAPI starter contracts and GitHub issue forms; JSON Schema covers structured data. Provider-specific skills, commands, hooks, and configuration can be layered on later, but are never needed for core use.

CraftRail can coexist with [GitHub Spec Kit](https://github.com/github/spec-kit) or [OpenSpec](https://openspec.dev/): choose one canonical home for each artifact and link across systems rather than maintaining conflicting copies. The [ecosystem comparison](docs/framework/ecosystem-comparison.md) describes the tradeoffs and was reviewed 2026-11-08.

## Website and documentation

Visit the [CraftRail website](https://craft-rail-docs.vercel.app) for a product overview and a clear starting point. The site keeps the detailed resources in separate sections:

1. [Docs for adoption](https://craft-rail-docs.vercel.app/adoption/) — start a project from the template, adopt CraftRail into an existing repository, and use its engineering workflow.
2. [Technical implementation of CraftRail](https://craft-rail-docs.vercel.app/implementation/) — understand how this repository's architecture, Python tools, quality pipeline, releases, and docs site work.

The hosted site may ask for Vercel authentication. Its Markdown source and linked guides are available in [`docs/`](docs/).

## Demo walkthrough

The illustrative [account recovery feature](specs/000-example-feature/spec.md) starts with `FR-001` and two acceptance criteria. Its [plan](specs/000-example-feature/plan.md) includes a sequence view and operational considerations; [tasks](specs/000-example-feature/tasks.md) reference the spec; [verification](specs/000-example-feature/verification.md) maps criteria to tests and evidence. Read the [walkthrough](docs/examples/sample-feature-walkthrough.md) for the end-to-end path. The sample is not a production security design.

## License

See [LICENSE](LICENSE) for the license terms.
