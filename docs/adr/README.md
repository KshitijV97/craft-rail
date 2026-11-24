# CraftRail architecture decisions

Decisions about the CraftRail framework itself, named `ADR-NNN-short-title.md` from the repository's [ADR template](https://github.com/kshitijv97/craft-rail/blob/main/templates/adr.md). Accepted ADRs are historical records: supersede them with a new record rather than rewriting them.

These are separate from `docs/project/decisions/`, which is starter content for projects that adopt the template.

`ADR-001` is reserved for the proposed Studio and machine-readable conventions record in the `proposal/craftrail-studio` pull request. Studio itself is shelved (see [Product direction](../direction/vision.md)); that record will be revised before it is accepted.

| ADR | Decision | Status |
|---|---|---|
| [ADR-002](ADR-002-evidence-gated-acceptance-is-the-core.md) | Evidence-gated acceptance is CraftRail's core | accepted |
| [ADR-003](ADR-003-verification-status-is-computed.md) | Verification status is computed; humans accept links and waivers | accepted |
| [ADR-004](ADR-004-evidence-is-fresh-only-at-its-commit.md) | Evidence is fresh only at the commit it ran against | accepted |
| [ADR-005](ADR-005-craftrail-ships-as-an-installable-cli.md) | CraftRail ships as a versioned, installable CLI | accepted |
| [ADR-006](ADR-006-acceptance-is-recorded-on-the-protected-branch.md) | A link or waiver is accepted when it is on the protected base branch | accepted |
| [ADR-007](ADR-007-acceptance-criteria-declare-a-required-verification-level.md) | Each acceptance criterion declares a required verification level | accepted |
| [ADR-008](ADR-008-links-live-in-spec-files-and-evidence-comes-from-junit.md) | Links and waivers live in spec files; evidence starts with JUnit XML | accepted |
| [ADR-009](ADR-009-failing-outranks-waived-and-levels-form-one-chain.md) | Failing outranks waived; verification levels form one ordered chain | accepted |
| [ADR-010](ADR-010-craftrail-is-the-verification-loop-for-software-factories.md) | CraftRail is the verification loop for software factories, alongside existing agent workflows | accepted |
