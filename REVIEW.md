# Review policy

@CODING_STANDARDS.md

This file holds this repository's review policy: what each severity means here, what not to flag, and the evidence a finding needs. It is a provisional first draft written before any review history existed. Revise it as pull requests show what the team actually treats as urgent or declines.

## Severity

- **Blocking:** the change breaks a rule in `CODING_STANDARDS.md` that affects users of the template, contradicts an accepted ADR or approved requirement, claims a check passed that did not run, or adds provider-specific logic to a core artifact.
- **Should fix:** a correctness gap with a concrete failure scenario, such as unvalidated input or a missing test for changed behavior, that does not break the template for users today.
- **Nit:** wording, naming, or structure that would read better. The author may decline these without discussion.

## Do not flag

- Anything Ruff, Mypy (strict), coverage, actionlint, pre-commit, or `scripts/validate_docs.py` enforces. CI owns those.
- Style preferences that no written rule backs.
- Draft or proposed specs that are not yet approved, except to point out where they contradict approved ones.

## Evidence a finding needs

Each finding names the file and line, the rule or requirement it breaks, and a concrete scenario: the input or state, and the wrong result or failure it causes. A finding with no scenario is a nit at most.
