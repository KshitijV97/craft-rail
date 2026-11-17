# CraftRail

CraftRail decides, from evidence produced by real tools, whether each acceptance criterion of a piece of software is satisfied. This glossary is the framework's own vocabulary. It is separate from the starter `docs/project/glossary.md` that adopting projects fill in.

## Language

### Intent

**Requirement**:
A stated obligation the software must meet, identified by a stable ID (`BR`, `FR`, `NFR`, `CON`).
_Avoid_: Ticket, story (a user story is a framing device, not the obligation)

**Acceptance criterion**:
One observable outcome that decides whether part of a requirement is met. It is the unit of verification: atomic (one outcome) and independently checkable (it can pass or fail on its own). Non-functional requirements are verified through acceptance criteria too.
_Avoid_: Requirement Slice, slice, test case

**Feature**:
The unit of delivery that groups the requirements and acceptance criteria being changed together.
_Avoid_: Slice, vertical slice (as a stored concept), epic

### Verification

**Check**:
Anything a tool executes or a person performs that produces a pass, fail, or skip result: a test, a contract validation, an architecture rule, a scan, a recorded manual procedure.
_Avoid_: Test (too narrow), verification (ambiguous with the status)

**Verification level**:
The kind of check, by what it exercises: `unit`, `component`, `integration`, `contract`, `architecture`, `acceptance`, or `non-functional`.
_Avoid_: Test type, test layer

**Required verification level**:
The minimum verification level an acceptance criterion declares for the checks that may verify it. A check below it does not count, however well it passes.
_Avoid_: Test strategy, coverage target

**Verification link**:
A human-accepted statement that a specific check counts as evidence for a specific acceptance criterion. An agent may propose one; it counts only once accepted.
_Avoid_: Mapping, test-to-requirement relationship, traceability row

**Proposed link**:
A verification link that has been written down but not yet accepted. It does not count toward verification status.
_Avoid_: Draft link, pending link (pending is a status)

**Evidence**:
The recorded result of a check run, tied to the commit and environment it ran against. A skipped result is not evidence.
_Avoid_: Proof, test output (one input to evidence, not evidence itself)

**Fresh evidence**:
Evidence produced at the commit being judged. Evidence from any other commit is **stale** and does not count.
_Avoid_: Recent, up to date

**Verification status**:
The state of an acceptance criterion, computed from its accepted verification links, their evidence, and any waiver. It is never typed in by hand. Its values are:

- **Unlinked**: no accepted verification link and no waiver.
- **Pending**: accepted links exist, but at least one has no fresh evidence.
- **Failing**: at least one accepted link's check failed at the current commit. A check that fails on any run is failing, even if a retry passes.
- **Verified**: every accepted link's check passed at the current commit.
- **Waived**: a waiver covers the criterion.

_Avoid_: Test status, done, complete, partially verified, blocked

**Roll-up**:
A view of verification status over many acceptance criteria, such as a requirement, feature, or project. It has no status of its own.
_Avoid_: Requirement status, feature status

**Waiver**:
A named human's recorded acceptance that an acceptance criterion will go unverified, with a reason and scope.
_Avoid_: Skip, exception, override

**Evidence-gated acceptance**:
The rule that an acceptance criterion is accepted only on computed verification status, never on any party's claim that it works.
_Avoid_: Sign-off, definition of done
