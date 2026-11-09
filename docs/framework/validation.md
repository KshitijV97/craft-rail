# Documentation validation

Run from any working directory:

```bash
python3 scripts/validate_docs.py
python3 scripts/validate_docs.py --strict
```

The script resolves its repository root from its own file path. It uses only the Python standard library and makes no network requests.

## Checks

- Required root files and baseline directories exist.
- Markdown fences balance; recognized Mermaid fences and `.mmd` files are non-empty and begin with a known diagram declaration.
- Common double-brace tokens, angle-bracket placeholder markers, and explicit TODO labels do not appear in non-template/non-example Markdown.
- Declared requirement/task/verification IDs with supported prefixes have at least three digits and are not duplicated within the same Markdown document's declarations.
- Numbered feature directories contain `spec.md`, `plan.md`, `tasks.md`, and `verification.md`; the spec has a supported status.
- Inline relative Markdown links resolve to an existing local path.
- `.json` files parse as JSON.

The validator reports errors and warnings separately. It does not assess whether requirements are correct, complete, secure, or semantically consistent. It does not render Mermaid; Markdown links using reference definitions and fragment anchor existence are not checked. JSON Schema files are checked for JSON syntax, not against the JSON Schema meta-schema. OpenAPI YAML is not parsed because there is no YAML dependency; its warning is expected.

`--strict` returns a failing exit status if either an error or warning is reported. Therefore, with the current intentionally unvalidated OpenAPI YAML warning, ordinary validation passes and strict validation returns status 1 until YAML validation is added or the warning is otherwise resolved.
