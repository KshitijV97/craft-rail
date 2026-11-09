# Assumptions and decisions

Reviewed 2026-11-08. This is a first local draft; publication has not occurred.

| ID | Decision / assumption | Rationale and consequence | Owner action |
|---|---|---|---|
| D-001 | Use CraftRail and the tagline selected by the owner. | Preserve explicit project identity; name conflict remains material. | Review brand risk before public promotion, domains, or investment. |
| D-002 | Use Markdown, Mermaid, YAML, and JSON as canonical artifact formats. | Readable, diffable, interoperable; no proprietary runtime required. | None for draft. |
| D-003 | Root `AGENTS.md` is canonical; `CLAUDE.md` imports it; OpenCode reads `AGENTS.md` directly. | Prevent instruction drift and support direct OpenCode discovery. | Validate with each agent before claiming direct product verification. |
| D-004 | MIT is a provisional license draft; Apache-2.0 is the alternative to consider. | MIT is simple and permissive; Apache-2.0 includes an explicit patent grant and additional terms. | Owner/legal reviewer must confirm before release. No copyright holder is invented. |
| D-005 | Python standard library only for MVP scripts and tests. | Low setup and offline use. | Revisit only if a concrete need outweighs dependencies. |
| D-006 | Ecosystem docs reviewed 2026-11-08. | Official sources are linked in comparison and compatibility pages. | Recheck before release because external tools change. |
| D-007 | Preserve the supplied `CRAFTRAIL_CODEX_BUILD_BRIEF.md` and `CRAFTRAIL_CODEX_START_PROMPT.md` as implementation-input records; canonical ongoing requirements and conventions live in the neutral `docs/`, `templates/`, and `AGENTS.md` artifacts. | Preserve user-provided work while keeping the maintainable framework usable without Codex. | Owner may archive/remove these input records after review if desired. |

## Naming risk

The supplied brief records an existing Japanese company, Craftrail Inc. (株式会社クラフトレイル), using `https://craftrail.co.jp/` for HR/organizational services including AI-related offerings. This is a material brand-confusion risk, not a legal conclusion. The selected name remains the working identity. No trademark, domain, or GitHub handle availability is asserted. Owner review is a release blocker before public promotion or brand/domain investment.

## Release decisions

- Confirm MIT or select another license and add an accurate copyright notice if needed.
- Confirm maintainer identity and a private security contact/reporting route.
- Confirm repository namespace/URL and whether to enable template mode.
- Review name/namespace clearance and public positioning.
- Run the portability acceptance procedure with Codex, Claude Code, and OpenCode before claiming direct verification.
