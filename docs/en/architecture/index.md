# Architecture

This document describes the structure and data flow of the Auto Version Action.

## System Overview

The action consists of three main components executed sequentially.

```mermaid
graph TD
    A[GitHub Event] --> B{Auto Version Action}
    B --> C[increment_version.py]
    B --> D[fix_md_lists.py]
    B --> E[add_badges.py]
    C --> F[pyproject.toml updated]
    D --> G[Markdown files fixed]
    E --> H[README.md updated with badges]
    F & G & H --> I[Git Commit & Push]
    I --> J[Git Tag creation]
```

## Data Flow

The data flow focuses on analyzing the repository status and subsequently modifying metadata and documentation.

```mermaid
sequenceDiagram
    participant GH as GitHub Workflow
    participant IV as increment_version.py
    participant FB as fix_md_lists.py
    participant AB as add_badges.py
    participant Git as Git Commands

    GH->>IV: Start Versioning
    IV->>IV: Read pyproject.toml
    IV-->>GH: Version incremented
    GH->>FB: Start Markdown Fixer
    FB->>FB: Scan .md files
    FB-->>GH: Lists fixed
    GH->>AB: Start Badge Detection
    AB->>AB: Analyze Repository
    AB-->>GH: README updated
    GH->>Git: Commit, Push & Tag
```
