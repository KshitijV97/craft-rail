# ADR-008: Links and waivers live in spec files; evidence starts with JUnit XML

- **Status:** accepted
- **Date:** 2026-11-24
- **Decision owner:** CraftRail project owner
- **Related:** [ADR-004](ADR-004-evidence-is-fresh-only-at-its-commit.md), [ADR-006](ADR-006-acceptance-is-recorded-on-the-protected-branch.md), [ADR-007](ADR-007-acceptance-criteria-declare-a-required-verification-level.md)

## Context and forces

ADR-006 makes acceptance depend on review of the files that hold links and waivers, and left open where those files are. If links sit as annotations in test code, the agent that writes a test also writes its link in the same file, so review rules such as CODEOWNERS cannot tell the two apart, and every language needs its own annotation syntax. Evidence also needs a first input format that most test runners already produce.

## Decision

- Verification links and waivers are written in spec files, next to the acceptance criterion they belong to. Test code does not refer to CraftRail.
- A link names its check by the identifier the test runner reports, such as the JUnit `classname` and `name`, and declares the check's verification level.
- The first evidence format CraftRail reads is JUnit XML. The CLI stamps each result with the commit and environment it observes from git and the run, never from the report file.
- Manual checks and other result formats come later.

## Alternatives considered

- **Annotations or decorators in test code.** Rejected: puts the check and its claim in one file the same author controls, and needs per-language support.
- **A separate links database or service.** Rejected: CraftRail stays in the repository and works offline (ADR-005).
- **Trust a commit recorded inside the report.** Rejected: the report is produced by the run being judged and can be edited.

## Consequences

- Positive: CODEOWNERS on spec files separates writing a check from accepting it.
- Positive: JUnit XML covers pytest, Jest, Go, JVM, and .NET runners without CraftRail-specific plugins.
- Negative / risks: renaming a test breaks its link until the spec is updated. CraftRail should report a link whose check never appears in the evidence.
- Open: the exact syntax for criteria, links, and waivers in spec files.

## Supersedes / superseded by

None.
