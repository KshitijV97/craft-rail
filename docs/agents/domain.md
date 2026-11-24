# Domain Docs

How the engineering skills should consume this repo's domain documentation when exploring the codebase.

This is a **single-context** repo. The repository is both the CraftRail framework and a GitHub template, so the framework's own domain docs are kept apart from the template's starter content:

- CraftRail's own vocabulary and decisions: root `GLOSSARY.md` and `docs/adr/`.
- `docs/project/` is **starter content for adopting projects**. Never write CraftRail's own terms or decisions there.

## Before exploring, read these

- **`GLOSSARY.md`** at the repo root: CraftRail's domain vocabulary.
- **`docs/adr/`**: CraftRail's architecture decision records, named `ADR-NNN-short-title.md` (CraftRail's convention, not `0001-slug.md`) and written from `templates/adr.md`. Read ADRs that touch the area you're about to work in.
- For feature work, also read the relevant `specs/NNN-name/spec.md` and its status (see `AGENTS.md`).

If an entry you expect is missing, **proceed silently**. Don't flag its absence; don't suggest filling it upfront. The `/domain-modeling` skill (reached via `/grill-with-docs` and `/improve-codebase-architecture`) adds terms and decisions lazily when they actually get resolved, writing to the paths above.

## File structure

```
/
├── GLOSSARY.md
├── docs/adr/
│   ├── README.md
│   └── ADR-002-short-title.md
├── docs/project/        ← starter content for adopters, not CraftRail's own docs
├── templates/adr.md
└── src/
```

## Use the glossary's vocabulary

When your output names a domain concept (in an issue title, a refactor proposal, a hypothesis, a test name), use the term as defined in `GLOSSARY.md`. Don't drift to synonyms the glossary explicitly avoids.

If the concept you need isn't in the glossary yet, that's a signal: either you're inventing language the project doesn't use (reconsider) or there's a real gap (note it for `/domain-modeling`).

## Flag ADR conflicts

If your output contradicts an existing ADR, surface it explicitly rather than silently overriding. Accepted ADRs are historical records: never rewrite one to fit an implementation; supersede it with a new ADR that links back.

> _Contradicts ADR-NNN (the earlier decision), but worth reopening because…_
