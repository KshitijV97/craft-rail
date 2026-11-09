# Contributing

Contributions should improve a practical, agent-neutral engineering framework. Start with an issue or a concise proposal for changes that affect workflow, scope, or policy. Keep canonical content in Markdown, Mermaid, YAML, or JSON; provider-specific integrations must remain optional adapters.

## Development

Use Python 3.10 or later; runtime tools and tests use only the standard library.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_docs.py
```

`python3 scripts/validate_docs.py --strict` also fails when warnings exist. Current warnings include the deliberate lack of OpenAPI YAML parsing.

## Pull requests

Include the problem and proposed change, affected docs/templates/tooling, exact validation results, and compatibility impact. Update examples and links when conventions change. Do not claim an agent integration works unless it was tested directly; distinguish documented compatibility from verified behavior. Keep sample content clearly illustrative, add tests for tooling changes, and explain any accepted exception to existing conventions.

By participating, contributors agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md). See [support](SUPPORT.md) for questions and [security](SECURITY.md) for vulnerability reports.
