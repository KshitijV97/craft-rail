# ADR-002: Evidence-gated acceptance is CraftRail's core

- **Status:** accepted
- **Date:** 2026-11-17
- **Decision owner:** CraftRail project owner
- **Related:** [ADR-003](ADR-003-verification-status-is-computed.md), [GLOSSARY.md](https://github.com/kshitijv97/craft-rail/blob/main/GLOSSARY.md), product vision and discovery brief (discovery session 2026-11-17), critical review findings F-01, F-05, F-06 (`docs/critical-review` branch)

## Context and forces

CraftRail started as a repository template of conventions: requirement IDs, feature folders, a lifecycle, and a structural validator. The product vision asks it to be a harness-agnostic governance layer with five engines (specification, architecture, verification, evidence, agent adapter) and a twelve-stage lifecycle.

Most of that surface already exists elsewhere. Spec Kit, OpenSpec, Matt Pocock's skills and Compound Engineering author specs and drive agent workflow. CI runs tests. ArchUnit, dependency-cruiser and import-linter enforce architecture rules. Pact and Schemathesis verify contracts. None of them answers whether a particular acceptance criterion is satisfied by tool-produced evidence for the current commit, and whether that evidence is still fresh, without trusting an agent's claim. CI reports that the suite passed; it does not report which criteria have no evidence or whose evidence went stale.

## Decision

CraftRail's core is **evidence-gated acceptance**: a deterministic engine that computes each acceptance criterion's verification status from evidence produced by real tools.

- Spec authoring, workflow orchestration, test execution, and architecture or contract checking are delegated to existing tools. CraftRail integrates with them; it does not rebuild them.
- CraftRail's conventions and templates become the input format for the engine, not the product on their own.
- The acceptance criterion is the unit of verification. "Requirement Slice" is not a stored concept: the criterion is the atomic, independently checkable outcome, and the feature is the delivery grouping. "Slice" may survive informally as a delivery-planning word outside the model.
- Non-functional requirements are verified through acceptance criteria like any other requirement.

## Alternatives considered

- **Full engineering framework (all five engines and the full lifecycle).** Rejected as the core: it overlaps heavily with mature tools, spreads a small project thin, and its distinct value is buried among capabilities others already provide.
- **Requirements traceability system (links only, no evidence).** Rejected: links without execution evidence reproduce the hand-maintained matrix that already exists in `docs/framework/traceability-and-verification.md` and that the critical review shows can be satisfied by editing a string.
- **Stay a template of conventions.** Rejected: conventions are advisory, and the tagline "guardrails" is not met by advice (critical review F-06).
- **Requirement Slice as a distinct entity between requirement and acceptance criterion.** Rejected: in every worked example it was either a synonym for an acceptance criterion or had no definable boundary, and "vertical slice" already means a delivery unit.

## Consequences

- Positive: a narrow, defensible value proposition that CI and existing workflow tools do not cover; clear grounds to decline features that belong to other tools.
- Positive: existing assets (stable IDs, feature folders, the read-only knowledge reader, the graph export proposed in PR #2) become inputs and adapters rather than throwaway work.
- Negative / risks: the product depends on ingesting other tools' output formats, which vary by stack. Value must be demonstrated against a baseline (Compound Engineering + TDD + CI) rather than assumed.
- Open: how evidence freshness is decided, what architecture model (if any) the core keeps, distribution model (template vs installable tool), and the fate of the Studio proposal.

## Supersedes / superseded by

None.
