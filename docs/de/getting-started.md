# Erste Schritte

Diese Anleitung hilft dir dabei, die Auto Version Action in dein Repository zu integrieren.

## Voraussetzungen

- Ein Python-Projekt mit einer `pyproject.toml`.  
- GitHub Actions sind aktiviert.  

## Einrichtung

1. Erstelle eine neue Workflow-Datei unter `.github/workflows/docs.yml`.  
2. Füge die Action zu deinen Schritten hinzu:  

```yaml
jobs:
  maintenance:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: Auto Version and Badges
        uses: dgaida/auto-version-action@main
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
```

3. Committe und pushe die Datei. Die Action wird nun bei jedem Push auf den Haupt-Branch ausgeführt.  
