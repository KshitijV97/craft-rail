# Technical implementation of CraftRail

This section documents how the CraftRail repository itself is organized, built, checked, and released. It is maintainer and contributor documentation; project adopters can use CraftRail without installing this repository's development toolchain or deploying its website.

## Implementation map

| Area | Implementation in this repository | Guide |
|---|---|---|
| Core, Workflow, and Adapters | Agent-neutral project content, lifecycle, and minimal instruction adapters | [Design rationale](../framework/design-rationale.md) |
| Repository layout | Framework docs, starter project docs, specs, templates, scripts, and tests | [Repository structure](../framework/repository-structure.md) |
| Python tools | Feature initializer and structural documentation validator using the standard library | [Python quality checks](../framework/python-quality.md) and [validator boundaries](../framework/validation.md) |
| Automated checks | Ruff, Mypy strict mode, pytest coverage, pre-commit, Actionlint, GitHub Actions | [Python quality checks](../framework/python-quality.md) |
| Marketing and documentation website | The root page introduces CraftRail; separate sections hold adoption and implementation docs. Zensical builds canonical Markdown to static pages and Vercel serves `site/` | [Documentation site](../framework/documentation-site.md) |
| Agent neutrality | `AGENTS.md` is canonical; `CLAUDE.md` imports it; OpenCode reads `AGENTS.md` directly | [Agent compatibility](../framework/agent-compatibility.md) |

## Build and test the repository

Install development checks in an isolated environment:

```bash
python3 -m venv .venv-dev
source .venv-dev/bin/activate
python -m pip install -r requirements-dev.txt
pre-commit run --all-files
```

The checks type-check `scripts/` and `tests/`, run 26 unit tests, require at least 90% combined line/branch coverage for the scripts, and validate supported workflow and document structures. GitHub Actions repeats them on pushes and pull requests. See the complete [quality and release guide](../framework/python-quality.md).

## Maintain the documentation site

The marketing page and detailed guides are presentation layers over `docs/`, not separate sources of truth. Edit Markdown, update the explicit navigation in `zensical.toml` when adding a page, run a strict site build, and deploy to Vercel. GitHub Actions builds the site but does not currently publish it; publication uses the authenticated Vercel CLI. The [deployment guide](../framework/documentation-site.md) explains the architecture and the current separation work tracked as `TD-001` in the repository-root `ROADMAP.md`.

## Contribute and release

Contribution conventions live in the repository-root `CONTRIBUTING.md`. The release workflow validates semantic version tags, reruns quality checks, and creates GitHub releases with generated notes after an annotated tag is pushed. Review the release process and owner decisions in the [quality and release guide](../framework/python-quality.md) before creating a release.
