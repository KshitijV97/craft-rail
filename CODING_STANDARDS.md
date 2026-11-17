# Coding standards

Rules that code and docs in this repository follow. Each one is a defect class an author should avoid and a reviewer can see in a diff. Anything Ruff, Mypy, coverage, actionlint, pre-commit, or `scripts/validate_docs.py` already enforces is left out: the checks own it.

This first draft was written before the repository had merged pull requests or review history. Its rules come from conventions the repository already states, and each one names its source. Treat it as provisional until review history confirms or retires a rule.

## Python core

- **Core code stays standard-library only.** Code in `scripts/` and `src/craftrail/knowledge.py` imports nothing outside the Python standard library and runs on Python 3.10. A new third-party import there, or a stdlib API added after 3.10, is a defect even when it passes locally on a newer interpreter. Source: `docs/framework/python-quality.md`.
- **Provider SDKs stay in optional adapters.** Code for a specific agent or provider, such as the MCP SDK, lives only in an optional adapter module. Core modules, templates, validation, and workflows never import it or branch on a provider. Source: `AGENTS.md` (Engineering behavior), engineering principle 6.
- **Types do not replace runtime validation.** JSON, Markdown, YAML, filesystem state, CLI arguments, and OS errors are checked at runtime where they enter the code. An annotation alone does not count as handling malformed input. Source: `docs/framework/python-quality.md`.
- **No silenced type uncertainty without a reason.** `Any`, `# type: ignore`, and `cast` appear only with a comment that says why the uncertainty is real and safe. Source: `docs/framework/python-quality.md`.

## Tests

- **Behavior changes come with tests.** A change to what a script or module does adds or updates a test in `tests/` that would fail without the change. Where the change implements a requirement or acceptance criterion, the test names or links it. Source: `AGENTS.md` (Engineering behavior, Verification and reporting).
- **Tests run without pytest.** Tests are written as `unittest.TestCase` so the Python-version matrix can run them with `python -m unittest`. A test that depends on pytest-only fixtures or plugins breaks that matrix. Source: `docs/framework/python-quality.md`.

## Framework artifacts and docs

- **Accepted records are not rewritten.** An accepted ADR or approved requirement is never edited to make an implementation look compliant. Changes go through a new ADR that supersedes the old one and links back. Source: `AGENTS.md`, `docs/project/decisions/README.md`.
- **Behavior changes update their docs in the same change.** A change to approved behavior also updates the affected spec, contract, diagram, decision, and traceability entries. Code that drifts from its spec is a defect in the change, not a follow-up. Source: `AGENTS.md`, engineering principle 5.
- **Canonical knowledge uses portable formats.** Requirements, architecture, contracts, decisions, workflow, and conventions are written in Markdown, Mermaid, YAML, or JSON. A canonical artifact that only works in one agent or tool is a defect. Source: `AGENTS.md`.
- **Internal notes stay off the published site.** Everything under `docs/` is published by Zensical except `docs/project/`. Working notes, plans, learnings, and drafts go under `docs/project/` or outside `docs/`. Source: `zensical.toml` (`exclude_docs`).

## Maintaining this file

Add a rule only when a defect class appeared in a review finding the author fixed, a fix commit, a cleanup that removed it across the codebase, or a solution record in `docs/project/ce/solutions/`, and no check covers it. State the rule as a condition that stays true without naming volatile numbers or symbols, and group it by area. When a check starts enforcing a rule, or the team keeps declining findings under it, remove the rule.
