# ADR-005: CraftRail ships as a versioned, installable CLI

- **Status:** accepted
- **Date:** 2026-11-17
- **Decision owner:** CraftRail project owner
- **Related:** [ADR-002](ADR-002-evidence-gated-acceptance-is-the-core.md), critical review findings F-07 (the template ships maintainer content) and F-08 (no upgrade path)

## Context and forces

CraftRail is distributed as a GitHub template. A project created from it gets a copy of the scripts and conventions at that moment, with no way to receive fixes, and it inherits CraftRail's own maintainer content. An engine that computes verification status has to behave the same way in every project that uses a given version, or two projects would compute different statuses from the same inputs.

## Decision

- The engine ships as a versioned Python package with a command-line interface, installable with `pipx`.
- Each project pins the CraftRail version it uses, so status is reproducible and upgrades are deliberate.
- The repository template becomes an optional starter: example conventions and folders. It is not how the engine is delivered.

## Alternatives considered

- **Stay a template only.** Rejected: copied scripts cannot be upgraded (F-08), and every project's copy may drift.
- **Git submodule or vendored scripts.** Rejected: awkward to pin and update, and still mixes CraftRail's files into the project.
- **Hosted service.** Rejected for the core: evidence-gated acceptance must work offline, in the repository, without an account.

## Consequences

- Positive: one engine version, one behavior; fixes reach projects through upgrades.
- Positive: separates CraftRail's own content from what adopters receive (F-07).
- Negative / risks: adds packaging and release work, and installation becomes a step for adopters.
- Open: whether the core keeps the standard-library-only rule now that it is an installed package.

## Supersedes / superseded by

None.
