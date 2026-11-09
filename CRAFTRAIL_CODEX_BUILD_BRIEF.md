# CraftRail — Codex Build Brief

> **Purpose:** Build CraftRail, a polished, reusable, open-source framework that provides practical guardrails for agent-driven software development. CraftRail keeps product intent, functional requirements, technical architecture, decisions, contracts, tasks, and verification in a version-controlled repository that both humans and coding agents can understand and maintain.
>
> **Project name selected by the owner:** CraftRail.
> **Suggested repository name:** `craft-rail` (confirmed by owner on 2026-11-08).
> **Tagline:** Guardrails for agent-driven development.
> **Naming caveat:** A preliminary web search found an existing Japanese company, Craftrail Inc. (株式会社クラフトレイル), using the same name at https://craftrail.co.jp/ and offering HR / organizational services that include AI-related offerings. This is a material brand-confusion risk. Use CraftRail as the owner-selected working project name during implementation, but explicitly document this conflict and require owner review before public branding, domain purchases, or promotion. Do not claim trademark, GitHub handle, or domain clearance.
>
> **Primary outcome:** A public GitHub repository that engineers can use as a starter template for new software projects or adopt incrementally into existing repositories. It should be immediately useful to individual engineers and sufficiently documented, tested, and maintainable for engineering teams to evaluate and adopt.

---

# Instructions to Codex

## Start here

The owner has chosen the name **CraftRail** and the tagline **Guardrails for agent-driven development**. Do not ask the owner to choose a name. The repository slug is `craft-rail` in the `kshitijv97` namespace.

Create a complete first version of the CraftRail project in the current workspace. If the workspace is empty, initialize the project files directly at its root. If it is not empty, inspect it and preserve existing work; do not blindly overwrite files. The intended result is a repository that can be reviewed locally and then published by the owner as a public GitHub project.

The project should feel like a credible open-source developer tool, not a personal notes folder or a prompt dump. Prioritize working conventions, good examples, lightweight validation, onboarding, and clear boundaries. Do not create a website, logo, hosted service, or complex CLI before the repository template and validation workflow are genuinely useful.


Act as a staff-level software architect, developer-experience engineer, technical writer, and open-source maintainer. Build the first usable version of this framework in the current workspace.

**Do not respond with only a plan or recommendations.** Inspect the workspace, make reasonable assumptions, create the actual files and tooling, run available checks, and leave the repository in a coherent working state.

## Execution rules

1. **Inspect before changing anything.** Determine whether the current directory is empty, an existing Git repository, or an existing project. Read its README, agent instructions, and relevant files before making changes.
2. **Preserve existing work.** Do not delete, overwrite, or reorganize unrelated project files. If this is an existing project, implement the framework in an isolated directory or document a safe integration path.
3. **Work autonomously.** Do not stop for reversible decisions. Record assumptions in `docs/framework/assumptions-and-decisions.md`. Flag decisions that require owner approval, especially license selection and publication. The project name and tagline are owner-selected; do not reopen that decision.
4. **Build, don't merely describe.** Create the docs, templates, sample artifacts, scripts, tests, CI workflow, and GitHub community files below.
5. **Keep the framework agent-neutral.** Markdown is the canonical source of truth. Include compatibility guidance for Codex, Claude Code, and OpenCode without depending on one vendor or model.
6. **Keep dependencies minimal.** Prefer Markdown, Mermaid, YAML, JSON Schema, and Python's standard library. Do not introduce a runtime framework, database, hosted service, or mandatory JavaScript toolchain.
7. **Verify the result.** Run all local validation and tests that can run in this environment. Fix failures. Never claim a check passed unless it was actually run.
8. **Do not publish anything.** Do not create a remote repository, push commits, publish a package, release a version, or take external account actions. Prepare the repo for the owner to publish.
9. **Be transparent.** At the end, list created files, checks run and outcomes, limitations, and owner decisions still needed.

## Initial ecosystem investigation

Before implementation, inspect current official documentation and avoid rebuilding existing projects without a clear reason. At minimum review:

- GitHub Spec Kit: <https://github.com/github/spec-kit>
- OpenSpec: find and confirm its canonical current repository at <https://openspec.dev/>
- Codex `AGENTS.md` guidance: <https://developers.openai.com/codex/guides/agents-md/>
- Claude Code memory / `CLAUDE.md`: <https://docs.anthropic.com/en/docs/claude-code/memory>
- OpenCode agent instructions: <https://opencode.ai/docs/>

Treat these as ecosystem references and potential integrations, not competitors to imitate feature-for-feature. If URLs have moved, find canonical current docs and record the verified links. Document what this framework deliberately does and does not do.

