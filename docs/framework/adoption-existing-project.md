# Adopt CraftRail in an existing project

Adopt in slices:

1. Add or adapt the concise root `AGENTS.md`; preserve existing instructions and link to one authoritative source where possible.
2. Identify current owners for product requirements, architecture, contracts, and decisions. Record canonical locations in `docs/project/README.md`.
3. Add only templates and feature folders that solve a current need. Existing specs and issue trackers can remain in place.
4. Avoid copying an existing requirement into a second authoritative location. Link it or plan a reviewed migration.
5. Add the validator after deciding which baseline files are relevant; keep validation scope explicit.
6. Add `CLAUDE.md` as a minimal `@AGENTS.md` import only if Claude Code compatibility is wanted. OpenCode uses `AGENTS.md` itself.

Start with one feature and improve the conventions from experience. No migration of chat history, agent commands, or existing requirements is necessary.
