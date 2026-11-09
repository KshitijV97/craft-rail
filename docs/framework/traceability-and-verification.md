# Traceability and verification

Use a matrix that links **Requirement → Acceptance Criterion → Verification ID → evidence/location → status**. Verification may be an automated test, manual procedure, review, or operational observation. Code generation is not evidence by itself.

Statuses: `planned` means defined but not run; `implemented` means the check exists or work is present but not yet confirmed; `verified` means evidence was reviewed and the criterion passed; `blocked` means a dependency prevents checking; `waived` means an accountable human accepted the risk with rationale; `deprecated` means no longer applicable. Record date/build or commit context when useful. Structural validation catches selected ID and format errors; it cannot judge semantic correctness.
