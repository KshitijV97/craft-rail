# Contributing

Contributions should improve a practical, agent-neutral engineering framework. Start with an issue or a concise proposal for changes that affect workflow, scope, or policy. Keep canonical content in Markdown, Mermaid, YAML, or JSON; provider-specific integrations must remain optional adapters.

## Development

Core scripts and tests support Python 3.10 or later and run with the standard library. Use Python 3.12 or later for the pinned developer quality toolchain.

```bash
python3 -m venv .venv-dev
source .venv-dev/bin/activate
python -m pip install -r requirements-dev.txt
pre-commit install
pre-commit run --all-files
```

See [Python quality checks](docs/framework/python-quality.md) for the exact lint, format, strict type, coverage, and CI commands. `python scripts/validate_docs.py --strict` also fails when warnings exist. The standard validator currently warns that OpenAPI YAML is not parsed by the dependency-free core tool.

## Pull requests

Include the problem and proposed change, affected docs/templates/tooling, exact validation results, and compatibility impact. Update examples and links when conventions change. Do not claim an agent integration works unless it was tested directly; distinguish documented compatibility from verified behavior. Keep sample content clearly illustrative, add tests for tooling changes, and explain any accepted exception to existing conventions.

By participating, contributors agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md). See [support](SUPPORT.md) for questions and [security](SECURITY.md) for vulnerability reports.
