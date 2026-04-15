# Architektur

Dieses Dokument beschreibt den Aufbau und den Datenfluss der Auto Version Action.

## Systemübersicht

Die Action besteht aus drei Hauptkomponenten, die nacheinander ausgeführt werden.

```mermaid
graph TD
    A[GitHub Event] --> B{Auto Version Action}
    B --> C[increment_version.py]
    B --> D[fix_md_lists.py]
    B --> E[add_badges.py]
    C --> F[pyproject.toml aktualisiert]
    D --> G[Markdown-Dateien korrigiert]
    E --> H[README.md mit Badges aktualisiert]
    F & G & H --> I[Git Commit & Push]
    I --> J[Git Tag Erstellung]
```

## Datenfluss

Der Datenfluss konzentriert sich auf die Analyse des Repository-Status und die anschließende Modifikation von Metadaten und Dokumentation.

```mermaid
sequenceDiagram
    participant GH as GitHub Workflow
    participant IV as increment_version.py
    participant FB as fix_md_lists.py
    participant AB as add_badges.py
    participant Git as Git Commands

    GH->>IV: Starte Versionierung
    IV->>IV: Lese pyproject.toml
    IV-->>GH: Version erhöht
    GH->>FB: Starte Markdown Fixer
    FB->>FB: Scanne .md Dateien
    FB-->>GH: Listen korrigiert
    GH->>AB: Starte Badge-Erkennung
    AB->>AB: Analysiere Repository
    AB-->>GH: README aktualisiert
    GH->>Git: Commit, Push & Tag
```
