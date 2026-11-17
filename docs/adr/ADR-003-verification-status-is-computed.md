# ADR-003: Verification status is computed; humans accept links and waivers

- **Status:** accepted
- **Date:** 2026-11-17
- **Decision owner:** CraftRail project owner
- **Related:** [ADR-002](ADR-002-evidence-gated-acceptance-is-the-core.md), [GLOSSARY.md](https://github.com/kshitijv97/craft-rail/blob/main/GLOSSARY.md), critical review finding F-05 (approval is an editable string)

## Context and forces

"Deterministic at the core" needs a precise boundary. Whether a check meaningfully verifies an acceptance criterion is a semantic judgment no rule can make: an agent can write a test named after a criterion that asserts nothing. Today a feature's verification status is a free-text field, so any party, including the agent whose work is being judged, can mark a criterion `verified`.

## Decision

Authority is split three ways:

| Decided by | What |
|---|---|
| A human, or a reviewer independent of the author | Accepting a **verification link** (this check counts as evidence for this acceptance criterion) and granting a **waiver** (named approver, reason, scope) |
| Deterministic rules | Whether the check ran, passed and was not skipped; whether it ran against the current commit; whether what it depends on changed since |
| Agents | Proposing links, writing checks, investigating failures. Never accepting a link, granting a waiver, or setting a status |

**Verification status is computed** from accepted links plus evidence plus freshness. It is never stored as an editable field.

## Alternatives considered

- **Editable status with review discipline (current state).** Rejected: the party whose work is judged can flip the string; review attention is the only guard.
- **Fully deterministic verification (any linked passing check counts).** Rejected: an agent could create both the check and the link, so a trivial test would verify any criterion.
- **AI judge decides whether a check is meaningful.** Rejected as an authority: it reintroduces the self-assessment problem and makes status non-reproducible. An AI may still advise the human accepting a link.

## Consequences

- Positive: no single edit by an agent can make a criterion count as verified.
- Positive: status is reproducible from the repository and evidence alone.
- Negative / risks: link acceptance adds human work. Where and how acceptance is recorded so it cannot be forged by the same agent (for example, through review-protected files or forge approvals) is still open.
- Open: the exact freshness rule, the full status vocabulary, and how flaky, skipped and environment-dependent checks map to status.

## Supersedes / superseded by

None.
