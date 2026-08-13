# Auto Version Action

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/dgaida/auto-version-action/graphs/commit-activity)
![Last commit](https://img.shields.io/github/last-commit/dgaida/auto-version-action)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/github/v/tag/dgaida/auto-version-action?label=version)](https://github.com/dgaida/auto-version-action/tags)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
![Interrogate Coverage](../assets/interrogate.svg)

Willkommen zur Dokumentation der **Auto Version Action**. Diese Sammlung von GitHub Actions automatisiert die Wartung deiner Repositories.

## Hauptfunktionen

- **Auto Versioning**: Inkrementiert die Version in `pyproject.toml` oder `package.json` und erstellt Git-Tags. Die bestehende JSON-Formatierung und -Einrückung wird automatisch beibehalten.  
- **Add Badges**: Erkennt Repository-Features und fügt automatisch Badges zur `README.md` hinzu. Es unterstützt sowohl `pyproject.toml` als auch `package.json` für die Versions- und Badge-Erkennung.  
- **Markdown List Fixer**: Korrigiert Formatierungsfehler in Markdown-Listen für eine bessere Darstellung.  

## Schnellstart

```yaml
- name: Auto Version and Badges
  uses: dgaida/auto-version-action@main
  with:
    github-token: ${{ secrets.GITHUB_TOKEN }}
```