---

# 1. Product vision and positioning

## 1.1 Problem

AI coding agents can generate code quickly, but many projects lack a durable, shared source of truth for:

- what the product should do and who it serves;
- business rules, functional and non-functional requirements;
- system boundaries, components, dependencies, and data flows;
- API and data contracts;
- why architectural decisions were made;
- how requirements are verified;
- what changed and what remains incomplete.

This knowledge is often trapped in chat history, oversized agent instruction files, disconnected diagrams, personal notes, or undocumented assumptions. This causes context loss, implementation drift, repeated discovery, and inconsistent agent decisions.

## 1.2 Solution

Create **CraftRail**, a repository-native engineering framework: an opinionated set of conventions, templates, examples, lightweight validation tools, and agent workflows that keeps engineering intent close to code and versioned in Git.

It should make a repository understandable to both a new engineer and a coding agent without requiring a proprietary platform or a specific AI provider.

## 1.3 Target users

1. Individual software engineers building with Codex, Claude Code, OpenCode, Cursor, or other coding agents.
2. Senior engineers and technical leads who need durable requirements, architecture decisions, and traceability.
3. Small engineering teams seeking lightweight standards without a heavyweight requirements-management platform.
4. Open-source maintainers who want contributors and agents to understand project intent and constraints.

## 1.4 Initial positioning

Use this as the starting point and improve it if ecosystem research supports a better version:

> CraftRail provides practical guardrails for agent-driven development by turning a Git repository into a durable source of truth for product intent, requirements, architecture, decisions, tasks, and verification.

Use the owner-selected tagline: **Guardrails for agent-driven development.** Supporting message: **Keep intent in the repo. Keep agents aligned.**

Do not market it as a replacement for engineering judgment, tests, code review, Spec Kit, OpenSpec, or requirements-management systems.

## 1.5 Product principles

- **Repository-first:** Git is the source of truth for approved engineering intent.
- **Markdown-first:** core artifacts are readable, editable, searchable, and diffable as plain text.
- **Agent-neutral:** no provider-specific format is required for canonical artifacts.
- **Human-governed:** agents may propose changes; humans approve material product and architecture decisions.
- **Traceable:** requirements connect to acceptance criteria and verification evidence.
- **Progressive disclosure:** keep root agent instructions short; link to deeper docs instead of loading everything into every agent context.
- **Small surface area:** make the default workflow useful before adding automation.
- **Maintainable:** documentation evolves with code rather than becoming a stale second implementation.
- **Accessible:** examples and quickstarts should help engineers new to formal requirements engineering.

## 1.6 Differentiation

Do not clone every feature of GitHub Spec Kit or OpenSpec. Build a coherent, opinionated starter standard with:

- an understandable project-level and feature-level repository layout;
- stable requirement IDs and practical requirement-to-test traceability;
- C4-inspired architecture documentation and Mermaid conventions;
- lightweight architecture decision records (ADRs);
- API and data contract conventions;
- compact instructions for multiple coding agents;
- a simple local/CI validator with minimal dependencies;
- high-quality templates and a complete worked example;
- guidance for greenfield projects and adoption into existing repositories.

If research shows an existing tool already solves a proposed feature well, document integration rather than duplicating it.

---

# 2. Scope

## 2.1 MVP: required

1. A polished README explaining the problem, benefits, quickstart, workflow, formats, and adoption paths.
2. A recommended repository structure separating framework documentation, project documentation, feature specs, templates, and tooling.
3. Reusable templates for:
   - product/project brief;
   - project constitution / engineering principles;
   - stakeholder/persona notes and glossary;
   - functional requirements;
   - non-functional requirements;
   - feature specification;
   - technical implementation plan;
   - task breakdown;
   - acceptance criteria and verification matrix;
   - architecture overview;
   - C4-style context/container/component views;
   - sequence, data-flow, and state diagrams;
   - ADR;
   - OpenAPI starter contract;
   - JSON Schema data contract;
   - change proposal.
4. Agent instructions for Codex, Claude Code, and OpenCode, with a shared canonical policy and minimal provider-specific adapters.
5. A documented lifecycle: Discover → Specify → Clarify → Plan → Tasks → Analyze → Implement → Verify → Converge.
6. A worked example feature demonstrating requirements, acceptance criteria, Mermaid diagrams, tasks, and test traceability. Mark it as illustrative.
7. Python standard-library tooling to initialize a feature and validate documentation.
8. Automated tests for the tooling.
9. GitHub Actions CI for validation on pushes and pull requests.
10. Open-source essentials: license file, contributing guide, code of conduct, security policy, issue templates, PR template, and support guidance.
11. Documentation for using the repo as a GitHub template and adopting its conventions in an existing project.

