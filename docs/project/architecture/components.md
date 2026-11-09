# Component view

**Abstraction:** important internal responsibilities
**Scope:** [container or module]
**Last reviewed:** YYYY-MM-DD

```mermaid
flowchart LR
    Client[Entry point] --> Service[Application service]
    Service --> Port[Domain port]
    Port --> Adapter[Infrastructure adapter]
```

Replace the generic view; explain boundaries and dependencies that matter to change.
