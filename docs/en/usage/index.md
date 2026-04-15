# Usage

In this section, you will find detailed examples of how to use the various components.

## Add Badges Only

If you only want to use the automatic badge detection:

```yaml
- name: Add Badges
  uses: dgaida/auto-version-action@main
  with:
    auto-version: false
    create-badge: true
```

## Versioning Only

If you only want to use the automatic versioning:

```yaml
- name: Auto Versioning
  uses: dgaida/auto-version-action@main
  with:
    auto-version: true
    create-badge: false
```

## Fix Markdown Lists

```yaml
- name: Markdown List Fixer
  uses: dgaida/auto-version-action@main
  with:
    auto-version: false
    create-badge: false
    md-list-fix: true
```