## 2.2 Explicitly out of scope for MVP

Do not build these unless the MVP is complete and they can be added without compromising simplicity:

- hosted web application or SaaS;
- database or cloud backend;
- graphical requirements or diagram editor;
- proprietary agent runtime or orchestration engine;
- automatic code generation from every requirement;
- automatic approval of requirements or architecture changes;
- complex plugin marketplace;
- mandatory package installation or large dependency tree;
- full clone of Spec Kit, OpenSpec, BMAD, or another established framework.

The first release is a useful repository template and lightweight toolkit, not a platform.

---

# 3. Recommended repository structure

Implement and document a clean structure. Adjust names only with a good reason, preserving the conceptual separation.

```text
craftrail/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── SUPPORT.md
├── CHANGELOG.md
├── AGENTS.md
├── CLAUDE.md
│
├── docs/
│   ├── framework/
│   │   ├── overview.md
│   │   ├── quickstart.md
│   │   ├── concepts.md
│   │   ├── repository-structure.md
│   │   ├── workflow.md
│   │   ├── requirements-writing-guide.md
│   │   ├── architecture-documentation-guide.md
│   │   ├── diagrams-guide.md
│   │   ├── adr-guide.md
│   │   ├── traceability-and-verification.md
│   │   ├── agent-compatibility.md
│   │   ├── adoption-existing-project.md
│   │   ├── github-template-usage.md
│   │   ├── ecosystem-comparison.md
│   │   ├── assumptions-and-decisions.md
│   │   ├── brand-and-positioning.md
│   │   └── faq.md
│   │
│   ├── project/                  # Starter files customized by adopting projects
│   │   ├── product-brief.md
│   │   ├── engineering-principles.md
│   │   ├── stakeholders.md
│   │   ├── glossary.md
│   │   ├── requirements/
│   │   │   ├── functional-requirements.md
│   │   │   ├── non-functional-requirements.md
│   │   │   └── business-rules.md
│   │   ├── architecture/
│   │   │   ├── overview.md
│   │   │   ├── system-context.md
│   │   │   ├── containers.md
│   │   │   ├── components.md
│   │   │   ├── data-flow.md
│   │   │   └── security-and-trust-boundaries.md
│   │   ├── decisions/README.md
│   │   └── contracts/
│   │       ├── README.md
│   │       ├── openapi.yaml
│   │       └── schemas/example.schema.json
│   │
│   ├── examples/sample-feature-walkthrough.md
│   └──
│
├── specs/
│   ├── README.md
│   └── 000-example-feature/       # Clearly illustrative
│       ├── spec.md
│       ├── plan.md
│       ├── tasks.md
│       ├── verification.md
│       └── diagrams/sequence.mmd
│
├── templates/
│   ├── feature/
│   │   ├── spec.md
│   │   ├── plan.md
│   │   ├── tasks.md
│   │   ├── verification.md
│   │   └── diagrams/sequence.mmd
│   ├── adr.md
│   ├── change-proposal.md
│   ├── product-brief.md
│   ├── functional-requirements.md
│   ├── non-functional-requirements.md
│   └── architecture-overview.md
│
├── scripts/
│   ├── new_feature.py
│   └── validate_docs.py
├── tests/test_scripts.py
└── .github/
    ├── workflows/validate-docs.yml
    ├── ISSUE_TEMPLATE/
    │   ├── bug_report.yml
    │   ├── feature_request.yml
    │   └── config.yml
    └── PULL_REQUEST_TEMPLATE.md
```

This is a target, not a reason to create empty files. Every committed file must have useful content or be omitted until needed. Avoid duplicate copies of canonical policies and templates.

`docs/framework/` explains the framework. `docs/project/` contains starter artifacts for an adopting project to customize. `specs/` holds feature-specific specifications. `templates/` contains reusable blank templates used by humans and helper scripts.

---

# 4. Canonical content standards

## 4.1 Project brief

Capture the problem statement, intended users/stakeholders, outcomes and measurable success signals, product boundaries and non-goals, operating environment and constraints, assumptions/risks/open questions, and links to requirements and architecture. Keep it concise; do not turn it into a marketing pitch or detailed implementation plan.

## 4.2 Requirements taxonomy

Define and distinguish:

