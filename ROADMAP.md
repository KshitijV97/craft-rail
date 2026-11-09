# Roadmap

This roadmap is a small set of possible next steps, not a delivery commitment.

## Open technical debt

- [ ] **TD-001 — Separate the documentation deployment from Golden Tide Retreat.** The current `craft-rail-docs` Vercel project is under the `golden-tide-retreat` scope as a temporary setup. Move it to a CraftRail-owned Vercel account/team and project when those credentials and ownership are available. Revoke the old project's generated protection-bypass secret, explicitly decide whether production docs should be public or protected, and establish an authorized GitHub-to-Vercel deployment path. Update `zensical.toml`, the README, and deployment guidance if the canonical URL changes. Consider this resolved only after an authorized maintainer can deploy from the new scope, a production build is verified, and no CraftRail deployment depends on Golden Tide Retreat.

See the [documentation deployment guide](docs/framework/documentation-site.md) for the current setup and update commands.

1. **Improve portability evidence:** run and record the documented shared-repository acceptance procedure in Codex, Claude Code, and OpenCode.
2. **Strengthen offline validation:** consider optional YAML/OpenAPI validation while keeping core checks dependency-free.
3. **Gather maintainer feedback:** refine adoption guidance and templates after real projects try the starter structure.

Out of scope for the first version: hosted service, proprietary agent runtime, automatic code generation/approval, mandatory plugin ecosystem, or complex CLI.
