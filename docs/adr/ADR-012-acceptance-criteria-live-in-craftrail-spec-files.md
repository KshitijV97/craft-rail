# ADR-012: Acceptance criteria live in CraftRail spec files; workflow tools refer to them

- **Status:** accepted
- **Date:** 2026-11-24
- **Decision owner:** CraftRail project owner
- **Related:** [ADR-006](ADR-006-acceptance-is-recorded-on-the-protected-branch.md), [ADR-008](ADR-008-links-live-in-spec-files-and-evidence-comes-from-junit.md), [ADR-010](ADR-010-craftrail-is-the-verification-loop-for-software-factories.md)

## Context and forces

Agent workflow tools write their own planning artifacts: Compound Engineering writes plan files in the repository, and Matt Pocock's `to-spec` writes GitHub issues. CraftRail needs acceptance criteria next to their verification links (ADR-008), reviewed under branch protection (ADR-006). Criteria written in two places drift apart.

## Decision

- Acceptance criteria, with their required verification levels, live in CraftRail spec files (`specs/NNN-name/`). That is their only home.
- A plan, issue, or other workflow artifact refers to the feature or criterion ID instead of restating the criteria.
- CraftRail does not read criteria out of plans or issues.

## Alternatives considered

- **Adapters that read criteria from plans and issues.** Rejected: GitHub issues are outside branch protection, and each workflow tool's format would need its own parser.
- **Criteria copied into both places.** Rejected: two sources of truth.

## Consequences

- Positive: one reviewed home for criteria, links, and waivers.
- Negative / risks: workflow tools need to be told to write criteria into the spec file; the agent-neutral skill (ADR-013) carries that instruction.

## Supersedes / superseded by

None.