- **Business requirement:** desired business outcome or policy.
- **Functional requirement:** observable system behaviour.
- **Non-functional requirement:** quality attribute or operational constraint, such as security, reliability, performance, accessibility, maintainability, or privacy.
- **Constraint:** boundary the solution must respect (regulatory, technical, organizational, budgetary, or platform).
- **Assumption:** something treated as true pending confirmation.
- **Acceptance criterion:** an evaluable condition used to decide whether a requirement or feature is satisfied.

Use stable IDs, for example:

- `BR-001` business requirement;
- `FR-001` functional requirement;
- `NFR-001` non-functional requirement;
- `CON-001` constraint;
- `US-001` user story;
- `AC-001` acceptance criterion;
- `ADR-001` architecture decision record;
- `TASK-001` optional task ID;
- `TEST-001` verification/test reference.

Requirements should be atomic where practical, unambiguous, testable (or explicitly marked for qualitative review), expressed as required behaviour rather than a preferred implementation, and linked to rationale/source/verification where appropriate.

Use normative language consistently: **MUST** = mandatory; **SHOULD** = strongly recommended with documented exceptions; **MAY** = optional. Do not assign IDs to every sentence. IDs should identify items needing stable reference, review, or traceability. Do not casually recycle IDs after deletion; mark retired requirements deprecated or superseded.

## 4.3 Feature specification

Include as relevant:

1. Metadata: feature ID, title, status, owner, dates, related issues/PRs.
2. Context and problem statement.
3. Goals and measurable outcomes.
4. Actors/personas and use cases.
5. Scope and explicit non-goals.
6. Functional requirements with stable IDs.
7. Non-functional requirements and constraints.
8. Business rules.
9. User stories or usage scenarios.
10. Acceptance criteria (Given/When/Then where useful).
11. Edge cases, failure paths, and abuse cases.
12. Data requirements and lifecycle.
13. External dependencies and integrations.
14. Security, privacy, accessibility, and observability considerations.
15. Assumptions, unresolved questions, and risks.
16. Traceability references.

Do not force irrelevant sections into trivial features. Mark optional sections clearly.

## 4.4 Technical plan

Describe the proposed solution and alternatives; impacted services/modules/components; interfaces and API changes; data model/migrations; sequence, data-flow, or state diagrams; security and trust boundaries; error handling, retries, idempotency, and consistency; observability and operations; rollout, compatibility, rollback, and migration strategy; test strategy; and open technical decisions.

The plan must not silently change approved feature scope. If it reveals a requirement problem, send it for clarification or an approved specification change.

## 4.5 Tasks

Tasks should be small enough to implement/review independently, ordered by dependency, tied to requirement/acceptance/plan references, explicit about expected output and verification, and categorized where useful (implementation, tests, docs, migration, operations). Prefer meaningful vertical slices over mechanical file-by-file task lists. Do not generate arbitrary task counts.

## 4.6 Verification and traceability

Provide a practical matrix linking:

`Requirement ID → Acceptance Criterion ID → Test/Verification ID → Evidence or location → Status`

Support automated tests, manual test cases, review evidence, and operational verification. Code generation alone does not verify a requirement. Define statuses such as `planned`, `implemented`, `verified`, `blocked`, `waived`, and `deprecated` and explain their use.

The validator should catch structural and ID errors, but must not claim to determine whether business requirements are semantically correct.

## 4.7 Architecture documentation

Use a layered approach rather than one giant block diagram:

- System context: users, external systems, and system boundary.
- Container view: deployable/runtime units and data stores.
- Component view: important internal modules and responsibilities.
- Sequence diagrams: time-ordered interactions.
- Data-flow diagrams: movement, transformation, and storage of data.
- State diagrams: lifecycle and state transitions.
- Deployment view: infrastructure and runtime topology where useful.

Use C4 concepts where useful, but do not require every project to create every view. State abstraction level, scope, and last-reviewed date near each diagram. Diagrams should explain boundaries and relationships, not merely decorate a document.

## 4.8 Mermaid conventions

- Keep Mermaid source in Markdown fences or `.mmd` files.
- Prefer text-based diagrams committed to Git.
- Give each diagram a title and short explanation.
- Use consistent names for services and actors across diagrams.
- Never use screenshots as the only source of truth.
- If diagrams.net is used for detailed visuals, commit the editable `.drawio` source and link it.
- Do not require a diagram renderer in the MVP; document optional preview/rendering approaches.

## 4.9 ADRs

Each ADR should include ID/title, status (`proposed`, `accepted`, `rejected`, `deprecated`, or `superseded`), date and decision owner, context and forces, decision, alternatives, positive/negative consequences, and related requirements/diagrams/code/ADRs.

