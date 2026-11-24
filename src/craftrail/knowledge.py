"""Read-only discovery and retrieval for Git-backed CraftRail artifacts."""

from __future__ import annotations

import re
from collections.abc import Iterable
from dataclasses import asdict, dataclass
from pathlib import Path

IDENTIFIER_RE = re.compile(r"\b(?:BR|FR|NFR|CON|US|AC|ADR|TASK|TEST)-\d{3,}\b")
DECLARED_ID_RE = re.compile(
    r"^\s*(?:[-*]\s*)?\|?\s*`?((?:BR|FR|NFR|CON|US|AC|ADR|TASK|TEST)-\d{3,})`?(?=\s|\||$)"
)
STATUS_RE = re.compile(r"^\s*-?\s*\*\*Status:\*\*\s*([^*\n]+)", re.IGNORECASE | re.MULTILINE)
TITLE_RE = re.compile(r"^#\s+(.+?)\s*#*\s*$", re.MULTILINE)
MAX_FILE_BYTES = 1_000_000
SUPPORTED_SUFFIXES = {".md", ".markdown", ".yaml", ".yml", ".json"}
EXCLUDED_PARTS = {".git", ".venv", "node_modules", "site", "__pycache__"}
DEFAULT_SOURCE_PATHS = (
    "README.md",
    "AGENTS.md",
    "docs/project",
    "docs/framework",
    "docs/implementation",
    "specs",
)


@dataclass(frozen=True)
class Artifact:
    """A source-backed document and the metadata safely derived from it."""

    path: str
    artifact_type: str
    title: str
    status: str
    identifiers: tuple[str, ...]
    declared_identifiers: tuple[str, ...]
    content: str

    def public_record(self, *, include_content: bool = True) -> dict[str, object]:
        record = asdict(self)
        if not include_content:
            record.pop("content")
        return record


class KnowledgeError(ValueError):
    """Base class for invalid repository or artifact requests."""


class ArtifactNotFound(KnowledgeError):
    """Raised when an artifact identifier has no declaration in the project."""


class AmbiguousArtifact(KnowledgeError):
    """Raised when an identifier is declared by more than one source."""


