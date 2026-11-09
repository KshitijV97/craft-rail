# Quickstart

## New project

1. Create a repository from the CraftRail GitHub template or copy it locally.
2. Rewrite `docs/project/product-brief.md`, `engineering-principles.md`, stakeholders, and glossary.
3. Replace starter requirements and architecture with reviewed project facts; remove irrelevant examples.
4. Keep `AGENTS.md` canonical. Confirm `CLAUDE.md` imports it and OpenCode users open the repository root.
5. Create a feature with `python3 scripts/new_feature.py "Feature title"`.
6. Discover and specify the change. Resolve material questions; obtain human approval before implementation.
7. Plan, task, implement, verify, and converge the docs with the shipped change.
8. Run `python3 scripts/validate_docs.py` and `python3 -m unittest discover -s tests -v`.

## Existing project

Adopt incrementally. Keep existing authoritative documents in place, name their ownership in `docs/project/README.md`, and link from CraftRail rather than copying the same requirements into a second store. See [adoption guidance](adoption-existing-project.md).

## The first feature

Copyable prompts are in [workflow-prompts.md](workflow-prompts.md). The worked example is explicitly illustrative and shows IDs flowing through spec, plan, tasks, and verification.