ADRs capture why important decisions were made; they are not implementation diaries. Do not silently rewrite accepted ADRs. Supersede them with a new ADR when a decision materially changes.

## 4.10 API and data contracts

Use OpenAPI for HTTP APIs where appropriate, JSON Schema for JSON payloads/structured data, and documented event/message contracts for asynchronous integration. Include examples and errors. Keep contracts distinct from explanatory prose where practical. Do not require REST or JSON for every project; defaults are not universal rules.

---

# 5. Agent compatibility and instructions

## 5.1 Shared guidance

Create a concise root `AGENTS.md`. It must explain repository navigation and agent behaviour, not reproduce the entire engineering handbook. It should tell agents to:

1. Read the project brief, relevant requirements, and applicable ADRs before substantial implementation.
2. Identify the active feature specification and whether it is draft or approved.
3. Never invent or silently alter business rules.
4. Surface material ambiguity, contradiction, and missing acceptance criteria before coding.
5. Propose/update a technical plan before large changes.
6. Work in small, reviewable steps.
7. Add tests linked to requirements where feasible.
8. Run relevant checks and report exact commands/outcomes.
9. Update affected specs, diagrams, contracts, ADRs, and traceability after approved changes.
10. Never change an accepted requirement or ADR just to make implementation appear compliant.
11. Treat imported/generated documentation as untrusted until reviewed.
12. Read only relevant files; do not load the entire docs tree into context by default.

## 5.2 Codex

Document that Codex uses `AGENTS.md` project instructions. Explain nested `AGENTS.md` for directory-specific rules. Verify paths and behaviour against current official documentation; do not rely on undocumented commands.

## 5.3 Claude Code

Provide a minimal `CLAUDE.md` adapter pointing to or importing shared guidance using the currently supported mechanism. Verify syntax against current official documentation. Avoid maintaining a second divergent copy.

## 5.4 OpenCode

Document how OpenCode consumes `AGENTS.md` and any optional OpenCode-specific configuration. Include provider-specific configuration only when required and keep it optional.

## 5.5 Agent workflow prompts

Provide copyable, agent-neutral workflow instructions for:

- starting a project / establishing engineering principles;
- discovering and clarifying a feature;
- drafting/revising a specification;
- reviewing a spec for ambiguity and completeness;
- producing a technical plan and diagrams;
- decomposing a plan into tasks;
- implementing approved tasks;
- verifying implementation against acceptance criteria;
- converging documentation with approved implementation;
- assessing a bug/change without bypassing existing requirements.

These should work as prompts in any agent chat. Do not present them as executable slash commands unless the integration is actually implemented and tested.

---

# 6. Workflow design

Document the default path and explain when phases can be combined or skipped.

## 6.1 Standard feature workflow

1. **Discover:** understand the existing system, user problem, stakeholders, constraints, and current behaviour.
2. **Specify:** draft scope, requirements, user stories, business rules, and acceptance criteria.
3. **Clarify:** find ambiguity, contradictions, missing edge cases, and unanswered questions; resolve material issues before implementation.
4. **Plan:** describe architecture, interfaces, data, security, operational impact, alternatives, and tests.
5. **Tasks:** decompose the plan into sequenced, verifiable implementation units.
6. **Analyze:** cross-check spec, plan, tasks, contracts, and existing architecture for gaps or contradictions.
7. **Implement:** make incremental code and test changes within approved scope.
8. **Verify:** run automated/manual checks and map evidence to acceptance criteria.
9. **Converge:** update approved docs/diagrams to the shipped state; record deviations and unresolved work.

These are logical quality gates, not necessarily nine meetings or agent sessions. Small changes may use a lighter path; high-impact changes should use the full path.

## 6.2 Change control

Define handling for scope changes after approval, requirement supersession, architecture changes, implementation deviations, deferred requirements, emergency fixes, and deprecated features. Make the current approved state clear without deleting historical reasoning.

---

# 7. Lightweight tooling

Use Python's standard library unless a dependency is genuinely necessary and justified.

## 7.1 `scripts/new_feature.py`

Support a command such as:

```bash
python scripts/new_feature.py "User authentication"
```

Expected behaviour:

- derive a safe slug, e.g. `user-authentication`;
- find the next available zero-padded feature number, e.g. `001`;
- create `specs/001-user-authentication/`;
- copy feature templates into that directory;
- safely replace supported metadata placeholders (ID, title, creation date);
- refuse to overwrite an existing feature directory;
- print created paths and suggested next steps;
- support `--help` and clear error messages;
- reliably resolve the repository root or clearly require invocation from the repository root.

