# ADR-011: CraftRail's conventions stay; its lifecycle becomes a reference workflow

- **Status:** accepted
- **Date:** 2026-11-24
- **Decision owner:** CraftRail project owner
- **Related:** [ADR-002](ADR-002-evidence-gated-acceptance-is-the-core.md), [ADR-010](ADR-010-craftrail-is-the-verification-loop-for-software-factories.md)

## Context and forces

ADR-010 says CraftRail complements agent workflow tools and does not supply its own workflow. The repository still teaches a 9-step lifecycle with copyable workflow prompts, and `AGENTS.md` and the `craftrail-workflow` skill say "the framework owns the engineering process". Those overlap with `ce-plan`, `ce-work`, `to-spec`, and `tdd`. Some of what the lifecycle introduced is still needed: stable IDs and feature folders are the engine's input format.

## Decision

- The conventions stay: stable IDs (`FR`, `NFR`, `AC`, and the rest) and feature folders under `specs/NNN-name/`. They are what `craftrail` reads.
- The 9-step lifecycle and the workflow prompts become a **reference workflow** for teams that have no agent workflow. They are not presented as the product, and nothing in the engine depends on them.
- The "framework owns the engineering process" statement in `AGENTS.md` and in the `craftrail-workflow` skill is rewritten to match ADR-010, as a separate change.

## Alternatives considered

- **Delete the lifecycle and prompts.** Rejected: teams without an agent workflow still benefit from them, and they cost little to keep labelled.
- **Keep the lifecycle as the product.** Rejected by ADR-010.

## Consequences

- Positive: a team using Compound Engineering or Matt Pocock's skills adopts CraftRail without changing how it plans and builds.
- Negative / risks: the adoption docs need rework to lead with the verification loop rather than the lifecycle.

## Supersedes / superseded by

None.
