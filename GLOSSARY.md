# CraftRail

CraftRail gives software factories a deterministic verification loop: it decides, from evidence produced by real tools, whether each acceptance criterion of a piece of software is satisfied. This glossary is the framework's own vocabulary. It is separate from the starter `docs/project/glossary.md` that adopting projects fill in.

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
The kind of check, by what it exercises. `unit`, `component`, `integration`, and `acceptance` form one ordered chain, lowest first. `contract`, `architecture`, and `non-functional` are separate kinds outside the chain.
_Avoid_: Test type, test layer

**Required verification level**:
The verification level an acceptance criterion declares for the checks that may verify it. On the ordered chain, a check at or above it counts; for a separate kind, only a check of exactly that kind counts.
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
- **Waived**: a waiver covers the criterion and no accepted link's check is failing. Failing outranks waived.

_Avoid_: Test status, done, complete, partially verified, blocked

**Reason code**:
The single cause CraftRail reports for an acceptance criterion's status: `no-link`, `no-evidence`, `stale`, `skipped`, `failed`, `below-level`, or `check-not-found`.
_Avoid_: Error, failure message

**Acceptance change**:
A verification link or waiver added, changed, or removed on a branch relative to its base. It is proposed until merged and is flagged for human review.
_Avoid_: Spec change (too broad)

**Roll-up**:
A view of verification status over many acceptance criteria, such as a requirement, feature, or project. It has no status of its own.
_Avoid_: Requirement status, feature status

**Waiver**:
A named human's recorded acceptance that an acceptance criterion will go unverified, with a reason and scope.
_Avoid_: Skip, exception, override

**Evidence-gated acceptance**:
The rule that an acceptance criterion is accepted only on computed verification status, never on any party's claim that it works.
_Avoid_: Sign-off, definition of done

### Factory

**Software factory**:
A pipeline in which coding agents take work from a specification to a merged change with little human intervention.
_Avoid_: Autopilot, agent pipeline (too vague about where humans gate the work)

**Verification loop**:
The cycle in which an agent changes code, CraftRail computes each acceptance criterion's verification status from fresh evidence, and the agent acts on the reasons, until every criterion is verified or waived. Humans enter the loop only to accept links and waivers.
_Avoid_: Feedback loop, CI loop (CI runs checks; the loop judges criteria)

**Agent workflow**:
The process an agent follows to brainstorm, plan, specify, implement, and review work, supplied by tools such as Matt Pocock's skills or Compound Engineering. CraftRail runs inside an agent workflow; it does not supply one.
_Avoid_: CraftRail lifecycle, framework process

**Reference workflow**:
CraftRail's own lifecycle and workflow prompts, kept for teams that have no agent workflow. CraftRail does not depend on it.
_Avoid_: CraftRail process, the framework workflow