No third-party packages.

## 7.2 `scripts/validate_docs.py`

Support:

```bash
python scripts/validate_docs.py
python scripts/validate_docs.py --strict
```

Check at least:

- required baseline files/directories exist;
- Markdown fenced code blocks are balanced;
- obvious unresolved template placeholders do not appear in non-template/non-example areas (make exclusions explicit);
- requirement IDs follow supported patterns and are not duplicated in the applicable scope;
- feature directories contain core files;
- feature metadata/status values follow documented conventions to the extent safely checkable without an external parser;
- Mermaid fences are non-empty and start with a recognized diagram declaration;
- local Markdown links resolve where safely supported;
- JSON files and JSON Schema examples parse with the standard library;
- do not claim OpenAPI YAML is validated unless a YAML parser exists; report this limitation or support an optional validator.

Show useful file paths and line numbers where practical. Separate errors from warnings. Document exactly what `--strict` does. Do not attempt semantic requirements analysis.

## 7.3 Tests

Test feature creation, slug normalization, next ID selection, duplicate directory protection, malformed Markdown fences, duplicate requirement IDs, empty/invalid Mermaid declarations, broken internal Markdown links, and valid/invalid JSON examples.

Use temporary directories. Tests must not mutate repository fixtures.

---

# 8. GitHub and open-source readiness

Repository hygiene, onboarding, and documentation quality are product features.

## 8.1 README

Create a practical README containing:

1. CraftRail name, tagline, and one-sentence value proposition; make no unsupported availability or legal-clearance claims.
2. The problem it solves and intended users.
3. Key capabilities and principles.
4. A compact lifecycle visual (Mermaid is appropriate).
5. Repository layout overview.
6. Quickstart using the repo as a GitHub template.
7. Quickstart adopting conventions in an existing project.
8. Feature creation and validation commands.
9. Agent compatibility summary.
10. Supported document formats and rationale.
11. Comparison/coexistence guidance for Spec Kit and OpenSpec.
12. Contribution/support links, license, and project status.
13. A clear statement of what it does not do.

Make it scannable. No exaggerated claims, fake badges, usage statistics, testimonials, or unsupported statements such as "industry-leading".

## 8.2 Public positioning and adoption

Create `docs/framework/brand-and-positioning.md` and `ROADMAP.md`. The positioning document must define:

- Name: CraftRail.
- Tagline: Guardrails for agent-driven development.
- One-sentence description: a Git-native, agent-neutral framework for keeping engineering intent, architecture, and verification aligned across human and AI-assisted development.
- Primary audiences: individual engineers using coding agents, staff/principal engineers, technical leads, and small engineering teams.
- Core pains: context loss, undocumented assumptions, requirements drift, inconsistent agent instructions, architecture decisions that disappear into chat, and weak traceability from intent to tests.
- Product promises that are demonstrable in the repository: reusable project structure, consistent templates, agent instructions, requirement IDs, traceability, and lightweight validation.
- Clear non-promises: CraftRail does not guarantee agent correctness, replace tests/code review, or force a team into a specific agent, language, architecture, or delivery methodology.
- Adoption modes: use as a GitHub template for a new project; copy selected conventions into an existing repo; adopt gradually without replacing existing tooling.
- Differentiation and coexistence with Spec Kit and OpenSpec, grounded in verified capabilities rather than unsupported superiority claims.

README copy should be suitable for a public GitHub landing page: concise, specific, technically credible, and supported by working examples. Include a short demo walkthrough that lets a reader see how a hypothetical feature moves from intent to spec, architecture, tasks, and verification. Include a contribution path and a small, honest roadmap. Do not fabricate user numbers, adoption claims, testimonials, logos, or endorsements.

## 8.3 Community files

Create:

- `CONTRIBUTING.md`: contribution flow, style conventions, validation commands, PR expectations.
- `CODE_OF_CONDUCT.md`: use a recognized standard such as Contributor Covenant; include required attribution/version.
- `SECURITY.md`: responsible disclosure guidance. Do not invent an email address. Explain GitHub private vulnerability reporting if it is configured or how an owner can configure it.
- `SUPPORT.md`: where to ask questions and what information to include.
- `CHANGELOG.md`: initial Unreleased section.
- GitHub issue forms for bugs and feature requests.
- PR template with summary, validation, documentation impact, and compatibility impact.
- CI workflow that checks out the repo, installs a supported Python version, runs tests, and runs the validator.

## 8.4 License

Do not silently make a final legal decision. Record this recommendation in `docs/framework/assumptions-and-decisions.md`:

