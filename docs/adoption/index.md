# Docs for adoption

This section is for developers and teams using CraftRail in a software project. It explains what files to create, when to use each artifact, and how to keep intent connected to implementation and verification.

## Pick your starting point

| Your situation | Start here |
|---|---|
| New project using GitHub | Create from the [CraftRail GitHub template](https://github.com/kshitijv97/craft-rail), then follow [GitHub template usage](../framework/github-template-usage.md) |
| Existing repository | Follow [incremental adoption](../framework/adoption-existing-project.md) |
| First feature | Read the [quickstart](../framework/quickstart.md), then create a feature from the supplied templates |
| New to requirements and traceability | Begin with [concepts and identifiers](../framework/concepts.md) and [requirements writing](../framework/requirements-writing-guide.md) |
| Using Claude Code, Codex, OpenCode, or another agent | Read [agent compatibility](../framework/agent-compatibility.md) and open the project normally; no setup prompt is required |

## The normal project path

1. Describe the product, users, outcomes, constraints, and non-goals.
2. Write stable, testable requirements and link them to business rules where needed.
3. Document relevant system boundaries, decisions, and contracts.
4. Specify each substantial feature before implementing it.
5. Break approved scope into tasks and explicit acceptance criteria.
6. Implement, test, record evidence, and update docs when the shipped behavior changes.

Use the [workflow guide](../framework/workflow.md) proportionally. A small fix does not need a large specification package; a high-impact feature benefits from the complete path.

## Adoption guides

- [Quickstart](../framework/quickstart.md)
- [Use the GitHub template](../framework/github-template-usage.md)
- [Adopt into an existing project](../framework/adoption-existing-project.md)
- [Overview and architecture](../framework/overview.md)
- [Repository structure](../framework/repository-structure.md)
- [Concepts and identifiers](../framework/concepts.md)
- [Requirements writing](../framework/requirements-writing-guide.md)
- [Feature specifications](../framework/feature-specification-guide.md)
- [Architecture documentation](../framework/architecture-documentation-guide.md)
- [Mermaid diagrams](../framework/diagrams-guide.md)
- [Architecture decisions](../framework/adr-guide.md)
- [API and data contracts](../framework/contracts-guide.md)
- [Lifecycle and gates](../framework/workflow.md)
- [Agent-neutral prompts](../framework/workflow-prompts.md)
- [Tasks and planning](../framework/tasks-guide.md)
- [Verification and traceability](../framework/traceability-and-verification.md)
- [Change control](../framework/change-control.md)
- [Agent compatibility](../framework/agent-compatibility.md)
- [Validator reference](../framework/validation.md)
- [Ecosystem comparison](../framework/ecosystem-comparison.md)
- [FAQ](../framework/faq.md)

The [account recovery walkthrough](../examples/sample-feature-walkthrough.md) shows how one illustrative feature connects its spec, plan, tasks, diagrams, acceptance criteria, and verification evidence.
