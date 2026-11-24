# ADR-006: A link or waiver is accepted when it is on the protected base branch

- **Status:** accepted
- **Date:** 2026-11-17
- **Decision owner:** CraftRail project owner
- **Related:** [ADR-003](ADR-003-verification-status-is-computed.md), critical review finding F-05 (approval is an editable string)

## Context and forces

ADR-003 says a human, not the authoring agent, accepts verification links and waivers, but left open how that acceptance is recorded so the agent cannot forge it. Any field CraftRail stores in the repository can be written by whoever can write files, including an agent. The code host already enforces who may approve and merge changes.

## Decision

- A verification link or waiver counts as accepted when it is present on the project's protected base branch.
- Getting it there goes through the code host's normal review: branch protection, required reviews, and CODEOWNERS for the files that hold links and waivers. CraftRail documents this setup and can check that it is in place.
- CraftRail has no approval system, user accounts, or signatures of its own.
- On a pull request branch, a new link or waiver is proposed. It is accepted once merged.

## Alternatives considered

- **Approval field or signature in the file.** Rejected: an agent that can edit the file can edit the field.
- **CraftRail's own approval service.** Rejected: it duplicates what the code host already enforces and adds an account system.
- **Cryptographic signing of each link.** Rejected for now: key management is heavy for small teams, and branch protection already gives the needed guarantee where it is configured.

## Consequences

- Positive: acceptance reuses review that teams already do and cannot be granted by a file edit alone.
- Negative / risks: the guarantee is only as strong as the project's branch protection. A solo developer without required reviews accepts their own agent's links by merging.
- Negative / risks: depends on the code host's features. Hosts without CODEOWNERS need an equivalent.
- Open: where links and waivers are stored (spec files or code annotations), which decides what CODEOWNERS must cover.

## Supersedes / superseded by

None.
