# Domain Docs

How the engineering skills should consume this repo's domain documentation when exploring the codebase.

This is a **single-context** repo. CraftRail already owns canonical locations for its glossary and decisions; the skills use those instead of a root `GLOSSARY.md` or `docs/adr/`. Do not create `GLOSSARY.md` or `docs/adr/` at the repo root.

## Before exploring, read these

- **`docs/project/glossary.md`**: the project glossary (stands in for `GLOSSARY.md`).
- **`docs/project/decisions/`**: architecture decision records, named `ADR-NNN-short-title.md` and written from `templates/adr.md`. Read ADRs that touch the area you're about to work in.
- For feature work, also read the relevant `docs/project/requirements/` and `specs/NNN-name/spec.md` (see `AGENTS.md`).

If an entry you expect is missing, **proceed silently**. Don't flag its absence; don't suggest filling it upfront. The `/domain-modeling` skill (reached via `/grill-with-docs` and `/improve-codebase-architecture`) adds terms and decisions lazily when they actually get resolved, writing to the paths above.

## File structure

```
/
├── docs/project/
│   ├── glossary.md
│   └── decisions/
│       ├── README.md
│       └── ADR-001-short-title.md
├── templates/adr.md
└── src/
```

## Use the glossary's vocabulary

When your output names a domain concept (in an issue title, a refactor proposal, a hypothesis, a test name), use the term as defined in `docs/project/glossary.md`. Don't drift to synonyms the glossary explicitly avoids.

If the concept you need isn't in the glossary yet, that's a signal: either you're inventing language the project doesn't use (reconsider) or there's a real gap (note it for `/domain-modeling`).

## Flag ADR conflicts

If your output contradicts an existing ADR, surface it explicitly rather than silently overriding. Accepted ADRs are historical records: never rewrite one to fit an implementation; supersede it with a new ADR that links back.

> _Contradicts ADR-007 (event-sourced orders), but worth reopening because…_
