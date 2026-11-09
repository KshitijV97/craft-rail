# Agent compatibility

The Core and Workflow are ordinary repository files and prompts. Adapters are optional pointers. **Documented compatibility is not the same as direct product testing.** No direct interactive end-to-end session has been run with Codex, Claude Code, or OpenCode as part of this repository draft.

| Agent | Shared instructions | Adapter/config | Documented behavior | Directly verified here |
|---|---|---|---|---|
| Codex | Root `AGENTS.md` | None required | Codex project guidance discovers `AGENTS.md`; nested files may scope instructions. | No |
| Claude Code | Root `AGENTS.md` | `CLAUDE.md` contains `@AGENTS.md` | Claude Code supports importing another instruction file with `@path`. | No |
| OpenCode | Root `AGENTS.md` | None required | OpenCode instruction discovery uses `AGENTS.md`; its current docs explicitly say it does not fall back to `CLAUDE.md`. | No |

The compatibility evidence is current official documentation linked below, reviewed 2026-11-08. This repository has not tested instruction loading inside each agent application. The Python tooling and Markdown links are independently testable without any agent.

| Capability | Status |
|---|---|
| Same requirements, diagrams, decisions, and workflow files usable by all three | Documented; acceptance test described, not directly run in all products |
| Provider-specific skills, slash commands, hooks, MCP, or runtime | Optional future adapters; not required or included |
| Claude import syntax | Documented via official syntax; not executed in Claude Code |
| OpenCode `CLAUDE.md` fallback | Not supported per current OpenCode docs; do not rely on it |

Official references: [Codex AGENTS.md guidance](https://developers.openai.com/codex/guides/agents-md/), [Claude Code memory and imports](https://docs.anthropic.com/en/docs/claude-code/memory), [OpenCode instructions](https://opencode.ai/docs/instructions/).

## Portability acceptance test

An adopter should clone the same repository, open it at the repository root in Codex, Claude Code, and OpenCode, and ask each to summarize the same requirement and propose a plan without editing. Confirm each identifies the same `AGENTS.md` policy and canonical spec, and that no provider configuration or migrated project knowledge is needed. Then make a small approved documentation change in each environment and compare diffs. This procedure is documented, not claimed as already passed.
