# Architecture documentation guide

Document boundaries and relationships at the level needed for a decision or change. A layered set of views is easier to maintain than one giant diagram:

- **System context:** users, external systems, and system boundary.
- **Container:** deployable/runtime units and data stores.
- **Component:** important internal modules and responsibilities.
- **Sequence:** time-ordered interactions.
- **Data flow:** data movement, transformation, and storage.
- **State:** lifecycle and transitions.
- **Deployment:** infrastructure and runtime topology when useful.

C4 concepts are useful, not mandatory. Every diagram should name its scope and abstraction level, include a last-reviewed date, use consistent component names, and explain what question it answers. Include security/trust boundaries where relevant. Keep editable source in Git; a screenshot is not a source of truth. Detailed diagrams.net work should include its `.drawio` source. Mermaid preview may use GitHub rendering or a local editor extension; no renderer is required.
