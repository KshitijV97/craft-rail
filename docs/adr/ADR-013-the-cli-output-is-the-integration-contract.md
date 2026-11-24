# ADR-013: The CLI's exit code and JSON output are the integration contract

- **Status:** accepted
- **Date:** 2026-11-24
- **Decision owner:** CraftRail project owner
- **Related:** [ADR-005](ADR-005-craftrail-ships-as-an-installable-cli.md), [ADR-010](ADR-010-craftrail-is-the-verification-loop-for-software-factories.md), [ADR-014](ADR-014-acceptance-changes-are-flagged-for-human-review.md)

## Context and forces

CraftRail has to work under any agent workflow and in any CI. An agent in the verification loop needs to know which criteria are unsatisfied and why, in a form it can act on without parsing prose.

## Decision

- `craftrail status` is the integration point. Its exit code and its `--format json` output are a versioned contract.
- For each acceptance criterion the output gives its ID, its status, one reason code, and the check IDs involved. The reason codes are `no-link`, `no-evidence`, `stale`, `skipped`, `failed`, `below-level`, and `check-not-found`.
- Exit codes: `0` every criterion is verified or waived; `1` at least one criterion is not satisfied; `2` the input or configuration is invalid; `3` acceptance changes are present (ADR-014).
- CraftRail ships one agent-neutral skill that runs `craftrail status`, reads the reasons, writes criteria into spec files, and proposes links. Any agent workflow can load it.
- Ecosystem-specific packages, such as a Compound Pack, wait until dogfooding shows what they need.

## Alternatives considered

- **A plugin per ecosystem first.** Rejected: ties the contract to one workflow before it is proven.
- **Human-readable output only.** Rejected: agents would scrape prose, and any wording change would break them.

## Consequences

- Positive: any workflow, CI, or factory integrates with a process call.
- Negative / risks: the JSON shape becomes a compatibility promise; changes need versioning.

## Supersedes / superseded by

None.
