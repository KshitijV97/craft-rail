# Requirements writing guide

Write one observable obligation per requirement when practical. State the actor, trigger, behavior, and relevant conditions. Prefer required outcomes over implementation preferences. Include rationale/source and verification references where they improve understanding.

Good requirements are unambiguous, bounded, and testable. If a quality is evaluated by review rather than automation, say how. Distinguish BR, FR, NFR, CON, assumptions, and ACs as defined in [concepts](concepts.md). Use stable IDs and do not recycle IDs after removal; mark a requirement deprecated or superseded. Keep business rules explicit and avoid smuggling them into implementation notes.

Acceptance criteria should describe observable outcomes. Given/When/Then is useful for behavior, but not mandatory for every criterion. Negative paths, permissions, boundaries, and failure behavior deserve consideration. No validator can establish that the underlying requirement is correct or complete.
