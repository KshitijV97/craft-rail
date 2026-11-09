# Feature lifecycle

The standard path is **Discover → Specify → Clarify → Plan → Tasks → Analyze → Implement → Verify → Converge**. These are quality gates, not mandatory meetings. A small, low-risk change may combine phases; high-impact work should use the full path.

| Phase | Output / gate |
|---|---|
| Discover | Current behavior, user problem, stakeholders, constraints, and sources are understood. |
| Specify | Scope, goals, requirements, rules, edge cases, and acceptance criteria are drafted. |
| Clarify | Material ambiguity, contradictions, missing cases, and open questions are resolved or explicitly owned. |
| Plan | Components, interfaces, data, security, operations, alternatives, rollout, and tests are addressed where relevant. |
| Tasks | Dependency-ordered, reviewable slices reference requirements and verification. |
| Analyze | Cross-check spec, plan, tasks, architecture, and contracts; repair gaps at their source. |
| Implement | Make incremental changes within approved scope; ask for an approved spec change when scope shifts. |
| Verify | Execute automated/manual checks and attach evidence to acceptance criteria. |
| Converge | Update docs to shipped behavior, record deviations, deferred work, and superseded decisions. |

## Change control

If implementation exposes a scope change, pause affected work, propose a spec revision, explain impacts, and obtain the project's required approval. Preserve accepted history; mark superseded requirements and use a new ADR for material decision changes. Record deviations rather than rewriting intent after the fact. Deferred requirements retain IDs and status. Emergency fixes may use a shortened path, then document rationale, risk, and follow-up verification during convergence. Deprecation is explicit and linked to replacement guidance where applicable.
