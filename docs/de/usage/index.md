# Verwendung

In diesem Abschnitt findest du detaillierte Beispiele für die Verwendung der verschiedenen Komponenten.

## Nur Badges hinzufügen

Wenn du nur die automatische Badge-Erkennung nutzen möchtest:

```yaml
- name: Add Badges
  uses: dgaida/auto-version-action@main
  with:
    auto-version: false
    create-badge: true
```

## Nur Versionierung

Wenn du nur die automatische Versionierung nutzen möchtest:

```yaml
- name: Auto Versioning
  uses: dgaida/auto-version-action@main
  with:
    auto-version: true
    create-badge: false
```

## Markdown-Listen korrigieren

```yaml
- name: Markdown List Fixer
  uses: dgaida/auto-version-action@main
  with:
    auto-version: false
    create-badge: false
    md-list-fix: true
```