class ProjectKnowledge:
    """Discover and query project knowledge without writing to the worktree."""

    def __init__(self, project_root: Path, source_paths: Iterable[str] = DEFAULT_SOURCE_PATHS):
        self.project_root = project_root.expanduser().resolve(strict=True)
        if not self.project_root.is_dir():
            raise KnowledgeError(f"project root is not a directory: {self.project_root}")
        self.source_paths = tuple(source_paths)

    def artifacts(self) -> list[Artifact]:
        """Read supported files under the configured canonical source paths."""
        paths: set[Path] = set()
        for configured_path in self.source_paths:
            candidate = (self.project_root / configured_path).resolve()
            self._ensure_inside_root(candidate)
            if candidate.is_file():
                if candidate.suffix.lower() in SUPPORTED_SUFFIXES:
                    paths.add(candidate)
            elif candidate.is_dir():
                for path in candidate.rglob("*"):
                    if any(part in EXCLUDED_PARTS for part in path.parts):
                        continue
                    if path.is_file() and path.suffix.lower() in SUPPORTED_SUFFIXES:
                        resolved = path.resolve()
                        self._ensure_inside_root(resolved)
                        paths.add(resolved)
        return [self._read_artifact(path) for path in sorted(paths)]

    def search(
        self,
        query: str,
        *,
        artifact_type: str | None = None,
        status: str | None = None,
        limit: int = 10,
    ) -> list[dict[str, object]]:
        """Search artifact titles and content, returning provenance with snippets."""
        normalized = query.strip().casefold()
        if not normalized:
            raise KnowledgeError("query must contain non-whitespace text")
        if not 1 <= limit <= 50:
            raise KnowledgeError("limit must be between 1 and 50")
        matches: list[tuple[int, Artifact, str]] = []
        for artifact in self.artifacts():
            if artifact_type and artifact.artifact_type != artifact_type:
                continue
            if status:
                requested_status = status.casefold()
                artifact_status = artifact.status.casefold()
                status_token = artifact_status.split(maxsplit=1)[0]
                if requested_status not in {artifact_status, status_token}:
                    continue
            haystack = f"{artifact.title}\n{artifact.content}".casefold()
            score = haystack.count(normalized)
            if score:
                excerpt = self._excerpt(artifact.content, normalized)
                matches.append((score, artifact, excerpt))
        matches.sort(key=lambda item: (-item[0], item[1].path))
        return [
            {
                **artifact.public_record(include_content=False),
                "score": score,
                "excerpt": excerpt,
            }
            for score, artifact, excerpt in matches[:limit]
        ]

    def get_requirement(self, identifier: str) -> dict[str, object]:
        """Retrieve a requirement only when it is declared in a source artifact."""
        if not re.fullmatch(r"(?:BR|FR|NFR|CON)-\d{3,}", identifier):
            raise KnowledgeError("identifier must be a BR, FR, NFR, or CON ID")
        artifact = self._get_declared_artifact(identifier)
        record = artifact.public_record()
        declaration = self._declaration_line(artifact.content, identifier)
        if declaration is not None:
            record["content"] = declaration
            row_status = self._table_row_status(declaration)
            if row_status:
                record["status"] = row_status
        return record

    def get_adr(self, identifier: str) -> dict[str, object]:
        """Retrieve an ADR by stable ID or its numbered ADR filename."""
        if not re.fullmatch(r"ADR-\d{3,}", identifier):
            raise KnowledgeError("identifier must use the ADR-NNN format")
        records = [
            artifact
            for artifact in self.artifacts()
            if identifier in artifact.declared_identifiers
            or Path(artifact.path).name.upper().startswith(identifier + "-")
        ]
        return self._single_record(identifier, records)

    def get_feature_context(self, feature_id: str) -> dict[str, object]:
        """Assemble the feature's own records and declared requirement records."""
        if not re.fullmatch(r"\d{3,}", feature_id):
            raise KnowledgeError("feature_id must contain at least three digits")
        artifacts = self.artifacts()
        feature_records = [
            artifact for artifact in artifacts if artifact.path.startswith(f"specs/{feature_id}-")
        ]
        if not feature_records:
            raise ArtifactNotFound(f"feature not found: {feature_id}")
        related_ids = sorted(
            {
                identifier
                for artifact in feature_records
                for identifier in artifact.identifiers
                if identifier.startswith(("BR-", "FR-", "NFR-", "CON-"))
            }
        )
        related: list[dict[str, object]] = []
        for identifier in related_ids:
            try:
                related.append(self._get_declared(identifier))
            except ArtifactNotFound:
                continue
        return {
            "feature_id": feature_id,
            "artifacts": [item.public_record() for item in feature_records],
            "related_requirements": related,
        }

    def validate_artifacts(self) -> dict[str, object]:
        """Report basic source and identifier issues without claiming semantic validation."""
        artifacts = self.artifacts()
        declarations: dict[str, list[str]] = {}
        for artifact in artifacts:
            for identifier in artifact.declared_identifiers:
                declarations.setdefault(identifier, []).append(artifact.path)
        duplicates = {
            identifier: paths for identifier, paths in declarations.items() if len(paths) > 1
        }
        return {
            "artifact_count": len(artifacts),
            "duplicate_declarations": duplicates,
            "validation_scope": "supported source files and duplicate declared IDs only",
            "semantic_validation": False,
            "sources": [artifact.path for artifact in artifacts],
        }

    def _get_declared(self, identifier: str) -> dict[str, object]:
        return self._get_declared_artifact(identifier).public_record()

    def _get_declared_artifact(self, identifier: str) -> Artifact:
        records = [
            artifact for artifact in self.artifacts() if identifier in artifact.declared_identifiers
        ]
        if not records:
            raise ArtifactNotFound(f"artifact not found: {identifier}")
        if len(records) > 1:
            paths = ", ".join(record.path for record in records)
            raise AmbiguousArtifact(f"artifact {identifier} is declared in multiple files: {paths}")
        return records[0]

    @staticmethod
    def _declaration_line(content: str, identifier: str) -> str | None:
        for line in content.splitlines():
            match = DECLARED_ID_RE.match(line)
            if match and match.group(1) == identifier:
                return line.strip()
        return None

    @staticmethod
    def _table_row_status(line: str) -> str | None:
        if not line.lstrip().startswith("|"):
            return None
        cells = [cell.strip().strip("`") for cell in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            return None
        status = cells[-1].strip().lower()
        if status in {
            "draft",
            "proposed",
            "approved",
            "accepted",
            "deprecated",
            "superseded",
            "verified",
        }:
            return status
        return None

    @staticmethod
    def _single_record(identifier: str, records: list[Artifact]) -> dict[str, object]:
        if not records:
            raise ArtifactNotFound(f"artifact not found: {identifier}")
        if len(records) > 1:
            paths = ", ".join(record.path for record in records)
            raise AmbiguousArtifact(f"artifact {identifier} is declared in multiple files: {paths}")
        return records[0].public_record()

    def _read_artifact(self, path: Path) -> Artifact:
        self._ensure_inside_root(path.resolve())
        if path.stat().st_size > MAX_FILE_BYTES:
            raise KnowledgeError(
                f"source exceeds the {MAX_FILE_BYTES}-byte limit: {self._relative(path)}"
            )
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            raise KnowledgeError(f"source is not valid UTF-8: {self._relative(path)}") from exc
        relative_path = self._relative(path)
        declarations = tuple(
            sorted(
                {
                    match.group(1)
                    for line in content.splitlines()
                    if (match := DECLARED_ID_RE.match(line)) is not None
                }
            )
        )
        identifiers = tuple(sorted(set(IDENTIFIER_RE.findall(content))))
        title_match = TITLE_RE.search(content)
        title = title_match.group(1).strip() if title_match else path.stem.replace("-", " ")
        status_match = STATUS_RE.search(content)
        status = status_match.group(1).strip().strip("`").lower() if status_match else "unspecified"
        return Artifact(
            path=relative_path,
            artifact_type=self._artifact_type(relative_path),
            title=title,
            status=status,
            identifiers=identifiers,
            declared_identifiers=declarations,
            content=content,
        )

    @staticmethod
    def _artifact_type(relative_path: str) -> str:
        path = Path(relative_path)
        parts = path.parts
        if len(parts) >= 3 and parts[0] == "specs":
            return f"feature_{path.stem}"
        if "decisions" in parts or path.name.upper().startswith("ADR-"):
            return "adr"
        if "requirements" in parts:
            if "functional" in path.stem:
                return "functional_requirements"
            if "non-functional" in path.stem:
                return "non_functional_requirements"
            return "requirements"
        if "architecture" in parts:
            return "architecture"
        if "contracts" in parts:
            return "contract"
        if "framework" in parts:
            return "workflow"
        return "project_document"

    def _relative(self, path: Path) -> str:
        self._ensure_inside_root(path.resolve())
        return path.resolve().relative_to(self.project_root).as_posix()

    def _ensure_inside_root(self, path: Path) -> None:
        try:
            path.relative_to(self.project_root)
        except ValueError as exc:
            raise KnowledgeError(
                f"source resolves outside configured project root: {path}"
            ) from exc

    @staticmethod
    def _excerpt(content: str, query: str, width: int = 280) -> str:
        lowered = content.casefold()
        position = lowered.find(query)
        if position < 0:
            return content[:width].strip()
        start = max(position - width // 3, 0)
        end = min(position + width * 2 // 3, len(content))
        excerpt = content[start:end].strip()
        return ("…" if start else "") + excerpt + ("…" if end < len(content) else "")
