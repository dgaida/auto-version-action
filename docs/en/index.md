# Auto Version Action

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/dgaida/auto-version-action/graphs/commit-activity)
![Last commit](https://img.shields.io/github/last-commit/dgaida/auto-version-action)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/github/v/tag/dgaida/auto-version-action?label=version)](https://github.com/dgaida/auto-version-action/tags)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
![Interrogate Coverage](../assets/interrogate.svg)

Welcome to the **Auto Version Action** documentation. This collection of GitHub Actions automates your repository maintenance.

## Key Features

- **Auto Versioning**: Increments the version in `pyproject.toml` and creates Git tags.  
- **Add Badges**: Detects repository features and automatically adds badges to `README.md`.  
- **Markdown List Fixer**: Fixes formatting errors in Markdown lists for better rendering.  

## Quick Start

```yaml
- name: Auto Version and Badges
  uses: dgaida/auto-version-action@main
  with:
    github-token: ${{ secrets.GITHUB_TOKEN }}
```
