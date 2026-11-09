# Repository structure

```text
AGENTS.md / CLAUDE.md       Shared instructions / Claude import adapter
docs/framework/             Framework explanation and operating guides
docs/project/               Project-level intent, requirements, architecture, contracts
docs/examples/               End-to-end walkthrough
specs/NNN-feature/           One folder per feature; spec, plan, tasks, verification
templates/                   Blank reusable source templates
scripts/                     Dependency-free helper tools
tests/                       Tooling tests using temporary repositories
.github/                     CI and contribution forms
```

`docs/framework/` describes CraftRail. `docs/project/` is meant to be customized by adopters. `specs/` records feature-level intent and delivery state. `templates/` are blank sources; examples are illustrative and not alternate canonical policy. Do not copy framework docs into every feature. Existing projects may keep their current layout and link to it.
