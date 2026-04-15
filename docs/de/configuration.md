# Konfiguration

Die Action kann über verschiedene Inputs angepasst werden.

| Input | Beschreibung | Standardwert |
|-------|-------------|---------|
| `github-token` | GitHub Token für die Authentifizierung | `${{ github.token }}` |
| `auto-version` | Ob die Version automatisch erhöht werden soll | `true` |
| `create-badge` | Ob Badges automatisch hinzugefügt/aktualisiert werden sollen | `true` |
| `md-list-fix` | Ob Markdown-Listen korrigiert werden sollen | `true` |
| `run-on-push` | Ob die Action bei Push-Events (außerhalb von PRs) laufen soll | `true` |