- MIT: simplest permissive option for a template/toolkit.
- Apache-2.0: permissive option with an explicit patent grant and additional terms.

For the first working draft, use MIT as a clearly flagged provisional default if a license file is required. State that the owner must review/confirm before public release. Do not invent a copyright holder or personal details.

## 8.5 Branding

The owner selected **CraftRail** with the tagline **Guardrails for agent-driven development** and repository slug `craft-rail` under `kshitijv97`. Do not rename the project or generate competing names. A preliminary search found an existing Japanese company using the same Craftrail name and operating `https://craftrail.co.jp/`; its services include HR/organizational consulting and AI-related offerings. Record this as a material naming/brand-confusion risk in `docs/framework/brand-and-positioning.md`, with source links and the date checked. Do not claim trademark, domain, or GitHub handle clearance. Continue implementing under the selected working name, but flag owner review as a release blocker before public promotion or domain/brand investment. Do not spend MVP effort on a logo or elaborate website; prioritize a clean README, clear positioning, useful examples, polished diagrams, and a credible project roadmap.

---

# 9. Ecosystem research and coexistence

Create `docs/framework/ecosystem-comparison.md` comparing current versions of:

- GitHub Spec Kit;
- OpenSpec;
- plain Markdown plus `AGENTS.md` conventions;
- optionally one other established approach if research supports it.

Compare only verifiable attributes: purpose, workflow shape, agent compatibility, artifacts, extensibility, and adoption model. Link official sources and include a `Last reviewed` date. Attribute marketing claims; do not treat GitHub stars as proof of quality.

Answer:

- What does this framework provide that teams would otherwise assemble manually?
- When should a user choose Spec Kit or OpenSpec instead?
- Can this framework coexist with either?
- Which artifacts are canonical versus generated/adapters?
- What is intentionally not automated?

Aim for interoperability, not lock-in. A team could use this framework for durable requirements and ADRs while using Spec Kit or OpenSpec to orchestrate feature work. Avoid competing sources of truth.

---

# 10. Documentation and writing quality

Write for technically capable engineers without assuming formal requirements-engineering experience.

- Use direct, precise language; explain unfamiliar terms on first use.
- Include realistic examples, not lorem ipsum.
- Distinguish mandatory rules from recommendations.
- Keep root README concise and link to deeper guides.
- Avoid marketing fluff, buzzwords, and claims that agents will always behave correctly.
- Explain trade-offs and limitations honestly.
- Keep example names and IDs consistent across documents.
- Use consistent spelling, heading hierarchy, terminology, and metadata conventions.
- Prefer canonical official documentation links.

---

# 11. Acceptance criteria

The task is complete only when the applicable criteria below are met.

## Product and documentation

- [ ] Repository explains its problem, target users, value proposition, principles, and non-goals.
- [ ] A new user can understand the structure without asking the author.
- [ ] A user can use it as a GitHub template and knows what to customize first.
- [ ] A user can adopt it into an existing repository without replacing existing docs.
- [ ] Functional and non-functional requirements are clearly distinguished.
- [ ] Feature templates cover scope, requirements, acceptance criteria, edge cases, assumptions, and risks.
- [ ] Technical plans cover components, interfaces, data, security, operations, rollout, and tests where applicable.
- [ ] Mermaid examples include sequence and at least one architecture/data-flow/state view.
- [ ] ADR guidance covers status, context, decision, alternatives, and consequences.
- [ ] Traceability is demonstrated end-to-end in the worked example.
- [ ] Agent guidance is concise and provider adapters do not diverge.
- [ ] Spec Kit/OpenSpec positioning is fair, fact-checked, linked, and non-hostile.

## Tooling

- [ ] `new_feature.py` creates the next valid feature directory from templates.
- [ ] It refuses to overwrite an existing feature.
- [ ] `validate_docs.py` detects the documented structural and syntax issues.
- [ ] Validator distinguishes errors/warnings and documents limitations.
- [ ] Automated tests cover success and failure cases.
- [ ] Validator and tests run without network access and third-party Python packages.

## GitHub readiness

- [ ] README, contribution, conduct, support, security, changelog, issue forms, PR template, and CI are present and consistent.
- [ ] No fake badges, usage statistics, testimonials, maintainer contacts, or unverified claims.
- [ ] License is explicitly flagged for owner review.
- [ ] Branding is provisional; trademark/availability claims are not overstated.
- [ ] CI runs the same core checks contributors are told to run locally.

## Engineering quality

