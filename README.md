# GitHub Actions Collection

This repository provides useful GitHub Actions for repository maintenance.

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/dgaida/auto-version-action/graphs/commit-activity)
![Last commit](https://img.shields.io/github/last-commit/dgaida/auto-version-action)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/github/v/tag/dgaida/auto-version-action?label=version)](https://github.com/dgaida/auto-version-action/tags)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Code Quality](https://github.com/dgaida/auto-version-action/actions/workflows/lint.yml/badge.svg)](https://github.com/dgaida/auto-version-action/actions/workflows/lint.yml)
[![Tests](https://github.com/dgaida/auto-version-action/actions/workflows/tests.yml/badge.svg)](https://github.com/dgaida/auto-version-action/actions/workflows/tests.yml)
[![CodeQL](https://github.com/dgaida/auto-version-action/actions/workflows/codeql.yml/badge.svg)](https://github.com/dgaida/auto-version-action/actions/workflows/codeql.yml)
[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://dgaida.github.io/auto-version-action/)


## Features

This action provides two main functionalities that can be used independently or together:

### 1. Add Badges
Automatically detects repository features and adds relevant badges to your `README.md`. It checks for:  
- **Version**: From `pyproject.toml` or `package.json`.  
- **Python Version**: From `pyproject.toml`.  
- **License**: MIT license detection.  
- **Codecov**: Integration detection.  
- **GitHub Workflows**: Badges for `lint`, `tests`, and `codeql`.  
- **Code Style**: `black` or `ruff`.  
- **Documentation**: GitHub Pages or `docs/` folder.  
- **Maintenance**: Status and last commit.  

### 3. Markdown List Fixer
Ensures that Markdown list items and the lines preceding them end with two spaces. This ensures that they are correctly rendered with a line break in many Markdown viewers.

### 2. Auto Versioning
Increments the version number in `pyproject.toml` (patch level, with overflow to minor and major) and creates a corresponding Git tag.

---

## Usage

The simplest way is to use the combined action.

### Combined Action (Recommended)

Create a workflow file (e.g., `.github/workflows/auto-version-badges.yml`):

```yaml
name: Auto Version and Badges

on:
  push:
    branches: [main, master]

jobs:
  version-and-badges:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: Auto Version and Badges
        uses: dgaida/auto-version-action@main  # You can also use a specific tag like @v0.1.4
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          auto-version: true
          create-badge: true
```

### Inputs

| Input | Description | Default |
|-------|-------------|---------|
| `github-token` | GitHub token for authentication | `${{ github.token }}` |
| `auto-version` | Whether to automatically increment the version | `true` |
| `create-badge` | Whether to automatically add/update badges | `true` |
| `md-list-fix` | Whether to automatically fix Markdown lists | `true` |
| `run-on-push` | Whether to run on push events (outside of PRs) | `true` |

---

## Separate Usage

If you prefer to run them separately or on different events, you can still do so.

### Only Add Badges

```yaml
      - name: Add Badges
        uses: dgaida/auto-version-action@main
        with:
          auto-version: false
          create-badge: true
```

### Only Auto Versioning

```yaml
      - name: Auto Versioning
        uses: dgaida/auto-version-action@main
        with:
          auto-version: true
          create-badge: false
```

## How it works
The actions use Python scripts to analyze the repository state and modify files accordingly. Changes are then automatically committed and pushed back to the repository in a single step to avoid conflicts.

### Only Markdown List Fixer

```yaml
      - name: Markdown List Fixer
        uses: dgaida/auto-version-action@main
        with:
          auto-version: false
          create-badge: false
          md-list-fix: true
```
