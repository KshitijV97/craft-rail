# CraftRail overview

CraftRail is a repository-native standard for capturing engineering intent and keeping it connected to implementation and verification. It is a starter framework, not an agent runtime or requirements-management platform.

## Architecture

CraftRail has three conceptual layers:

1. **Core:** product and engineering requirements, specifications, architecture, contracts, decisions, traceability, and validation. These stay in agent-neutral Markdown, Mermaid, YAML, and JSON.
2. **Workflow:** Discover → Specify → Clarify → Plan → Tasks → Analyze → Implement → Verify → Converge. Gates define the engineering process independently of any model or product.
3. **Adapters:** small files/configuration that help a tool discover shared guidance. They may point to Core and Workflow but cannot become a second source of truth.

The framework owns the engineering process. The coding agent is replaceable. The canonical project instructions are in root `AGENTS.md`; `CLAUDE.md` is only an import adapter. OpenCode consumes `AGENTS.md` directly. Provider-specific features are optional and outside the core contract.

## What it offers

- A progressive repository layout for project and feature artifacts.
- Reusable templates, realistic examples, and stable IDs.
- Architecture views and ADRs that preserve important boundaries and reasoning.
- Traceability from requirement to acceptance criterion to verification evidence.
- A standard-library feature initializer and structural documentation validator.

## Limits

CraftRail checks document structure and selected syntax; it cannot judge whether a requirement is valuable, safe, complete, or true. It does not generate code from specs, approve changes, render Mermaid, validate YAML without an optional parser, or guarantee an agent follows instructions. Human review and executable tests remain necessary.