- [ ] Internal Markdown links resolve or documented exceptions are recorded.
- [ ] Sample IDs are consistent and unique in their defined scopes.
- [ ] No contradictory instructions or duplicate sources of truth are introduced.
- [ ] No unrelated files are changed or removed.
- [ ] Final report accurately lists checks run and limitations.

---

# 12. Implementation sequence

### Phase A — Inspect and decide

- Inspect workspace and existing instructions.
- Research current ecosystem and canonical agent documentation.
- Record assumptions, design decisions, naming options, and license recommendation.
- Choose a safe target structure without asking the user for reversible decisions.

### Phase B — Build documentation

- Create project starter docs, requirement templates, feature templates, ADR template, contracts, and sample feature.
- Create framework guides and quickstarts.
- Create concise agent instructions and agent-neutral workflow prompts.

### Phase C — Build tooling

- Implement feature initializer and documentation validator.
- Add automated tests.
- Run and fix checks.

### Phase D — Prepare public repository

- Create README and open-source governance files.
- Add issue forms, PR template, and GitHub Actions workflow.
- Ensure CI and local commands are consistent.
- Review ecosystem comparison and public claims.

### Phase E — Maintainer review

Review for usability, duplication, confusing instructions, broken links, bad examples, overengineering, and missing onboarding.

Then provide a final report with:

1. What was built.
2. Final repository tree (at least top two levels).
3. How to create a new feature.
4. How to validate the repository.
5. How to use it as a GitHub template.
6. How to adopt it in an existing repository.
7. Exact checks run and outcomes.
8. Known limitations and deferred ideas.
9. Decisions requiring owner input before public release (license, maintainer identity/contact, repository URL, and any outstanding name/namespace clearance).
10. Three recommended next improvements, ranked by value.

**Begin by inspecting the current workspace, then implement the first working version. Do not stop after producing a proposal.**

---

# 13. Binding architecture amendment: complete agent neutrality

This amendment incorporates the project owner's additional architectural requirements and takes precedence over any conflicting interpretation elsewhere in this build brief. The Codex wording above describes the one-time implementation context only; Codex is not a CraftRail runtime dependency or architectural authority.

The owner confirmed `kshitijv97/craft-rail` as the GitHub repository on 2026-11-08; this supersedes any earlier suggested slug.

## 13.1 Three conceptual layers

- **Core:** specifications, requirements, architecture, contracts, traceability, decisions, and validation.
- **Workflow:** Discover, Specify, Clarify, Plan, Tasks, Analyze, Implement, Verify, and Converge.
- **Adapters:** Codex, Claude Code, OpenCode, and future coding-agent instruction discovery or optional integrations.

The framework owns the engineering process. The coding agent is replaceable.

## 13.2 Canonical source and shared instructions

Engineering requirements, specifications, architecture, workflows, decisions, and development conventions MUST be stored in agent-neutral Markdown, Mermaid, YAML, or JSON. Maintain exactly one canonical shared `AGENTS.md`. `CLAUDE.md` MUST remain a minimal adapter that imports `AGENTS.md` using Claude Code's supported `@AGENTS.md` import syntax. OpenCode MUST be documented to read `AGENTS.md` directly; it MUST NOT rely on `CLAUDE.md` fallback behavior.

Codex, Claude Code, and OpenCode adapters MUST NOT maintain divergent copies of shared policy. Provider-specific configuration, skills, commands, hooks, and MCP integrations MAY be added later as optional adapters, but the core framework MUST remain usable without them.

## 13.3 Provider independence

Core templates, specifications, validation tooling, GitHub workflows, and agent-neutral workflow prompts MUST NOT contain provider-specific business logic, API/runtime dependencies, proprietary slash commands, mandatory skills, hooks, subagents, or MCP integrations. Workflow prompts MUST work as ordinary instructions in Codex, Claude Code, and OpenCode.

Switching between the three agents MUST NOT require migrating project knowledge or rewriting canonical specifications. The repository's own requirements and conventions MUST remain understandable and maintainable in each.

## 13.4 Compatibility evidence and acceptance test

The compatibility guide MUST include a matrix of supported instruction files, optional integrations, limitations, and behavior directly verified with each agent. It MUST distinguish documented compatibility from functionality tested directly and MUST NOT claim direct testing unless performed.

Portability acceptance test: clone the same repository and open it at its root in Codex, Claude Code, and OpenCode. In each agent, identify the same canonical `AGENTS.md`, project requirement, and specification; ask for a proposed plan without editing; then make the same small approved documentation change and compare the result. No provider-specific project knowledge or configuration beyond the documented adapter may be required. If this test has not actually been run, record it as pending rather than passed.
