# ADR-014: Changes to links or waivers are flagged for human review

- **Status:** accepted
- **Date:** 2026-11-24
- **Decision owner:** CraftRail project owner
- **Related:** [ADR-006](ADR-006-acceptance-is-recorded-on-the-protected-branch.md), [ADR-013](ADR-013-the-cli-output-is-the-integration-contract.md)

## Context and forces

ADR-006 makes a link or waiver accepted once it is merged to the protected branch. A software factory that merges its own pull requests would accept an agent's links with no human seeing them, and the guarantee of ADR-003 would be gone. Requiring a human on every pull request would defeat the factory.

## Decision

- `craftrail status`, given the base branch, reports any added, changed, or removed verification link or waiver as **acceptance changes present** and exits with code `3`.
- Links and waivers that exist only on the branch are proposed: they do not count toward status until merged.
- When criteria are also unsatisfied, exit code `1` takes precedence, so the agent keeps working; code `3` appears once everything else is satisfied. Invalid input (`2`) outranks both.
- A factory routes pull requests with code `3` to a human and lets code-only changes merge. Whether that routing is enforced is up to the project's branch protection; CraftRail reports, it does not block merges itself.

## Alternatives considered

- **Human review on every pull request.** Rejected: removes the factory's autonomy for changes that do not touch acceptance.
- **CraftRail blocks the merge itself.** Rejected: merge control belongs to the code host.

## Consequences

- Positive: human attention goes only to the pull requests that change what counts as evidence.
- Negative / risks: a project that ignores code `3` loses the guarantee; the docs must say so plainly.

## Supersedes / superseded by

None.
