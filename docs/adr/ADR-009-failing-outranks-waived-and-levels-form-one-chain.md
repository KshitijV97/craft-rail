# ADR-009: Failing outranks waived; verification levels form one ordered chain

- **Status:** accepted
- **Date:** 2026-11-24
- **Decision owner:** CraftRail project owner
- **Related:** [ADR-004](ADR-004-evidence-is-fresh-only-at-its-commit.md) (open item: waivers and failing checks), [ADR-007](ADR-007-acceptance-criteria-declare-a-required-verification-level.md) (open item: whether levels are ordered)

## Context and forces

ADR-004 left open what status a criterion has when it is waived and one of its checks fails. ADR-007 says a check "below" the required level does not count, which assumes the levels have an order. Contract, architecture, and non-functional checks do not sit on a line with unit and integration tests.

## Decision

- **Failing outranks waived.** A waiver accepts that a criterion goes unverified; it does not accept that it is broken. A waiver applies only where the status would otherwise be unlinked or pending.
- **One ordered chain:** `unit` < `component` < `integration` < `acceptance`. A check at or above the required level in this chain counts.
- **Separate kinds:** `contract`, `architecture`, and `non-functional` are not on the chain. A check of one of these kinds counts only for a criterion that requires exactly that kind.

## Alternatives considered

- **Waived outranks failing.** Rejected: a waiver would hide a check that shows the criterion is broken.
- **All seven levels in one order.** Rejected: there is no meaningful sense in which an architecture rule is above or below an integration test.
- **No ordering; exact match always.** Rejected: an end-to-end acceptance check should satisfy a criterion that only requires integration.

## Consequences

- Positive: both rules are deterministic and short enough to state in the CLI's output.
- Negative / risks: a criterion that needs both an integration check and a contract check must be split into two criteria.

## Supersedes / superseded by

None. Resolves open items in ADR-004 and ADR-007.
