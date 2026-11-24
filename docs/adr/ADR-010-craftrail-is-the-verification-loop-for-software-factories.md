# ADR-010: CraftRail is the verification loop for software factories, alongside existing agent workflows

- **Status:** accepted
- **Date:** 2026-11-24
- **Decision owner:** CraftRail project owner
- **Related:** [ADR-002](ADR-002-evidence-gated-acceptance-is-the-core.md), [ADR-003](ADR-003-verification-status-is-computed.md)

## Context and forces

Teams are building software factories: pipelines where coding agents take work from a specification to a merged change with little human intervention. Agent workflow ecosystems such as Matt Pocock's skills and Compound Engineering already cover how agents brainstorm, plan, specify, write code test-first, review, and capture lessons. What a factory still lacks is a loop that tells an agent, deterministically, which acceptance criteria are not yet satisfied at the current commit and why, and that cannot be closed by the agent's own claim.

CraftRail today describes itself as owning the engineering process, with its own lifecycle and workflow prompts. That overlaps with those ecosystems.

## Decision

- CraftRail's purpose is to give software factories a **deterministic verification loop**: an agent changes code, CraftRail computes each criterion's status from fresh evidence, the agent reads machine-readable reasons, and the loop repeats until every criterion is verified or waived.
- CraftRail complements agent workflow ecosystems and does not compete with them. It does not ship its own brainstorming, planning, test-driven development, review, or knowledge-capture workflow.
- CraftRail works under any of those workflows through stable, tool-neutral surfaces: the CLI's exit code and machine-readable output, and optional adapters that a workflow can call.

## Alternatives considered

- **CraftRail as a full engineering framework that owns the process.** Rejected: duplicates mature workflow tools and forces teams to choose between them and CraftRail.
- **CraftRail as a plugin of one ecosystem.** Rejected: ties the verification core to one workflow and one agent harness.

## Consequences

- Positive: teams keep the workflow they use and add CraftRail as the gate.
- Positive: narrows what CraftRail builds and gives clear grounds to decline workflow features.
- Negative / risks: CraftRail depends on those ecosystems producing acceptance criteria it can read; integration design carries the product.
- Open: what happens to CraftRail's existing lifecycle, workflow prompts, and the "framework owns the engineering process" statement in `AGENTS.md`; who writes acceptance criteria when the planning tool has its own format.

## Supersedes / superseded by

None. Narrows the "framework owns the engineering process" positioning; the repository instructions still need to be updated to match.
