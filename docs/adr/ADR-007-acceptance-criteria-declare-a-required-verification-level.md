# ADR-007: Each acceptance criterion declares a required verification level

- **Status:** accepted
- **Date:** 2026-11-17
- **Decision owner:** CraftRail project owner
- **Related:** [ADR-003](ADR-003-verification-status-is-computed.md), [ADR-004](ADR-004-evidence-is-fresh-only-at-its-commit.md), product brief sections 6 (verification taxonomy) and 7 (Verification Specification)

## Context and forces

Human acceptance of a link (ADR-003) guards against a check that asserts nothing, but not against a check of the wrong kind. A unit test with every dependency mocked can pass while the integration it claims to cover is broken. The product brief proposes a Verification Specification document per behavior, with ten fields, written before implementation. Most of those fields already live on the acceptance criterion or the check itself, and a document per criterion is heavy for small changes.

## Decision

- Each acceptance criterion declares the minimum level of check that can verify it: `unit`, `component`, `integration`, `contract`, `architecture`, `acceptance`, or `non-functional`.
- A verification link whose check is below that level does not count. This is a deterministic rule, checked when links are validated.
- There is no separate Verification Specification document. The verification plan is the criterion's required level plus its proposed links, written before implementation.
- A criterion that requires `integration` also records which dependencies are real and which are simulated.

## Alternatives considered

- **Verification Specification document per behavior.** Rejected: duplicates fields held elsewhere and adds a document to every small change.
- **No levels; trust human link acceptance.** Rejected: leaves "a mocked unit test verifies an integration criterion" to reviewer attention.
- **CraftRail infers a check's level from the code.** Rejected: not deterministic across stacks.

## Consequences

- Positive: makes the product brief's problems #3 (implementation-centric tests) and #4 (integration failures) checkable.
- Negative / risks: a check's level is declared by its author, so a mislabelled check passes the rule; the human accepting the link must catch it.
- Open: how a check declares its level, whether the levels are ordered or some are separate kinds (for example `contract` versus `integration`), and whether a criterion may require more than one level.

## Supersedes / superseded by

None.
