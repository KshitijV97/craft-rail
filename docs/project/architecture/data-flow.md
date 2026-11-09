# Data flow

**Abstraction:** data movement, transformation, and storage
**Scope:** [flow]
**Last reviewed:** YYYY-MM-DD

```mermaid
flowchart LR
    Source[Source] --> Validate[Validate]
    Validate -->|accepted| Store[(Data store)]
    Validate -->|rejected| Error[Error handling]
```

Identify sensitive data, trust boundaries, retention, and failure behavior.
