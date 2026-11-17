# ADR-004: Evidence is fresh only at the commit it ran against

- **Status:** accepted
- **Date:** 2026-11-17
- **Decision owner:** CraftRail project owner
- **Related:** [ADR-003](ADR-003-verification-status-is-computed.md), [GLOSSARY.md](https://github.com/kshitijv97/craft-rail/blob/main/GLOSSARY.md)

## Context and forces

ADR-003 makes verification status depend on whether evidence is still fresh, but left the rule open. A loose rule (evidence stays valid until someone notices a relevant change) makes status depend on judgment. A precise rule that tracks which files a check depends on needs a dependency or component model, which CraftRail does not have yet.

## Decision

- Evidence counts only for the exact commit it ran against. Any new commit makes earlier evidence stale.
- A stale, missing, or skipped result is not evidence. A check that fails on any run at the commit counts as failing, so a flaky check is a failing check.
- Verification status has five values, computed per acceptance criterion: **unlinked**, **pending**, **failing**, **verified**, **waived** (defined in the glossary).
- Status for a requirement, feature, or project is a view over its criteria, not a status of its own. "Partially verified" is such a view. "Blocked" belongs to the issue tracker.
- Finer freshness, where evidence survives a commit that does not touch what the check depends on, may come later. Anything it cannot map falls back to this rule.

## Alternatives considered

- **Path-based freshness now.** Deferred: it needs each check's dependencies declared or inferred, and a wrong mapping would mark stale evidence fresh.
- **Time-based freshness (evidence valid for N days).** Rejected: time says nothing about whether the code changed.
- **Seven statuses from the product brief, including partially verified and blocked.** Rejected as stored statuses: neither can be computed from links and evidence for one criterion.

## Consequences

- Positive: status is reproducible and needs no dependency model.
- Positive: flaky checks show up as failing instead of hiding behind a retry.
- Negative / risks: every commit needs a full verification run to stay verified, which costs CI time on large suites. Path-based freshness is the planned relief.
- Open: how a waiver interacts with a failing check on the same criterion.

## Supersedes / superseded by

None.
